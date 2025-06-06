"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SipTypedDict(TypedDict):
    code: NotRequired[int]
    server: NotRequired[str]
    r"""Server software reported by service"""
    status: NotRequired[str]
    version: NotRequired[str]
    r"""SIP version"""


class Sip(BaseModel):
    code: Optional[int] = None

    server: Optional[str] = None
    r"""Server software reported by service"""

    status: Optional[str] = None

    version: Optional[str] = None
    r"""SIP version"""
