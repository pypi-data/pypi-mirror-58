"Main interface for macie service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_macie.type_defs import (
    ListMemberAccountsResultTypeDef,
    ListS3ResourcesResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListMemberAccountsPaginator", "ListS3ResourcesPaginator")


class ListMemberAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Paginator.ListMemberAccounts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMemberAccountsResultTypeDef, None, None]:
        """
        [ListMemberAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Paginator.ListMemberAccounts.paginate)
        """


class ListS3ResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListS3Resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Paginator.ListS3Resources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, memberAccountId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListS3ResourcesResultTypeDef, None, None]:
        """
        [ListS3Resources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Paginator.ListS3Resources.paginate)
        """
