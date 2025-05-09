"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .responseenvelopesearchqueryresponse import (
    ResponseEnvelopeSearchQueryResponse,
    ResponseEnvelopeSearchQueryResponseTypedDict,
)
from .searchqueryinputbody import SearchQueryInputBody, SearchQueryInputBodyTypedDict
from censys_platform.types import BaseModel
from censys_platform.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V3CollectionsSearchQueryGlobalsTypedDict(TypedDict):
    organization_id: NotRequired[str]


class V3CollectionsSearchQueryGlobals(BaseModel):
    organization_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class V3CollectionsSearchQueryRequestTypedDict(TypedDict):
    collection_uid: str
    r"""The UID for the collection"""
    search_query_input_body: SearchQueryInputBodyTypedDict
    organization_id: NotRequired[str]
    r"""The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information."""


class V3CollectionsSearchQueryRequest(BaseModel):
    collection_uid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UID for the collection"""

    search_query_input_body: Annotated[
        SearchQueryInputBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    organization_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""The ID of a Censys organization to associate the request with. See the [Getting Started docs](https://docs.censys.com/reference/get-started#step-3-set-your-organization-id) for more information."""


class V3CollectionsSearchQueryResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: ResponseEnvelopeSearchQueryResponseTypedDict


class V3CollectionsSearchQueryResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: ResponseEnvelopeSearchQueryResponse
