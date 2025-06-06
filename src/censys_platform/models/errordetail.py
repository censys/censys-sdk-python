"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Any, Optional
from typing_extensions import NotRequired, TypedDict


class ErrorDetailTypedDict(TypedDict):
    location: NotRequired[str]
    r"""Where the error occurred, e.g. 'body.items[3].tags' or 'path.thing-id'"""
    message: NotRequired[str]
    r"""Error message text"""
    value: NotRequired[Any]
    r"""The value at the given location"""


class ErrorDetail(BaseModel):
    location: Optional[str] = None
    r"""Where the error occurred, e.g. 'body.items[3].tags' or 'path.thing-id'"""

    message: Optional[str] = None
    r"""Error message text"""

    value: Optional[Any] = None
    r"""The value at the given location"""
