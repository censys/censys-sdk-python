"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class MurmurMessageMurmurHeaderTypedDict(TypedDict):
    length: NotRequired[int]
    type: NotRequired[str]


class MurmurMessageMurmurHeader(BaseModel):
    length: Optional[int] = None

    type: Optional[str] = None
