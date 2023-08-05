"Main interface for schemas service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_schemas.client as client_scope

# pylint: disable=import-self
import mypy_boto3_schemas.paginator as paginator_scope
from mypy_boto3_schemas.type_defs import (
    CreateDiscovererResponseTypeDef,
    CreateRegistryResponseTypeDef,
    CreateSchemaResponseTypeDef,
    DescribeCodeBindingResponseTypeDef,
    DescribeDiscovererResponseTypeDef,
    DescribeRegistryResponseTypeDef,
    DescribeSchemaResponseTypeDef,
    GetCodeBindingSourceResponseTypeDef,
    GetDiscoveredSchemaResponseTypeDef,
    ListDiscoverersResponseTypeDef,
    ListRegistriesResponseTypeDef,
    ListSchemaVersionsResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LockServiceLinkedRoleResponseTypeDef,
    PutCodeBindingResponseTypeDef,
    SearchSchemasResponseTypeDef,
    StartDiscovererResponseTypeDef,
    StopDiscovererResponseTypeDef,
    UpdateDiscovererResponseTypeDef,
    UpdateRegistryResponseTypeDef,
    UpdateSchemaResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_schemas.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SchemasClient",)


class SchemasClient(BaseClient):
    """
    [Schemas.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_discoverer(
        self, SourceArn: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> CreateDiscovererResponseTypeDef:
        """
        [Client.create_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.create_discoverer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_registry(
        self, RegistryName: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> CreateRegistryResponseTypeDef:
        """
        [Client.create_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.create_registry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_schema(
        self,
        Content: str,
        RegistryName: str,
        SchemaName: str,
        Type: Literal["OpenApi3"],
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateSchemaResponseTypeDef:
        """
        [Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.create_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_discoverer(self, DiscovererId: str) -> None:
        """
        [Client.delete_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.delete_discoverer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_registry(self, RegistryName: str) -> None:
        """
        [Client.delete_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.delete_registry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_schema(self, RegistryName: str, SchemaName: str) -> None:
        """
        [Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.delete_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_schema_version(self, RegistryName: str, SchemaName: str, SchemaVersion: str) -> None:
        """
        [Client.delete_schema_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.delete_schema_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_code_binding(
        self, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> DescribeCodeBindingResponseTypeDef:
        """
        [Client.describe_code_binding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.describe_code_binding)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_discoverer(self, DiscovererId: str) -> DescribeDiscovererResponseTypeDef:
        """
        [Client.describe_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.describe_discoverer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_registry(self, RegistryName: str) -> DescribeRegistryResponseTypeDef:
        """
        [Client.describe_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.describe_registry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_schema(
        self, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> DescribeSchemaResponseTypeDef:
        """
        [Client.describe_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.describe_schema)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_code_binding_source(
        self, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> GetCodeBindingSourceResponseTypeDef:
        """
        [Client.get_code_binding_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.get_code_binding_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_discovered_schema(
        self, Events: List[str], Type: Literal["OpenApi3"]
    ) -> GetDiscoveredSchemaResponseTypeDef:
        """
        [Client.get_discovered_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.get_discovered_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_discoverers(
        self,
        DiscovererIdPrefix: str = None,
        Limit: int = None,
        NextToken: str = None,
        SourceArnPrefix: str = None,
    ) -> ListDiscoverersResponseTypeDef:
        """
        [Client.list_discoverers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.list_discoverers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_registries(
        self,
        Limit: int = None,
        NextToken: str = None,
        RegistryNamePrefix: str = None,
        Scope: str = None,
    ) -> ListRegistriesResponseTypeDef:
        """
        [Client.list_registries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.list_registries)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_schema_versions(
        self, RegistryName: str, SchemaName: str, Limit: int = None, NextToken: str = None
    ) -> ListSchemaVersionsResponseTypeDef:
        """
        [Client.list_schema_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.list_schema_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_schemas(
        self,
        RegistryName: str,
        Limit: int = None,
        NextToken: str = None,
        SchemaNamePrefix: str = None,
    ) -> ListSchemasResponseTypeDef:
        """
        [Client.list_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.list_schemas)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def lock_service_linked_role(
        self, RoleArn: str, Timeout: int
    ) -> LockServiceLinkedRoleResponseTypeDef:
        """
        [Client.lock_service_linked_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.lock_service_linked_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_code_binding(
        self, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> PutCodeBindingResponseTypeDef:
        """
        [Client.put_code_binding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.put_code_binding)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_schemas(
        self, Keywords: str, RegistryName: str, Limit: int = None, NextToken: str = None
    ) -> SearchSchemasResponseTypeDef:
        """
        [Client.search_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.search_schemas)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_discoverer(self, DiscovererId: str) -> StartDiscovererResponseTypeDef:
        """
        [Client.start_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.start_discoverer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_discoverer(self, DiscovererId: str) -> StopDiscovererResponseTypeDef:
        """
        [Client.stop_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.stop_discoverer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unlock_service_linked_role(self, RoleArn: str) -> Dict[str, Any]:
        """
        [Client.unlock_service_linked_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.unlock_service_linked_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_discoverer(
        self, DiscovererId: str, Description: str = None
    ) -> UpdateDiscovererResponseTypeDef:
        """
        [Client.update_discoverer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.update_discoverer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_registry(
        self, RegistryName: str, Description: str = None
    ) -> UpdateRegistryResponseTypeDef:
        """
        [Client.update_registry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.update_registry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_schema(
        self,
        RegistryName: str,
        SchemaName: str,
        ClientTokenId: str = None,
        Content: str = None,
        Description: str = None,
        Type: Literal["OpenApi3"] = None,
    ) -> UpdateSchemaResponseTypeDef:
        """
        [Client.update_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Client.update_schema)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_discoverers"]
    ) -> paginator_scope.ListDiscoverersPaginator:
        """
        [Paginator.ListDiscoverers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Paginator.ListDiscoverers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_registries"]
    ) -> paginator_scope.ListRegistriesPaginator:
        """
        [Paginator.ListRegistries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Paginator.ListRegistries)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_schema_versions"]
    ) -> paginator_scope.ListSchemaVersionsPaginator:
        """
        [Paginator.ListSchemaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Paginator.ListSchemaVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_schemas"]
    ) -> paginator_scope.ListSchemasPaginator:
        """
        [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Paginator.ListSchemas)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["search_schemas"]
    ) -> paginator_scope.SearchSchemasPaginator:
        """
        [Paginator.SearchSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Paginator.SearchSchemas)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["code_binding_exists"]
    ) -> waiter_scope.CodeBindingExistsWaiter:
        """
        [Waiter.CodeBindingExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/schemas.html#Schemas.Waiter.CodeBindingExists)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    GoneException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
