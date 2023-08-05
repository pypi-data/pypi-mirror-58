"Main interface for route53 service"
from mypy_boto3_route53.client import Route53Client as Client, Route53Client
from mypy_boto3_route53.paginator import (
    ListHealthChecksPaginator,
    ListHostedZonesPaginator,
    ListQueryLoggingConfigsPaginator,
    ListResourceRecordSetsPaginator,
    ListVPCAssociationAuthorizationsPaginator,
)
from mypy_boto3_route53.waiter import ResourceRecordSetsChangedWaiter


__all__ = (
    "Client",
    "ListHealthChecksPaginator",
    "ListHostedZonesPaginator",
    "ListQueryLoggingConfigsPaginator",
    "ListResourceRecordSetsPaginator",
    "ListVPCAssociationAuthorizationsPaginator",
    "ResourceRecordSetsChangedWaiter",
    "Route53Client",
)
