"Main interface for connect service"
from mypy_boto3_connect.client import ConnectClient, ConnectClient as Client
from mypy_boto3_connect.paginator import (
    GetMetricDataPaginator,
    ListContactFlowsPaginator,
    ListHoursOfOperationsPaginator,
    ListPhoneNumbersPaginator,
    ListQueuesPaginator,
    ListRoutingProfilesPaginator,
    ListSecurityProfilesPaginator,
    ListUserHierarchyGroupsPaginator,
    ListUsersPaginator,
)


__all__ = (
    "Client",
    "ConnectClient",
    "GetMetricDataPaginator",
    "ListContactFlowsPaginator",
    "ListHoursOfOperationsPaginator",
    "ListPhoneNumbersPaginator",
    "ListQueuesPaginator",
    "ListRoutingProfilesPaginator",
    "ListSecurityProfilesPaginator",
    "ListUserHierarchyGroupsPaginator",
    "ListUsersPaginator",
)
