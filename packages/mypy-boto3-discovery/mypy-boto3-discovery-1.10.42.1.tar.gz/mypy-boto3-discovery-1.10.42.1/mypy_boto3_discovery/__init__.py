"Main interface for discovery service"
from mypy_boto3_discovery.client import (
    ApplicationDiscoveryServiceClient as Client,
    ApplicationDiscoveryServiceClient,
)
from mypy_boto3_discovery.paginator import (
    DescribeAgentsPaginator,
    DescribeContinuousExportsPaginator,
    DescribeExportConfigurationsPaginator,
    DescribeExportTasksPaginator,
    DescribeTagsPaginator,
    ListConfigurationsPaginator,
)


__all__ = (
    "ApplicationDiscoveryServiceClient",
    "Client",
    "DescribeAgentsPaginator",
    "DescribeContinuousExportsPaginator",
    "DescribeExportConfigurationsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeTagsPaginator",
    "ListConfigurationsPaginator",
)
