"Main interface for lambda service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, IO, List, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_lambda.client as client_scope

# pylint: disable=import-self
import mypy_boto3_lambda.paginator as paginator_scope
from mypy_boto3_lambda.type_defs import (
    AddLayerVersionPermissionResponseTypeDef,
    AddPermissionResponseTypeDef,
    AliasConfigurationTypeDef,
    AliasRoutingConfigurationTypeDef,
    ConcurrencyTypeDef,
    DeadLetterConfigTypeDef,
    DestinationConfigTypeDef,
    EnvironmentTypeDef,
    EventSourceMappingConfigurationTypeDef,
    FunctionCodeTypeDef,
    FunctionConfigurationTypeDef,
    FunctionEventInvokeConfigTypeDef,
    GetAccountSettingsResponseTypeDef,
    GetFunctionConcurrencyResponseTypeDef,
    GetFunctionResponseTypeDef,
    GetLayerVersionPolicyResponseTypeDef,
    GetLayerVersionResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetProvisionedConcurrencyConfigResponseTypeDef,
    InvocationResponseTypeDef,
    InvokeAsyncResponseTypeDef,
    LayerVersionContentInputTypeDef,
    ListAliasesResponseTypeDef,
    ListEventSourceMappingsResponseTypeDef,
    ListFunctionEventInvokeConfigsResponseTypeDef,
    ListFunctionsResponseTypeDef,
    ListLayerVersionsResponseTypeDef,
    ListLayersResponseTypeDef,
    ListProvisionedConcurrencyConfigsResponseTypeDef,
    ListTagsResponseTypeDef,
    ListVersionsByFunctionResponseTypeDef,
    PublishLayerVersionResponseTypeDef,
    PutProvisionedConcurrencyConfigResponseTypeDef,
    TracingConfigTypeDef,
    VpcConfigTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_lambda.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LambdaClient",)


class LambdaClient(BaseClient):
    """
    [Lambda.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_layer_version_permission(
        self,
        LayerName: str,
        VersionNumber: int,
        StatementId: str,
        Action: str,
        Principal: str,
        OrganizationId: str = None,
        RevisionId: str = None,
    ) -> AddLayerVersionPermissionResponseTypeDef:
        """
        [Client.add_layer_version_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.add_layer_version_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_permission(
        self,
        FunctionName: str,
        StatementId: str,
        Action: str,
        Principal: str,
        SourceArn: str = None,
        SourceAccount: str = None,
        EventSourceToken: str = None,
        Qualifier: str = None,
        RevisionId: str = None,
    ) -> AddPermissionResponseTypeDef:
        """
        [Client.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.add_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_alias(
        self,
        FunctionName: str,
        Name: str,
        FunctionVersion: str,
        Description: str = None,
        RoutingConfig: AliasRoutingConfigurationTypeDef = None,
    ) -> AliasConfigurationTypeDef:
        """
        [Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.create_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_event_source_mapping(
        self,
        EventSourceArn: str,
        FunctionName: str,
        Enabled: bool = None,
        BatchSize: int = None,
        MaximumBatchingWindowInSeconds: int = None,
        ParallelizationFactor: int = None,
        StartingPosition: Literal["TRIM_HORIZON", "LATEST", "AT_TIMESTAMP"] = None,
        StartingPositionTimestamp: datetime = None,
        DestinationConfig: DestinationConfigTypeDef = None,
        MaximumRecordAgeInSeconds: int = None,
        BisectBatchOnFunctionError: bool = None,
        MaximumRetryAttempts: int = None,
    ) -> EventSourceMappingConfigurationTypeDef:
        """
        [Client.create_event_source_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.create_event_source_mapping)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_function(
        self,
        FunctionName: str,
        Runtime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        Role: str,
        Handler: str,
        Code: FunctionCodeTypeDef,
        Description: str = None,
        Timeout: int = None,
        MemorySize: int = None,
        Publish: bool = None,
        VpcConfig: VpcConfigTypeDef = None,
        DeadLetterConfig: DeadLetterConfigTypeDef = None,
        Environment: EnvironmentTypeDef = None,
        KMSKeyArn: str = None,
        TracingConfig: TracingConfigTypeDef = None,
        Tags: Dict[str, str] = None,
        Layers: List[str] = None,
    ) -> FunctionConfigurationTypeDef:
        """
        [Client.create_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.create_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_alias(self, FunctionName: str, Name: str) -> None:
        """
        [Client.delete_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.delete_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_event_source_mapping(self, UUID: str) -> EventSourceMappingConfigurationTypeDef:
        """
        [Client.delete_event_source_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.delete_event_source_mapping)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_function(self, FunctionName: str, Qualifier: str = None) -> None:
        """
        [Client.delete_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.delete_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_function_concurrency(self, FunctionName: str) -> None:
        """
        [Client.delete_function_concurrency documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.delete_function_concurrency)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_function_event_invoke_config(self, FunctionName: str, Qualifier: str = None) -> None:
        """
        [Client.delete_function_event_invoke_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.delete_function_event_invoke_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_layer_version(self, LayerName: str, VersionNumber: int) -> None:
        """
        [Client.delete_layer_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.delete_layer_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_provisioned_concurrency_config(self, FunctionName: str, Qualifier: str) -> None:
        """
        [Client.delete_provisioned_concurrency_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.delete_provisioned_concurrency_config)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_account_settings(self) -> GetAccountSettingsResponseTypeDef:
        """
        [Client.get_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_account_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_alias(self, FunctionName: str, Name: str) -> AliasConfigurationTypeDef:
        """
        [Client.get_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_event_source_mapping(self, UUID: str) -> EventSourceMappingConfigurationTypeDef:
        """
        [Client.get_event_source_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_event_source_mapping)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function(self, FunctionName: str, Qualifier: str = None) -> GetFunctionResponseTypeDef:
        """
        [Client.get_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_concurrency(self, FunctionName: str) -> GetFunctionConcurrencyResponseTypeDef:
        """
        [Client.get_function_concurrency documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_function_concurrency)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_configuration(
        self, FunctionName: str, Qualifier: str = None
    ) -> FunctionConfigurationTypeDef:
        """
        [Client.get_function_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_function_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_event_invoke_config(
        self, FunctionName: str, Qualifier: str = None
    ) -> FunctionEventInvokeConfigTypeDef:
        """
        [Client.get_function_event_invoke_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_function_event_invoke_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_layer_version(
        self, LayerName: str, VersionNumber: int
    ) -> GetLayerVersionResponseTypeDef:
        """
        [Client.get_layer_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_layer_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_layer_version_by_arn(self, Arn: str) -> GetLayerVersionResponseTypeDef:
        """
        [Client.get_layer_version_by_arn documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_layer_version_by_arn)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_layer_version_policy(
        self, LayerName: str, VersionNumber: int
    ) -> GetLayerVersionPolicyResponseTypeDef:
        """
        [Client.get_layer_version_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_layer_version_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_policy(self, FunctionName: str, Qualifier: str = None) -> GetPolicyResponseTypeDef:
        """
        [Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_provisioned_concurrency_config(
        self, FunctionName: str, Qualifier: str
    ) -> GetProvisionedConcurrencyConfigResponseTypeDef:
        """
        [Client.get_provisioned_concurrency_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.get_provisioned_concurrency_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invoke(
        self,
        FunctionName: str,
        InvocationType: Literal["Event", "RequestResponse", "DryRun"] = None,
        LogType: Literal["None", "Tail"] = None,
        ClientContext: str = None,
        Payload: Union[bytes, IO] = None,
        Qualifier: str = None,
    ) -> InvocationResponseTypeDef:
        """
        [Client.invoke documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.invoke)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invoke_async(
        self, FunctionName: str, InvokeArgs: Union[bytes, IO]
    ) -> InvokeAsyncResponseTypeDef:
        """
        [Client.invoke_async documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.invoke_async)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_aliases(
        self,
        FunctionName: str,
        FunctionVersion: str = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListAliasesResponseTypeDef:
        """
        [Client.list_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.list_aliases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_event_source_mappings(
        self,
        EventSourceArn: str = None,
        FunctionName: str = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListEventSourceMappingsResponseTypeDef:
        """
        [Client.list_event_source_mappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.list_event_source_mappings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_function_event_invoke_configs(
        self, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ListFunctionEventInvokeConfigsResponseTypeDef:
        """
        [Client.list_function_event_invoke_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.list_function_event_invoke_configs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_functions(
        self,
        MasterRegion: str = None,
        FunctionVersion: Literal["ALL"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListFunctionsResponseTypeDef:
        """
        [Client.list_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.list_functions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_layer_versions(
        self,
        LayerName: str,
        CompatibleRuntime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListLayerVersionsResponseTypeDef:
        """
        [Client.list_layer_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.list_layer_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_layers(
        self,
        CompatibleRuntime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListLayersResponseTypeDef:
        """
        [Client.list_layers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.list_layers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_provisioned_concurrency_configs(
        self, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ListProvisionedConcurrencyConfigsResponseTypeDef:
        """
        [Client.list_provisioned_concurrency_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.list_provisioned_concurrency_configs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags(self, Resource: str) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.list_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_versions_by_function(
        self, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ListVersionsByFunctionResponseTypeDef:
        """
        [Client.list_versions_by_function documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.list_versions_by_function)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def publish_layer_version(
        self,
        LayerName: str,
        Content: LayerVersionContentInputTypeDef,
        Description: str = None,
        CompatibleRuntimes: List[
            Literal[
                "nodejs",
                "nodejs4.3",
                "nodejs6.10",
                "nodejs8.10",
                "nodejs10.x",
                "nodejs12.x",
                "java8",
                "java11",
                "python2.7",
                "python3.6",
                "python3.7",
                "python3.8",
                "dotnetcore1.0",
                "dotnetcore2.0",
                "dotnetcore2.1",
                "nodejs4.3-edge",
                "go1.x",
                "ruby2.5",
                "provided",
            ]
        ] = None,
        LicenseInfo: str = None,
    ) -> PublishLayerVersionResponseTypeDef:
        """
        [Client.publish_layer_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.publish_layer_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def publish_version(
        self,
        FunctionName: str,
        CodeSha256: str = None,
        Description: str = None,
        RevisionId: str = None,
    ) -> FunctionConfigurationTypeDef:
        """
        [Client.publish_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.publish_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_function_concurrency(
        self, FunctionName: str, ReservedConcurrentExecutions: int
    ) -> ConcurrencyTypeDef:
        """
        [Client.put_function_concurrency documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.put_function_concurrency)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_function_event_invoke_config(
        self,
        FunctionName: str,
        Qualifier: str = None,
        MaximumRetryAttempts: int = None,
        MaximumEventAgeInSeconds: int = None,
        DestinationConfig: DestinationConfigTypeDef = None,
    ) -> FunctionEventInvokeConfigTypeDef:
        """
        [Client.put_function_event_invoke_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.put_function_event_invoke_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_provisioned_concurrency_config(
        self, FunctionName: str, Qualifier: str, ProvisionedConcurrentExecutions: int
    ) -> PutProvisionedConcurrencyConfigResponseTypeDef:
        """
        [Client.put_provisioned_concurrency_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.put_provisioned_concurrency_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_layer_version_permission(
        self, LayerName: str, VersionNumber: int, StatementId: str, RevisionId: str = None
    ) -> None:
        """
        [Client.remove_layer_version_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.remove_layer_version_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_permission(
        self, FunctionName: str, StatementId: str, Qualifier: str = None, RevisionId: str = None
    ) -> None:
        """
        [Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.remove_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, Resource: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, Resource: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_alias(
        self,
        FunctionName: str,
        Name: str,
        FunctionVersion: str = None,
        Description: str = None,
        RoutingConfig: AliasRoutingConfigurationTypeDef = None,
        RevisionId: str = None,
    ) -> AliasConfigurationTypeDef:
        """
        [Client.update_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.update_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_event_source_mapping(
        self,
        UUID: str,
        FunctionName: str = None,
        Enabled: bool = None,
        BatchSize: int = None,
        MaximumBatchingWindowInSeconds: int = None,
        DestinationConfig: DestinationConfigTypeDef = None,
        MaximumRecordAgeInSeconds: int = None,
        BisectBatchOnFunctionError: bool = None,
        MaximumRetryAttempts: int = None,
        ParallelizationFactor: int = None,
    ) -> EventSourceMappingConfigurationTypeDef:
        """
        [Client.update_event_source_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.update_event_source_mapping)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_function_code(
        self,
        FunctionName: str,
        ZipFile: Union[bytes, IO] = None,
        S3Bucket: str = None,
        S3Key: str = None,
        S3ObjectVersion: str = None,
        Publish: bool = None,
        DryRun: bool = None,
        RevisionId: str = None,
    ) -> FunctionConfigurationTypeDef:
        """
        [Client.update_function_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.update_function_code)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_function_configuration(
        self,
        FunctionName: str,
        Role: str = None,
        Handler: str = None,
        Description: str = None,
        Timeout: int = None,
        MemorySize: int = None,
        VpcConfig: VpcConfigTypeDef = None,
        Environment: EnvironmentTypeDef = None,
        Runtime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ] = None,
        DeadLetterConfig: DeadLetterConfigTypeDef = None,
        KMSKeyArn: str = None,
        TracingConfig: TracingConfigTypeDef = None,
        RevisionId: str = None,
        Layers: List[str] = None,
    ) -> FunctionConfigurationTypeDef:
        """
        [Client.update_function_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.update_function_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_function_event_invoke_config(
        self,
        FunctionName: str,
        Qualifier: str = None,
        MaximumRetryAttempts: int = None,
        MaximumEventAgeInSeconds: int = None,
        DestinationConfig: DestinationConfigTypeDef = None,
    ) -> FunctionEventInvokeConfigTypeDef:
        """
        [Client.update_function_event_invoke_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Client.update_function_event_invoke_config)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_aliases"]
    ) -> paginator_scope.ListAliasesPaginator:
        """
        [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Paginator.ListAliases)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_event_source_mappings"]
    ) -> paginator_scope.ListEventSourceMappingsPaginator:
        """
        [Paginator.ListEventSourceMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Paginator.ListEventSourceMappings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_function_event_invoke_configs"]
    ) -> paginator_scope.ListFunctionEventInvokeConfigsPaginator:
        """
        [Paginator.ListFunctionEventInvokeConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Paginator.ListFunctionEventInvokeConfigs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_functions"]
    ) -> paginator_scope.ListFunctionsPaginator:
        """
        [Paginator.ListFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Paginator.ListFunctions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_layer_versions"]
    ) -> paginator_scope.ListLayerVersionsPaginator:
        """
        [Paginator.ListLayerVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Paginator.ListLayerVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_layers"]
    ) -> paginator_scope.ListLayersPaginator:
        """
        [Paginator.ListLayers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Paginator.ListLayers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_provisioned_concurrency_configs"]
    ) -> paginator_scope.ListProvisionedConcurrencyConfigsPaginator:
        """
        [Paginator.ListProvisionedConcurrencyConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Paginator.ListProvisionedConcurrencyConfigs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_versions_by_function"]
    ) -> paginator_scope.ListVersionsByFunctionPaginator:
        """
        [Paginator.ListVersionsByFunction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Paginator.ListVersionsByFunction)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["function_active"]
    ) -> waiter_scope.FunctionActiveWaiter:
        """
        [Waiter.FunctionActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Waiter.FunctionActive)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["function_exists"]
    ) -> waiter_scope.FunctionExistsWaiter:
        """
        [Waiter.FunctionExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Waiter.FunctionExists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["function_updated"]
    ) -> waiter_scope.FunctionUpdatedWaiter:
        """
        [Waiter.FunctionUpdated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Waiter.FunctionUpdated)
        """


class Exceptions:
    ClientError: Boto3ClientError
    CodeStorageExceededException: Boto3ClientError
    EC2AccessDeniedException: Boto3ClientError
    EC2ThrottledException: Boto3ClientError
    EC2UnexpectedException: Boto3ClientError
    ENILimitReachedException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidRequestContentException: Boto3ClientError
    InvalidRuntimeException: Boto3ClientError
    InvalidSecurityGroupIDException: Boto3ClientError
    InvalidSubnetIDException: Boto3ClientError
    InvalidZipFileException: Boto3ClientError
    KMSAccessDeniedException: Boto3ClientError
    KMSDisabledException: Boto3ClientError
    KMSInvalidStateException: Boto3ClientError
    KMSNotFoundException: Boto3ClientError
    PolicyLengthExceededException: Boto3ClientError
    PreconditionFailedException: Boto3ClientError
    ProvisionedConcurrencyConfigNotFoundException: Boto3ClientError
    RequestTooLargeException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceNotReadyException: Boto3ClientError
    ServiceException: Boto3ClientError
    SubnetIPAddressLimitReachedException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnsupportedMediaTypeException: Boto3ClientError
