"Main interface for personalize-events service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_personalize_events.client as client_scope
from mypy_boto3_personalize_events.type_defs import EventTypeDef


__all__ = ("PersonalizeEventsClient",)


class PersonalizeEventsClient(BaseClient):
    """
    [PersonalizeEvents.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/personalize-events.html#PersonalizeEvents.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/personalize-events.html#PersonalizeEvents.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/personalize-events.html#PersonalizeEvents.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_events(
        self, trackingId: str, sessionId: str, eventList: List[EventTypeDef], userId: str = None
    ) -> None:
        """
        [Client.put_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/personalize-events.html#PersonalizeEvents.Client.put_events)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
