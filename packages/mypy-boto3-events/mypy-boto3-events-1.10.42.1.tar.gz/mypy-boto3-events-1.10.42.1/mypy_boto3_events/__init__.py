"Main interface for events service"
from mypy_boto3_events.client import EventBridgeClient, EventBridgeClient as Client
from mypy_boto3_events.paginator import (
    ListRuleNamesByTargetPaginator,
    ListRulesPaginator,
    ListTargetsByRulePaginator,
)


__all__ = (
    "Client",
    "EventBridgeClient",
    "ListRuleNamesByTargetPaginator",
    "ListRulesPaginator",
    "ListTargetsByRulePaginator",
)
