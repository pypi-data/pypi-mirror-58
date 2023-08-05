"Main interface for iam service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iam.type_defs import (
    ContextEntryTypeDef,
    GetAccountAuthorizationDetailsResponseTypeDef,
    GetGroupResponseTypeDef,
    ListAccessKeysResponseTypeDef,
    ListAccountAliasesResponseTypeDef,
    ListAttachedGroupPoliciesResponseTypeDef,
    ListAttachedRolePoliciesResponseTypeDef,
    ListAttachedUserPoliciesResponseTypeDef,
    ListEntitiesForPolicyResponseTypeDef,
    ListGroupPoliciesResponseTypeDef,
    ListGroupsForUserResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListInstanceProfilesForRoleResponseTypeDef,
    ListInstanceProfilesResponseTypeDef,
    ListMFADevicesResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyVersionsResponseTypeDef,
    ListRolePoliciesResponseTypeDef,
    ListRolesResponseTypeDef,
    ListSSHPublicKeysResponseTypeDef,
    ListServerCertificatesResponseTypeDef,
    ListSigningCertificatesResponseTypeDef,
    ListUserPoliciesResponseTypeDef,
    ListUsersResponseTypeDef,
    ListVirtualMFADevicesResponseTypeDef,
    PaginatorConfigTypeDef,
    SimulatePolicyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetAccountAuthorizationDetailsPaginator",
    "GetGroupPaginator",
    "ListAccessKeysPaginator",
    "ListAccountAliasesPaginator",
    "ListAttachedGroupPoliciesPaginator",
    "ListAttachedRolePoliciesPaginator",
    "ListAttachedUserPoliciesPaginator",
    "ListEntitiesForPolicyPaginator",
    "ListGroupPoliciesPaginator",
    "ListGroupsPaginator",
    "ListGroupsForUserPaginator",
    "ListInstanceProfilesPaginator",
    "ListInstanceProfilesForRolePaginator",
    "ListMFADevicesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyVersionsPaginator",
    "ListRolePoliciesPaginator",
    "ListRolesPaginator",
    "ListSSHPublicKeysPaginator",
    "ListServerCertificatesPaginator",
    "ListSigningCertificatesPaginator",
    "ListUserPoliciesPaginator",
    "ListUsersPaginator",
    "ListVirtualMFADevicesPaginator",
    "SimulateCustomPolicyPaginator",
    "SimulatePrincipalPolicyPaginator",
)


class GetAccountAuthorizationDetailsPaginator(Boto3Paginator):
    """
    [Paginator.GetAccountAuthorizationDetails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.GetAccountAuthorizationDetails)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: List[
            Literal["User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetAccountAuthorizationDetailsResponseTypeDef, None, None]:
        """
        [GetAccountAuthorizationDetails.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.GetAccountAuthorizationDetails.paginate)
        """


class GetGroupPaginator(Boto3Paginator):
    """
    [Paginator.GetGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.GetGroup)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetGroupResponseTypeDef, None, None]:
        """
        [GetGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.GetGroup.paginate)
        """


class ListAccessKeysPaginator(Boto3Paginator):
    """
    [Paginator.ListAccessKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListAccessKeys)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAccessKeysResponseTypeDef, None, None]:
        """
        [ListAccessKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListAccessKeys.paginate)
        """


class ListAccountAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListAccountAliases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAccountAliasesResponseTypeDef, None, None]:
        """
        [ListAccountAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListAccountAliases.paginate)
        """


class ListAttachedGroupPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttachedGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListAttachedGroupPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GroupName: str,
        PathPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAttachedGroupPoliciesResponseTypeDef, None, None]:
        """
        [ListAttachedGroupPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListAttachedGroupPolicies.paginate)
        """


class ListAttachedRolePoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttachedRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListAttachedRolePolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, RoleName: str, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAttachedRolePoliciesResponseTypeDef, None, None]:
        """
        [ListAttachedRolePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListAttachedRolePolicies.paginate)
        """


class ListAttachedUserPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttachedUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListAttachedUserPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserName: str, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAttachedUserPoliciesResponseTypeDef, None, None]:
        """
        [ListAttachedUserPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListAttachedUserPolicies.paginate)
        """


class ListEntitiesForPolicyPaginator(Boto3Paginator):
    """
    [Paginator.ListEntitiesForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListEntitiesForPolicy)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PolicyArn: str,
        EntityFilter: Literal[
            "User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"
        ] = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListEntitiesForPolicyResponseTypeDef, None, None]:
        """
        [ListEntitiesForPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListEntitiesForPolicy.paginate)
        """


class ListGroupPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListGroupPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGroupPoliciesResponseTypeDef, None, None]:
        """
        [ListGroupPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListGroupPolicies.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGroupsResponseTypeDef, None, None]:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListGroups.paginate)
        """


class ListGroupsForUserPaginator(Boto3Paginator):
    """
    [Paginator.ListGroupsForUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListGroupsForUser)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGroupsForUserResponseTypeDef, None, None]:
        """
        [ListGroupsForUser.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListGroupsForUser.paginate)
        """


class ListInstanceProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListInstanceProfiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInstanceProfilesResponseTypeDef, None, None]:
        """
        [ListInstanceProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListInstanceProfiles.paginate)
        """


class ListInstanceProfilesForRolePaginator(Boto3Paginator):
    """
    [Paginator.ListInstanceProfilesForRole documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListInstanceProfilesForRole)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, RoleName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInstanceProfilesForRoleResponseTypeDef, None, None]:
        """
        [ListInstanceProfilesForRole.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListInstanceProfilesForRole.paginate)
        """


class ListMFADevicesPaginator(Boto3Paginator):
    """
    [Paginator.ListMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListMFADevices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMFADevicesResponseTypeDef, None, None]:
        """
        [ListMFADevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListMFADevices.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Scope: Literal["All", "AWS", "Local"] = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPoliciesResponseTypeDef, None, None]:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListPolicies.paginate)
        """


class ListPolicyVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicyVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListPolicyVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PolicyArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPolicyVersionsResponseTypeDef, None, None]:
        """
        [ListPolicyVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListPolicyVersions.paginate)
        """


class ListRolePoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListRolePolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, RoleName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRolePoliciesResponseTypeDef, None, None]:
        """
        [ListRolePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListRolePolicies.paginate)
        """


class ListRolesPaginator(Boto3Paginator):
    """
    [Paginator.ListRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListRoles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRolesResponseTypeDef, None, None]:
        """
        [ListRoles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListRoles.paginate)
        """


class ListSSHPublicKeysPaginator(Boto3Paginator):
    """
    [Paginator.ListSSHPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListSSHPublicKeys)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSSHPublicKeysResponseTypeDef, None, None]:
        """
        [ListSSHPublicKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListSSHPublicKeys.paginate)
        """


class ListServerCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.ListServerCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListServerCertificates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListServerCertificatesResponseTypeDef, None, None]:
        """
        [ListServerCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListServerCertificates.paginate)
        """


class ListSigningCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.ListSigningCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListSigningCertificates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSigningCertificatesResponseTypeDef, None, None]:
        """
        [ListSigningCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListSigningCertificates.paginate)
        """


class ListUserPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListUserPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListUserPoliciesResponseTypeDef, None, None]:
        """
        [ListUserPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListUserPolicies.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListUsers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PathPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListUsersResponseTypeDef, None, None]:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListUsers.paginate)
        """


class ListVirtualMFADevicesPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListVirtualMFADevices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AssignmentStatus: Literal["Assigned", "Unassigned", "Any"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListVirtualMFADevicesResponseTypeDef, None, None]:
        """
        [ListVirtualMFADevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.ListVirtualMFADevices.paginate)
        """


class SimulateCustomPolicyPaginator(Boto3Paginator):
    """
    [Paginator.SimulateCustomPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.SimulateCustomPolicy)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PolicyInputList: List[str],
        ActionNames: List[str],
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ContextEntryTypeDef] = None,
        ResourceHandlingOption: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SimulatePolicyResponseTypeDef, None, None]:
        """
        [SimulateCustomPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.SimulateCustomPolicy.paginate)
        """


class SimulatePrincipalPolicyPaginator(Boto3Paginator):
    """
    [Paginator.SimulatePrincipalPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.SimulatePrincipalPolicy)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PolicySourceArn: str,
        ActionNames: List[str],
        PolicyInputList: List[str] = None,
        ResourceArns: List[str] = None,
        ResourcePolicy: str = None,
        ResourceOwner: str = None,
        CallerArn: str = None,
        ContextEntries: List[ContextEntryTypeDef] = None,
        ResourceHandlingOption: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SimulatePolicyResponseTypeDef, None, None]:
        """
        [SimulatePrincipalPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iam.html#IAM.Paginator.SimulatePrincipalPolicy.paginate)
        """
