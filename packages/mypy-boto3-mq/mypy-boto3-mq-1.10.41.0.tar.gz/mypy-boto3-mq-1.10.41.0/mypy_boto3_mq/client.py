"Main interface for mq service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_mq.client as client_scope

# pylint: disable=import-self
import mypy_boto3_mq.paginator as paginator_scope
from mypy_boto3_mq.type_defs import (
    ConfigurationIdTypeDef,
    CreateBrokerResponseTypeDef,
    CreateConfigurationResponseTypeDef,
    DeleteBrokerResponseTypeDef,
    DescribeBrokerEngineTypesResponseTypeDef,
    DescribeBrokerInstanceOptionsResponseTypeDef,
    DescribeBrokerResponseTypeDef,
    DescribeConfigurationResponseTypeDef,
    DescribeConfigurationRevisionResponseTypeDef,
    DescribeUserResponseTypeDef,
    EncryptionOptionsTypeDef,
    ListBrokersResponseTypeDef,
    ListConfigurationRevisionsResponseTypeDef,
    ListConfigurationsResponseTypeDef,
    ListTagsResponseTypeDef,
    ListUsersResponseTypeDef,
    LogsTypeDef,
    UpdateBrokerResponseTypeDef,
    UpdateConfigurationResponseTypeDef,
    UserTypeDef,
    WeeklyStartTimeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MQClient",)


class MQClient(BaseClient):
    """
    [MQ.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_broker(
        self,
        AutoMinorVersionUpgrade: bool = None,
        BrokerName: str = None,
        Configuration: ConfigurationIdTypeDef = None,
        CreatorRequestId: str = None,
        DeploymentMode: Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ"] = None,
        EncryptionOptions: EncryptionOptionsTypeDef = None,
        EngineType: Literal["ACTIVEMQ"] = None,
        EngineVersion: str = None,
        HostInstanceType: str = None,
        Logs: LogsTypeDef = None,
        MaintenanceWindowStartTime: WeeklyStartTimeTypeDef = None,
        PubliclyAccessible: bool = None,
        SecurityGroups: List[str] = None,
        StorageType: Literal["EBS", "EFS"] = None,
        SubnetIds: List[str] = None,
        Tags: Dict[str, str] = None,
        Users: List[UserTypeDef] = None,
    ) -> CreateBrokerResponseTypeDef:
        """
        [Client.create_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.create_broker)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_configuration(
        self,
        EngineType: Literal["ACTIVEMQ"] = None,
        EngineVersion: str = None,
        Name: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateConfigurationResponseTypeDef:
        """
        [Client.create_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.create_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(self, ResourceArn: str, Tags: Dict[str, str] = None) -> None:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user(
        self,
        BrokerId: str,
        Username: str,
        ConsoleAccess: bool = None,
        Groups: List[str] = None,
        Password: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.create_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_broker(self, BrokerId: str) -> DeleteBrokerResponseTypeDef:
        """
        [Client.delete_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.delete_broker)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tags(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.delete_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user(self, BrokerId: str, Username: str) -> Dict[str, Any]:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.delete_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_broker(self, BrokerId: str) -> DescribeBrokerResponseTypeDef:
        """
        [Client.describe_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.describe_broker)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_broker_engine_types(
        self, EngineType: str = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBrokerEngineTypesResponseTypeDef:
        """
        [Client.describe_broker_engine_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.describe_broker_engine_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_broker_instance_options(
        self,
        EngineType: str = None,
        HostInstanceType: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        StorageType: str = None,
    ) -> DescribeBrokerInstanceOptionsResponseTypeDef:
        """
        [Client.describe_broker_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.describe_broker_instance_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_configuration(self, ConfigurationId: str) -> DescribeConfigurationResponseTypeDef:
        """
        [Client.describe_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.describe_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_configuration_revision(
        self, ConfigurationId: str, ConfigurationRevision: str
    ) -> DescribeConfigurationRevisionResponseTypeDef:
        """
        [Client.describe_configuration_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.describe_configuration_revision)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user(self, BrokerId: str, Username: str) -> DescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.describe_user)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_brokers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListBrokersResponseTypeDef:
        """
        [Client.list_brokers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.list_brokers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configuration_revisions(
        self, ConfigurationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListConfigurationRevisionsResponseTypeDef:
        """
        [Client.list_configuration_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.list_configuration_revisions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListConfigurationsResponseTypeDef:
        """
        [Client.list_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.list_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags(self, ResourceArn: str) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.list_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_users(
        self, BrokerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.list_users)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot_broker(self, BrokerId: str) -> Dict[str, Any]:
        """
        [Client.reboot_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.reboot_broker)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_broker(
        self,
        BrokerId: str,
        AutoMinorVersionUpgrade: bool = None,
        Configuration: ConfigurationIdTypeDef = None,
        EngineVersion: str = None,
        HostInstanceType: str = None,
        Logs: LogsTypeDef = None,
        SecurityGroups: List[str] = None,
    ) -> UpdateBrokerResponseTypeDef:
        """
        [Client.update_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.update_broker)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_configuration(
        self, ConfigurationId: str, Data: str = None, Description: str = None
    ) -> UpdateConfigurationResponseTypeDef:
        """
        [Client.update_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.update_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user(
        self,
        BrokerId: str,
        Username: str,
        ConsoleAccess: bool = None,
        Groups: List[str] = None,
        Password: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Client.update_user)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_brokers"]
    ) -> paginator_scope.ListBrokersPaginator:
        """
        [Paginator.ListBrokers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mq.html#MQ.Paginator.ListBrokers)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
