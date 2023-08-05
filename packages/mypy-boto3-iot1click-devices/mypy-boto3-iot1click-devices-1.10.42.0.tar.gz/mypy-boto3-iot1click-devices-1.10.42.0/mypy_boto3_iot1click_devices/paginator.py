"Main interface for iot1click-devices service Paginators"
from __future__ import annotations

from datetime import datetime
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iot1click_devices.type_defs import (
    ListDeviceEventsResponseTypeDef,
    ListDevicesResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListDeviceEventsPaginator", "ListDevicesPaginator")


class ListDeviceEventsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeviceEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDeviceEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDeviceEventsResponseTypeDef, None, None]:
        """
        [ListDeviceEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDeviceEvents.paginate)
        """


class ListDevicesPaginator(Boto3Paginator):
    """
    [Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDevices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DeviceType: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDevicesResponseTypeDef, None, None]:
        """
        [ListDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDevices.paginate)
        """
