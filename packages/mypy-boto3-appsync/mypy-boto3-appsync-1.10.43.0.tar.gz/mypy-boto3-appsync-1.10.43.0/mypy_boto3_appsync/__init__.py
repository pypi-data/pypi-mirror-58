"Main interface for appsync service"
from mypy_boto3_appsync.client import AppSyncClient as Client, AppSyncClient
from mypy_boto3_appsync.paginator import (
    ListApiKeysPaginator,
    ListDataSourcesPaginator,
    ListFunctionsPaginator,
    ListGraphqlApisPaginator,
    ListResolversByFunctionPaginator,
    ListResolversPaginator,
    ListTypesPaginator,
)


__all__ = (
    "AppSyncClient",
    "Client",
    "ListApiKeysPaginator",
    "ListDataSourcesPaginator",
    "ListFunctionsPaginator",
    "ListGraphqlApisPaginator",
    "ListResolversByFunctionPaginator",
    "ListResolversPaginator",
    "ListTypesPaginator",
)
