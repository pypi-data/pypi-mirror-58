"Main interface for mgh service"
from mypy_boto3_mgh.client import MigrationHubClient, MigrationHubClient as Client
from mypy_boto3_mgh.paginator import (
    ListCreatedArtifactsPaginator,
    ListDiscoveredResourcesPaginator,
    ListMigrationTasksPaginator,
    ListProgressUpdateStreamsPaginator,
)


__all__ = (
    "Client",
    "ListCreatedArtifactsPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListMigrationTasksPaginator",
    "ListProgressUpdateStreamsPaginator",
    "MigrationHubClient",
)
