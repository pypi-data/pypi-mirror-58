"Main interface for ec2-instance-connect service type defs"
from __future__ import annotations

import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


SendSSHPublicKeyResponseTypeDef = TypedDict(
    "SendSSHPublicKeyResponseTypeDef", {"RequestId": str, "Success": bool}, total=False
)
