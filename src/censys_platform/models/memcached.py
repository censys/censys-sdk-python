"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class MemcachedTypedDict(TypedDict):
    ascii_binding_protocol_enabled: NotRequired[bool]
    r"""Whether server responds to a handshake using the ASCII wire format of the protocol."""
    binary_binding_protocol_enabled: NotRequired[bool]
    r"""Whether server responds to a handshake using the binary wire format of the protocol."""
    responds_to_udp: NotRequired[bool]
    r"""Whether the server on the UDP port with the same number responds to a handshake using the ASCII wire format of the protocol."""
    stats: NotRequired[Dict[str, str]]
    r"""Server information returned in response to the stats command, as a set of key:value pairs."""
    version: NotRequired[str]
    r"""The Memcached version indicated in the server's response."""


class Memcached(BaseModel):
    ascii_binding_protocol_enabled: Optional[bool] = None
    r"""Whether server responds to a handshake using the ASCII wire format of the protocol."""

    binary_binding_protocol_enabled: Optional[bool] = None
    r"""Whether server responds to a handshake using the binary wire format of the protocol."""

    responds_to_udp: Optional[bool] = None
    r"""Whether the server on the UDP port with the same number responds to a handshake using the ASCII wire format of the protocol."""

    stats: Optional[Dict[str, str]] = None
    r"""Server information returned in response to the stats command, as a set of key:value pairs."""

    version: Optional[str] = None
    r"""The Memcached version indicated in the server's response."""
