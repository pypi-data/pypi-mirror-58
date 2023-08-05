"Main interface for mgh service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mgh.type_defs import (
    ListCreatedArtifactsResultTypeDef,
    ListDiscoveredResourcesResultTypeDef,
    ListMigrationTasksResultTypeDef,
    ListProgressUpdateStreamsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListCreatedArtifactsPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListMigrationTasksPaginator",
    "ListProgressUpdateStreamsPaginator",
)


class ListCreatedArtifactsPaginator(Boto3Paginator):
    """
    [Paginator.ListCreatedArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mgh.html#MigrationHub.Paginator.ListCreatedArtifacts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListCreatedArtifactsResultTypeDef, None, None]:
        """
        [ListCreatedArtifacts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mgh.html#MigrationHub.Paginator.ListCreatedArtifacts.paginate)
        """


class ListDiscoveredResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mgh.html#MigrationHub.Paginator.ListDiscoveredResources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDiscoveredResourcesResultTypeDef, None, None]:
        """
        [ListDiscoveredResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mgh.html#MigrationHub.Paginator.ListDiscoveredResources.paginate)
        """


class ListMigrationTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListMigrationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mgh.html#MigrationHub.Paginator.ListMigrationTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMigrationTasksResultTypeDef, None, None]:
        """
        [ListMigrationTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mgh.html#MigrationHub.Paginator.ListMigrationTasks.paginate)
        """


class ListProgressUpdateStreamsPaginator(Boto3Paginator):
    """
    [Paginator.ListProgressUpdateStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mgh.html#MigrationHub.Paginator.ListProgressUpdateStreams)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListProgressUpdateStreamsResultTypeDef, None, None]:
        """
        [ListProgressUpdateStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mgh.html#MigrationHub.Paginator.ListProgressUpdateStreams.paginate)
        """
