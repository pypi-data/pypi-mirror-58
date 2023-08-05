"Main interface for sns service"
from mypy_boto3_sns.client import SNSClient, SNSClient as Client
from mypy_boto3_sns.paginator import (
    ListEndpointsByPlatformApplicationPaginator,
    ListPhoneNumbersOptedOutPaginator,
    ListPlatformApplicationsPaginator,
    ListSubscriptionsByTopicPaginator,
    ListSubscriptionsPaginator,
    ListTopicsPaginator,
)
from mypy_boto3_sns.service_resource import (
    SNSServiceResource as ServiceResource,
    SNSServiceResource,
)


__all__ = (
    "Client",
    "ListEndpointsByPlatformApplicationPaginator",
    "ListPhoneNumbersOptedOutPaginator",
    "ListPlatformApplicationsPaginator",
    "ListSubscriptionsByTopicPaginator",
    "ListSubscriptionsPaginator",
    "ListTopicsPaginator",
    "SNSClient",
    "SNSServiceResource",
    "ServiceResource",
)
