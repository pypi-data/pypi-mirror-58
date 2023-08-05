"Main interface for sso service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sso.type_defs import (
    ListAccountRolesResponseTypeDef,
    ListAccountsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListAccountRolesPaginator", "ListAccountsPaginator")


class ListAccountRolesPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sso.html#SSO.Paginator.ListAccountRoles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, accessToken: str, accountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAccountRolesResponseTypeDef, None, None]:
        """
        [ListAccountRoles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sso.html#SSO.Paginator.ListAccountRoles.paginate)
        """


class ListAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sso.html#SSO.Paginator.ListAccounts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, accessToken: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAccountsResponseTypeDef, None, None]:
        """
        [ListAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sso.html#SSO.Paginator.ListAccounts.paginate)
        """
