"Main interface for machinelearning service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_machinelearning.type_defs import (
    DescribeBatchPredictionsOutputTypeDef,
    DescribeDataSourcesOutputTypeDef,
    DescribeEvaluationsOutputTypeDef,
    DescribeMLModelsOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeBatchPredictionsPaginator",
    "DescribeDataSourcesPaginator",
    "DescribeEvaluationsPaginator",
    "DescribeMLModelsPaginator",
)


class DescribeBatchPredictionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBatchPredictions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeBatchPredictions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FilterVariable: Literal[
            "CreatedAt",
            "LastUpdatedAt",
            "Status",
            "Name",
            "IAMUser",
            "MLModelId",
            "DataSourceId",
            "DataURI",
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeBatchPredictionsOutputTypeDef, None, None]:
        """
        [DescribeBatchPredictions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeBatchPredictions.paginate)
        """


class DescribeDataSourcesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeDataSources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FilterVariable: Literal[
            "CreatedAt", "LastUpdatedAt", "Status", "Name", "DataLocationS3", "IAMUser"
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeDataSourcesOutputTypeDef, None, None]:
        """
        [DescribeDataSources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeDataSources.paginate)
        """


class DescribeEvaluationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvaluations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeEvaluations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FilterVariable: Literal[
            "CreatedAt",
            "LastUpdatedAt",
            "Status",
            "Name",
            "IAMUser",
            "MLModelId",
            "DataSourceId",
            "DataURI",
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEvaluationsOutputTypeDef, None, None]:
        """
        [DescribeEvaluations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeEvaluations.paginate)
        """


class DescribeMLModelsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMLModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeMLModels)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FilterVariable: Literal[
            "CreatedAt",
            "LastUpdatedAt",
            "Status",
            "Name",
            "IAMUser",
            "TrainingDataSourceId",
            "RealtimeEndpointStatus",
            "MLModelType",
            "Algorithm",
            "TrainingDataURI",
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMLModelsOutputTypeDef, None, None]:
        """
        [DescribeMLModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeMLModels.paginate)
        """
