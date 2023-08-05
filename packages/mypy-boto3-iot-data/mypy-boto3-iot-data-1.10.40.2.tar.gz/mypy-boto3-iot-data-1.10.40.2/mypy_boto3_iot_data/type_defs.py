"Main interface for iot-data service type defs"
from __future__ import annotations

import sys
from typing import IO, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


DeleteThingShadowResponseTypeDef = TypedDict(
    "DeleteThingShadowResponseTypeDef", {"payload": Union[bytes, IO]}
)

GetThingShadowResponseTypeDef = TypedDict(
    "GetThingShadowResponseTypeDef", {"payload": Union[bytes, IO]}, total=False
)

UpdateThingShadowResponseTypeDef = TypedDict(
    "UpdateThingShadowResponseTypeDef", {"payload": Union[bytes, IO]}, total=False
)
