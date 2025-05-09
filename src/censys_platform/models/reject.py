"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RejectType(str, Enum):
    UNKNOWN = ""
    WRONG_VERSION = "wrong_version"
    INVALID_USERNAME = "invalid_username"
    WRONG_USER_PW = "wrong_user_pw"
    WRONG_SERVER_PW = "wrong_server_pw"
    USERNAME_IN_USE = "username_in_use"
    SERVER_FULL = "server_full"
    NO_CERTIFICATE = "no_certificate"
    AUTHENTICATOR_FAIL = "authenticator_fail"


class RejectTypedDict(TypedDict):
    reason: NotRequired[str]
    type: NotRequired[RejectType]


class Reject(BaseModel):
    reason: Optional[str] = None

    type: Optional[RejectType] = None
