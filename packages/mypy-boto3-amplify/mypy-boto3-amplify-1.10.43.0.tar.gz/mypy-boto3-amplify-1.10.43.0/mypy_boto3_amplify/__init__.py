"Main interface for amplify service"
from mypy_boto3_amplify.client import AmplifyClient as Client, AmplifyClient
from mypy_boto3_amplify.paginator import (
    ListAppsPaginator,
    ListBranchesPaginator,
    ListDomainAssociationsPaginator,
    ListJobsPaginator,
)


__all__ = (
    "AmplifyClient",
    "Client",
    "ListAppsPaginator",
    "ListBranchesPaginator",
    "ListDomainAssociationsPaginator",
    "ListJobsPaginator",
)
