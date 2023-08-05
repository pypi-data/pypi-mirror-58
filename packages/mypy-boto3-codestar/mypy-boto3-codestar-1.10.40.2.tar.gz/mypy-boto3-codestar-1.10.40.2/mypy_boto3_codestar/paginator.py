"Main interface for codestar service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codestar.type_defs import (
    ListProjectsResultTypeDef,
    ListResourcesResultTypeDef,
    ListTeamMembersResultTypeDef,
    ListUserProfilesResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListProjectsPaginator",
    "ListResourcesPaginator",
    "ListTeamMembersPaginator",
    "ListUserProfilesPaginator",
)


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar.html#CodeStar.Paginator.ListProjects)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListProjectsResultTypeDef, None, None]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar.html#CodeStar.Paginator.ListProjects.paginate)
        """


class ListResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar.html#CodeStar.Paginator.ListResources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, projectId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListResourcesResultTypeDef, None, None]:
        """
        [ListResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar.html#CodeStar.Paginator.ListResources.paginate)
        """


class ListTeamMembersPaginator(Boto3Paginator):
    """
    [Paginator.ListTeamMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar.html#CodeStar.Paginator.ListTeamMembers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, projectId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTeamMembersResultTypeDef, None, None]:
        """
        [ListTeamMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar.html#CodeStar.Paginator.ListTeamMembers.paginate)
        """


class ListUserProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListUserProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar.html#CodeStar.Paginator.ListUserProfiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListUserProfilesResultTypeDef, None, None]:
        """
        [ListUserProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar.html#CodeStar.Paginator.ListUserProfiles.paginate)
        """
