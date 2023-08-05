"Main interface for codebuild service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codebuild.type_defs import (
    ListBuildsForProjectOutputTypeDef,
    ListBuildsOutputTypeDef,
    ListProjectsOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListBuildsPaginator", "ListBuildsForProjectPaginator", "ListProjectsPaginator")


class ListBuildsPaginator(Boto3Paginator):
    """
    [Paginator.ListBuilds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListBuildsOutputTypeDef, None, None]:
        """
        [ListBuilds.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds.paginate)
        """


class ListBuildsForProjectPaginator(Boto3Paginator):
    """
    [Paginator.ListBuildsForProject documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        projectName: str,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListBuildsForProjectOutputTypeDef, None, None]:
        """
        [ListBuildsForProject.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListProjectsOutputTypeDef, None, None]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects.paginate)
        """
