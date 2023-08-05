"Main interface for iot-data service Client"
from __future__ import annotations

from typing import Any, Dict, IO, Union
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_iot_data.client as client_scope
from mypy_boto3_iot_data.type_defs import (
    DeleteThingShadowResponseTypeDef,
    GetThingShadowResponseTypeDef,
    UpdateThingShadowResponseTypeDef,
)


__all__ = ("IoTDataPlaneClient",)


class IoTDataPlaneClient(BaseClient):
    """
    [IoTDataPlane.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot-data.html#IoTDataPlane.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot-data.html#IoTDataPlane.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_thing_shadow(self, thingName: str) -> DeleteThingShadowResponseTypeDef:
        """
        [Client.delete_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot-data.html#IoTDataPlane.Client.delete_thing_shadow)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot-data.html#IoTDataPlane.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_thing_shadow(self, thingName: str) -> GetThingShadowResponseTypeDef:
        """
        [Client.get_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot-data.html#IoTDataPlane.Client.get_thing_shadow)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def publish(self, topic: str, qos: int = None, payload: Union[bytes, IO] = None) -> None:
        """
        [Client.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot-data.html#IoTDataPlane.Client.publish)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_thing_shadow(
        self, thingName: str, payload: Union[bytes, IO]
    ) -> UpdateThingShadowResponseTypeDef:
        """
        [Client.update_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot-data.html#IoTDataPlane.Client.update_thing_shadow)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    MethodNotAllowedException: Boto3ClientError
    RequestEntityTooLargeException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
    UnsupportedDocumentEncodingException: Boto3ClientError
