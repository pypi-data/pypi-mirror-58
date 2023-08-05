"Main interface for iot1click-devices service"
from mypy_boto3_iot1click_devices.client import (
    IoT1ClickDevicesServiceClient as Client,
    IoT1ClickDevicesServiceClient,
)
from mypy_boto3_iot1click_devices.paginator import ListDeviceEventsPaginator, ListDevicesPaginator


__all__ = (
    "Client",
    "IoT1ClickDevicesServiceClient",
    "ListDeviceEventsPaginator",
    "ListDevicesPaginator",
)
