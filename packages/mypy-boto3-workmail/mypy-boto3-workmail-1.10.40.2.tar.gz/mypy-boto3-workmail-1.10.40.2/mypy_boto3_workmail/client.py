"Main interface for workmail service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_workmail.client as client_scope

# pylint: disable=import-self
import mypy_boto3_workmail.paginator as paginator_scope
from mypy_boto3_workmail.type_defs import (
    BookingOptionsTypeDef,
    CreateGroupResponseTypeDef,
    CreateResourceResponseTypeDef,
    CreateUserResponseTypeDef,
    DescribeGroupResponseTypeDef,
    DescribeOrganizationResponseTypeDef,
    DescribeResourceResponseTypeDef,
    DescribeUserResponseTypeDef,
    GetMailboxDetailsResponseTypeDef,
    ListAliasesResponseTypeDef,
    ListGroupMembersResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListMailboxPermissionsResponseTypeDef,
    ListOrganizationsResponseTypeDef,
    ListResourceDelegatesResponseTypeDef,
    ListResourcesResponseTypeDef,
    ListUsersResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WorkMailClient",)


class WorkMailClient(BaseClient):
    """
    [WorkMail.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_delegate_to_resource(
        self, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_delegate_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.associate_delegate_to_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_member_to_group(
        self, OrganizationId: str, GroupId: str, MemberId: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_member_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.associate_member_to_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict[str, Any]:
        """
        [Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.create_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(self, OrganizationId: str, Name: str) -> CreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.create_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resource(
        self, OrganizationId: str, Name: str, Type: Literal["ROOM", "EQUIPMENT"]
    ) -> CreateResourceResponseTypeDef:
        """
        [Client.create_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.create_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user(
        self, OrganizationId: str, Name: str, DisplayName: str, Password: str
    ) -> CreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.create_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict[str, Any]:
        """
        [Client.delete_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.delete_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_group(self, OrganizationId: str, GroupId: str) -> Dict[str, Any]:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.delete_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_mailbox_permissions(
        self, OrganizationId: str, EntityId: str, GranteeId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_mailbox_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.delete_mailbox_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource(self, OrganizationId: str, ResourceId: str) -> Dict[str, Any]:
        """
        [Client.delete_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.delete_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user(self, OrganizationId: str, UserId: str) -> Dict[str, Any]:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.delete_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_from_work_mail(self, OrganizationId: str, EntityId: str) -> Dict[str, Any]:
        """
        [Client.deregister_from_work_mail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.deregister_from_work_mail)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_group(self, OrganizationId: str, GroupId: str) -> DescribeGroupResponseTypeDef:
        """
        [Client.describe_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.describe_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_organization(self, OrganizationId: str) -> DescribeOrganizationResponseTypeDef:
        """
        [Client.describe_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.describe_organization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_resource(
        self, OrganizationId: str, ResourceId: str
    ) -> DescribeResourceResponseTypeDef:
        """
        [Client.describe_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.describe_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user(self, OrganizationId: str, UserId: str) -> DescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.describe_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_delegate_from_resource(
        self, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_delegate_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.disassociate_delegate_from_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_member_from_group(
        self, OrganizationId: str, GroupId: str, MemberId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_member_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.disassociate_member_from_group)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_mailbox_details(
        self, OrganizationId: str, UserId: str
    ) -> GetMailboxDetailsResponseTypeDef:
        """
        [Client.get_mailbox_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.get_mailbox_details)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_aliases(
        self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAliasesResponseTypeDef:
        """
        [Client.list_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.list_aliases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_group_members(
        self, OrganizationId: str, GroupId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListGroupMembersResponseTypeDef:
        """
        [Client.list_group_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.list_group_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_groups(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.list_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_mailbox_permissions(
        self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMailboxPermissionsResponseTypeDef:
        """
        [Client.list_mailbox_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.list_mailbox_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_organizations(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListOrganizationsResponseTypeDef:
        """
        [Client.list_organizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.list_organizations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_delegates(
        self, OrganizationId: str, ResourceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListResourceDelegatesResponseTypeDef:
        """
        [Client.list_resource_delegates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.list_resource_delegates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resources(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListResourcesResponseTypeDef:
        """
        [Client.list_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.list_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_users(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.list_users)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_mailbox_permissions(
        self,
        OrganizationId: str,
        EntityId: str,
        GranteeId: str,
        PermissionValues: List[Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]],
    ) -> Dict[str, Any]:
        """
        [Client.put_mailbox_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.put_mailbox_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_to_work_mail(
        self, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        """
        [Client.register_to_work_mail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.register_to_work_mail)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_password(self, OrganizationId: str, UserId: str, Password: str) -> Dict[str, Any]:
        """
        [Client.reset_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.reset_password)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_mailbox_quota(
        self, OrganizationId: str, UserId: str, MailboxQuota: int
    ) -> Dict[str, Any]:
        """
        [Client.update_mailbox_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.update_mailbox_quota)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_primary_email_address(
        self, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        """
        [Client.update_primary_email_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.update_primary_email_address)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_resource(
        self,
        OrganizationId: str,
        ResourceId: str,
        Name: str = None,
        BookingOptions: BookingOptionsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Client.update_resource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_aliases"]
    ) -> paginator_scope.ListAliasesPaginator:
        """
        [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListAliases)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_group_members"]
    ) -> paginator_scope.ListGroupMembersPaginator:
        """
        [Paginator.ListGroupMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_groups"]
    ) -> paginator_scope.ListGroupsPaginator:
        """
        [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_mailbox_permissions"]
    ) -> paginator_scope.ListMailboxPermissionsPaginator:
        """
        [Paginator.ListMailboxPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_organizations"]
    ) -> paginator_scope.ListOrganizationsPaginator:
        """
        [Paginator.ListOrganizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_delegates"]
    ) -> paginator_scope.ListResourceDelegatesPaginator:
        """
        [Paginator.ListResourceDelegates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resources"]
    ) -> paginator_scope.ListResourcesPaginator:
        """
        [Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListResources)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_users"]
    ) -> paginator_scope.ListUsersPaginator:
        """
        [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListUsers)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DirectoryServiceAuthenticationFailedException: Boto3ClientError
    DirectoryUnavailableException: Boto3ClientError
    EmailAddressInUseException: Boto3ClientError
    EntityAlreadyRegisteredException: Boto3ClientError
    EntityNotFoundException: Boto3ClientError
    EntityStateException: Boto3ClientError
    InvalidConfigurationException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidPasswordException: Boto3ClientError
    MailDomainNotFoundException: Boto3ClientError
    MailDomainStateException: Boto3ClientError
    NameAvailabilityException: Boto3ClientError
    OrganizationNotFoundException: Boto3ClientError
    OrganizationStateException: Boto3ClientError
    ReservedNameException: Boto3ClientError
    UnsupportedOperationException: Boto3ClientError
