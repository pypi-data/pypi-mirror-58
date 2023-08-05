"Main interface for budgets service"
from mypy_boto3_budgets.client import BudgetsClient as Client, BudgetsClient
from mypy_boto3_budgets.paginator import (
    DescribeBudgetsPaginator,
    DescribeNotificationsForBudgetPaginator,
    DescribeSubscribersForNotificationPaginator,
)


__all__ = (
    "BudgetsClient",
    "Client",
    "DescribeBudgetsPaginator",
    "DescribeNotificationsForBudgetPaginator",
    "DescribeSubscribersForNotificationPaginator",
)
