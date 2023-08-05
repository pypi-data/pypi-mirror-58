"Main interface for sso service"
from mypy_boto3_sso.client import SSOClient, SSOClient as Client
from mypy_boto3_sso.paginator import ListAccountRolesPaginator, ListAccountsPaginator


__all__ = ("Client", "ListAccountRolesPaginator", "ListAccountsPaginator", "SSOClient")
