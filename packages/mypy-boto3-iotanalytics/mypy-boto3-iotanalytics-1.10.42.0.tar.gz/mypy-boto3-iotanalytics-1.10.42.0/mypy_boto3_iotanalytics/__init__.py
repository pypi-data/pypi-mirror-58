"Main interface for iotanalytics service"
from mypy_boto3_iotanalytics.client import IoTAnalyticsClient as Client, IoTAnalyticsClient
from mypy_boto3_iotanalytics.paginator import (
    ListChannelsPaginator,
    ListDatasetContentsPaginator,
    ListDatasetsPaginator,
    ListDatastoresPaginator,
    ListPipelinesPaginator,
)


__all__ = (
    "Client",
    "IoTAnalyticsClient",
    "ListChannelsPaginator",
    "ListDatasetContentsPaginator",
    "ListDatasetsPaginator",
    "ListDatastoresPaginator",
    "ListPipelinesPaginator",
)
