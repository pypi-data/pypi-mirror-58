"Main interface for discovery service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_discovery.type_defs import (
    DescribeAgentsResponseTypeDef,
    DescribeContinuousExportsResponseTypeDef,
    DescribeExportConfigurationsResponseTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeTagsResponseTypeDef,
    ExportFilterTypeDef,
    FilterTypeDef,
    ListConfigurationsResponseTypeDef,
    OrderByElementTypeDef,
    PaginatorConfigTypeDef,
    TagFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAgentsPaginator",
    "DescribeContinuousExportsPaginator",
    "DescribeExportConfigurationsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeTagsPaginator",
    "ListConfigurationsPaginator",
)


class DescribeAgentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        agentIds: List[str] = None,
        filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAgentsResponseTypeDef, None, None]:
        """
        [DescribeAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents.paginate)
        """


class DescribeContinuousExportsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeContinuousExports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, exportIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeContinuousExportsResponseTypeDef, None, None]:
        """
        [DescribeContinuousExports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports.paginate)
        """


class DescribeExportConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeExportConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, exportIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeExportConfigurationsResponseTypeDef, None, None]:
        """
        [DescribeExportConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations.paginate)
        """


class DescribeExportTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        exportIds: List[str] = None,
        filters: List[ExportFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeExportTasksResponseTypeDef, None, None]:
        """
        [DescribeExportTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[TagFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTagsResponseTypeDef, None, None]:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags.paginate)
        """


class ListConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        configurationType: Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        filters: List[FilterTypeDef] = None,
        orderBy: List[OrderByElementTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListConfigurationsResponseTypeDef, None, None]:
        """
        [ListConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations.paginate)
        """
