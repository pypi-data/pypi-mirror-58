"Main interface for fms service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_fms.client as client_scope

# pylint: disable=import-self
import mypy_boto3_fms.paginator as paginator_scope
from mypy_boto3_fms.type_defs import (
    GetAdminAccountResponseTypeDef,
    GetComplianceDetailResponseTypeDef,
    GetNotificationChannelResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetProtectionStatusResponseTypeDef,
    ListComplianceStatusResponseTypeDef,
    ListMemberAccountsResponseTypeDef,
    ListPoliciesResponseTypeDef,
    PolicyTypeDef,
    PutPolicyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FMSClient",)


class FMSClient(BaseClient):
    """
    [FMS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_admin_account(self, AdminAccount: str) -> None:
        """
        [Client.associate_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.associate_admin_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_notification_channel(self) -> None:
        """
        [Client.delete_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.delete_notification_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_policy(self, PolicyId: str, DeleteAllPolicyResources: bool = None) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.delete_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_admin_account(self) -> None:
        """
        [Client.disassociate_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.disassociate_admin_account)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_admin_account(self) -> GetAdminAccountResponseTypeDef:
        """
        [Client.get_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.get_admin_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_compliance_detail(
        self, PolicyId: str, MemberAccount: str
    ) -> GetComplianceDetailResponseTypeDef:
        """
        [Client.get_compliance_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.get_compliance_detail)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_notification_channel(self) -> GetNotificationChannelResponseTypeDef:
        """
        [Client.get_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.get_notification_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_policy(self, PolicyId: str) -> GetPolicyResponseTypeDef:
        """
        [Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.get_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_protection_status(
        self,
        PolicyId: str,
        MemberAccountId: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetProtectionStatusResponseTypeDef:
        """
        [Client.get_protection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.get_protection_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_compliance_status(
        self, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListComplianceStatusResponseTypeDef:
        """
        [Client.list_compliance_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.list_compliance_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_member_accounts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListMemberAccountsResponseTypeDef:
        """
        [Client.list_member_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.list_member_accounts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_policies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListPoliciesResponseTypeDef:
        """
        [Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.list_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_notification_channel(self, SnsTopicArn: str, SnsRoleName: str) -> None:
        """
        [Client.put_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.put_notification_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_policy(self, Policy: PolicyTypeDef) -> PutPolicyResponseTypeDef:
        """
        [Client.put_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Client.put_policy)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_compliance_status"]
    ) -> paginator_scope.ListComplianceStatusPaginator:
        """
        [Paginator.ListComplianceStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Paginator.ListComplianceStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_member_accounts"]
    ) -> paginator_scope.ListMemberAccountsPaginator:
        """
        [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Paginator.ListMemberAccounts)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_policies"]
    ) -> paginator_scope.ListPoliciesPaginator:
        """
        [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/fms.html#FMS.Paginator.ListPolicies)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    InvalidTypeException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
