"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cvssv4_components import CVSSv4Components, CVSSv4ComponentsTypedDict
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CVSSv4TypedDict(TypedDict):
    components: NotRequired[CVSSv4ComponentsTypedDict]
    score: NotRequired[float]
    r"""Score of the vulnerability; 0.1 is the lowest, 10 is the maximum"""
    vector: NotRequired[str]
    r"""The path, method, or scenario used to exploit the vulnerability. Each section represents components that contribute to the overall CVSS score."""


class CVSSv4(BaseModel):
    components: Optional[CVSSv4Components] = None

    score: Optional[float] = None
    r"""Score of the vulnerability; 0.1 is the lowest, 10 is the maximum"""

    vector: Optional[str] = None
    r"""The path, method, or scenario used to exploit the vulnerability. Each section represents components that contribute to the overall CVSS score."""
