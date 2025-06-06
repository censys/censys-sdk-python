"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .ssh_algorithmselection import (
    SSHAlgorithmSelection,
    SSHAlgorithmSelectionTypedDict,
)
from .ssh_endpointid import SSHEndpointID, SSHEndpointIDTypedDict
from .ssh_kexinitmessage import SSHKexInitMessage, SSHKexInitMessageTypedDict
from .ssh_serverhostkey import SSHServerHostKey, SSHServerHostKeyTypedDict
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SSHTypedDict(TypedDict):
    algorithm_selection: NotRequired[SSHAlgorithmSelectionTypedDict]
    endpoint_id: NotRequired[SSHEndpointIDTypedDict]
    hassh_fingerprint: NotRequired[str]
    kex_init_message: NotRequired[SSHKexInitMessageTypedDict]
    server_host_key: NotRequired[SSHServerHostKeyTypedDict]


class SSH(BaseModel):
    algorithm_selection: Optional[SSHAlgorithmSelection] = None

    endpoint_id: Optional[SSHEndpointID] = None

    hassh_fingerprint: Optional[str] = None

    kex_init_message: Optional[SSHKexInitMessage] = None

    server_host_key: Optional[SSHServerHostKey] = None
