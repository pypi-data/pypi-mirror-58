"Main interface for organizations service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_organizations.type_defs import (
    HandshakeFilterTypeDef,
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
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAWSServiceAccessForOrganizationPaginator",
    "ListAccountsPaginator",
    "ListAccountsForParentPaginator",
    "ListChildrenPaginator",
    "ListCreateAccountStatusPaginator",
    "ListHandshakesForAccountPaginator",
    "ListHandshakesForOrganizationPaginator",
    "ListOrganizationalUnitsForParentPaginator",
    "ListParentsPaginator",
    "ListPoliciesPaginator",
    "ListPoliciesForTargetPaginator",
    "ListRootsPaginator",
    "ListTagsForResourcePaginator",
    "ListTargetsForPolicyPaginator",
)


class ListAWSServiceAccessForOrganizationPaginator(Boto3Paginator):
    """
    [Paginator.ListAWSServiceAccessForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAWSServiceAccessForOrganizationResponseTypeDef, None, None]:
        """
        [ListAWSServiceAccessForOrganization.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization.paginate)
        """


class ListAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListAccounts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAccountsResponseTypeDef, None, None]:
        """
        [ListAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListAccounts.paginate)
        """


class ListAccountsForParentPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ParentId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAccountsForParentResponseTypeDef, None, None]:
        """
        [ListAccountsForParent.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent.paginate)
        """


class ListChildrenPaginator(Boto3Paginator):
    """
    [Paginator.ListChildren documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListChildren)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ParentId: str,
        ChildType: Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListChildrenResponseTypeDef, None, None]:
        """
        [ListChildren.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListChildren.paginate)
        """


class ListCreateAccountStatusPaginator(Boto3Paginator):
    """
    [Paginator.ListCreateAccountStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        States: List[Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListCreateAccountStatusResponseTypeDef, None, None]:
        """
        [ListCreateAccountStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus.paginate)
        """


class ListHandshakesForAccountPaginator(Boto3Paginator):
    """
    [Paginator.ListHandshakesForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filter: HandshakeFilterTypeDef = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListHandshakesForAccountResponseTypeDef, None, None]:
        """
        [ListHandshakesForAccount.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount.paginate)
        """


class ListHandshakesForOrganizationPaginator(Boto3Paginator):
    """
    [Paginator.ListHandshakesForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filter: HandshakeFilterTypeDef = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListHandshakesForOrganizationResponseTypeDef, None, None]:
        """
        [ListHandshakesForOrganization.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization.paginate)
        """


class ListOrganizationalUnitsForParentPaginator(Boto3Paginator):
    """
    [Paginator.ListOrganizationalUnitsForParent documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ParentId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListOrganizationalUnitsForParentResponseTypeDef, None, None]:
        """
        [ListOrganizationalUnitsForParent.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent.paginate)
        """


class ListParentsPaginator(Boto3Paginator):
    """
    [Paginator.ListParents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListParents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ChildId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListParentsResponseTypeDef, None, None]:
        """
        [ListParents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListParents.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPoliciesResponseTypeDef, None, None]:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListPolicies.paginate)
        """


class ListPoliciesForTargetPaginator(Boto3Paginator):
    """
    [Paginator.ListPoliciesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TargetId: str,
        Filter: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPoliciesForTargetResponseTypeDef, None, None]:
        """
        [ListPoliciesForTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget.paginate)
        """


class ListRootsPaginator(Boto3Paginator):
    """
    [Paginator.ListRoots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListRoots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRootsResponseTypeDef, None, None]:
        """
        [ListRoots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListRoots.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceResponseTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource.paginate)
        """


class ListTargetsForPolicyPaginator(Boto3Paginator):
    """
    [Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PolicyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTargetsForPolicyResponseTypeDef, None, None]:
        """
        [ListTargetsForPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy.paginate)
        """
