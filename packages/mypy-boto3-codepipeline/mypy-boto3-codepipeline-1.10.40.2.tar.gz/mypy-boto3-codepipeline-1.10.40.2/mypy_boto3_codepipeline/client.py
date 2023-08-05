"Main interface for codepipeline service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_codepipeline.client as client_scope

# pylint: disable=import-self
import mypy_boto3_codepipeline.paginator as paginator_scope
from mypy_boto3_codepipeline.type_defs import (
    AcknowledgeJobOutputTypeDef,
    AcknowledgeThirdPartyJobOutputTypeDef,
    ActionConfigurationPropertyTypeDef,
    ActionExecutionFilterTypeDef,
    ActionRevisionTypeDef,
    ActionTypeIdTypeDef,
    ActionTypeSettingsTypeDef,
    ApprovalResultTypeDef,
    ArtifactDetailsTypeDef,
    CreateCustomActionTypeOutputTypeDef,
    CreatePipelineOutputTypeDef,
    CurrentRevisionTypeDef,
    ExecutionDetailsTypeDef,
    FailureDetailsTypeDef,
    GetJobDetailsOutputTypeDef,
    GetPipelineExecutionOutputTypeDef,
    GetPipelineOutputTypeDef,
    GetPipelineStateOutputTypeDef,
    GetThirdPartyJobDetailsOutputTypeDef,
    ListActionExecutionsOutputTypeDef,
    ListActionTypesOutputTypeDef,
    ListPipelineExecutionsOutputTypeDef,
    ListPipelinesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWebhooksOutputTypeDef,
    PipelineDeclarationTypeDef,
    PollForJobsOutputTypeDef,
    PollForThirdPartyJobsOutputTypeDef,
    PutActionRevisionOutputTypeDef,
    PutApprovalResultOutputTypeDef,
    PutWebhookOutputTypeDef,
    RetryStageExecutionOutputTypeDef,
    StartPipelineExecutionOutputTypeDef,
    TagTypeDef,
    UpdatePipelineOutputTypeDef,
    WebhookDefinitionTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodePipelineClient",)


class CodePipelineClient(BaseClient):
    """
    [CodePipeline.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def acknowledge_job(self, jobId: str, nonce: str) -> AcknowledgeJobOutputTypeDef:
        """
        [Client.acknowledge_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.acknowledge_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def acknowledge_third_party_job(
        self, jobId: str, nonce: str, clientToken: str
    ) -> AcknowledgeThirdPartyJobOutputTypeDef:
        """
        [Client.acknowledge_third_party_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.acknowledge_third_party_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_custom_action_type(
        self,
        category: Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        provider: str,
        version: str,
        inputArtifactDetails: ArtifactDetailsTypeDef,
        outputArtifactDetails: ArtifactDetailsTypeDef,
        settings: ActionTypeSettingsTypeDef = None,
        configurationProperties: List[ActionConfigurationPropertyTypeDef] = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateCustomActionTypeOutputTypeDef:
        """
        [Client.create_custom_action_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.create_custom_action_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_pipeline(
        self, pipeline: PipelineDeclarationTypeDef, tags: List[TagTypeDef] = None
    ) -> CreatePipelineOutputTypeDef:
        """
        [Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.create_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_custom_action_type(
        self,
        category: Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        provider: str,
        version: str,
    ) -> None:
        """
        [Client.delete_custom_action_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.delete_custom_action_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_pipeline(self, name: str) -> None:
        """
        [Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.delete_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_webhook(self, name: str) -> Dict[str, Any]:
        """
        [Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.delete_webhook)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_webhook_with_third_party(self, webhookName: str = None) -> Dict[str, Any]:
        """
        [Client.deregister_webhook_with_third_party documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.deregister_webhook_with_third_party)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_stage_transition(
        self,
        pipelineName: str,
        stageName: str,
        transitionType: Literal["Inbound", "Outbound"],
        reason: str,
    ) -> None:
        """
        [Client.disable_stage_transition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.disable_stage_transition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_stage_transition(
        self, pipelineName: str, stageName: str, transitionType: Literal["Inbound", "Outbound"]
    ) -> None:
        """
        [Client.enable_stage_transition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.enable_stage_transition)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_details(self, jobId: str) -> GetJobDetailsOutputTypeDef:
        """
        [Client.get_job_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.get_job_details)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_pipeline(self, name: str, version: int = None) -> GetPipelineOutputTypeDef:
        """
        [Client.get_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_pipeline_execution(
        self, pipelineName: str, pipelineExecutionId: str
    ) -> GetPipelineExecutionOutputTypeDef:
        """
        [Client.get_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_pipeline_state(self, name: str) -> GetPipelineStateOutputTypeDef:
        """
        [Client.get_pipeline_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_state)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_third_party_job_details(
        self, jobId: str, clientToken: str
    ) -> GetThirdPartyJobDetailsOutputTypeDef:
        """
        [Client.get_third_party_job_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.get_third_party_job_details)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_action_executions(
        self,
        pipelineName: str,
        filter: ActionExecutionFilterTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListActionExecutionsOutputTypeDef:
        """
        [Client.list_action_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.list_action_executions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_action_types(
        self,
        actionOwnerFilter: Literal["AWS", "ThirdParty", "Custom"] = None,
        nextToken: str = None,
    ) -> ListActionTypesOutputTypeDef:
        """
        [Client.list_action_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.list_action_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_pipeline_executions(
        self, pipelineName: str, maxResults: int = None, nextToken: str = None
    ) -> ListPipelineExecutionsOutputTypeDef:
        """
        [Client.list_pipeline_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.list_pipeline_executions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_pipelines(self, nextToken: str = None) -> ListPipelinesOutputTypeDef:
        """
        [Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.list_pipelines)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_webhooks(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListWebhooksOutputTypeDef:
        """
        [Client.list_webhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.list_webhooks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def poll_for_jobs(
        self,
        actionTypeId: ActionTypeIdTypeDef,
        maxBatchSize: int = None,
        queryParam: Dict[str, str] = None,
    ) -> PollForJobsOutputTypeDef:
        """
        [Client.poll_for_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.poll_for_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def poll_for_third_party_jobs(
        self, actionTypeId: ActionTypeIdTypeDef, maxBatchSize: int = None
    ) -> PollForThirdPartyJobsOutputTypeDef:
        """
        [Client.poll_for_third_party_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.poll_for_third_party_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_action_revision(
        self,
        pipelineName: str,
        stageName: str,
        actionName: str,
        actionRevision: ActionRevisionTypeDef,
    ) -> PutActionRevisionOutputTypeDef:
        """
        [Client.put_action_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.put_action_revision)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_approval_result(
        self,
        pipelineName: str,
        stageName: str,
        actionName: str,
        result: ApprovalResultTypeDef,
        token: str,
    ) -> PutApprovalResultOutputTypeDef:
        """
        [Client.put_approval_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.put_approval_result)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_job_failure_result(self, jobId: str, failureDetails: FailureDetailsTypeDef) -> None:
        """
        [Client.put_job_failure_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.put_job_failure_result)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_job_success_result(
        self,
        jobId: str,
        currentRevision: CurrentRevisionTypeDef = None,
        continuationToken: str = None,
        executionDetails: ExecutionDetailsTypeDef = None,
        outputVariables: Dict[str, str] = None,
    ) -> None:
        """
        [Client.put_job_success_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.put_job_success_result)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_third_party_job_failure_result(
        self, jobId: str, clientToken: str, failureDetails: FailureDetailsTypeDef
    ) -> None:
        """
        [Client.put_third_party_job_failure_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.put_third_party_job_failure_result)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_third_party_job_success_result(
        self,
        jobId: str,
        clientToken: str,
        currentRevision: CurrentRevisionTypeDef = None,
        continuationToken: str = None,
        executionDetails: ExecutionDetailsTypeDef = None,
    ) -> None:
        """
        [Client.put_third_party_job_success_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.put_third_party_job_success_result)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_webhook(
        self, webhook: WebhookDefinitionTypeDef, tags: List[TagTypeDef] = None
    ) -> PutWebhookOutputTypeDef:
        """
        [Client.put_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.put_webhook)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_webhook_with_third_party(self, webhookName: str = None) -> Dict[str, Any]:
        """
        [Client.register_webhook_with_third_party documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.register_webhook_with_third_party)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def retry_stage_execution(
        self,
        pipelineName: str,
        stageName: str,
        pipelineExecutionId: str,
        retryMode: Literal["FAILED_ACTIONS"],
    ) -> RetryStageExecutionOutputTypeDef:
        """
        [Client.retry_stage_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.retry_stage_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_pipeline_execution(
        self, name: str, clientRequestToken: str = None
    ) -> StartPipelineExecutionOutputTypeDef:
        """
        [Client.start_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.start_pipeline_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_pipeline(self, pipeline: PipelineDeclarationTypeDef) -> UpdatePipelineOutputTypeDef:
        """
        [Client.update_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Client.update_pipeline)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_action_executions"]
    ) -> paginator_scope.ListActionExecutionsPaginator:
        """
        [Paginator.ListActionExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionExecutions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_action_types"]
    ) -> paginator_scope.ListActionTypesPaginator:
        """
        [Paginator.ListActionTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionTypes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_pipeline_executions"]
    ) -> paginator_scope.ListPipelineExecutionsPaginator:
        """
        [Paginator.ListPipelineExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelineExecutions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_pipelines"]
    ) -> paginator_scope.ListPipelinesPaginator:
        """
        [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelines)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Paginator.ListTagsForResource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_webhooks"]
    ) -> paginator_scope.ListWebhooksPaginator:
        """
        [Paginator.ListWebhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codepipeline.html#CodePipeline.Paginator.ListWebhooks)
        """


class Exceptions:
    ActionNotFoundException: Boto3ClientError
    ActionTypeNotFoundException: Boto3ClientError
    ApprovalAlreadyCompletedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InvalidActionDeclarationException: Boto3ClientError
    InvalidApprovalTokenException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidBlockerDeclarationException: Boto3ClientError
    InvalidClientTokenException: Boto3ClientError
    InvalidJobException: Boto3ClientError
    InvalidJobStateException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidNonceException: Boto3ClientError
    InvalidStageDeclarationException: Boto3ClientError
    InvalidStructureException: Boto3ClientError
    InvalidTagsException: Boto3ClientError
    InvalidWebhookAuthenticationParametersException: Boto3ClientError
    InvalidWebhookFilterPatternException: Boto3ClientError
    JobNotFoundException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotLatestPipelineExecutionException: Boto3ClientError
    OutputVariablesSizeExceededException: Boto3ClientError
    PipelineExecutionNotFoundException: Boto3ClientError
    PipelineNameInUseException: Boto3ClientError
    PipelineNotFoundException: Boto3ClientError
    PipelineVersionNotFoundException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    StageNotFoundException: Boto3ClientError
    StageNotRetryableException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    ValidationException: Boto3ClientError
    WebhookNotFoundException: Boto3ClientError
