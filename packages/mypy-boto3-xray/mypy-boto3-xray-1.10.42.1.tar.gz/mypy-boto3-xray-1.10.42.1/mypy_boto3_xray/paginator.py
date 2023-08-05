"Main interface for xray service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_xray.type_defs import (
    BatchGetTracesResultTypeDef,
    GetGroupsResultTypeDef,
    GetSamplingRulesResultTypeDef,
    GetSamplingStatisticSummariesResultTypeDef,
    GetServiceGraphResultTypeDef,
    GetTimeSeriesServiceStatisticsResultTypeDef,
    GetTraceGraphResultTypeDef,
    GetTraceSummariesResultTypeDef,
    PaginatorConfigTypeDef,
    SamplingStrategyTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BatchGetTracesPaginator",
    "GetGroupsPaginator",
    "GetSamplingRulesPaginator",
    "GetSamplingStatisticSummariesPaginator",
    "GetServiceGraphPaginator",
    "GetTimeSeriesServiceStatisticsPaginator",
    "GetTraceGraphPaginator",
    "GetTraceSummariesPaginator",
)


class BatchGetTracesPaginator(Boto3Paginator):
    """
    [Paginator.BatchGetTraces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.BatchGetTraces)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, TraceIds: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[BatchGetTracesResultTypeDef, None, None]:
        """
        [BatchGetTraces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.BatchGetTraces.paginate)
        """


class GetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.GetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetGroupsResultTypeDef, None, None]:
        """
        [GetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetGroups.paginate)
        """


class GetSamplingRulesPaginator(Boto3Paginator):
    """
    [Paginator.GetSamplingRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetSamplingRules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetSamplingRulesResultTypeDef, None, None]:
        """
        [GetSamplingRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetSamplingRules.paginate)
        """


class GetSamplingStatisticSummariesPaginator(Boto3Paginator):
    """
    [Paginator.GetSamplingStatisticSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetSamplingStatisticSummaries)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetSamplingStatisticSummariesResultTypeDef, None, None]:
        """
        [GetSamplingStatisticSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetSamplingStatisticSummaries.paginate)
        """


class GetServiceGraphPaginator(Boto3Paginator):
    """
    [Paginator.GetServiceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetServiceGraph)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetServiceGraphResultTypeDef, None, None]:
        """
        [GetServiceGraph.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetServiceGraph.paginate)
        """


class GetTimeSeriesServiceStatisticsPaginator(Boto3Paginator):
    """
    [Paginator.GetTimeSeriesServiceStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetTimeSeriesServiceStatistics)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        EntitySelectorExpression: str = None,
        Period: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetTimeSeriesServiceStatisticsResultTypeDef, None, None]:
        """
        [GetTimeSeriesServiceStatistics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetTimeSeriesServiceStatistics.paginate)
        """


class GetTraceGraphPaginator(Boto3Paginator):
    """
    [Paginator.GetTraceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetTraceGraph)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, TraceIds: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetTraceGraphResultTypeDef, None, None]:
        """
        [GetTraceGraph.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetTraceGraph.paginate)
        """


class GetTraceSummariesPaginator(Boto3Paginator):
    """
    [Paginator.GetTraceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetTraceSummaries)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        TimeRangeType: Literal["TraceId", "Event"] = None,
        Sampling: bool = None,
        SamplingStrategy: SamplingStrategyTypeDef = None,
        FilterExpression: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetTraceSummariesResultTypeDef, None, None]:
        """
        [GetTraceSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/xray.html#XRay.Paginator.GetTraceSummaries.paginate)
        """
