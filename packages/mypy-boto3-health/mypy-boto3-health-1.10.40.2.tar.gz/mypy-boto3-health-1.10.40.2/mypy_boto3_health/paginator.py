"Main interface for health service Paginators"
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
    [Paginator.DescribeAffectedEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/health.html#Health.Paginator.DescribeAffectedEntities)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filter: EntityFilterTypeDef,
        locale: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAffectedEntitiesResponseTypeDef, None, None]:
        """
        [DescribeAffectedEntities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/health.html#Health.Paginator.DescribeAffectedEntities.paginate)
        """


class DescribeEventAggregatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventAggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/health.html#Health.Paginator.DescribeEventAggregates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        aggregateField: Literal["eventTypeCategory"],
        filter: EventFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventAggregatesResponseTypeDef, None, None]:
        """
        [DescribeEventAggregates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/health.html#Health.Paginator.DescribeEventAggregates.paginate)
        """


class DescribeEventTypesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/health.html#Health.Paginator.DescribeEventTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filter: EventTypeFilterTypeDef = None,
        locale: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventTypesResponseTypeDef, None, None]:
        """
        [DescribeEventTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/health.html#Health.Paginator.DescribeEventTypes.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/health.html#Health.Paginator.DescribeEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filter: EventFilterTypeDef = None,
        locale: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEventsResponseTypeDef, None, None]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/health.html#Health.Paginator.DescribeEvents.paginate)
        """
