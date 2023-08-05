"Main interface for health service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


AffectedEntityTypeDef = TypedDict(
    "AffectedEntityTypeDef",
    {
        "entityArn": str,
        "eventArn": str,
        "entityValue": str,
        "entityUrl": str,
        "awsAccountId": str,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"],
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeAffectedEntitiesResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesResponseTypeDef",
    {"entities": List[AffectedEntityTypeDef], "nextToken": str},
    total=False,
)

EntityAggregateTypeDef = TypedDict(
    "EntityAggregateTypeDef", {"eventArn": str, "count": int}, total=False
)

DescribeEntityAggregatesResponseTypeDef = TypedDict(
    "DescribeEntityAggregatesResponseTypeDef",
    {"entityAggregates": List[EntityAggregateTypeDef]},
    total=False,
)

EventAggregateTypeDef = TypedDict(
    "EventAggregateTypeDef", {"aggregateValue": str, "count": int}, total=False
)

DescribeEventAggregatesResponseTypeDef = TypedDict(
    "DescribeEventAggregatesResponseTypeDef",
    {"eventAggregates": List[EventAggregateTypeDef], "nextToken": str},
    total=False,
)

EventDetailsErrorItemTypeDef = TypedDict(
    "EventDetailsErrorItemTypeDef",
    {"eventArn": str, "errorName": str, "errorMessage": str},
    total=False,
)

EventDescriptionTypeDef = TypedDict(
    "EventDescriptionTypeDef", {"latestDescription": str}, total=False
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": Literal[
            "issue", "accountNotification", "scheduledChange", "investigation"
        ],
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": Literal["open", "closed", "upcoming"],
    },
    total=False,
)

EventDetailsTypeDef = TypedDict(
    "EventDetailsTypeDef",
    {
        "event": EventTypeDef,
        "eventDescription": EventDescriptionTypeDef,
        "eventMetadata": Dict[str, str],
    },
    total=False,
)

DescribeEventDetailsResponseTypeDef = TypedDict(
    "DescribeEventDetailsResponseTypeDef",
    {"successfulSet": List[EventDetailsTypeDef], "failedSet": List[EventDetailsErrorItemTypeDef]},
    total=False,
)

EventTypeTypeDef = TypedDict(
    "EventTypeTypeDef",
    {
        "service": str,
        "code": str,
        "category": Literal["issue", "accountNotification", "scheduledChange", "investigation"],
    },
    total=False,
)

DescribeEventTypesResponseTypeDef = TypedDict(
    "DescribeEventTypesResponseTypeDef",
    {"eventTypes": List[EventTypeTypeDef], "nextToken": str},
    total=False,
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef", {"events": List[EventTypeDef], "nextToken": str}, total=False
)

DateTimeRangeTypeDef = TypedDict(
    "DateTimeRangeTypeDef", {"from": datetime, "to": datetime}, total=False
)

_RequiredEntityFilterTypeDef = TypedDict("_RequiredEntityFilterTypeDef", {"eventArns": List[str]})
_OptionalEntityFilterTypeDef = TypedDict(
    "_OptionalEntityFilterTypeDef",
    {
        "entityArns": List[str],
        "entityValues": List[str],
        "lastUpdatedTimes": List[DateTimeRangeTypeDef],
        "tags": List[Dict[str, str]],
        "statusCodes": List[Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"]],
    },
    total=False,
)


class EntityFilterTypeDef(_RequiredEntityFilterTypeDef, _OptionalEntityFilterTypeDef):
    pass


EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[DateTimeRangeTypeDef],
        "endTimes": List[DateTimeRangeTypeDef],
        "lastUpdatedTimes": List[DateTimeRangeTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[Literal["open", "closed", "upcoming"]],
    },
    total=False,
)

EventTypeFilterTypeDef = TypedDict(
    "EventTypeFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "services": List[str],
        "eventTypeCategories": List[
            Literal["issue", "accountNotification", "scheduledChange", "investigation"]
        ],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
