"Main interface for route53domains service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_route53domains.client as client_scope

# pylint: disable=import-self
import mypy_boto3_route53domains.paginator as paginator_scope
from mypy_boto3_route53domains.type_defs import (
    CheckDomainAvailabilityResponseTypeDef,
    CheckDomainTransferabilityResponseTypeDef,
    ContactDetailTypeDef,
    DisableDomainTransferLockResponseTypeDef,
    EnableDomainTransferLockResponseTypeDef,
    GetContactReachabilityStatusResponseTypeDef,
    GetDomainDetailResponseTypeDef,
    GetDomainSuggestionsResponseTypeDef,
    GetOperationDetailResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListTagsForDomainResponseTypeDef,
    NameserverTypeDef,
    RegisterDomainResponseTypeDef,
    RenewDomainResponseTypeDef,
    ResendContactReachabilityEmailResponseTypeDef,
    RetrieveDomainAuthCodeResponseTypeDef,
    TagTypeDef,
    TransferDomainResponseTypeDef,
    UpdateDomainContactPrivacyResponseTypeDef,
    UpdateDomainContactResponseTypeDef,
    UpdateDomainNameserversResponseTypeDef,
    ViewBillingResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Route53DomainsClient",)


class Route53DomainsClient(BaseClient):
    """
    [Route53Domains.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def check_domain_availability(
        self, DomainName: str, IdnLangCode: str = None
    ) -> CheckDomainAvailabilityResponseTypeDef:
        """
        [Client.check_domain_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.check_domain_availability)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def check_domain_transferability(
        self, DomainName: str, AuthCode: str = None
    ) -> CheckDomainTransferabilityResponseTypeDef:
        """
        [Client.check_domain_transferability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.check_domain_transferability)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tags_for_domain(self, DomainName: str, TagsToDelete: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.delete_tags_for_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_domain_auto_renew(self, DomainName: str) -> Dict[str, Any]:
        """
        [Client.disable_domain_auto_renew documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.disable_domain_auto_renew)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_domain_transfer_lock(
        self, DomainName: str
    ) -> DisableDomainTransferLockResponseTypeDef:
        """
        [Client.disable_domain_transfer_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.disable_domain_transfer_lock)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_domain_auto_renew(self, DomainName: str) -> Dict[str, Any]:
        """
        [Client.enable_domain_auto_renew documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.enable_domain_auto_renew)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_domain_transfer_lock(
        self, DomainName: str
    ) -> EnableDomainTransferLockResponseTypeDef:
        """
        [Client.enable_domain_transfer_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.enable_domain_transfer_lock)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_contact_reachability_status(
        self, domainName: str = None
    ) -> GetContactReachabilityStatusResponseTypeDef:
        """
        [Client.get_contact_reachability_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.get_contact_reachability_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_domain_detail(self, DomainName: str) -> GetDomainDetailResponseTypeDef:
        """
        [Client.get_domain_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.get_domain_detail)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_domain_suggestions(
        self, DomainName: str, SuggestionCount: int, OnlyAvailable: bool
    ) -> GetDomainSuggestionsResponseTypeDef:
        """
        [Client.get_domain_suggestions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.get_domain_suggestions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_operation_detail(self, OperationId: str) -> GetOperationDetailResponseTypeDef:
        """
        [Client.get_operation_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.get_operation_detail)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_domains(self, Marker: str = None, MaxItems: int = None) -> ListDomainsResponseTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.list_domains)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_operations(
        self, SubmittedSince: datetime = None, Marker: str = None, MaxItems: int = None
    ) -> ListOperationsResponseTypeDef:
        """
        [Client.list_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.list_operations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_domain(self, DomainName: str) -> ListTagsForDomainResponseTypeDef:
        """
        [Client.list_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.list_tags_for_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_domain(
        self,
        DomainName: str,
        DurationInYears: int,
        AdminContact: ContactDetailTypeDef,
        RegistrantContact: ContactDetailTypeDef,
        TechContact: ContactDetailTypeDef,
        IdnLangCode: str = None,
        AutoRenew: bool = None,
        PrivacyProtectAdminContact: bool = None,
        PrivacyProtectRegistrantContact: bool = None,
        PrivacyProtectTechContact: bool = None,
    ) -> RegisterDomainResponseTypeDef:
        """
        [Client.register_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.register_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def renew_domain(
        self, DomainName: str, CurrentExpiryYear: int, DurationInYears: int = None
    ) -> RenewDomainResponseTypeDef:
        """
        [Client.renew_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.renew_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resend_contact_reachability_email(
        self, domainName: str = None
    ) -> ResendContactReachabilityEmailResponseTypeDef:
        """
        [Client.resend_contact_reachability_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.resend_contact_reachability_email)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def retrieve_domain_auth_code(self, DomainName: str) -> RetrieveDomainAuthCodeResponseTypeDef:
        """
        [Client.retrieve_domain_auth_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.retrieve_domain_auth_code)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def transfer_domain(
        self,
        DomainName: str,
        DurationInYears: int,
        AdminContact: ContactDetailTypeDef,
        RegistrantContact: ContactDetailTypeDef,
        TechContact: ContactDetailTypeDef,
        IdnLangCode: str = None,
        Nameservers: List[NameserverTypeDef] = None,
        AuthCode: str = None,
        AutoRenew: bool = None,
        PrivacyProtectAdminContact: bool = None,
        PrivacyProtectRegistrantContact: bool = None,
        PrivacyProtectTechContact: bool = None,
    ) -> TransferDomainResponseTypeDef:
        """
        [Client.transfer_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.transfer_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_domain_contact(
        self,
        DomainName: str,
        AdminContact: ContactDetailTypeDef = None,
        RegistrantContact: ContactDetailTypeDef = None,
        TechContact: ContactDetailTypeDef = None,
    ) -> UpdateDomainContactResponseTypeDef:
        """
        [Client.update_domain_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_domain_contact_privacy(
        self,
        DomainName: str,
        AdminPrivacy: bool = None,
        RegistrantPrivacy: bool = None,
        TechPrivacy: bool = None,
    ) -> UpdateDomainContactPrivacyResponseTypeDef:
        """
        [Client.update_domain_contact_privacy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.update_domain_contact_privacy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_domain_nameservers(
        self, DomainName: str, Nameservers: List[NameserverTypeDef], FIAuthKey: str = None
    ) -> UpdateDomainNameserversResponseTypeDef:
        """
        [Client.update_domain_nameservers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.update_domain_nameservers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_tags_for_domain(
        self, DomainName: str, TagsToUpdate: List[TagTypeDef] = None
    ) -> Dict[str, Any]:
        """
        [Client.update_tags_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.update_tags_for_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def view_billing(
        self, Start: datetime = None, End: datetime = None, Marker: str = None, MaxItems: int = None
    ) -> ViewBillingResponseTypeDef:
        """
        [Client.view_billing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Client.view_billing)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_domains"]
    ) -> paginator_scope.ListDomainsPaginator:
        """
        [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_operations"]
    ) -> paginator_scope.ListOperationsPaginator:
        """
        [Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["view_billing"]
    ) -> paginator_scope.ViewBillingPaginator:
        """
        [Paginator.ViewBilling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DomainLimitExceeded: Boto3ClientError
    DuplicateRequest: Boto3ClientError
    InvalidInput: Boto3ClientError
    OperationLimitExceeded: Boto3ClientError
    TLDRulesViolation: Boto3ClientError
    UnsupportedTLD: Boto3ClientError
