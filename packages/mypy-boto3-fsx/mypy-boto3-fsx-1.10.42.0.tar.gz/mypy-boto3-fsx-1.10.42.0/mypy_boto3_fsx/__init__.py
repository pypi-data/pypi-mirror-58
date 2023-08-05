"Main interface for fsx service"
from mypy_boto3_fsx.client import FSxClient as Client, FSxClient
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
