"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class MoneroP2PEntryTypedDict(TypedDict):
    data: NotRequired[str]
    name: NotRequired[str]


class MoneroP2PEntry(BaseModel):
    data: Optional[str] = None

    name: Optional[str] = None
