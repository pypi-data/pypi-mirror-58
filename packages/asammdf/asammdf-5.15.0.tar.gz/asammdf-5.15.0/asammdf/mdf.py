# -*- coding: utf-8 -*-
""" common MDF file format module """

import csv
from datetime import datetime, timezone
from functools import reduce
import logging
import xml.etree.ElementTree as ET
from collections import OrderedDict, defaultdict
from copy import deepcopy
from struct import unpack
from shutil import copy
from pathlib import Path
from time import perf_counter

import canmatrix
import numpy as np
from numpy.core.defchararray import encode, decode
import pandas as pd

from .blocks.conversion_utils import from_dict
from .blocks.mdf_v2 import MDF2
from .blocks.mdf_v3 import MDF3
from .blocks.mdf_v4 import MDF4
from .signal import Signal
from .blocks.utils import (
    CHANNEL_COUNT,
    MERGE,
    MdfException,
    matlab_compatible,
    validate_version_argument,
    MDF2_VERSIONS,
    MDF3_VERSIONS,
    MDF4_VERSIONS,
    SUPPORTED_VERSIONS,
    randomized_string,
    is_file_like,
    count_channel_groups,
    UINT16_u,
    UINT64_u,
    UniqueDB,
    components,
    downcast,
    master_using_raster,
    extract_can_signal,
    extract_mux,
    csv_int2hex,
    csv_bytearray2hex,
    load_can_database,
)

from .blocks.v2_v3_blocks import HeaderBlock as HeaderV3
from .blocks.v2_v3_blocks import ChannelConversion as ChannelConversionV3
from .blocks.v2_v3_blocks import ChannelExtension
from .blocks.v4_blocks import SourceInformation
from .blocks.v4_blocks import ChannelConversion as ChannelConversionV4
from .blocks.v4_blocks import HeaderBlock as HeaderV4
from .blocks.v4_blocks import ChannelArrayBlock, EventBlock
from .blocks import v4_constants as v4c
from .blocks import v2_v3_constants as v23c


logger = logging.getLogger("asammdf")
LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo


__all__ = ["MDF", "SUPPORTED_VERSIONS"]


