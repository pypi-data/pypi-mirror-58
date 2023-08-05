"Main interface for discovery service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_discovery.client as client_scope

# pylint: disable=import-self
import mypy_boto3_discovery.paginator as paginator_scope
from mypy_boto3_discovery.type_defs import (
    BatchDeleteImportDataResponseTypeDef,
    CreateApplicationResponseTypeDef,
    DescribeAgentsResponseTypeDef,
    DescribeConfigurationsResponseTypeDef,
    DescribeContinuousExportsResponseTypeDef,
    DescribeExportConfigurationsResponseTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeImportTasksResponseTypeDef,
    DescribeTagsResponseTypeDef,
    ExportConfigurationsResponseTypeDef,
    ExportFilterTypeDef,
    FilterTypeDef,
    GetDiscoverySummaryResponseTypeDef,
    ImportTaskFilterTypeDef,
    ListConfigurationsResponseTypeDef,
    ListServerNeighborsResponseTypeDef,
    OrderByElementTypeDef,
    StartContinuousExportResponseTypeDef,
    StartDataCollectionByAgentIdsResponseTypeDef,
    StartExportTaskResponseTypeDef,
    StartImportTaskResponseTypeDef,
    StopContinuousExportResponseTypeDef,
    StopDataCollectionByAgentIdsResponseTypeDef,
    TagFilterTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ApplicationDiscoveryServiceClient",)


class ApplicationDiscoveryServiceClient(BaseClient):
    """
    [ApplicationDiscoveryService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_configuration_items_to_application(
        self, applicationConfigurationId: str, configurationIds: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.associate_configuration_items_to_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.associate_configuration_items_to_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_import_data(
        self, importTaskIds: List[str]
    ) -> BatchDeleteImportDataResponseTypeDef:
        """
        [Client.batch_delete_import_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.batch_delete_import_data)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_application(
        self, name: str, description: str = None
    ) -> CreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(self, configurationIds: List[str], tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_applications(self, configurationIds: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_applications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tags(
        self, configurationIds: List[str], tags: List[TagTypeDef] = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_agents(
        self,
        agentIds: List[str] = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeAgentsResponseTypeDef:
        """
        [Client.describe_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_agents)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_configurations(
        self, configurationIds: List[str]
    ) -> DescribeConfigurationsResponseTypeDef:
        """
        [Client.describe_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_continuous_exports(
        self, exportIds: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeContinuousExportsResponseTypeDef:
        """
        [Client.describe_continuous_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_continuous_exports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_export_configurations(
        self, exportIds: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeExportConfigurationsResponseTypeDef:
        """
        [Client.describe_export_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_export_tasks(
        self,
        exportIds: List[str] = None,
        filters: List[ExportFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeExportTasksResponseTypeDef:
        """
        [Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_import_tasks(
        self,
        filters: List[ImportTaskFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeImportTasksResponseTypeDef:
        """
        [Client.describe_import_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_import_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tags(
        self, filters: List[TagFilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_configuration_items_from_application(
        self, applicationConfigurationId: str, configurationIds: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_configuration_items_from_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.disassociate_configuration_items_from_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_configurations(self) -> ExportConfigurationsResponseTypeDef:
        """
        [Client.export_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.export_configurations)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_discovery_summary(self) -> GetDiscoverySummaryResponseTypeDef:
        """
        [Client.get_discovery_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.get_discovery_summary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configurations(
        self,
        configurationType: Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
        orderBy: List[OrderByElementTypeDef] = None,
    ) -> ListConfigurationsResponseTypeDef:
        """
        [Client.list_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_server_neighbors(
        self,
        configurationId: str,
        portInformationNeeded: bool = None,
        neighborConfigurationIds: List[str] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListServerNeighborsResponseTypeDef:
        """
        [Client.list_server_neighbors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_server_neighbors)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_continuous_export(self) -> StartContinuousExportResponseTypeDef:
        """
        [Client.start_continuous_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_continuous_export)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_data_collection_by_agent_ids(
        self, agentIds: List[str]
    ) -> StartDataCollectionByAgentIdsResponseTypeDef:
        """
        [Client.start_data_collection_by_agent_ids documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_data_collection_by_agent_ids)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_export_task(
        self,
        exportDataFormat: List[Literal["CSV", "GRAPHML"]] = None,
        filters: List[ExportFilterTypeDef] = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> StartExportTaskResponseTypeDef:
        """
        [Client.start_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_export_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_import_task(
        self, name: str, importUrl: str, clientRequestToken: str = None
    ) -> StartImportTaskResponseTypeDef:
        """
        [Client.start_import_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_import_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_continuous_export(self, exportId: str) -> StopContinuousExportResponseTypeDef:
        """
        [Client.stop_continuous_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_continuous_export)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_data_collection_by_agent_ids(
        self, agentIds: List[str]
    ) -> StopDataCollectionByAgentIdsResponseTypeDef:
        """
        [Client.stop_data_collection_by_agent_ids documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_data_collection_by_agent_ids)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_application(
        self, configurationId: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Client.update_application)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_agents"]
    ) -> paginator_scope.DescribeAgentsPaginator:
        """
        [Paginator.DescribeAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_continuous_exports"]
    ) -> paginator_scope.DescribeContinuousExportsPaginator:
        """
        [Paginator.DescribeContinuousExports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_export_configurations"]
    ) -> paginator_scope.DescribeExportConfigurationsPaginator:
        """
        [Paginator.DescribeExportConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> paginator_scope.DescribeExportTasksPaginator:
        """
        [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_tags"]
    ) -> paginator_scope.DescribeTagsPaginator:
        """
        [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_configurations"]
    ) -> paginator_scope.ListConfigurationsPaginator:
        """
        [Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations)
        """


class Exceptions:
    AuthorizationErrorException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictErrorException: Boto3ClientError
    HomeRegionNotSetException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServerInternalErrorException: Boto3ClientError
