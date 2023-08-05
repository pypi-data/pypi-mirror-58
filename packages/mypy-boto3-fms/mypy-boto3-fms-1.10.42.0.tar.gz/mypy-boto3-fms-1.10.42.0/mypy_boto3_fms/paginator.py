"Main interface for fms service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_fms.type_defs import (
    ListComplianceStatusResponseTypeDef,
    ListMemberAccountsResponseTypeDef,
    ListPoliciesResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListComplianceStatusPaginator", "ListMemberAccountsPaginator", "ListPoliciesPaginator")


class ListComplianceStatusPaginator(Boto3Paginator):
    """
    [Paginator.ListComplianceStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/fms.html#FMS.Paginator.ListComplianceStatus)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PolicyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListComplianceStatusResponseTypeDef, None, None]:
        """
        [ListComplianceStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/fms.html#FMS.Paginator.ListComplianceStatus.paginate)
        """


class ListMemberAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/fms.html#FMS.Paginator.ListMemberAccounts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMemberAccountsResponseTypeDef, None, None]:
        """
        [ListMemberAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/fms.html#FMS.Paginator.ListMemberAccounts.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/fms.html#FMS.Paginator.ListPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPoliciesResponseTypeDef, None, None]:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/fms.html#FMS.Paginator.ListPolicies.paginate)
        """
