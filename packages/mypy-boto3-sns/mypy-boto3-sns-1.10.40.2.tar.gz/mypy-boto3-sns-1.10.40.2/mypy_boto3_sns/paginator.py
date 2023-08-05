"Main interface for sns service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sns.type_defs import (
    ListEndpointsByPlatformApplicationResponseTypeDef,
    ListPhoneNumbersOptedOutResponseTypeDef,
    ListPlatformApplicationsResponseTypeDef,
    ListSubscriptionsByTopicResponseTypeDef,
    ListSubscriptionsResponseTypeDef,
    ListTopicsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListEndpointsByPlatformApplicationPaginator",
    "ListPhoneNumbersOptedOutPaginator",
    "ListPlatformApplicationsPaginator",
    "ListSubscriptionsPaginator",
    "ListSubscriptionsByTopicPaginator",
    "ListTopicsPaginator",
)


class ListEndpointsByPlatformApplicationPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpointsByPlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PlatformApplicationArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListEndpointsByPlatformApplicationResponseTypeDef, None, None]:
        """
        [ListEndpointsByPlatformApplication.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication.paginate)
        """


class ListPhoneNumbersOptedOutPaginator(Boto3Paginator):
    """
    [Paginator.ListPhoneNumbersOptedOut documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPhoneNumbersOptedOutResponseTypeDef, None, None]:
        """
        [ListPhoneNumbersOptedOut.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut.paginate)
        """


class ListPlatformApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListPlatformApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListPlatformApplications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPlatformApplicationsResponseTypeDef, None, None]:
        """
        [ListPlatformApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListPlatformApplications.paginate)
        """


class ListSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListSubscriptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSubscriptionsResponseTypeDef, None, None]:
        """
        [ListSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListSubscriptions.paginate)
        """


class ListSubscriptionsByTopicPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscriptionsByTopic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, TopicArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSubscriptionsByTopicResponseTypeDef, None, None]:
        """
        [ListSubscriptionsByTopic.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic.paginate)
        """


class ListTopicsPaginator(Boto3Paginator):
    """
    [Paginator.ListTopics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListTopics)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTopicsResponseTypeDef, None, None]:
        """
        [ListTopics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sns.html#SNS.Paginator.ListTopics.paginate)
        """
