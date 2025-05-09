"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .mongodb_buildinfo import MongodbBuildInfo, MongodbBuildInfoTypedDict
from .mongodb_ismaster import MongodbIsMaster, MongodbIsMasterTypedDict
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class MongodbTypedDict(TypedDict):
    build_info: NotRequired[MongodbBuildInfoTypedDict]
    is_master: NotRequired[MongodbIsMasterTypedDict]


class Mongodb(BaseModel):
    build_info: Optional[MongodbBuildInfo] = None

    is_master: Optional[MongodbIsMaster] = None
