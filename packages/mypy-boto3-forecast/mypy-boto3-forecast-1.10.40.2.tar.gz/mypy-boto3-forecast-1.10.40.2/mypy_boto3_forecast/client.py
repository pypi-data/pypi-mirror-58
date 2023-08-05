"Main interface for forecast service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_forecast.client as client_scope

# pylint: disable=import-self
import mypy_boto3_forecast.paginator as paginator_scope
from mypy_boto3_forecast.type_defs import (
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateForecastExportJobResponseTypeDef,
    CreateForecastResponseTypeDef,
    CreatePredictorResponseTypeDef,
    DataDestinationTypeDef,
    DataSourceTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeForecastExportJobResponseTypeDef,
    DescribeForecastResponseTypeDef,
    DescribePredictorResponseTypeDef,
    EncryptionConfigTypeDef,
    EvaluationParametersTypeDef,
    FeaturizationConfigTypeDef,
    FilterTypeDef,
    GetAccuracyMetricsResponseTypeDef,
    HyperParameterTuningJobConfigTypeDef,
    InputDataConfigTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListForecastExportJobsResponseTypeDef,
    ListForecastsResponseTypeDef,
    ListPredictorsResponseTypeDef,
    SchemaTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ForecastServiceClient",)


class ForecastServiceClient(BaseClient):
    """
    [ForecastService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dataset(
        self,
        DatasetName: str,
        Domain: Literal[
            "RETAIL",
            "CUSTOM",
            "INVENTORY_PLANNING",
            "EC2_CAPACITY",
            "WORK_FORCE",
            "WEB_TRAFFIC",
            "METRICS",
        ],
        DatasetType: Literal["TARGET_TIME_SERIES", "RELATED_TIME_SERIES", "ITEM_METADATA"],
        Schema: SchemaTypeDef,
        DataFrequency: str = None,
        EncryptionConfig: EncryptionConfigTypeDef = None,
    ) -> CreateDatasetResponseTypeDef:
        """
        [Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.create_dataset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dataset_group(
        self,
        DatasetGroupName: str,
        Domain: Literal[
            "RETAIL",
            "CUSTOM",
            "INVENTORY_PLANNING",
            "EC2_CAPACITY",
            "WORK_FORCE",
            "WEB_TRAFFIC",
            "METRICS",
        ],
        DatasetArns: List[str] = None,
    ) -> CreateDatasetGroupResponseTypeDef:
        """
        [Client.create_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.create_dataset_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dataset_import_job(
        self,
        DatasetImportJobName: str,
        DatasetArn: str,
        DataSource: DataSourceTypeDef,
        TimestampFormat: str = None,
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        [Client.create_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.create_dataset_import_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_forecast(
        self, ForecastName: str, PredictorArn: str, ForecastTypes: List[str] = None
    ) -> CreateForecastResponseTypeDef:
        """
        [Client.create_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.create_forecast)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_forecast_export_job(
        self, ForecastExportJobName: str, ForecastArn: str, Destination: DataDestinationTypeDef
    ) -> CreateForecastExportJobResponseTypeDef:
        """
        [Client.create_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.create_forecast_export_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_predictor(
        self,
        PredictorName: str,
        ForecastHorizon: int,
        InputDataConfig: InputDataConfigTypeDef,
        FeaturizationConfig: FeaturizationConfigTypeDef,
        AlgorithmArn: str = None,
        PerformAutoML: bool = None,
        PerformHPO: bool = None,
        TrainingParameters: Dict[str, str] = None,
        EvaluationParameters: EvaluationParametersTypeDef = None,
        HPOConfig: HyperParameterTuningJobConfigTypeDef = None,
        EncryptionConfig: EncryptionConfigTypeDef = None,
    ) -> CreatePredictorResponseTypeDef:
        """
        [Client.create_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.create_predictor)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dataset(self, DatasetArn: str) -> None:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.delete_dataset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dataset_group(self, DatasetGroupArn: str) -> None:
        """
        [Client.delete_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.delete_dataset_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dataset_import_job(self, DatasetImportJobArn: str) -> None:
        """
        [Client.delete_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.delete_dataset_import_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_forecast(self, ForecastArn: str) -> None:
        """
        [Client.delete_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.delete_forecast)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_forecast_export_job(self, ForecastExportJobArn: str) -> None:
        """
        [Client.delete_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.delete_forecast_export_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_predictor(self, PredictorArn: str) -> None:
        """
        [Client.delete_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.delete_predictor)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dataset(self, DatasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.describe_dataset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dataset_group(self, DatasetGroupArn: str) -> DescribeDatasetGroupResponseTypeDef:
        """
        [Client.describe_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.describe_dataset_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dataset_import_job(
        self, DatasetImportJobArn: str
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        [Client.describe_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.describe_dataset_import_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_forecast(self, ForecastArn: str) -> DescribeForecastResponseTypeDef:
        """
        [Client.describe_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.describe_forecast)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_forecast_export_job(
        self, ForecastExportJobArn: str
    ) -> DescribeForecastExportJobResponseTypeDef:
        """
        [Client.describe_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.describe_forecast_export_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_predictor(self, PredictorArn: str) -> DescribePredictorResponseTypeDef:
        """
        [Client.describe_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.describe_predictor)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_accuracy_metrics(self, PredictorArn: str) -> GetAccuracyMetricsResponseTypeDef:
        """
        [Client.get_accuracy_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.get_accuracy_metrics)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dataset_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        [Client.list_dataset_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.list_dataset_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dataset_import_jobs(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        [Client.list_dataset_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.list_dataset_import_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_datasets(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.list_datasets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_forecast_export_jobs(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListForecastExportJobsResponseTypeDef:
        """
        [Client.list_forecast_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.list_forecast_export_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_forecasts(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListForecastsResponseTypeDef:
        """
        [Client.list_forecasts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.list_forecasts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_predictors(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListPredictorsResponseTypeDef:
        """
        [Client.list_predictors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.list_predictors)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_dataset_group(self, DatasetGroupArn: str, DatasetArns: List[str]) -> Dict[str, Any]:
        """
        [Client.update_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Client.update_dataset_group)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_dataset_groups"]
    ) -> paginator_scope.ListDatasetGroupsPaginator:
        """
        [Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> paginator_scope.ListDatasetImportJobsPaginator:
        """
        [Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_datasets"]
    ) -> paginator_scope.ListDatasetsPaginator:
        """
        [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Paginator.ListDatasets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_forecast_export_jobs"]
    ) -> paginator_scope.ListForecastExportJobsPaginator:
        """
        [Paginator.ListForecastExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_forecasts"]
    ) -> paginator_scope.ListForecastsPaginator:
        """
        [Paginator.ListForecasts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Paginator.ListForecasts)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_predictors"]
    ) -> paginator_scope.ListPredictorsPaginator:
        """
        [Paginator.ListPredictors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/forecast.html#ForecastService.Paginator.ListPredictors)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
