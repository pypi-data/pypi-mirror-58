"Main interface for datasync service"
from mypy_boto3_datasync.client import DataSyncClient as Client, DataSyncClient
from mypy_boto3_datasync.paginator import (
    ListAgentsPaginator,
    ListLocationsPaginator,
    ListTagsForResourcePaginator,
    ListTaskExecutionsPaginator,
    ListTasksPaginator,
)


__all__ = (
    "Client",
    "DataSyncClient",
    "ListAgentsPaginator",
    "ListLocationsPaginator",
    "ListTagsForResourcePaginator",
    "ListTaskExecutionsPaginator",
    "ListTasksPaginator",
)
