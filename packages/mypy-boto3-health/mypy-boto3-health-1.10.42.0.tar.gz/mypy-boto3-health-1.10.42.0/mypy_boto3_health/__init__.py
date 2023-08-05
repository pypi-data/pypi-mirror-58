"Main interface for health service"
from mypy_boto3_health.client import HealthClient as Client, HealthClient
from mypy_boto3_health.paginator import (
    DescribeAffectedEntitiesPaginator,
    DescribeEventAggregatesPaginator,
    DescribeEventTypesPaginator,
    DescribeEventsPaginator,
)


__all__ = (
    "Client",
    "DescribeAffectedEntitiesPaginator",
    "DescribeEventAggregatesPaginator",
    "DescribeEventTypesPaginator",
    "DescribeEventsPaginator",
    "HealthClient",
)
