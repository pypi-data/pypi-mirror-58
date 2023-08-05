"Main interface for codebuild service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_codebuild.client as client_scope

# pylint: disable=import-self
import mypy_boto3_codebuild.paginator as paginator_scope
from mypy_boto3_codebuild.type_defs import (
    BatchDeleteBuildsOutputTypeDef,
    BatchGetBuildsOutputTypeDef,
    BatchGetProjectsOutputTypeDef,
    BatchGetReportGroupsOutputTypeDef,
    BatchGetReportsOutputTypeDef,
    CreateProjectOutputTypeDef,
    CreateReportGroupOutputTypeDef,
    CreateWebhookOutputTypeDef,
    DeleteSourceCredentialsOutputTypeDef,
    DescribeTestCasesOutputTypeDef,
    EnvironmentVariableTypeDef,
    GetResourcePolicyOutputTypeDef,
    GitSubmodulesConfigTypeDef,
    ImportSourceCredentialsOutputTypeDef,
    ListBuildsForProjectOutputTypeDef,
    ListBuildsOutputTypeDef,
    ListCuratedEnvironmentImagesOutputTypeDef,
    ListProjectsOutputTypeDef,
    ListReportGroupsOutputTypeDef,
    ListReportsForReportGroupOutputTypeDef,
    ListReportsOutputTypeDef,
    ListSharedProjectsOutputTypeDef,
    ListSharedReportGroupsOutputTypeDef,
    ListSourceCredentialsOutputTypeDef,
    LogsConfigTypeDef,
    ProjectArtifactsTypeDef,
    ProjectCacheTypeDef,
    ProjectEnvironmentTypeDef,
    ProjectSourceTypeDef,
    ProjectSourceVersionTypeDef,
    PutResourcePolicyOutputTypeDef,
    RegistryCredentialTypeDef,
    ReportExportConfigTypeDef,
    ReportFilterTypeDef,
    SourceAuthTypeDef,
    StartBuildOutputTypeDef,
    StopBuildOutputTypeDef,
    TagTypeDef,
    TestCaseFilterTypeDef,
    UpdateProjectOutputTypeDef,
    UpdateReportGroupOutputTypeDef,
    UpdateWebhookOutputTypeDef,
    VpcConfigTypeDef,
    WebhookFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeBuildClient",)


class CodeBuildClient(BaseClient):
    """
    [CodeBuild.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_builds(self, ids: List[str]) -> BatchDeleteBuildsOutputTypeDef:
        """
        [Client.batch_delete_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.batch_delete_builds)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_builds(self, ids: List[str]) -> BatchGetBuildsOutputTypeDef:
        """
        [Client.batch_get_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.batch_get_builds)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_projects(self, names: List[str]) -> BatchGetProjectsOutputTypeDef:
        """
        [Client.batch_get_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.batch_get_projects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_report_groups(
        self, reportGroupArns: List[str]
    ) -> BatchGetReportGroupsOutputTypeDef:
        """
        [Client.batch_get_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.batch_get_report_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_reports(self, reportArns: List[str]) -> BatchGetReportsOutputTypeDef:
        """
        [Client.batch_get_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.batch_get_reports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_project(
        self,
        name: str,
        source: ProjectSourceTypeDef,
        artifacts: ProjectArtifactsTypeDef,
        environment: ProjectEnvironmentTypeDef,
        serviceRole: str,
        description: str = None,
        secondarySources: List[ProjectSourceTypeDef] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List[ProjectSourceVersionTypeDef] = None,
        secondaryArtifacts: List[ProjectArtifactsTypeDef] = None,
        cache: ProjectCacheTypeDef = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List[TagTypeDef] = None,
        vpcConfig: VpcConfigTypeDef = None,
        badgeEnabled: bool = None,
        logsConfig: LogsConfigTypeDef = None,
    ) -> CreateProjectOutputTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.create_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_report_group(
        self, name: str, type: Literal["TEST"], exportConfig: ReportExportConfigTypeDef
    ) -> CreateReportGroupOutputTypeDef:
        """
        [Client.create_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.create_report_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        filterGroups: List[List[WebhookFilterTypeDef]] = None,
    ) -> CreateWebhookOutputTypeDef:
        """
        [Client.create_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.create_webhook)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_project(self, name: str) -> Dict[str, Any]:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.delete_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_report(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.delete_report)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_report_group(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.delete_report_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource_policy(self, resourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.delete_resource_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_source_credentials(self, arn: str) -> DeleteSourceCredentialsOutputTypeDef:
        """
        [Client.delete_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.delete_source_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_webhook(self, projectName: str) -> Dict[str, Any]:
        """
        [Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.delete_webhook)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_test_cases(
        self,
        reportArn: str,
        nextToken: str = None,
        maxResults: int = None,
        filter: TestCaseFilterTypeDef = None,
    ) -> DescribeTestCasesOutputTypeDef:
        """
        [Client.describe_test_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.describe_test_cases)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_policy(self, resourceArn: str) -> GetResourcePolicyOutputTypeDef:
        """
        [Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.get_resource_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_source_credentials(
        self,
        token: str,
        serverType: Literal["GITHUB", "BITBUCKET", "GITHUB_ENTERPRISE"],
        authType: Literal["OAUTH", "BASIC_AUTH", "PERSONAL_ACCESS_TOKEN"],
        username: str = None,
        shouldOverwrite: bool = None,
    ) -> ImportSourceCredentialsOutputTypeDef:
        """
        [Client.import_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.import_source_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invalidate_project_cache(self, projectName: str) -> Dict[str, Any]:
        """
        [Client.invalidate_project_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.invalidate_project_cache)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_builds(
        self, sortOrder: Literal["ASCENDING", "DESCENDING"] = None, nextToken: str = None
    ) -> ListBuildsOutputTypeDef:
        """
        [Client.list_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.list_builds)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_builds_for_project(
        self,
        projectName: str,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ListBuildsForProjectOutputTypeDef:
        """
        [Client.list_builds_for_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.list_builds_for_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_curated_environment_images(self) -> ListCuratedEnvironmentImagesOutputTypeDef:
        """
        [Client.list_curated_environment_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.list_curated_environment_images)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_projects(
        self,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ListProjectsOutputTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.list_projects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_report_groups(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListReportGroupsOutputTypeDef:
        """
        [Client.list_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.list_report_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_reports(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: ReportFilterTypeDef = None,
    ) -> ListReportsOutputTypeDef:
        """
        [Client.list_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.list_reports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_reports_for_report_group(
        self,
        reportGroupArn: str,
        nextToken: str = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        maxResults: int = None,
        filter: ReportFilterTypeDef = None,
    ) -> ListReportsForReportGroupOutputTypeDef:
        """
        [Client.list_reports_for_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.list_reports_for_report_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_shared_projects(
        self,
        sortBy: Literal["ARN", "MODIFIED_TIME"] = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSharedProjectsOutputTypeDef:
        """
        [Client.list_shared_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.list_shared_projects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_shared_report_groups(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        sortBy: Literal["ARN", "MODIFIED_TIME"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListSharedReportGroupsOutputTypeDef:
        """
        [Client.list_shared_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.list_shared_report_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_source_credentials(self) -> ListSourceCredentialsOutputTypeDef:
        """
        [Client.list_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.list_source_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_resource_policy(self, policy: str, resourceArn: str) -> PutResourcePolicyOutputTypeDef:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.put_resource_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_build(
        self,
        projectName: str,
        secondarySourcesOverride: List[ProjectSourceTypeDef] = None,
        secondarySourcesVersionOverride: List[ProjectSourceVersionTypeDef] = None,
        sourceVersion: str = None,
        artifactsOverride: ProjectArtifactsTypeDef = None,
        secondaryArtifactsOverride: List[ProjectArtifactsTypeDef] = None,
        environmentVariablesOverride: List[EnvironmentVariableTypeDef] = None,
        sourceTypeOverride: Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ] = None,
        sourceLocationOverride: str = None,
        sourceAuthOverride: SourceAuthTypeDef = None,
        gitCloneDepthOverride: int = None,
        gitSubmodulesConfigOverride: GitSubmodulesConfigTypeDef = None,
        buildspecOverride: str = None,
        insecureSslOverride: bool = None,
        reportBuildStatusOverride: bool = None,
        environmentTypeOverride: Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ] = None,
        imageOverride: str = None,
        computeTypeOverride: Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ] = None,
        certificateOverride: str = None,
        cacheOverride: ProjectCacheTypeDef = None,
        serviceRoleOverride: str = None,
        privilegedModeOverride: bool = None,
        timeoutInMinutesOverride: int = None,
        queuedTimeoutInMinutesOverride: int = None,
        idempotencyToken: str = None,
        logsConfigOverride: LogsConfigTypeDef = None,
        registryCredentialOverride: RegistryCredentialTypeDef = None,
        imagePullCredentialsTypeOverride: Literal["CODEBUILD", "SERVICE_ROLE"] = None,
    ) -> StartBuildOutputTypeDef:
        """
        [Client.start_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.start_build)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_build(self, id: str) -> StopBuildOutputTypeDef:
        """
        [Client.stop_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.stop_build)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_project(
        self,
        name: str,
        description: str = None,
        source: ProjectSourceTypeDef = None,
        secondarySources: List[ProjectSourceTypeDef] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List[ProjectSourceVersionTypeDef] = None,
        artifacts: ProjectArtifactsTypeDef = None,
        secondaryArtifacts: List[ProjectArtifactsTypeDef] = None,
        cache: ProjectCacheTypeDef = None,
        environment: ProjectEnvironmentTypeDef = None,
        serviceRole: str = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List[TagTypeDef] = None,
        vpcConfig: VpcConfigTypeDef = None,
        badgeEnabled: bool = None,
        logsConfig: LogsConfigTypeDef = None,
    ) -> UpdateProjectOutputTypeDef:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.update_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_report_group(
        self, arn: str, exportConfig: ReportExportConfigTypeDef = None
    ) -> UpdateReportGroupOutputTypeDef:
        """
        [Client.update_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.update_report_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        rotateSecret: bool = None,
        filterGroups: List[List[WebhookFilterTypeDef]] = None,
    ) -> UpdateWebhookOutputTypeDef:
        """
        [Client.update_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Client.update_webhook)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_builds"]
    ) -> paginator_scope.ListBuildsPaginator:
        """
        [Paginator.ListBuilds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_builds_for_project"]
    ) -> paginator_scope.ListBuildsForProjectPaginator:
        """
        [Paginator.ListBuildsForProject documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_projects"]
    ) -> paginator_scope.ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects)
        """


class Exceptions:
    AccountLimitExceededException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    OAuthProviderException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
