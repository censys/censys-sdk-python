"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ExtensionTypedDict(TypedDict):
    critical: NotRequired[bool]
    id: NotRequired[str]
    value: NotRequired[str]


class Extension(BaseModel):
    critical: Optional[bool] = None

    id: Optional[str] = None

    value: Optional[str] = None
