"Main interface for schemas service"
from mypy_boto3_schemas.client import SchemasClient as Client, SchemasClient
from mypy_boto3_schemas.paginator import (
    ListDiscoverersPaginator,
    ListRegistriesPaginator,
    ListSchemaVersionsPaginator,
    ListSchemasPaginator,
    SearchSchemasPaginator,
)
from mypy_boto3_schemas.waiter import CodeBindingExistsWaiter


__all__ = (
    "Client",
    "CodeBindingExistsWaiter",
    "ListDiscoverersPaginator",
    "ListRegistriesPaginator",
    "ListSchemaVersionsPaginator",
    "ListSchemasPaginator",
    "SchemasClient",
    "SearchSchemasPaginator",
)
