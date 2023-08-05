"Main interface for sso service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sso.client as client_scope

# pylint: disable=import-self
import mypy_boto3_sso.paginator as paginator_scope
from mypy_boto3_sso.type_defs import (
    GetRoleCredentialsResponseTypeDef,
    ListAccountRolesResponseTypeDef,
    ListAccountsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SSOClient",)


class SSOClient(BaseClient):
    """
    [SSO.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sso.html#SSO.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sso.html#SSO.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sso.html#SSO.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_role_credentials(
        self, roleName: str, accountId: str, accessToken: str
    ) -> GetRoleCredentialsResponseTypeDef:
        """
        [Client.get_role_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sso.html#SSO.Client.get_role_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_account_roles(
        self, accessToken: str, accountId: str, nextToken: str = None, maxResults: int = None
    ) -> ListAccountRolesResponseTypeDef:
        """
        [Client.list_account_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sso.html#SSO.Client.list_account_roles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_accounts(
        self, accessToken: str, nextToken: str = None, maxResults: int = None
    ) -> ListAccountsResponseTypeDef:
        """
        [Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sso.html#SSO.Client.list_accounts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def logout(self, accessToken: str) -> None:
        """
        [Client.logout documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sso.html#SSO.Client.logout)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_account_roles"]
    ) -> paginator_scope.ListAccountRolesPaginator:
        """
        [Paginator.ListAccountRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sso.html#SSO.Paginator.ListAccountRoles)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_accounts"]
    ) -> paginator_scope.ListAccountsPaginator:
        """
        [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sso.html#SSO.Paginator.ListAccounts)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
