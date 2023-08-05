"Main interface for resource-groups service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_resource_groups.type_defs import (
    GroupFilterTypeDef,
    ListGroupResourcesOutputTypeDef,
    ListGroupsOutputTypeDef,
    PaginatorConfigTypeDef,
    ResourceFilterTypeDef,
    ResourceQueryTypeDef,
    SearchResourcesOutputTypeDef,
)


__all__ = ("ListGroupResourcesPaginator", "ListGroupsPaginator", "SearchResourcesPaginator")


class ListGroupResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListGroupResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroupResources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GroupName: str,
        Filters: List[ResourceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListGroupResourcesOutputTypeDef, None, None]:
        """
        [ListGroupResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroupResources.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[GroupFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListGroupsOutputTypeDef, None, None]:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroups.paginate)
        """


class SearchResourcesPaginator(Boto3Paginator):
    """
    [Paginator.SearchResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resource-groups.html#ResourceGroups.Paginator.SearchResources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceQuery: ResourceQueryTypeDef, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[SearchResourcesOutputTypeDef, None, None]:
        """
        [SearchResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resource-groups.html#ResourceGroups.Paginator.SearchResources.paginate)
        """
