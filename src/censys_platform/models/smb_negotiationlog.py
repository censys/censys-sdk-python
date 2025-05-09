"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .smb_headerlog import SmbHeaderLog, SmbHeaderLogTypedDict
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


class SmbNegotiationLogTypedDict(TypedDict):
    authentication_types: NotRequired[Nullable[List[str]]]
    capabilities: NotRequired[int]
    dialect_revision: NotRequired[int]
    header_log: NotRequired[SmbHeaderLogTypedDict]
    security_mode: NotRequired[int]
    server_guid: NotRequired[str]
    server_start_time: NotRequired[int]
    system_time: NotRequired[int]


class SmbNegotiationLog(BaseModel):
    authentication_types: OptionalNullable[List[str]] = UNSET

    capabilities: Optional[int] = None

    dialect_revision: Optional[int] = None

    header_log: Optional[SmbHeaderLog] = None

    security_mode: Optional[int] = None

    server_guid: Optional[str] = None

    server_start_time: Optional[int] = None

    system_time: Optional[int] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "authentication_types",
            "capabilities",
            "dialect_revision",
            "header_log",
            "security_mode",
            "server_guid",
            "server_start_time",
            "system_time",
        ]
        nullable_fields = ["authentication_types"]
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
