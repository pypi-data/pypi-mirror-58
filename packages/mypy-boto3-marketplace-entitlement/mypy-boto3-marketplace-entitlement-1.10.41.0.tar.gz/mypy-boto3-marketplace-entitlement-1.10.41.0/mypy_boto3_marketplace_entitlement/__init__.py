"Main interface for marketplace-entitlement service"
from mypy_boto3_marketplace_entitlement.client import (
    MarketplaceEntitlementServiceClient as Client,
    MarketplaceEntitlementServiceClient,
)
from mypy_boto3_marketplace_entitlement.paginator import GetEntitlementsPaginator


__all__ = ("Client", "GetEntitlementsPaginator", "MarketplaceEntitlementServiceClient")
