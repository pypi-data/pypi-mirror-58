"Main interface for fms service"
from mypy_boto3_fms.client import FMSClient as Client, FMSClient
from mypy_boto3_fms.paginator import (
    ListComplianceStatusPaginator,
    ListMemberAccountsPaginator,
    ListPoliciesPaginator,
)


__all__ = (
    "Client",
    "FMSClient",
    "ListComplianceStatusPaginator",
    "ListMemberAccountsPaginator",
    "ListPoliciesPaginator",
)
