"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class UnitronicsPcomTypedDict(TypedDict):
    buffer_size: NotRequired[str]
    hardware_version: NotRequired[str]
    model: NotRequired[str]
    model_executor: NotRequired[str]
    model_op_executor: NotRequired[str]
    name: NotRequired[str]
    os_build: NotRequired[str]
    os_version: NotRequired[str]
    unique_id: NotRequired[int]
    unit_id: NotRequired[str]


class UnitronicsPcom(BaseModel):
    buffer_size: Optional[str] = None

    hardware_version: Optional[str] = None

    model: Optional[str] = None

    model_executor: Optional[str] = None

    model_op_executor: Optional[str] = None

    name: Optional[str] = None

    os_build: Optional[str] = None

    os_version: Optional[str] = None

    unique_id: Optional[int] = None

    unit_id: Optional[str] = None
