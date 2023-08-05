"Main interface for budgets service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_budgets.client as client_scope

# pylint: disable=import-self
import mypy_boto3_budgets.paginator as paginator_scope
from mypy_boto3_budgets.type_defs import (
    BudgetTypeDef,
    DescribeBudgetPerformanceHistoryResponseTypeDef,
    DescribeBudgetResponseTypeDef,
    DescribeBudgetsResponseTypeDef,
    DescribeNotificationsForBudgetResponseTypeDef,
    DescribeSubscribersForNotificationResponseTypeDef,
    NotificationTypeDef,
    NotificationWithSubscribersTypeDef,
    SubscriberTypeDef,
    TimePeriodTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BudgetsClient",)


class BudgetsClient(BaseClient):
    """
    [Budgets.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_budget(
        self,
        AccountId: str,
        Budget: BudgetTypeDef,
        NotificationsWithSubscribers: List[NotificationWithSubscribersTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.create_budget)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: NotificationTypeDef,
        Subscribers: List[SubscriberTypeDef],
    ) -> Dict[str, Any]:
        """
        [Client.create_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.create_notification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: NotificationTypeDef,
        Subscriber: SubscriberTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.create_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.create_subscriber)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_budget(self, AccountId: str, BudgetName: str) -> Dict[str, Any]:
        """
        [Client.delete_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.delete_budget)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_notification(
        self, AccountId: str, BudgetName: str, Notification: NotificationTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.delete_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.delete_notification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: NotificationTypeDef,
        Subscriber: SubscriberTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.delete_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.delete_subscriber)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_budget(self, AccountId: str, BudgetName: str) -> DescribeBudgetResponseTypeDef:
        """
        [Client.describe_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.describe_budget)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_budget_performance_history(
        self,
        AccountId: str,
        BudgetName: str,
        TimePeriod: TimePeriodTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeBudgetPerformanceHistoryResponseTypeDef:
        """
        [Client.describe_budget_performance_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.describe_budget_performance_history)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_budgets(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetsResponseTypeDef:
        """
        [Client.describe_budgets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.describe_budgets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_notifications_for_budget(
        self, AccountId: str, BudgetName: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeNotificationsForBudgetResponseTypeDef:
        """
        [Client.describe_notifications_for_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.describe_notifications_for_budget)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_subscribers_for_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: NotificationTypeDef,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeSubscribersForNotificationResponseTypeDef:
        """
        [Client.describe_subscribers_for_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.describe_subscribers_for_notification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_budget(self, AccountId: str, NewBudget: BudgetTypeDef) -> Dict[str, Any]:
        """
        [Client.update_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.update_budget)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_notification(
        self,
        AccountId: str,
        BudgetName: str,
        OldNotification: NotificationTypeDef,
        NewNotification: NotificationTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.update_notification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: NotificationTypeDef,
        OldSubscriber: SubscriberTypeDef,
        NewSubscriber: SubscriberTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Client.update_subscriber)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_budgets"]
    ) -> paginator_scope.DescribeBudgetsPaginator:
        """
        [Paginator.DescribeBudgets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_notifications_for_budget"]
    ) -> paginator_scope.DescribeNotificationsForBudgetPaginator:
        """
        [Paginator.DescribeNotificationsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_subscribers_for_notification"]
    ) -> paginator_scope.DescribeSubscribersForNotificationPaginator:
        """
        [Paginator.DescribeSubscribersForNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    CreationLimitExceededException: Boto3ClientError
    DuplicateRecordException: Boto3ClientError
    ExpiredNextTokenException: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    NotFoundException: Boto3ClientError
