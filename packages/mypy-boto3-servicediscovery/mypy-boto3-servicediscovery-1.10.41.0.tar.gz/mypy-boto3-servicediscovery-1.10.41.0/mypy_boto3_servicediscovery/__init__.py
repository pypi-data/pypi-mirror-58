"Main interface for servicediscovery service"
from mypy_boto3_servicediscovery.client import (
    ServiceDiscoveryClient,
    ServiceDiscoveryClient as Client,
)
from mypy_boto3_servicediscovery.paginator import (
    ListInstancesPaginator,
    ListNamespacesPaginator,
    ListOperationsPaginator,
    ListServicesPaginator,
)


__all__ = (
    "Client",
    "ListInstancesPaginator",
    "ListNamespacesPaginator",
    "ListOperationsPaginator",
    "ListServicesPaginator",
    "ServiceDiscoveryClient",
)
