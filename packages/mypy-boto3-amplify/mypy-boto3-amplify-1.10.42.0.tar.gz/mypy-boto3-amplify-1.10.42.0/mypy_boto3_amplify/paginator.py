"Main interface for amplify service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_amplify.type_defs import (
    ListAppsResultTypeDef,
    ListBranchesResultTypeDef,
    ListDomainAssociationsResultTypeDef,
    ListJobsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListAppsPaginator",
    "ListBranchesPaginator",
    "ListDomainAssociationsPaginator",
    "ListJobsPaginator",
)


class ListAppsPaginator(Boto3Paginator):
    """
    [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/amplify.html#Amplify.Paginator.ListApps)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAppsResultTypeDef, None, None]:
        """
        [ListApps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/amplify.html#Amplify.Paginator.ListApps.paginate)
        """


class ListBranchesPaginator(Boto3Paginator):
    """
    [Paginator.ListBranches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/amplify.html#Amplify.Paginator.ListBranches)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, appId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListBranchesResultTypeDef, None, None]:
        """
        [ListBranches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/amplify.html#Amplify.Paginator.ListBranches.paginate)
        """


class ListDomainAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomainAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/amplify.html#Amplify.Paginator.ListDomainAssociations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, appId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDomainAssociationsResultTypeDef, None, None]:
        """
        [ListDomainAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/amplify.html#Amplify.Paginator.ListDomainAssociations.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/amplify.html#Amplify.Paginator.ListJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, appId: str, branchName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListJobsResultTypeDef, None, None]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/amplify.html#Amplify.Paginator.ListJobs.paginate)
        """
