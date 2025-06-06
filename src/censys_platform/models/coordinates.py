"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CoordinatesTypedDict(TypedDict):
    latitude: NotRequired[float]
    longitude: NotRequired[float]


class Coordinates(BaseModel):
    latitude: Optional[float] = None

    longitude: Optional[float] = None
