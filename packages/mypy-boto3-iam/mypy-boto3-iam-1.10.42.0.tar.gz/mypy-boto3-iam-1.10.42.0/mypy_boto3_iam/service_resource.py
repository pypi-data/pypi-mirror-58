"Main interface for iam service ServiceResource"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_iam.service_resource as service_resource_scope
from mypy_boto3_iam.type_defs import (
    CreateAccessKeyResponseTypeDef,
    CreateGroupResponseTypeDef,
    CreateInstanceProfileResponseTypeDef,
    CreateLoginProfileResponseTypeDef,
    CreatePolicyResponseTypeDef,
    CreatePolicyVersionResponseTypeDef,
    CreateRoleResponseTypeDef,
    CreateSAMLProviderResponseTypeDef,
    CreateUserResponseTypeDef,
    CreateVirtualMFADeviceResponseTypeDef,
    TagTypeDef,
    UpdateSAMLProviderResponseTypeDef,
    UploadServerCertificateResponseTypeDef,
    UploadSigningCertificateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "IAMServiceResource",
    "AccessKey",
    "AccessKeyPair",
    "AccountPasswordPolicy",
    "AccountSummary",
    "AssumeRolePolicy",
    "CurrentUser",
    "Group",
    "GroupPolicy",
    "InstanceProfile",
    "LoginProfile",
    "MfaDevice",
    "Policy",
    "PolicyVersion",
    "Role",
    "RolePolicy",
    "SamlProvider",
    "ServerCertificate",
    "SigningCertificate",
    "User",
    "UserPolicy",
    "VirtualMfaDevice",
    "ServiceResourceGroupsCollection",
    "ServiceResourceInstanceProfilesCollection",
    "ServiceResourcePoliciesCollection",
    "ServiceResourceRolesCollection",
    "ServiceResourceSamlProvidersCollection",
    "ServiceResourceServerCertificatesCollection",
    "ServiceResourceUsersCollection",
    "ServiceResourceVirtualMfaDevicesCollection",
    "CurrentUserAccessKeysCollection",
    "CurrentUserMfaDevicesCollection",
    "CurrentUserSigningCertificatesCollection",
    "GroupAttachedPoliciesCollection",
    "GroupPoliciesCollection",
    "GroupUsersCollection",
    "PolicyAttachedGroupsCollection",
    "PolicyAttachedRolesCollection",
    "PolicyAttachedUsersCollection",
    "PolicyVersionsCollection",
    "RoleAttachedPoliciesCollection",
    "RoleInstanceProfilesCollection",
    "RolePoliciesCollection",
    "UserAccessKeysCollection",
    "UserAttachedPoliciesCollection",
    "UserGroupsCollection",
    "UserMfaDevicesCollection",
    "UserPoliciesCollection",
    "UserSigningCertificatesCollection",
)


