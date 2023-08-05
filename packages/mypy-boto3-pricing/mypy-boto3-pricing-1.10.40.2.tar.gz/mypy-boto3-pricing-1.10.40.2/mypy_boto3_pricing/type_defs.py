"Main interface for pricing service type defs"
from __future__ import annotations

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


ServiceTypeDef = TypedDict(
    "ServiceTypeDef", {"ServiceCode": str, "AttributeNames": List[str]}, total=False
)

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {"Services": List[ServiceTypeDef], "FormatVersion": str, "NextToken": str},
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef", {"Type": Literal["TERM_MATCH"], "Field": str, "Value": str}
)

AttributeValueTypeDef = TypedDict("AttributeValueTypeDef", {"Value": str}, total=False)

GetAttributeValuesResponseTypeDef = TypedDict(
    "GetAttributeValuesResponseTypeDef",
    {"AttributeValues": List[AttributeValueTypeDef], "NextToken": str},
    total=False,
)

GetProductsResponseTypeDef = TypedDict(
    "GetProductsResponseTypeDef",
    {"FormatVersion": str, "PriceList": List[str], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
