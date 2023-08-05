"Main interface for apigatewaymanagementapi service type defs"
from __future__ import annotations

from datetime import datetime
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


IdentityTypeDef = TypedDict("IdentityTypeDef", {"SourceIp": str, "UserAgent": str})

GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef",
    {"ConnectedAt": datetime, "Identity": IdentityTypeDef, "LastActiveAt": datetime},
    total=False,
)
