"Main interface for apigatewaymanagementapi service Client"
from __future__ import annotations

from typing import Any, Dict, IO, Union
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_apigatewaymanagementapi.client as client_scope
from mypy_boto3_apigatewaymanagementapi.type_defs import GetConnectionResponseTypeDef


__all__ = ("ApiGatewayManagementApiClient",)


class ApiGatewayManagementApiClient(BaseClient):
    """
    [ApiGatewayManagementApi.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_connection(self, ConnectionId: str) -> None:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.delete_connection)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connection(self, ConnectionId: str) -> GetConnectionResponseTypeDef:
        """
        [Client.get_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.get_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def post_to_connection(self, Data: Union[bytes, IO], ConnectionId: str) -> None:
        """
        [Client.post_to_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.post_to_connection)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    GoneException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    PayloadTooLargeException: Boto3ClientError
