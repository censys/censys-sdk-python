"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class KeyAlgorithmTypedDict(TypedDict):
    name: NotRequired[str]
    r"""Name of public key type, such as RSA or ECDSA. Information specific to the key type is available in the named sub-record."""
    oid: NotRequired[str]


class KeyAlgorithm(BaseModel):
    name: Optional[str] = None
    r"""Name of public key type, such as RSA or ECDSA. Information specific to the key type is available in the named sub-record."""

    oid: Optional[str] = None
