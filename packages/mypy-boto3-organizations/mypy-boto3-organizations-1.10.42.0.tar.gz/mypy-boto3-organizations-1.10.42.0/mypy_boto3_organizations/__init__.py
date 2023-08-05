"Main interface for organizations service"
from mypy_boto3_organizations.client import OrganizationsClient, OrganizationsClient as Client
from mypy_boto3_organizations.paginator import (
    ListAWSServiceAccessForOrganizationPaginator,
    ListAccountsForParentPaginator,
    ListAccountsPaginator,
    ListChildrenPaginator,
    ListCreateAccountStatusPaginator,
    ListHandshakesForAccountPaginator,
    ListHandshakesForOrganizationPaginator,
    ListOrganizationalUnitsForParentPaginator,
    ListParentsPaginator,
    ListPoliciesForTargetPaginator,
    ListPoliciesPaginator,
    ListRootsPaginator,
    ListTagsForResourcePaginator,
    ListTargetsForPolicyPaginator,
)


__all__ = (
    "Client",
    "ListAWSServiceAccessForOrganizationPaginator",
    "ListAccountsForParentPaginator",
    "ListAccountsPaginator",
    "ListChildrenPaginator",
    "ListCreateAccountStatusPaginator",
    "ListHandshakesForAccountPaginator",
    "ListHandshakesForOrganizationPaginator",
    "ListOrganizationalUnitsForParentPaginator",
    "ListParentsPaginator",
    "ListPoliciesForTargetPaginator",
    "ListPoliciesPaginator",
    "ListRootsPaginator",
    "ListTagsForResourcePaginator",
    "ListTargetsForPolicyPaginator",
    "OrganizationsClient",
)
