"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cvss import Cvss, CvssTypedDict
from .cvssv4 import CVSSv4, CVSSv4TypedDict
from .epss import Epss, EpssTypedDict
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class MetricsTypedDict(TypedDict):
    cvss_v30: NotRequired[CvssTypedDict]
    cvss_v31: NotRequired[CvssTypedDict]
    cvss_v40: NotRequired[CVSSv4TypedDict]
    epss: NotRequired[EpssTypedDict]


class Metrics(BaseModel):
    cvss_v30: Optional[Cvss] = None

    cvss_v31: Optional[Cvss] = None

    cvss_v40: Optional[CVSSv4] = None

    epss: Optional[Epss] = None
