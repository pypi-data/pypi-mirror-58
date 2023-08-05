"Main interface for codepipeline service"
from mypy_boto3_codepipeline.client import CodePipelineClient as Client, CodePipelineClient
from mypy_boto3_codepipeline.paginator import (
    ListActionExecutionsPaginator,
    ListActionTypesPaginator,
    ListPipelineExecutionsPaginator,
    ListPipelinesPaginator,
    ListTagsForResourcePaginator,
    ListWebhooksPaginator,
)


__all__ = (
    "Client",
    "CodePipelineClient",
    "ListActionExecutionsPaginator",
    "ListActionTypesPaginator",
    "ListPipelineExecutionsPaginator",
    "ListPipelinesPaginator",
    "ListTagsForResourcePaginator",
    "ListWebhooksPaginator",
)
