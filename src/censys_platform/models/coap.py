"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CoapTypedDict(TypedDict):
    code: NotRequired[str]
    message_id: NotRequired[int]
    message_type: NotRequired[str]
    payload: NotRequired[str]
    token: NotRequired[str]
    version: NotRequired[int]


class Coap(BaseModel):
    code: Optional[str] = None

    message_id: Optional[int] = None

    message_type: Optional[str] = None

    payload: Optional[str] = None

    token: Optional[str] = None

    version: Optional[int] = None
