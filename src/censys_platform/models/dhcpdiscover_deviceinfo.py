"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dhcpdiscover_ipaddress import (
    DhcpdiscoverIPAddress,
    DhcpdiscoverIPAddressTypedDict,
)
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DhcpdiscoverDeviceInfoTypedDict(TypedDict):
    alarm_input_channels: NotRequired[int]
    alarm_output_channels: NotRequired[int]
    device_class: NotRequired[str]
    device_id: NotRequired[str]
    device_type: NotRequired[str]
    http_port: NotRequired[int]
    ipv4_address: NotRequired[DhcpdiscoverIPAddressTypedDict]
    ipv6_address: NotRequired[DhcpdiscoverIPAddressTypedDict]
    machine_group: NotRequired[str]
    machine_name: NotRequired[str]
    manufacturer: NotRequired[str]
    port: NotRequired[int]
    remote_video_input_channels: NotRequired[int]
    serial_number: NotRequired[str]
    unlogin_func_mask: NotRequired[int]
    vendor: NotRequired[str]
    version: NotRequired[str]
    video_input_channels: NotRequired[int]
    video_output_channels: NotRequired[int]


class DhcpdiscoverDeviceInfo(BaseModel):
    alarm_input_channels: Optional[int] = None

    alarm_output_channels: Optional[int] = None

    device_class: Optional[str] = None

    device_id: Optional[str] = None

    device_type: Optional[str] = None

    http_port: Optional[int] = None

    ipv4_address: Optional[DhcpdiscoverIPAddress] = None

    ipv6_address: Optional[DhcpdiscoverIPAddress] = None

    machine_group: Optional[str] = None

    machine_name: Optional[str] = None

    manufacturer: Optional[str] = None

    port: Optional[int] = None

    remote_video_input_channels: Optional[int] = None

    serial_number: Optional[str] = None

    unlogin_func_mask: Optional[int] = None

    vendor: Optional[str] = None

    version: Optional[str] = None

    video_input_channels: Optional[int] = None

    video_output_channels: Optional[int] = None
