"Main interface for macie service"
from mypy_boto3_macie.client import MacieClient as Client, MacieClient
from mypy_boto3_macie.paginator import ListMemberAccountsPaginator, ListS3ResourcesPaginator


__all__ = ("Client", "ListMemberAccountsPaginator", "ListS3ResourcesPaginator", "MacieClient")
