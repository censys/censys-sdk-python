"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class FtpTypedDict(TypedDict):
    auth_ssl_response: NotRequired[str]
    auth_tls_response: NotRequired[str]
    implicit_tls: NotRequired[bool]
    status_code: NotRequired[int]
    status_meaning: NotRequired[str]


class Ftp(BaseModel):
    auth_ssl_response: Optional[str] = None

    auth_tls_response: Optional[str] = None

    implicit_tls: Optional[bool] = None

    status_code: Optional[int] = None

    status_meaning: Optional[str] = None
