"Main interface for codestar-notifications service"
from mypy_boto3_codestar_notifications.client import (
    CodeStarNotificationsClient,
    CodeStarNotificationsClient as Client,
)
from mypy_boto3_codestar_notifications.paginator import (
    ListEventTypesPaginator,
    ListNotificationRulesPaginator,
    ListTargetsPaginator,
)


__all__ = (
    "Client",
    "CodeStarNotificationsClient",
    "ListEventTypesPaginator",
    "ListNotificationRulesPaginator",
    "ListTargetsPaginator",
)
