"Main interface for machinelearning service"
from mypy_boto3_machinelearning.client import MachineLearningClient as Client, MachineLearningClient
from mypy_boto3_machinelearning.paginator import (
    DescribeBatchPredictionsPaginator,
    DescribeDataSourcesPaginator,
    DescribeEvaluationsPaginator,
    DescribeMLModelsPaginator,
)
from mypy_boto3_machinelearning.waiter import (
    BatchPredictionAvailableWaiter,
    DataSourceAvailableWaiter,
    EvaluationAvailableWaiter,
    MLModelAvailableWaiter,
)


__all__ = (
    "BatchPredictionAvailableWaiter",
    "Client",
    "DataSourceAvailableWaiter",
    "DescribeBatchPredictionsPaginator",
    "DescribeDataSourcesPaginator",
    "DescribeEvaluationsPaginator",
    "DescribeMLModelsPaginator",
    "EvaluationAvailableWaiter",
    "MLModelAvailableWaiter",
    "MachineLearningClient",
)
