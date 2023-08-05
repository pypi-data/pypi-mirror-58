"Main interface for serverlessrepo service"
from mypy_boto3_serverlessrepo.client import (
    ServerlessApplicationRepositoryClient,
    ServerlessApplicationRepositoryClient as Client,
)
from mypy_boto3_serverlessrepo.paginator import (
    ListApplicationDependenciesPaginator,
    ListApplicationVersionsPaginator,
    ListApplicationsPaginator,
)


__all__ = (
    "Client",
    "ListApplicationDependenciesPaginator",
    "ListApplicationVersionsPaginator",
    "ListApplicationsPaginator",
    "ServerlessApplicationRepositoryClient",
)
