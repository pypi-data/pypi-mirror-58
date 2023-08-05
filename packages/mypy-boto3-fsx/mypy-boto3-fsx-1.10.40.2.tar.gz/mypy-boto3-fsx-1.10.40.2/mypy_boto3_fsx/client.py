"Main interface for fsx service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_fsx.client as client_scope

# pylint: disable=import-self
import mypy_boto3_fsx.paginator as paginator_scope
from mypy_boto3_fsx.type_defs import (
    CreateBackupResponseTypeDef,
    CreateFileSystemFromBackupResponseTypeDef,
    CreateFileSystemLustreConfigurationTypeDef,
    CreateFileSystemResponseTypeDef,
    CreateFileSystemWindowsConfigurationTypeDef,
    DeleteBackupResponseTypeDef,
    DeleteFileSystemResponseTypeDef,
    DeleteFileSystemWindowsConfigurationTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeFileSystemsResponseTypeDef,
    FilterTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagTypeDef,
    UpdateFileSystemLustreConfigurationTypeDef,
    UpdateFileSystemResponseTypeDef,
    UpdateFileSystemWindowsConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FSxClient",)


class FSxClient(BaseClient):
    """
    [FSx.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_backup(
        self, FileSystemId: str, ClientRequestToken: str = None, Tags: List[TagTypeDef] = None
    ) -> CreateBackupResponseTypeDef:
        """
        [Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.create_backup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_file_system(
        self,
        FileSystemType: Literal["WINDOWS", "LUSTRE"],
        StorageCapacity: int,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[str] = None,
        Tags: List[TagTypeDef] = None,
        KmsKeyId: str = None,
        WindowsConfiguration: CreateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: CreateFileSystemLustreConfigurationTypeDef = None,
    ) -> CreateFileSystemResponseTypeDef:
        """
        [Client.create_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.create_file_system)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_file_system_from_backup(
        self,
        BackupId: str,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[str] = None,
        Tags: List[TagTypeDef] = None,
        WindowsConfiguration: CreateFileSystemWindowsConfigurationTypeDef = None,
    ) -> CreateFileSystemFromBackupResponseTypeDef:
        """
        [Client.create_file_system_from_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.create_file_system_from_backup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_backup(
        self, BackupId: str, ClientRequestToken: str = None
    ) -> DeleteBackupResponseTypeDef:
        """
        [Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.delete_backup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: DeleteFileSystemWindowsConfigurationTypeDef = None,
    ) -> DeleteFileSystemResponseTypeDef:
        """
        [Client.delete_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.delete_file_system)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_backups(
        self,
        BackupIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeBackupsResponseTypeDef:
        """
        [Client.describe_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.describe_backups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_file_systems(
        self, FileSystemIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeFileSystemsResponseTypeDef:
        """
        [Client.describe_file_systems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.describe_file_systems)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceARN: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceARN: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_file_system(
        self,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: UpdateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: UpdateFileSystemLustreConfigurationTypeDef = None,
    ) -> UpdateFileSystemResponseTypeDef:
        """
        [Client.update_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Client.update_file_system)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> paginator_scope.DescribeBackupsPaginator:
        """
        [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Paginator.DescribeBackups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_file_systems"]
    ) -> paginator_scope.DescribeFileSystemsPaginator:
        """
        [Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/fsx.html#FSx.Paginator.ListTagsForResource)
        """


class Exceptions:
    ActiveDirectoryError: Boto3ClientError
    BackupInProgress: Boto3ClientError
    BackupNotFound: Boto3ClientError
    BackupRestoring: Boto3ClientError
    BadRequest: Boto3ClientError
    ClientError: Boto3ClientError
    FileSystemNotFound: Boto3ClientError
    IncompatibleParameterError: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidExportPath: Boto3ClientError
    InvalidImportPath: Boto3ClientError
    InvalidNetworkSettings: Boto3ClientError
    MissingFileSystemConfiguration: Boto3ClientError
    NotServiceResourceError: Boto3ClientError
    ResourceDoesNotSupportTagging: Boto3ClientError
    ResourceNotFound: Boto3ClientError
    ServiceLimitExceeded: Boto3ClientError
    UnsupportedOperation: Boto3ClientError
