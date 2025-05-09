"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .analyticscapabilities import AnalyticsCapabilities, AnalyticsCapabilitiesTypedDict
from .devicecapabilities import DeviceCapabilities, DeviceCapabilitiesTypedDict
from .deviceiocapabilities import DeviceIOCapabilities, DeviceIOCapabilitiesTypedDict
from .eventscapabilities import EventsCapabilities, EventsCapabilitiesTypedDict
from .imagecapabilities import ImageCapabilities, ImageCapabilitiesTypedDict
from .mediacapabilities import MediaCapabilities, MediaCapabilitiesTypedDict
from .pantiltzoomcapabilities import (
    PanTiltZoomCapabilities,
    PanTiltZoomCapabilitiesTypedDict,
)
from .recordingcapabilities import RecordingCapabilities, RecordingCapabilitiesTypedDict
from .replaycapabilities import ReplayCapabilities, ReplayCapabilitiesTypedDict
from .searchcapabilities import SearchCapabilities, SearchCapabilitiesTypedDict
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CapabilitiesTypedDict(TypedDict):
    analytics: NotRequired[AnalyticsCapabilitiesTypedDict]
    device: NotRequired[DeviceCapabilitiesTypedDict]
    device_io: NotRequired[DeviceIOCapabilitiesTypedDict]
    events: NotRequired[EventsCapabilitiesTypedDict]
    image: NotRequired[ImageCapabilitiesTypedDict]
    media: NotRequired[MediaCapabilitiesTypedDict]
    pan_tilt_zoom: NotRequired[PanTiltZoomCapabilitiesTypedDict]
    recording: NotRequired[RecordingCapabilitiesTypedDict]
    replay: NotRequired[ReplayCapabilitiesTypedDict]
    search: NotRequired[SearchCapabilitiesTypedDict]


class Capabilities(BaseModel):
    analytics: Optional[AnalyticsCapabilities] = None

    device: Optional[DeviceCapabilities] = None

    device_io: Optional[DeviceIOCapabilities] = None

    events: Optional[EventsCapabilities] = None

    image: Optional[ImageCapabilities] = None

    media: Optional[MediaCapabilities] = None

    pan_tilt_zoom: Optional[PanTiltZoomCapabilities] = None

    recording: Optional[RecordingCapabilities] = None

    replay: Optional[ReplayCapabilities] = None

    search: Optional[SearchCapabilities] = None
