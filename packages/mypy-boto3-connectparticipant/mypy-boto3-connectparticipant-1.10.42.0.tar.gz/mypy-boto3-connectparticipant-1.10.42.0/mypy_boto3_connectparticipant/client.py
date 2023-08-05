"Main interface for connectparticipant service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_connectparticipant.client as client_scope
from mypy_boto3_connectparticipant.type_defs import (
    CreateParticipantConnectionResponseTypeDef,
    GetTranscriptResponseTypeDef,
    SendEventResponseTypeDef,
    SendMessageResponseTypeDef,
    StartPositionTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ConnectParticipantClient",)


class ConnectParticipantClient(BaseClient):
    """
    [ConnectParticipant.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/connectparticipant.html#ConnectParticipant.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/connectparticipant.html#ConnectParticipant.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_participant_connection(
        self, Type: List[Literal["WEBSOCKET", "CONNECTION_CREDENTIALS"]], ParticipantToken: str
    ) -> CreateParticipantConnectionResponseTypeDef:
        """
        [Client.create_participant_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/connectparticipant.html#ConnectParticipant.Client.create_participant_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disconnect_participant(
        self, ConnectionToken: str, ClientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disconnect_participant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/connectparticipant.html#ConnectParticipant.Client.disconnect_participant)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/connectparticipant.html#ConnectParticipant.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_transcript(
        self,
        ConnectionToken: str,
        ContactId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        ScanDirection: Literal["FORWARD", "BACKWARD"] = None,
        SortOrder: Literal["DESCENDING", "ASCENDING"] = None,
        StartPosition: StartPositionTypeDef = None,
    ) -> GetTranscriptResponseTypeDef:
        """
        [Client.get_transcript documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/connectparticipant.html#ConnectParticipant.Client.get_transcript)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_event(
        self, ContentType: str, ConnectionToken: str, Content: str = None, ClientToken: str = None
    ) -> SendEventResponseTypeDef:
        """
        [Client.send_event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/connectparticipant.html#ConnectParticipant.Client.send_event)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_message(
        self, ContentType: str, Content: str, ConnectionToken: str, ClientToken: str = None
    ) -> SendMessageResponseTypeDef:
        """
        [Client.send_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/connectparticipant.html#ConnectParticipant.Client.send_message)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
