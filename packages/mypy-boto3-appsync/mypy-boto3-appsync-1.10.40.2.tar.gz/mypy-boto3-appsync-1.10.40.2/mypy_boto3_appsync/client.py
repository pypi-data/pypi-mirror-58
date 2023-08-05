"Main interface for appsync service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, IO, List, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_appsync.client as client_scope

# pylint: disable=import-self
import mypy_boto3_appsync.paginator as paginator_scope
from mypy_boto3_appsync.type_defs import (
    AdditionalAuthenticationProviderTypeDef,
    CachingConfigTypeDef,
    CreateApiCacheResponseTypeDef,
    CreateApiKeyResponseTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateFunctionResponseTypeDef,
    CreateGraphqlApiResponseTypeDef,
    CreateResolverResponseTypeDef,
    CreateTypeResponseTypeDef,
    DynamodbDataSourceConfigTypeDef,
    ElasticsearchDataSourceConfigTypeDef,
    GetApiCacheResponseTypeDef,
    GetDataSourceResponseTypeDef,
    GetFunctionResponseTypeDef,
    GetGraphqlApiResponseTypeDef,
    GetIntrospectionSchemaResponseTypeDef,
    GetResolverResponseTypeDef,
    GetSchemaCreationStatusResponseTypeDef,
    GetTypeResponseTypeDef,
    HttpDataSourceConfigTypeDef,
    LambdaDataSourceConfigTypeDef,
    ListApiKeysResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListFunctionsResponseTypeDef,
    ListGraphqlApisResponseTypeDef,
    ListResolversByFunctionResponseTypeDef,
    ListResolversResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTypesResponseTypeDef,
    LogConfigTypeDef,
    OpenIDConnectConfigTypeDef,
    PipelineConfigTypeDef,
    RelationalDatabaseDataSourceConfigTypeDef,
    StartSchemaCreationResponseTypeDef,
    SyncConfigTypeDef,
    UpdateApiCacheResponseTypeDef,
    UpdateApiKeyResponseTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateFunctionResponseTypeDef,
    UpdateGraphqlApiResponseTypeDef,
    UpdateResolverResponseTypeDef,
    UpdateTypeResponseTypeDef,
    UserPoolConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AppSyncClient",)


class AppSyncClient(BaseClient):
    """
    [AppSync.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_api_cache(
        self,
        apiId: str,
        ttl: int,
        apiCachingBehavior: Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"],
        type: Literal[
            "T2_SMALL",
            "T2_MEDIUM",
            "R4_LARGE",
            "R4_XLARGE",
            "R4_2XLARGE",
            "R4_4XLARGE",
            "R4_8XLARGE",
        ],
        transitEncryptionEnabled: bool = None,
        atRestEncryptionEnabled: bool = None,
    ) -> CreateApiCacheResponseTypeDef:
        """
        [Client.create_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.create_api_cache)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_api_key(
        self, apiId: str, description: str = None, expires: int = None
    ) -> CreateApiKeyResponseTypeDef:
        """
        [Client.create_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.create_api_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_data_source(
        self,
        apiId: str,
        name: str,
        type: Literal[
            "AWS_LAMBDA",
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "NONE",
            "HTTP",
            "RELATIONAL_DATABASE",
        ],
        description: str = None,
        serviceRoleArn: str = None,
        dynamodbConfig: DynamodbDataSourceConfigTypeDef = None,
        lambdaConfig: LambdaDataSourceConfigTypeDef = None,
        elasticsearchConfig: ElasticsearchDataSourceConfigTypeDef = None,
        httpConfig: HttpDataSourceConfigTypeDef = None,
        relationalDatabaseConfig: RelationalDatabaseDataSourceConfigTypeDef = None,
    ) -> CreateDataSourceResponseTypeDef:
        """
        [Client.create_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.create_data_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_function(
        self,
        apiId: str,
        name: str,
        dataSourceName: str,
        requestMappingTemplate: str,
        functionVersion: str,
        description: str = None,
        responseMappingTemplate: str = None,
    ) -> CreateFunctionResponseTypeDef:
        """
        [Client.create_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.create_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_graphql_api(
        self,
        name: str,
        authenticationType: Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ],
        logConfig: LogConfigTypeDef = None,
        userPoolConfig: UserPoolConfigTypeDef = None,
        openIDConnectConfig: OpenIDConnectConfigTypeDef = None,
        tags: Dict[str, str] = None,
        additionalAuthenticationProviders: List[AdditionalAuthenticationProviderTypeDef] = None,
    ) -> CreateGraphqlApiResponseTypeDef:
        """
        [Client.create_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.create_graphql_api)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resolver(
        self,
        apiId: str,
        typeName: str,
        fieldName: str,
        requestMappingTemplate: str,
        dataSourceName: str = None,
        responseMappingTemplate: str = None,
        kind: Literal["UNIT", "PIPELINE"] = None,
        pipelineConfig: PipelineConfigTypeDef = None,
        syncConfig: SyncConfigTypeDef = None,
        cachingConfig: CachingConfigTypeDef = None,
    ) -> CreateResolverResponseTypeDef:
        """
        [Client.create_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.create_resolver)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_type(
        self, apiId: str, definition: str, format: Literal["SDL", "JSON"]
    ) -> CreateTypeResponseTypeDef:
        """
        [Client.create_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.create_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_api_cache(self, apiId: str) -> Dict[str, Any]:
        """
        [Client.delete_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.delete_api_cache)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_api_key(self, apiId: str, id: str) -> Dict[str, Any]:
        """
        [Client.delete_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.delete_api_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_data_source(self, apiId: str, name: str) -> Dict[str, Any]:
        """
        [Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.delete_data_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_function(self, apiId: str, functionId: str) -> Dict[str, Any]:
        """
        [Client.delete_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.delete_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_graphql_api(self, apiId: str) -> Dict[str, Any]:
        """
        [Client.delete_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.delete_graphql_api)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resolver(self, apiId: str, typeName: str, fieldName: str) -> Dict[str, Any]:
        """
        [Client.delete_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.delete_resolver)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_type(self, apiId: str, typeName: str) -> Dict[str, Any]:
        """
        [Client.delete_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.delete_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def flush_api_cache(self, apiId: str) -> Dict[str, Any]:
        """
        [Client.flush_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.flush_api_cache)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_api_cache(self, apiId: str) -> GetApiCacheResponseTypeDef:
        """
        [Client.get_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.get_api_cache)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_data_source(self, apiId: str, name: str) -> GetDataSourceResponseTypeDef:
        """
        [Client.get_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.get_data_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function(self, apiId: str, functionId: str) -> GetFunctionResponseTypeDef:
        """
        [Client.get_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.get_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_graphql_api(self, apiId: str) -> GetGraphqlApiResponseTypeDef:
        """
        [Client.get_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.get_graphql_api)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_introspection_schema(
        self, apiId: str, format: Literal["SDL", "JSON"], includeDirectives: bool = None
    ) -> GetIntrospectionSchemaResponseTypeDef:
        """
        [Client.get_introspection_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.get_introspection_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resolver(self, apiId: str, typeName: str, fieldName: str) -> GetResolverResponseTypeDef:
        """
        [Client.get_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.get_resolver)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_schema_creation_status(self, apiId: str) -> GetSchemaCreationStatusResponseTypeDef:
        """
        [Client.get_schema_creation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.get_schema_creation_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_type(
        self, apiId: str, typeName: str, format: Literal["SDL", "JSON"]
    ) -> GetTypeResponseTypeDef:
        """
        [Client.get_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.get_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_api_keys(
        self, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListApiKeysResponseTypeDef:
        """
        [Client.list_api_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.list_api_keys)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_data_sources(
        self, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        [Client.list_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.list_data_sources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_functions(
        self, apiId: str, nextToken: str = None, maxResults: int = None
    ) -> ListFunctionsResponseTypeDef:
        """
        [Client.list_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.list_functions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_graphql_apis(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListGraphqlApisResponseTypeDef:
        """
        [Client.list_graphql_apis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.list_graphql_apis)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resolvers(
        self, apiId: str, typeName: str, nextToken: str = None, maxResults: int = None
    ) -> ListResolversResponseTypeDef:
        """
        [Client.list_resolvers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.list_resolvers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resolvers_by_function(
        self, apiId: str, functionId: str, nextToken: str = None, maxResults: int = None
    ) -> ListResolversByFunctionResponseTypeDef:
        """
        [Client.list_resolvers_by_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.list_resolvers_by_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_types(
        self,
        apiId: str,
        format: Literal["SDL", "JSON"],
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListTypesResponseTypeDef:
        """
        [Client.list_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.list_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_schema_creation(
        self, apiId: str, definition: Union[bytes, IO]
    ) -> StartSchemaCreationResponseTypeDef:
        """
        [Client.start_schema_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.start_schema_creation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_api_cache(
        self,
        apiId: str,
        ttl: int,
        apiCachingBehavior: Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"],
        type: Literal[
            "T2_SMALL",
            "T2_MEDIUM",
            "R4_LARGE",
            "R4_XLARGE",
            "R4_2XLARGE",
            "R4_4XLARGE",
            "R4_8XLARGE",
        ],
    ) -> UpdateApiCacheResponseTypeDef:
        """
        [Client.update_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.update_api_cache)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_api_key(
        self, apiId: str, id: str, description: str = None, expires: int = None
    ) -> UpdateApiKeyResponseTypeDef:
        """
        [Client.update_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.update_api_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_data_source(
        self,
        apiId: str,
        name: str,
        type: Literal[
            "AWS_LAMBDA",
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "NONE",
            "HTTP",
            "RELATIONAL_DATABASE",
        ],
        description: str = None,
        serviceRoleArn: str = None,
        dynamodbConfig: DynamodbDataSourceConfigTypeDef = None,
        lambdaConfig: LambdaDataSourceConfigTypeDef = None,
        elasticsearchConfig: ElasticsearchDataSourceConfigTypeDef = None,
        httpConfig: HttpDataSourceConfigTypeDef = None,
        relationalDatabaseConfig: RelationalDatabaseDataSourceConfigTypeDef = None,
    ) -> UpdateDataSourceResponseTypeDef:
        """
        [Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.update_data_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_function(
        self,
        apiId: str,
        name: str,
        functionId: str,
        dataSourceName: str,
        requestMappingTemplate: str,
        functionVersion: str,
        description: str = None,
        responseMappingTemplate: str = None,
    ) -> UpdateFunctionResponseTypeDef:
        """
        [Client.update_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.update_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_graphql_api(
        self,
        apiId: str,
        name: str,
        logConfig: LogConfigTypeDef = None,
        authenticationType: Literal[
            "API_KEY", "AWS_IAM", "AMAZON_COGNITO_USER_POOLS", "OPENID_CONNECT"
        ] = None,
        userPoolConfig: UserPoolConfigTypeDef = None,
        openIDConnectConfig: OpenIDConnectConfigTypeDef = None,
        additionalAuthenticationProviders: List[AdditionalAuthenticationProviderTypeDef] = None,
    ) -> UpdateGraphqlApiResponseTypeDef:
        """
        [Client.update_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.update_graphql_api)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_resolver(
        self,
        apiId: str,
        typeName: str,
        fieldName: str,
        requestMappingTemplate: str,
        dataSourceName: str = None,
        responseMappingTemplate: str = None,
        kind: Literal["UNIT", "PIPELINE"] = None,
        pipelineConfig: PipelineConfigTypeDef = None,
        syncConfig: SyncConfigTypeDef = None,
        cachingConfig: CachingConfigTypeDef = None,
    ) -> UpdateResolverResponseTypeDef:
        """
        [Client.update_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.update_resolver)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_type(
        self, apiId: str, typeName: str, format: Literal["SDL", "JSON"], definition: str = None
    ) -> UpdateTypeResponseTypeDef:
        """
        [Client.update_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Client.update_type)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_api_keys"]
    ) -> paginator_scope.ListApiKeysPaginator:
        """
        [Paginator.ListApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Paginator.ListApiKeys)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> paginator_scope.ListDataSourcesPaginator:
        """
        [Paginator.ListDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Paginator.ListDataSources)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_functions"]
    ) -> paginator_scope.ListFunctionsPaginator:
        """
        [Paginator.ListFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Paginator.ListFunctions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_graphql_apis"]
    ) -> paginator_scope.ListGraphqlApisPaginator:
        """
        [Paginator.ListGraphqlApis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Paginator.ListGraphqlApis)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resolvers"]
    ) -> paginator_scope.ListResolversPaginator:
        """
        [Paginator.ListResolvers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Paginator.ListResolvers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resolvers_by_function"]
    ) -> paginator_scope.ListResolversByFunctionPaginator:
        """
        [Paginator.ListResolversByFunction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Paginator.ListResolversByFunction)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_types"]
    ) -> paginator_scope.ListTypesPaginator:
        """
        [Paginator.ListTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appsync.html#AppSync.Paginator.ListTypes)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ApiKeyLimitExceededException: Boto3ClientError
    ApiKeyValidityOutOfBoundsException: Boto3ClientError
    ApiLimitExceededException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    GraphQLSchemaException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
