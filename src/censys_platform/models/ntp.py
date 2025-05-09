"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .ntp_ntpheader import NTPNTPHeader, NTPNTPHeaderTypedDict
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class NtpTypedDict(TypedDict):
    get_time_header: NotRequired[NTPNTPHeaderTypedDict]


class Ntp(BaseModel):
    get_time_header: Optional[NTPNTPHeader] = None
