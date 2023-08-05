"Main interface for workmailmessageflow service Client"
from __future__ import annotations

from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_workmailmessageflow.client as client_scope
from mypy_boto3_workmailmessageflow.type_defs import GetRawMessageContentResponseTypeDef


__all__ = ("WorkMailMessageFlowClient",)


class WorkMailMessageFlowClient(BaseClient):
    """
    [WorkMailMessageFlow.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmailmessageflow.html#WorkMailMessageFlow.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmailmessageflow.html#WorkMailMessageFlow.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmailmessageflow.html#WorkMailMessageFlow.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_raw_message_content(self, messageId: str) -> GetRawMessageContentResponseTypeDef:
        """
        [Client.get_raw_message_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workmailmessageflow.html#WorkMailMessageFlow.Client.get_raw_message_content)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
