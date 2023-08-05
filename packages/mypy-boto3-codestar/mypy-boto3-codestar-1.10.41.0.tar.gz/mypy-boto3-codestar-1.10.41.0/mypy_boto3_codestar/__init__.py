"Main interface for codestar service"
from mypy_boto3_codestar.client import CodeStarClient, CodeStarClient as Client
from mypy_boto3_codestar.paginator import (
    ListProjectsPaginator,
    ListResourcesPaginator,
    ListTeamMembersPaginator,
    ListUserProfilesPaginator,
)


__all__ = (
    "Client",
    "CodeStarClient",
    "ListProjectsPaginator",
    "ListResourcesPaginator",
    "ListTeamMembersPaginator",
    "ListUserProfilesPaginator",
)
