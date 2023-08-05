"Main interface for pinpoint-email service"
from mypy_boto3_pinpoint_email.client import PinpointEmailClient, PinpointEmailClient as Client
from mypy_boto3_pinpoint_email.paginator import (
    GetDedicatedIpsPaginator,
    ListConfigurationSetsPaginator,
    ListDedicatedIpPoolsPaginator,
    ListDeliverabilityTestReportsPaginator,
    ListEmailIdentitiesPaginator,
)


__all__ = (
    "Client",
    "GetDedicatedIpsPaginator",
    "ListConfigurationSetsPaginator",
    "ListDedicatedIpPoolsPaginator",
    "ListDeliverabilityTestReportsPaginator",
    "ListEmailIdentitiesPaginator",
    "PinpointEmailClient",
)
