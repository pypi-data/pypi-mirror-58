"Main interface for fsx service"
from mypy_boto3_fsx.client import FSxClient, FSxClient as Client
from mypy_boto3_fsx.paginator import (
    DescribeBackupsPaginator,
    DescribeFileSystemsPaginator,
    ListTagsForResourcePaginator,
)


__all__ = (
    "Client",
    "DescribeBackupsPaginator",
    "DescribeFileSystemsPaginator",
    "FSxClient",
    "ListTagsForResourcePaginator",
)
