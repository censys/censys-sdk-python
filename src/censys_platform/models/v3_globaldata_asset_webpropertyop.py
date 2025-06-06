"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .responseenvelopewebpropertyasset import (
    ResponseEnvelopeWebpropertyAsset,
    ResponseEnvelopeWebpropertyAssetTypedDict,
)
from censys_platform.types import BaseModel
from censys_platform.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from datetime import datetime
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V3GlobaldataAssetWebpropertyGlobalsTypedDict(TypedDict):
    organization_id: NotRequired[str]


class V3GlobaldataAssetWebpropertyGlobals(BaseModel):
    organization_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class V3GlobaldataAssetWebpropertyRequestTypedDict(TypedDict):
    webproperty_id: str
    r"""A web property host identifier, the format is hostname:port."""
    organization_id: NotRequired[str]
    r"""The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information."""
    at_time: NotRequired[datetime]
    r"""RFC3339 Timestamp to view a webproperty at a specific point in time. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time"""


class V3GlobaldataAssetWebpropertyRequest(BaseModel):
    webproperty_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""A web property host identifier, the format is hostname:port."""

    organization_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information."""

    at_time: Annotated[
        Optional[datetime],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""RFC3339 Timestamp to view a webproperty at a specific point in time. Must be a valid RFC3339 string. Ensure that you suffix the date with T00:00:00Z or a specific time"""


class V3GlobaldataAssetWebpropertyResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ResponseEnvelopeWebpropertyAssetTypedDict


class V3GlobaldataAssetWebpropertyResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ResponseEnvelopeWebpropertyAsset
