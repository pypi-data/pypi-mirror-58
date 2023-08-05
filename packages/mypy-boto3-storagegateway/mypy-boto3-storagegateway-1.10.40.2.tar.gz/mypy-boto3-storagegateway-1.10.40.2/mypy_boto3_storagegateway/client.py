"Main interface for storagegateway service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_storagegateway.client as client_scope

# pylint: disable=import-self
import mypy_boto3_storagegateway.paginator as paginator_scope
from mypy_boto3_storagegateway.type_defs import (
    ActivateGatewayOutputTypeDef,
    AddCacheOutputTypeDef,
    AddTagsToResourceOutputTypeDef,
    AddUploadBufferOutputTypeDef,
    AddWorkingStorageOutputTypeDef,
    AssignTapePoolOutputTypeDef,
    AttachVolumeOutputTypeDef,
    CancelArchivalOutputTypeDef,
    CancelRetrievalOutputTypeDef,
    CreateCachediSCSIVolumeOutputTypeDef,
    CreateNFSFileShareOutputTypeDef,
    CreateSMBFileShareOutputTypeDef,
    CreateSnapshotFromVolumeRecoveryPointOutputTypeDef,
    CreateSnapshotOutputTypeDef,
    CreateStorediSCSIVolumeOutputTypeDef,
    CreateTapeWithBarcodeOutputTypeDef,
    CreateTapesOutputTypeDef,
    DeleteBandwidthRateLimitOutputTypeDef,
    DeleteChapCredentialsOutputTypeDef,
    DeleteFileShareOutputTypeDef,
    DeleteGatewayOutputTypeDef,
    DeleteSnapshotScheduleOutputTypeDef,
    DeleteTapeArchiveOutputTypeDef,
    DeleteTapeOutputTypeDef,
    DeleteVolumeOutputTypeDef,
    DescribeAvailabilityMonitorTestOutputTypeDef,
    DescribeBandwidthRateLimitOutputTypeDef,
    DescribeCacheOutputTypeDef,
    DescribeCachediSCSIVolumesOutputTypeDef,
    DescribeChapCredentialsOutputTypeDef,
    DescribeGatewayInformationOutputTypeDef,
    DescribeMaintenanceStartTimeOutputTypeDef,
    DescribeNFSFileSharesOutputTypeDef,
    DescribeSMBFileSharesOutputTypeDef,
    DescribeSMBSettingsOutputTypeDef,
    DescribeSnapshotScheduleOutputTypeDef,
    DescribeStorediSCSIVolumesOutputTypeDef,
    DescribeTapeArchivesOutputTypeDef,
    DescribeTapeRecoveryPointsOutputTypeDef,
    DescribeTapesOutputTypeDef,
    DescribeUploadBufferOutputTypeDef,
    DescribeVTLDevicesOutputTypeDef,
    DescribeWorkingStorageOutputTypeDef,
    DetachVolumeOutputTypeDef,
    DisableGatewayOutputTypeDef,
    JoinDomainOutputTypeDef,
    ListFileSharesOutputTypeDef,
    ListGatewaysOutputTypeDef,
    ListLocalDisksOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTapesOutputTypeDef,
    ListVolumeInitiatorsOutputTypeDef,
    ListVolumeRecoveryPointsOutputTypeDef,
    ListVolumesOutputTypeDef,
    NFSFileShareDefaultsTypeDef,
    NotifyWhenUploadedOutputTypeDef,
    RefreshCacheOutputTypeDef,
    RemoveTagsFromResourceOutputTypeDef,
    ResetCacheOutputTypeDef,
    RetrieveTapeArchiveOutputTypeDef,
    RetrieveTapeRecoveryPointOutputTypeDef,
    SetLocalConsolePasswordOutputTypeDef,
    SetSMBGuestPasswordOutputTypeDef,
    ShutdownGatewayOutputTypeDef,
    StartAvailabilityMonitorTestOutputTypeDef,
    StartGatewayOutputTypeDef,
    TagTypeDef,
    UpdateBandwidthRateLimitOutputTypeDef,
    UpdateChapCredentialsOutputTypeDef,
    UpdateGatewayInformationOutputTypeDef,
    UpdateGatewaySoftwareNowOutputTypeDef,
    UpdateMaintenanceStartTimeOutputTypeDef,
    UpdateNFSFileShareOutputTypeDef,
    UpdateSMBFileShareOutputTypeDef,
    UpdateSMBSecurityStrategyOutputTypeDef,
    UpdateSnapshotScheduleOutputTypeDef,
    UpdateVTLDeviceTypeOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("StorageGatewayClient",)


class StorageGatewayClient(BaseClient):
    """
    [StorageGateway.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate_gateway(
        self,
        ActivationKey: str,
        GatewayName: str,
        GatewayTimezone: str,
        GatewayRegion: str,
        GatewayType: str = None,
        TapeDriveType: str = None,
        MediumChangerType: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> ActivateGatewayOutputTypeDef:
        """
        [Client.activate_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.activate_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_cache(self, GatewayARN: str, DiskIds: List[str]) -> AddCacheOutputTypeDef:
        """
        [Client.add_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.add_cache)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_resource(
        self, ResourceARN: str, Tags: List[TagTypeDef]
    ) -> AddTagsToResourceOutputTypeDef:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.add_tags_to_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_upload_buffer(
        self, GatewayARN: str, DiskIds: List[str]
    ) -> AddUploadBufferOutputTypeDef:
        """
        [Client.add_upload_buffer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.add_upload_buffer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_working_storage(
        self, GatewayARN: str, DiskIds: List[str]
    ) -> AddWorkingStorageOutputTypeDef:
        """
        [Client.add_working_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.add_working_storage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assign_tape_pool(self, TapeARN: str, PoolId: str) -> AssignTapePoolOutputTypeDef:
        """
        [Client.assign_tape_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.assign_tape_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_volume(
        self,
        GatewayARN: str,
        VolumeARN: str,
        NetworkInterfaceId: str,
        TargetName: str = None,
        DiskId: str = None,
    ) -> AttachVolumeOutputTypeDef:
        """
        [Client.attach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.attach_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_archival(self, GatewayARN: str, TapeARN: str) -> CancelArchivalOutputTypeDef:
        """
        [Client.cancel_archival documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.cancel_archival)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_retrieval(self, GatewayARN: str, TapeARN: str) -> CancelRetrievalOutputTypeDef:
        """
        [Client.cancel_retrieval documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.cancel_retrieval)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cached_iscsi_volume(
        self,
        GatewayARN: str,
        VolumeSizeInBytes: int,
        TargetName: str,
        NetworkInterfaceId: str,
        ClientToken: str,
        SnapshotId: str = None,
        SourceVolumeARN: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateCachediSCSIVolumeOutputTypeDef:
        """
        [Client.create_cached_iscsi_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.create_cached_iscsi_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_nfs_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        NFSFileShareDefaults: NFSFileShareDefaultsTypeDef = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateNFSFileShareOutputTypeDef:
        """
        [Client.create_nfs_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.create_nfs_file_share)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_smb_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        SMBACLEnabled: bool = None,
        AdminUserList: List[str] = None,
        ValidUserList: List[str] = None,
        InvalidUserList: List[str] = None,
        Authentication: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateSMBFileShareOutputTypeDef:
        """
        [Client.create_smb_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.create_smb_file_share)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot(
        self, VolumeARN: str, SnapshotDescription: str, Tags: List[TagTypeDef] = None
    ) -> CreateSnapshotOutputTypeDef:
        """
        [Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot_from_volume_recovery_point(
        self, VolumeARN: str, SnapshotDescription: str, Tags: List[TagTypeDef] = None
    ) -> CreateSnapshotFromVolumeRecoveryPointOutputTypeDef:
        """
        [Client.create_snapshot_from_volume_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot_from_volume_recovery_point)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stored_iscsi_volume(
        self,
        GatewayARN: str,
        DiskId: str,
        PreserveExistingData: bool,
        TargetName: str,
        NetworkInterfaceId: str,
        SnapshotId: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateStorediSCSIVolumeOutputTypeDef:
        """
        [Client.create_stored_iscsi_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.create_stored_iscsi_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tape_with_barcode(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        TapeBarcode: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateTapeWithBarcodeOutputTypeDef:
        """
        [Client.create_tape_with_barcode documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.create_tape_with_barcode)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tapes(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        ClientToken: str,
        NumTapesToCreate: int,
        TapeBarcodePrefix: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateTapesOutputTypeDef:
        """
        [Client.create_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.create_tapes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bandwidth_rate_limit(
        self, GatewayARN: str, BandwidthType: str
    ) -> DeleteBandwidthRateLimitOutputTypeDef:
        """
        [Client.delete_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.delete_bandwidth_rate_limit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_chap_credentials(
        self, TargetARN: str, InitiatorName: str
    ) -> DeleteChapCredentialsOutputTypeDef:
        """
        [Client.delete_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.delete_chap_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_file_share(
        self, FileShareARN: str, ForceDelete: bool = None
    ) -> DeleteFileShareOutputTypeDef:
        """
        [Client.delete_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.delete_file_share)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_gateway(self, GatewayARN: str) -> DeleteGatewayOutputTypeDef:
        """
        [Client.delete_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.delete_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_snapshot_schedule(self, VolumeARN: str) -> DeleteSnapshotScheduleOutputTypeDef:
        """
        [Client.delete_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.delete_snapshot_schedule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tape(self, GatewayARN: str, TapeARN: str) -> DeleteTapeOutputTypeDef:
        """
        [Client.delete_tape documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.delete_tape)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tape_archive(self, TapeARN: str) -> DeleteTapeArchiveOutputTypeDef:
        """
        [Client.delete_tape_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.delete_tape_archive)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_volume(self, VolumeARN: str) -> DeleteVolumeOutputTypeDef:
        """
        [Client.delete_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.delete_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_availability_monitor_test(
        self, GatewayARN: str
    ) -> DescribeAvailabilityMonitorTestOutputTypeDef:
        """
        [Client.describe_availability_monitor_test documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_availability_monitor_test)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_bandwidth_rate_limit(
        self, GatewayARN: str
    ) -> DescribeBandwidthRateLimitOutputTypeDef:
        """
        [Client.describe_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_bandwidth_rate_limit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cache(self, GatewayARN: str) -> DescribeCacheOutputTypeDef:
        """
        [Client.describe_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_cache)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cached_iscsi_volumes(
        self, VolumeARNs: List[str]
    ) -> DescribeCachediSCSIVolumesOutputTypeDef:
        """
        [Client.describe_cached_iscsi_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_cached_iscsi_volumes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_chap_credentials(self, TargetARN: str) -> DescribeChapCredentialsOutputTypeDef:
        """
        [Client.describe_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_chap_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_gateway_information(
        self, GatewayARN: str
    ) -> DescribeGatewayInformationOutputTypeDef:
        """
        [Client.describe_gateway_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_gateway_information)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_maintenance_start_time(
        self, GatewayARN: str
    ) -> DescribeMaintenanceStartTimeOutputTypeDef:
        """
        [Client.describe_maintenance_start_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_maintenance_start_time)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_nfs_file_shares(
        self, FileShareARNList: List[str]
    ) -> DescribeNFSFileSharesOutputTypeDef:
        """
        [Client.describe_nfs_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_nfs_file_shares)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_smb_file_shares(
        self, FileShareARNList: List[str]
    ) -> DescribeSMBFileSharesOutputTypeDef:
        """
        [Client.describe_smb_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_file_shares)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_smb_settings(self, GatewayARN: str) -> DescribeSMBSettingsOutputTypeDef:
        """
        [Client.describe_smb_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_snapshot_schedule(self, VolumeARN: str) -> DescribeSnapshotScheduleOutputTypeDef:
        """
        [Client.describe_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_snapshot_schedule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stored_iscsi_volumes(
        self, VolumeARNs: List[str]
    ) -> DescribeStorediSCSIVolumesOutputTypeDef:
        """
        [Client.describe_stored_iscsi_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_stored_iscsi_volumes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tape_archives(
        self, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> DescribeTapeArchivesOutputTypeDef:
        """
        [Client.describe_tape_archives documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_archives)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tape_recovery_points(
        self, GatewayARN: str, Marker: str = None, Limit: int = None
    ) -> DescribeTapeRecoveryPointsOutputTypeDef:
        """
        [Client.describe_tape_recovery_points documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_recovery_points)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tapes(
        self, GatewayARN: str, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> DescribeTapesOutputTypeDef:
        """
        [Client.describe_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_tapes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_upload_buffer(self, GatewayARN: str) -> DescribeUploadBufferOutputTypeDef:
        """
        [Client.describe_upload_buffer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_upload_buffer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vtl_devices(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        Marker: str = None,
        Limit: int = None,
    ) -> DescribeVTLDevicesOutputTypeDef:
        """
        [Client.describe_vtl_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_vtl_devices)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_working_storage(self, GatewayARN: str) -> DescribeWorkingStorageOutputTypeDef:
        """
        [Client.describe_working_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.describe_working_storage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_volume(self, VolumeARN: str, ForceDetach: bool = None) -> DetachVolumeOutputTypeDef:
        """
        [Client.detach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.detach_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_gateway(self, GatewayARN: str) -> DisableGatewayOutputTypeDef:
        """
        [Client.disable_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.disable_gateway)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def join_domain(
        self,
        GatewayARN: str,
        DomainName: str,
        UserName: str,
        Password: str,
        OrganizationalUnit: str = None,
        DomainControllers: List[str] = None,
        TimeoutInSeconds: int = None,
    ) -> JoinDomainOutputTypeDef:
        """
        [Client.join_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.join_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_file_shares(
        self, GatewayARN: str = None, Limit: int = None, Marker: str = None
    ) -> ListFileSharesOutputTypeDef:
        """
        [Client.list_file_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.list_file_shares)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_gateways(self, Marker: str = None, Limit: int = None) -> ListGatewaysOutputTypeDef:
        """
        [Client.list_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.list_gateways)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_local_disks(self, GatewayARN: str) -> ListLocalDisksOutputTypeDef:
        """
        [Client.list_local_disks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.list_local_disks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceARN: str, Marker: str = None, Limit: int = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tapes(
        self, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ListTapesOutputTypeDef:
        """
        [Client.list_tapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.list_tapes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_volume_initiators(self, VolumeARN: str) -> ListVolumeInitiatorsOutputTypeDef:
        """
        [Client.list_volume_initiators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.list_volume_initiators)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_volume_recovery_points(self, GatewayARN: str) -> ListVolumeRecoveryPointsOutputTypeDef:
        """
        [Client.list_volume_recovery_points documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.list_volume_recovery_points)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_volumes(
        self, GatewayARN: str = None, Marker: str = None, Limit: int = None
    ) -> ListVolumesOutputTypeDef:
        """
        [Client.list_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.list_volumes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def notify_when_uploaded(self, FileShareARN: str) -> NotifyWhenUploadedOutputTypeDef:
        """
        [Client.notify_when_uploaded documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.notify_when_uploaded)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def refresh_cache(
        self, FileShareARN: str, FolderList: List[str] = None, Recursive: bool = None
    ) -> RefreshCacheOutputTypeDef:
        """
        [Client.refresh_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.refresh_cache)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_resource(
        self, ResourceARN: str, TagKeys: List[str]
    ) -> RemoveTagsFromResourceOutputTypeDef:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.remove_tags_from_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_cache(self, GatewayARN: str) -> ResetCacheOutputTypeDef:
        """
        [Client.reset_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.reset_cache)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def retrieve_tape_archive(
        self, TapeARN: str, GatewayARN: str
    ) -> RetrieveTapeArchiveOutputTypeDef:
        """
        [Client.retrieve_tape_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_archive)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def retrieve_tape_recovery_point(
        self, TapeARN: str, GatewayARN: str
    ) -> RetrieveTapeRecoveryPointOutputTypeDef:
        """
        [Client.retrieve_tape_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_recovery_point)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_local_console_password(
        self, GatewayARN: str, LocalConsolePassword: str
    ) -> SetLocalConsolePasswordOutputTypeDef:
        """
        [Client.set_local_console_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.set_local_console_password)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_smb_guest_password(
        self, GatewayARN: str, Password: str
    ) -> SetSMBGuestPasswordOutputTypeDef:
        """
        [Client.set_smb_guest_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.set_smb_guest_password)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def shutdown_gateway(self, GatewayARN: str) -> ShutdownGatewayOutputTypeDef:
        """
        [Client.shutdown_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.shutdown_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_availability_monitor_test(
        self, GatewayARN: str
    ) -> StartAvailabilityMonitorTestOutputTypeDef:
        """
        [Client.start_availability_monitor_test documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.start_availability_monitor_test)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_gateway(self, GatewayARN: str) -> StartGatewayOutputTypeDef:
        """
        [Client.start_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.start_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_bandwidth_rate_limit(
        self,
        GatewayARN: str,
        AverageUploadRateLimitInBitsPerSec: int = None,
        AverageDownloadRateLimitInBitsPerSec: int = None,
    ) -> UpdateBandwidthRateLimitOutputTypeDef:
        """
        [Client.update_bandwidth_rate_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.update_bandwidth_rate_limit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_chap_credentials(
        self,
        TargetARN: str,
        SecretToAuthenticateInitiator: str,
        InitiatorName: str,
        SecretToAuthenticateTarget: str = None,
    ) -> UpdateChapCredentialsOutputTypeDef:
        """
        [Client.update_chap_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.update_chap_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_gateway_information(
        self,
        GatewayARN: str,
        GatewayName: str = None,
        GatewayTimezone: str = None,
        CloudWatchLogGroupARN: str = None,
    ) -> UpdateGatewayInformationOutputTypeDef:
        """
        [Client.update_gateway_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_information)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_gateway_software_now(self, GatewayARN: str) -> UpdateGatewaySoftwareNowOutputTypeDef:
        """
        [Client.update_gateway_software_now documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_software_now)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_maintenance_start_time(
        self,
        GatewayARN: str,
        HourOfDay: int,
        MinuteOfHour: int,
        DayOfWeek: int = None,
        DayOfMonth: int = None,
    ) -> UpdateMaintenanceStartTimeOutputTypeDef:
        """
        [Client.update_maintenance_start_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.update_maintenance_start_time)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_nfs_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        NFSFileShareDefaults: NFSFileShareDefaultsTypeDef = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
    ) -> UpdateNFSFileShareOutputTypeDef:
        """
        [Client.update_nfs_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.update_nfs_file_share)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_smb_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        SMBACLEnabled: bool = None,
        AdminUserList: List[str] = None,
        ValidUserList: List[str] = None,
        InvalidUserList: List[str] = None,
    ) -> UpdateSMBFileShareOutputTypeDef:
        """
        [Client.update_smb_file_share documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.update_smb_file_share)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_smb_security_strategy(
        self,
        GatewayARN: str,
        SMBSecurityStrategy: Literal["ClientSpecified", "MandatorySigning", "MandatoryEncryption"],
    ) -> UpdateSMBSecurityStrategyOutputTypeDef:
        """
        [Client.update_smb_security_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.update_smb_security_strategy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_snapshot_schedule(
        self,
        VolumeARN: str,
        StartAt: int,
        RecurrenceInHours: int,
        Description: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> UpdateSnapshotScheduleOutputTypeDef:
        """
        [Client.update_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.update_snapshot_schedule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_vtl_device_type(
        self, VTLDeviceARN: str, DeviceType: str
    ) -> UpdateVTLDeviceTypeOutputTypeDef:
        """
        [Client.update_vtl_device_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Client.update_vtl_device_type)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_tape_archives"]
    ) -> paginator_scope.DescribeTapeArchivesPaginator:
        """
        [Paginator.DescribeTapeArchives documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_tape_recovery_points"]
    ) -> paginator_scope.DescribeTapeRecoveryPointsPaginator:
        """
        [Paginator.DescribeTapeRecoveryPoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_tapes"]
    ) -> paginator_scope.DescribeTapesPaginator:
        """
        [Paginator.DescribeTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_vtl_devices"]
    ) -> paginator_scope.DescribeVTLDevicesPaginator:
        """
        [Paginator.DescribeVTLDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_file_shares"]
    ) -> paginator_scope.ListFileSharesPaginator:
        """
        [Paginator.ListFileShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_gateways"]
    ) -> paginator_scope.ListGatewaysPaginator:
        """
        [Paginator.ListGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tapes"]
    ) -> paginator_scope.ListTapesPaginator:
        """
        [Paginator.ListTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_volumes"]
    ) -> paginator_scope.ListVolumesPaginator:
        """
        [Paginator.ListVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidGatewayRequestException: Boto3ClientError
    ServiceUnavailableError: Boto3ClientError
