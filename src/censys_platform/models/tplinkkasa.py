"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class TplinkKasaTypedDict(TypedDict):
    active_mode: NotRequired[str]
    brightness: NotRequired[int]
    dev_name: NotRequired[str]
    err_code: NotRequired[int]
    feature: NotRequired[str]
    hw_ver: NotRequired[str]
    icon_hash: NotRequired[str]
    led_off: NotRequired[int]
    mic_type: NotRequired[str]
    model: NotRequired[str]
    on_time: NotRequired[int]
    relay_state: NotRequired[int]
    rssi: NotRequired[int]
    sw_ver: NotRequired[str]
    updating: NotRequired[int]


class TplinkKasa(BaseModel):
    active_mode: Optional[str] = None

    brightness: Optional[int] = None

    dev_name: Optional[str] = None

    err_code: Optional[int] = None

    feature: Optional[str] = None

    hw_ver: Optional[str] = None

    icon_hash: Optional[str] = None

    led_off: Optional[int] = None

    mic_type: Optional[str] = None

    model: Optional[str] = None

    on_time: Optional[int] = None

    relay_state: Optional[int] = None

    rssi: Optional[int] = None

    sw_ver: Optional[str] = None

    updating: Optional[int] = None
