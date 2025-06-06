"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AmqpVersionTypedDict(TypedDict):
    major: NotRequired[int]
    minor: NotRequired[int]
    revision: NotRequired[int]


class AmqpVersion(BaseModel):
    major: Optional[int] = None

    minor: Optional[int] = None

    revision: Optional[int] = None
