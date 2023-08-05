"Main interface for marketplace-entitlement service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_marketplace_entitlement.client as client_scope

# pylint: disable=import-self
import mypy_boto3_marketplace_entitlement.paginator as paginator_scope
from mypy_boto3_marketplace_entitlement.type_defs import GetEntitlementsResultTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MarketplaceEntitlementServiceClient",)


class MarketplaceEntitlementServiceClient(BaseClient):
    """
    [MarketplaceEntitlementService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_entitlements(
        self,
        ProductCode: str,
        Filter: Dict[Literal["CUSTOMER_IDENTIFIER", "DIMENSION"], List[str]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetEntitlementsResultTypeDef:
        """
        [Client.get_entitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.get_entitlements)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_entitlements"]
    ) -> paginator_scope.GetEntitlementsPaginator:
        """
        [Paginator.GetEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    ThrottlingException: Boto3ClientError
