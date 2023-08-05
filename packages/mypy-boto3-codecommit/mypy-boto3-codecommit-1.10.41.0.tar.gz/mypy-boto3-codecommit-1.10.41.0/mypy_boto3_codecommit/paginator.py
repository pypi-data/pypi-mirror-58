"Main interface for codecommit service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codecommit.type_defs import (
    DescribePullRequestEventsOutputTypeDef,
    GetCommentsForComparedCommitOutputTypeDef,
    GetCommentsForPullRequestOutputTypeDef,
    GetDifferencesOutputTypeDef,
    ListBranchesOutputTypeDef,
    ListPullRequestsOutputTypeDef,
    ListRepositoriesOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribePullRequestEventsPaginator",
    "GetCommentsForComparedCommitPaginator",
    "GetCommentsForPullRequestPaginator",
    "GetDifferencesPaginator",
    "ListBranchesPaginator",
    "ListPullRequestsPaginator",
    "ListRepositoriesPaginator",
)


class DescribePullRequestEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePullRequestEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pullRequestId: str,
        pullRequestEventType: Literal[
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_STATUS_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
        ] = None,
        actorArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribePullRequestEventsOutputTypeDef, None, None]:
        """
        [DescribePullRequestEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents.paginate)
        """


class GetCommentsForComparedCommitPaginator(Boto3Paginator):
    """
    [Paginator.GetCommentsForComparedCommit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetCommentsForComparedCommitOutputTypeDef, None, None]:
        """
        [GetCommentsForComparedCommit.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit.paginate)
        """


class GetCommentsForPullRequestPaginator(Boto3Paginator):
    """
    [Paginator.GetCommentsForPullRequest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetCommentsForPullRequestOutputTypeDef, None, None]:
        """
        [GetCommentsForPullRequest.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest.paginate)
        """


class GetDifferencesPaginator(Boto3Paginator):
    """
    [Paginator.GetDifferences documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetDifferencesOutputTypeDef, None, None]:
        """
        [GetDifferences.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences.paginate)
        """


class ListBranchesPaginator(Boto3Paginator):
    """
    [Paginator.ListBranches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, repositoryName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListBranchesOutputTypeDef, None, None]:
        """
        [ListBranches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches.paginate)
        """


class ListPullRequestsPaginator(Boto3Paginator):
    """
    [Paginator.ListPullRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: Literal["OPEN", "CLOSED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPullRequestsOutputTypeDef, None, None]:
        """
        [ListPullRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests.paginate)
        """


class ListRepositoriesPaginator(Boto3Paginator):
    """
    [Paginator.ListRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        sortBy: Literal["repositoryName", "lastModifiedDate"] = None,
        order: Literal["ascending", "descending"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRepositoriesOutputTypeDef, None, None]:
        """
        [ListRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories.paginate)
        """
