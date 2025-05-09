"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class StatusTypedDict(TypedDict):
    available_workers: NotRequired[int]
    function: NotRequired[str]
    running: NotRequired[int]
    total: NotRequired[int]


class Status(BaseModel):
    available_workers: Optional[int] = None

    function: Optional[str] = None

    running: Optional[int] = None

    total: Optional[int] = None
