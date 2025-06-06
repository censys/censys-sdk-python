"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class Reason(str, Enum):
    r"""An enumerated value indicating the issuer-supplied reason for the revocation."""

    UNKNOWN = ""
    UNSPECIFIED = "unspecified"
    KEY_COMPROMISE = "key_compromise"
    CA_COMPROMISE = "ca_compromise"
    AFFILIATION_CHANGED = "affiliation_changed"
    SUPERSEDED = "superseded"
    CESSATION_OF_OPERATION = "cessation_of_operation"
    CERTIFICATE_HOLD = "certificate_hold"
    REMOVE_FROM_CRL = "remove_from_crl"
    PRIVILEGE_WITHDRAWN = "privilege_withdrawn"
    AA_COMPROMISE = "aa_compromise"


class CertificateRevocationRevocationInfoTypedDict(TypedDict):
    next_update: NotRequired[str]
    reason: NotRequired[Reason]
    r"""An enumerated value indicating the issuer-supplied reason for the revocation."""
    revocation_time: NotRequired[str]
    r"""The issuer-supplied timestamp indicating when the certificate was revoked."""
    revoked: NotRequired[bool]
    r"""Whether the certificate has been revoked before its expiry date by the issuer."""


class CertificateRevocationRevocationInfo(BaseModel):
    next_update: Optional[str] = None

    reason: Optional[Reason] = None
    r"""An enumerated value indicating the issuer-supplied reason for the revocation."""

    revocation_time: Optional[str] = None
    r"""The issuer-supplied timestamp indicating when the certificate was revoked."""

    revoked: Optional[bool] = None
    r"""Whether the certificate has been revoked before its expiry date by the issuer."""
