"Main interface for resource-groups service"
from mypy_boto3_resource_groups.client import ResourceGroupsClient as Client, ResourceGroupsClient
from mypy_boto3_resource_groups.paginator import (
    ListGroupResourcesPaginator,
    ListGroupsPaginator,
    SearchResourcesPaginator,
)


__all__ = (
    "Client",
    "ListGroupResourcesPaginator",
    "ListGroupsPaginator",
    "ResourceGroupsClient",
    "SearchResourcesPaginator",
)
