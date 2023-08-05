"Main interface for sesv2 service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sesv2.client as client_scope
from mypy_boto3_sesv2.type_defs import (
    CreateDeliverabilityTestReportResponseTypeDef,
    CreateEmailIdentityResponseTypeDef,
    DeliveryOptionsTypeDef,
    DestinationTypeDef,
    DkimSigningAttributesTypeDef,
    DomainDeliverabilityTrackingOptionTypeDef,
    EmailContentTypeDef,
    EventDestinationDefinitionTypeDef,
    GetAccountResponseTypeDef,
    GetBlacklistReportsResponseTypeDef,
    GetConfigurationSetEventDestinationsResponseTypeDef,
    GetConfigurationSetResponseTypeDef,
    GetDedicatedIpResponseTypeDef,
    GetDedicatedIpsResponseTypeDef,
    GetDeliverabilityDashboardOptionsResponseTypeDef,
    GetDeliverabilityTestReportResponseTypeDef,
    GetDomainDeliverabilityCampaignResponseTypeDef,
    GetDomainStatisticsReportResponseTypeDef,
    GetEmailIdentityResponseTypeDef,
    GetSuppressedDestinationResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListDedicatedIpPoolsResponseTypeDef,
    ListDeliverabilityTestReportsResponseTypeDef,
    ListDomainDeliverabilityCampaignsResponseTypeDef,
    ListEmailIdentitiesResponseTypeDef,
    ListSuppressedDestinationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MessageTagTypeDef,
    PutEmailIdentityDkimSigningAttributesResponseTypeDef,
    ReputationOptionsTypeDef,
    SendEmailResponseTypeDef,
    SendingOptionsTypeDef,
    SuppressionOptionsTypeDef,
    TagTypeDef,
    TrackingOptionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SESV2Client",)


class SESV2Client(BaseClient):
    """
    [SESV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_configuration_set(
        self,
        ConfigurationSetName: str,
        TrackingOptions: TrackingOptionsTypeDef = None,
        DeliveryOptions: DeliveryOptionsTypeDef = None,
        ReputationOptions: ReputationOptionsTypeDef = None,
        SendingOptions: SendingOptionsTypeDef = None,
        Tags: List[TagTypeDef] = None,
        SuppressionOptions: SuppressionOptionsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.create_configuration_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.create_configuration_set_event_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dedicated_ip_pool(
        self, PoolName: str, Tags: List[TagTypeDef] = None
    ) -> Dict[str, Any]:
        """
        [Client.create_dedicated_ip_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.create_dedicated_ip_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_deliverability_test_report(
        self,
        FromEmailAddress: str,
        Content: EmailContentTypeDef,
        ReportName: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDeliverabilityTestReportResponseTypeDef:
        """
        [Client.create_deliverability_test_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.create_deliverability_test_report)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_email_identity(
        self,
        EmailIdentity: str,
        Tags: List[TagTypeDef] = None,
        DkimSigningAttributes: DkimSigningAttributesTypeDef = None,
    ) -> CreateEmailIdentityResponseTypeDef:
        """
        [Client.create_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.create_email_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.delete_configuration_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.delete_configuration_set_event_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dedicated_ip_pool(self, PoolName: str) -> Dict[str, Any]:
        """
        [Client.delete_dedicated_ip_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.delete_dedicated_ip_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_email_identity(self, EmailIdentity: str) -> Dict[str, Any]:
        """
        [Client.delete_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.delete_email_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_suppressed_destination(self, EmailAddress: str) -> Dict[str, Any]:
        """
        [Client.delete_suppressed_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.delete_suppressed_destination)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_account(self) -> GetAccountResponseTypeDef:
        """
        [Client.get_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_blacklist_reports(
        self, BlacklistItemNames: List[str]
    ) -> GetBlacklistReportsResponseTypeDef:
        """
        [Client.get_blacklist_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_blacklist_reports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_configuration_set(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetResponseTypeDef:
        """
        [Client.get_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_configuration_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        [Client.get_configuration_set_event_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_configuration_set_event_destinations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dedicated_ip(self, Ip: str) -> GetDedicatedIpResponseTypeDef:
        """
        [Client.get_dedicated_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_dedicated_ip)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dedicated_ips(
        self, PoolName: str = None, NextToken: str = None, PageSize: int = None
    ) -> GetDedicatedIpsResponseTypeDef:
        """
        [Client.get_dedicated_ips documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_dedicated_ips)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deliverability_dashboard_options(
        self,
    ) -> GetDeliverabilityDashboardOptionsResponseTypeDef:
        """
        [Client.get_deliverability_dashboard_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_deliverability_dashboard_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deliverability_test_report(
        self, ReportId: str
    ) -> GetDeliverabilityTestReportResponseTypeDef:
        """
        [Client.get_deliverability_test_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_deliverability_test_report)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_domain_deliverability_campaign(
        self, CampaignId: str
    ) -> GetDomainDeliverabilityCampaignResponseTypeDef:
        """
        [Client.get_domain_deliverability_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_domain_deliverability_campaign)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_domain_statistics_report(
        self, Domain: str, StartDate: datetime, EndDate: datetime
    ) -> GetDomainStatisticsReportResponseTypeDef:
        """
        [Client.get_domain_statistics_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_domain_statistics_report)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_email_identity(self, EmailIdentity: str) -> GetEmailIdentityResponseTypeDef:
        """
        [Client.get_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_email_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_suppressed_destination(
        self, EmailAddress: str
    ) -> GetSuppressedDestinationResponseTypeDef:
        """
        [Client.get_suppressed_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.get_suppressed_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configuration_sets(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        [Client.list_configuration_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.list_configuration_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dedicated_ip_pools(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDedicatedIpPoolsResponseTypeDef:
        """
        [Client.list_dedicated_ip_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.list_dedicated_ip_pools)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deliverability_test_reports(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDeliverabilityTestReportsResponseTypeDef:
        """
        [Client.list_deliverability_test_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.list_deliverability_test_reports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_domain_deliverability_campaigns(
        self,
        StartDate: datetime,
        EndDate: datetime,
        SubscribedDomain: str,
        NextToken: str = None,
        PageSize: int = None,
    ) -> ListDomainDeliverabilityCampaignsResponseTypeDef:
        """
        [Client.list_domain_deliverability_campaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.list_domain_deliverability_campaigns)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_email_identities(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListEmailIdentitiesResponseTypeDef:
        """
        [Client.list_email_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.list_email_identities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_suppressed_destinations(
        self,
        Reasons: List[Literal["BOUNCE", "COMPLAINT"]] = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        NextToken: str = None,
        PageSize: int = None,
    ) -> ListSuppressedDestinationsResponseTypeDef:
        """
        [Client.list_suppressed_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.list_suppressed_destinations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_account_dedicated_ip_warmup_attributes(
        self, AutoWarmupEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_account_dedicated_ip_warmup_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_account_dedicated_ip_warmup_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_account_sending_attributes(self, SendingEnabled: bool = None) -> Dict[str, Any]:
        """
        [Client.put_account_sending_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_account_sending_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_account_suppression_attributes(
        self, SuppressedReasons: List[Literal["BOUNCE", "COMPLAINT"]] = None
    ) -> Dict[str, Any]:
        """
        [Client.put_account_suppression_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_account_suppression_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_configuration_set_delivery_options(
        self,
        ConfigurationSetName: str,
        TlsPolicy: Literal["REQUIRE", "OPTIONAL"] = None,
        SendingPoolName: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_delivery_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_configuration_set_delivery_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_configuration_set_reputation_options(
        self, ConfigurationSetName: str, ReputationMetricsEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_reputation_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_configuration_set_reputation_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_configuration_set_sending_options(
        self, ConfigurationSetName: str, SendingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_sending_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_configuration_set_sending_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_configuration_set_suppression_options(
        self,
        ConfigurationSetName: str,
        SuppressedReasons: List[Literal["BOUNCE", "COMPLAINT"]] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_suppression_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_configuration_set_suppression_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_configuration_set_tracking_options(
        self, ConfigurationSetName: str, CustomRedirectDomain: str = None
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_configuration_set_tracking_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_dedicated_ip_in_pool(self, Ip: str, DestinationPoolName: str) -> Dict[str, Any]:
        """
        [Client.put_dedicated_ip_in_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_dedicated_ip_in_pool)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_dedicated_ip_warmup_attributes(self, Ip: str, WarmupPercentage: int) -> Dict[str, Any]:
        """
        [Client.put_dedicated_ip_warmup_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_dedicated_ip_warmup_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_deliverability_dashboard_option(
        self,
        DashboardEnabled: bool,
        SubscribedDomains: List[DomainDeliverabilityTrackingOptionTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_deliverability_dashboard_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_deliverability_dashboard_option)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_email_identity_dkim_attributes(
        self, EmailIdentity: str, SigningEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_email_identity_dkim_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_email_identity_dkim_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_email_identity_dkim_signing_attributes(
        self,
        EmailIdentity: str,
        SigningAttributesOrigin: Literal["AWS_SES", "EXTERNAL"],
        SigningAttributes: DkimSigningAttributesTypeDef = None,
    ) -> PutEmailIdentityDkimSigningAttributesResponseTypeDef:
        """
        [Client.put_email_identity_dkim_signing_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_email_identity_dkim_signing_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_email_identity_feedback_attributes(
        self, EmailIdentity: str, EmailForwardingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_email_identity_feedback_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_email_identity_feedback_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_email_identity_mail_from_attributes(
        self,
        EmailIdentity: str,
        MailFromDomain: str = None,
        BehaviorOnMxFailure: Literal["USE_DEFAULT_VALUE", "REJECT_MESSAGE"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_email_identity_mail_from_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_email_identity_mail_from_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_suppressed_destination(
        self, EmailAddress: str, Reason: Literal["BOUNCE", "COMPLAINT"]
    ) -> Dict[str, Any]:
        """
        [Client.put_suppressed_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.put_suppressed_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_email(
        self,
        Destination: DestinationTypeDef,
        Content: EmailContentTypeDef,
        FromEmailAddress: str = None,
        ReplyToAddresses: List[str] = None,
        FeedbackForwardingEmailAddress: str = None,
        EmailTags: List[MessageTagTypeDef] = None,
        ConfigurationSetName: str = None,
    ) -> SendEmailResponseTypeDef:
        """
        [Client.send_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.send_email)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/sesv2.html#SESV2.Client.update_configuration_set_event_destination)
        """


class Exceptions:
    AccountSuspendedException: Boto3ClientError
    AlreadyExistsException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MailFromDomainNotVerifiedException: Boto3ClientError
    MessageRejected: Boto3ClientError
    NotFoundException: Boto3ClientError
    SendingPausedException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
