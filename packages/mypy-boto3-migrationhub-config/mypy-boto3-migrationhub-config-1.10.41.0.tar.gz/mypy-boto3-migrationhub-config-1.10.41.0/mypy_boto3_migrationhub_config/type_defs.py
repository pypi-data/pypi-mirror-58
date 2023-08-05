"Main interface for migrationhub-config service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


_RequiredTargetTypeDef = TypedDict("_RequiredTargetTypeDef", {"Type": Literal["ACCOUNT"]})
_OptionalTargetTypeDef = TypedDict("_OptionalTargetTypeDef", {"Id": str}, total=False)


class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass


HomeRegionControlTypeDef = TypedDict(
    "HomeRegionControlTypeDef",
    {"ControlId": str, "HomeRegion": str, "Target": TargetTypeDef, "RequestedTime": datetime},
    total=False,
)

CreateHomeRegionControlResultTypeDef = TypedDict(
    "CreateHomeRegionControlResultTypeDef",
    {"HomeRegionControl": HomeRegionControlTypeDef},
    total=False,
)

DescribeHomeRegionControlsResultTypeDef = TypedDict(
    "DescribeHomeRegionControlsResultTypeDef",
    {"HomeRegionControls": List[HomeRegionControlTypeDef], "NextToken": str},
    total=False,
)

GetHomeRegionResultTypeDef = TypedDict(
    "GetHomeRegionResultTypeDef", {"HomeRegion": str}, total=False
)