class IAMServiceResource(Boto3ServiceResource):
    """
    [IAM.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource)
    """

    groups: service_resource_scope.ServiceResourceGroupsCollection
    instance_profiles: service_resource_scope.ServiceResourceInstanceProfilesCollection
    policies: service_resource_scope.ServiceResourcePoliciesCollection
    roles: service_resource_scope.ServiceResourceRolesCollection
    saml_providers: service_resource_scope.ServiceResourceSamlProvidersCollection
    server_certificates: service_resource_scope.ServiceResourceServerCertificatesCollection
    users: service_resource_scope.ServiceResourceUsersCollection
    virtual_mfa_devices: service_resource_scope.ServiceResourceVirtualMfaDevicesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccessKey(self, user_name: str, id: str) -> service_resource_scope.AccessKey:
        """
        [ServiceResource.AccessKey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.AccessKey)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccessKeyPair(
        self, user_name: str, id: str, secret: str
    ) -> service_resource_scope.AccessKeyPair:
        """
        [ServiceResource.AccessKeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccountPasswordPolicy(
        self, *args: Any, **kwargs: Any
    ) -> service_resource_scope.AccountPasswordPolicy:
        """
        [ServiceResource.AccountPasswordPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccountSummary(self, *args: Any, **kwargs: Any) -> service_resource_scope.AccountSummary:
        """
        [ServiceResource.AccountSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.AccountSummary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AssumeRolePolicy(self, role_name: str) -> service_resource_scope.AssumeRolePolicy:
        """
        [ServiceResource.AssumeRolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def CurrentUser(self, *args: Any, **kwargs: Any) -> service_resource_scope.CurrentUser:
        """
        [ServiceResource.CurrentUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.CurrentUser)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Group(self, name: str) -> service_resource_scope.Group:
        """
        [ServiceResource.Group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.Group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def GroupPolicy(self, group_name: str, name: str) -> service_resource_scope.GroupPolicy:
        """
        [ServiceResource.GroupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def InstanceProfile(self, name: str) -> service_resource_scope.InstanceProfile:
        """
        [ServiceResource.InstanceProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def LoginProfile(self, user_name: str) -> service_resource_scope.LoginProfile:
        """
        [ServiceResource.LoginProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.LoginProfile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def MfaDevice(self, user_name: str, serial_number: str) -> service_resource_scope.MfaDevice:
        """
        [ServiceResource.MfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.MfaDevice)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Policy(self, policy_arn: str) -> service_resource_scope.Policy:
        """
        [ServiceResource.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.Policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def PolicyVersion(self, arn: str, version_id: str) -> service_resource_scope.PolicyVersion:
        """
        [ServiceResource.PolicyVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Role(self, name: str) -> service_resource_scope.Role:
        """
        [ServiceResource.Role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.Role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def RolePolicy(self, role_name: str, name: str) -> service_resource_scope.RolePolicy:
        """
        [ServiceResource.RolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.RolePolicy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def SamlProvider(self, arn: str) -> service_resource_scope.SamlProvider:
        """
        [ServiceResource.SamlProvider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.SamlProvider)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def ServerCertificate(self, name: str) -> service_resource_scope.ServerCertificate:
        """
        [ServiceResource.ServerCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def SigningCertificate(
        self, user_name: str, id: str
    ) -> service_resource_scope.SigningCertificate:
        """
        [ServiceResource.SigningCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def User(self, name: str) -> service_resource_scope.User:
        """
        [ServiceResource.User documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.User)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def UserPolicy(self, user_name: str, name: str) -> service_resource_scope.UserPolicy:
        """
        [ServiceResource.UserPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.UserPolicy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def VirtualMfaDevice(self, serial_number: str) -> service_resource_scope.VirtualMfaDevice:
        """
        [ServiceResource.VirtualMfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def change_password(self, OldPassword: str, NewPassword: str) -> None:
        """
        [ServiceResource.change_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.change_password)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_account_alias(self, AccountAlias: str) -> None:
        """
        [ServiceResource.create_account_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.create_account_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_account_password_policy(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> service_resource_scope.AccountPasswordPolicy:
        """
        [ServiceResource.create_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.create_account_password_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(self, GroupName: str, Path: str = None) -> CreateGroupResponseTypeDef:
        """
        [ServiceResource.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.create_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instance_profile(
        self, InstanceProfileName: str, Path: str = None
    ) -> CreateInstanceProfileResponseTypeDef:
        """
        [ServiceResource.create_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.create_instance_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy(
        self, PolicyName: str, PolicyDocument: str, Path: str = None, Description: str = None
    ) -> CreatePolicyResponseTypeDef:
        """
        [ServiceResource.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.create_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_role(
        self,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: str = None,
        Description: str = None,
        MaxSessionDuration: int = None,
        PermissionsBoundary: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateRoleResponseTypeDef:
        """
        [ServiceResource.create_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.create_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_saml_provider(
        self, SAMLMetadataDocument: str, Name: str
    ) -> CreateSAMLProviderResponseTypeDef:
        """
        [ServiceResource.create_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.create_saml_provider)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_server_certificate(
        self,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: str = None,
        CertificateChain: str = None,
    ) -> UploadServerCertificateResponseTypeDef:
        """
        [ServiceResource.create_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.create_server_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_signing_certificate(
        self, CertificateBody: str, UserName: str = None
    ) -> UploadSigningCertificateResponseTypeDef:
        """
        [ServiceResource.create_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.create_signing_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user(
        self,
        UserName: str,
        Path: str = None,
        PermissionsBoundary: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateUserResponseTypeDef:
        """
        [ServiceResource.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.create_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_virtual_mfa_device(
        self, VirtualMFADeviceName: str, Path: str = None
    ) -> CreateVirtualMFADeviceResponseTypeDef:
        """
        [ServiceResource.create_virtual_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.create_virtual_mfa_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.get_available_subresources)
        """


class AccessKey(Boto3ServiceResource):
    """
    [AccessKey documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.AccessKey)
    """

    access_key_id: str
    status: str
    create_date: datetime
    user_name: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [AccessKey.activate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccessKey.activate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [AccessKey.deactivate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccessKey.deactivate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [AccessKey.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccessKey.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [AccessKey.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccessKey.get_available_subresources)
        """


class AccessKeyPair(Boto3ServiceResource):
    """
    [AccessKeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)
    """

    access_key_id: str
    status: str
    secret_access_key: str
    create_date: datetime
    user_name: str
    id: str
    secret: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [AccessKeyPair.activate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccessKeyPair.activate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [AccessKeyPair.deactivate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccessKeyPair.deactivate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [AccessKeyPair.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccessKeyPair.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [AccessKeyPair.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccessKeyPair.get_available_subresources)
        """


class AccountPasswordPolicy(Boto3ServiceResource):
    """
    [AccountPasswordPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)
    """

    minimum_password_length: int
    require_symbols: bool
    require_numbers: bool
    require_uppercase_characters: bool
    require_lowercase_characters: bool
    allow_users_to_change_password: bool
    expire_passwords: bool
    max_password_age: int
    password_reuse_prevention: int
    hard_expiry: bool

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [AccountPasswordPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccountPasswordPolicy.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [AccountPasswordPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccountPasswordPolicy.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [AccountPasswordPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccountPasswordPolicy.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [AccountPasswordPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccountPasswordPolicy.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> None:
        """
        [AccountPasswordPolicy.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccountPasswordPolicy.update)
        """


class AccountSummary(Boto3ServiceResource):
    """
    [AccountSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.AccountSummary)
    """

    summary_map: Dict[str, Any]

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [AccountSummary.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccountSummary.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [AccountSummary.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccountSummary.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [AccountSummary.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AccountSummary.reload)
        """


class AssumeRolePolicy(Boto3ServiceResource):
    """
    [AssumeRolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)
    """

    role_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [AssumeRolePolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AssumeRolePolicy.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, PolicyDocument: str) -> None:
        """
        [AssumeRolePolicy.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.AssumeRolePolicy.update)
        """


class CurrentUser(Boto3ServiceResource):
    """
    [CurrentUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.CurrentUser)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    access_keys: service_resource_scope.CurrentUserAccessKeysCollection
    mfa_devices: service_resource_scope.CurrentUserMfaDevicesCollection
    signing_certificates: service_resource_scope.CurrentUserSigningCertificatesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [CurrentUser.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.CurrentUser.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [CurrentUser.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.CurrentUser.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [CurrentUser.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.CurrentUser.reload)
        """


class Group(Boto3ServiceResource):
    """
    [Group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.Group)
    """

    path: str
    group_name: str
    group_id: str
    arn: str
    create_date: datetime
    name: str
    attached_policies: service_resource_scope.GroupAttachedPoliciesCollection
    policies: service_resource_scope.GroupPoliciesCollection
    users: service_resource_scope.GroupUsersCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_user(self, UserName: str) -> None:
        """
        [Group.add_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.add_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(self, PolicyArn: str) -> None:
        """
        [Group.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.attach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create(self, Path: str = None) -> CreateGroupResponseTypeDef:
        """
        [Group.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.create)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy(
        self, PolicyName: str, PolicyDocument: str
    ) -> service_resource_scope.GroupPolicy:
        """
        [Group.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.create_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [Group.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(self, PolicyArn: str) -> None:
        """
        [Group.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.detach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Group.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Group.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Group.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_user(self, UserName: str) -> None:
        """
        [Group.remove_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.remove_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, NewPath: str = None, NewGroupName: str = None) -> service_resource_scope.Group:
        """
        [Group.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.update)
        """


class GroupPolicy(Boto3ServiceResource):
    """
    [GroupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)
    """

    policy_name: str
    policy_document: str
    group_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [GroupPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.GroupPolicy.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [GroupPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.GroupPolicy.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [GroupPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.GroupPolicy.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, PolicyDocument: str) -> None:
        """
        [GroupPolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.GroupPolicy.put)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [GroupPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.GroupPolicy.reload)
        """


class InstanceProfile(Boto3ServiceResource):
    """
    [InstanceProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)
    """

    path: str
    instance_profile_name: str
    instance_profile_id: str
    arn: str
    create_date: datetime
    roles_attribute: List[Any]
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_role(self, RoleName: str) -> None:
        """
        [InstanceProfile.add_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.InstanceProfile.add_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [InstanceProfile.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.InstanceProfile.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [InstanceProfile.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.InstanceProfile.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [InstanceProfile.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.InstanceProfile.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [InstanceProfile.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.InstanceProfile.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_role(self, RoleName: str) -> None:
        """
        [InstanceProfile.remove_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.InstanceProfile.remove_role)
        """


class LoginProfile(Boto3ServiceResource):
    """
    [LoginProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.LoginProfile)
    """

    create_date: datetime
    password_reset_required: bool
    user_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create(
        self, Password: str, PasswordResetRequired: bool = None
    ) -> CreateLoginProfileResponseTypeDef:
        """
        [LoginProfile.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.LoginProfile.create)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [LoginProfile.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.LoginProfile.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [LoginProfile.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.LoginProfile.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [LoginProfile.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.LoginProfile.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [LoginProfile.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.LoginProfile.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, Password: str = None, PasswordResetRequired: bool = None) -> None:
        """
        [LoginProfile.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.LoginProfile.update)
        """


class MfaDevice(Boto3ServiceResource):
    """
    [MfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.MfaDevice)
    """

    enable_date: datetime
    user_name: str
    serial_number: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        [MfaDevice.associate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.MfaDevice.associate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate(self) -> None:
        """
        [MfaDevice.disassociate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.MfaDevice.disassociate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [MfaDevice.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.MfaDevice.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resync(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        [MfaDevice.resync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.MfaDevice.resync)
        """


class Policy(Boto3ServiceResource):
    """
    [Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.Policy)
    """

    policy_name: str
    policy_id: str
    path: str
    default_version_id: str
    attachment_count: int
    permissions_boundary_usage_count: int
    is_attachable: bool
    description: str
    create_date: datetime
    update_date: datetime
    arn: str
    attached_groups: service_resource_scope.PolicyAttachedGroupsCollection
    attached_roles: service_resource_scope.PolicyAttachedRolesCollection
    attached_users: service_resource_scope.PolicyAttachedUsersCollection
    versions: service_resource_scope.PolicyVersionsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_group(self, GroupName: str) -> None:
        """
        [Policy.attach_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.attach_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_role(self, RoleName: str) -> None:
        """
        [Policy.attach_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.attach_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_user(self, UserName: str) -> None:
        """
        [Policy.attach_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.attach_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_version(
        self, PolicyDocument: str, SetAsDefault: bool = None
    ) -> CreatePolicyVersionResponseTypeDef:
        """
        [Policy.create_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.create_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [Policy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_group(self, GroupName: str) -> None:
        """
        [Policy.detach_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.detach_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_role(self, RoleName: str) -> None:
        """
        [Policy.detach_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.detach_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_user(self, UserName: str) -> None:
        """
        [Policy.detach_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.detach_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Policy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Policy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Policy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.reload)
        """


class PolicyVersion(Boto3ServiceResource):
    """
    [PolicyVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)
    """

    document: str
    is_default_version: bool
    create_date: datetime
    arn: str
    version_id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [PolicyVersion.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.PolicyVersion.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [PolicyVersion.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.PolicyVersion.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [PolicyVersion.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.PolicyVersion.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [PolicyVersion.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.PolicyVersion.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_as_default(self) -> None:
        """
        [PolicyVersion.set_as_default documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.PolicyVersion.set_as_default)
        """


class Role(Boto3ServiceResource):
    """
    [Role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.Role)
    """

    path: str
    role_name: str
    role_id: str
    arn: str
    create_date: datetime
    assume_role_policy_document: str
    description: str
    max_session_duration: int
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    role_last_used: Dict[str, Any]
    name: str
    attached_policies: service_resource_scope.RoleAttachedPoliciesCollection
    instance_profiles: service_resource_scope.RoleInstanceProfilesCollection
    policies: service_resource_scope.RolePoliciesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(self, PolicyArn: str) -> None:
        """
        [Role.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Role.attach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [Role.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Role.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(self, PolicyArn: str) -> None:
        """
        [Role.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Role.detach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Role.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Role.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Role.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Role.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Role.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Role.reload)
        """


class RolePolicy(Boto3ServiceResource):
    """
    [RolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.RolePolicy)
    """

    policy_name: str
    policy_document: str
    role_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [RolePolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.RolePolicy.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [RolePolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.RolePolicy.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [RolePolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.RolePolicy.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, PolicyDocument: str) -> None:
        """
        [RolePolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.RolePolicy.put)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [RolePolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.RolePolicy.reload)
        """


class SamlProvider(Boto3ServiceResource):
    """
    [SamlProvider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.SamlProvider)
    """

    saml_metadata_document: str
    create_date: datetime
    valid_until: datetime
    arn: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [SamlProvider.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.SamlProvider.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [SamlProvider.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.SamlProvider.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [SamlProvider.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.SamlProvider.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [SamlProvider.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.SamlProvider.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, SAMLMetadataDocument: str) -> UpdateSAMLProviderResponseTypeDef:
        """
        [SamlProvider.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.SamlProvider.update)
        """


class ServerCertificate(Boto3ServiceResource):
    """
    [ServerCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)
    """

    server_certificate_metadata: Dict[str, Any]
    certificate_body: str
    certificate_chain: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [ServerCertificate.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServerCertificate.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServerCertificate.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServerCertificate.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [ServerCertificate.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServerCertificate.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [ServerCertificate.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServerCertificate.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(
        self, NewPath: str = None, NewServerCertificateName: str = None
    ) -> service_resource_scope.ServerCertificate:
        """
        [ServerCertificate.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServerCertificate.update)
        """


class SigningCertificate(Boto3ServiceResource):
    """
    [SigningCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)
    """

    certificate_id: str
    certificate_body: str
    status: str
    upload_date: datetime
    user_name: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [SigningCertificate.activate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.SigningCertificate.activate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate(self, Status: Literal["Active", "Inactive"]) -> None:
        """
        [SigningCertificate.deactivate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.SigningCertificate.deactivate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [SigningCertificate.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.SigningCertificate.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [SigningCertificate.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.SigningCertificate.get_available_subresources)
        """


class User(Boto3ServiceResource):
    """
    [User documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.User)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    name: str
    access_keys: service_resource_scope.UserAccessKeysCollection
    attached_policies: service_resource_scope.UserAttachedPoliciesCollection
    groups: service_resource_scope.UserGroupsCollection
    mfa_devices: service_resource_scope.UserMfaDevicesCollection
    policies: service_resource_scope.UserPoliciesCollection
    signing_certificates: service_resource_scope.UserSigningCertificatesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_group(self, GroupName: str) -> None:
        """
        [User.add_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.add_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(self, PolicyArn: str) -> None:
        """
        [User.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.attach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create(
        self, Path: str = None, PermissionsBoundary: str = None, Tags: List[TagTypeDef] = None
    ) -> CreateUserResponseTypeDef:
        """
        [User.create documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.create)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_access_key_pair(self) -> CreateAccessKeyResponseTypeDef:
        """
        [User.create_access_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.create_access_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_login_profile(
        self, Password: str, PasswordResetRequired: bool = None
    ) -> CreateLoginProfileResponseTypeDef:
        """
        [User.create_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.create_login_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy(
        self, PolicyName: str, PolicyDocument: str
    ) -> service_resource_scope.UserPolicy:
        """
        [User.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.create_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [User.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(self, PolicyArn: str) -> None:
        """
        [User.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.detach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_mfa(
        self, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str
    ) -> service_resource_scope.MfaDevice:
        """
        [User.enable_mfa documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.enable_mfa)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [User.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [User.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [User.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_group(self, GroupName: str) -> None:
        """
        [User.remove_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.remove_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, NewPath: str = None, NewUserName: str = None) -> service_resource_scope.User:
        """
        [User.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.update)
        """


class UserPolicy(Boto3ServiceResource):
    """
    [UserPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.UserPolicy)
    """

    policy_name: str
    policy_document: str
    user_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [UserPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.UserPolicy.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [UserPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.UserPolicy.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [UserPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.UserPolicy.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, PolicyDocument: str) -> None:
        """
        [UserPolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.UserPolicy.put)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [UserPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.UserPolicy.reload)
        """


class VirtualMfaDevice(Boto3ServiceResource):
    """
    [VirtualMfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)
    """

    base32_string_seed: bytes
    qr_code_png: bytes
    user_attribute: Dict[str, Any]
    enable_date: datetime
    serial_number: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [VirtualMfaDevice.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.VirtualMfaDevice.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [VirtualMfaDevice.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.VirtualMfaDevice.get_available_subresources)
        """


class ServiceResourceGroupsCollection(ResourceCollection):
    """
    [ServiceResource.groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.groups)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Group]:
        pass


class ServiceResourceInstanceProfilesCollection(ResourceCollection):
    """
    [ServiceResource.instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.instance_profiles)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceInstanceProfilesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceInstanceProfilesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceInstanceProfilesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.ServiceResourceInstanceProfilesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.InstanceProfile]:
        pass


class ServiceResourcePoliciesCollection(ResourceCollection):
    """
    [ServiceResource.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.policies)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourcePoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourcePoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourcePoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourcePoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Policy]:
        pass


class ServiceResourceRolesCollection(ResourceCollection):
    """
    [ServiceResource.roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.roles)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceRolesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceRolesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceRolesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceRolesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Role]:
        pass


class ServiceResourceSamlProvidersCollection(ResourceCollection):
    """
    [ServiceResource.saml_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.saml_providers)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceSamlProvidersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceSamlProvidersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceSamlProvidersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceSamlProvidersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.SamlProvider]:
        pass


class ServiceResourceServerCertificatesCollection(ResourceCollection):
    """
    [ServiceResource.server_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.server_certificates)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceServerCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceServerCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(
        cls, count: int
    ) -> service_resource_scope.ServiceResourceServerCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.ServiceResourceServerCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.ServerCertificate]:
        pass


class ServiceResourceUsersCollection(ResourceCollection):
    """
    [ServiceResource.users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.users)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.User]:
        pass


class ServiceResourceVirtualMfaDevicesCollection(ResourceCollection):
    """
    [ServiceResource.virtual_mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceVirtualMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceVirtualMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceVirtualMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.ServiceResourceVirtualMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.VirtualMfaDevice]:
        pass


class CurrentUserAccessKeysCollection(ResourceCollection):
    """
    [CurrentUser.access_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.CurrentUser.access_keys)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.CurrentUserAccessKeysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.CurrentUserAccessKeysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.CurrentUserAccessKeysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.CurrentUserAccessKeysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.AccessKey]:
        pass


class CurrentUserMfaDevicesCollection(ResourceCollection):
    """
    [CurrentUser.mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.CurrentUser.mfa_devices)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.CurrentUserMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.CurrentUserMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.CurrentUserMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.CurrentUserMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.MfaDevice]:
        pass


class CurrentUserSigningCertificatesCollection(ResourceCollection):
    """
    [CurrentUser.signing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.CurrentUser.signing_certificates)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.CurrentUserSigningCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.CurrentUserSigningCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.CurrentUserSigningCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.CurrentUserSigningCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.SigningCertificate]:
        pass


class GroupAttachedPoliciesCollection(ResourceCollection):
    """
    [Group.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.attached_policies)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.GroupAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.GroupAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.GroupAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.GroupAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Policy]:
        pass


class GroupPoliciesCollection(ResourceCollection):
    """
    [Group.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.policies)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.GroupPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.GroupPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.GroupPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.GroupPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.GroupPolicy]:
        pass


class GroupUsersCollection(ResourceCollection):
    """
    [Group.users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Group.users)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.GroupUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.GroupUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.GroupUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.GroupUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.User]:
        pass


class PolicyAttachedGroupsCollection(ResourceCollection):
    """
    [Policy.attached_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.attached_groups)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.PolicyAttachedGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.PolicyAttachedGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.PolicyAttachedGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.PolicyAttachedGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Group]:
        pass


class PolicyAttachedRolesCollection(ResourceCollection):
    """
    [Policy.attached_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.attached_roles)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.PolicyAttachedRolesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.PolicyAttachedRolesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.PolicyAttachedRolesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.PolicyAttachedRolesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Role]:
        pass


class PolicyAttachedUsersCollection(ResourceCollection):
    """
    [Policy.attached_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.attached_users)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.PolicyAttachedUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.PolicyAttachedUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.PolicyAttachedUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.PolicyAttachedUsersCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.User]:
        pass


class PolicyVersionsCollection(ResourceCollection):
    """
    [Policy.versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Policy.versions)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.PolicyVersionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.PolicyVersionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.PolicyVersionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.PolicyVersionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.PolicyVersion]:
        pass


class RoleAttachedPoliciesCollection(ResourceCollection):
    """
    [Role.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Role.attached_policies)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.RoleAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.RoleAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.RoleAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.RoleAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Policy]:
        pass


class RoleInstanceProfilesCollection(ResourceCollection):
    """
    [Role.instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Role.instance_profiles)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.RoleInstanceProfilesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.RoleInstanceProfilesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.RoleInstanceProfilesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.RoleInstanceProfilesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.InstanceProfile]:
        pass


class RolePoliciesCollection(ResourceCollection):
    """
    [Role.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.Role.policies)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.RolePoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.RolePoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.RolePoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.RolePoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.RolePolicy]:
        pass


class UserAccessKeysCollection(ResourceCollection):
    """
    [User.access_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.access_keys)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.UserAccessKeysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.UserAccessKeysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.UserAccessKeysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.UserAccessKeysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.AccessKey]:
        pass


class UserAttachedPoliciesCollection(ResourceCollection):
    """
    [User.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.attached_policies)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.UserAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.UserAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.UserAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.UserAttachedPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Policy]:
        pass


class UserGroupsCollection(ResourceCollection):
    """
    [User.groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.groups)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.UserGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.UserGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.UserGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.UserGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Group]:
        pass


class UserMfaDevicesCollection(ResourceCollection):
    """
    [User.mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.mfa_devices)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.UserMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.UserMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.UserMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.UserMfaDevicesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.MfaDevice]:
        pass


class UserPoliciesCollection(ResourceCollection):
    """
    [User.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.policies)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.UserPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.UserPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.UserPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.UserPoliciesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.UserPolicy]:
        pass


class UserSigningCertificatesCollection(ResourceCollection):
    """
    [User.signing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iam.html#IAM.User.signing_certificates)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.UserSigningCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.UserSigningCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.UserSigningCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.UserSigningCertificatesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.SigningCertificate]:
        pass
