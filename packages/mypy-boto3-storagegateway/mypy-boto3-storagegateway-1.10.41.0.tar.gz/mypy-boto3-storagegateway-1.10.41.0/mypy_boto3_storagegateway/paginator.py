"Main interface for storagegateway service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_storagegateway.type_defs import (
    DescribeTapeArchivesOutputTypeDef,
    DescribeTapeRecoveryPointsOutputTypeDef,
    DescribeTapesOutputTypeDef,
    DescribeVTLDevicesOutputTypeDef,
    ListFileSharesOutputTypeDef,
    ListGatewaysOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTapesOutputTypeDef,
    ListVolumesOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeTapeArchivesPaginator",
    "DescribeTapeRecoveryPointsPaginator",
    "DescribeTapesPaginator",
    "DescribeVTLDevicesPaginator",
    "ListFileSharesPaginator",
    "ListGatewaysPaginator",
    "ListTagsForResourcePaginator",
    "ListTapesPaginator",
    "ListVolumesPaginator",
)


class DescribeTapeArchivesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTapeArchives documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, TapeARNs: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeTapeArchivesOutputTypeDef, None, None]:
        """
        [DescribeTapeArchives.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives.paginate)
        """


class DescribeTapeRecoveryPointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTapeRecoveryPoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GatewayARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeTapeRecoveryPointsOutputTypeDef, None, None]:
        """
        [DescribeTapeRecoveryPoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints.paginate)
        """


class DescribeTapesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str,
        TapeARNs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTapesOutputTypeDef, None, None]:
        """
        [DescribeTapes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes.paginate)
        """


class DescribeVTLDevicesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVTLDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVTLDevicesOutputTypeDef, None, None]:
        """
        [DescribeVTLDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices.paginate)
        """


class ListFileSharesPaginator(Boto3Paginator):
    """
    [Paginator.ListFileShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GatewayARN: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFileSharesOutputTypeDef, None, None]:
        """
        [ListFileShares.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares.paginate)
        """


class ListGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.ListGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGatewaysOutputTypeDef, None, None]:
        """
        [ListGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsForResourceOutputTypeDef, None, None]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource.paginate)
        """


class ListTapesPaginator(Boto3Paginator):
    """
    [Paginator.ListTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, TapeARNs: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTapesOutputTypeDef, None, None]:
        """
        [ListTapes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes.paginate)
        """


class ListVolumesPaginator(Boto3Paginator):
    """
    [Paginator.ListVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GatewayARN: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListVolumesOutputTypeDef, None, None]:
        """
        [ListVolumes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes.paginate)
        """
