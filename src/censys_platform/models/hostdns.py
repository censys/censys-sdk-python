"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .hostdns_forwardresolution import (
    HostDNSForwardResolution,
    HostDNSForwardResolutionTypedDict,
)
from .hostdns_reverseresolution import (
    HostDNSReverseResolution,
    HostDNSReverseResolutionTypedDict,
)
from censys_platform.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class HostDNSTypedDict(TypedDict):
    forward_dns: NotRequired[Dict[str, HostDNSForwardResolutionTypedDict]]
    names: NotRequired[Nullable[List[str]]]
    reverse_dns: NotRequired[HostDNSReverseResolutionTypedDict]


class HostDNS(BaseModel):
    forward_dns: Optional[Dict[str, HostDNSForwardResolution]] = None

    names: OptionalNullable[List[str]] = UNSET

    reverse_dns: Optional[HostDNSReverseResolution] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["forward_dns", "names", "reverse_dns"]
        nullable_fields = ["names"]
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
