"Main interface for organizations service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_organizations.client as client_scope

# pylint: disable=import-self
import mypy_boto3_organizations.paginator as paginator_scope
from mypy_boto3_organizations.type_defs import (
    AcceptHandshakeResponseTypeDef,
    CancelHandshakeResponseTypeDef,
    CreateAccountResponseTypeDef,
    CreateGovCloudAccountResponseTypeDef,
    CreateOrganizationResponseTypeDef,
    CreateOrganizationalUnitResponseTypeDef,
    CreatePolicyResponseTypeDef,
    DeclineHandshakeResponseTypeDef,
    DescribeAccountResponseTypeDef,
    DescribeCreateAccountStatusResponseTypeDef,
    DescribeEffectivePolicyResponseTypeDef,
    DescribeHandshakeResponseTypeDef,
    DescribeOrganizationResponseTypeDef,
    DescribeOrganizationalUnitResponseTypeDef,
    DescribePolicyResponseTypeDef,
    DisablePolicyTypeResponseTypeDef,
    EnableAllFeaturesResponseTypeDef,
    EnablePolicyTypeResponseTypeDef,
    HandshakeFilterTypeDef,
    HandshakePartyTypeDef,
    InviteAccountToOrganizationResponseTypeDef,
    ListAWSServiceAccessForOrganizationResponseTypeDef,
    ListAccountsForParentResponseTypeDef,
    ListAccountsResponseTypeDef,
    ListChildrenResponseTypeDef,
    ListCreateAccountStatusResponseTypeDef,
    ListHandshakesForAccountResponseTypeDef,
    ListHandshakesForOrganizationResponseTypeDef,
    ListOrganizationalUnitsForParentResponseTypeDef,
    ListParentsResponseTypeDef,
    ListPoliciesForTargetResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListRootsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsForPolicyResponseTypeDef,
    TagTypeDef,
    UpdateOrganizationalUnitResponseTypeDef,
    UpdatePolicyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("OrganizationsClient",)


class OrganizationsClient(BaseClient):
    """
    [Organizations.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_handshake(self, HandshakeId: str) -> AcceptHandshakeResponseTypeDef:
        """
        [Client.accept_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.accept_handshake)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(self, PolicyId: str, TargetId: str) -> None:
        """
        [Client.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.attach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_handshake(self, HandshakeId: str) -> CancelHandshakeResponseTypeDef:
        """
        [Client.cancel_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.cancel_handshake)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_account(
        self,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: Literal["ALLOW", "DENY"] = None,
    ) -> CreateAccountResponseTypeDef:
        """
        [Client.create_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.create_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_gov_cloud_account(
        self,
        Email: str,
        AccountName: str,
        RoleName: str = None,
        IamUserAccessToBilling: Literal["ALLOW", "DENY"] = None,
    ) -> CreateGovCloudAccountResponseTypeDef:
        """
        [Client.create_gov_cloud_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.create_gov_cloud_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_organization(
        self, FeatureSet: Literal["ALL", "CONSOLIDATED_BILLING"] = None
    ) -> CreateOrganizationResponseTypeDef:
        """
        [Client.create_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.create_organization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_organizational_unit(
        self, ParentId: str, Name: str
    ) -> CreateOrganizationalUnitResponseTypeDef:
        """
        [Client.create_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.create_organizational_unit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy(
        self,
        Content: str,
        Description: str,
        Name: str,
        Type: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
    ) -> CreatePolicyResponseTypeDef:
        """
        [Client.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.create_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def decline_handshake(self, HandshakeId: str) -> DeclineHandshakeResponseTypeDef:
        """
        [Client.decline_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.decline_handshake)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_organization(self) -> None:
        """
        [Client.delete_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.delete_organization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_organizational_unit(self, OrganizationalUnitId: str) -> None:
        """
        [Client.delete_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.delete_organizational_unit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_policy(self, PolicyId: str) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.delete_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account(self, AccountId: str) -> DescribeAccountResponseTypeDef:
        """
        [Client.describe_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.describe_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_create_account_status(
        self, CreateAccountRequestId: str
    ) -> DescribeCreateAccountStatusResponseTypeDef:
        """
        [Client.describe_create_account_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.describe_create_account_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_effective_policy(
        self, PolicyType: Literal["TAG_POLICY"], TargetId: str = None
    ) -> DescribeEffectivePolicyResponseTypeDef:
        """
        [Client.describe_effective_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.describe_effective_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_handshake(self, HandshakeId: str) -> DescribeHandshakeResponseTypeDef:
        """
        [Client.describe_handshake documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.describe_handshake)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_organization(self) -> DescribeOrganizationResponseTypeDef:
        """
        [Client.describe_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.describe_organization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_organizational_unit(
        self, OrganizationalUnitId: str
    ) -> DescribeOrganizationalUnitResponseTypeDef:
        """
        [Client.describe_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.describe_organizational_unit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_policy(self, PolicyId: str) -> DescribePolicyResponseTypeDef:
        """
        [Client.describe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.describe_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(self, PolicyId: str, TargetId: str) -> None:
        """
        [Client.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.detach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_aws_service_access(self, ServicePrincipal: str) -> None:
        """
        [Client.disable_aws_service_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.disable_aws_service_access)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_policy_type(
        self, RootId: str, PolicyType: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"]
    ) -> DisablePolicyTypeResponseTypeDef:
        """
        [Client.disable_policy_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.disable_policy_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_all_features(self) -> EnableAllFeaturesResponseTypeDef:
        """
        [Client.enable_all_features documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.enable_all_features)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_aws_service_access(self, ServicePrincipal: str) -> None:
        """
        [Client.enable_aws_service_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.enable_aws_service_access)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_policy_type(
        self, RootId: str, PolicyType: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"]
    ) -> EnablePolicyTypeResponseTypeDef:
        """
        [Client.enable_policy_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.enable_policy_type)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invite_account_to_organization(
        self, Target: HandshakePartyTypeDef, Notes: str = None
    ) -> InviteAccountToOrganizationResponseTypeDef:
        """
        [Client.invite_account_to_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.invite_account_to_organization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def leave_organization(self) -> None:
        """
        [Client.leave_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.leave_organization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_accounts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountsResponseTypeDef:
        """
        [Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_accounts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_accounts_for_parent(
        self, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAccountsForParentResponseTypeDef:
        """
        [Client.list_accounts_for_parent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_accounts_for_parent)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_aws_service_access_for_organization(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListAWSServiceAccessForOrganizationResponseTypeDef:
        """
        [Client.list_aws_service_access_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_aws_service_access_for_organization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_children(
        self,
        ParentId: str,
        ChildType: Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListChildrenResponseTypeDef:
        """
        [Client.list_children documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_children)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_create_account_status(
        self,
        States: List[Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListCreateAccountStatusResponseTypeDef:
        """
        [Client.list_create_account_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_create_account_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_handshakes_for_account(
        self, Filter: HandshakeFilterTypeDef = None, NextToken: str = None, MaxResults: int = None
    ) -> ListHandshakesForAccountResponseTypeDef:
        """
        [Client.list_handshakes_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_handshakes_for_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_handshakes_for_organization(
        self, Filter: HandshakeFilterTypeDef = None, NextToken: str = None, MaxResults: int = None
    ) -> ListHandshakesForOrganizationResponseTypeDef:
        """
        [Client.list_handshakes_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_handshakes_for_organization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_organizational_units_for_parent(
        self, ParentId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListOrganizationalUnitsForParentResponseTypeDef:
        """
        [Client.list_organizational_units_for_parent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_organizational_units_for_parent)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_parents(
        self, ChildId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListParentsResponseTypeDef:
        """
        [Client.list_parents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_parents)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_policies(
        self,
        Filter: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPoliciesResponseTypeDef:
        """
        [Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_policies_for_target(
        self,
        TargetId: str,
        Filter: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPoliciesForTargetResponseTypeDef:
        """
        [Client.list_policies_for_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_policies_for_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_roots(self, NextToken: str = None, MaxResults: int = None) -> ListRootsResponseTypeDef:
        """
        [Client.list_roots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_roots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceId: str, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_targets_for_policy(
        self, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTargetsForPolicyResponseTypeDef:
        """
        [Client.list_targets_for_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.list_targets_for_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def move_account(self, AccountId: str, SourceParentId: str, DestinationParentId: str) -> None:
        """
        [Client.move_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.move_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_account_from_organization(self, AccountId: str) -> None:
        """
        [Client.remove_account_from_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.remove_account_from_organization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceId: str, Tags: List[TagTypeDef]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceId: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_organizational_unit(
        self, OrganizationalUnitId: str, Name: str = None
    ) -> UpdateOrganizationalUnitResponseTypeDef:
        """
        [Client.update_organizational_unit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.update_organizational_unit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_policy(
        self, PolicyId: str, Name: str = None, Description: str = None, Content: str = None
    ) -> UpdatePolicyResponseTypeDef:
        """
        [Client.update_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Client.update_policy)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_aws_service_access_for_organization"]
    ) -> paginator_scope.ListAWSServiceAccessForOrganizationPaginator:
        """
        [Paginator.ListAWSServiceAccessForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_accounts"]
    ) -> paginator_scope.ListAccountsPaginator:
        """
        [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListAccounts)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_accounts_for_parent"]
    ) -> paginator_scope.ListAccountsForParentPaginator:
        """
        [Paginator.ListAccountsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_children"]
    ) -> paginator_scope.ListChildrenPaginator:
        """
        [Paginator.ListChildren documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListChildren)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_create_account_status"]
    ) -> paginator_scope.ListCreateAccountStatusPaginator:
        """
        [Paginator.ListCreateAccountStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_account"]
    ) -> paginator_scope.ListHandshakesForAccountPaginator:
        """
        [Paginator.ListHandshakesForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_organization"]
    ) -> paginator_scope.ListHandshakesForOrganizationPaginator:
        """
        [Paginator.ListHandshakesForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_organizational_units_for_parent"]
    ) -> paginator_scope.ListOrganizationalUnitsForParentPaginator:
        """
        [Paginator.ListOrganizationalUnitsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_parents"]
    ) -> paginator_scope.ListParentsPaginator:
        """
        [Paginator.ListParents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListParents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_policies"]
    ) -> paginator_scope.ListPoliciesPaginator:
        """
        [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListPolicies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_policies_for_target"]
    ) -> paginator_scope.ListPoliciesForTargetPaginator:
        """
        [Paginator.ListPoliciesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_roots"]
    ) -> paginator_scope.ListRootsPaginator:
        """
        [Paginator.ListRoots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListRoots)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> paginator_scope.ListTargetsForPolicyPaginator:
        """
        [Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy)
        """


class Exceptions:
    AWSOrganizationsNotInUseException: Boto3ClientError
    AccessDeniedException: Boto3ClientError
    AccessDeniedForDependencyException: Boto3ClientError
    AccountNotFoundException: Boto3ClientError
    AccountOwnerNotVerifiedException: Boto3ClientError
    AlreadyInOrganizationException: Boto3ClientError
    ChildNotFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    ConstraintViolationException: Boto3ClientError
    CreateAccountStatusNotFoundException: Boto3ClientError
    DestinationParentNotFoundException: Boto3ClientError
    DuplicateAccountException: Boto3ClientError
    DuplicateHandshakeException: Boto3ClientError
    DuplicateOrganizationalUnitException: Boto3ClientError
    DuplicatePolicyAttachmentException: Boto3ClientError
    DuplicatePolicyException: Boto3ClientError
    EffectivePolicyNotFoundException: Boto3ClientError
    FinalizingOrganizationException: Boto3ClientError
    HandshakeAlreadyInStateException: Boto3ClientError
    HandshakeConstraintViolationException: Boto3ClientError
    HandshakeNotFoundException: Boto3ClientError
    InvalidHandshakeTransitionException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    MalformedPolicyDocumentException: Boto3ClientError
    MasterCannotLeaveOrganizationException: Boto3ClientError
    OrganizationNotEmptyException: Boto3ClientError
    OrganizationalUnitNotEmptyException: Boto3ClientError
    OrganizationalUnitNotFoundException: Boto3ClientError
    ParentNotFoundException: Boto3ClientError
    PolicyChangesInProgressException: Boto3ClientError
    PolicyInUseException: Boto3ClientError
    PolicyNotAttachedException: Boto3ClientError
    PolicyNotFoundException: Boto3ClientError
    PolicyTypeAlreadyEnabledException: Boto3ClientError
    PolicyTypeNotAvailableForOrganizationException: Boto3ClientError
    PolicyTypeNotEnabledException: Boto3ClientError
    RootNotFoundException: Boto3ClientError
    ServiceException: Boto3ClientError
    SourceParentNotFoundException: Boto3ClientError
    TargetNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnsupportedAPIEndpointException: Boto3ClientError
