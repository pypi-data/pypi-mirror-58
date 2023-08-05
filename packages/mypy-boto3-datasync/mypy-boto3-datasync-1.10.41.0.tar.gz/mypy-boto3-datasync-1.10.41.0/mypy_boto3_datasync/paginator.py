"Main interface for datasync service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_datasync.type_defs import (
    ListAgentsResponseTypeDef,
    ListLocationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskExecutionsResponseTypeDef,
    ListTasksResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListAgentsPaginator",
    "ListLocationsPaginator",
    "ListTagsForResourcePaginator",
    "ListTaskExecutionsPaginator",
    "ListTasksPaginator",
)


class ListAgentsPaginator(Boto3Paginator):
    """
    [Paginator.ListAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datasync.html#DataSync.Paginator.ListAgents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAgentsResponseTypeDef, None, None]:
        """
        [ListAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datasync.html#DataSync.Paginator.ListAgents.paginate)
        """


class ListLocationsPaginator(Boto3Paginator):
    """
    [Paginator.ListLocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datasync.html#DataSync.Paginator.ListLocations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListLocationsResponseTypeDef, None, None]:
        """
        [ListLocations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datasync.html#DataSync.Paginator.ListLocations.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceResponseTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource.paginate)
        """


class ListTaskExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListTaskExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, TaskArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTaskExecutionsResponseTypeDef, None, None]:
        """
        [ListTaskExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions.paginate)
        """


class ListTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datasync.html#DataSync.Paginator.ListTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTasksResponseTypeDef, None, None]:
        """
        [ListTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/datasync.html#DataSync.Paginator.ListTasks.paginate)
        """
