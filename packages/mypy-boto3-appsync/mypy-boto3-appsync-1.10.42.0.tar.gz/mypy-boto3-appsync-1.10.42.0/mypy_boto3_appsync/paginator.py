"Main interface for appsync service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_appsync.type_defs import (
    ListApiKeysResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListFunctionsResponseTypeDef,
    ListGraphqlApisResponseTypeDef,
    ListResolversByFunctionResponseTypeDef,
    ListResolversResponseTypeDef,
    ListTypesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListApiKeysPaginator",
    "ListDataSourcesPaginator",
    "ListFunctionsPaginator",
    "ListGraphqlApisPaginator",
    "ListResolversPaginator",
    "ListResolversByFunctionPaginator",
    "ListTypesPaginator",
)


class ListApiKeysPaginator(Boto3Paginator):
    """
    [Paginator.ListApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListApiKeys)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, apiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListApiKeysResponseTypeDef, None, None]:
        """
        [ListApiKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListApiKeys.paginate)
        """


class ListDataSourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListDataSources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, apiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDataSourcesResponseTypeDef, None, None]:
        """
        [ListDataSources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListDataSources.paginate)
        """


class ListFunctionsPaginator(Boto3Paginator):
    """
    [Paginator.ListFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListFunctions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, apiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFunctionsResponseTypeDef, None, None]:
        """
        [ListFunctions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListFunctions.paginate)
        """


class ListGraphqlApisPaginator(Boto3Paginator):
    """
    [Paginator.ListGraphqlApis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListGraphqlApis)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGraphqlApisResponseTypeDef, None, None]:
        """
        [ListGraphqlApis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListGraphqlApis.paginate)
        """


class ListResolversPaginator(Boto3Paginator):
    """
    [Paginator.ListResolvers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListResolvers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, apiId: str, typeName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListResolversResponseTypeDef, None, None]:
        """
        [ListResolvers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListResolvers.paginate)
        """


class ListResolversByFunctionPaginator(Boto3Paginator):
    """
    [Paginator.ListResolversByFunction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListResolversByFunction)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, apiId: str, functionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListResolversByFunctionResponseTypeDef, None, None]:
        """
        [ListResolversByFunction.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListResolversByFunction.paginate)
        """


class ListTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        apiId: str,
        format: Literal["SDL", "JSON"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTypesResponseTypeDef, None, None]:
        """
        [ListTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/appsync.html#AppSync.Paginator.ListTypes.paginate)
        """
