"Main interface for chime service"
from mypy_boto3_chime.client import ChimeClient, ChimeClient as Client
from mypy_boto3_chime.paginator import ListAccountsPaginator, ListUsersPaginator


__all__ = ("ChimeClient", "Client", "ListAccountsPaginator", "ListUsersPaginator")
