"Main interface for fsx service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ActiveDirectoryBackupAttributesTypeDef = TypedDict(
    "ActiveDirectoryBackupAttributesTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str},
    total=False,
)

BackupFailureDetailsTypeDef = TypedDict(
    "BackupFailureDetailsTypeDef", {"Message": str}, total=False
)

FileSystemFailureDetailsTypeDef = TypedDict(
    "FileSystemFailureDetailsTypeDef", {"Message": str}, total=False
)

DataRepositoryConfigurationTypeDef = TypedDict(
    "DataRepositoryConfigurationTypeDef",
    {"ImportPath": str, "ExportPath": str, "ImportedFileChunkSize": int},
    total=False,
)

LustreFileSystemConfigurationTypeDef = TypedDict(
    "LustreFileSystemConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": DataRepositoryConfigurationTypeDef,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

SelfManagedActiveDirectoryAttributesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryAttributesTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

WindowsFileSystemConfigurationTypeDef = TypedDict(
    "WindowsFileSystemConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": SelfManagedActiveDirectoryAttributesTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[Literal["PATCHING", "BACKING_UP"]],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)

FileSystemTypeDef = TypedDict(
    "FileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS", "LUSTRE"],
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "FailureDetails": FileSystemFailureDetailsTypeDef,
        "StorageCapacity": int,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[TagTypeDef],
        "WindowsConfiguration": WindowsFileSystemConfigurationTypeDef,
        "LustreConfiguration": LustreFileSystemConfigurationTypeDef,
    },
    total=False,
)

_RequiredBackupTypeDef = TypedDict(
    "_RequiredBackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": Literal["AVAILABLE", "CREATING", "DELETED", "FAILED"],
        "Type": Literal["AUTOMATIC", "USER_INITIATED"],
        "CreationTime": datetime,
        "FileSystem": FileSystemTypeDef,
    },
)
_OptionalBackupTypeDef = TypedDict(
    "_OptionalBackupTypeDef",
    {
        "FailureDetails": BackupFailureDetailsTypeDef,
        "ProgressPercent": int,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List[TagTypeDef],
        "DirectoryInformation": ActiveDirectoryBackupAttributesTypeDef,
    },
    total=False,
)


class BackupTypeDef(_RequiredBackupTypeDef, _OptionalBackupTypeDef):
    pass


CreateBackupResponseTypeDef = TypedDict(
    "CreateBackupResponseTypeDef", {"Backup": BackupTypeDef}, total=False
)

CreateFileSystemFromBackupResponseTypeDef = TypedDict(
    "CreateFileSystemFromBackupResponseTypeDef", {"FileSystem": FileSystemTypeDef}, total=False
)

CreateFileSystemLustreConfigurationTypeDef = TypedDict(
    "CreateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
    },
    total=False,
)

CreateFileSystemResponseTypeDef = TypedDict(
    "CreateFileSystemResponseTypeDef", {"FileSystem": FileSystemTypeDef}, total=False
)

_RequiredSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_RequiredSelfManagedActiveDirectoryConfigurationTypeDef",
    {"DomainName": str, "UserName": str, "Password": str, "DnsIps": List[str]},
)
_OptionalSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_OptionalSelfManagedActiveDirectoryConfigurationTypeDef",
    {"OrganizationalUnitDistinguishedName": str, "FileSystemAdministratorsGroup": str},
    total=False,
)


class SelfManagedActiveDirectoryConfigurationTypeDef(
    _RequiredSelfManagedActiveDirectoryConfigurationTypeDef,
    _OptionalSelfManagedActiveDirectoryConfigurationTypeDef,
):
    pass


_RequiredCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_RequiredCreateFileSystemWindowsConfigurationTypeDef", {"ThroughputCapacity": int}
)
_OptionalCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_OptionalCreateFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": SelfManagedActiveDirectoryConfigurationTypeDef,
        "DeploymentType": Literal["MULTI_AZ_1", "SINGLE_AZ_1"],
        "PreferredSubnetId": str,
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
    },
    total=False,
)


class CreateFileSystemWindowsConfigurationTypeDef(
    _RequiredCreateFileSystemWindowsConfigurationTypeDef,
    _OptionalCreateFileSystemWindowsConfigurationTypeDef,
):
    pass


DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef",
    {"BackupId": str, "Lifecycle": Literal["AVAILABLE", "CREATING", "DELETED", "FAILED"]},
    total=False,
)

DeleteFileSystemWindowsResponseTypeDef = TypedDict(
    "DeleteFileSystemWindowsResponseTypeDef",
    {"FinalBackupId": str, "FinalBackupTags": List[TagTypeDef]},
    total=False,
)

DeleteFileSystemResponseTypeDef = TypedDict(
    "DeleteFileSystemResponseTypeDef",
    {
        "FileSystemId": str,
        "Lifecycle": Literal[
            "AVAILABLE", "CREATING", "FAILED", "DELETING", "MISCONFIGURED", "UPDATING"
        ],
        "WindowsResponse": DeleteFileSystemWindowsResponseTypeDef,
    },
    total=False,
)

DeleteFileSystemWindowsConfigurationTypeDef = TypedDict(
    "DeleteFileSystemWindowsConfigurationTypeDef",
    {"SkipFinalBackup": bool, "FinalBackupTags": List[TagTypeDef]},
    total=False,
)

DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {"Backups": List[BackupTypeDef], "NextToken": str},
    total=False,
)

DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {"FileSystems": List[FileSystemTypeDef], "NextToken": str},
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {"Name": Literal["file-system-id", "backup-type"], "Values": List[str]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List[TagTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateFileSystemLustreConfigurationTypeDef = TypedDict(
    "UpdateFileSystemLustreConfigurationTypeDef", {"WeeklyMaintenanceStartTime": str}, total=False
)

UpdateFileSystemResponseTypeDef = TypedDict(
    "UpdateFileSystemResponseTypeDef", {"FileSystem": FileSystemTypeDef}, total=False
)

SelfManagedActiveDirectoryConfigurationUpdatesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    {"UserName": str, "Password": str, "DnsIps": List[str]},
    total=False,
)

UpdateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "UpdateFileSystemWindowsConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "SelfManagedActiveDirectoryConfiguration": SelfManagedActiveDirectoryConfigurationUpdatesTypeDef,
    },
    total=False,
)
