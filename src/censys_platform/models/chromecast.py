"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .chromecast_application import (
    ChromecastApplication,
    ChromecastApplicationTypedDict,
)
from .chromecast_volume import ChromecastVolume, ChromecastVolumeTypedDict
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


class ChromecastTypedDict(TypedDict):
    applications: NotRequired[Nullable[List[ChromecastApplicationTypedDict]]]
    icon_url: NotRequired[str]
    is_active_input: NotRequired[bool]
    protocol_version: NotRequired[int]
    status_text: NotRequired[str]
    universal_app_id: NotRequired[str]
    volume: NotRequired[ChromecastVolumeTypedDict]


class Chromecast(BaseModel):
    applications: OptionalNullable[List[ChromecastApplication]] = UNSET

    icon_url: Optional[str] = None

    is_active_input: Optional[bool] = None

    protocol_version: Optional[int] = None

    status_text: Optional[str] = None

    universal_app_id: Optional[str] = None

    volume: Optional[ChromecastVolume] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "applications",
            "icon_url",
            "is_active_input",
            "protocol_version",
            "status_text",
            "universal_app_id",
            "volume",
        ]
        nullable_fields = ["applications"]
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
