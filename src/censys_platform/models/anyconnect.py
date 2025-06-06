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


class AnyConnectTypedDict(TypedDict):
    aggregate_auth_version: NotRequired[int]
    r"""Version number indicated by the response for config-auth exchange"""
    auth_methods: NotRequired[Nullable[List[str]]]
    r"""Supported methods for users to enter credentials for this VPN"""
    groups: NotRequired[Nullable[List[str]]]
    r"""List of groups a user can authenticate with to use this VPN"""
    raw: NotRequired[str]
    r"""XML content of the config-auth response"""
    response_type: NotRequired[str]
    r"""Type of the response packet received after initializing the config-auth exchange"""


class AnyConnect(BaseModel):
    aggregate_auth_version: Optional[int] = None
    r"""Version number indicated by the response for config-auth exchange"""

    auth_methods: OptionalNullable[List[str]] = UNSET
    r"""Supported methods for users to enter credentials for this VPN"""

    groups: OptionalNullable[List[str]] = UNSET
    r"""List of groups a user can authenticate with to use this VPN"""

    raw: Optional[str] = None
    r"""XML content of the config-auth response"""

    response_type: Optional[str] = None
    r"""Type of the response packet received after initializing the config-auth exchange"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "aggregate_auth_version",
            "auth_methods",
            "groups",
            "raw",
            "response_type",
        ]
        nullable_fields = ["auth_methods", "groups"]
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
