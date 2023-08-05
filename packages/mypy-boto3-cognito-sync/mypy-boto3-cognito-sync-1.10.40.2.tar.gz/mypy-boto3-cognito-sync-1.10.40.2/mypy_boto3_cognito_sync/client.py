"Main interface for cognito-sync service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_cognito_sync.client as client_scope
from mypy_boto3_cognito_sync.type_defs import (
    BulkPublishResponseTypeDef,
    CognitoStreamsTypeDef,
    DeleteDatasetResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeIdentityPoolUsageResponseTypeDef,
    DescribeIdentityUsageResponseTypeDef,
    GetBulkPublishDetailsResponseTypeDef,
    GetCognitoEventsResponseTypeDef,
    GetIdentityPoolConfigurationResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListIdentityPoolUsageResponseTypeDef,
    ListRecordsResponseTypeDef,
    PushSyncTypeDef,
    RecordPatchTypeDef,
    RegisterDeviceResponseTypeDef,
    SetIdentityPoolConfigurationResponseTypeDef,
    UpdateRecordsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CognitoSyncClient",)


class CognitoSyncClient(BaseClient):
    """
    [CognitoSync.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def bulk_publish(self, IdentityPoolId: str) -> BulkPublishResponseTypeDef:
        """
        [Client.bulk_publish documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.bulk_publish)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str
    ) -> DeleteDatasetResponseTypeDef:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.delete_dataset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str
    ) -> DescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.describe_dataset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_identity_pool_usage(
        self, IdentityPoolId: str
    ) -> DescribeIdentityPoolUsageResponseTypeDef:
        """
        [Client.describe_identity_pool_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.describe_identity_pool_usage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_identity_usage(
        self, IdentityPoolId: str, IdentityId: str
    ) -> DescribeIdentityUsageResponseTypeDef:
        """
        [Client.describe_identity_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.describe_identity_usage)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bulk_publish_details(self, IdentityPoolId: str) -> GetBulkPublishDetailsResponseTypeDef:
        """
        [Client.get_bulk_publish_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.get_bulk_publish_details)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cognito_events(self, IdentityPoolId: str) -> GetCognitoEventsResponseTypeDef:
        """
        [Client.get_cognito_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.get_cognito_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_identity_pool_configuration(
        self, IdentityPoolId: str
    ) -> GetIdentityPoolConfigurationResponseTypeDef:
        """
        [Client.get_identity_pool_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.get_identity_pool_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_datasets(
        self, IdentityPoolId: str, IdentityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.list_datasets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_identity_pool_usage(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListIdentityPoolUsageResponseTypeDef:
        """
        [Client.list_identity_pool_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.list_identity_pool_usage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_records(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        LastSyncCount: int = None,
        NextToken: str = None,
        MaxResults: int = None,
        SyncSessionToken: str = None,
    ) -> ListRecordsResponseTypeDef:
        """
        [Client.list_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.list_records)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_device(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        Platform: Literal["APNS", "APNS_SANDBOX", "GCM", "ADM"],
        Token: str,
    ) -> RegisterDeviceResponseTypeDef:
        """
        [Client.register_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.register_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_cognito_events(self, IdentityPoolId: str, Events: Dict[str, str]) -> None:
        """
        [Client.set_cognito_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.set_cognito_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_identity_pool_configuration(
        self,
        IdentityPoolId: str,
        PushSync: PushSyncTypeDef = None,
        CognitoStreams: CognitoStreamsTypeDef = None,
    ) -> SetIdentityPoolConfigurationResponseTypeDef:
        """
        [Client.set_identity_pool_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.set_identity_pool_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def subscribe_to_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str
    ) -> Dict[str, Any]:
        """
        [Client.subscribe_to_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.subscribe_to_dataset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unsubscribe_from_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str
    ) -> Dict[str, Any]:
        """
        [Client.unsubscribe_from_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.unsubscribe_from_dataset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_records(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        SyncSessionToken: str,
        DeviceId: str = None,
        RecordPatches: List[RecordPatchTypeDef] = None,
        ClientContext: str = None,
    ) -> UpdateRecordsResponseTypeDef:
        """
        [Client.update_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cognito-sync.html#CognitoSync.Client.update_records)
        """


class Exceptions:
    AlreadyStreamedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    DuplicateRequestException: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidConfigurationException: Boto3ClientError
    InvalidLambdaFunctionOutputException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    LambdaThrottledException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
