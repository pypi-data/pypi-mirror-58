"Main interface for macie service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_macie.client as client_scope

# pylint: disable=import-self
import mypy_boto3_macie.paginator as paginator_scope
from mypy_boto3_macie.type_defs import (
    AssociateS3ResourcesResultTypeDef,
    DisassociateS3ResourcesResultTypeDef,
    ListMemberAccountsResultTypeDef,
    ListS3ResourcesResultTypeDef,
    S3ResourceClassificationTypeDef,
    S3ResourceClassificationUpdateTypeDef,
    S3ResourceTypeDef,
    UpdateS3ResourcesResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MacieClient",)


class MacieClient(BaseClient):
    """
    [Macie.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_member_account(self, memberAccountId: str) -> None:
        """
        [Client.associate_member_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Client.associate_member_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_s3_resources(
        self, s3Resources: List[S3ResourceClassificationTypeDef], memberAccountId: str = None
    ) -> AssociateS3ResourcesResultTypeDef:
        """
        [Client.associate_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Client.associate_s3_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_member_account(self, memberAccountId: str) -> None:
        """
        [Client.disassociate_member_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Client.disassociate_member_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_s3_resources(
        self, associatedS3Resources: List[S3ResourceTypeDef], memberAccountId: str = None
    ) -> DisassociateS3ResourcesResultTypeDef:
        """
        [Client.disassociate_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Client.disassociate_s3_resources)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_member_accounts(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListMemberAccountsResultTypeDef:
        """
        [Client.list_member_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Client.list_member_accounts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_s3_resources(
        self, memberAccountId: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListS3ResourcesResultTypeDef:
        """
        [Client.list_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Client.list_s3_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_s3_resources(
        self,
        s3ResourcesUpdate: List[S3ResourceClassificationUpdateTypeDef],
        memberAccountId: str = None,
    ) -> UpdateS3ResourcesResultTypeDef:
        """
        [Client.update_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Client.update_s3_resources)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_member_accounts"]
    ) -> paginator_scope.ListMemberAccountsPaginator:
        """
        [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Paginator.ListMemberAccounts)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_s3_resources"]
    ) -> paginator_scope.ListS3ResourcesPaginator:
        """
        [Paginator.ListS3Resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/macie.html#Macie.Paginator.ListS3Resources)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    LimitExceededException: Boto3ClientError
