"Main interface for machinelearning service Waiters"
from __future__ import annotations

import sys
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_machinelearning.type_defs import WaiterConfigTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BatchPredictionAvailableWaiter",
    "DataSourceAvailableWaiter",
    "EvaluationAvailableWaiter",
    "MLModelAvailableWaiter",
)


class BatchPredictionAvailableWaiter(Boto3Waiter):
    """
    [Waiter.BatchPredictionAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/machinelearning.html#MachineLearning.Waiter.BatchPredictionAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
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
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [BatchPredictionAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/machinelearning.html#MachineLearning.Waiter.BatchPredictionAvailable.wait)
        """


class DataSourceAvailableWaiter(Boto3Waiter):
    """
    [Waiter.DataSourceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/machinelearning.html#MachineLearning.Waiter.DataSourceAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
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
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DataSourceAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/machinelearning.html#MachineLearning.Waiter.DataSourceAvailable.wait)
        """


class EvaluationAvailableWaiter(Boto3Waiter):
    """
    [Waiter.EvaluationAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/machinelearning.html#MachineLearning.Waiter.EvaluationAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
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
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [EvaluationAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/machinelearning.html#MachineLearning.Waiter.EvaluationAvailable.wait)
        """


class MLModelAvailableWaiter(Boto3Waiter):
    """
    [Waiter.MLModelAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/machinelearning.html#MachineLearning.Waiter.MLModelAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
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
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [MLModelAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/machinelearning.html#MachineLearning.Waiter.MLModelAvailable.wait)
        """
