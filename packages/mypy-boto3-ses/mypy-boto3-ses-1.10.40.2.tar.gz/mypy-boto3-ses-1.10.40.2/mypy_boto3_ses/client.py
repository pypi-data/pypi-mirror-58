"Main interface for ses service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_ses.client as client_scope

# pylint: disable=import-self
import mypy_boto3_ses.paginator as paginator_scope
from mypy_boto3_ses.type_defs import (
    BouncedRecipientInfoTypeDef,
    BulkEmailDestinationTypeDef,
    ConfigurationSetTypeDef,
    DeliveryOptionsTypeDef,
    DescribeActiveReceiptRuleSetResponseTypeDef,
    DescribeConfigurationSetResponseTypeDef,
    DescribeReceiptRuleResponseTypeDef,
    DescribeReceiptRuleSetResponseTypeDef,
    DestinationTypeDef,
    EventDestinationTypeDef,
    GetAccountSendingEnabledResponseTypeDef,
    GetCustomVerificationEmailTemplateResponseTypeDef,
    GetIdentityDkimAttributesResponseTypeDef,
    GetIdentityMailFromDomainAttributesResponseTypeDef,
    GetIdentityNotificationAttributesResponseTypeDef,
    GetIdentityPoliciesResponseTypeDef,
    GetIdentityVerificationAttributesResponseTypeDef,
    GetSendQuotaResponseTypeDef,
    GetSendStatisticsResponseTypeDef,
    GetTemplateResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListCustomVerificationEmailTemplatesResponseTypeDef,
    ListIdentitiesResponseTypeDef,
    ListIdentityPoliciesResponseTypeDef,
    ListReceiptFiltersResponseTypeDef,
    ListReceiptRuleSetsResponseTypeDef,
    ListTemplatesResponseTypeDef,
    ListVerifiedEmailAddressesResponseTypeDef,
    MessageDsnTypeDef,
    MessageTagTypeDef,
    MessageTypeDef,
    RawMessageTypeDef,
    ReceiptFilterTypeDef,
    ReceiptRuleTypeDef,
    SendBounceResponseTypeDef,
    SendBulkTemplatedEmailResponseTypeDef,
    SendCustomVerificationEmailResponseTypeDef,
    SendEmailResponseTypeDef,
    SendRawEmailResponseTypeDef,
    SendTemplatedEmailResponseTypeDef,
    TemplateTypeDef,
    TestRenderTemplateResponseTypeDef,
    TrackingOptionsTypeDef,
    VerifyDomainDkimResponseTypeDef,
    VerifyDomainIdentityResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_ses.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SESClient",)


class SESClient(BaseClient):
    """
    [SES.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def clone_receipt_rule_set(self, RuleSetName: str, OriginalRuleSetName: str) -> Dict[str, Any]:
        """
        [Client.clone_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.clone_receipt_rule_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_configuration_set(self, ConfigurationSet: ConfigurationSetTypeDef) -> Dict[str, Any]:
        """
        [Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.create_configuration_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestination: EventDestinationTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.create_configuration_set_event_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_configuration_set_tracking_options(
        self, ConfigurationSetName: str, TrackingOptions: TrackingOptionsTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.create_configuration_set_tracking_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str,
    ) -> None:
        """
        [Client.create_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.create_custom_verification_email_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_receipt_filter(self, Filter: ReceiptFilterTypeDef) -> Dict[str, Any]:
        """
        [Client.create_receipt_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.create_receipt_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_receipt_rule(
        self, RuleSetName: str, Rule: ReceiptRuleTypeDef, After: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.create_receipt_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_receipt_rule_set(self, RuleSetName: str) -> Dict[str, Any]:
        """
        [Client.create_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.create_receipt_rule_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_template(self, Template: TemplateTypeDef) -> Dict[str, Any]:
        """
        [Client.create_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.create_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.delete_configuration_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.delete_configuration_set_event_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_configuration_set_tracking_options(
        self, ConfigurationSetName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.delete_configuration_set_tracking_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_custom_verification_email_template(self, TemplateName: str) -> None:
        """
        [Client.delete_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.delete_custom_verification_email_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_identity(self, Identity: str) -> Dict[str, Any]:
        """
        [Client.delete_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.delete_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_identity_policy(self, Identity: str, PolicyName: str) -> Dict[str, Any]:
        """
        [Client.delete_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.delete_identity_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_receipt_filter(self, FilterName: str) -> Dict[str, Any]:
        """
        [Client.delete_receipt_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.delete_receipt_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_receipt_rule(self, RuleSetName: str, RuleName: str) -> Dict[str, Any]:
        """
        [Client.delete_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.delete_receipt_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_receipt_rule_set(self, RuleSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.delete_receipt_rule_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_template(self, TemplateName: str) -> Dict[str, Any]:
        """
        [Client.delete_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.delete_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_verified_email_address(self, EmailAddress: str) -> None:
        """
        [Client.delete_verified_email_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.delete_verified_email_address)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_active_receipt_rule_set(self) -> DescribeActiveReceiptRuleSetResponseTypeDef:
        """
        [Client.describe_active_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.describe_active_receipt_rule_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_configuration_set(
        self,
        ConfigurationSetName: str,
        ConfigurationSetAttributeNames: List[
            Literal["eventDestinations", "trackingOptions", "deliveryOptions", "reputationOptions"]
        ] = None,
    ) -> DescribeConfigurationSetResponseTypeDef:
        """
        [Client.describe_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.describe_configuration_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_receipt_rule(
        self, RuleSetName: str, RuleName: str
    ) -> DescribeReceiptRuleResponseTypeDef:
        """
        [Client.describe_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.describe_receipt_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_receipt_rule_set(self, RuleSetName: str) -> DescribeReceiptRuleSetResponseTypeDef:
        """
        [Client.describe_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.describe_receipt_rule_set)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_account_sending_enabled(self) -> GetAccountSendingEnabledResponseTypeDef:
        """
        [Client.get_account_sending_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.get_account_sending_enabled)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_custom_verification_email_template(
        self, TemplateName: str
    ) -> GetCustomVerificationEmailTemplateResponseTypeDef:
        """
        [Client.get_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.get_custom_verification_email_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_identity_dkim_attributes(
        self, Identities: List[str]
    ) -> GetIdentityDkimAttributesResponseTypeDef:
        """
        [Client.get_identity_dkim_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.get_identity_dkim_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_identity_mail_from_domain_attributes(
        self, Identities: List[str]
    ) -> GetIdentityMailFromDomainAttributesResponseTypeDef:
        """
        [Client.get_identity_mail_from_domain_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.get_identity_mail_from_domain_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_identity_notification_attributes(
        self, Identities: List[str]
    ) -> GetIdentityNotificationAttributesResponseTypeDef:
        """
        [Client.get_identity_notification_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.get_identity_notification_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_identity_policies(
        self, Identity: str, PolicyNames: List[str]
    ) -> GetIdentityPoliciesResponseTypeDef:
        """
        [Client.get_identity_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.get_identity_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_identity_verification_attributes(
        self, Identities: List[str]
    ) -> GetIdentityVerificationAttributesResponseTypeDef:
        """
        [Client.get_identity_verification_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.get_identity_verification_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_send_quota(self) -> GetSendQuotaResponseTypeDef:
        """
        [Client.get_send_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.get_send_quota)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_send_statistics(self) -> GetSendStatisticsResponseTypeDef:
        """
        [Client.get_send_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.get_send_statistics)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_template(self, TemplateName: str) -> GetTemplateResponseTypeDef:
        """
        [Client.get_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.get_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configuration_sets(
        self, NextToken: str = None, MaxItems: int = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        [Client.list_configuration_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.list_configuration_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_custom_verification_email_templates(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListCustomVerificationEmailTemplatesResponseTypeDef:
        """
        [Client.list_custom_verification_email_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.list_custom_verification_email_templates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_identities(
        self,
        IdentityType: Literal["EmailAddress", "Domain"] = None,
        NextToken: str = None,
        MaxItems: int = None,
    ) -> ListIdentitiesResponseTypeDef:
        """
        [Client.list_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.list_identities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_identity_policies(self, Identity: str) -> ListIdentityPoliciesResponseTypeDef:
        """
        [Client.list_identity_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.list_identity_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_receipt_filters(self) -> ListReceiptFiltersResponseTypeDef:
        """
        [Client.list_receipt_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.list_receipt_filters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_receipt_rule_sets(self, NextToken: str = None) -> ListReceiptRuleSetsResponseTypeDef:
        """
        [Client.list_receipt_rule_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.list_receipt_rule_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_templates(
        self, NextToken: str = None, MaxItems: int = None
    ) -> ListTemplatesResponseTypeDef:
        """
        [Client.list_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.list_templates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_verified_email_addresses(self) -> ListVerifiedEmailAddressesResponseTypeDef:
        """
        [Client.list_verified_email_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.list_verified_email_addresses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_configuration_set_delivery_options(
        self, ConfigurationSetName: str, DeliveryOptions: DeliveryOptionsTypeDef = None
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_delivery_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.put_configuration_set_delivery_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_identity_policy(self, Identity: str, PolicyName: str, Policy: str) -> Dict[str, Any]:
        """
        [Client.put_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.put_identity_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reorder_receipt_rule_set(self, RuleSetName: str, RuleNames: List[str]) -> Dict[str, Any]:
        """
        [Client.reorder_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.reorder_receipt_rule_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_bounce(
        self,
        OriginalMessageId: str,
        BounceSender: str,
        BouncedRecipientInfoList: List[BouncedRecipientInfoTypeDef],
        Explanation: str = None,
        MessageDsn: MessageDsnTypeDef = None,
        BounceSenderArn: str = None,
    ) -> SendBounceResponseTypeDef:
        """
        [Client.send_bounce documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.send_bounce)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_bulk_templated_email(
        self,
        Source: str,
        Template: str,
        Destinations: List[BulkEmailDestinationTypeDef],
        SourceArn: str = None,
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        ReturnPathArn: str = None,
        ConfigurationSetName: str = None,
        DefaultTags: List[MessageTagTypeDef] = None,
        TemplateArn: str = None,
        DefaultTemplateData: str = None,
    ) -> SendBulkTemplatedEmailResponseTypeDef:
        """
        [Client.send_bulk_templated_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.send_bulk_templated_email)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_custom_verification_email(
        self, EmailAddress: str, TemplateName: str, ConfigurationSetName: str = None
    ) -> SendCustomVerificationEmailResponseTypeDef:
        """
        [Client.send_custom_verification_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.send_custom_verification_email)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_email(
        self,
        Source: str,
        Destination: DestinationTypeDef,
        Message: MessageTypeDef,
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List[MessageTagTypeDef] = None,
        ConfigurationSetName: str = None,
    ) -> SendEmailResponseTypeDef:
        """
        [Client.send_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.send_email)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_raw_email(
        self,
        RawMessage: RawMessageTypeDef,
        Source: str = None,
        Destinations: List[str] = None,
        FromArn: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List[MessageTagTypeDef] = None,
        ConfigurationSetName: str = None,
    ) -> SendRawEmailResponseTypeDef:
        """
        [Client.send_raw_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.send_raw_email)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_templated_email(
        self,
        Source: str,
        Destination: DestinationTypeDef,
        Template: str,
        TemplateData: str,
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List[MessageTagTypeDef] = None,
        ConfigurationSetName: str = None,
        TemplateArn: str = None,
    ) -> SendTemplatedEmailResponseTypeDef:
        """
        [Client.send_templated_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.send_templated_email)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_active_receipt_rule_set(self, RuleSetName: str = None) -> Dict[str, Any]:
        """
        [Client.set_active_receipt_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.set_active_receipt_rule_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_identity_dkim_enabled(self, Identity: str, DkimEnabled: bool) -> Dict[str, Any]:
        """
        [Client.set_identity_dkim_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.set_identity_dkim_enabled)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_identity_feedback_forwarding_enabled(
        self, Identity: str, ForwardingEnabled: bool
    ) -> Dict[str, Any]:
        """
        [Client.set_identity_feedback_forwarding_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.set_identity_feedback_forwarding_enabled)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_identity_headers_in_notifications_enabled(
        self,
        Identity: str,
        NotificationType: Literal["Bounce", "Complaint", "Delivery"],
        Enabled: bool,
    ) -> Dict[str, Any]:
        """
        [Client.set_identity_headers_in_notifications_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.set_identity_headers_in_notifications_enabled)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_identity_mail_from_domain(
        self,
        Identity: str,
        MailFromDomain: str = None,
        BehaviorOnMXFailure: Literal["UseDefaultValue", "RejectMessage"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.set_identity_mail_from_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.set_identity_mail_from_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_identity_notification_topic(
        self,
        Identity: str,
        NotificationType: Literal["Bounce", "Complaint", "Delivery"],
        SnsTopic: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.set_identity_notification_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.set_identity_notification_topic)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_receipt_rule_position(
        self, RuleSetName: str, RuleName: str, After: str = None
    ) -> Dict[str, Any]:
        """
        [Client.set_receipt_rule_position documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.set_receipt_rule_position)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def test_render_template(
        self, TemplateName: str, TemplateData: str
    ) -> TestRenderTemplateResponseTypeDef:
        """
        [Client.test_render_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.test_render_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_account_sending_enabled(self, Enabled: bool = None) -> None:
        """
        [Client.update_account_sending_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.update_account_sending_enabled)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestination: EventDestinationTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.update_configuration_set_event_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_configuration_set_reputation_metrics_enabled(
        self, ConfigurationSetName: str, Enabled: bool
    ) -> None:
        """
        [Client.update_configuration_set_reputation_metrics_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.update_configuration_set_reputation_metrics_enabled)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_configuration_set_sending_enabled(
        self, ConfigurationSetName: str, Enabled: bool
    ) -> None:
        """
        [Client.update_configuration_set_sending_enabled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.update_configuration_set_sending_enabled)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_configuration_set_tracking_options(
        self, ConfigurationSetName: str, TrackingOptions: TrackingOptionsTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.update_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.update_configuration_set_tracking_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str = None,
        TemplateSubject: str = None,
        TemplateContent: str = None,
        SuccessRedirectionURL: str = None,
        FailureRedirectionURL: str = None,
    ) -> None:
        """
        [Client.update_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.update_custom_verification_email_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_receipt_rule(self, RuleSetName: str, Rule: ReceiptRuleTypeDef) -> Dict[str, Any]:
        """
        [Client.update_receipt_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.update_receipt_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_template(self, Template: TemplateTypeDef) -> Dict[str, Any]:
        """
        [Client.update_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.update_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def verify_domain_dkim(self, Domain: str) -> VerifyDomainDkimResponseTypeDef:
        """
        [Client.verify_domain_dkim documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.verify_domain_dkim)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def verify_domain_identity(self, Domain: str) -> VerifyDomainIdentityResponseTypeDef:
        """
        [Client.verify_domain_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.verify_domain_identity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def verify_email_address(self, EmailAddress: str) -> None:
        """
        [Client.verify_email_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.verify_email_address)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def verify_email_identity(self, EmailAddress: str) -> Dict[str, Any]:
        """
        [Client.verify_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Client.verify_email_identity)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_configuration_sets"]
    ) -> paginator_scope.ListConfigurationSetsPaginator:
        """
        [Paginator.ListConfigurationSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Paginator.ListConfigurationSets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_custom_verification_email_templates"]
    ) -> paginator_scope.ListCustomVerificationEmailTemplatesPaginator:
        """
        [Paginator.ListCustomVerificationEmailTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_identities"]
    ) -> paginator_scope.ListIdentitiesPaginator:
        """
        [Paginator.ListIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Paginator.ListIdentities)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_receipt_rule_sets"]
    ) -> paginator_scope.ListReceiptRuleSetsPaginator:
        """
        [Paginator.ListReceiptRuleSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_templates"]
    ) -> paginator_scope.ListTemplatesPaginator:
        """
        [Paginator.ListTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Paginator.ListTemplates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["identity_exists"]
    ) -> waiter_scope.IdentityExistsWaiter:
        """
        [Waiter.IdentityExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ses.html#SES.Waiter.IdentityExists)
        """


class Exceptions:
    AccountSendingPausedException: Boto3ClientError
    AlreadyExistsException: Boto3ClientError
    CannotDeleteException: Boto3ClientError
    ClientError: Boto3ClientError
    ConfigurationSetAlreadyExistsException: Boto3ClientError
    ConfigurationSetDoesNotExistException: Boto3ClientError
    ConfigurationSetSendingPausedException: Boto3ClientError
    CustomVerificationEmailInvalidContentException: Boto3ClientError
    CustomVerificationEmailTemplateAlreadyExistsException: Boto3ClientError
    CustomVerificationEmailTemplateDoesNotExistException: Boto3ClientError
    EventDestinationAlreadyExistsException: Boto3ClientError
    EventDestinationDoesNotExistException: Boto3ClientError
    FromEmailAddressNotVerifiedException: Boto3ClientError
    InvalidCloudWatchDestinationException: Boto3ClientError
    InvalidConfigurationSetException: Boto3ClientError
    InvalidDeliveryOptionsException: Boto3ClientError
    InvalidFirehoseDestinationException: Boto3ClientError
    InvalidLambdaFunctionException: Boto3ClientError
    InvalidPolicyException: Boto3ClientError
    InvalidRenderingParameterException: Boto3ClientError
    InvalidS3ConfigurationException: Boto3ClientError
    InvalidSNSDestinationException: Boto3ClientError
    InvalidSnsTopicException: Boto3ClientError
    InvalidTemplateException: Boto3ClientError
    InvalidTrackingOptionsException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MailFromDomainNotVerifiedException: Boto3ClientError
    MessageRejected: Boto3ClientError
    MissingRenderingAttributeException: Boto3ClientError
    ProductionAccessNotGrantedException: Boto3ClientError
    RuleDoesNotExistException: Boto3ClientError
    RuleSetDoesNotExistException: Boto3ClientError
    TemplateDoesNotExistException: Boto3ClientError
    TrackingOptionsAlreadyExistsException: Boto3ClientError
    TrackingOptionsDoesNotExistException: Boto3ClientError
