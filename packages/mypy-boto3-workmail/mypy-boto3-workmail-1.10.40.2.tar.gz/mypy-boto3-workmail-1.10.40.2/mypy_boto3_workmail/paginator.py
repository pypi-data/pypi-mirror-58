"Main interface for workmail service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_workmail.type_defs import (
    ListAliasesResponseTypeDef,
    ListGroupMembersResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListMailboxPermissionsResponseTypeDef,
    ListOrganizationsResponseTypeDef,
    ListResourceDelegatesResponseTypeDef,
    ListResourcesResponseTypeDef,
    ListUsersResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListAliasesPaginator",
    "ListGroupMembersPaginator",
    "ListGroupsPaginator",
    "ListMailboxPermissionsPaginator",
    "ListOrganizationsPaginator",
    "ListResourceDelegatesPaginator",
    "ListResourcesPaginator",
    "ListUsersPaginator",
)


class ListAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListAliases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, OrganizationId: str, EntityId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAliasesResponseTypeDef, None, None]:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListAliases.paginate)
        """


class ListGroupMembersPaginator(Boto3Paginator):
    """
    [Paginator.ListGroupMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, OrganizationId: str, GroupId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGroupMembersResponseTypeDef, None, None]:
        """
        [ListGroupMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, OrganizationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGroupsResponseTypeDef, None, None]:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListGroups.paginate)
        """


class ListMailboxPermissionsPaginator(Boto3Paginator):
    """
    [Paginator.ListMailboxPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, OrganizationId: str, EntityId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMailboxPermissionsResponseTypeDef, None, None]:
        """
        [ListMailboxPermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions.paginate)
        """


class ListOrganizationsPaginator(Boto3Paginator):
    """
    [Paginator.ListOrganizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListOrganizationsResponseTypeDef, None, None]:
        """
        [ListOrganizations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations.paginate)
        """


class ListResourceDelegatesPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceDelegates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, OrganizationId: str, ResourceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListResourceDelegatesResponseTypeDef, None, None]:
        """
        [ListResourceDelegates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates.paginate)
        """


class ListResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListResources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, OrganizationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListResourcesResponseTypeDef, None, None]:
        """
        [ListResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListResources.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListUsers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, OrganizationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListUsersResponseTypeDef, None, None]:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmail.html#WorkMail.Paginator.ListUsers.paginate)
        """
