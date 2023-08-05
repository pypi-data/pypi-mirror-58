"Main interface for cloudwatch service"
from mypy_boto3_cloudwatch.client import CloudWatchClient, CloudWatchClient as Client
from mypy_boto3_cloudwatch.paginator import (
    DescribeAlarmHistoryPaginator,
    DescribeAlarmsPaginator,
    GetMetricDataPaginator,
    ListDashboardsPaginator,
    ListMetricsPaginator,
)
from mypy_boto3_cloudwatch.service_resource import (
    CloudWatchServiceResource,
    CloudWatchServiceResource as ServiceResource,
)
from mypy_boto3_cloudwatch.waiter import AlarmExistsWaiter


__all__ = (
    "AlarmExistsWaiter",
    "Client",
    "CloudWatchClient",
    "CloudWatchServiceResource",
    "DescribeAlarmHistoryPaginator",
    "DescribeAlarmsPaginator",
    "GetMetricDataPaginator",
    "ListDashboardsPaginator",
    "ListMetricsPaginator",
    "ServiceResource",
)
