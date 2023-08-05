"Main interface for greengrass service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_greengrass.client as client_scope

# pylint: disable=import-self
import mypy_boto3_greengrass.paginator as paginator_scope
from mypy_boto3_greengrass.type_defs import (
    AssociateRoleToGroupResponseTypeDef,
    AssociateServiceRoleToAccountResponseTypeDef,
    ConnectivityInfoTypeDef,
    ConnectorDefinitionVersionTypeDef,
    ConnectorTypeDef,
    CoreDefinitionVersionTypeDef,
    CoreTypeDef,
    CreateConnectorDefinitionResponseTypeDef,
    CreateConnectorDefinitionVersionResponseTypeDef,
    CreateCoreDefinitionResponseTypeDef,
    CreateCoreDefinitionVersionResponseTypeDef,
    CreateDeploymentResponseTypeDef,
    CreateDeviceDefinitionResponseTypeDef,
    CreateDeviceDefinitionVersionResponseTypeDef,
    CreateFunctionDefinitionResponseTypeDef,
    CreateFunctionDefinitionVersionResponseTypeDef,
    CreateGroupCertificateAuthorityResponseTypeDef,
    CreateGroupResponseTypeDef,
    CreateGroupVersionResponseTypeDef,
    CreateLoggerDefinitionResponseTypeDef,
    CreateLoggerDefinitionVersionResponseTypeDef,
    CreateResourceDefinitionResponseTypeDef,
    CreateResourceDefinitionVersionResponseTypeDef,
    CreateSoftwareUpdateJobResponseTypeDef,
    CreateSubscriptionDefinitionResponseTypeDef,
    CreateSubscriptionDefinitionVersionResponseTypeDef,
    DeviceDefinitionVersionTypeDef,
    DeviceTypeDef,
    DisassociateRoleFromGroupResponseTypeDef,
    DisassociateServiceRoleFromAccountResponseTypeDef,
    FunctionDefaultConfigTypeDef,
    FunctionDefinitionVersionTypeDef,
    FunctionTypeDef,
    GetAssociatedRoleResponseTypeDef,
    GetBulkDeploymentStatusResponseTypeDef,
    GetConnectivityInfoResponseTypeDef,
    GetConnectorDefinitionResponseTypeDef,
    GetConnectorDefinitionVersionResponseTypeDef,
    GetCoreDefinitionResponseTypeDef,
    GetCoreDefinitionVersionResponseTypeDef,
    GetDeploymentStatusResponseTypeDef,
    GetDeviceDefinitionResponseTypeDef,
    GetDeviceDefinitionVersionResponseTypeDef,
    GetFunctionDefinitionResponseTypeDef,
    GetFunctionDefinitionVersionResponseTypeDef,
    GetGroupCertificateAuthorityResponseTypeDef,
    GetGroupCertificateConfigurationResponseTypeDef,
    GetGroupResponseTypeDef,
    GetGroupVersionResponseTypeDef,
    GetLoggerDefinitionResponseTypeDef,
    GetLoggerDefinitionVersionResponseTypeDef,
    GetResourceDefinitionResponseTypeDef,
    GetResourceDefinitionVersionResponseTypeDef,
    GetServiceRoleForAccountResponseTypeDef,
    GetSubscriptionDefinitionResponseTypeDef,
    GetSubscriptionDefinitionVersionResponseTypeDef,
    GroupVersionTypeDef,
    ListBulkDeploymentDetailedReportsResponseTypeDef,
    ListBulkDeploymentsResponseTypeDef,
    ListConnectorDefinitionVersionsResponseTypeDef,
    ListConnectorDefinitionsResponseTypeDef,
    ListCoreDefinitionVersionsResponseTypeDef,
    ListCoreDefinitionsResponseTypeDef,
    ListDeploymentsResponseTypeDef,
    ListDeviceDefinitionVersionsResponseTypeDef,
    ListDeviceDefinitionsResponseTypeDef,
    ListFunctionDefinitionVersionsResponseTypeDef,
    ListFunctionDefinitionsResponseTypeDef,
    ListGroupCertificateAuthoritiesResponseTypeDef,
    ListGroupVersionsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListLoggerDefinitionVersionsResponseTypeDef,
    ListLoggerDefinitionsResponseTypeDef,
    ListResourceDefinitionVersionsResponseTypeDef,
    ListResourceDefinitionsResponseTypeDef,
    ListSubscriptionDefinitionVersionsResponseTypeDef,
    ListSubscriptionDefinitionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggerDefinitionVersionTypeDef,
    LoggerTypeDef,
    ResetDeploymentsResponseTypeDef,
    ResourceDefinitionVersionTypeDef,
    ResourceTypeDef,
    StartBulkDeploymentResponseTypeDef,
    SubscriptionDefinitionVersionTypeDef,
    SubscriptionTypeDef,
    UpdateConnectivityInfoResponseTypeDef,
    UpdateGroupCertificateConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GreengrassClient",)


class GreengrassClient(BaseClient):
    """
    [Greengrass.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_role_to_group(
        self, GroupId: str, RoleArn: str
    ) -> AssociateRoleToGroupResponseTypeDef:
        """
        [Client.associate_role_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.associate_role_to_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_service_role_to_account(
        self, RoleArn: str
    ) -> AssociateServiceRoleToAccountResponseTypeDef:
        """
        [Client.associate_service_role_to_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.associate_service_role_to_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_connector_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ConnectorDefinitionVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateConnectorDefinitionResponseTypeDef:
        """
        [Client.create_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_connector_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_connector_definition_version(
        self,
        ConnectorDefinitionId: str,
        AmznClientToken: str = None,
        Connectors: List[ConnectorTypeDef] = None,
    ) -> CreateConnectorDefinitionVersionResponseTypeDef:
        """
        [Client.create_connector_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_connector_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_core_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: CoreDefinitionVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateCoreDefinitionResponseTypeDef:
        """
        [Client.create_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_core_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_core_definition_version(
        self, CoreDefinitionId: str, AmznClientToken: str = None, Cores: List[CoreTypeDef] = None
    ) -> CreateCoreDefinitionVersionResponseTypeDef:
        """
        [Client.create_core_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_core_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_deployment(
        self,
        DeploymentType: Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        GroupId: str,
        AmznClientToken: str = None,
        DeploymentId: str = None,
        GroupVersionId: str = None,
    ) -> CreateDeploymentResponseTypeDef:
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_deployment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_device_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: DeviceDefinitionVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateDeviceDefinitionResponseTypeDef:
        """
        [Client.create_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_device_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_device_definition_version(
        self,
        DeviceDefinitionId: str,
        AmznClientToken: str = None,
        Devices: List[DeviceTypeDef] = None,
    ) -> CreateDeviceDefinitionVersionResponseTypeDef:
        """
        [Client.create_device_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_device_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_function_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: FunctionDefinitionVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateFunctionDefinitionResponseTypeDef:
        """
        [Client.create_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_function_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_function_definition_version(
        self,
        FunctionDefinitionId: str,
        AmznClientToken: str = None,
        DefaultConfig: FunctionDefaultConfigTypeDef = None,
        Functions: List[FunctionTypeDef] = None,
    ) -> CreateFunctionDefinitionVersionResponseTypeDef:
        """
        [Client.create_function_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_function_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(
        self,
        AmznClientToken: str = None,
        InitialVersion: GroupVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group_certificate_authority(
        self, GroupId: str, AmznClientToken: str = None
    ) -> CreateGroupCertificateAuthorityResponseTypeDef:
        """
        [Client.create_group_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_group_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group_version(
        self,
        GroupId: str,
        AmznClientToken: str = None,
        ConnectorDefinitionVersionArn: str = None,
        CoreDefinitionVersionArn: str = None,
        DeviceDefinitionVersionArn: str = None,
        FunctionDefinitionVersionArn: str = None,
        LoggerDefinitionVersionArn: str = None,
        ResourceDefinitionVersionArn: str = None,
        SubscriptionDefinitionVersionArn: str = None,
    ) -> CreateGroupVersionResponseTypeDef:
        """
        [Client.create_group_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_group_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_logger_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: LoggerDefinitionVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateLoggerDefinitionResponseTypeDef:
        """
        [Client.create_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_logger_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_logger_definition_version(
        self,
        LoggerDefinitionId: str,
        AmznClientToken: str = None,
        Loggers: List[LoggerTypeDef] = None,
    ) -> CreateLoggerDefinitionVersionResponseTypeDef:
        """
        [Client.create_logger_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_logger_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resource_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ResourceDefinitionVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateResourceDefinitionResponseTypeDef:
        """
        [Client.create_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_resource_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resource_definition_version(
        self,
        ResourceDefinitionId: str,
        AmznClientToken: str = None,
        Resources: List[ResourceTypeDef] = None,
    ) -> CreateResourceDefinitionVersionResponseTypeDef:
        """
        [Client.create_resource_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_resource_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_software_update_job(
        self,
        S3UrlSignerRole: str,
        SoftwareToUpdate: Literal["core", "ota_agent"],
        UpdateTargets: List[str],
        UpdateTargetsArchitecture: Literal["armv6l", "armv7l", "x86_64", "aarch64"],
        UpdateTargetsOperatingSystem: Literal["ubuntu", "raspbian", "amazon_linux", "openwrt"],
        AmznClientToken: str = None,
        UpdateAgentLogLevel: Literal[
            "NONE", "TRACE", "DEBUG", "VERBOSE", "INFO", "WARN", "ERROR", "FATAL"
        ] = None,
    ) -> CreateSoftwareUpdateJobResponseTypeDef:
        """
        [Client.create_software_update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_software_update_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subscription_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: SubscriptionDefinitionVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateSubscriptionDefinitionResponseTypeDef:
        """
        [Client.create_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_subscription_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        AmznClientToken: str = None,
        Subscriptions: List[SubscriptionTypeDef] = None,
    ) -> CreateSubscriptionDefinitionVersionResponseTypeDef:
        """
        [Client.create_subscription_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.create_subscription_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_connector_definition(self, ConnectorDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.delete_connector_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_core_definition(self, CoreDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.delete_core_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_device_definition(self, DeviceDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.delete_device_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_function_definition(self, FunctionDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.delete_function_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_group(self, GroupId: str) -> Dict[str, Any]:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.delete_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_logger_definition(self, LoggerDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.delete_logger_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource_definition(self, ResourceDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.delete_resource_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_subscription_definition(self, SubscriptionDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.delete_subscription_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_role_from_group(
        self, GroupId: str
    ) -> DisassociateRoleFromGroupResponseTypeDef:
        """
        [Client.disassociate_role_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.disassociate_role_from_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_service_role_from_account(
        self,
    ) -> DisassociateServiceRoleFromAccountResponseTypeDef:
        """
        [Client.disassociate_service_role_from_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.disassociate_service_role_from_account)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_associated_role(self, GroupId: str) -> GetAssociatedRoleResponseTypeDef:
        """
        [Client.get_associated_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_associated_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bulk_deployment_status(
        self, BulkDeploymentId: str
    ) -> GetBulkDeploymentStatusResponseTypeDef:
        """
        [Client.get_bulk_deployment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_bulk_deployment_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connectivity_info(self, ThingName: str) -> GetConnectivityInfoResponseTypeDef:
        """
        [Client.get_connectivity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_connectivity_info)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connector_definition(
        self, ConnectorDefinitionId: str
    ) -> GetConnectorDefinitionResponseTypeDef:
        """
        [Client.get_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_connector_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connector_definition_version(
        self, ConnectorDefinitionId: str, ConnectorDefinitionVersionId: str, NextToken: str = None
    ) -> GetConnectorDefinitionVersionResponseTypeDef:
        """
        [Client.get_connector_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_connector_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_core_definition(self, CoreDefinitionId: str) -> GetCoreDefinitionResponseTypeDef:
        """
        [Client.get_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_core_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_core_definition_version(
        self, CoreDefinitionId: str, CoreDefinitionVersionId: str
    ) -> GetCoreDefinitionVersionResponseTypeDef:
        """
        [Client.get_core_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_core_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deployment_status(
        self, DeploymentId: str, GroupId: str
    ) -> GetDeploymentStatusResponseTypeDef:
        """
        [Client.get_deployment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_deployment_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device_definition(self, DeviceDefinitionId: str) -> GetDeviceDefinitionResponseTypeDef:
        """
        [Client.get_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_device_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device_definition_version(
        self, DeviceDefinitionId: str, DeviceDefinitionVersionId: str, NextToken: str = None
    ) -> GetDeviceDefinitionVersionResponseTypeDef:
        """
        [Client.get_device_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_device_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_definition(
        self, FunctionDefinitionId: str
    ) -> GetFunctionDefinitionResponseTypeDef:
        """
        [Client.get_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_function_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_definition_version(
        self, FunctionDefinitionId: str, FunctionDefinitionVersionId: str, NextToken: str = None
    ) -> GetFunctionDefinitionVersionResponseTypeDef:
        """
        [Client.get_function_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_function_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group(self, GroupId: str) -> GetGroupResponseTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group_certificate_authority(
        self, CertificateAuthorityId: str, GroupId: str
    ) -> GetGroupCertificateAuthorityResponseTypeDef:
        """
        [Client.get_group_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_group_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group_certificate_configuration(
        self, GroupId: str
    ) -> GetGroupCertificateConfigurationResponseTypeDef:
        """
        [Client.get_group_certificate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_group_certificate_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group_version(
        self, GroupId: str, GroupVersionId: str
    ) -> GetGroupVersionResponseTypeDef:
        """
        [Client.get_group_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_group_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_logger_definition(self, LoggerDefinitionId: str) -> GetLoggerDefinitionResponseTypeDef:
        """
        [Client.get_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_logger_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_logger_definition_version(
        self, LoggerDefinitionId: str, LoggerDefinitionVersionId: str, NextToken: str = None
    ) -> GetLoggerDefinitionVersionResponseTypeDef:
        """
        [Client.get_logger_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_logger_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_definition(
        self, ResourceDefinitionId: str
    ) -> GetResourceDefinitionResponseTypeDef:
        """
        [Client.get_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_resource_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_definition_version(
        self, ResourceDefinitionId: str, ResourceDefinitionVersionId: str
    ) -> GetResourceDefinitionVersionResponseTypeDef:
        """
        [Client.get_resource_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_resource_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service_role_for_account(self) -> GetServiceRoleForAccountResponseTypeDef:
        """
        [Client.get_service_role_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_service_role_for_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_subscription_definition(
        self, SubscriptionDefinitionId: str
    ) -> GetSubscriptionDefinitionResponseTypeDef:
        """
        [Client.get_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_subscription_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        SubscriptionDefinitionVersionId: str,
        NextToken: str = None,
    ) -> GetSubscriptionDefinitionVersionResponseTypeDef:
        """
        [Client.get_subscription_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.get_subscription_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bulk_deployment_detailed_reports(
        self, BulkDeploymentId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListBulkDeploymentDetailedReportsResponseTypeDef:
        """
        [Client.list_bulk_deployment_detailed_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_bulk_deployment_detailed_reports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bulk_deployments(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListBulkDeploymentsResponseTypeDef:
        """
        [Client.list_bulk_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_bulk_deployments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_connector_definition_versions(
        self, ConnectorDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListConnectorDefinitionVersionsResponseTypeDef:
        """
        [Client.list_connector_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_connector_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_connector_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListConnectorDefinitionsResponseTypeDef:
        """
        [Client.list_connector_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_connector_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_core_definition_versions(
        self, CoreDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListCoreDefinitionVersionsResponseTypeDef:
        """
        [Client.list_core_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_core_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_core_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListCoreDefinitionsResponseTypeDef:
        """
        [Client.list_core_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_core_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deployments(
        self, GroupId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListDeploymentsResponseTypeDef:
        """
        [Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_deployments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_device_definition_versions(
        self, DeviceDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListDeviceDefinitionVersionsResponseTypeDef:
        """
        [Client.list_device_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_device_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_device_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListDeviceDefinitionsResponseTypeDef:
        """
        [Client.list_device_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_device_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_function_definition_versions(
        self, FunctionDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListFunctionDefinitionVersionsResponseTypeDef:
        """
        [Client.list_function_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_function_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_function_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListFunctionDefinitionsResponseTypeDef:
        """
        [Client.list_function_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_function_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_group_certificate_authorities(
        self, GroupId: str
    ) -> ListGroupCertificateAuthoritiesResponseTypeDef:
        """
        [Client.list_group_certificate_authorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_group_certificate_authorities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_group_versions(
        self, GroupId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListGroupVersionsResponseTypeDef:
        """
        [Client.list_group_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_group_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_groups(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_logger_definition_versions(
        self, LoggerDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListLoggerDefinitionVersionsResponseTypeDef:
        """
        [Client.list_logger_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_logger_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_logger_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListLoggerDefinitionsResponseTypeDef:
        """
        [Client.list_logger_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_logger_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_definition_versions(
        self, ResourceDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListResourceDefinitionVersionsResponseTypeDef:
        """
        [Client.list_resource_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_resource_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListResourceDefinitionsResponseTypeDef:
        """
        [Client.list_resource_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_resource_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_subscription_definition_versions(
        self, SubscriptionDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListSubscriptionDefinitionVersionsResponseTypeDef:
        """
        [Client.list_subscription_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_subscription_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_subscription_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListSubscriptionDefinitionsResponseTypeDef:
        """
        [Client.list_subscription_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_subscription_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_deployments(
        self, GroupId: str, AmznClientToken: str = None, Force: bool = None
    ) -> ResetDeploymentsResponseTypeDef:
        """
        [Client.reset_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.reset_deployments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_bulk_deployment(
        self,
        ExecutionRoleArn: str,
        InputFileUri: str,
        AmznClientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> StartBulkDeploymentResponseTypeDef:
        """
        [Client.start_bulk_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.start_bulk_deployment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_bulk_deployment(self, BulkDeploymentId: str) -> Dict[str, Any]:
        """
        [Client.stop_bulk_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.stop_bulk_deployment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, tags: Dict[str, str] = None) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_connectivity_info(
        self, ThingName: str, ConnectivityInfo: List[ConnectivityInfoTypeDef] = None
    ) -> UpdateConnectivityInfoResponseTypeDef:
        """
        [Client.update_connectivity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.update_connectivity_info)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_connector_definition(
        self, ConnectorDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.update_connector_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_core_definition(self, CoreDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.update_core_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_device_definition(self, DeviceDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.update_device_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_function_definition(
        self, FunctionDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.update_function_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_group(self, GroupId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.update_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_group_certificate_configuration(
        self, GroupId: str, CertificateExpiryInMilliseconds: str = None
    ) -> UpdateGroupCertificateConfigurationResponseTypeDef:
        """
        [Client.update_group_certificate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.update_group_certificate_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_logger_definition(self, LoggerDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.update_logger_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_resource_definition(
        self, ResourceDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.update_resource_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_subscription_definition(
        self, SubscriptionDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Client.update_subscription_definition)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_bulk_deployment_detailed_reports"]
    ) -> paginator_scope.ListBulkDeploymentDetailedReportsPaginator:
        """
        [Paginator.ListBulkDeploymentDetailedReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_bulk_deployments"]
    ) -> paginator_scope.ListBulkDeploymentsPaginator:
        """
        [Paginator.ListBulkDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeployments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_connector_definition_versions"]
    ) -> paginator_scope.ListConnectorDefinitionVersionsPaginator:
        """
        [Paginator.ListConnectorDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_connector_definitions"]
    ) -> paginator_scope.ListConnectorDefinitionsPaginator:
        """
        [Paginator.ListConnectorDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_core_definition_versions"]
    ) -> paginator_scope.ListCoreDefinitionVersionsPaginator:
        """
        [Paginator.ListCoreDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_core_definitions"]
    ) -> paginator_scope.ListCoreDefinitionsPaginator:
        """
        [Paginator.ListCoreDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> paginator_scope.ListDeploymentsPaginator:
        """
        [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListDeployments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_device_definition_versions"]
    ) -> paginator_scope.ListDeviceDefinitionVersionsPaginator:
        """
        [Paginator.ListDeviceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_device_definitions"]
    ) -> paginator_scope.ListDeviceDefinitionsPaginator:
        """
        [Paginator.ListDeviceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_function_definition_versions"]
    ) -> paginator_scope.ListFunctionDefinitionVersionsPaginator:
        """
        [Paginator.ListFunctionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_function_definitions"]
    ) -> paginator_scope.ListFunctionDefinitionsPaginator:
        """
        [Paginator.ListFunctionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_group_versions"]
    ) -> paginator_scope.ListGroupVersionsPaginator:
        """
        [Paginator.ListGroupVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListGroupVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_groups"]
    ) -> paginator_scope.ListGroupsPaginator:
        """
        [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_logger_definition_versions"]
    ) -> paginator_scope.ListLoggerDefinitionVersionsPaginator:
        """
        [Paginator.ListLoggerDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_logger_definitions"]
    ) -> paginator_scope.ListLoggerDefinitionsPaginator:
        """
        [Paginator.ListLoggerDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_definition_versions"]
    ) -> paginator_scope.ListResourceDefinitionVersionsPaginator:
        """
        [Paginator.ListResourceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_definitions"]
    ) -> paginator_scope.ListResourceDefinitionsPaginator:
        """
        [Paginator.ListResourceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_subscription_definition_versions"]
    ) -> paginator_scope.ListSubscriptionDefinitionVersionsPaginator:
        """
        [Paginator.ListSubscriptionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_subscription_definitions"]
    ) -> paginator_scope.ListSubscriptionDefinitionsPaginator:
        """
        [Paginator.ListSubscriptionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitions)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
