"Main interface for events service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_events.type_defs import (
    ListRuleNamesByTargetResponseTypeDef,
    ListRulesResponseTypeDef,
    ListTargetsByRuleResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListRuleNamesByTargetPaginator", "ListRulesPaginator", "ListTargetsByRulePaginator")


class ListRuleNamesByTargetPaginator(Boto3Paginator):
    """
    [Paginator.ListRuleNamesByTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TargetArn: str,
        EventBusName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRuleNamesByTargetResponseTypeDef, None, None]:
        """
        [ListRuleNamesByTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget.paginate)
        """


class ListRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/events.html#EventBridge.Paginator.ListRules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        NamePrefix: str = None,
        EventBusName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRulesResponseTypeDef, None, None]:
        """
        [ListRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/events.html#EventBridge.Paginator.ListRules.paginate)
        """


class ListTargetsByRulePaginator(Boto3Paginator):
    """
    [Paginator.ListTargetsByRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Rule: str, EventBusName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTargetsByRuleResponseTypeDef, None, None]:
        """
        [ListTargetsByRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule.paginate)
        """
