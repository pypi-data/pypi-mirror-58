"Main interface for pi service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_pi.client as client_scope
from mypy_boto3_pi.type_defs import (
    DescribeDimensionKeysResponseTypeDef,
    DimensionGroupTypeDef,
    GetResourceMetricsResponseTypeDef,
    MetricQueryTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PIClient",)


class PIClient(BaseClient):
    """
    [PI.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/pi.html#PI.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/pi.html#PI.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dimension_keys(
        self,
        ServiceType: Literal["RDS"],
        Identifier: str,
        StartTime: datetime,
        EndTime: datetime,
        Metric: str,
        GroupBy: DimensionGroupTypeDef,
        PeriodInSeconds: int = None,
        PartitionBy: DimensionGroupTypeDef = None,
        Filter: Dict[str, str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeDimensionKeysResponseTypeDef:
        """
        [Client.describe_dimension_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/pi.html#PI.Client.describe_dimension_keys)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/pi.html#PI.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_metrics(
        self,
        ServiceType: Literal["RDS"],
        Identifier: str,
        MetricQueries: List[MetricQueryTypeDef],
        StartTime: datetime,
        EndTime: datetime,
        PeriodInSeconds: int = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetResourceMetricsResponseTypeDef:
        """
        [Client.get_resource_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/pi.html#PI.Client.get_resource_metrics)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServiceError: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
