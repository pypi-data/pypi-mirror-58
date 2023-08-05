"Main interface for iot1click-devices service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_iot1click_devices.client as client_scope

# pylint: disable=import-self
import mypy_boto3_iot1click_devices.paginator as paginator_scope
from mypy_boto3_iot1click_devices.type_defs import (
    ClaimDevicesByClaimCodeResponseTypeDef,
    DescribeDeviceResponseTypeDef,
    DeviceMethodTypeDef,
    FinalizeDeviceClaimResponseTypeDef,
    GetDeviceMethodsResponseTypeDef,
    InitiateDeviceClaimResponseTypeDef,
    InvokeDeviceMethodResponseTypeDef,
    ListDeviceEventsResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    UnclaimDeviceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoT1ClickDevicesServiceClient",)


class IoT1ClickDevicesServiceClient(BaseClient):
    """
    [IoT1ClickDevicesService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def claim_devices_by_claim_code(self, ClaimCode: str) -> ClaimDevicesByClaimCodeResponseTypeDef:
        """
        [Client.claim_devices_by_claim_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.claim_devices_by_claim_code)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_device(self, DeviceId: str) -> DescribeDeviceResponseTypeDef:
        """
        [Client.describe_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.describe_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def finalize_device_claim(
        self, DeviceId: str, Tags: Dict[str, str] = None
    ) -> FinalizeDeviceClaimResponseTypeDef:
        """
        [Client.finalize_device_claim documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.finalize_device_claim)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device_methods(self, DeviceId: str) -> GetDeviceMethodsResponseTypeDef:
        """
        [Client.get_device_methods documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.get_device_methods)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_device_claim(self, DeviceId: str) -> InitiateDeviceClaimResponseTypeDef:
        """
        [Client.initiate_device_claim documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.initiate_device_claim)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invoke_device_method(
        self,
        DeviceId: str,
        DeviceMethod: DeviceMethodTypeDef = None,
        DeviceMethodParameters: str = None,
    ) -> InvokeDeviceMethodResponseTypeDef:
        """
        [Client.invoke_device_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.invoke_device_method)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_device_events(
        self,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListDeviceEventsResponseTypeDef:
        """
        [Client.list_device_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_device_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_devices(
        self, DeviceType: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListDevicesResponseTypeDef:
        """
        [Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_devices)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unclaim_device(self, DeviceId: str) -> UnclaimDeviceResponseTypeDef:
        """
        [Client.unclaim_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.unclaim_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_device_state(self, DeviceId: str, Enabled: bool = None) -> Dict[str, Any]:
        """
        [Client.update_device_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.update_device_state)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_device_events"]
    ) -> paginator_scope.ListDeviceEventsPaginator:
        """
        [Paginator.ListDeviceEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDeviceEvents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_devices"]
    ) -> paginator_scope.ListDevicesPaginator:
        """
        [Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDevices)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    PreconditionFailedException: Boto3ClientError
    RangeNotSatisfiableException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
