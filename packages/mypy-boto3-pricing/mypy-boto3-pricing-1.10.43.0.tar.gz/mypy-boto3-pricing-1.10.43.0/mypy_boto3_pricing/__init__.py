"Main interface for pricing service"
from mypy_boto3_pricing.client import PricingClient as Client, PricingClient
from mypy_boto3_pricing.paginator import (
    DescribeServicesPaginator,
    GetAttributeValuesPaginator,
    GetProductsPaginator,
)


__all__ = (
    "Client",
    "DescribeServicesPaginator",
    "GetAttributeValuesPaginator",
    "GetProductsPaginator",
    "PricingClient",
)
