"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RocketmqResponseHeaderTypedDict(TypedDict):
    code: NotRequired[int]
    flag: NotRequired[int]
    language: NotRequired[str]
    opaque: NotRequired[int]
    serialize_type_current_rpc: NotRequired[str]


class RocketmqResponseHeader(BaseModel):
    code: Optional[int] = None

    flag: Optional[int] = None

    language: Optional[str] = None

    opaque: Optional[int] = None

    serialize_type_current_rpc: Optional[str] = None
