"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .prometheus_response import PrometheusResponse, PrometheusResponseTypedDict
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PrometheusTypedDict(TypedDict):
    response: NotRequired[PrometheusResponseTypedDict]


class Prometheus(BaseModel):
    response: Optional[PrometheusResponse] = None
