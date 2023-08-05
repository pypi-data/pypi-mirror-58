"Main interface for elastic-inference service type defs"
from __future__ import annotations

import sys
from typing import Dict

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef", {"tags": Dict[str, str]}, total=False
)
