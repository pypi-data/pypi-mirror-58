"Main interface for appmesh service"
from mypy_boto3_appmesh.client import AppMeshClient, AppMeshClient as Client
from mypy_boto3_appmesh.paginator import (
    ListMeshesPaginator,
    ListRoutesPaginator,
    ListTagsForResourcePaginator,
    ListVirtualNodesPaginator,
    ListVirtualRoutersPaginator,
    ListVirtualServicesPaginator,
)


__all__ = (
    "AppMeshClient",
    "Client",
    "ListMeshesPaginator",
    "ListRoutesPaginator",
    "ListTagsForResourcePaginator",
    "ListVirtualNodesPaginator",
    "ListVirtualRoutersPaginator",
    "ListVirtualServicesPaginator",
)
