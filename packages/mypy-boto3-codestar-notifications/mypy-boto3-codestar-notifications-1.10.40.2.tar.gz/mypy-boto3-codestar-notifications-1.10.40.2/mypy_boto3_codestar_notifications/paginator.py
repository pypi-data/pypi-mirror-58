"Main interface for codestar-notifications service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codestar_notifications.type_defs import (
    ListEventTypesFilterTypeDef,
    ListEventTypesResultTypeDef,
    ListNotificationRulesFilterTypeDef,
    ListNotificationRulesResultTypeDef,
    ListTargetsFilterTypeDef,
    ListTargetsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListEventTypesPaginator", "ListNotificationRulesPaginator", "ListTargetsPaginator")


class ListEventTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListEventTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListEventTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListEventTypesFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListEventTypesResultTypeDef, None, None]:
        """
        [ListEventTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListEventTypes.paginate)
        """


class ListNotificationRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListNotificationRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListNotificationRules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListNotificationRulesFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListNotificationRulesResultTypeDef, None, None]:
        """
        [ListNotificationRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListNotificationRules.paginate)
        """


class ListTargetsPaginator(Boto3Paginator):
    """
    [Paginator.ListTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListTargets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListTargetsFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListTargetsResultTypeDef, None, None]:
        """
        [ListTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListTargets.paginate)
        """
