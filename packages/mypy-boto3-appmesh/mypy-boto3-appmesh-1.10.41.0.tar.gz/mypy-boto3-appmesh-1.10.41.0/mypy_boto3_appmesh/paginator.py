"Main interface for appmesh service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_appmesh.type_defs import (
    ListMeshesOutputTypeDef,
    ListRoutesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListVirtualNodesOutputTypeDef,
    ListVirtualRoutersOutputTypeDef,
    ListVirtualServicesOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListMeshesPaginator",
    "ListRoutesPaginator",
    "ListTagsForResourcePaginator",
    "ListVirtualNodesPaginator",
    "ListVirtualRoutersPaginator",
    "ListVirtualServicesPaginator",
)


class ListMeshesPaginator(Boto3Paginator):
    """
    [Paginator.ListMeshes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListMeshes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMeshesOutputTypeDef, None, None]:
        """
        [ListMeshes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListMeshes.paginate)
        """


class ListRoutesPaginator(Boto3Paginator):
    """
    [Paginator.ListRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListRoutes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, meshName: str, virtualRouterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRoutesOutputTypeDef, None, None]:
        """
        [ListRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListRoutes.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListTagsForResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceOutputTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListTagsForResource.paginate)
        """


class ListVirtualNodesPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualNodes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, meshName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListVirtualNodesOutputTypeDef, None, None]:
        """
        [ListVirtualNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualNodes.paginate)
        """


class ListVirtualRoutersPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualRouters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualRouters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, meshName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListVirtualRoutersOutputTypeDef, None, None]:
        """
        [ListVirtualRouters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualRouters.paginate)
        """


class ListVirtualServicesPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualServices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, meshName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListVirtualServicesOutputTypeDef, None, None]:
        """
        [ListVirtualServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualServices.paginate)
        """
