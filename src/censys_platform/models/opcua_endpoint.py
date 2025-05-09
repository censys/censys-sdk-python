"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .opcua_description import OpcUaDescription, OpcUaDescriptionTypedDict
from .opcua_usertokenpolicy import OpcUaUserTokenPolicy, OpcUaUserTokenPolicyTypedDict
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


class OpcUaEndpointTypedDict(TypedDict):
    endpoint_url: NotRequired[str]
    security_level: NotRequired[int]
    security_mode: NotRequired[int]
    security_policy_uri: NotRequired[str]
    serve_cert: NotRequired[str]
    server: NotRequired[OpcUaDescriptionTypedDict]
    transport_profile_uri: NotRequired[str]
    user_identity_token: NotRequired[Nullable[List[OpcUaUserTokenPolicyTypedDict]]]


class OpcUaEndpoint(BaseModel):
    endpoint_url: Optional[str] = None

    security_level: Optional[int] = None

    security_mode: Optional[int] = None

    security_policy_uri: Optional[str] = None

    serve_cert: Optional[str] = None

    server: Optional[OpcUaDescription] = None

    transport_profile_uri: Optional[str] = None

    user_identity_token: OptionalNullable[List[OpcUaUserTokenPolicy]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "endpoint_url",
            "security_level",
            "security_mode",
            "security_policy_uri",
            "serve_cert",
            "server",
            "transport_profile_uri",
            "user_identity_token",
        ]
        nullable_fields = ["user_identity_token"]
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
