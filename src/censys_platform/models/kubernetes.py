"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .kubernetes_endpoint import KubernetesEndpoint, KubernetesEndpointTypedDict
from .kubernetes_node import KubernetesNode, KubernetesNodeTypedDict
from .kubernetes_role import KubernetesRole, KubernetesRoleTypedDict
from .kubernetes_versioninfo import (
    KubernetesVersionInfo,
    KubernetesVersionInfoTypedDict,
)
from censys_platform.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class KubernetesTypedDict(TypedDict):
    endpoints: NotRequired[Nullable[List[KubernetesEndpointTypedDict]]]
    kubernetes_dashboard_found: NotRequired[bool]
    r"""True if the dashboard is running and accessible"""
    nodes: NotRequired[Nullable[List[KubernetesNodeTypedDict]]]
    pod_names: NotRequired[Nullable[List[str]]]
    roles: NotRequired[Nullable[List[KubernetesRoleTypedDict]]]
    version_info: NotRequired[KubernetesVersionInfoTypedDict]


class Kubernetes(BaseModel):
    endpoints: OptionalNullable[List[KubernetesEndpoint]] = UNSET

    kubernetes_dashboard_found: Optional[bool] = None
    r"""True if the dashboard is running and accessible"""

    nodes: OptionalNullable[List[KubernetesNode]] = UNSET

    pod_names: OptionalNullable[List[str]] = UNSET

    roles: OptionalNullable[List[KubernetesRole]] = UNSET

    version_info: Optional[KubernetesVersionInfo] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "endpoints",
            "kubernetes_dashboard_found",
            "nodes",
            "pod_names",
            "roles",
            "version_info",
        ]
        nullable_fields = ["endpoints", "nodes", "pod_names", "roles"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
