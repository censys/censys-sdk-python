"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cryptsetup import CryptSetup, CryptSetupTypedDict
from .murmur_murmurversion import MurmurMurmurVersion, MurmurMurmurVersionTypedDict
from .murmurmessage import MurmurMessage, MurmurMessageTypedDict
from .reject import Reject, RejectTypedDict
from .serverconfig import ServerConfig, ServerConfigTypedDict
from .serversync import ServerSync, ServerSyncTypedDict
from .textmessage import TextMessage, TextMessageTypedDict
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


class MurmurTypedDict(TypedDict):
    crypt_setup: NotRequired[CryptSetupTypedDict]
    murmur_messages: NotRequired[Nullable[List[MurmurMessageTypedDict]]]
    reject: NotRequired[RejectTypedDict]
    server_config: NotRequired[ServerConfigTypedDict]
    server_sync: NotRequired[ServerSyncTypedDict]
    text_messages: NotRequired[Nullable[List[TextMessageTypedDict]]]
    version: NotRequired[MurmurMurmurVersionTypedDict]


class Murmur(BaseModel):
    crypt_setup: Optional[CryptSetup] = None

    murmur_messages: OptionalNullable[List[MurmurMessage]] = UNSET

    reject: Optional[Reject] = None

    server_config: Optional[ServerConfig] = None

    server_sync: Optional[ServerSync] = None

    text_messages: OptionalNullable[List[TextMessage]] = UNSET

    version: Optional[MurmurMurmurVersion] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "crypt_setup",
            "murmur_messages",
            "reject",
            "server_config",
            "server_sync",
            "text_messages",
            "version",
        ]
        nullable_fields = ["murmur_messages", "text_messages"]
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
