"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class EdiPartyNameTypedDict(TypedDict):
    name_assigner: NotRequired[str]
    party_name: NotRequired[str]


class EdiPartyName(BaseModel):
    name_assigner: Optional[str] = None

    party_name: Optional[str] = None
