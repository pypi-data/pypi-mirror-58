"Main interface for serverlessrepo service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_serverlessrepo.client as client_scope

# pylint: disable=import-self
import mypy_boto3_serverlessrepo.paginator as paginator_scope
from mypy_boto3_serverlessrepo.type_defs import (
    ApplicationPolicyStatementTypeDef,
    CreateApplicationResponseTypeDef,
    CreateApplicationVersionResponseTypeDef,
    CreateCloudFormationChangeSetResponseTypeDef,
    CreateCloudFormationTemplateResponseTypeDef,
    GetApplicationPolicyResponseTypeDef,
    GetApplicationResponseTypeDef,
    GetCloudFormationTemplateResponseTypeDef,
    ListApplicationDependenciesResponseTypeDef,
    ListApplicationVersionsResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ParameterValueTypeDef,
    PutApplicationPolicyResponseTypeDef,
    RollbackConfigurationTypeDef,
    TagTypeDef,
    UpdateApplicationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServerlessApplicationRepositoryClient",)


class ServerlessApplicationRepositoryClient(BaseClient):
    """
    [ServerlessApplicationRepository.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_application(
        self,
        Author: str,
        Description: str,
        Name: str,
        HomePageUrl: str = None,
        Labels: List[str] = None,
        LicenseBody: str = None,
        LicenseUrl: str = None,
        ReadmeBody: str = None,
        ReadmeUrl: str = None,
        SemanticVersion: str = None,
        SourceCodeArchiveUrl: str = None,
        SourceCodeUrl: str = None,
        SpdxLicenseId: str = None,
        TemplateBody: str = None,
        TemplateUrl: str = None,
    ) -> CreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_application_version(
        self,
        ApplicationId: str,
        SemanticVersion: str,
        SourceCodeArchiveUrl: str = None,
        SourceCodeUrl: str = None,
        TemplateBody: str = None,
        TemplateUrl: str = None,
    ) -> CreateApplicationVersionResponseTypeDef:
        """
        [Client.create_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_application_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cloud_formation_change_set(
        self,
        ApplicationId: str,
        StackName: str,
        Capabilities: List[str] = None,
        ChangeSetName: str = None,
        ClientToken: str = None,
        Description: str = None,
        NotificationArns: List[str] = None,
        ParameterOverrides: List[ParameterValueTypeDef] = None,
        ResourceTypes: List[str] = None,
        RollbackConfiguration: RollbackConfigurationTypeDef = None,
        SemanticVersion: str = None,
        Tags: List[TagTypeDef] = None,
        TemplateId: str = None,
    ) -> CreateCloudFormationChangeSetResponseTypeDef:
        """
        [Client.create_cloud_formation_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_cloud_formation_change_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cloud_formation_template(
        self, ApplicationId: str, SemanticVersion: str = None
    ) -> CreateCloudFormationTemplateResponseTypeDef:
        """
        [Client.create_cloud_formation_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_cloud_formation_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_application(self, ApplicationId: str) -> None:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.delete_application)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_application(
        self, ApplicationId: str, SemanticVersion: str = None
    ) -> GetApplicationResponseTypeDef:
        """
        [Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_application_policy(self, ApplicationId: str) -> GetApplicationPolicyResponseTypeDef:
        """
        [Client.get_application_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_application_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cloud_formation_template(
        self, ApplicationId: str, TemplateId: str
    ) -> GetCloudFormationTemplateResponseTypeDef:
        """
        [Client.get_cloud_formation_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_cloud_formation_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_application_dependencies(
        self,
        ApplicationId: str,
        MaxItems: int = None,
        NextToken: str = None,
        SemanticVersion: str = None,
    ) -> ListApplicationDependenciesResponseTypeDef:
        """
        [Client.list_application_dependencies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_application_dependencies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_application_versions(
        self, ApplicationId: str, MaxItems: int = None, NextToken: str = None
    ) -> ListApplicationVersionsResponseTypeDef:
        """
        [Client.list_application_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_application_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_applications(
        self, MaxItems: int = None, NextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_applications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_application_policy(
        self, ApplicationId: str, Statements: List[ApplicationPolicyStatementTypeDef]
    ) -> PutApplicationPolicyResponseTypeDef:
        """
        [Client.put_application_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.put_application_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_application(
        self,
        ApplicationId: str,
        Author: str = None,
        Description: str = None,
        HomePageUrl: str = None,
        Labels: List[str] = None,
        ReadmeBody: str = None,
        ReadmeUrl: str = None,
    ) -> UpdateApplicationResponseTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.update_application)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_application_dependencies"]
    ) -> paginator_scope.ListApplicationDependenciesPaginator:
        """
        [Paginator.ListApplicationDependencies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_application_versions"]
    ) -> paginator_scope.ListApplicationVersionsPaginator:
        """
        [Paginator.ListApplicationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> paginator_scope.ListApplicationsPaginator:
        """
        [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplications)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
