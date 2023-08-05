"Main interface for amplify service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_amplify.client as client_scope

# pylint: disable=import-self
import mypy_boto3_amplify.paginator as paginator_scope
from mypy_boto3_amplify.type_defs import (
    AutoBranchCreationConfigTypeDef,
    CreateAppResultTypeDef,
    CreateBackendEnvironmentResultTypeDef,
    CreateBranchResultTypeDef,
    CreateDeploymentResultTypeDef,
    CreateDomainAssociationResultTypeDef,
    CreateWebhookResultTypeDef,
    CustomRuleTypeDef,
    DeleteAppResultTypeDef,
    DeleteBackendEnvironmentResultTypeDef,
    DeleteBranchResultTypeDef,
    DeleteDomainAssociationResultTypeDef,
    DeleteJobResultTypeDef,
    DeleteWebhookResultTypeDef,
    GenerateAccessLogsResultTypeDef,
    GetAppResultTypeDef,
    GetArtifactUrlResultTypeDef,
    GetBackendEnvironmentResultTypeDef,
    GetBranchResultTypeDef,
    GetDomainAssociationResultTypeDef,
    GetJobResultTypeDef,
    GetWebhookResultTypeDef,
    ListAppsResultTypeDef,
    ListArtifactsResultTypeDef,
    ListBackendEnvironmentsResultTypeDef,
    ListBranchesResultTypeDef,
    ListDomainAssociationsResultTypeDef,
    ListJobsResultTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebhooksResultTypeDef,
    StartDeploymentResultTypeDef,
    StartJobResultTypeDef,
    StopJobResultTypeDef,
    SubDomainSettingTypeDef,
    UpdateAppResultTypeDef,
    UpdateBranchResultTypeDef,
    UpdateDomainAssociationResultTypeDef,
    UpdateWebhookResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AmplifyClient",)


class AmplifyClient(BaseClient):
    """
    [Amplify.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_app(
        self,
        name: str,
        description: str = None,
        repository: str = None,
        platform: Literal["WEB"] = None,
        iamServiceRoleArn: str = None,
        oauthToken: str = None,
        accessToken: str = None,
        environmentVariables: Dict[str, str] = None,
        enableBranchAutoBuild: bool = None,
        enableBasicAuth: bool = None,
        basicAuthCredentials: str = None,
        customRules: List[CustomRuleTypeDef] = None,
        tags: Dict[str, str] = None,
        buildSpec: str = None,
        enableAutoBranchCreation: bool = None,
        autoBranchCreationPatterns: List[str] = None,
        autoBranchCreationConfig: AutoBranchCreationConfigTypeDef = None,
    ) -> CreateAppResultTypeDef:
        """
        [Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.create_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_backend_environment(
        self,
        appId: str,
        environmentName: str,
        stackName: str = None,
        deploymentArtifacts: str = None,
    ) -> CreateBackendEnvironmentResultTypeDef:
        """
        [Client.create_backend_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.create_backend_environment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_branch(
        self,
        appId: str,
        branchName: str,
        description: str = None,
        stage: Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"] = None,
        framework: str = None,
        enableNotification: bool = None,
        enableAutoBuild: bool = None,
        environmentVariables: Dict[str, str] = None,
        basicAuthCredentials: str = None,
        enableBasicAuth: bool = None,
        tags: Dict[str, str] = None,
        buildSpec: str = None,
        ttl: str = None,
        displayName: str = None,
        enablePullRequestPreview: bool = None,
        pullRequestEnvironmentName: str = None,
        backendEnvironmentArn: str = None,
    ) -> CreateBranchResultTypeDef:
        """
        [Client.create_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.create_branch)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_deployment(
        self, appId: str, branchName: str, fileMap: Dict[str, str] = None
    ) -> CreateDeploymentResultTypeDef:
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.create_deployment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_domain_association(
        self,
        appId: str,
        domainName: str,
        subDomainSettings: List[SubDomainSettingTypeDef],
        enableAutoSubDomain: bool = None,
    ) -> CreateDomainAssociationResultTypeDef:
        """
        [Client.create_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.create_domain_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_webhook(
        self, appId: str, branchName: str, description: str = None
    ) -> CreateWebhookResultTypeDef:
        """
        [Client.create_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.create_webhook)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_app(self, appId: str) -> DeleteAppResultTypeDef:
        """
        [Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.delete_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_backend_environment(
        self, appId: str, environmentName: str
    ) -> DeleteBackendEnvironmentResultTypeDef:
        """
        [Client.delete_backend_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.delete_backend_environment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_branch(self, appId: str, branchName: str) -> DeleteBranchResultTypeDef:
        """
        [Client.delete_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.delete_branch)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_domain_association(
        self, appId: str, domainName: str
    ) -> DeleteDomainAssociationResultTypeDef:
        """
        [Client.delete_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.delete_domain_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_job(self, appId: str, branchName: str, jobId: str) -> DeleteJobResultTypeDef:
        """
        [Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.delete_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_webhook(self, webhookId: str) -> DeleteWebhookResultTypeDef:
        """
        [Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.delete_webhook)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_access_logs(
        self, domainName: str, appId: str, startTime: datetime = None, endTime: datetime = None
    ) -> GenerateAccessLogsResultTypeDef:
        """
        [Client.generate_access_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.generate_access_logs)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_app(self, appId: str) -> GetAppResultTypeDef:
        """
        [Client.get_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.get_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_artifact_url(self, artifactId: str) -> GetArtifactUrlResultTypeDef:
        """
        [Client.get_artifact_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.get_artifact_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_backend_environment(
        self, appId: str, environmentName: str
    ) -> GetBackendEnvironmentResultTypeDef:
        """
        [Client.get_backend_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.get_backend_environment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_branch(self, appId: str, branchName: str) -> GetBranchResultTypeDef:
        """
        [Client.get_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.get_branch)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_domain_association(
        self, appId: str, domainName: str
    ) -> GetDomainAssociationResultTypeDef:
        """
        [Client.get_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.get_domain_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job(self, appId: str, branchName: str, jobId: str) -> GetJobResultTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.get_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_webhook(self, webhookId: str) -> GetWebhookResultTypeDef:
        """
        [Client.get_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.get_webhook)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_apps(self, nextToken: str = None, maxResults: int = None) -> ListAppsResultTypeDef:
        """
        [Client.list_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.list_apps)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_artifacts(
        self, appId: str, branchName: str, jobId: str, nextToken: str = None, maxResults: int = None
    ) -> ListArtifactsResultTypeDef:
        """
        [Client.list_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.list_artifacts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_backend_environments(
        self, appId: str, environmentName: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListBackendEnvironmentsResultTypeDef:
        """
        [Client.list_backend_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.list_backend_environments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_branches(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ListBranchesResultTypeDef:
        """
        [Client.list_branches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.list_branches)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_domain_associations(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ListDomainAssociationsResultTypeDef:
        """
        [Client.list_domain_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.list_domain_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(
        self, appId: str, branchName: str, nextToken: str = None, maxResults: int = None
    ) -> ListJobsResultTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.list_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_webhooks(
        self, appId: str, nextToken: str = None, maxResults: int = None
    ) -> ListWebhooksResultTypeDef:
        """
        [Client.list_webhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.list_webhooks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_deployment(
        self, appId: str, branchName: str, jobId: str = None, sourceUrl: str = None
    ) -> StartDeploymentResultTypeDef:
        """
        [Client.start_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.start_deployment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_job(
        self,
        appId: str,
        branchName: str,
        jobType: Literal["RELEASE", "RETRY", "MANUAL", "WEB_HOOK"],
        jobId: str = None,
        jobReason: str = None,
        commitId: str = None,
        commitMessage: str = None,
        commitTime: datetime = None,
    ) -> StartJobResultTypeDef:
        """
        [Client.start_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.start_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_job(self, appId: str, branchName: str, jobId: str) -> StopJobResultTypeDef:
        """
        [Client.stop_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.stop_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_app(
        self,
        appId: str,
        name: str = None,
        description: str = None,
        platform: Literal["WEB"] = None,
        iamServiceRoleArn: str = None,
        environmentVariables: Dict[str, str] = None,
        enableBranchAutoBuild: bool = None,
        enableBasicAuth: bool = None,
        basicAuthCredentials: str = None,
        customRules: List[CustomRuleTypeDef] = None,
        buildSpec: str = None,
        enableAutoBranchCreation: bool = None,
        autoBranchCreationPatterns: List[str] = None,
        autoBranchCreationConfig: AutoBranchCreationConfigTypeDef = None,
        repository: str = None,
        oauthToken: str = None,
        accessToken: str = None,
    ) -> UpdateAppResultTypeDef:
        """
        [Client.update_app documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.update_app)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_branch(
        self,
        appId: str,
        branchName: str,
        description: str = None,
        framework: str = None,
        stage: Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"] = None,
        enableNotification: bool = None,
        enableAutoBuild: bool = None,
        environmentVariables: Dict[str, str] = None,
        basicAuthCredentials: str = None,
        enableBasicAuth: bool = None,
        buildSpec: str = None,
        ttl: str = None,
        displayName: str = None,
        enablePullRequestPreview: bool = None,
        pullRequestEnvironmentName: str = None,
        backendEnvironmentArn: str = None,
    ) -> UpdateBranchResultTypeDef:
        """
        [Client.update_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.update_branch)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_domain_association(
        self,
        appId: str,
        domainName: str,
        subDomainSettings: List[SubDomainSettingTypeDef],
        enableAutoSubDomain: bool = None,
    ) -> UpdateDomainAssociationResultTypeDef:
        """
        [Client.update_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.update_domain_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_webhook(
        self, webhookId: str, branchName: str = None, description: str = None
    ) -> UpdateWebhookResultTypeDef:
        """
        [Client.update_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Client.update_webhook)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_apps"]
    ) -> paginator_scope.ListAppsPaginator:
        """
        [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Paginator.ListApps)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_branches"]
    ) -> paginator_scope.ListBranchesPaginator:
        """
        [Paginator.ListBranches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Paginator.ListBranches)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_domain_associations"]
    ) -> paginator_scope.ListDomainAssociationsPaginator:
        """
        [Paginator.ListDomainAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Paginator.ListDomainAssociations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> paginator_scope.ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/amplify.html#Amplify.Paginator.ListJobs)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    DependentServiceFailureException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
