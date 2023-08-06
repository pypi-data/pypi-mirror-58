"""
Main interface for health service client paginators.

Usage::

    import boto3
    from mypy_boto3.health import (
        DescribeAffectedEntitiesPaginator,
        DescribeEventAggregatesPaginator,
        DescribeEventTypesPaginator,
        DescribeEventsPaginator,
    )

    client: HealthClient = boto3.client("health")

    describe_affected_entities_paginator: DescribeAffectedEntitiesPaginator = client.get_paginator("describe_affected_entities")
    describe_event_aggregates_paginator: DescribeEventAggregatesPaginator = client.get_paginator("describe_event_aggregates")
    describe_event_types_paginator: DescribeEventTypesPaginator = client.get_paginator("describe_event_types")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_health.type_defs import (
    DescribeAffectedEntitiesResponseTypeDef,
    DescribeEventAggregatesResponseTypeDef,
    DescribeEventTypesResponseTypeDef,
    DescribeEventsResponseTypeDef,
    EntityFilterTypeDef,
    EventFilterTypeDef,
    EventTypeFilterTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAffectedEntitiesPaginator",
    "DescribeEventAggregatesPaginator",
    "DescribeEventTypesPaginator",
    "DescribeEventsPaginator",
)


class DescribeAffectedEntitiesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAffectedEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.44/reference/services/health.html#Health.Paginator.DescribeAffectedEntities)
    """

    def paginate(
        self,
        filter: EntityFilterTypeDef,
        locale: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAffectedEntitiesResponseTypeDef, None, None]:
        """
        [DescribeAffectedEntities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.44/reference/services/health.html#Health.Paginator.DescribeAffectedEntities.paginate)
        """


class DescribeEventAggregatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventAggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.44/reference/services/health.html#Health.Paginator.DescribeEventAggregates)
    """

    def paginate(
        self,
        aggregateField: Literal["eventTypeCategory"],
        filter: EventFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventAggregatesResponseTypeDef, None, None]:
        """
        [DescribeEventAggregates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.44/reference/services/health.html#Health.Paginator.DescribeEventAggregates.paginate)
        """


class DescribeEventTypesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.44/reference/services/health.html#Health.Paginator.DescribeEventTypes)
    """

    def paginate(
        self,
        filter: EventTypeFilterTypeDef = None,
        locale: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventTypesResponseTypeDef, None, None]:
        """
        [DescribeEventTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.44/reference/services/health.html#Health.Paginator.DescribeEventTypes.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.44/reference/services/health.html#Health.Paginator.DescribeEvents)
    """

    def paginate(
        self,
        filter: EventFilterTypeDef = None,
        locale: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventsResponseTypeDef, None, None]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.44/reference/services/health.html#Health.Paginator.DescribeEvents.paginate)
        """
