"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .nodeinfov0 import NodeInfoV0, NodeInfoV0TypedDict
from .nodeinfov1 import NodeInfoV1, NodeInfoV1TypedDict
from .nodeinfov2 import NodeInfoV2, NodeInfoV2TypedDict
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class IotaTypedDict(TypedDict):
    v0_info: NotRequired[NodeInfoV0TypedDict]
    v1_info: NotRequired[NodeInfoV1TypedDict]
    v2_info: NotRequired[NodeInfoV2TypedDict]


class Iota(BaseModel):
    v0_info: Optional[NodeInfoV0] = None

    v1_info: Optional[NodeInfoV1] = None

    v2_info: Optional[NodeInfoV2] = None