class MDF(object):
    """Unified access to MDF v3 and v4 files. Underlying _mdf's attributes and
    methods are linked to the `MDF` object via *setattr*. This is done to expose
    them to the user code and for performance considerations.

    Parameters
    ----------
    name : string | BytesIO
        mdf file name (if provided it must be a real file name) or
        file-like object

    version : string
        mdf file version from ('2.00', '2.10', '2.14', '3.00', '3.10', '3.20',
        '3.30', '4.00', '4.10', '4.11', '4.20'); default '4.10'


    callback (\*\*kwargs) : function
        keyword only argument: function to call to update the progress; the
        function must accept two arguments (the current progress and maximum
        progress value)
    use_display_names (\*\*kwargs) : bool
        keyword only argument: for MDF4 files parse the XML channel comment to
        search for the display name; XML parsing is quite expensive so setting
        this to *False* can decrease the loading times very much; default
        *False*
    remove_source_from_channel_names (\*\*kwargs) : bool
        remove source from channel names ("Speed\XCP3" -> "Speed")
    copy_on_get (\*\*kwargs) : bool
        copy arrays in the get method; default *True*

    """

    _terminate = False

    def __init__(self, name=None, version="4.10", **kwargs):
        if name:
            if is_file_like(name):
                file_stream = name
            else:
                name = Path(name)
                if name.is_file():
                    file_stream = open(name, "rb")
                else:
                    raise MdfException(f'File "{name}" does not exist')
            file_stream.seek(0)
            magic_header = file_stream.read(8)
            if magic_header != b"MDF     " and magic_header != b"UnFinMF ":
                raise MdfException(f'"{name}" is not a valid ASAM MDF file')
            file_stream.seek(8)
            version = file_stream.read(4).decode("ascii").strip(" \0")
            if not version:
                file_stream.read(16)
                version = unpack("<H", file_stream.read(2))[0]
                version = str(version)
                version = f"{version[0]}.{version[1:]}"
            if version in MDF3_VERSIONS:
                self._mdf = MDF3(name, **kwargs)
            elif version in MDF4_VERSIONS:
                self._mdf = MDF4(name, **kwargs)
            elif version in MDF2_VERSIONS:
                self._mdf = MDF2(name, **kwargs)
            else:
                message = f'"{name}" is not a supported MDF file; "{version}" file version was found'
                raise MdfException(message)

        else:
            version = validate_version_argument(version)
            if version in MDF2_VERSIONS:
                self._mdf = MDF3(version=version, **kwargs)
            elif version in MDF3_VERSIONS:
                self._mdf = MDF3(version=version, **kwargs)
            elif version in MDF4_VERSIONS:
                self._mdf = MDF4(version=version, **kwargs)
            else:
                message = (
                    f'"{version}" is not a supported MDF file version; '
                    f"Supported versions are {SUPPORTED_VERSIONS}"
                )
                raise MdfException(message)

        self._initial_attributes = set(dir(self))
        self._link_attributes()

    def _link_attributes(self):
        # link underlying _mdf attributes and methods to the new MDF object
        for attr in set(dir(self._mdf)) - self._initial_attributes:
            setattr(self, attr, getattr(self._mdf, attr))

        for attr in set(dir(self)) - set(dir(self._mdf)):
            if not attr.startswith("_"):
                setattr(self._mdf, attr, getattr(self, attr))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __del__(self):
        self.close()

    def __lt__(self, other):
        if self.header.start_time < other.header.start_time:
            return True
        elif self.header.start_time > other.header.start_time:
            return False
        else:

            t_min = []
            for i, group in enumerate(self.groups):
                cycles_nr = group.channel_group.cycles_nr
                if cycles_nr and i in self.masters_db:
                    master_min = self.get_master(i, record_offset=0, record_count=1)
                    if len(master_min):
                        t_min.append(master_min[0])

            other_t_min = []
            for i, group in enumerate(other.groups):
                cycles_nr = group.channel_group.cycles_nr
                if cycles_nr and i in other.masters_db:
                    master_min = other.get_master(i, record_offset=0, record_count=1)
                    if len(master_min):
                        other_t_min.append(master_min[0])

            if not t_min or not other_t_min:
                return True
            else:
                return min(t_min) < min(other_t_min)

    def _transfer_events(self, other):
        self._link_attributes()

        def get_scopes(event, events):
            if event.scopes:
                return event.scopes
            else:
                if event.parent is not None:
                    return get_scopes(events[event.parent], events)
                elif event.range_start is not None:
                    return get_scopes(events[event.range_start], events)
                else:
                    return event.scopes

        if other.version >= "4.00":
            for event in other.events:
                if self.version >= "4.00":
                    new_event = deepcopy(event)
                    event_valid = True
                    for i, ref in enumerate(new_event.scopes):
                        try:
                            dg_cntr, ch_cntr = ref
                            try:
                                (self.groups[dg_cntr].channels[ch_cntr])
                            except:
                                event_valid = False
                        except TypeError:
                            dg_cntr = ref
                            try:
                                (self.groups[dg_cntr].channel_group)
                            except:
                                event_valid = False
                    # ignore attachments for now
                    for i in range(new_event.attachment_nr):
                        key = f"attachment_{i}_addr"
                        event[key] = 0
                    if event_valid:
                        self.events.append(new_event)
                else:
                    ev_type = event.event_type
                    ev_range = event.range_type
                    ev_base = event.sync_base
                    ev_factor = event.sync_factor

                    timestamp = ev_base * ev_factor

                    try:
                        comment = ET.fromstring(
                            event.comment.replace(
                                ' xmlns="http://www.asam.net/mdf/v4"', ""
                            )
                        )
                        pre = comment.find(".//pre_trigger_interval")
                        if pre is not None:
                            pre = float(pre.text)
                        else:
                            pre = 0.0
                        post = comment.find(".//post_trigger_interval")
                        if post is not None:
                            post = float(post.text)
                        else:
                            post = 0.0
                        comment = comment.find(".//TX")
                        if comment is not None:
                            comment = comment.text
                        else:
                            comment = ""

                    except:
                        pre = 0.0
                        post = 0.0
                        comment = event.comment

                    if comment:
                        comment += ": "

                    if ev_range == v4c.EVENT_RANGE_TYPE_BEGINNING:
                        comment += "Begin of "
                    elif ev_range == v4c.EVENT_RANGE_TYPE_END:
                        comment += "End of "
                    else:
                        comment += "Single point "

                    if ev_type == v4c.EVENT_TYPE_RECORDING:
                        comment += "recording"
                    elif ev_type == v4c.EVENT_TYPE_RECORDING_INTERRUPT:
                        comment += "recording interrupt"
                    elif ev_type == v4c.EVENT_TYPE_ACQUISITION_INTERRUPT:
                        comment += "acquisition interrupt"
                    elif ev_type == v4c.EVENT_TYPE_START_RECORDING_TRIGGER:
                        comment += "measurement start trigger"
                    elif ev_type == v4c.EVENT_TYPE_STOP_RECORDING_TRIGGER:
                        comment += "measurement stop trigger"
                    elif ev_type == v4c.EVENT_TYPE_TRIGGER:
                        comment += "trigger"
                    else:
                        comment += "marker"

                    scopes = get_scopes(event, other.events)
                    if scopes:
                        for i, ref in enumerate(scopes):
                            event_valid = True
                            try:
                                dg_cntr, ch_cntr = ref
                                try:
                                    (self.groups[dg_cntr])
                                except:
                                    event_valid = False
                            except TypeError:
                                dg_cntr = ref
                                try:
                                    (self.groups[dg_cntr])
                                except:
                                    event_valid = False
                            if event_valid:

                                self.add_trigger(
                                    dg_cntr,
                                    timestamp,
                                    pre_time=pre,
                                    post_time=post,
                                    comment=comment,
                                )
                    else:
                        for i, _ in enumerate(self.groups):
                            self.add_trigger(
                                i,
                                timestamp,
                                pre_time=pre,
                                post_time=post,
                                comment=comment,
                            )

        else:
            for trigger_info in other.iter_get_triggers():
                comment = trigger_info["comment"]
                timestamp = trigger_info["time"]
                group = trigger_info["group"]

                if self.version < "4.00":
                    self.add_trigger(
                        group,
                        timestamp,
                        pre_time=trigger_info["pre_time"],
                        post_time=trigger_info["post_time"],
                        comment=comment,
                    )
                else:
                    if timestamp:
                        ev_type = v4c.EVENT_TYPE_TRIGGER
                    else:
                        ev_type = v4c.EVENT_TYPE_START_RECORDING_TRIGGER
                    event = EventBlock(
                        event_type=ev_type,
                        sync_base=int(timestamp * 10 ** 9),
                        sync_factor=10 ** -9,
                        scope_0_addr=0,
                    )
                    event.comment = comment
                    event.scopes.append(group)
                    self.events.append(event)

    def _included_channels(self, index, skip_master=True):
        """ get the minimum channels needed to extract all information from the
        channel group (for example keep onl the structure channel and exclude the
        strucutre fields channels)

        Parameters
        ----------
        index : int
            channel group index

        Returns
        -------
        included_channels : set
            set of excluded channels

        """
        self._link_attributes()

        group = self.groups[index]

        included_channels = set(range(len(group.channels)))
        master_index = self.masters_db.get(index, None)
        if master_index is not None and skip_master:
            included_channels.remove(master_index)

        channels = group.channels

        if self.version in MDF2_VERSIONS + MDF3_VERSIONS:
            for dep in group.channel_dependencies:
                if dep is None:
                    continue
                for gp_nr, ch_nr in dep.referenced_channels:
                    if gp_nr == index:
                        included_channels.remove(ch_nr)
        else:
            if group.CAN_logging:
                found = True
                where = (
                    self.whereis("CAN_DataFrame")
                    + self.whereis("CAN_ErrorFrame")
                    + self.whereis("CAN_RemoteFrame")
                )

                for dg_cntr, ch_cntr in where:
                    if dg_cntr == index:
                        break
                else:
                    found = False
                    #                    raise MdfException(
                    #                        f"CAN_DataFrame or CAN_ErrorFrame not found in group {index}"
                    #                    )
                    group.CAN_logging = False

                if found:
                    channel = channels[ch_cntr]

                    frame_bytes = range(
                        channel.byte_offset,
                        channel.byte_offset + channel.bit_count // 8,
                    )

                    for i, channel in enumerate(channels):
                        if channel.byte_offset in frame_bytes:
                            included_channels.remove(i)

                    included_channels.add(ch_cntr)

                    if group.CAN_database:
                        dbc_addr = group.dbc_addr
                        message_id = group.message_id
                        for m_ in message_id:
                            try:
                                can_msg = self._dbc_cache[dbc_addr].frameById(m_)
                            except AttributeError:
                                can_msg = self._dbc_cache[dbc_addr].frame_by_id(
                                    canmatrix.ArbitrationId(m_)
                                )

                            for i, _ in enumerate(can_msg.signals, 1):
                                included_channels.add(-i)

            for dependencies in group.channel_dependencies:
                if dependencies is None:
                    continue
                if all(not isinstance(dep, ChannelArrayBlock) for dep in dependencies):
                    for _, ch_nr in dependencies:
                        try:
                            included_channels.remove(ch_nr)
                        except KeyError:
                            pass
                else:
                    for dep in dependencies:
                        for referenced_channels in (
                            dep.axis_channels,
                            dep.dynamic_size_channels,
                            dep.input_quantity_channels,
                        ):
                            for gp_nr, ch_nr in referenced_channels:
                                if gp_nr == index:
                                    try:
                                        included_channels.remove(ch_nr)
                                    except KeyError:
                                        pass

                        if dep.output_quantity_channel:
                            gp_nr, ch_nr = dep.output_quantity_channel
                            if gp_nr == index:
                                try:
                                    included_channels.remove(ch_nr)
                                except KeyError:
                                    pass

                        if dep.comparison_quantity_channel:
                            gp_nr, ch_nr = dep.comparison_quantity_channel
                            if gp_nr == index:
                                try:
                                    included_channels.remove(ch_nr)
                                except KeyError:
                                    pass

        return included_channels

    def __contains__(self, channel):
        """ if *'channel name'* in *'mdf file'* """
        return channel in self.channels_db

    def __iter__(self):
        """ iterate over all the channels found in the file; master channels
        are skipped from iteration

        """

        for signal in self.iter_channels():
            yield signal

    def convert(self, version):
        """convert *MDF* to other version

        Parameters
        ----------
        version : str
            new mdf file version from ('2.00', '2.10', '2.14', '3.00', '3.10',
            '3.20', '3.30', '4.00', '4.10', '4.11'); default '4.10'

        Returns
        -------
        out : MDF
            new *MDF* object

        """
        self._link_attributes()
        version = validate_version_argument(version)

        out = MDF(version=version)

        out.header.start_time = self.header.start_time

        try:
            for can_id, info in self.can_logging_db.items():
                if can_id not in out.can_logging_db:
                    out.can_logging_db[can_id] = {}
                out.can_logging_db[can_id].update(info)
        except AttributeError:
            pass

        groups_nr = len(self.groups)

        if self._callback:
            self._callback(0, groups_nr)

        cg_nr = None

        self.configure(copy_on_get=False)

        # walk through all groups and get all channels
        for i, group in enumerate(self.groups):

            encodings = []
            included_channels = self._included_channels(i)
            if not included_channels:
                continue

            parents, dtypes = self._prepare_record(group)

            data = self._load_data(group, optimize_read=False)
            for idx, fragment in enumerate(data):
                if dtypes.itemsize:
                    group.record = np.core.records.fromstring(fragment[0], dtype=dtypes)
                else:
                    group.record = None
                    continue

                self._set_temporary_master(self.get_master(i, data=fragment))

                # the first fragment triggers and append that will add the
                # metadata for all channels
                if idx == 0:
                    sigs = []
                    for j in included_channels:
                        sig = self.get(
                            group=i,
                            index=j,
                            data=fragment,
                            raw=True,
                            ignore_invalidation_bits=True,
                        )
                        if version < "4.00":
                            if sig.samples.dtype.kind == "S":
                                encodings.append(sig.encoding)
                                strsig = self.get(
                                    group=i,
                                    index=j,
                                    samples_only=True,
                                    ignore_invalidation_bits=True,
                                )[0]
                                sig.samples = sig.samples.astype(strsig.dtype)
                                del strsig
                                if sig.encoding != "latin-1":

                                    if sig.encoding == "utf-16-le":
                                        sig.samples = (
                                            sig.samples.view(np.uint16)
                                            .byteswap()
                                            .view(sig.samples.dtype)
                                        )
                                        sig.samples = encode(
                                            decode(sig.samples, "utf-16-be"), "latin-1",
                                        )
                                    else:
                                        sig.samples = encode(
                                            decode(sig.samples, sig.encoding),
                                            "latin-1",
                                        )
                            else:
                                encodings.append(None)
                        if not sig.samples.flags.writeable:
                            sig.samples = sig.samples.copy()
                        sigs.append(sig)
                    source_info = f"Converted from {self.version} to {version}"

                    if sigs:
                        cg_nr = out.append(sigs, source_info, common_timebase=True)
                        try:
                            if group.channel_group.flags & v4c.FLAG_CG_BUS_EVENT:
                                out.groups[
                                    -1
                                ].channel_group.flags = group.channel_group.flags
                                out.groups[
                                    -1
                                ].channel_group.acq_name = group.channel_group.acq_name
                                out.groups[
                                    -1
                                ].channel_group.acq_source = (
                                    group.channel_group.acq_source
                                )
                                out.groups[
                                    -1
                                ].channel_group.comment = group.channel_group.comment
                        except AttributeError:
                            pass
                    else:
                        break

                # the other fragments will trigger onl the extension of
                # samples records to the data block
                else:
                    sigs = [(self.get_master(i, data=fragment), None)]

                    for k, j in enumerate(included_channels):
                        sig = self.get(
                            group=i,
                            index=j,
                            data=fragment,
                            raw=True,
                            samples_only=True,
                            ignore_invalidation_bits=True,
                        )

                        if version < "4.00":
                            encoding = encodings[k]
                            samples = sig[0]
                            if encoding:
                                if encoding != "latin-1":

                                    if encoding == "utf-16-le":
                                        samples = (
                                            samples.view(np.uint16)
                                            .byteswap()
                                            .view(samples.dtype)
                                        )
                                        samples = encode(
                                            decode(samples, "utf-16-be"), "latin-1"
                                        )
                                    else:
                                        samples = encode(
                                            decode(samples, encoding), "latin-1"
                                        )
                                    sig.samples = samples

                        if not sig[0].flags.writeable:
                            sig = sig[0].copy(), sig[1]
                        sigs.append(sig)
                    out.extend(cg_nr, sigs)

                group.record = None
                self._set_temporary_master(None)

            if self._callback:
                self._callback(i + 1, groups_nr)

            if self._terminate:
                return

        out._transfer_events(self)
        self.configure(copy_on_get=True)
        if self._callback:
            out._callback = out._mdf._callback = self._callback
        return out

    def cut(
        self,
        start=None,
        stop=None,
        whence=0,
        version=None,
        include_ends=True,
        time_from_zero=False,
    ):
        """cut *MDF* file. *start* and *stop* limits are absolute values
        or values relative to the first timestamp depending on the *whence*
        argument.

        Parameters
        ----------
        start : float
            start time, default *None*. If *None* then the start of measurement
            is used
        stop : float
            stop time, default *None*. If *None* then the end of measurement is
            used
        whence : int
            how to search for the start and stop values

            * 0 : absolute
            * 1 : relative to first timestamp
        version : str
            new mdf file version from ('2.00', '2.10', '2.14', '3.00', '3.10',
            '3.20', '3.30', '4.00', '4.10', '4.11'); default *None* and in this
            case the original file version is used
        include_ends : bool
            include the *start* and *stop* timestamps after cutting the signal.
            If *start* and *stop* are found in the original timestamps, then
            the new samples will be computed using interpolation. Default *True*
        time_from_zero : bool
            start time stamps from 0s in the cut measurement

        Returns
        -------
        out : MDF
            new MDF object

        """

        self._link_attributes()

        if version is None:
            version = self.version
        else:
            version = validate_version_argument(version)

        out = MDF(version=version)
        self.configure(copy_on_get=False)

        if whence == 1:
            timestamps = []
            for i, group in enumerate(self.groups):
                master = self.get_master(i, record_offset=0, record_count=1,)
                if master.size:
                    timestamps.append(master[0])

            if timestamps:
                first_timestamp = np.amin(timestamps)
            else:
                first_timestamp = 0

            if start is not None:
                start += first_timestamp
            if stop is not None:
                stop += first_timestamp

        if time_from_zero:
            delta = start
            t_epoch = self.header.start_time.timestamp() + delta
            out.header.start_time = datetime.fromtimestamp(t_epoch)
        else:
            delta = 0
            out.header.start_time = self.header.start_time

        groups_nr = len(self.groups)

        if self._callback:
            self._callback(0, groups_nr)

        cg_nr = -1

        interpolation_mode = self._integer_interpolation

        # walk through all groups and get all channels
        for i, group in enumerate(self.groups):
            included_channels = self._included_channels(i)
            if included_channels:
                cg_nr += 1
            else:
                continue

            data = self._load_data(group, optimize_read=False)
            parents, dtypes = self._prepare_record(group)

            idx = 0
            for fragment in data:
                if dtypes.itemsize:
                    group.record = np.core.records.fromstring(fragment[0], dtype=dtypes)
                else:
                    group.record = None
                #                master = self.get_master(i, data=fragment, one_piece=True)
                self._set_temporary_master(None)
                master = self.get_master(i, data=fragment)

                self._set_temporary_master(master)
                if not len(master):
                    self._set_temporary_master(None)
                    continue

                needs_cutting = True

                # check if this fragement is within the cut interval or
                # if the cut interval has ended
                if start is None and stop is None:
                    fragment_start = None
                    fragment_stop = None
                    start_index = 0
                    stop_index = len(master)
                    needs_cutting = False
                elif start is None:
                    fragment_start = None
                    start_index = 0
                    if master[0] > stop:
                        break
                    else:
                        fragment_stop = min(stop, master[-1])
                        stop_index = np.searchsorted(
                            master, fragment_stop, side="right"
                        )
                        if stop_index == len(master):
                            needs_cutting = False
                elif stop is None:
                    fragment_stop = None
                    if master[-1] < start:
                        continue
                    else:
                        fragment_start = max(start, master[0])
                        start_index = np.searchsorted(
                            master, fragment_start, side="left"
                        )
                        stop_index = len(master)
                        if start_index == 0:
                            needs_cutting = False
                else:
                    if master[0] > stop:
                        break
                    elif master[-1] < start:
                        continue
                    else:
                        fragment_start = max(start, master[0])
                        start_index = np.searchsorted(
                            master, fragment_start, side="left"
                        )
                        fragment_stop = min(stop, master[-1])
                        stop_index = np.searchsorted(
                            master, fragment_stop, side="right"
                        )
                        if start_index == 0 and stop_index == len(master):
                            needs_cutting = False

                if needs_cutting:
                    cut_timebase = (
                        Signal(master, master, name="_")
                        .cut(
                            fragment_start,
                            fragment_stop,
                            include_ends,
                            interpolation_mode=interpolation_mode,
                        )
                        .timestamps
                    )

                # the first fragment triggers and append that will add the
                # metadata for all channels
                if idx == 0:
                    sigs = []
                    for j in included_channels:
                        sig = self.get(
                            group=i,
                            index=j,
                            data=fragment,
                            raw=True,
                            ignore_invalidation_bits=True,
                        )
                        if needs_cutting:
                            sig = sig.interp(
                                cut_timebase, interpolation_mode=interpolation_mode
                            )

                        # if sig.stream_sync and False:
                        #     attachment, _name = sig.attachment
                        #     duration = get_video_stream_duration(attachment)
                        #     if start is None:
                        #         start_t = 0
                        #     else:
                        #         start_t = start
                        #
                        #     if stop is None:
                        #         end_t = duration
                        #     else:
                        #         end_t = stop
                        #
                        #     attachment = cut_video_stream(
                        #         attachment,
                        #         start_t,
                        #         end_t,
                        #         Path(_name).suffix,
                        #     )
                        #     sig.attachment = attachment, _name

                        if not sig.samples.flags.writeable:
                            sig.samples = sig.samples.copy()
                        sigs.append(sig)

                    if sigs:
                        if time_from_zero:
                            new_timestamps = cut_timebase - delta
                            for sig in sigs:
                                sig.timestamps = new_timestamps
                        if start:
                            start_ = f"{start}s"
                        else:
                            start_ = "start of measurement"
                        if stop:
                            stop_ = f"{stop}s"
                        else:
                            stop_ = "end of measurement"
                        out.append(
                            sigs, f"Cut from {start_} to {stop_}", common_timebase=True
                        )
                        try:
                            if group.channel_group.flags & v4c.FLAG_CG_BUS_EVENT:
                                out.groups[
                                    -1
                                ].channel_group.flags = group.channel_group.flags
                                out.groups[
                                    -1
                                ].channel_group.acq_name = group.channel_group.acq_name
                                out.groups[
                                    -1
                                ].channel_group.acq_source = (
                                    group.channel_group.acq_source
                                )
                                out.groups[
                                    -1
                                ].channel_group.comment = group.channel_group.comment
                        except AttributeError:
                            pass
                    else:
                        break

                    idx += 1

                # the other fragments will trigger onl the extension of
                # samples records to the data block
                else:
                    if needs_cutting:
                        timestamps = cut_timebase
                    else:
                        timestamps = master

                    if time_from_zero:
                        timestamps = timestamps - delta

                    sigs = [(timestamps, None)]

                    for j in included_channels:
                        sig = self.get(
                            group=i,
                            index=j,
                            data=fragment,
                            raw=True,
                            samples_only=True,
                            ignore_invalidation_bits=True,
                        )
                        if needs_cutting:
                            _sig = Signal(
                                sig[0], master, name="_", invalidation_bits=sig[1]
                            ).interp(
                                cut_timebase, interpolation_mode=interpolation_mode
                            )
                            sig = (_sig.samples, _sig.invalidation_bits)

                            del _sig
                        sigs.append(sig)

                    if sigs:
                        out.extend(cg_nr, sigs)

                    idx += 1

                group.record = None
                self._set_temporary_master(None)

            # if the cut interval is not found in the measurement
            # then append an empty data group
            if idx == 0:

                self.configure(read_fragment_size=1)
                sigs = []

                fragment = next(self._load_data(group, optimize_read=False))

                for j in included_channels:
                    sig = self.get(
                        group=i,
                        index=j,
                        data=fragment,
                        raw=True,
                        ignore_invalidation_bits=True,
                    )
                    sig.samples = sig.samples[:0]
                    sig.timestamps = sig.timestamps[:0]
                    sigs.append(sig)

                if start:
                    start_ = f"{start}s"
                else:
                    start_ = "start of measurement"
                if stop:
                    stop_ = f"{stop}s"
                else:
                    stop_ = "end of measurement"
                out.append(sigs, f"Cut from {start_} to {stop_}", common_timebase=True)

                self.configure(read_fragment_size=0)

            if self._callback:
                self._callback(i + 1, groups_nr)

            if self._terminate:
                return

        self.configure(copy_on_get=True)

        out._transfer_events(self)
        if self._callback:
            out._callback = out._mdf._callback = self._callback
        return out

    def export(self, fmt, filename=None, **kwargs):
        """ export *MDF* to other formats. The *MDF* file name is used is
        available, else the *filename* argument must be provided.

        The *pandas* export option was removed. you should use the method
        *to_dataframe* instead.

        Parameters
        ----------
        fmt : string
            can be one of the following:

            * `csv` : CSV export that uses the "," delimiter. This option
              will generate a new csv file for each data group
              (<MDFNAME>_DataGroup_<cntr>.csv)

            * `hdf5` : HDF5 file output; each *MDF* data group is mapped to
              a *HDF5* group with the name 'DataGroup_<cntr>'
              (where <cntr> is the index)

            * `mat` : Matlab .mat version 4, 5 or 7.3 export. If
              *single_time_base==False* the channels will be renamed in the mat
              file to 'D<cntr>_<channel name>'. The channel group
              master will be renamed to 'DM<cntr>_<channel name>'
              ( *<cntr>* is the data group index starting from 0)

            * `parquet` : export to Apache parquet format

        filename : string | pathlib.Path
            export file name

        **kwargs

            * `single_time_base`: resample all channels to common time base,
              default *False*
            * `raster`: float time raster for resampling. Valid if
              *single_time_base* is *True*
            * `time_from_zero`: adjust time channel to start from 0
            * `use_display_names`: use display name instead of standard channel
              name, if available.
            * `empty_channels`: behaviour for channels without samples; the
              options are *skip* or *zeros*; default is *skip*
            * `format`: only valid for *mat* export; can be '4', '5' or '7.3',
              default is '5'
            * `oned_as`: only valid for *mat* export; can be 'row' or 'column'
            * `keep_arrays` : keep arrays and structure channels as well as the
              component channels. If *True* this can be very slow. If *False*
              only the component channels are saved, and their names will be
              prefixed with the parent channel.
            * reduce_memory_usage : bool
              reduce memory usage by converting all float columns to float32 and
              searching for minimum dtype that can reprezent the values found
              in integer columns; default *False*
            * compression : str
              compression to be used

              * for ``parquet`` : "GZIP" or "SANPPY"
              * for ``hfd5`` : "gzip", "lzf" or "szip"
              * for ``mat`` : bool

            * time_as_date (False) : bool
              export time as local timezone datetimee; only valid for CSV export

              .. versionadded:: 5.8.0

            * ignore_value2text_conversions (False) : bool
              valid only for the channels that have value to text conversions and
              if *raw=False*. If this is True then the raw numeric values will be
              used, and the conversion will not be applied.

              .. versionadded:: 5.8.0


        """

        self._link_attributes()

        header_items = (
            "date",
            "time",
            "author_field",
            "department_field",
            "project_field",
            "subject_field",
        )

        if fmt != "pandas" and filename is None and self.name is None:
            message = (
                "Must specify filename for export"
                "if MDF was created without a file name"
            )
            logger.warning(message)
            return

        single_time_base = kwargs.get("single_time_base", False)
        raster = kwargs.get("raster", 0)
        time_from_zero = kwargs.get("time_from_zero", True)
        use_display_names = kwargs.get("use_display_names", True)
        empty_channels = kwargs.get("empty_channels", "skip")
        format = kwargs.get("format", "5")
        oned_as = kwargs.get("oned_as", "row")
        reduce_memory_usage = kwargs.get("reduce_memory_usage", False)
        compression = kwargs.get("compression", "")
        time_as_date = kwargs.get("time_as_date", False)
        ignore_value2text_conversions = kwargs.get(
            "ignore_value2text_conversions", False
        )

        if compression == "SNAPPY":
            try:
                import snappy
            except ImportError:
                logger.warning(
                    "snappy compressor is not installed; compression will be set to GZIP"
                )
                compression = "GZIP"

        filename = Path(filename) if filename else self.name

        if fmt == "parquet":
            try:
                from fastparquet import write as write_parquet
            except ImportError:
                logger.warning(
                    "fastparquet not found; export to parquet is unavailable"
                )
                return

        elif fmt == "hdf5":
            try:
                from h5py import File as HDF5
            except ImportError:
                logger.warning("h5py not found; export to HDF5 is unavailable")
                return

        elif fmt == "mat":
            if format == "7.3":
                try:
                    from hdf5storage import savemat
                except ImportError:
                    logger.warning(
                        "hdf5storage not found; export to mat v7.3 is unavailable"
                    )
                    return
            else:
                try:
                    from scipy.io import savemat
                except ImportError:
                    logger.warning("scipy not found; export to mat is unavailable")
                    return

        elif fmt not in ("csv",):
            raise MdfException(f"Export to {fmt} is not implemented")

        name = ""

        if self._callback:
            self._callback(0, 100)

        if single_time_base or fmt == "parquet":
            df = self.to_dataframe(
                raster=raster,
                time_from_zero=time_from_zero,
                use_display_names=use_display_names,
                empty_channels=empty_channels,
                reduce_memory_usage=reduce_memory_usage,
                ignore_value2text_conversions=ignore_value2text_conversions,
            )
            units = OrderedDict()
            comments = OrderedDict()
            used_names = UniqueDB()

            dropped = {}

            groups_nr = len(self.groups)
            for i, grp in enumerate(self.groups):
                if self._terminate:
                    return

                included_channels = self._included_channels(i)

                for j in included_channels:
                    ch = grp.channels[j]

                    if use_display_names:
                        channel_name = ch.display_name or ch.name
                    else:
                        channel_name = ch.name

                    channel_name = used_names.get_unique_name(channel_name)

                    if hasattr(ch, "unit"):
                        unit = ch.unit
                        if ch.conversion:
                            unit = unit or ch.conversion.unit
                    else:
                        unit = ""
                    comment = ch.comment

                    units[channel_name] = unit
                    comments[channel_name] = comment

                if self._callback:
                    self._callback(i + 1, groups_nr * 2)

        if fmt == "hdf5":
            filename = filename.with_suffix(".hdf")

            if single_time_base:

                with HDF5(str(filename), "w") as hdf:
                    # header information
                    group = hdf.create_group(str(filename))

                    if self.version in MDF2_VERSIONS + MDF3_VERSIONS:
                        for item in header_items:
                            group.attrs[item] = self.header[item].replace(b"\0", b"")

                    # save each data group in a HDF5 group called
                    # "DataGroup_<cntr>" with the index starting from 1
                    # each HDF5 group will have a string attribute "master"
                    # that will hold the name of the master channel

                    count = len(df.columns)

                    for i, channel in enumerate(df):
                        samples = df[channel]
                        unit = units.get(channel, "")
                        comment = comments.get(channel, "")

                        if samples.dtype.kind == "O":
                            if isinstance(samples[0], np.ndarray):
                                samples = np.vstack(samples)
                            else:
                                continue

                        if compression:
                            dataset = group.create_dataset(
                                channel, data=samples, compression=compression,
                            )
                        else:
                            dataset = group.create_dataset(channel, data=samples)
                        unit = unit.replace("\0", "")
                        if unit:
                            dataset.attrs["unit"] = unit
                        comment = comment.replace("\0", "")
                        if comment:
                            dataset.attrs["comment"] = comment

                        if self._callback:
                            self._callback(i + 1 + count, count * 2)

            else:
                with HDF5(str(filename), "w") as hdf:
                    # header information
                    group = hdf.create_group(str(filename))

                    if self.version in MDF2_VERSIONS + MDF3_VERSIONS:
                        for item in header_items:
                            group.attrs[item] = self.header[item].replace(b"\0", b"")

                    # save each data group in a HDF5 group called
                    # "DataGroup_<cntr>" with the index starting from 1
                    # each HDF5 group will have a string attribute "master"
                    # that will hold the name of the master channel

                    groups_nr = len(self.groups)
                    for i, grp in enumerate(self.groups):
                        if not len(grp.channels):
                            continue
                        names = UniqueDB()
                        if self._terminate:
                            return
                        group_name = r"/" + f"ChannelGroup_{i}"
                        group = hdf.create_group(group_name)

                        group.attrs["comment"] = grp.channel_group.comment

                        master_index = self.masters_db.get(i, -1)

                        if master_index >= 0:
                            group.attrs["master"] = grp.channels[master_index].name

                        channels = self.select(
                            [(ch.name, i, None) for ch in grp.channels]
                        )

                        for j, sig in enumerate(channels):
                            if use_display_names:
                                name = sig.display_name or sig.name
                            else:
                                name = sig.name
                            name = name.replace("\\", "_").replace("/", "_")
                            name = names.get_unique_name(name)
                            if reduce_memory_usage:
                                sig.samples = downcast(sig.samples)
                            if compression:
                                dataset = group.create_dataset(
                                    name, data=sig.samples, compression=compression,
                                )
                            else:
                                dataset = group.create_dataset(
                                    name, data=sig.samples, dtype=sig.samples.dtype
                                )
                            unit = sig.unit.replace("\0", "")
                            if unit:
                                dataset.attrs["unit"] = unit
                            comment = sig.comment.replace("\0", "")
                            if comment:
                                dataset.attrs["comment"] = comment

                        if self._callback:
                            self._callback(i + 1, groups_nr)

        elif fmt == "csv":
            if single_time_base:
                filename = filename.with_suffix(".csv")
                message = f'Writing csv export to file "{filename}"'
                logger.info(message)

                if time_as_date:
                    index = (
                        pd.to_datetime(
                            df.index + self.header.start_time.timestamp(), unit="s"
                        )
                        .tz_localize("UTC")
                        .tz_convert(LOCAL_TIMEZONE)
                        .astype(str)
                    )
                    df.index = index
                    df.index.name = "timestamps"

                with open(filename, "w", newline="") as csvfile:
                    writer = csv.writer(csvfile)

                    if hasattr(self, "can_logging_db") and self.can_logging_db:

                        dropped = {}

                        for name_ in df.columns:
                            if name_.endswith("CAN_DataFrame.ID"):
                                dropped[name_] = pd.Series(
                                    csv_int2hex(df[name_].astype("<u4") & 0x1FFFFFFF),
                                    index=df.index,
                                )

                            elif name_.endswith("CAN_DataFrame.DataBytes"):
                                dropped[name_] = pd.Series(
                                    csv_bytearray2hex(df[name_]), index=df.index
                                )

                        df = df.drop(columns=list(dropped))
                        for name, s in dropped.items():
                            df[name] = s

                    names_row = [df.index.name, *df.columns]
                    writer.writerow(names_row)

                    vals = [df.index, *(df[name] for name in df)]

                    count = len(df.index)

                    if self._terminate:
                        return

                    for i, row in enumerate(zip(*vals)):
                        writer.writerow(row)

                        if self._callback:
                            self._callback(i + 1 + count, count * 2)

            else:

                filename = filename.with_suffix(".csv")

                gp_count = len(self.groups)
                for i, grp in enumerate(self.groups):

                    if self._terminate:
                        return
                    if not len(grp.channels):
                        continue
                    message = f"Exporting group {i+1} of {gp_count}"
                    logger.info(message)

                    comment = grp.channel_group.comment
                    if comment:
                        for char in r" \/:":
                            comment = comment.replace(char, "_")
                        group_csv_name = (
                            filename.parent
                            / f"{filename.stem}.ChannelGroup_{i}_{comment}.csv"
                        )
                    else:
                        group_csv_name = (
                            filename.parent / f"{filename.stem}.ChannelGroup_{i}.csv"
                        )

                    df = self.get_group(
                        i,
                        raster=raster,
                        time_from_zero=time_from_zero,
                        use_display_names=use_display_names,
                        reduce_memory_usage=reduce_memory_usage,
                        ignore_value2text_conversions=ignore_value2text_conversions,
                    )

                    if time_as_date:
                        index = (
                            pd.to_datetime(
                                df.index + self.header.start_time.timestamp(), unit="s"
                            )
                            .tz_localize("UTC")
                            .tz_convert(LOCAL_TIMEZONE)
                            .astype(str)
                        )
                        df.index = index
                        df.index.name = "timestamps"

                    with open(group_csv_name, "w", newline="") as csvfile:
                        writer = csv.writer(csvfile)

                        if hasattr(self, "can_logging_db") and self.can_logging_db:

                            dropped = {}

                            for name_ in df.columns:
                                if name_.endswith("CAN_DataFrame.ID"):
                                    dropped[name_] = pd.Series(
                                        csv_int2hex(df[name_] & 0x1FFFFFFF),
                                        index=df.index,
                                    )

                                elif name_.endswith("CAN_DataFrame.DataBytes"):
                                    dropped[name_] = pd.Series(
                                        csv_bytearray2hex(df[name_]), index=df.index
                                    )

                            df = df.drop(columns=list(dropped))
                            for name_, s in dropped.items():
                                df[name_] = s

                        names_row = [df.index.name, *df.columns]
                        writer.writerow(names_row)

                        vals = [df.index, *(df[name] for name in df)]

                        count = len(df.index)

                        for i, row in enumerate(zip(*vals)):
                            writer.writerow(row)

                    if self._callback:
                        self._callback(i + 1, gp_count)

        elif fmt == "mat":

            filename = filename.with_suffix(".mat")

            if not single_time_base:
                mdict = {}

                master_name_template = "DGM{}_{}"
                channel_name_template = "DG{}_{}"
                used_names = UniqueDB()

                groups_nr = len(self.groups)

                for i, grp in enumerate(self.groups):
                    if self._terminate:
                        return
                    if not len(grp.channels):
                        continue

                    included_channels = self._included_channels(i)

                    master_index = self.masters_db.get(i, -1)

                    if master_index >= 0:
                        included_channels.add(master_index)

                    channels = self.select(
                        [(None, i, idx) for idx in included_channels],
                        ignore_value2text_conversions=ignore_value2text_conversions,
                    )

                    for j, sig in zip(included_channels, channels):

                        if j == master_index:
                            channel_name = master_name_template.format(i, sig.name)
                        else:
                            if use_display_names:
                                channel_name = sig.display_name or sig.name
                            else:
                                channel_name = sig.name
                            channel_name = channel_name_template.format(i, channel_name)

                        channel_name = matlab_compatible(channel_name)
                        channel_name = used_names.get_unique_name(channel_name)

                        if sig.samples.dtype.names:
                            sig.samples.dtype.names = [
                                matlab_compatible(name)
                                for name in sig.samples.dtype.names
                            ]

                        mdict[channel_name] = sig.samples

                    if self._callback:
                        self._callback(i + 1, groups_nr + 1)

            else:
                used_names = UniqueDB()
                mdict = {}

                count = len(df.columns)

                for i, name in enumerate(df.columns):
                    channel_name = matlab_compatible(name)
                    channel_name = used_names.get_unique_name(channel_name)

                    mdict[channel_name] = df[name].values

                    if hasattr(mdict[channel_name].dtype, "categories"):
                        mdict[channel_name] = np.array(mdict[channel_name], dtype="S")

                    if self._callback:
                        self._callback(i + 1 + count, count * 2)

                mdict["timestamps"] = df.index.values

            if self._callback:
                self._callback(80, 100)
            if format == "7.3":

                savemat(
                    str(filename),
                    mdict,
                    long_field_names=True,
                    format="7.3",
                    delete_unused_variables=False,
                    oned_as=oned_as,
                    structured_numpy_ndarray_as_struct=True,
                )
            else:
                savemat(
                    str(filename),
                    mdict,
                    long_field_names=True,
                    oned_as=oned_as,
                    do_compression=bool(compression),
                )
            if self._callback:
                self._callback(100, 100)

        elif fmt == "parquet":
            filename = filename.with_suffix(".parquet")
            if compression:
                write_parquet(filename, df, compression=compression)
            else:
                write_parquet(filename, df)

        else:
            message = (
                'Unsopported export type "{}". '
                'Please select "csv", "excel", "hdf5", "mat" or "pandas"'
            )
            message.format(fmt)
            logger.warning(message)

    def filter(self, channels, version=None):
        """ return new *MDF* object that contains only the channels listed in
        *channels* argument

        Parameters
        ----------
        channels : list
            list of items to be filtered; each item can be :

                * a channel name string
                * (channel name, group index, channel index) list or tuple
                * (channel name, group index) list or tuple
                * (None, group index, channel index) list or tuple

        version : str
            new mdf file version from ('2.00', '2.10', '2.14', '3.00', '3.10',
            '3.20', '3.30', '4.00', '4.10', '4.11'); default *None* and in this
            case the original file version is used

        Returns
        -------
        mdf : MDF
            new *MDF* file

        Examples
        --------
        >>> from asammdf import MDF, Signal
        >>> import numpy as np
        >>> t = np.arange(5)
        >>> s = np.ones(5)
        >>> mdf = MDF()
        >>> for i in range(4):
        ...     sigs = [Signal(s*(i*10+j), t, name='SIG') for j in range(1,4)]
        ...     mdf.append(sigs)
        ...
        >>> filtered = mdf.filter(['SIG', ('SIG', 3, 1), ['SIG', 2], (None, 1, 2)])
        >>> for gp_nr, ch_nr in filtered.channels_db['SIG']:
        ...     print(filtered.get(group=gp_nr, index=ch_nr))
        ...
        <Signal SIG:
                samples=[ 1.  1.  1.  1.  1.]
                timestamps=[0 1 2 3 4]
                unit=""
                info=None
                comment="">
        <Signal SIG:
                samples=[ 31.  31.  31.  31.  31.]
                timestamps=[0 1 2 3 4]
                unit=""
                info=None
                comment="">
        <Signal SIG:
                samples=[ 21.  21.  21.  21.  21.]
                timestamps=[0 1 2 3 4]
                unit=""
                info=None
                comment="">
        <Signal SIG:
                samples=[ 12.  12.  12.  12.  12.]
                timestamps=[0 1 2 3 4]
                unit=""
                info=None
                comment="">

        """

        self._link_attributes()

        if version is None:
            version = self.version
        else:
            version = validate_version_argument(version)

        # group channels by group index
        gps = {}

        for item in channels:
            if isinstance(item, (list, tuple)):
                if len(item) not in (2, 3):
                    raise MdfException(
                        "The items used for filtering must be strings, "
                        "or they must match the first 3 argumens of the get "
                        "method"
                    )
                else:
                    group, index = self._validate_channel_selection(*item)
                    if group not in gps:
                        gps[group] = {index}
                    else:
                        gps[group].add(index)
            else:
                name = item
                group, index = self._validate_channel_selection(name)
                if group not in gps:
                    gps[group] = {index}
                else:
                    gps[group].add(index)

        self.configure(copy_on_get=False)

        # see if there are excluded channels in the filter list
        for group_index, indexes in gps.items():
            grp = self.groups[group_index]
            included_channels = set(indexes)
            master_index = self.masters_db.get(group_index, None)
            if master_index is not None:
                to_exclude = {master_index}
            else:
                to_exclude = set()

            if included_channels == to_exclude:
                gps[group_index] = [
                    master_index,
                ]
                continue

            for index in indexes:
                if self.version in MDF2_VERSIONS + MDF3_VERSIONS:
                    dep = grp.channel_dependencies[index]
                    if dep:
                        for gp_nr, ch_nr in dep.referenced_channels:
                            if gp_nr == group:
                                try:
                                    included_channels.remove(ch_nr)
                                except:
                                    pass
                else:
                    dependencies = grp.channel_dependencies[index]
                    if dependencies is None:
                        continue
                    if all(
                        not isinstance(dep, ChannelArrayBlock) for dep in dependencies
                    ):
                        channels = grp.channels
                        for _, channel in dependencies:
                            to_exclude.add(channel)
                    else:
                        for dep in dependencies:
                            for referenced_channels in (
                                dep.axis_channels,
                                dep.dynamic_size_channels,
                                dep.input_quantity_channels,
                            ):
                                for gp_nr, ch_nr in referenced_channels:
                                    if gp_nr == index:
                                        try:
                                            included_channels.remove(ch_nr)
                                        except KeyError:
                                            pass

                            if dep.output_quantity_channel:
                                gp_nr, ch_nr = dep.output_quantity_channel
                                if gp_nr == index:
                                    try:
                                        included_channels.remove(ch_nr)
                                    except KeyError:
                                        pass

                            if dep.comparison_quantity_channel:
                                gp_nr, ch_nr = dep.comparison_quantity_channel
                                if gp_nr == index:
                                    try:
                                        included_channels.remove(ch_nr)
                                    except KeyError:
                                        pass

            gps[group_index] = sorted(included_channels - to_exclude)

        mdf = MDF(version=version)

        mdf.header.start_time = self.header.start_time

        if self.name:
            origin = self.name.parent
        else:
            origin = "New MDF"

        groups_nr = len(gps)

        if self._callback:
            self._callback(0, groups_nr)

        # append filtered channels to new MDF
        for new_index, (group_index, indexes) in enumerate(gps.items()):
            if version < "4.00":
                encodings = []

            group = self.groups[group_index]

            data = self._load_data(group, optimize_read=False)
            _, dtypes = self._prepare_record(group)

            for idx, fragment in enumerate(data):

                if dtypes.itemsize:
                    group.record = np.core.records.fromstring(fragment[0], dtype=dtypes)
                else:
                    group.record = None

                self._set_temporary_master(self.get_master(group_index, data=fragment))

                # the first fragment triggers and append that will add the
                # metadata for all channels
                if idx == 0:
                    sigs = []
                    for j in indexes:
                        sig = self.get(
                            group=group_index,
                            index=j,
                            data=fragment,
                            raw=True,
                            ignore_invalidation_bits=True,
                        )
                        if version < "4.00":
                            if sig.samples.dtype.kind == "S":
                                encodings.append(sig.encoding)
                                strsig = self.get(
                                    group=group_index,
                                    index=j,
                                    samples_only=True,
                                    ignore_invalidation_bits=True,
                                )[0]
                                sig.samples = sig.samples.astype(strsig.dtype)
                                del strsig
                                if sig.encoding != "latin-1":

                                    if sig.encoding == "utf-16-le":
                                        sig.samples = (
                                            sig.samples.view(np.uint16)
                                            .byteswap()
                                            .view(sig.samples.dtype)
                                        )
                                        sig.samples = encode(
                                            decode(sig.samples, "utf-16-be"), "latin-1"
                                        )
                                    else:
                                        sig.samples = encode(
                                            decode(sig.samples, sig.encoding), "latin-1"
                                        )
                            else:
                                encodings.append(None)
                        if not sig.samples.flags.writeable:
                            sig.samples = sig.samples.copy()
                        sigs.append(sig)

                    source_info = f"Signals filtered from <{origin}>"

                    if sigs:
                        mdf.append(sigs, source_info, common_timebase=True)
                        try:
                            mdf.groups[
                                -1
                            ].channel_group.flags = group.channel_group.flags
                            mdf.groups[
                                -1
                            ].channel_group.acq_name = group.channel_group.acq_name
                            mdf.groups[
                                -1
                            ].channel_group.acq_source = group.channel_group.acq_source
                            mdf.groups[
                                -1
                            ].channel_group.comment = group.channel_group.comment
                        except AttributeError:
                            pass
                    else:
                        break

                # the other fragments will trigger onl the extension of
                # samples records to the data block
                else:
                    sigs = [(self.get_master(group_index, data=fragment,), None,)]

                    for k, j in enumerate(indexes):
                        sig = self.get(
                            group=group_index,
                            index=j,
                            data=fragment,
                            samples_only=True,
                            raw=True,
                            ignore_invalidation_bits=True,
                        )
                        if version < "4.00":
                            encoding = encodings[k]
                            samples = sig[0]
                            if encoding:
                                if encoding != "latin-1":

                                    if encoding == "utf-16-le":
                                        samples = (
                                            samples.view(np.uint16)
                                            .byteswap()
                                            .view(samples.dtype)
                                        )
                                        samples = encode(
                                            decode(samples, "utf-16-be"), "latin-1"
                                        )
                                    else:
                                        samples = encode(
                                            decode(samples, encoding), "latin-1"
                                        )
                                    sig.samples = samples

                        sigs.append(sig)

                    if sigs:
                        mdf.extend(new_index, sigs)

                group.record = None
                self._set_temporary_master(None)

            if self._callback:
                self._callback(new_index + 1, groups_nr)

            if self._terminate:
                return

        self.configure(copy_on_get=True)

        mdf._transfer_events(self)
        if self._callback:
            mdf._callback = mdf._mdf._callback = self._callback
        return mdf

    def iter_get(
        self,
        name=None,
        group=None,
        index=None,
        raster=None,
        samples_only=False,
        raw=False,
    ):
        """ iterator over a channel

        This is usefull in case of large files with a small number of channels.

        If the *raster* keyword argument is not *None* the output is
        interpolated accordingly

        Parameters
        ----------
        name : string
            name of channel
        group : int
            0-based group index
        index : int
            0-based channel index
        raster : float
            time raster in seconds
        samples_only : bool
            if *True* return only the channel samples as numpy array; if
                *False* return a *Signal* object
        raw : bool
            return channel samples without appling the conversion rule; default
            `False`

        """
        self._link_attributes()

        gp_nr, ch_nr = self._validate_channel_selection(name, group, index)

        grp = self.groups[gp_nr]

        data = self._load_data(grp)

        for fragment in data:
            yield self.get(
                group=gp_nr,
                index=ch_nr,
                raster=raster,
                samples_only=samples_only,
                data=fragment,
                raw=raw,
            )

    @staticmethod
    def concatenate(
        files, version="4.10", sync=True, add_samples_origin=False, **kwargs
    ):
        """ concatenates several files. The files
        must have the same internal structure (same number of groups, and same
        channels in each group)

        Parameters
        ----------
        files : list | tuple
            list of *MDF* file names or *MDF* instances
        version : str
            merged file version
        sync : bool
            sync the files based on the start of measurement, default *True*
        add_samples_origin : bool
            option to create a new "__samples_origin" channel that will hold
            the index of the measurement from where each timestamp originated

        Returns
        -------
        concatenate : MDF
            new *MDF* object with concatenated channels

        Raises
        ------
        MdfException : if there are inconsistencies between the files

        """
        if not files:
            raise MdfException("No files given for merge")

        callback = kwargs.get("callback", None)
        if callback:
            callback(0, 100)

        mdf_nr = len(files)

        input_types = [isinstance(mdf, MDF) for mdf in files]

        versions = []
        if sync:
            timestamps = []
            for file in files:
                if isinstance(file, MDF):
                    timestamps.append(file.header.start_time)
                    versions.append(file.version)
                else:
                    with open(file, "rb") as mdf:
                        mdf.seek(64)
                        blk_id = mdf.read(2)
                        if blk_id == b"HD":
                            header = HeaderV3
                            versions.append("3.00")
                        else:
                            versions.append("4.00")
                            blk_id += mdf.read(2)
                            if blk_id == b"##HD":
                                header = HeaderV4
                            else:
                                raise MdfException(f'"{file}" is not a valid MDF file')

                        header = header(address=64, stream=mdf)

                        timestamps.append(header.start_time)

            try:
                oldest = min(timestamps)
            except TypeError:
                timestamps = [
                    timestamp.astimezone(timezone.utc) for timestamp in timestamps
                ]
                oldest = min(timestamps)

            offsets = [(timestamp - oldest).total_seconds() for timestamp in timestamps]
            offsets = [offset if offset > 0 else 0 for offset in offsets]

        else:
            file = files[0]
            if isinstance(file, MDF):
                oldest = file.header.start_time
                versions.append(file.version)
            else:
                with open(file, "rb") as mdf:
                    mdf.seek(64)
                    blk_id = mdf.read(2)
                    if blk_id == b"HD":
                        versions.append("3.00")
                        header = HeaderV3
                    else:
                        versions.append("4.00")
                        blk_id += mdf.read(2)
                        if blk_id == b"##HD":
                            header = HeaderV4
                        else:
                            raise MdfException(f'"{file}" is not a valid MDF file')

                    header = header(address=64, stream=mdf)

                    oldest = header.start_time

            offsets = [0 for _ in files]

        version = validate_version_argument(version)

        merged = MDF(version=version, callback=callback)

        merged.header.start_time = oldest

        encodings = []
        included_channel_names = []

        if add_samples_origin:
            origin_conversion = {}
            for i, mdf in enumerate(files):
                origin_conversion[f"val_{i}"] = i
                if isinstance(mdf, MDF):
                    origin_conversion[f"text_{i}"] = str(mdf.name)
                else:
                    origin_conversion[f"text_{i}"] = str(mdf)
            origin_conversion = from_dict(origin_conversion)

        for mdf_index, (offset, mdf) in enumerate(zip(offsets, files)):
            if not isinstance(mdf, MDF):
                mdf = MDF(mdf)

            mdf.configure(copy_on_get=False)

            try:
                for can_id, info in mdf.can_logging_db.items():
                    if can_id not in merged.can_logging_db:
                        merged.can_logging_db[can_id] = {}
                    merged.can_logging_db[can_id].update(info)
            except AttributeError:
                pass

            if mdf_index == 0:
                last_timestamps = [None for gp in mdf.groups]
                groups_nr = len(mdf.groups)

            cg_nr = -1

            for i, group in enumerate(mdf.groups):
                included_channels = mdf._included_channels(i)

                if mdf_index == 0:
                    included_channel_names.append(
                        [group.channels[k].name for k in included_channels]
                    )
                else:
                    names = [group.channels[k].name for k in included_channels]
                    if names != included_channel_names[i]:
                        if sorted(names) != sorted(included_channel_names[i]):
                            raise MdfException(
                                f"internal structure of file {mdf_index} is different"
                            )
                        else:
                            logger.warning(
                                f"Different channel order in channel group {i} of file {mdf_index}."
                                " Data can be corrupted if the there are channels with the same "
                                "name in this channel group"
                            )
                            included_channels = [
                                mdf._validate_channel_selection(name=name_, group=i,)[1]
                                for name_ in included_channel_names[i]
                            ]

                if included_channels:
                    cg_nr += 1
                else:
                    continue
                channels_nr = len(group.channels)

                y_axis = MERGE

                idx = np.searchsorted(CHANNEL_COUNT, channels_nr, side="right") - 1
                if idx < 0:
                    idx = 0
                read_size = y_axis[idx]

                idx = 0
                last_timestamp = last_timestamps[i]
                first_timestamp = None
                original_first_timestamp = None

                if read_size:
                    mdf.configure(read_fragment_size=int(read_size))

                parents, dtypes = mdf._prepare_record(group)

                data = mdf._load_data(group, optimize_read=False)

                for f_index, fragment in enumerate(data):

                    if dtypes.itemsize:
                        group.record = np.core.records.fromstring(
                            fragment[0], dtype=dtypes
                        )
                    else:
                        group.record = None

                    mdf._set_temporary_master(mdf.get_master(i, data=fragment))

                    if mdf_index == 0 and idx == 0:
                        encodings_ = []
                        encodings.append(encodings_)
                        signals = []
                        for j in included_channels:
                            sig = mdf.get(
                                group=i,
                                index=j,
                                data=fragment,
                                raw=True,
                                ignore_invalidation_bits=True,
                            )

                            if version < "4.00":
                                if sig.samples.dtype.kind == "S":
                                    encodings_.append(sig.encoding)
                                    strsig = mdf.get(
                                        group=i,
                                        index=j,
                                        samples_only=True,
                                        ignore_invalidation_bits=True,
                                    )[0]
                                    sig.samples = sig.samples.astype(strsig.dtype)
                                    del strsig
                                    if sig.encoding != "latin-1":

                                        if sig.encoding == "utf-16-le":
                                            sig.samples = (
                                                sig.samples.view(np.uint16)
                                                .byteswap()
                                                .view(sig.samples.dtype)
                                            )
                                            sig.samples = encode(
                                                decode(sig.samples, "utf-16-be"),
                                                "latin-1",
                                            )
                                        else:
                                            sig.samples = encode(
                                                decode(sig.samples, sig.encoding),
                                                "latin-1",
                                            )
                                else:
                                    encodings_.append(None)

                            if not sig.samples.flags.writeable:
                                sig.samples = sig.samples.copy()
                            signals.append(sig)

                        if signals and len(signals[0]):
                            if offset > 0:
                                timestamps = signals[0].timestamps + offset
                                for sig in signals:
                                    sig.timestamps = timestamps
                            last_timestamp = signals[0].timestamps[-1]
                            first_timestamp = signals[0].timestamps[0]
                            original_first_timestamp = first_timestamp

                        if add_samples_origin:
                            if signals:
                                _s = signals[-1]
                                signals.append(
                                    Signal(
                                        samples=np.ones(len(_s), dtype="<u2")
                                        * mdf_index,
                                        timestamps=_s.timestamps,
                                        conversion=origin_conversion,
                                        name="__samples_origin",
                                    )
                                )
                                _s = None

                        if signals:
                            merged.append(signals, common_timebase=True)
                            try:
                                if group.channel_group.flags & v4c.FLAG_CG_BUS_EVENT:
                                    merged.groups[
                                        -1
                                    ].channel_group.flags = group.channel_group.flags
                                    merged.groups[
                                        -1
                                    ].channel_group.acq_name = (
                                        group.channel_group.acq_name
                                    )
                                    merged.groups[
                                        -1
                                    ].channel_group.acq_source = (
                                        group.channel_group.acq_source
                                    )
                                    merged.groups[
                                        -1
                                    ].channel_group.comment = (
                                        group.channel_group.comment
                                    )
                            except AttributeError:
                                pass
                        else:
                            break
                        idx += 1
                    else:
                        master = mdf.get_master(i, fragment)
                        _copied = False

                        if len(master):
                            if original_first_timestamp is None:
                                original_first_timestamp = master[0]
                            if offset > 0:
                                master = master + offset
                                _copied = True
                            if last_timestamp is None:
                                last_timestamp = master[-1]
                            else:
                                if last_timestamp >= master[0]:
                                    if len(master) >= 2:
                                        delta = master[1] - master[0]
                                    else:
                                        delta = 0.001
                                    if _copied:
                                        master -= master[0]
                                    else:
                                        master = master - master[0]
                                        _copied = True
                                    master += last_timestamp + delta
                                last_timestamp = master[-1]

                            signals = [(master, None)]

                            for k, j in enumerate(included_channels):
                                sig = mdf.get(
                                    group=i,
                                    index=j,
                                    data=fragment,
                                    raw=True,
                                    samples_only=True,
                                    ignore_invalidation_bits=True,
                                )

                                signals.append(sig)

                                if version < "4.00":
                                    encoding = encodings[i][k]
                                    samples = sig[0]
                                    if encoding:
                                        if encoding != "latin-1":

                                            if encoding == "utf-16-le":
                                                samples = (
                                                    samples.view(np.uint16)
                                                    .byteswap()
                                                    .view(samples.dtype)
                                                )
                                                samples = encode(
                                                    decode(samples, "utf-16-be"),
                                                    "latin-1",
                                                )
                                            else:
                                                samples = encode(
                                                    decode(samples, encoding), "latin-1"
                                                )
                                            sig.samples = samples

                            if signals:
                                if add_samples_origin:
                                    _s = signals[-1][0]
                                    signals.append(
                                        (
                                            np.ones(len(_s), dtype="<u2") * mdf_index,
                                            None,
                                        )
                                    )
                                    _s = None
                                merged.extend(cg_nr, signals)

                            if first_timestamp is None:
                                first_timestamp = master[0]
                        idx += 1

                    group.record = None
                    mdf._set_temporary_master(None)

                last_timestamps[i] = last_timestamp

            mdf.configure(copy_on_get=True)

            if not input_types[mdf_index]:
                mdf.close()

            if callback:
                callback(i + 1 + mdf_index * groups_nr, groups_nr * mdf_nr)

            if MDF._terminate:
                return

            merged._transfer_events(mdf)

        return merged

    @staticmethod
    def stack(files, version="4.10", sync=True, **kwargs):
        """ stack several files and return the stacked *MDF* object

        Parameters
        ----------
        files : list | tuple
            list of *MDF* file names or *MDF* instances
        version : str
            merged file version
        sync : bool
            sync the files based on the start of measurement, default *True*

        Returns
        -------
        stacked : MDF
            new *MDF* object with stacked channels

        """
        if not files:
            raise MdfException("No files given for stack")

        version = validate_version_argument(version)

        callback = kwargs.get("callback", None)

        stacked = MDF(version=version, callback=callback)

        files_nr = len(files)

        input_types = [isinstance(mdf, MDF) for mdf in files]

        if callback:
            callback(0, files_nr)

        if sync:
            timestamps = []
            for file in files:
                if isinstance(file, MDF):
                    timestamps.append(file.header.start_time)
                else:
                    with open(file, "rb") as mdf:
                        mdf.seek(64)
                        blk_id = mdf.read(2)
                        if blk_id == b"HD":
                            header = HeaderV3
                        else:
                            blk_id += mdf.read(2)
                            if blk_id == b"##HD":
                                header = HeaderV4
                            else:
                                raise MdfException(f'"{file}" is not a valid MDF file')

                        header = header(address=64, stream=mdf)

                        timestamps.append(header.start_time)

            try:
                oldest = min(timestamps)
            except TypeError:
                timestamps = [
                    timestamp.astimezone(timezone.utc) for timestamp in timestamps
                ]
                oldest = min(timestamps)

            offsets = [(timestamp - oldest).total_seconds() for timestamp in timestamps]

            stacked.header.start_time = oldest
        else:
            offsets = [0 for file in files]

        cg_nr = -1
        for mdf_index, (offset, mdf) in enumerate(zip(offsets, files)):
            if not isinstance(mdf, MDF):
                mdf = MDF(mdf)

            mdf.configure(copy_on_get=False)

            cg_offset = cg_nr + 1

            for i, group in enumerate(mdf.groups):
                idx = 0
                if version < "4.00":
                    encodings = []
                included_channels = mdf._included_channels(i)
                if included_channels:
                    cg_nr += 1
                else:
                    continue

                try:
                    for can_id, info in mdf.can_logging_db.items():
                        if can_id not in mdf.can_logging_db:
                            mdf.can_logging_db[can_id] = {}
                        mdf.can_logging_db[can_id].update(
                            {
                                message_id: cg_index + cg_offset
                                for message_id, cg_index in info.items()
                            }
                        )
                except AttributeError:
                    pass

                _, dtypes = mdf._prepare_record(group)

                data = mdf._load_data(group, optimize_read=False)

                for fragment in data:

                    if dtypes.itemsize:
                        group.record = np.core.records.fromstring(
                            fragment[0], dtype=dtypes
                        )
                    else:
                        group.record = None
                    mdf._set_temporary_master(mdf.get_master(i, data=fragment))
                    if idx == 0:
                        signals = []
                        for j in included_channels:
                            sig = mdf.get(
                                group=i,
                                index=j,
                                data=fragment,
                                raw=True,
                                ignore_invalidation_bits=True,
                            )

                            if version < "4.00":
                                if sig.samples.dtype.kind == "S":
                                    encodings.append(sig.encoding)
                                    strsig = mdf.get(
                                        group=i,
                                        index=j,
                                        samples_only=True,
                                        ignore_invalidation_bits=True,
                                    )[0]
                                    sig.samples = sig.samples.astype(strsig.dtype)
                                    del strsig
                                    if sig.encoding != "latin-1":

                                        if sig.encoding == "utf-16-le":
                                            sig.samples = (
                                                sig.samples.view(np.uint16)
                                                .byteswap()
                                                .view(sig.samples.dtype)
                                            )
                                            sig.samples = encode(
                                                decode(sig.samples, "utf-16-be"),
                                                "latin-1",
                                            )
                                        else:
                                            sig.samples = encode(
                                                decode(sig.samples, sig.encoding),
                                                "latin-1",
                                            )
                                else:
                                    encodings.append(None)

                            if not sig.samples.flags.writeable:
                                sig.samples = sig.samples.copy()
                            signals.append(sig)

                        if signals:
                            if sync:
                                timestamps = signals[0].timestamps + offset
                                for sig in signals:
                                    sig.timestamps = timestamps
                            stacked.append(signals, common_timebase=True)
                            try:
                                if group.channel_group.flags & v4c.FLAG_CG_BUS_EVENT:
                                    stacked.groups[
                                        -1
                                    ].channel_group.flags = group.channel_group.flags
                                    stacked.groups[
                                        -1
                                    ].channel_group.acq_name = (
                                        group.channel_group.acq_name
                                    )
                                    stacked.groups[
                                        -1
                                    ].channel_group.acq_source = (
                                        group.channel_group.acq_source
                                    )
                                    stacked.groups[
                                        -1
                                    ].channel_group.comment = (
                                        group.channel_group.comment
                                    )
                            except AttributeError:
                                pass
                        idx += 1
                    else:
                        master = mdf.get_master(i, fragment)
                        if sync:
                            master = master + offset
                        if len(master):

                            signals = [(master, None)]

                            for k, j in enumerate(included_channels):
                                sig = mdf.get(
                                    group=i,
                                    index=j,
                                    data=fragment,
                                    raw=True,
                                    samples_only=True,
                                    ignore_invalidation_bits=True,
                                )
                                signals.append(sig)

                                if version < "4.00":
                                    encoding = encodings[k]
                                    samples = sig[0]
                                    if encoding:
                                        if encoding != "latin-1":

                                            if encoding == "utf-16-le":
                                                samples = (
                                                    samples.view(np.uint16)
                                                    .byteswap()
                                                    .view(samples.dtype)
                                                )
                                                samples = encode(
                                                    decode(samples, "utf-16-be"),
                                                    "latin-1",
                                                )
                                            else:
                                                samples = encode(
                                                    decode(samples, encoding), "latin-1"
                                                )
                                            sig.samples = samples

                            if signals:
                                stacked.extend(cg_nr, signals)
                        idx += 1

                    group.record = None
                    mdf._set_temporary_master(None)

                stacked.groups[
                    -1
                ].channel_group.comment = (
                    f'stacked from channel group {i} of "{mdf.name.parent}"'
                )

            if callback:
                callback(mdf_index, files_nr)

            mdf.configure(copy_on_get=True)

            if not input_types[mdf_index]:
                mdf.close()

            if MDF._terminate:
                return

        return stacked

    def iter_channels(self, skip_master=True, copy_master=True):
        """ generator that yields a *Signal* for each non-master channel

        Parameters
        ----------
        skip_master : bool
            do not yield master channels; default *True*
        copy_master : bool
            copy master for each yielded channel

        """

        self._link_attributes()

        for i, group in enumerate(self.groups):

            included_channels = self._included_channels(i, skip_master=skip_master)

            channels = [(None, i, idx) for idx in included_channels]

            channels = self.select(channels, copy_master=copy_master,)

            for channel in channels:
                yield channel

    def iter_groups(self):
        """ generator that yields channel groups as pandas DataFrames. If there
        are multiple occurences for the same channel name inside a channel
        group, then a counter will be used to make the names unique
        (<original_name>_<counter>)

        """

        self._link_attributes()

        for i, _ in enumerate(self.groups):
            yield self.get_group(i)

    def resample(self, raster, version=None, time_from_zero=False):
        """ resample all channels using the given raster. See *configure* to select
        the interpolation method for interger channels

        Parameters
        ----------
        raster : float | np.array | str
            new raster that can be

            * a float step value
            * a channel name who's timestamps will be used as raster (starting with asammdf 5.5.0)
            * an array (starting with asammdf 5.5.0)

        version : str
            new mdf file version from ('2.00', '2.10', '2.14', '3.00', '3.10',
            '3.20', '3.30', '4.00', '4.10', '4.11'); default *None* and in this
            case the original file version is used

        time_from_zero : bool
            start time stamps from 0s in the cut measurement

        Returns
        -------
        mdf : MDF
            new *MDF* with resampled channels

        Examples
        --------
        >>> from asammdf import MDF, Signal
        >>> import numpy as np
        >>> mdf = MDF()
        >>> sig = Signal(name='S1', samples=[1,2,3,4], timestamps=[1,2,3,4])
        >>> mdf.append(sig)
        >>> sig = Signal(name='S2', samples=[1,2,3,4], timestamps=[1.1, 3.5, 3.7, 3.9])
        >>> mdf.append(sig)
        >>> resampled = mdf.resample(raster=0.1)
        >>> resampled.select(['S1', 'S2'])
        [<Signal S1:
                samples=[1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 4]
                timestamps=[1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7
         2.8 2.9 3.  3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 4. ]
                invalidation_bits=None
                unit=""
                conversion=None
                source=SignalSource(name='Python', path='Python', comment='', source_type=4, bus_type=0)
                comment=""
                mastermeta="('time', 1)"
                raw=True
                display_name=
                attachment=()>
        , <Signal S2:
                samples=[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 3 3 4 4]
                timestamps=[1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7
         2.8 2.9 3.  3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 4. ]
                invalidation_bits=None
                unit=""
                conversion=None
                source=SignalSource(name='Python', path='Python', comment='', source_type=4, bus_type=0)
                comment=""
                mastermeta="('time', 1)"
                raw=True
                display_name=
                attachment=()>
        ]
        >>> resampled = mdf.resample(raster='S2')
        >>> resampled.select(['S1', 'S2'])
        [<Signal S1:
                samples=[1 3 3 3]
                timestamps=[1.1 3.5 3.7 3.9]
                invalidation_bits=None
                unit=""
                conversion=None
                source=SignalSource(name='Python', path='Python', comment='', source_type=4, bus_type=0)
                comment=""
                mastermeta="('time', 1)"
                raw=True
                display_name=
                attachment=()>
        , <Signal S2:
                samples=[1 2 3 4]
                timestamps=[1.1 3.5 3.7 3.9]
                invalidation_bits=None
                unit=""
                conversion=None
                source=SignalSource(name='Python', path='Python', comment='', source_type=4, bus_type=0)
                comment=""
                mastermeta="('time', 1)"
                raw=True
                display_name=
                attachment=()>
        ]
        >>> resampled = mdf.resample(raster=[1.9, 2.0, 2.1])
        >>> resampled.select(['S1', 'S2'])
        [<Signal S1:
                samples=[1 2 2]
                timestamps=[1.9 2.  2.1]
                invalidation_bits=None
                unit=""
                conversion=None
                source=SignalSource(name='Python', path='Python', comment='', source_type=4, bus_type=0)
                comment=""
                mastermeta="('time', 1)"
                raw=True
                display_name=
                attachment=()>
        , <Signal S2:
                samples=[1 1 1]
                timestamps=[1.9 2.  2.1]
                invalidation_bits=None
                unit=""
                conversion=None
                source=SignalSource(name='Python', path='Python', comment='', source_type=4, bus_type=0)
                comment=""
                mastermeta="('time', 1)"
                raw=True
                display_name=
                attachment=()>
        ]
        >>> resampled = mdf.resample(raster='S2', time_from_zero=True)
        >>> resampled.select(['S1', 'S2'])
        [<Signal S1:
                samples=[1 3 3 3]
                timestamps=[0.  2.4 2.6 2.8]
                invalidation_bits=None
                unit=""
                conversion=None
                source=SignalSource(name='Python', path='Python', comment='', source_type=4, bus_type=0)
                comment=""
                mastermeta="('time', 1)"
                raw=True
                display_name=
                attachment=()>
        , <Signal S2:
                samples=[1 2 3 4]
                timestamps=[0.  2.4 2.6 2.8]
                invalidation_bits=None
                unit=""
                conversion=None
                source=SignalSource(name='Python', path='Python', comment='', source_type=4, bus_type=0)
                comment=""
                mastermeta="('time', 1)"
                raw=True
                display_name=
                attachment=()>
        ]
        """

        self._link_attributes()

        if version is None:
            version = self.version
        else:
            version = validate_version_argument(version)

        interpolation_mode = self._integer_interpolation

        mdf = MDF(version=version)

        mdf.header.start_time = self.header.start_time

        groups_nr = len(self.groups)

        if self._callback:
            self._callback(0, groups_nr)

        try:
            raster = float(raster)
            assert raster > 0
        except (TypeError, ValueError):
            if isinstance(raster, str):
                raster = self.get(raster).timestamps
            else:
                raster = np.array(raster)
        else:
            raster = master_using_raster(self, raster)

        if time_from_zero and len(raster):
            delta = raster[0]
            new_raster = raster - delta
            t_epoch = self.header.start_time.timestamp() + delta
            mdf.header.start_time = datetime.fromtimestamp(t_epoch)
        else:
            delta = 0
            new_raster = None
            mdf.header.start_time = self.header.start_time

        for i, group in enumerate(self.groups):
            included_channels = self._included_channels(i)
            channels = [(None, i, idx) for idx in included_channels]
            sigs = self.select(channels, raw=True,)
            sigs = [
                sig.interp(raster, interpolation_mode=interpolation_mode)
                for sig in sigs
            ]

            if new_raster is not None:
                for sig in sigs:
                    sig.timestamps = new_raster

            mdf.append(sigs, common_timebase=True)
            try:
                if group.channel_group.flags & v4c.FLAG_CG_BUS_EVENT:
                    mdf.groups[-1].channel_group.flags = group.channel_group.flags
                    mdf.groups[-1].channel_group.acq_name = group.channel_group.acq_name
                    mdf.groups[
                        -1
                    ].channel_group.acq_source = group.channel_group.acq_source
                    mdf.groups[-1].channel_group.comment = group.channel_group.comment
            except AttributeError:
                pass

            if self._callback:
                self._callback(i + 1, groups_nr)

            if self._terminate:
                return

        if self._callback:
            self._callback(groups_nr, groups_nr)

        mdf._transfer_events(self)
        if self._callback:
            mdf._callback = mdf._mdf._callback = self._callback
        return mdf

    def select(
        self,
        channels,
        record_offset=0,
        raw=False,
        copy_master=True,
        ignore_value2text_conversions=False,
        record_count=None,
    ):
        """ retrieve the channels listed in *channels* argument as *Signal*
        objects

        .. note:: the *dataframe* argument was removed in version 5.8.0
                  use the ``to_dataframe`` method instead

        Parameters
        ----------
        channels : list
            list of items to be filtered; each item can be :

                * a channel name string
                * (channel name, group index, channel index) list or tuple
                * (channel name, group index) list or tuple
                * (None, group index, channel index) list or tuple

        record_offset : int
            record number offset; optimization to get the last part of signal samples
        raw : bool
            get raw channel samples; default *False*
        copy_master : bool
            option to get a new timestamps array for each selected Signal or to
            use a shared array for channels of the same channel group; default *True*
        ignore_value2text_conversions (False) : bool
            valid only for the channels that have value to text conversions and
            if *raw=False*. If this is True then the raw numeric values will be
            used, and the conversion will not be applied.

            .. versionadded:: 5.8.0

        Returns
        -------
        signals : list
            list of *Signal* objects based on the input channel list

        Examples
        --------
        >>> from asammdf import MDF, Signal
        >>> import numpy as np
        >>> t = np.arange(5)
        >>> s = np.ones(5)
        >>> mdf = MDF()
        >>> for i in range(4):
        ...     sigs = [Signal(s*(i*10+j), t, name='SIG') for j in range(1,4)]
        ...     mdf.append(sigs)
        ...
        >>> # select SIG group 0 default index 1 default, SIG group 3 index 1, SIG group 2 index 1 default and channel index 2 from group 1
        ...
        >>> mdf.select(['SIG', ('SIG', 3, 1), ['SIG', 2],  (None, 1, 2)])
        [<Signal SIG:
                samples=[ 1.  1.  1.  1.  1.]
                timestamps=[0 1 2 3 4]
                unit=""
                info=None
                comment="">
        , <Signal SIG:
                samples=[ 31.  31.  31.  31.  31.]
                timestamps=[0 1 2 3 4]
                unit=""
                info=None
                comment="">
        , <Signal SIG:
                samples=[ 21.  21.  21.  21.  21.]
                timestamps=[0 1 2 3 4]
                unit=""
                info=None
                comment="">
        , <Signal SIG:
                samples=[ 12.  12.  12.  12.  12.]
                timestamps=[0 1 2 3 4]
                unit=""
                info=None
                comment="">
        ]

        """

        self._link_attributes()

        # group channels by group index
        gps = {}

        indexes = []

        for item in channels:
            if isinstance(item, (list, tuple)):
                if len(item) not in (2, 3):
                    raise MdfException(
                        "The items used for filtering must be strings, "
                        "or they must match the first 3 argumens of the get "
                        "method"
                    )
                else:
                    group, index = self._validate_channel_selection(*item)
                    indexes.append((group, index))
                    if group not in gps:
                        gps[group] = {index}
                    else:
                        gps[group].add(index)
            else:
                name = item
                group, index = self._validate_channel_selection(name)

                indexes.append((group, index))
                if group not in gps:
                    gps[group] = {index}
                else:
                    gps[group].add(index)

        output_signals = {}

        for group in gps:
            grp = self.groups[group]
            data = self._load_data(
                grp, record_offset=record_offset, record_count=record_count
            )
            parents, dtypes = self._prepare_record(grp)

            channel_indexes = list(gps[group])

            if record_count is None:
                cycles = grp.channel_group.cycles_nr - record_offset
            else:
                if grp.channel_group.cycles_nr < record_count + record_offset:
                    cycles = grp.channel_group.cycles_nr - record_offset
                else:
                    cycles = record_count

            signals = []
            invalidation_bits = []

            sigs = []

            current_pos = 0

            for i, fragment in enumerate(data):

                if dtypes.itemsize:
                    # TODO: optimize for channel groups with a single channel
                    # and LDBLOCK (records 6us; array 0.5us)
                    grp.record = np.core.records.fromstring(fragment[0], dtype=dtypes)
                else:
                    grp.record = None

                self._set_temporary_master(None)
                self._set_temporary_master(self.get_master(group, data=fragment))

                if i == 0:
                    for index in channel_indexes:
                        signal = self.get(
                            group=group,
                            index=index,
                            data=fragment,
                            raw=True,
                            ignore_invalidation_bits=True,
                        )

                        sigs.append(signal)

                    next_pos = current_pos + len(sigs[0])

                    master = np.empty(cycles, dtype=sigs[0].timestamps.dtype)

                    master[current_pos:next_pos] = sigs[0].timestamps

                    for sig in sigs:
                        shape = (cycles,) + sig.samples.shape[1:]
                        signal = np.empty(shape, dtype=sig.samples.dtype)
                        signals.append(signal)
                        signal[current_pos:next_pos] = sig.samples

                        if sig.invalidation_bits is not None:
                            inval = np.empty(cycles, dtype=sig.invalidation_bits.dtype)
                            invalidation_bits.append(inval)
                            inval[current_pos:next_pos] = sig.invalidation_bits
                        else:
                            invalidation_bits.append(None)

                else:
                    next_pos = current_pos + len(self._mdf._master)

                    master[current_pos:next_pos] = self._mdf._master

                    for signal, inval, index in zip(
                        signals, invalidation_bits, channel_indexes
                    ):
                        sig = self.get(
                            group=group,
                            index=index,
                            data=fragment,
                            raw=True,
                            samples_only=True,
                            ignore_invalidation_bits=True,
                        )

                        signal[current_pos:next_pos] = sig[0]
                        if inval is not None:
                            inval[current_pos:next_pos] = sig[1]

                current_pos = next_pos

                grp.record = None
                self._set_temporary_master(None)

            for signal, inval, index, sig in zip(
                signals, invalidation_bits, channel_indexes, sigs
            ):
                pair = group, index

                output_signals[pair] = Signal(
                    samples=signal,
                    timestamps=master,
                    name=sig.name,
                    unit=sig.unit,
                    bit_count=sig.bit_count,
                    attachment=sig.attachment,
                    comment=sig.comment,
                    conversion=sig.conversion,
                    display_name=sig.display_name,
                    encoding=sig.encoding,
                    master_metadata=sig.master_metadata,
                    raw=True,
                    source=sig.source,
                    stream_sync=sig.stream_sync,
                    invalidation_bits=inval,
                )

        signals = [output_signals[pair] for pair in indexes]

        if copy_master:
            for signal in signals:
                signal.timestamps = signal.timestamps.copy()

        if not raw:
            if ignore_value2text_conversions:
                if self.version < "4.00":
                    text_conversion = 11
                else:
                    text_conversion = 7
                for signal in signals:
                    conversion = signal.conversion
                    if conversion and conversion.conversion_type < text_conversion:
                        signal.samples = conversion.convert(signal.samples)
                    signal.raw = False
                    signal.conversion = None
            else:
                for signal in signals:
                    conversion = signal.conversion
                    if conversion:
                        signal.samples = conversion.convert(signal.samples)
                    signal.raw = False
                    signal.conversion = None

        return signals

    def whereis(self, channel):
        """ get ocurrences of channel name in the file

        Parameters
        ----------
        channel : str
            channel name string

        Returns
        -------
        ocurrences : tuple


        Examples
        --------
        >>> mdf = MDF(file_name)
        >>> mdf.whereis('VehicleSpeed') # "VehicleSpeed" exists in the file
        ((1, 2), (2, 4))
        >>> mdf.whereis('VehicleSPD') # "VehicleSPD" doesn't exist in the file
        ()

        """
        self._link_attributes()

        if channel in self:
            return tuple(self.channels_db[channel])
        else:
            return tuple()

    @staticmethod
    def scramble(name, skip_attachments=False, **kwargs):
        """ scramble text blocks and keep original file structure

        Parameters
        ----------
        name : str | pathlib.Path
            file name
        skip_attachments : bool
            skip scrambling of attachments data if True

            .. versionadded:: 5.9.0

        Returns
        -------
        name : str
            scrambled file name

        """

        name = Path(name)

        mdf = MDF(name)
        texts = {}

        callback = kwargs.get("callback", None)
        if callback:
            callback(0, 100)

        count = len(mdf.groups)

        if mdf.version >= "4.00":
            ChannelConversion = ChannelConversionV4

            stream = mdf._file

            if mdf.header.comment_addr:
                stream.seek(mdf.header.comment_addr + 8)
                size = UINT64_u(stream.read(8))[0] - 24
                texts[mdf.header.comment_addr] = randomized_string(size)

            for fh in mdf.file_history:
                addr = fh.comment_addr
                if addr and addr not in texts:
                    stream.seek(addr + 8)
                    size = UINT64_u(stream.read(8))[0] - 24
                    texts[addr] = randomized_string(size)

            for ev in mdf.events:
                for addr in (ev.comment_addr, ev.name_addr):
                    if addr and addr not in texts:
                        stream.seek(addr + 8)
                        size = UINT64_u(stream.read(8))[0] - 24
                        texts[addr] = randomized_string(size)

            for at in mdf.attachments:
                for addr in (at.comment_addr, at.file_name_addr):
                    if addr and addr not in texts:
                        stream.seek(addr + 8)
                        size = UINT64_u(stream.read(8))[0] - 24
                        texts[addr] = randomized_string(size)
                if not skip_attachments and at.embedded_data:
                    texts[at.address + v4c.AT_COMMON_SIZE] = randomized_string(
                        at.embedded_size
                    )

            for idx, gp in enumerate(mdf.groups, 1):

                addr = gp.data_group.comment_addr
                if addr and addr not in texts:
                    stream.seek(addr + 8)
                    size = UINT64_u(stream.read(8))[0] - 24
                    texts[addr] = randomized_string(size)

                cg = gp.channel_group
                for addr in (cg.acq_name_addr, cg.comment_addr):
                    if cg.flags & v4c.FLAG_CG_BUS_EVENT:
                        continue

                    if addr and addr not in texts:
                        stream.seek(addr + 8)
                        size = UINT64_u(stream.read(8))[0] - 24
                        texts[addr] = randomized_string(size)

                    source = cg.acq_source_addr
                    if source:
                        source = SourceInformation(address=source, stream=stream)
                        for addr in (
                            source.name_addr,
                            source.path_addr,
                            source.comment_addr,
                        ):
                            if addr and addr not in texts:
                                stream.seek(addr + 8)
                                size = UINT64_u(stream.read(8))[0] - 24
                                texts[addr] = randomized_string(size)

                for ch in gp.channels:

                    for addr in (ch.name_addr, ch.unit_addr, ch.comment_addr):
                        if addr and addr not in texts:
                            stream.seek(addr + 8)
                            size = UINT64_u(stream.read(8))[0] - 24
                            texts[addr] = randomized_string(size)

                    source = ch.source_addr
                    if source:
                        source = SourceInformation(address=source, stream=stream)
                        for addr in (
                            source.name_addr,
                            source.path_addr,
                            source.comment_addr,
                        ):
                            if addr and addr not in texts:
                                stream.seek(addr + 8)
                                size = UINT64_u(stream.read(8))[0] - 24
                                texts[addr] = randomized_string(size)

                    conv = ch.conversion_addr
                    if conv:
                        conv = ChannelConversion(address=conv, stream=stream)
                        for addr in (conv.name_addr, conv.unit_addr, conv.comment_addr):
                            if addr and addr not in texts:
                                stream.seek(addr + 8)
                                size = UINT64_u(stream.read(8))[0] - 24
                                texts[addr] = randomized_string(size)
                        if conv.conversion_type == v4c.CONVERSION_TYPE_ALG:
                            addr = conv.formula_addr
                            if addr and addr not in texts:
                                stream.seek(addr + 8)
                                size = UINT64_u(stream.read(8))[0] - 24
                                texts[addr] = randomized_string(size)

                        if conv.referenced_blocks:
                            for key, block in conv.referenced_blocks.items():
                                if block:
                                    if isinstance(block, bytes):
                                        addr = conv[key]
                                        if addr not in texts:
                                            stream.seek(addr + 8)
                                            size = len(block)
                                            texts[addr] = randomized_string(size)

                if callback:
                    callback(int(idx / count * 66), 100)

            mdf.close()

            dst = name.with_suffix(".scrambled.mf4")

            copy(name, dst)

            with open(dst, "rb+") as mdf:
                count = len(texts)
                chunk = max(count // 34, 1)
                idx = 0
                for index, (addr, bts) in enumerate(texts.items()):
                    mdf.seek(addr + 24)
                    mdf.write(bts)
                    if index % chunk == 0:
                        if callback:
                            callback(66 + idx, 100)

            if callback:
                callback(100, 100)

        else:
            ChannelConversion = ChannelConversionV3

            stream = mdf._file

            if mdf.header.comment_addr:
                stream.seek(mdf.header.comment_addr + 2)
                size = UINT16_u(stream.read(2))[0] - 4
                texts[mdf.header.comment_addr + 4] = randomized_string(size)
            texts[36 + 0x40] = randomized_string(32)
            texts[68 + 0x40] = randomized_string(32)
            texts[100 + 0x40] = randomized_string(32)
            texts[132 + 0x40] = randomized_string(32)

            for idx, gp in enumerate(mdf.groups, 1):

                cg = gp.channel_group
                addr = cg.comment_addr

                if addr and addr not in texts:
                    stream.seek(addr + 2)
                    size = UINT16_u(stream.read(2))[0] - 4
                    texts[addr + 4] = randomized_string(size)

                if gp.trigger:
                    addr = gp.trigger.text_addr
                    if addr:
                        stream.seek(addr + 2)
                        size = UINT16_u(stream.read(2))[0] - 4
                        texts[addr + 4] = randomized_string(size)

                for ch in gp.channels:

                    for key in ("long_name_addr", "display_name_addr", "comment_addr"):
                        if hasattr(ch, key):
                            addr = getattr(ch, key)
                        else:
                            addr = 0
                        if addr and addr not in texts:
                            stream.seek(addr + 2)
                            size = UINT16_u(stream.read(2))[0] - 4
                            texts[addr + 4] = randomized_string(size)

                    texts[ch.address + 26] = randomized_string(32)
                    texts[ch.address + 58] = randomized_string(128)

                    source = ch.source_addr
                    if source:
                        source = ChannelExtension(address=source, stream=stream)
                        if source.type == v23c.SOURCE_ECU:
                            texts[source.address + 12] = randomized_string(80)
                            texts[source.address + 92] = randomized_string(32)
                        else:
                            texts[source.address + 14] = randomized_string(36)
                            texts[source.address + 50] = randomized_string(36)

                    conv = ch.conversion_addr
                    if conv:
                        texts[conv + 22] = randomized_string(20)

                        conv = ChannelConversion(address=conv, stream=stream)

                        if conv.conversion_type == v23c.CONVERSION_TYPE_FORMULA:
                            texts[conv + 36] = randomized_string(conv.block_len - 36)

                        if conv.referenced_blocks:
                            for key, block in conv.referenced_blocks.items():
                                if block:
                                    if isinstance(block, bytes):
                                        addr = conv[key]
                                        if addr and addr not in texts:
                                            stream.seek(addr + 2)
                                            size = UINT16_u(stream.read(2))[0] - 4
                                            texts[addr + 4] = randomized_string(size)
                if callback:
                    callback(int(idx / count * 66), 100)

            mdf.close()

            dst = name.with_suffix(".scrambled.mf4")

            copy(name, dst)

            with open(dst, "rb+") as mdf:
                chunk = count // 34
                idx = 0
                for index, (addr, bts) in enumerate(texts.items()):
                    mdf.seek(addr)
                    mdf.write(bts)
                    if chunk and index % chunk == 0:
                        if callback:
                            callback(66 + idx, 100)

            if callback:
                callback(100, 100)

        return dst

    def get_group(
        self,
        index,
        channels=None,
        raster=None,
        time_from_zero=True,
        empty_channels="skip",
        keep_arrays=False,
        use_display_names=False,
        time_as_date=False,
        reduce_memory_usage=False,
        raw=False,
        ignore_value2text_conversions=False,
        only_basenames=False,
    ):
        """ get channel group as pandas DataFrames. If there are multiple
        occurences for the same channel name, then a counter will be used to
        make the names unique (<original_name>_<counter>)

        Parameters
        ----------
        index : int
            channel group index
        use_display_names : bool
            use display name instead of standard channel name, if available.
        reduce_memory_usage : bool
            reduce memory usage by converting all float columns to float32 and
            searching for minimum dtype that can reprezent the values found
            in integer columns; default *False*
        raw (False) : bool
            the dataframe will contain the raw channel values

            .. versionadded:: 5.7.0

        ignore_value2text_conversions (False) : bool
            valid only for the channels that have value to text conversions and
            if *raw=False*. If this is True then the raw numeric values will be
            used, and the conversion will not be applied.

            .. versionadded:: 5.8.0

        keep_arrays (False) : bool
            keep arrays and structure channels as well as the
            component channels. If *True* this can be very slow. If *False*
            only the component channels are saved, and their names will be
            prefixed with the parent channel.

            .. versionadded:: 5.8.0

        empty_channels ("skip") : str
            behaviour for channels without samples; the options are *skip* or
            *zeros*; default is *skip*

            .. versionadded:: 5.8.0

        only_basenames (False) : bool
            use jsut the field names, without prefix, for structures and channel
            arrays

            .. versionadded:: 5.13.0

        Returns
        -------
        df : pandas.DataFrame

        """

        self._link_attributes()

        included_channels = self._included_channels(index)

        channels = [(None, index, ch_index) for ch_index in included_channels]

        return self.to_dataframe(
            channels=channels,
            raster=raster,
            time_from_zero=time_from_zero,
            empty_channels="skip",
            keep_arrays=False,
            use_display_names=use_display_names,
            time_as_date=time_as_date,
            reduce_memory_usage=reduce_memory_usage,
            raw=raw,
            ignore_value2text_conversions=ignore_value2text_conversions,
            only_basenames=only_basenames,
        )

    def iter_to_dataframe(
        self,
        channels=None,
        raster=None,
        time_from_zero=True,
        empty_channels="skip",
        keep_arrays=False,
        use_display_names=False,
        time_as_date=False,
        reduce_memory_usage=False,
        raw=False,
        ignore_value2text_conversions=False,
        use_interpolation=True,
        only_basenames=False,
        chunk_ram_size=200 * 1024 * 1024,
        interpolate_outwards_with_nan=False,
    ):
        """ generator that yields pandas DataFrame's that should not exceed
        200MB of RAM

        .. versionadded:: 5.15.0

        Parameters
        ----------
        channels : list
            filter a subset of channels; default *None*
        raster : float | np.array | str
            new raster that can be

            * a float step value
            * a channel name who's timestamps will be used as raster (starting with asammdf 5.5.0)
            * an array (starting with asammdf 5.5.0)

            see `resample` for examples of urisng this argument

        time_from_zero : bool
            adjust time channel to start from 0; default *True*
        empty_channels : str
            behaviour for channels without samples; the options are *skip* or
            *zeros*; default is *skip*
        use_display_names : bool
            use display name instead of standard channel name, if available.
        keep_arrays : bool
            keep arrays and structure channels as well as the
            component channels. If *True* this can be very slow. If *False*
            only the component channels are saved, and their names will be
            prefixed with the parent channel.
        time_as_date : bool
            the dataframe index will contain the datetime timestamps
            according to the measurement start time; default *False*. If
            *True* then the argument ``time_from_zero`` will be ignored.
        reduce_memory_usage : bool
            reduce memory usage by converting all float columns to float32 and
            searching for minimum dtype that can reprezent the values found
            in integer columns; default *False*
        raw (False) : bool
            the columns will contain the raw values
        ignore_value2text_conversions (False) : bool
            valid only for the channels that have value to text conversions and
            if *raw=False*. If this is True then the raw numeric values will be
            used, and the conversion will not be applied.
        use_interpolation (True) : bool
            option to perform interpoaltions when multiple timestamp raster are
            present. If *False* then dataframe columns will be automatically
            filled with NaN's were the dataframe index values are not found in
            the current column's timestamps
        only_basenames (False) : bool
            use jsut the field names, without prefix, for structures and channel
            arrays
        interpolate_outwards_with_nan : bool
            use NaN values for the samples that lie outside of the original
            signal's timestamps
        chunk_ram_size : int
            desired data frame RAM usage in bytes; default 200 MB


        Returns
        -------
        dataframe : pandas.DataFrame
            yields pandas DataFrame's that should not exceed 200MB of RAM

        """

        self._link_attributes()

        if channels:
            mdf = self.filter(channels)

            result = mdf.iter_to_dataframe(
                raster=raster,
                time_from_zero=time_from_zero,
                empty_channels=empty_channels,
                keep_arrays=keep_arrays,
                use_display_names=use_display_names,
                time_as_date=time_as_date,
                reduce_memory_usage=reduce_memory_usage,
                raw=raw,
                ignore_value2text_conversions=ignore_value2text_conversions,
                use_interpolation=use_interpolation,
                only_basenames=only_basenames,
                chunk_ram_size=chunk_ram_size,
            )

            for df in result:
                yield df

            mdf.close()

        df = pd.DataFrame()
        self._set_temporary_master(None)

        if raster:
            try:
                raster = float(raster)
                assert raster > 0
            except (TypeError, ValueError):
                if isinstance(raster, str):
                    raster = self.get(raster).timestamps
                else:
                    raster = np.array(raster)
            else:
                raster = master_using_raster(self, raster)
            master = raster
        else:
            masters = [self.get_master(i) for i, _ in enumerate(self.groups)]

            if masters:
                master = reduce(np.union1d, masters)
            else:
                master = np.array([], dtype="<f4")

        master_ = master
        channel_count = sum(len(gp.channels) - 1 for gp in self.groups) + 1
        # approximation with all float64 dtype
        itemsize = channel_count * 8
        # use 200MB DataFrame chunks
        chunk_count = chunk_ram_size // itemsize or 1

        chunks, r = divmod(len(master), chunk_count)
        if r:
            chunks += 1

        for i in range(chunks):

            master = master_[chunk_count * i : chunk_count * (i + 1)]
            start = master[0]
            end = master[-1]

            df = pd.DataFrame()
            self._set_temporary_master(None)

            df["timestamps"] = pd.Series(master, index=np.arange(len(master)))
            df.set_index("timestamps", inplace=True)

            used_names = UniqueDB()
            used_names.get_unique_name("timestamps")

            groups_nr = len(self.groups)

            for group_index, grp in enumerate(self.groups):
                group_cycles = grp.channel_group.cycles_nr
                if group_cycles == 0 and empty_channels == "skip":
                    continue

                record_offset = max(
                    np.searchsorted(masters[group_index], start).flatten()[0] - 1, 0
                )
                stop = np.searchsorted(masters[group_index], end).flatten()[0]
                record_count = min(stop - record_offset + 1, group_cycles)

                included_channels = [
                    (None, group_index, channel_index)
                    for channel_index in self._included_channels(group_index)
                ]

                signals = [
                    signal.validate(copy=False)
                    for signal in self.select(
                        included_channels,
                        raw=True,
                        copy_master=False,
                        record_offset=record_offset,
                        record_count=record_count,
                    )
                ]

                if not signals:
                    continue

                for sig in signals:
                    if len(sig) == 0:
                        if empty_channels == "zeros":
                            sig.samples = np.zeros(
                                len(df.index), dtype=sig.samples.dtype
                            )
                            sig.timestamps = master
                        else:
                            continue

                if not raw:
                    if ignore_value2text_conversions:
                        if self.version < "4.00":
                            text_conversion = 11
                        else:
                            text_conversion = 7

                        for signal in signals:
                            conversion = signal.conversion
                            if (
                                conversion
                                and conversion.conversion_type < text_conversion
                            ):
                                signal.samples = conversion.convert(signal.samples)

                    else:
                        for signal in signals:
                            if signal.conversion:
                                signal.samples = signal.conversion.convert(
                                    signal.samples
                                )

                if use_interpolation and not np.array_equal(
                    master, signals[0].timestamps
                ):

                    if interpolate_outwards_with_nan:
                        timestamps = signals[0].timestamps
                        idx = np.argwhere(
                            (master >= timestamps[0]) & (master <= timestamps[-1])
                        ).flatten()

                    signals = [
                        signal.interp(master, self._integer_interpolation)
                        for signal in signals
                    ]

                    if interpolate_outwards_with_nan:
                        for sig in signals:
                            sig.timestamps = sig.timestamps[idx]
                            sig.samples = sig.samples[idx]

                signals = [sig for sig in signals if len(sig)]

                for k, sig in enumerate(signals):
                    # byte arrays
                    if len(sig.samples.shape) > 1:

                        if use_display_names:
                            channel_name = sig.display_name or sig.name
                        else:
                            channel_name = sig.name

                        channel_name = used_names.get_unique_name(channel_name)

                        df[channel_name] = pd.Series(
                            list(sig.samples), index=sig.timestamps,
                        )

                    # arrays and structures
                    elif sig.samples.dtype.names:
                        for name, series in components(
                            sig.samples,
                            sig.name,
                            used_names,
                            master=sig.timestamps,
                            only_basenames=only_basenames,
                        ):
                            df[name] = series

                    # scalars
                    else:
                        if use_display_names:
                            channel_name = sig.display_name or sig.name
                        else:
                            channel_name = sig.name

                        channel_name = used_names.get_unique_name(channel_name)

                        if reduce_memory_usage and sig.samples.dtype.kind in "SU":
                            unique = np.unique(sig.samples)
                            if len(sig.samples) / len(unique) >= 2:
                                df[channel_name] = pd.Series(
                                    sig.samples, index=sig.timestamps, dtype="category"
                                )
                            else:
                                df[channel_name] = pd.Series(
                                    sig.samples, index=sig.timestamps
                                )
                        else:
                            if reduce_memory_usage:
                                sig.samples = downcast(sig.samples)
                            df[channel_name] = pd.Series(
                                sig.samples, index=sig.timestamps
                            )

                if self._callback:
                    self._callback(group_index + 1, groups_nr)

            if time_as_date:
                new_index = np.array(df.index) + self.header.start_time.timestamp()
                new_index = pd.to_datetime(new_index, unit="s")

                df.set_index(new_index, inplace=True)
            elif time_from_zero and len(master):
                df.set_index(df.index - df.index[0], inplace=True)

            yield df

    def to_dataframe(
        self,
        channels=None,
        raster=None,
        time_from_zero=True,
        empty_channels="skip",
        keep_arrays=False,
        use_display_names=False,
        time_as_date=False,
        reduce_memory_usage=False,
        raw=False,
        ignore_value2text_conversions=False,
        use_interpolation=True,
        only_basenames=False,
        interpolate_outwards_with_nan=False,
    ):
        """ generate pandas DataFrame

        Parameters
        ----------
        channels : list
            filter a subset of channels; default *None*
        raster : float | np.array | str
            new raster that can be

            * a float step value
            * a channel name who's timestamps will be used as raster (starting with asammdf 5.5.0)
            * an array (starting with asammdf 5.5.0)

            see `resample` for examples of urisng this argument

        time_from_zero : bool
            adjust time channel to start from 0; default *True*
        empty_channels : str
            behaviour for channels without samples; the options are *skip* or
            *zeros*; default is *skip*
        use_display_names : bool
            use display name instead of standard channel name, if available.
        keep_arrays : bool
            keep arrays and structure channels as well as the
            component channels. If *True* this can be very slow. If *False*
            only the component channels are saved, and their names will be
            prefixed with the parent channel.
        time_as_date : bool
            the dataframe index will contain the datetime timestamps
            according to the measurement start time; default *False*. If
            *True* then the argument ``time_from_zero`` will be ignored.
        reduce_memory_usage : bool
            reduce memory usage by converting all float columns to float32 and
            searching for minimum dtype that can reprezent the values found
            in integer columns; default *False*
        raw (False) : bool
            the columns will contain the raw values

            .. versionadded:: 5.7.0

        ignore_value2text_conversions (False) : bool
            valid only for the channels that have value to text conversions and
            if *raw=False*. If this is True then the raw numeric values will be
            used, and the conversion will not be applied.

            .. versionadded:: 5.8.0

        use_interpolation (True) : bool
            option to perform interpoaltions when multiple timestamp raster are
            present. If *False* then dataframe columns will be automatically
            filled with NaN's were the dataframe index values are not found in
            the current column's timestamps

            .. versionadded:: 5.11.0

        only_basenames (False) : bool
            use jsut the field names, without prefix, for structures and channel
            arrays

            .. versionadded:: 5.13.0

        interpolate_outwards_with_nan : bool
            use NaN values for the samples that lie outside of the original
            signal's timestamps

            .. versionadded:: 5.15.0

        Returns
        -------
        dataframe : pandas.DataFrame

        """

        self._link_attributes()

        if channels:
            mdf = self.filter(channels)

            result = mdf.to_dataframe(
                raster=raster,
                time_from_zero=time_from_zero,
                empty_channels=empty_channels,
                keep_arrays=keep_arrays,
                use_display_names=use_display_names,
                time_as_date=time_as_date,
                reduce_memory_usage=reduce_memory_usage,
                raw=raw,
                ignore_value2text_conversions=ignore_value2text_conversions,
                use_interpolation=use_interpolation,
                only_basenames=only_basenames,
                interpolate_outwards_with_nan=interpolate_outwards_with_nan,
            )

            mdf.close()
            return result

        df = pd.DataFrame()
        self._set_temporary_master(None)

        if raster:
            try:
                raster = float(raster)
                assert raster > 0
            except (TypeError, ValueError):
                if isinstance(raster, str):
                    raster = self.get(raster).timestamps
                else:
                    raster = np.array(raster)
            else:
                raster = master_using_raster(self, raster)
            master = raster
        else:
            masters = [self.get_master(i) for i, _ in enumerate(self.groups)]

            if masters:
                master = reduce(np.union1d, masters)
            else:
                master = np.array([], dtype="<f4")

        df["timestamps"] = pd.Series(master, index=np.arange(len(master)))
        df.set_index("timestamps", inplace=True)

        used_names = UniqueDB()
        used_names.get_unique_name("timestamps")

        groups_nr = len(self.groups)

        for group_index, grp in enumerate(self.groups):
            if grp.channel_group.cycles_nr == 0 and empty_channels == "skip":
                continue

            included_channels = [
                (None, group_index, channel_index)
                for channel_index in self._included_channels(group_index)
            ]

            signals = [
                signal.validate(copy=False)
                for signal in self.select(
                    included_channels, raw=True, copy_master=False,
                )
            ]

            if not signals:
                continue

            for sig in signals:
                if len(sig) == 0:
                    if empty_channels == "zeros":
                        sig.samples = np.zeros(len(df.index), dtype=sig.samples.dtype)
                        sig.timestamps = master
                    else:
                        continue

            if not raw:
                if ignore_value2text_conversions:
                    if self.version < "4.00":
                        text_conversion = 11
                    else:
                        text_conversion = 7

                    for signal in signals:
                        conversion = signal.conversion
                        if conversion and conversion.conversion_type < text_conversion:
                            signal.samples = conversion.convert(signal.samples)

                else:
                    for signal in signals:
                        if signal.conversion:
                            signal.samples = signal.conversion.convert(signal.samples)

            if use_interpolation and not np.array_equal(master, signals[0].timestamps):

                if interpolate_outwards_with_nan:
                    timestamps = signals[0].timestamps
                    idx = np.argwhere(
                        (master >= timestamps[0]) & (master <= timestamps[-1])
                    ).flatten()

                signals = [
                    signal.interp(master, self._integer_interpolation)
                    for signal in signals
                ]

                if interpolate_outwards_with_nan:
                    for sig in signals:
                        sig.timestamps = sig.timestamps[idx]
                        sig.samples = sig.samples[idx]

            signals = [sig for sig in signals if len(sig)]

            for k, sig in enumerate(signals):
                # byte arrays
                if len(sig.samples.shape) > 1:

                    if use_display_names:
                        channel_name = sig.display_name or sig.name
                    else:
                        channel_name = sig.name

                    channel_name = used_names.get_unique_name(channel_name)

                    df[channel_name] = pd.Series(
                        list(sig.samples), index=sig.timestamps,
                    )

                # arrays and structures
                elif sig.samples.dtype.names:
                    for name, series in components(
                        sig.samples,
                        sig.name,
                        used_names,
                        master=sig.timestamps,
                        only_basenames=only_basenames,
                    ):
                        df[name] = series

                # scalars
                else:
                    if use_display_names:
                        channel_name = sig.display_name or sig.name
                    else:
                        channel_name = sig.name

                    channel_name = used_names.get_unique_name(channel_name)

                    if reduce_memory_usage and sig.samples.dtype.kind in "SU":
                        unique = np.unique(sig.samples)
                        if len(sig.samples) / len(unique) >= 2:
                            df[channel_name] = pd.Series(
                                sig.samples, index=sig.timestamps, dtype="category"
                            )
                        else:
                            df[channel_name] = pd.Series(
                                sig.samples, index=sig.timestamps
                            )
                    else:
                        if reduce_memory_usage:
                            sig.samples = downcast(sig.samples)
                        df[channel_name] = pd.Series(sig.samples, index=sig.timestamps)

            if self._callback:
                self._callback(group_index + 1, groups_nr)

        if time_as_date:
            new_index = np.array(df.index) + self.header.start_time.timestamp()
            new_index = pd.to_datetime(new_index, unit="s")

            df.set_index(new_index, inplace=True)
        elif time_from_zero and len(master):
            df.set_index(df.index - df.index[0], inplace=True)

        return df

    def extract_can_logging(
        self, dbc_files, version=None, ignore_invalid_signals=False
    ):
        """ extract all possible CAN signal using the provided databases.

        Parameters
        ----------
        dbc_files : iterable
            iterable of str or pathlib.Path objects
        version (None) : str
            output file version
        ignore_invalid_signals (False) : bool
            ignore signals that have all samples equal to their maximum value

            .. versionadded:: 5.7.0

        Returns
        -------
        mdf : MDF
            new MDF file that contains the succesfully extracted signals

        """
        self._link_attributes()

        if version is None:
            version = self.version
        else:
            version = validate_version_argument(version)

        out = MDF(version=version, callback=self._callback)
        out.header.start_time = self.header.start_time

        if self._callback:
            out._callback = out._mdf._callback = self._callback

        max_flags = {}

        valid_dbc_files = []
        for dbc_name in dbc_files:
            dbc = load_can_database(dbc_name)
            if dbc is None:
                continue
            else:
                valid_dbc_files.append((dbc, dbc_name))

        count = sum(1 for group in self.groups if group.CAN_logging)
        count *= len(valid_dbc_files)

        cntr = 0

        total_unique_ids = set()
        found_ids = defaultdict(set)
        not_found_ids = defaultdict(list)
        unknown_ids = defaultdict(list)

        for dbc, dbc_name in valid_dbc_files:
            is_j1939 = dbc.contains_j1939
            if is_j1939:
                messages = {message.arbitration_id.pgn: message for message in dbc}
            else:
                messages = {message.arbitration_id.id: message for message in dbc}

            current_not_found_ids = {
                (msg_id, message.name) for msg_id, message in messages.items()
            }

            msg_map = {}

            for i, group in enumerate(self.groups):
                if not group.CAN_logging:
                    continue

                if not "CAN_DataFrame" in [ch.name for ch in group.channels]:
                    continue

                parents, dtypes = self._prepare_record(group)
                data = self._load_data(group, optimize_read=False)

                for fragment_index, fragment in enumerate(data):
                    if dtypes.itemsize:
                        group.record = np.core.records.fromstring(
                            fragment[0], dtype=dtypes
                        )
                    else:
                        group.record = None
                        continue

                    self._set_temporary_master(None)
                    self._set_temporary_master(self.get_master(i, data=fragment))

                    bus_ids = self.get(
                        "CAN_DataFrame.BusChannel",
                        group=i,
                        data=fragment,
                        samples_only=True,
                    )[0].astype("<u1")

                    msg_ids = (
                        self.get("CAN_DataFrame.ID", group=i, data=fragment,)
                        & 0x1FFFFFFF
                    )

                    if is_j1939:
                        ps = (msg_ids.samples >> 8) & 0xFF
                        pf = (msg_ids.samples >> 16) & 0xFF
                        _pgn = pf << 8
                        msg_ids.samples = np.where(pf >= 240, _pgn + ps, _pgn,)

                    data_bytes = self.get(
                        "CAN_DataFrame.DataBytes",
                        group=i,
                        data=fragment,
                        samples_only=True,
                    )[0]

                    buses = np.unique(bus_ids)

                    for bus in buses:
                        idx = np.argwhere(bus_ids == bus).ravel()
                        bus_t = msg_ids.timestamps[idx]
                        bus_msg_ids = msg_ids.samples[idx]
                        bus_data_bytes = data_bytes[idx]

                        unique_ids = np.unique(bus_msg_ids).astype("<u8")

                        total_unique_ids = total_unique_ids | set(unique_ids)

                        for msg_id in unique_ids:
                            message = messages.get(msg_id, None)
                            if message is None:
                                unknown_ids[msg_id].append(True)
                                continue

                            found_ids[dbc_name].add((msg_id, message.name))
                            try:
                                current_not_found_ids.remove((msg_id, message.name))
                            except KeyError:
                                pass

                            unknown_ids[msg_id].append(False)

                            idx = np.argwhere(bus_msg_ids == msg_id).ravel()
                            payload = bus_data_bytes[idx]
                            t = bus_t[idx]

                            extracted_signals = extract_mux(
                                payload, message, msg_id, bus, t
                            )

                            for entry, signals in extracted_signals.items():
                                if entry not in msg_map:
                                    sigs = []

                                    index = len(out.groups)
                                    msg_map[entry] = index

                                    for name_, signal in signals.items():
                                        sig = Signal(
                                            samples=signal["samples"],
                                            timestamps=signal["t"],
                                            name=signal["name"],
                                            comment=signal["comment"],
                                            unit=signal["unit"],
                                        )
                                        sig.comment = f"""\
<CNcomment>
<TX>{sig.comment}</TX>
<names>
    <display>
        CAN{bus}.{message.name}.{signal['name']}
    </display>
</names>
</CNcomment>"""

                                        sigs.append(sig)

                                        max_flags_entry = index, name_

                                        if max_flags_entry in max_flags:
                                            max_flags[max_flags_entry] = (
                                                max_flags[max_flags_entry]
                                                and signal["is_max"]
                                            )
                                        else:
                                            max_flags[max_flags_entry] = signal[
                                                "is_max"
                                            ]

                                    out.append(
                                        sigs,
                                        f"from CAN{bus} message ID=0x{msg_id:X}",
                                        common_timebase=True,
                                    )

                                    out.groups[
                                        -1
                                    ].channel_group.comment = f"{message} 0x{msg_id:X}"

                                else:
                                    index = msg_map[entry]

                                    sigs = [(t, None)]

                                    for name_, signal in signals.items():

                                        sigs.append((signal["samples"], None))

                                        max_flags_entry = index, name_

                                        max_flags[max_flags_entry] = (
                                            max_flags[max_flags_entry]
                                            and signal["is_max"]
                                        )

                                    out.extend(index, sigs)
                    self._set_temporary_master(None)
                cntr += 1
                if self._callback:
                    self._callback(cntr, count)

            if current_not_found_ids:
                not_found_ids[dbc_name] = list(current_not_found_ids)

        unknown_ids = {
            msg_id for msg_id, not_found in unknown_ids.items() if all(not_found)
        }

        self.last_call_info = {
            "dbc_files": dbc_files,
            "total_unique_ids": total_unique_ids,
            "unknown_id_count": len(unknown_ids),
            "not_found_ids": not_found_ids,
            "found_ids": found_ids,
            "unknown_ids": unknown_ids,
        }

        if ignore_invalid_signals:
            to_keep = []

            for i, group in enumerate(out.groups):
                for j, channel in enumerate(group.channels[1:], 1):
                    if not max_flags[(i, channel.name)]:
                        to_keep.append((None, i, j))

            tmp = out.filter(to_keep, version)
            out.close()
            out = tmp

        if self._callback:
            self._callback(100, 100)
        if not out.groups:
            logger.warning(
                f'No CAN signals could be extracted from "{self.name}". The'
                "output file will be empty."
            )

        return out

    def configure(
        self,
        *,
        read_fragment_size=None,
        write_fragment_size=None,
        use_display_names=None,
        single_bit_uint_as_bool=None,
        integer_interpolation=None,
        copy_on_get=None,
    ):
        """ configure MDF parameters

        Parameters
        ----------
        read_fragment_size : int
            size hint of split data blocks, default 8MB; if the initial size is
            smaller, then no data list is used. The actual split size depends on
            the data groups' records size
        write_fragment_size : int
            size hint of split data blocks, default 4MB; if the initial size is
            smaller, then no data list is used. The actual split size depends on
            the data groups' records size. Maximum size is 4MB to ensure
            compatibility with CANape
        use_display_names : bool
            search for display name in the Channel XML comment
        single_bit_uint_as_bool : bool
            return single bit channels are np.bool arrays
        integer_interpolation : int
            interpolation mode for integer channels:

                * 0 - repeat previous sample
                * 1 - use linear interpolation
        copy_on_get : bool
            copy arrays in the get method

        """

        self._mdf.configure(
            read_fragment_size=read_fragment_size,
            write_fragment_size=write_fragment_size,
            use_display_names=use_display_names,
            single_bit_uint_as_bool=single_bit_uint_as_bool,
            integer_interpolation=integer_interpolation,
            copy_on_get=copy_on_get,
        )
        self._link_attributes()


if __name__ == "__main__":
    pass
