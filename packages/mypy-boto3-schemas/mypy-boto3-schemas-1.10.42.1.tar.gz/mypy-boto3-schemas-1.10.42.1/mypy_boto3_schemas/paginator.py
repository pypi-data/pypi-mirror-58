"Main interface for schemas service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_schemas.type_defs import (
    ListDiscoverersResponseTypeDef,
    ListRegistriesResponseTypeDef,
    ListSchemaVersionsResponseTypeDef,
    ListSchemasResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchSchemasResponseTypeDef,
)


__all__ = (
    "ListDiscoverersPaginator",
    "ListRegistriesPaginator",
    "ListSchemaVersionsPaginator",
    "ListSchemasPaginator",
    "SearchSchemasPaginator",
)


class ListDiscoverersPaginator(Boto3Paginator):
    """
    [Paginator.ListDiscoverers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/schemas.html#Schemas.Paginator.ListDiscoverers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DiscovererIdPrefix: str = None,
        SourceArnPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDiscoverersResponseTypeDef, None, None]:
        """
        [ListDiscoverers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/schemas.html#Schemas.Paginator.ListDiscoverers.paginate)
        """


class ListRegistriesPaginator(Boto3Paginator):
    """
    [Paginator.ListRegistries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/schemas.html#Schemas.Paginator.ListRegistries)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RegistryNamePrefix: str = None,
        Scope: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRegistriesResponseTypeDef, None, None]:
        """
        [ListRegistries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/schemas.html#Schemas.Paginator.ListRegistries.paginate)
        """


class ListSchemaVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSchemaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/schemas.html#Schemas.Paginator.ListSchemaVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, RegistryName: str, SchemaName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSchemaVersionsResponseTypeDef, None, None]:
        """
        [ListSchemaVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/schemas.html#Schemas.Paginator.ListSchemaVersions.paginate)
        """


class ListSchemasPaginator(Boto3Paginator):
    """
    [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/schemas.html#Schemas.Paginator.ListSchemas)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RegistryName: str,
        SchemaNamePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListSchemasResponseTypeDef, None, None]:
        """
        [ListSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/schemas.html#Schemas.Paginator.ListSchemas.paginate)
        """


class SearchSchemasPaginator(Boto3Paginator):
    """
    [Paginator.SearchSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/schemas.html#Schemas.Paginator.SearchSchemas)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Keywords: str, RegistryName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[SearchSchemasResponseTypeDef, None, None]:
        """
        [SearchSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/schemas.html#Schemas.Paginator.SearchSchemas.paginate)
        """
