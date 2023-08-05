"Main interface for serverlessrepo service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_serverlessrepo.type_defs import (
    ListApplicationDependenciesResponseTypeDef,
    ListApplicationVersionsResponseTypeDef,
    ListApplicationsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListApplicationDependenciesPaginator",
    "ListApplicationVersionsPaginator",
    "ListApplicationsPaginator",
)


class ListApplicationDependenciesPaginator(Boto3Paginator):
    """
    [Paginator.ListApplicationDependencies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApplicationId: str,
        SemanticVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListApplicationDependenciesResponseTypeDef, None, None]:
        """
        [ListApplicationDependencies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies.paginate)
        """


class ListApplicationVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListApplicationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApplicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListApplicationVersionsResponseTypeDef, None, None]:
        """
        [ListApplicationVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions.paginate)
        """


class ListApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListApplicationsResponseTypeDef, None, None]:
        """
        [ListApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplications.paginate)
        """
