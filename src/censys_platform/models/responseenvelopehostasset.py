"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .hostasset import HostAsset, HostAssetTypedDict
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ResponseEnvelopeHostAssetTypedDict(TypedDict):
    result: NotRequired[HostAssetTypedDict]


class ResponseEnvelopeHostAsset(BaseModel):
    result: Optional[HostAsset] = None
