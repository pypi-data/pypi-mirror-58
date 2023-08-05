"Main interface for servicediscovery service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_servicediscovery.type_defs import (
    ListInstancesResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListServicesResponseTypeDef,
    NamespaceFilterTypeDef,
    OperationFilterTypeDef,
    PaginatorConfigTypeDef,
    ServiceFilterTypeDef,
)


__all__ = (
    "ListInstancesPaginator",
    "ListNamespacesPaginator",
    "ListOperationsPaginator",
    "ListServicesPaginator",
)


class ListInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ServiceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInstancesResponseTypeDef, None, None]:
        """
        [ListInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances.paginate)
        """


class ListNamespacesPaginator(Boto3Paginator):
    """
    [Paginator.ListNamespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[NamespaceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListNamespacesResponseTypeDef, None, None]:
        """
        [ListNamespaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces.paginate)
        """


class ListOperationsPaginator(Boto3Paginator):
    """
    [Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[OperationFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListOperationsResponseTypeDef, None, None]:
        """
        [ListOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations.paginate)
        """


class ListServicesPaginator(Boto3Paginator):
    """
    [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ServiceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListServicesResponseTypeDef, None, None]:
        """
        [ListServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices.paginate)
        """
