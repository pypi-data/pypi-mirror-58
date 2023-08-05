"Main interface for iotevents-data service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_iotevents_data.client as client_scope
from mypy_boto3_iotevents_data.type_defs import (
    BatchPutMessageResponseTypeDef,
    BatchUpdateDetectorResponseTypeDef,
    DescribeDetectorResponseTypeDef,
    ListDetectorsResponseTypeDef,
    MessageTypeDef,
    UpdateDetectorRequestTypeDef,
)


__all__ = ("IoTEventsDataClient",)


class IoTEventsDataClient(BaseClient):
    """
    [IoTEventsData.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iotevents-data.html#IoTEventsData.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_put_message(self, messages: List[MessageTypeDef]) -> BatchPutMessageResponseTypeDef:
        """
        [Client.batch_put_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iotevents-data.html#IoTEventsData.Client.batch_put_message)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_update_detector(
        self, detectors: List[UpdateDetectorRequestTypeDef]
    ) -> BatchUpdateDetectorResponseTypeDef:
        """
        [Client.batch_update_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iotevents-data.html#IoTEventsData.Client.batch_update_detector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iotevents-data.html#IoTEventsData.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_detector(
        self, detectorModelName: str, keyValue: str = None
    ) -> DescribeDetectorResponseTypeDef:
        """
        [Client.describe_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iotevents-data.html#IoTEventsData.Client.describe_detector)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iotevents-data.html#IoTEventsData.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_detectors(
        self,
        detectorModelName: str,
        stateName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListDetectorsResponseTypeDef:
        """
        [Client.list_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iotevents-data.html#IoTEventsData.Client.list_detectors)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError
