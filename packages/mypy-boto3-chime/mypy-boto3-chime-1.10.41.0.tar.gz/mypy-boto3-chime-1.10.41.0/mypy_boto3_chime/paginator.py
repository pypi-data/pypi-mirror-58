"Main interface for chime service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_chime.type_defs import (
    ListAccountsResponseTypeDef,
    ListUsersResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListAccountsPaginator", "ListUsersPaginator")


class ListAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Paginator.ListAccounts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Name: str = None,
        UserEmail: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAccountsResponseTypeDef, None, None]:
        """
        [ListAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Paginator.ListAccounts.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Paginator.ListUsers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, AccountId: str, UserEmail: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListUsersResponseTypeDef, None, None]:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/chime.html#Chime.Paginator.ListUsers.paginate)
        """
