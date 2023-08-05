"Main interface for route53domains service"
from mypy_boto3_route53domains.client import Route53DomainsClient, Route53DomainsClient as Client
from mypy_boto3_route53domains.paginator import (
    ListDomainsPaginator,
    ListOperationsPaginator,
    ViewBillingPaginator,
)


__all__ = (
    "Client",
    "ListDomainsPaginator",
    "ListOperationsPaginator",
    "Route53DomainsClient",
    "ViewBillingPaginator",
)
