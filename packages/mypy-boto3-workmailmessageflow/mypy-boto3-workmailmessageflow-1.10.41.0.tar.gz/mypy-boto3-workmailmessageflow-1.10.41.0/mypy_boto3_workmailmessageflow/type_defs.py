"Main interface for workmailmessageflow service type defs"
from __future__ import annotations

import sys
from typing import IO, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


GetRawMessageContentResponseTypeDef = TypedDict(
    "GetRawMessageContentResponseTypeDef", {"messageContent": Union[bytes, IO]}
)
