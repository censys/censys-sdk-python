"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class NatsIoTypedDict(TypedDict):
    auth_required: NotRequired[bool]
    cluster: NotRequired[str]
    connect_urls: NotRequired[Nullable[List[str]]]
    domain: NotRequired[str]
    git_commit: NotRequired[str]
    go: NotRequired[str]
    headers: NotRequired[bool]
    jetstream: NotRequired[bool]
    proto: NotRequired[int]
    server_id: NotRequired[str]
    server_name: NotRequired[str]
    tls_available: NotRequired[bool]
    tls_required: NotRequired[bool]
    tls_verify: NotRequired[bool]
    version: NotRequired[str]
    ws_connect_urls: NotRequired[Nullable[List[str]]]


class NatsIo(BaseModel):
    auth_required: Optional[bool] = None

    cluster: Optional[str] = None

    connect_urls: OptionalNullable[List[str]] = UNSET

    domain: Optional[str] = None

    git_commit: Optional[str] = None

    go: Optional[str] = None

    headers: Optional[bool] = None

    jetstream: Optional[bool] = None

    proto: Optional[int] = None

    server_id: Optional[str] = None

    server_name: Optional[str] = None

    tls_available: Optional[bool] = None

    tls_required: Optional[bool] = None

    tls_verify: Optional[bool] = None

    version: Optional[str] = None

    ws_connect_urls: OptionalNullable[List[str]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "auth_required",
            "cluster",
            "connect_urls",
            "domain",
            "git_commit",
            "go",
            "headers",
            "jetstream",
            "proto",
            "server_id",
            "server_name",
            "tls_available",
            "tls_required",
            "tls_verify",
            "version",
            "ws_connect_urls",
        ]
        nullable_fields = ["connect_urls", "ws_connect_urls"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
