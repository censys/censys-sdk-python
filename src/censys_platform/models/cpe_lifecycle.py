"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from censys_platform.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CPELifeCycleTypedDict(TypedDict):
    end_of_life: NotRequired[bool]
    end_of_life_date: NotRequired[str]
    release_date: NotRequired[str]


class CPELifeCycle(BaseModel):
    end_of_life: Optional[bool] = None

    end_of_life_date: Optional[str] = None

    release_date: Optional[str] = None
