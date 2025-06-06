"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .keyalgorithm import KeyAlgorithm, KeyAlgorithmTypedDict
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SignatureTypedDict(TypedDict):
    self_signed: NotRequired[bool]
    r"""Whether the certificate was signed by its own key."""
    signature_algorithm: NotRequired[KeyAlgorithmTypedDict]
    valid: NotRequired[bool]
    r"""Whether the signature is valid."""
    value: NotRequired[str]
    r"""Contents of the signature."""


class Signature(BaseModel):
    self_signed: Optional[bool] = None
    r"""Whether the certificate was signed by its own key."""

    signature_algorithm: Optional[KeyAlgorithm] = None

    valid: Optional[bool] = None
    r"""Whether the signature is valid."""

    value: Optional[str] = None
    r"""Contents of the signature."""
