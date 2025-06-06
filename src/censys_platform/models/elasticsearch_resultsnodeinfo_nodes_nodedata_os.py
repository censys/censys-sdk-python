"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ElasticSearchResultsNodeInfoNodesNodeDataOSTypedDict(TypedDict):
    allocated_proc: NotRequired[int]
    arch: NotRequired[str]
    available_proc: NotRequired[int]
    name: NotRequired[str]
    pretty_name: NotRequired[str]
    refresh_interval_ms: NotRequired[int]
    version: NotRequired[str]


class ElasticSearchResultsNodeInfoNodesNodeDataOS(BaseModel):
    allocated_proc: Optional[int] = None

    arch: Optional[str] = None

    available_proc: Optional[int] = None

    name: Optional[str] = None

    pretty_name: Optional[str] = None

    refresh_interval_ms: Optional[int] = None

    version: Optional[str] = None
