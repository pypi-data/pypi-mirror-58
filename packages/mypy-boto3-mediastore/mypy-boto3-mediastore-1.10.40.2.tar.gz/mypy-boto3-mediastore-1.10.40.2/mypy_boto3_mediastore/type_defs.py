"Main interface for mediastore service type defs"
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


_RequiredCorsRuleTypeDef = TypedDict(
    "_RequiredCorsRuleTypeDef", {"AllowedOrigins": List[str], "AllowedHeaders": List[str]}
)
_OptionalCorsRuleTypeDef = TypedDict(
    "_OptionalCorsRuleTypeDef",
    {
        "AllowedMethods": List[Literal["PUT", "GET", "DELETE", "HEAD"]],
        "MaxAgeSeconds": int,
        "ExposeHeaders": List[str],
    },
    total=False,
)


class CorsRuleTypeDef(_RequiredCorsRuleTypeDef, _OptionalCorsRuleTypeDef):
    pass


ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": Literal["ACTIVE", "CREATING", "DELETING"],
        "AccessLoggingEnabled": bool,
    },
    total=False,
)

CreateContainerOutputTypeDef = TypedDict(
    "CreateContainerOutputTypeDef", {"Container": ContainerTypeDef}
)

DescribeContainerOutputTypeDef = TypedDict(
    "DescribeContainerOutputTypeDef", {"Container": ContainerTypeDef}, total=False
)

GetContainerPolicyOutputTypeDef = TypedDict("GetContainerPolicyOutputTypeDef", {"Policy": str})

GetCorsPolicyOutputTypeDef = TypedDict(
    "GetCorsPolicyOutputTypeDef", {"CorsPolicy": List[CorsRuleTypeDef]}
)

GetLifecyclePolicyOutputTypeDef = TypedDict(
    "GetLifecyclePolicyOutputTypeDef", {"LifecyclePolicy": str}
)

_RequiredListContainersOutputTypeDef = TypedDict(
    "_RequiredListContainersOutputTypeDef", {"Containers": List[ContainerTypeDef]}
)
_OptionalListContainersOutputTypeDef = TypedDict(
    "_OptionalListContainersOutputTypeDef", {"NextToken": str}, total=False
)


class ListContainersOutputTypeDef(
    _RequiredListContainersOutputTypeDef, _OptionalListContainersOutputTypeDef
):
    pass


_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef", {"Tags": List[TagTypeDef]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
