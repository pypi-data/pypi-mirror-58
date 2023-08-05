"""
Main interface for health service.

Usage::

    import boto3
    from mypy_boto3.health import (
        Client,
        DescribeAffectedEntitiesPaginator,
        DescribeEventAggregatesPaginator,
        DescribeEventTypesPaginator,
        DescribeEventsPaginator,
        HealthClient,
        )

    session = boto3.Session()

    client: HealthClient = boto3.client("health")
    session_client: HealthClient = session.client("health")

    describe_affected_entities_paginator: DescribeAffectedEntitiesPaginator = client.get_paginator("describe_affected_entities")
    describe_event_aggregates_paginator: DescribeEventAggregatesPaginator = client.get_paginator("describe_event_aggregates")
    describe_event_types_paginator: DescribeEventTypesPaginator = client.get_paginator("describe_event_types")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
"""
from mypy_boto3_health.client import HealthClient, HealthClient as Client
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
