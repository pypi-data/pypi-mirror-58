"Main interface for route53domains service Paginators"
from __future__ import annotations

from datetime import datetime
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_route53domains.type_defs import (
    ListDomainsResponseTypeDef,
    ListOperationsResponseTypeDef,
    PaginatorConfigTypeDef,
    ViewBillingResponseTypeDef,
)


__all__ = ("ListDomainsPaginator", "ListOperationsPaginator", "ViewBillingPaginator")


class ListDomainsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDomainsResponseTypeDef, None, None]:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains.paginate)
        """


class ListOperationsPaginator(Boto3Paginator):
    """
    [Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, SubmittedSince: datetime = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListOperationsResponseTypeDef, None, None]:
        """
        [ListOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations.paginate)
        """


class ViewBillingPaginator(Boto3Paginator):
    """
    [Paginator.ViewBilling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Start: datetime = None,
        End: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ViewBillingResponseTypeDef, None, None]:
        """
        [ViewBilling.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling.paginate)
        """
