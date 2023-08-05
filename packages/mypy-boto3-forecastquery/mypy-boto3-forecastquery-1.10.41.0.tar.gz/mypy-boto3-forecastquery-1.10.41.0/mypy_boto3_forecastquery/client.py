"Main interface for forecastquery service Client"
from __future__ import annotations

from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_forecastquery.client as client_scope
from mypy_boto3_forecastquery.type_defs import QueryForecastResponseTypeDef


__all__ = ("ForecastQueryServiceClient",)


class ForecastQueryServiceClient(BaseClient):
    """
    [ForecastQueryService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/forecastquery.html#ForecastQueryService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/forecastquery.html#ForecastQueryService.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/forecastquery.html#ForecastQueryService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def query_forecast(
        self,
        ForecastArn: str,
        Filters: Dict[str, str],
        StartDate: str = None,
        EndDate: str = None,
        NextToken: str = None,
    ) -> QueryForecastResponseTypeDef:
        """
        [Client.query_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/forecastquery.html#ForecastQueryService.Client.query_forecast)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
