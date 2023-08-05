"Main interface for appconfig service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_appconfig.client as client_scope
from mypy_boto3_appconfig.type_defs import (
    ApplicationTypeDef,
    ApplicationsTypeDef,
    ConfigurationProfileTypeDef,
    ConfigurationProfilesTypeDef,
    ConfigurationTypeDef,
    DeploymentStrategiesTypeDef,
    DeploymentStrategyTypeDef,
    DeploymentTypeDef,
    DeploymentsTypeDef,
    EnvironmentTypeDef,
    EnvironmentsTypeDef,
    MonitorTypeDef,
    ResourceTagsTypeDef,
    ValidatorTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AppConfigClient",)


class AppConfigClient(BaseClient):
    """
    [AppConfig.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_application(
        self, Name: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> ApplicationTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.create_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_configuration_profile(
        self,
        ApplicationId: str,
        Name: str,
        LocationUri: str,
        RetrievalRoleArn: str,
        Description: str = None,
        Validators: List[ValidatorTypeDef] = None,
        Tags: Dict[str, str] = None,
    ) -> ConfigurationProfileTypeDef:
        """
        [Client.create_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.create_configuration_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_deployment_strategy(
        self,
        Name: str,
        DeploymentDurationInMinutes: int,
        GrowthFactor: float,
        ReplicateTo: Literal["NONE", "SSM_DOCUMENT"],
        Description: str = None,
        FinalBakeTimeInMinutes: int = None,
        GrowthType: Literal["LINEAR"] = None,
        Tags: Dict[str, str] = None,
    ) -> DeploymentStrategyTypeDef:
        """
        [Client.create_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.create_deployment_strategy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_environment(
        self,
        ApplicationId: str,
        Name: str,
        Description: str = None,
        Monitors: List[MonitorTypeDef] = None,
        Tags: Dict[str, str] = None,
    ) -> EnvironmentTypeDef:
        """
        [Client.create_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.create_environment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_application(self, ApplicationId: str) -> None:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.delete_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_profile(self, ApplicationId: str, ConfigurationProfileId: str) -> None:
        """
        [Client.delete_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.delete_configuration_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_deployment_strategy(self, DeploymentStrategyId: str) -> None:
        """
        [Client.delete_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.delete_deployment_strategy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_environment(self, ApplicationId: str, EnvironmentId: str) -> None:
        """
        [Client.delete_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.delete_environment)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_application(self, ApplicationId: str) -> ApplicationTypeDef:
        """
        [Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.get_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_configuration(
        self,
        Application: str,
        Environment: str,
        Configuration: str,
        ClientId: str,
        ClientConfigurationVersion: str = None,
    ) -> ConfigurationTypeDef:
        """
        [Client.get_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.get_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_configuration_profile(
        self, ApplicationId: str, ConfigurationProfileId: str
    ) -> ConfigurationProfileTypeDef:
        """
        [Client.get_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.get_configuration_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deployment(
        self, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> DeploymentTypeDef:
        """
        [Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.get_deployment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deployment_strategy(self, DeploymentStrategyId: str) -> DeploymentStrategyTypeDef:
        """
        [Client.get_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.get_deployment_strategy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_environment(self, ApplicationId: str, EnvironmentId: str) -> EnvironmentTypeDef:
        """
        [Client.get_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.get_environment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_applications(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ApplicationsTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.list_applications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configuration_profiles(
        self, ApplicationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ConfigurationProfilesTypeDef:
        """
        [Client.list_configuration_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.list_configuration_profiles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deployment_strategies(
        self, MaxResults: int = None, NextToken: str = None
    ) -> DeploymentStrategiesTypeDef:
        """
        [Client.list_deployment_strategies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.list_deployment_strategies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deployments(
        self, ApplicationId: str, EnvironmentId: str, MaxResults: int = None, NextToken: str = None
    ) -> DeploymentsTypeDef:
        """
        [Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.list_deployments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_environments(
        self, ApplicationId: str, MaxResults: int = None, NextToken: str = None
    ) -> EnvironmentsTypeDef:
        """
        [Client.list_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.list_environments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ResourceTagsTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_deployment(
        self,
        ApplicationId: str,
        EnvironmentId: str,
        DeploymentStrategyId: str,
        ConfigurationProfileId: str,
        ConfigurationVersion: str,
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> DeploymentTypeDef:
        """
        [Client.start_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.start_deployment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_deployment(
        self, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> DeploymentTypeDef:
        """
        [Client.stop_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.stop_deployment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_application(
        self, ApplicationId: str, Name: str = None, Description: str = None
    ) -> ApplicationTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.update_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_configuration_profile(
        self,
        ApplicationId: str,
        ConfigurationProfileId: str,
        Name: str = None,
        Description: str = None,
        RetrievalRoleArn: str = None,
        Validators: List[ValidatorTypeDef] = None,
    ) -> ConfigurationProfileTypeDef:
        """
        [Client.update_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.update_configuration_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_deployment_strategy(
        self,
        DeploymentStrategyId: str,
        Description: str = None,
        DeploymentDurationInMinutes: int = None,
        FinalBakeTimeInMinutes: int = None,
        GrowthFactor: float = None,
        GrowthType: Literal["LINEAR"] = None,
    ) -> DeploymentStrategyTypeDef:
        """
        [Client.update_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.update_deployment_strategy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_environment(
        self,
        ApplicationId: str,
        EnvironmentId: str,
        Name: str = None,
        Description: str = None,
        Monitors: List[MonitorTypeDef] = None,
    ) -> EnvironmentTypeDef:
        """
        [Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.update_environment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def validate_configuration(
        self, ApplicationId: str, ConfigurationProfileId: str, ConfigurationVersion: str
    ) -> None:
        """
        [Client.validate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/appconfig.html#AppConfig.Client.validate_configuration)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
