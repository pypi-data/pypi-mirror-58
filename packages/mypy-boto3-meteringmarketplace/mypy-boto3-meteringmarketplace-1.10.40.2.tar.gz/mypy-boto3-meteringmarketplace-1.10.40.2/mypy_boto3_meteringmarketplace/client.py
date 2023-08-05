"Main interface for meteringmarketplace service Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_meteringmarketplace.client as client_scope
from mypy_boto3_meteringmarketplace.type_defs import (
    BatchMeterUsageResultTypeDef,
    MeterUsageResultTypeDef,
    RegisterUsageResultTypeDef,
    ResolveCustomerResultTypeDef,
    UsageRecordTypeDef,
)


__all__ = ("MarketplaceMeteringClient",)


class MarketplaceMeteringClient(BaseClient):
    """
    [MarketplaceMetering.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/meteringmarketplace.html#MarketplaceMetering.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_meter_usage(
        self, UsageRecords: List[UsageRecordTypeDef], ProductCode: str
    ) -> BatchMeterUsageResultTypeDef:
        """
        [Client.batch_meter_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.batch_meter_usage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def meter_usage(
        self,
        ProductCode: str,
        Timestamp: datetime,
        UsageDimension: str,
        UsageQuantity: int = None,
        DryRun: bool = None,
    ) -> MeterUsageResultTypeDef:
        """
        [Client.meter_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.meter_usage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_usage(
        self, ProductCode: str, PublicKeyVersion: int, Nonce: str = None
    ) -> RegisterUsageResultTypeDef:
        """
        [Client.register_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.register_usage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resolve_customer(self, RegistrationToken: str) -> ResolveCustomerResultTypeDef:
        """
        [Client.resolve_customer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.resolve_customer)
        """


class Exceptions:
    ClientError: Boto3ClientError
    CustomerNotEntitledException: Boto3ClientError
    DisabledApiException: Boto3ClientError
    DuplicateRequestException: Boto3ClientError
    ExpiredTokenException: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidCustomerIdentifierException: Boto3ClientError
    InvalidEndpointRegionException: Boto3ClientError
    InvalidProductCodeException: Boto3ClientError
    InvalidPublicKeyVersionException: Boto3ClientError
    InvalidRegionException: Boto3ClientError
    InvalidTokenException: Boto3ClientError
    InvalidUsageDimensionException: Boto3ClientError
    PlatformNotSupportedException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    TimestampOutOfBoundsException: Boto3ClientError
