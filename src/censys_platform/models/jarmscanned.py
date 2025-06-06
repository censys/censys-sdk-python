"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .fielddiff import FieldDiff, FieldDiffTypedDict
from .jarmscan import JarmScan, JarmScanTypedDict
from censys_platform.types import BaseModel
from typing import Dict, Optional
from typing_extensions import NotRequired, TypedDict


class JarmScannedTypedDict(TypedDict):
    diff: NotRequired[Dict[str, FieldDiffTypedDict]]
    scan: NotRequired[JarmScanTypedDict]


class JarmScanned(BaseModel):
    diff: Optional[Dict[str, FieldDiff]] = None

    scan: Optional[JarmScan] = None
