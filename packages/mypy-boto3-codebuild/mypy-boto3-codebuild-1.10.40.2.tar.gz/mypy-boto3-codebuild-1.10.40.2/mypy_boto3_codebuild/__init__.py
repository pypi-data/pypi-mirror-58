"Main interface for codebuild service"
from mypy_boto3_codebuild.client import CodeBuildClient as Client, CodeBuildClient
from mypy_boto3_codebuild.paginator import (
    ListBuildsForProjectPaginator,
    ListBuildsPaginator,
    ListProjectsPaginator,
)


__all__ = (
    "Client",
    "CodeBuildClient",
    "ListBuildsForProjectPaginator",
    "ListBuildsPaginator",
    "ListProjectsPaginator",
)
