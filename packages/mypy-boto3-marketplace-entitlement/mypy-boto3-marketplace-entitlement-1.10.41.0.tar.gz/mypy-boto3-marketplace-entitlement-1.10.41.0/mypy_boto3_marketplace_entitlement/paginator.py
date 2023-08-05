"Main interface for marketplace-entitlement service Paginators"
from __future__ import annotations

import sys
from typing import Dict, Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_marketplace_entitlement.type_defs import (
    GetEntitlementsResultTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GetEntitlementsPaginator",)


class GetEntitlementsPaginator(Boto3Paginator):
    """
    [Paginator.GetEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProductCode: str,
        Filter: Dict[Literal["CUSTOMER_IDENTIFIER", "DIMENSION"], List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetEntitlementsResultTypeDef, None, None]:
        """
        [GetEntitlements.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements.paginate)
        """
