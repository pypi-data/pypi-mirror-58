"Main interface for personalize-events service type defs"
from __future__ import annotations

from datetime import datetime
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


_RequiredEventTypeDef = TypedDict(
    "_RequiredEventTypeDef", {"eventType": str, "properties": str, "sentAt": datetime}
)
_OptionalEventTypeDef = TypedDict("_OptionalEventTypeDef", {"eventId": str}, total=False)


class EventTypeDef(_RequiredEventTypeDef, _OptionalEventTypeDef):
    pass
