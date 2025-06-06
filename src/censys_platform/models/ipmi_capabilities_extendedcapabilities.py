"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class IpmiCapabilitiesExtendedCapabilitiesTypedDict(TypedDict):
    supports_ipmi_v1_5: NotRequired[bool]
    r"""True if IPMI v1.5 is supported"""
    supports_ipmi_v2_0: NotRequired[bool]
    r"""True if IPMI v2.0 is supported"""


class IpmiCapabilitiesExtendedCapabilities(BaseModel):
    supports_ipmi_v1_5: Optional[bool] = None
    r"""True if IPMI v1.5 is supported"""

    supports_ipmi_v2_0: Optional[bool] = None
    r"""True if IPMI v2.0 is supported"""
