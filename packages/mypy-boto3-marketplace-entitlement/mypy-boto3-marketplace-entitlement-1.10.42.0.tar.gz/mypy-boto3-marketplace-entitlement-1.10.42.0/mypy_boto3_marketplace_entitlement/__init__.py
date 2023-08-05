"Main interface for marketplace-entitlement service"
from mypy_boto3_marketplace_entitlement.client import (
    MarketplaceEntitlementServiceClient,
    MarketplaceEntitlementServiceClient as Client,
)
from mypy_boto3_marketplace_entitlement.paginator import GetEntitlementsPaginator


__all__ = ("Client", "GetEntitlementsPaginator", "MarketplaceEntitlementServiceClient")
