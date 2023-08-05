"Main interface for fsx service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_fsx.type_defs import (
    DescribeBackupsResponseTypeDef,
    DescribeFileSystemsResponseTypeDef,
    FilterTypeDef,
    ListTagsForResourceResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeBackupsPaginator",
    "DescribeFileSystemsPaginator",
    "ListTagsForResourcePaginator",
)


class DescribeBackupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Paginator.DescribeBackups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        BackupIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeBackupsResponseTypeDef, None, None]:
        """
        [DescribeBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Paginator.DescribeBackups.paginate)
        """


class DescribeFileSystemsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, FileSystemIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeFileSystemsResponseTypeDef, None, None]:
        """
        [DescribeFileSystems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Paginator.ListTagsForResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceResponseTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Paginator.ListTagsForResource.paginate)
        """
