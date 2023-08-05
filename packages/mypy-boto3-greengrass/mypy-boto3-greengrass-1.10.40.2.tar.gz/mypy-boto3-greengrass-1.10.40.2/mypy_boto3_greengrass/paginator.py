"Main interface for greengrass service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_greengrass.type_defs import (
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
    ListGroupVersionsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListLoggerDefinitionVersionsResponseTypeDef,
    ListLoggerDefinitionsResponseTypeDef,
    ListResourceDefinitionVersionsResponseTypeDef,
    ListResourceDefinitionsResponseTypeDef,
    ListSubscriptionDefinitionVersionsResponseTypeDef,
    ListSubscriptionDefinitionsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListBulkDeploymentDetailedReportsPaginator",
    "ListBulkDeploymentsPaginator",
    "ListConnectorDefinitionVersionsPaginator",
    "ListConnectorDefinitionsPaginator",
    "ListCoreDefinitionVersionsPaginator",
    "ListCoreDefinitionsPaginator",
    "ListDeploymentsPaginator",
    "ListDeviceDefinitionVersionsPaginator",
    "ListDeviceDefinitionsPaginator",
    "ListFunctionDefinitionVersionsPaginator",
    "ListFunctionDefinitionsPaginator",
    "ListGroupVersionsPaginator",
    "ListGroupsPaginator",
    "ListLoggerDefinitionVersionsPaginator",
    "ListLoggerDefinitionsPaginator",
    "ListResourceDefinitionVersionsPaginator",
    "ListResourceDefinitionsPaginator",
    "ListSubscriptionDefinitionVersionsPaginator",
    "ListSubscriptionDefinitionsPaginator",
)


class ListBulkDeploymentDetailedReportsPaginator(Boto3Paginator):
    """
    [Paginator.ListBulkDeploymentDetailedReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, BulkDeploymentId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListBulkDeploymentDetailedReportsResponseTypeDef, None, None]:
        """
        [ListBulkDeploymentDetailedReports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports.paginate)
        """


class ListBulkDeploymentsPaginator(Boto3Paginator):
    """
    [Paginator.ListBulkDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeployments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListBulkDeploymentsResponseTypeDef, None, None]:
        """
        [ListBulkDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeployments.paginate)
        """


class ListConnectorDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListConnectorDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitionVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ConnectorDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListConnectorDefinitionVersionsResponseTypeDef, None, None]:
        """
        [ListConnectorDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitionVersions.paginate)
        """


class ListConnectorDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListConnectorDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListConnectorDefinitionsResponseTypeDef, None, None]:
        """
        [ListConnectorDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitions.paginate)
        """


class ListCoreDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListCoreDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitionVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CoreDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListCoreDefinitionVersionsResponseTypeDef, None, None]:
        """
        [ListCoreDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitionVersions.paginate)
        """


class ListCoreDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListCoreDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListCoreDefinitionsResponseTypeDef, None, None]:
        """
        [ListCoreDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitions.paginate)
        """


class ListDeploymentsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListDeployments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GroupId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDeploymentsResponseTypeDef, None, None]:
        """
        [ListDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListDeployments.paginate)
        """


class ListDeviceDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeviceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitionVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DeviceDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDeviceDefinitionVersionsResponseTypeDef, None, None]:
        """
        [ListDeviceDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitionVersions.paginate)
        """


class ListDeviceDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeviceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDeviceDefinitionsResponseTypeDef, None, None]:
        """
        [ListDeviceDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitions.paginate)
        """


class ListFunctionDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListFunctionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitionVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, FunctionDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFunctionDefinitionVersionsResponseTypeDef, None, None]:
        """
        [ListFunctionDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitionVersions.paginate)
        """


class ListFunctionDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListFunctionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFunctionDefinitionsResponseTypeDef, None, None]:
        """
        [ListFunctionDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitions.paginate)
        """


class ListGroupVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroupVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListGroupVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GroupId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGroupVersionsResponseTypeDef, None, None]:
        """
        [ListGroupVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListGroupVersions.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGroupsResponseTypeDef, None, None]:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListGroups.paginate)
        """


class ListLoggerDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListLoggerDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitionVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, LoggerDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListLoggerDefinitionVersionsResponseTypeDef, None, None]:
        """
        [ListLoggerDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitionVersions.paginate)
        """


class ListLoggerDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListLoggerDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListLoggerDefinitionsResponseTypeDef, None, None]:
        """
        [ListLoggerDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitions.paginate)
        """


class ListResourceDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitionVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListResourceDefinitionVersionsResponseTypeDef, None, None]:
        """
        [ListResourceDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitionVersions.paginate)
        """


class ListResourceDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListResourceDefinitionsResponseTypeDef, None, None]:
        """
        [ListResourceDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitions.paginate)
        """


class ListSubscriptionDefinitionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscriptionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, SubscriptionDefinitionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSubscriptionDefinitionVersionsResponseTypeDef, None, None]:
        """
        [ListSubscriptionDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions.paginate)
        """


class ListSubscriptionDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscriptionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSubscriptionDefinitionsResponseTypeDef, None, None]:
        """
        [ListSubscriptionDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitions.paginate)
        """
