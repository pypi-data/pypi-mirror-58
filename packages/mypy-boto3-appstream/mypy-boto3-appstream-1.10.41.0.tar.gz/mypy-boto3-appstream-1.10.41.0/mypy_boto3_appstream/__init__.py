"Main interface for appstream service"
from mypy_boto3_appstream.client import AppStreamClient, AppStreamClient as Client
from mypy_boto3_appstream.paginator import (
    DescribeDirectoryConfigsPaginator,
    DescribeFleetsPaginator,
    DescribeImageBuildersPaginator,
    DescribeImagesPaginator,
    DescribeSessionsPaginator,
    DescribeStacksPaginator,
    DescribeUserStackAssociationsPaginator,
    DescribeUsersPaginator,
    ListAssociatedFleetsPaginator,
    ListAssociatedStacksPaginator,
)
from mypy_boto3_appstream.waiter import FleetStartedWaiter, FleetStoppedWaiter


__all__ = (
    "AppStreamClient",
    "Client",
    "DescribeDirectoryConfigsPaginator",
    "DescribeFleetsPaginator",
    "DescribeImageBuildersPaginator",
    "DescribeImagesPaginator",
    "DescribeSessionsPaginator",
    "DescribeStacksPaginator",
    "DescribeUserStackAssociationsPaginator",
    "DescribeUsersPaginator",
    "FleetStartedWaiter",
    "FleetStoppedWaiter",
    "ListAssociatedFleetsPaginator",
    "ListAssociatedStacksPaginator",
)
