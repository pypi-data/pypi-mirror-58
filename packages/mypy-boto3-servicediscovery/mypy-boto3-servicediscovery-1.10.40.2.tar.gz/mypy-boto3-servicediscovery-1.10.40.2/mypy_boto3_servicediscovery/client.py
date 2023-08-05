"Main interface for servicediscovery service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_servicediscovery.client as client_scope

# pylint: disable=import-self
import mypy_boto3_servicediscovery.paginator as paginator_scope
from mypy_boto3_servicediscovery.type_defs import (
    CreateHttpNamespaceResponseTypeDef,
    CreatePrivateDnsNamespaceResponseTypeDef,
    CreatePublicDnsNamespaceResponseTypeDef,
    CreateServiceResponseTypeDef,
    DeleteNamespaceResponseTypeDef,
    DeregisterInstanceResponseTypeDef,
    DiscoverInstancesResponseTypeDef,
    DnsConfigTypeDef,
    GetInstanceResponseTypeDef,
    GetInstancesHealthStatusResponseTypeDef,
    GetNamespaceResponseTypeDef,
    GetOperationResponseTypeDef,
    GetServiceResponseTypeDef,
    HealthCheckConfigTypeDef,
    HealthCheckCustomConfigTypeDef,
    ListInstancesResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListServicesResponseTypeDef,
    NamespaceFilterTypeDef,
    OperationFilterTypeDef,
    RegisterInstanceResponseTypeDef,
    ServiceChangeTypeDef,
    ServiceFilterTypeDef,
    UpdateServiceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceDiscoveryClient",)


class ServiceDiscoveryClient(BaseClient):
    """
    [ServiceDiscovery.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_http_namespace(
        self, Name: str, CreatorRequestId: str = None, Description: str = None
    ) -> CreateHttpNamespaceResponseTypeDef:
        """
        [Client.create_http_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_http_namespace)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_private_dns_namespace(
        self, Name: str, Vpc: str, CreatorRequestId: str = None, Description: str = None
    ) -> CreatePrivateDnsNamespaceResponseTypeDef:
        """
        [Client.create_private_dns_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_private_dns_namespace)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_public_dns_namespace(
        self, Name: str, CreatorRequestId: str = None, Description: str = None
    ) -> CreatePublicDnsNamespaceResponseTypeDef:
        """
        [Client.create_public_dns_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_public_dns_namespace)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_service(
        self,
        Name: str,
        NamespaceId: str = None,
        CreatorRequestId: str = None,
        Description: str = None,
        DnsConfig: DnsConfigTypeDef = None,
        HealthCheckConfig: HealthCheckConfigTypeDef = None,
        HealthCheckCustomConfig: HealthCheckCustomConfigTypeDef = None,
    ) -> CreateServiceResponseTypeDef:
        """
        [Client.create_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_service)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_namespace(self, Id: str) -> DeleteNamespaceResponseTypeDef:
        """
        [Client.delete_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.delete_namespace)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_service(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.delete_service)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_instance(
        self, ServiceId: str, InstanceId: str
    ) -> DeregisterInstanceResponseTypeDef:
        """
        [Client.deregister_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.deregister_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def discover_instances(
        self,
        NamespaceName: str,
        ServiceName: str,
        MaxResults: int = None,
        QueryParameters: Dict[str, str] = None,
        HealthStatus: Literal["HEALTHY", "UNHEALTHY", "ALL"] = None,
    ) -> DiscoverInstancesResponseTypeDef:
        """
        [Client.discover_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.discover_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instance(self, ServiceId: str, InstanceId: str) -> GetInstanceResponseTypeDef:
        """
        [Client.get_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instances_health_status(
        self,
        ServiceId: str,
        Instances: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetInstancesHealthStatusResponseTypeDef:
        """
        [Client.get_instances_health_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_instances_health_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_namespace(self, Id: str) -> GetNamespaceResponseTypeDef:
        """
        [Client.get_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_namespace)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_operation(self, OperationId: str) -> GetOperationResponseTypeDef:
        """
        [Client.get_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_operation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service(self, Id: str) -> GetServiceResponseTypeDef:
        """
        [Client.get_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_service)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_instances(
        self, ServiceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListInstancesResponseTypeDef:
        """
        [Client.list_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_namespaces(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[NamespaceFilterTypeDef] = None,
    ) -> ListNamespacesResponseTypeDef:
        """
        [Client.list_namespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_namespaces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_operations(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[OperationFilterTypeDef] = None,
    ) -> ListOperationsResponseTypeDef:
        """
        [Client.list_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_operations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_services(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ServiceFilterTypeDef] = None,
    ) -> ListServicesResponseTypeDef:
        """
        [Client.list_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_services)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_instance(
        self,
        ServiceId: str,
        InstanceId: str,
        Attributes: Dict[str, str],
        CreatorRequestId: str = None,
    ) -> RegisterInstanceResponseTypeDef:
        """
        [Client.register_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.register_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_instance_custom_health_status(
        self, ServiceId: str, InstanceId: str, Status: Literal["HEALTHY", "UNHEALTHY"]
    ) -> None:
        """
        [Client.update_instance_custom_health_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.update_instance_custom_health_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_service(
        self, Id: str, Service: ServiceChangeTypeDef
    ) -> UpdateServiceResponseTypeDef:
        """
        [Client.update_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Client.update_service)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_instances"]
    ) -> paginator_scope.ListInstancesPaginator:
        """
        [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_namespaces"]
    ) -> paginator_scope.ListNamespacesPaginator:
        """
        [Paginator.ListNamespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_operations"]
    ) -> paginator_scope.ListOperationsPaginator:
        """
        [Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_services"]
    ) -> paginator_scope.ListServicesPaginator:
        """
        [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices)
        """


class Exceptions:
    ClientError: Boto3ClientError
    CustomHealthNotFound: Boto3ClientError
    DuplicateRequest: Boto3ClientError
    InstanceNotFound: Boto3ClientError
    InvalidInput: Boto3ClientError
    NamespaceAlreadyExists: Boto3ClientError
    NamespaceNotFound: Boto3ClientError
    OperationNotFound: Boto3ClientError
    ResourceInUse: Boto3ClientError
    ResourceLimitExceeded: Boto3ClientError
    ServiceAlreadyExists: Boto3ClientError
    ServiceNotFound: Boto3ClientError
