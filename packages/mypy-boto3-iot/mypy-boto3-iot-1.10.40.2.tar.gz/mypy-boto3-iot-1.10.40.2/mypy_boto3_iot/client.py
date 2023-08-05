"Main interface for iot service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_iot.client as client_scope

# pylint: disable=import-self
import mypy_boto3_iot.paginator as paginator_scope
from mypy_boto3_iot.type_defs import (
    AbortConfigTypeDef,
    AlertTargetTypeDef,
    AssociateTargetsWithJobResponseTypeDef,
    AttributePayloadTypeDef,
    AuditCheckConfigurationTypeDef,
    AuditMitigationActionsTaskTargetTypeDef,
    AuditNotificationTargetTypeDef,
    AuthInfoTypeDef,
    AuthorizerConfigTypeDef,
    AwsJobExecutionsRolloutConfigTypeDef,
    BehaviorTypeDef,
    BillingGroupPropertiesTypeDef,
    CancelJobResponseTypeDef,
    ConfigurationTypeDef,
    CreateAuthorizerResponseTypeDef,
    CreateBillingGroupResponseTypeDef,
    CreateCertificateFromCsrResponseTypeDef,
    CreateDomainConfigurationResponseTypeDef,
    CreateDynamicThingGroupResponseTypeDef,
    CreateJobResponseTypeDef,
    CreateKeysAndCertificateResponseTypeDef,
    CreateMitigationActionResponseTypeDef,
    CreateOTAUpdateResponseTypeDef,
    CreatePolicyResponseTypeDef,
    CreatePolicyVersionResponseTypeDef,
    CreateProvisioningClaimResponseTypeDef,
    CreateProvisioningTemplateResponseTypeDef,
    CreateProvisioningTemplateVersionResponseTypeDef,
    CreateRoleAliasResponseTypeDef,
    CreateScheduledAuditResponseTypeDef,
    CreateSecurityProfileResponseTypeDef,
    CreateStreamResponseTypeDef,
    CreateThingGroupResponseTypeDef,
    CreateThingResponseTypeDef,
    CreateThingTypeResponseTypeDef,
    CreateTopicRuleDestinationResponseTypeDef,
    DescribeAccountAuditConfigurationResponseTypeDef,
    DescribeAuditFindingResponseTypeDef,
    DescribeAuditMitigationActionsTaskResponseTypeDef,
    DescribeAuditTaskResponseTypeDef,
    DescribeAuthorizerResponseTypeDef,
    DescribeBillingGroupResponseTypeDef,
    DescribeCACertificateResponseTypeDef,
    DescribeCertificateResponseTypeDef,
    DescribeDefaultAuthorizerResponseTypeDef,
    DescribeDomainConfigurationResponseTypeDef,
    DescribeEndpointResponseTypeDef,
    DescribeEventConfigurationsResponseTypeDef,
    DescribeIndexResponseTypeDef,
    DescribeJobExecutionResponseTypeDef,
    DescribeJobResponseTypeDef,
    DescribeMitigationActionResponseTypeDef,
    DescribeProvisioningTemplateResponseTypeDef,
    DescribeProvisioningTemplateVersionResponseTypeDef,
    DescribeRoleAliasResponseTypeDef,
    DescribeScheduledAuditResponseTypeDef,
    DescribeSecurityProfileResponseTypeDef,
    DescribeStreamResponseTypeDef,
    DescribeThingGroupResponseTypeDef,
    DescribeThingRegistrationTaskResponseTypeDef,
    DescribeThingResponseTypeDef,
    DescribeThingTypeResponseTypeDef,
    GetCardinalityResponseTypeDef,
    GetEffectivePoliciesResponseTypeDef,
    GetIndexingConfigurationResponseTypeDef,
    GetJobDocumentResponseTypeDef,
    GetLoggingOptionsResponseTypeDef,
    GetOTAUpdateResponseTypeDef,
    GetPercentilesResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetPolicyVersionResponseTypeDef,
    GetRegistrationCodeResponseTypeDef,
    GetStatisticsResponseTypeDef,
    GetTopicRuleDestinationResponseTypeDef,
    GetTopicRuleResponseTypeDef,
    GetV2LoggingOptionsResponseTypeDef,
    HttpContextTypeDef,
    JobExecutionsRolloutConfigTypeDef,
    ListActiveViolationsResponseTypeDef,
    ListAttachedPoliciesResponseTypeDef,
    ListAuditFindingsResponseTypeDef,
    ListAuditMitigationActionsExecutionsResponseTypeDef,
    ListAuditMitigationActionsTasksResponseTypeDef,
    ListAuditTasksResponseTypeDef,
    ListAuthorizersResponseTypeDef,
    ListBillingGroupsResponseTypeDef,
    ListCACertificatesResponseTypeDef,
    ListCertificatesByCAResponseTypeDef,
    ListCertificatesResponseTypeDef,
    ListDomainConfigurationsResponseTypeDef,
    ListIndicesResponseTypeDef,
    ListJobExecutionsForJobResponseTypeDef,
    ListJobExecutionsForThingResponseTypeDef,
    ListJobsResponseTypeDef,
    ListMitigationActionsResponseTypeDef,
    ListOTAUpdatesResponseTypeDef,
    ListOutgoingCertificatesResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyPrincipalsResponseTypeDef,
    ListPolicyVersionsResponseTypeDef,
    ListPrincipalPoliciesResponseTypeDef,
    ListPrincipalThingsResponseTypeDef,
    ListProvisioningTemplateVersionsResponseTypeDef,
    ListProvisioningTemplatesResponseTypeDef,
    ListRoleAliasesResponseTypeDef,
    ListScheduledAuditsResponseTypeDef,
    ListSecurityProfilesForTargetResponseTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListStreamsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsForPolicyResponseTypeDef,
    ListTargetsForSecurityProfileResponseTypeDef,
    ListThingGroupsForThingResponseTypeDef,
    ListThingGroupsResponseTypeDef,
    ListThingPrincipalsResponseTypeDef,
    ListThingRegistrationTaskReportsResponseTypeDef,
    ListThingRegistrationTasksResponseTypeDef,
    ListThingTypesResponseTypeDef,
    ListThingsInBillingGroupResponseTypeDef,
    ListThingsInThingGroupResponseTypeDef,
    ListThingsResponseTypeDef,
    ListTopicRuleDestinationsResponseTypeDef,
    ListTopicRulesResponseTypeDef,
    ListV2LoggingLevelsResponseTypeDef,
    ListViolationEventsResponseTypeDef,
    LogTargetTypeDef,
    LoggingOptionsPayloadTypeDef,
    MitigationActionParamsTypeDef,
    MqttContextTypeDef,
    OTAUpdateFileTypeDef,
    PresignedUrlConfigTypeDef,
    RegisterCACertificateResponseTypeDef,
    RegisterCertificateResponseTypeDef,
    RegisterThingResponseTypeDef,
    RegistrationConfigTypeDef,
    ResourceIdentifierTypeDef,
    SearchIndexResponseTypeDef,
    SetDefaultAuthorizerResponseTypeDef,
    StartAuditMitigationActionsTaskResponseTypeDef,
    StartOnDemandAuditTaskResponseTypeDef,
    StartThingRegistrationTaskResponseTypeDef,
    StreamFileTypeDef,
    TagTypeDef,
    TestAuthorizationResponseTypeDef,
    TestInvokeAuthorizerResponseTypeDef,
    ThingGroupIndexingConfigurationTypeDef,
    ThingGroupPropertiesTypeDef,
    ThingIndexingConfigurationTypeDef,
    ThingTypePropertiesTypeDef,
    TimeoutConfigTypeDef,
    TlsContextTypeDef,
    TopicRuleDestinationConfigurationTypeDef,
    TopicRulePayloadTypeDef,
    TransferCertificateResponseTypeDef,
    UpdateAuthorizerResponseTypeDef,
    UpdateBillingGroupResponseTypeDef,
    UpdateDomainConfigurationResponseTypeDef,
    UpdateDynamicThingGroupResponseTypeDef,
    UpdateMitigationActionResponseTypeDef,
    UpdateRoleAliasResponseTypeDef,
    UpdateScheduledAuditResponseTypeDef,
    UpdateSecurityProfileResponseTypeDef,
    UpdateStreamResponseTypeDef,
    UpdateThingGroupResponseTypeDef,
    ValidateSecurityProfileBehaviorsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTClient",)


class IoTClient(BaseClient):
    """
    [IoT.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_certificate_transfer(self, certificateId: str, setAsActive: bool = None) -> None:
        """
        [Client.accept_certificate_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.accept_certificate_transfer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_thing_to_billing_group(
        self,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.add_thing_to_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.add_thing_to_billing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_thing_to_thing_group(
        self,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
        overrideDynamicGroups: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.add_thing_to_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.add_thing_to_thing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_targets_with_job(
        self, targets: List[str], jobId: str, comment: str = None
    ) -> AssociateTargetsWithJobResponseTypeDef:
        """
        [Client.associate_targets_with_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.associate_targets_with_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(self, policyName: str, target: str) -> None:
        """
        [Client.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.attach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_principal_policy(self, policyName: str, principal: str) -> None:
        """
        [Client.attach_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.attach_principal_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_security_profile(
        self, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        """
        [Client.attach_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.attach_security_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_thing_principal(self, thingName: str, principal: str) -> Dict[str, Any]:
        """
        [Client.attach_thing_principal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.attach_thing_principal)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_audit_mitigation_actions_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Client.cancel_audit_mitigation_actions_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.cancel_audit_mitigation_actions_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_audit_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Client.cancel_audit_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.cancel_audit_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_certificate_transfer(self, certificateId: str) -> None:
        """
        [Client.cancel_certificate_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.cancel_certificate_transfer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_job(
        self, jobId: str, reasonCode: str = None, comment: str = None, force: bool = None
    ) -> CancelJobResponseTypeDef:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.cancel_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_job_execution(
        self,
        jobId: str,
        thingName: str,
        force: bool = None,
        expectedVersion: int = None,
        statusDetails: Dict[str, str] = None,
    ) -> None:
        """
        [Client.cancel_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.cancel_job_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def clear_default_authorizer(self) -> Dict[str, Any]:
        """
        [Client.clear_default_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.clear_default_authorizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_topic_rule_destination(self, confirmationToken: str) -> Dict[str, Any]:
        """
        [Client.confirm_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.confirm_topic_rule_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: str,
        tokenKeyName: str = None,
        tokenSigningPublicKeys: Dict[str, str] = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
        signingDisabled: bool = None,
    ) -> CreateAuthorizerResponseTypeDef:
        """
        [Client.create_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_authorizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: BillingGroupPropertiesTypeDef = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateBillingGroupResponseTypeDef:
        """
        [Client.create_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_billing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_certificate_from_csr(
        self, certificateSigningRequest: str, setAsActive: bool = None
    ) -> CreateCertificateFromCsrResponseTypeDef:
        """
        [Client.create_certificate_from_csr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_certificate_from_csr)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_domain_configuration(
        self,
        domainConfigurationName: str,
        domainName: str = None,
        serverCertificateArns: List[str] = None,
        validationCertificateArn: str = None,
        authorizerConfig: AuthorizerConfigTypeDef = None,
        serviceType: Literal["DATA", "CREDENTIAL_PROVIDER", "JOBS"] = None,
    ) -> CreateDomainConfigurationResponseTypeDef:
        """
        [Client.create_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_domain_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dynamic_thing_group(
        self,
        thingGroupName: str,
        queryString: str,
        thingGroupProperties: ThingGroupPropertiesTypeDef = None,
        indexName: str = None,
        queryVersion: str = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateDynamicThingGroupResponseTypeDef:
        """
        [Client.create_dynamic_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_dynamic_thing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_job(
        self,
        jobId: str,
        targets: List[str],
        documentSource: str = None,
        document: str = None,
        description: str = None,
        presignedUrlConfig: PresignedUrlConfigTypeDef = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        jobExecutionsRolloutConfig: JobExecutionsRolloutConfigTypeDef = None,
        abortConfig: AbortConfigTypeDef = None,
        timeoutConfig: TimeoutConfigTypeDef = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_keys_and_certificate(
        self, setAsActive: bool = None
    ) -> CreateKeysAndCertificateResponseTypeDef:
        """
        [Client.create_keys_and_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_keys_and_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_mitigation_action(
        self,
        actionName: str,
        roleArn: str,
        actionParams: MitigationActionParamsTypeDef,
        tags: List[TagTypeDef] = None,
    ) -> CreateMitigationActionResponseTypeDef:
        """
        [Client.create_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_mitigation_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_ota_update(
        self,
        otaUpdateId: str,
        targets: List[str],
        files: List[OTAUpdateFileTypeDef],
        roleArn: str,
        description: str = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        awsJobExecutionsRolloutConfig: AwsJobExecutionsRolloutConfigTypeDef = None,
        additionalParameters: Dict[str, str] = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateOTAUpdateResponseTypeDef:
        """
        [Client.create_ota_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_ota_update)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy(self, policyName: str, policyDocument: str) -> CreatePolicyResponseTypeDef:
        """
        [Client.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy_version(
        self, policyName: str, policyDocument: str, setAsDefault: bool = None
    ) -> CreatePolicyVersionResponseTypeDef:
        """
        [Client.create_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_policy_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_provisioning_claim(
        self, templateName: str
    ) -> CreateProvisioningClaimResponseTypeDef:
        """
        [Client.create_provisioning_claim documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_provisioning_claim)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_provisioning_template(
        self,
        templateName: str,
        templateBody: str,
        provisioningRoleArn: str,
        description: str = None,
        enabled: bool = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateProvisioningTemplateResponseTypeDef:
        """
        [Client.create_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_provisioning_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_provisioning_template_version(
        self, templateName: str, templateBody: str, setAsDefault: bool = None
    ) -> CreateProvisioningTemplateVersionResponseTypeDef:
        """
        [Client.create_provisioning_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_provisioning_template_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_role_alias(
        self, roleAlias: str, roleArn: str, credentialDurationSeconds: int = None
    ) -> CreateRoleAliasResponseTypeDef:
        """
        [Client.create_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_role_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_scheduled_audit(
        self,
        frequency: Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"],
        targetCheckNames: List[str],
        scheduledAuditName: str,
        dayOfMonth: str = None,
        dayOfWeek: Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"] = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateScheduledAuditResponseTypeDef:
        """
        [Client.create_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_scheduled_audit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List[BehaviorTypeDef] = None,
        alertTargets: Dict[Literal["SNS"], AlertTargetTypeDef] = None,
        additionalMetricsToRetain: List[str] = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateSecurityProfileResponseTypeDef:
        """
        [Client.create_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_security_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stream(
        self,
        streamId: str,
        files: List[StreamFileTypeDef],
        roleArn: str,
        description: str = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateStreamResponseTypeDef:
        """
        [Client.create_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_thing(
        self,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: AttributePayloadTypeDef = None,
        billingGroupName: str = None,
    ) -> CreateThingResponseTypeDef:
        """
        [Client.create_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_thing)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_thing_group(
        self,
        thingGroupName: str,
        parentGroupName: str = None,
        thingGroupProperties: ThingGroupPropertiesTypeDef = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateThingGroupResponseTypeDef:
        """
        [Client.create_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_thing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_thing_type(
        self,
        thingTypeName: str,
        thingTypeProperties: ThingTypePropertiesTypeDef = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateThingTypeResponseTypeDef:
        """
        [Client.create_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_thing_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_topic_rule(
        self, ruleName: str, topicRulePayload: TopicRulePayloadTypeDef, tags: str = None
    ) -> None:
        """
        [Client.create_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_topic_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_topic_rule_destination(
        self, destinationConfiguration: TopicRuleDestinationConfigurationTypeDef
    ) -> CreateTopicRuleDestinationResponseTypeDef:
        """
        [Client.create_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.create_topic_rule_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_account_audit_configuration(
        self, deleteScheduledAudits: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_account_audit_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_account_audit_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_authorizer(self, authorizerName: str) -> Dict[str, Any]:
        """
        [Client.delete_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_authorizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_billing_group(
        self, billingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_billing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_ca_certificate(self, certificateId: str) -> Dict[str, Any]:
        """
        [Client.delete_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_ca_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_certificate(self, certificateId: str, forceDelete: bool = None) -> None:
        """
        [Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_domain_configuration(self, domainConfigurationName: str) -> Dict[str, Any]:
        """
        [Client.delete_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_domain_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dynamic_thing_group(
        self, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_dynamic_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_dynamic_thing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_job(self, jobId: str, force: bool = None) -> None:
        """
        [Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_job_execution(
        self, jobId: str, thingName: str, executionNumber: int, force: bool = None
    ) -> None:
        """
        [Client.delete_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_job_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_mitigation_action(self, actionName: str) -> Dict[str, Any]:
        """
        [Client.delete_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_mitigation_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_ota_update(
        self, otaUpdateId: str, deleteStream: bool = None, forceDeleteAWSJob: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_ota_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_ota_update)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_policy(self, policyName: str) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_policy_version(self, policyName: str, policyVersionId: str) -> None:
        """
        [Client.delete_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_policy_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_provisioning_template(self, templateName: str) -> Dict[str, Any]:
        """
        [Client.delete_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_provisioning_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_provisioning_template_version(
        self, templateName: str, versionId: int
    ) -> Dict[str, Any]:
        """
        [Client.delete_provisioning_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_provisioning_template_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_registration_code(self) -> Dict[str, Any]:
        """
        [Client.delete_registration_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_registration_code)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_role_alias(self, roleAlias: str) -> Dict[str, Any]:
        """
        [Client.delete_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_role_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_scheduled_audit(self, scheduledAuditName: str) -> Dict[str, Any]:
        """
        [Client.delete_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_scheduled_audit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_security_profile(
        self, securityProfileName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_security_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_stream(self, streamId: str) -> Dict[str, Any]:
        """
        [Client.delete_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_thing(self, thingName: str, expectedVersion: int = None) -> Dict[str, Any]:
        """
        [Client.delete_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_thing)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_thing_group(
        self, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_thing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_thing_type(self, thingTypeName: str) -> Dict[str, Any]:
        """
        [Client.delete_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_thing_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_topic_rule(self, ruleName: str) -> None:
        """
        [Client.delete_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_topic_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_topic_rule_destination(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_topic_rule_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_v2_logging_level(
        self, targetType: Literal["DEFAULT", "THING_GROUP"], targetName: str
    ) -> None:
        """
        [Client.delete_v2_logging_level documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.delete_v2_logging_level)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deprecate_thing_type(
        self, thingTypeName: str, undoDeprecate: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.deprecate_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.deprecate_thing_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_audit_configuration(
        self,
    ) -> DescribeAccountAuditConfigurationResponseTypeDef:
        """
        [Client.describe_account_audit_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_account_audit_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_audit_finding(self, findingId: str) -> DescribeAuditFindingResponseTypeDef:
        """
        [Client.describe_audit_finding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_audit_finding)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_audit_mitigation_actions_task(
        self, taskId: str
    ) -> DescribeAuditMitigationActionsTaskResponseTypeDef:
        """
        [Client.describe_audit_mitigation_actions_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_audit_mitigation_actions_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_audit_task(self, taskId: str) -> DescribeAuditTaskResponseTypeDef:
        """
        [Client.describe_audit_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_audit_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_authorizer(self, authorizerName: str) -> DescribeAuthorizerResponseTypeDef:
        """
        [Client.describe_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_authorizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_billing_group(self, billingGroupName: str) -> DescribeBillingGroupResponseTypeDef:
        """
        [Client.describe_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_billing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_ca_certificate(self, certificateId: str) -> DescribeCACertificateResponseTypeDef:
        """
        [Client.describe_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_ca_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_certificate(self, certificateId: str) -> DescribeCertificateResponseTypeDef:
        """
        [Client.describe_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_default_authorizer(self) -> DescribeDefaultAuthorizerResponseTypeDef:
        """
        [Client.describe_default_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_default_authorizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_domain_configuration(
        self, domainConfigurationName: str
    ) -> DescribeDomainConfigurationResponseTypeDef:
        """
        [Client.describe_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_domain_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_endpoint(self, endpointType: str = None) -> DescribeEndpointResponseTypeDef:
        """
        [Client.describe_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_configurations(self) -> DescribeEventConfigurationsResponseTypeDef:
        """
        [Client.describe_event_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_event_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_index(self, indexName: str) -> DescribeIndexResponseTypeDef:
        """
        [Client.describe_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_index)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_job(self, jobId: str) -> DescribeJobResponseTypeDef:
        """
        [Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_job_execution(
        self, jobId: str, thingName: str, executionNumber: int = None
    ) -> DescribeJobExecutionResponseTypeDef:
        """
        [Client.describe_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_job_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_mitigation_action(
        self, actionName: str
    ) -> DescribeMitigationActionResponseTypeDef:
        """
        [Client.describe_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_mitigation_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_provisioning_template(
        self, templateName: str
    ) -> DescribeProvisioningTemplateResponseTypeDef:
        """
        [Client.describe_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_provisioning_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_provisioning_template_version(
        self, templateName: str, versionId: int
    ) -> DescribeProvisioningTemplateVersionResponseTypeDef:
        """
        [Client.describe_provisioning_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_provisioning_template_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_role_alias(self, roleAlias: str) -> DescribeRoleAliasResponseTypeDef:
        """
        [Client.describe_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_role_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scheduled_audit(
        self, scheduledAuditName: str
    ) -> DescribeScheduledAuditResponseTypeDef:
        """
        [Client.describe_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_scheduled_audit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_security_profile(
        self, securityProfileName: str
    ) -> DescribeSecurityProfileResponseTypeDef:
        """
        [Client.describe_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_security_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stream(self, streamId: str) -> DescribeStreamResponseTypeDef:
        """
        [Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_thing(self, thingName: str) -> DescribeThingResponseTypeDef:
        """
        [Client.describe_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_thing)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_thing_group(self, thingGroupName: str) -> DescribeThingGroupResponseTypeDef:
        """
        [Client.describe_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_thing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_thing_registration_task(
        self, taskId: str
    ) -> DescribeThingRegistrationTaskResponseTypeDef:
        """
        [Client.describe_thing_registration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_thing_registration_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_thing_type(self, thingTypeName: str) -> DescribeThingTypeResponseTypeDef:
        """
        [Client.describe_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.describe_thing_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(self, policyName: str, target: str) -> None:
        """
        [Client.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.detach_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_principal_policy(self, policyName: str, principal: str) -> None:
        """
        [Client.detach_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.detach_principal_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_security_profile(
        self, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        """
        [Client.detach_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.detach_security_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_thing_principal(self, thingName: str, principal: str) -> Dict[str, Any]:
        """
        [Client.detach_thing_principal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.detach_thing_principal)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_topic_rule(self, ruleName: str) -> None:
        """
        [Client.disable_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.disable_topic_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_topic_rule(self, ruleName: str) -> None:
        """
        [Client.enable_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.enable_topic_rule)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cardinality(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
    ) -> GetCardinalityResponseTypeDef:
        """
        [Client.get_cardinality documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_cardinality)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_effective_policies(
        self, principal: str = None, cognitoIdentityPoolId: str = None, thingName: str = None
    ) -> GetEffectivePoliciesResponseTypeDef:
        """
        [Client.get_effective_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_effective_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_indexing_configuration(self) -> GetIndexingConfigurationResponseTypeDef:
        """
        [Client.get_indexing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_indexing_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_document(self, jobId: str) -> GetJobDocumentResponseTypeDef:
        """
        [Client.get_job_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_job_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_logging_options(self) -> GetLoggingOptionsResponseTypeDef:
        """
        [Client.get_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_logging_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ota_update(self, otaUpdateId: str) -> GetOTAUpdateResponseTypeDef:
        """
        [Client.get_ota_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_ota_update)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_percentiles(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
        percents: List[float] = None,
    ) -> GetPercentilesResponseTypeDef:
        """
        [Client.get_percentiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_percentiles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_policy(self, policyName: str) -> GetPolicyResponseTypeDef:
        """
        [Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_policy_version(
        self, policyName: str, policyVersionId: str
    ) -> GetPolicyVersionResponseTypeDef:
        """
        [Client.get_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_policy_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_registration_code(self) -> GetRegistrationCodeResponseTypeDef:
        """
        [Client.get_registration_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_registration_code)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_statistics(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
    ) -> GetStatisticsResponseTypeDef:
        """
        [Client.get_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_statistics)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_topic_rule(self, ruleName: str) -> GetTopicRuleResponseTypeDef:
        """
        [Client.get_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_topic_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_topic_rule_destination(self, arn: str) -> GetTopicRuleDestinationResponseTypeDef:
        """
        [Client.get_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_topic_rule_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_v2_logging_options(self) -> GetV2LoggingOptionsResponseTypeDef:
        """
        [Client.get_v2_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.get_v2_logging_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_active_violations(
        self,
        thingName: str = None,
        securityProfileName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListActiveViolationsResponseTypeDef:
        """
        [Client.list_active_violations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_active_violations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_attached_policies(
        self, target: str, recursive: bool = None, marker: str = None, pageSize: int = None
    ) -> ListAttachedPoliciesResponseTypeDef:
        """
        [Client.list_attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_attached_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_audit_findings(
        self,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: ResourceIdentifierTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> ListAuditFindingsResponseTypeDef:
        """
        [Client.list_audit_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_audit_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_audit_mitigation_actions_executions(
        self,
        taskId: str,
        findingId: str,
        actionStatus: Literal[
            "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED", "SKIPPED", "PENDING"
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListAuditMitigationActionsExecutionsResponseTypeDef:
        """
        [Client.list_audit_mitigation_actions_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_audit_mitigation_actions_executions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_audit_mitigation_actions_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        auditTaskId: str = None,
        findingId: str = None,
        taskStatus: Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListAuditMitigationActionsTasksResponseTypeDef:
        """
        [Client.list_audit_mitigation_actions_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_audit_mitigation_actions_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_audit_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"] = None,
        taskStatus: Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAuditTasksResponseTypeDef:
        """
        [Client.list_audit_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_audit_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_authorizers(
        self,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
    ) -> ListAuthorizersResponseTypeDef:
        """
        [Client.list_authorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_authorizers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_billing_groups(
        self, nextToken: str = None, maxResults: int = None, namePrefixFilter: str = None
    ) -> ListBillingGroupsResponseTypeDef:
        """
        [Client.list_billing_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_billing_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_ca_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListCACertificatesResponseTypeDef:
        """
        [Client.list_ca_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_ca_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListCertificatesResponseTypeDef:
        """
        [Client.list_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_certificates_by_ca(
        self,
        caCertificateId: str,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None,
    ) -> ListCertificatesByCAResponseTypeDef:
        """
        [Client.list_certificates_by_ca documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_certificates_by_ca)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_domain_configurations(
        self,
        marker: str = None,
        pageSize: int = None,
        serviceType: Literal["DATA", "CREDENTIAL_PROVIDER", "JOBS"] = None,
    ) -> ListDomainConfigurationsResponseTypeDef:
        """
        [Client.list_domain_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_domain_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_indices(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListIndicesResponseTypeDef:
        """
        [Client.list_indices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_indices)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_job_executions_for_job(
        self,
        jobId: str,
        status: Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListJobExecutionsForJobResponseTypeDef:
        """
        [Client.list_job_executions_for_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_job_executions_for_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_job_executions_for_thing(
        self,
        thingName: str,
        status: Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListJobExecutionsForThingResponseTypeDef:
        """
        [Client.list_job_executions_for_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_job_executions_for_thing)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(
        self,
        status: Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"] = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        maxResults: int = None,
        nextToken: str = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
    ) -> ListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_mitigation_actions(
        self,
        actionType: Literal[
            "UPDATE_DEVICE_CERTIFICATE",
            "UPDATE_CA_CERTIFICATE",
            "ADD_THINGS_TO_THING_GROUP",
            "REPLACE_DEFAULT_POLICY_VERSION",
            "ENABLE_IOT_LOGGING",
            "PUBLISH_FINDING_TO_SNS",
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListMitigationActionsResponseTypeDef:
        """
        [Client.list_mitigation_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_mitigation_actions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_ota_updates(
        self,
        maxResults: int = None,
        nextToken: str = None,
        otaUpdateStatus: Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"
        ] = None,
    ) -> ListOTAUpdatesResponseTypeDef:
        """
        [Client.list_ota_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_ota_updates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_outgoing_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListOutgoingCertificatesResponseTypeDef:
        """
        [Client.list_outgoing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_outgoing_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_policies(
        self, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ListPoliciesResponseTypeDef:
        """
        [Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_policy_principals(
        self, policyName: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ListPolicyPrincipalsResponseTypeDef:
        """
        [Client.list_policy_principals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_policy_principals)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_policy_versions(self, policyName: str) -> ListPolicyVersionsResponseTypeDef:
        """
        [Client.list_policy_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_policy_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_principal_policies(
        self, principal: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ListPrincipalPoliciesResponseTypeDef:
        """
        [Client.list_principal_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_principal_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_principal_things(
        self, principal: str, nextToken: str = None, maxResults: int = None
    ) -> ListPrincipalThingsResponseTypeDef:
        """
        [Client.list_principal_things documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_principal_things)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_provisioning_template_versions(
        self, templateName: str, maxResults: int = None, nextToken: str = None
    ) -> ListProvisioningTemplateVersionsResponseTypeDef:
        """
        [Client.list_provisioning_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_provisioning_template_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_provisioning_templates(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListProvisioningTemplatesResponseTypeDef:
        """
        [Client.list_provisioning_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_provisioning_templates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_role_aliases(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListRoleAliasesResponseTypeDef:
        """
        [Client.list_role_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_role_aliases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_scheduled_audits(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListScheduledAuditsResponseTypeDef:
        """
        [Client.list_scheduled_audits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_scheduled_audits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_security_profiles(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListSecurityProfilesResponseTypeDef:
        """
        [Client.list_security_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_security_profiles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_security_profiles_for_target(
        self,
        securityProfileTargetArn: str,
        nextToken: str = None,
        maxResults: int = None,
        recursive: bool = None,
    ) -> ListSecurityProfilesForTargetResponseTypeDef:
        """
        [Client.list_security_profiles_for_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_security_profiles_for_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_streams(
        self, maxResults: int = None, nextToken: str = None, ascendingOrder: bool = None
    ) -> ListStreamsResponseTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_streams)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_targets_for_policy(
        self, policyName: str, marker: str = None, pageSize: int = None
    ) -> ListTargetsForPolicyResponseTypeDef:
        """
        [Client.list_targets_for_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_targets_for_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_targets_for_security_profile(
        self, securityProfileName: str, nextToken: str = None, maxResults: int = None
    ) -> ListTargetsForSecurityProfileResponseTypeDef:
        """
        [Client.list_targets_for_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_targets_for_security_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_thing_groups(
        self,
        nextToken: str = None,
        maxResults: int = None,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None,
    ) -> ListThingGroupsResponseTypeDef:
        """
        [Client.list_thing_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_thing_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_thing_groups_for_thing(
        self, thingName: str, nextToken: str = None, maxResults: int = None
    ) -> ListThingGroupsForThingResponseTypeDef:
        """
        [Client.list_thing_groups_for_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_thing_groups_for_thing)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_thing_principals(self, thingName: str) -> ListThingPrincipalsResponseTypeDef:
        """
        [Client.list_thing_principals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_thing_principals)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_thing_registration_task_reports(
        self,
        taskId: str,
        reportType: Literal["ERRORS", "RESULTS"],
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListThingRegistrationTaskReportsResponseTypeDef:
        """
        [Client.list_thing_registration_task_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_thing_registration_task_reports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_thing_registration_tasks(
        self,
        nextToken: str = None,
        maxResults: int = None,
        status: Literal["InProgress", "Completed", "Failed", "Cancelled", "Cancelling"] = None,
    ) -> ListThingRegistrationTasksResponseTypeDef:
        """
        [Client.list_thing_registration_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_thing_registration_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_thing_types(
        self, nextToken: str = None, maxResults: int = None, thingTypeName: str = None
    ) -> ListThingTypesResponseTypeDef:
        """
        [Client.list_thing_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_thing_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_things(
        self,
        nextToken: str = None,
        maxResults: int = None,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
    ) -> ListThingsResponseTypeDef:
        """
        [Client.list_things documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_things)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_things_in_billing_group(
        self, billingGroupName: str, nextToken: str = None, maxResults: int = None
    ) -> ListThingsInBillingGroupResponseTypeDef:
        """
        [Client.list_things_in_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_things_in_billing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_things_in_thing_group(
        self,
        thingGroupName: str,
        recursive: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListThingsInThingGroupResponseTypeDef:
        """
        [Client.list_things_in_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_things_in_thing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_topic_rule_destinations(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListTopicRuleDestinationsResponseTypeDef:
        """
        [Client.list_topic_rule_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_topic_rule_destinations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_topic_rules(
        self,
        topic: str = None,
        maxResults: int = None,
        nextToken: str = None,
        ruleDisabled: bool = None,
    ) -> ListTopicRulesResponseTypeDef:
        """
        [Client.list_topic_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_topic_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_v2_logging_levels(
        self,
        targetType: Literal["DEFAULT", "THING_GROUP"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListV2LoggingLevelsResponseTypeDef:
        """
        [Client.list_v2_logging_levels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_v2_logging_levels)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_violation_events(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: str = None,
        securityProfileName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListViolationEventsResponseTypeDef:
        """
        [Client.list_violation_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.list_violation_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_ca_certificate(
        self,
        caCertificate: str,
        verificationCertificate: str,
        setAsActive: bool = None,
        allowAutoRegistration: bool = None,
        registrationConfig: RegistrationConfigTypeDef = None,
    ) -> RegisterCACertificateResponseTypeDef:
        """
        [Client.register_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.register_ca_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_certificate(
        self,
        certificatePem: str,
        caCertificatePem: str = None,
        setAsActive: bool = None,
        status: Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ] = None,
    ) -> RegisterCertificateResponseTypeDef:
        """
        [Client.register_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.register_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_thing(
        self, templateBody: str, parameters: Dict[str, str] = None
    ) -> RegisterThingResponseTypeDef:
        """
        [Client.register_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.register_thing)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_certificate_transfer(self, certificateId: str, rejectReason: str = None) -> None:
        """
        [Client.reject_certificate_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.reject_certificate_transfer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_thing_from_billing_group(
        self,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.remove_thing_from_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.remove_thing_from_billing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_thing_from_thing_group(
        self,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.remove_thing_from_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.remove_thing_from_thing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_topic_rule(self, ruleName: str, topicRulePayload: TopicRulePayloadTypeDef) -> None:
        """
        [Client.replace_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.replace_topic_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_index(
        self,
        queryString: str,
        indexName: str = None,
        nextToken: str = None,
        maxResults: int = None,
        queryVersion: str = None,
    ) -> SearchIndexResponseTypeDef:
        """
        [Client.search_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.search_index)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_default_authorizer(self, authorizerName: str) -> SetDefaultAuthorizerResponseTypeDef:
        """
        [Client.set_default_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.set_default_authorizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_default_policy_version(self, policyName: str, policyVersionId: str) -> None:
        """
        [Client.set_default_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.set_default_policy_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_logging_options(self, loggingOptionsPayload: LoggingOptionsPayloadTypeDef) -> None:
        """
        [Client.set_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.set_logging_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_v2_logging_level(
        self,
        logTarget: LogTargetTypeDef,
        logLevel: Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"],
    ) -> None:
        """
        [Client.set_v2_logging_level documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.set_v2_logging_level)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_v2_logging_options(
        self,
        roleArn: str = None,
        defaultLogLevel: Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"] = None,
        disableAllLogs: bool = None,
    ) -> None:
        """
        [Client.set_v2_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.set_v2_logging_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_audit_mitigation_actions_task(
        self,
        taskId: str,
        target: AuditMitigationActionsTaskTargetTypeDef,
        auditCheckToActionsMapping: Dict[str, List[str]],
        clientRequestToken: str,
    ) -> StartAuditMitigationActionsTaskResponseTypeDef:
        """
        [Client.start_audit_mitigation_actions_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.start_audit_mitigation_actions_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_on_demand_audit_task(
        self, targetCheckNames: List[str]
    ) -> StartOnDemandAuditTaskResponseTypeDef:
        """
        [Client.start_on_demand_audit_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.start_on_demand_audit_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_thing_registration_task(
        self, templateBody: str, inputFileBucket: str, inputFileKey: str, roleArn: str
    ) -> StartThingRegistrationTaskResponseTypeDef:
        """
        [Client.start_thing_registration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.start_thing_registration_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_thing_registration_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Client.stop_thing_registration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.stop_thing_registration_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def test_authorization(
        self,
        authInfos: List[AuthInfoTypeDef],
        principal: str = None,
        cognitoIdentityPoolId: str = None,
        clientId: str = None,
        policyNamesToAdd: List[str] = None,
        policyNamesToSkip: List[str] = None,
    ) -> TestAuthorizationResponseTypeDef:
        """
        [Client.test_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.test_authorization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def test_invoke_authorizer(
        self,
        authorizerName: str,
        token: str = None,
        tokenSignature: str = None,
        httpContext: HttpContextTypeDef = None,
        mqttContext: MqttContextTypeDef = None,
        tlsContext: TlsContextTypeDef = None,
    ) -> TestInvokeAuthorizerResponseTypeDef:
        """
        [Client.test_invoke_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.test_invoke_authorizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def transfer_certificate(
        self, certificateId: str, targetAwsAccount: str, transferMessage: str = None
    ) -> TransferCertificateResponseTypeDef:
        """
        [Client.transfer_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.transfer_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_account_audit_configuration(
        self,
        roleArn: str = None,
        auditNotificationTargetConfigurations: Dict[
            Literal["SNS"], AuditNotificationTargetTypeDef
        ] = None,
        auditCheckConfigurations: Dict[str, AuditCheckConfigurationTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_account_audit_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_account_audit_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: str = None,
        tokenKeyName: str = None,
        tokenSigningPublicKeys: Dict[str, str] = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
    ) -> UpdateAuthorizerResponseTypeDef:
        """
        [Client.update_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_authorizer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: BillingGroupPropertiesTypeDef,
        expectedVersion: int = None,
    ) -> UpdateBillingGroupResponseTypeDef:
        """
        [Client.update_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_billing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_ca_certificate(
        self,
        certificateId: str,
        newStatus: Literal["ACTIVE", "INACTIVE"] = None,
        newAutoRegistrationStatus: Literal["ENABLE", "DISABLE"] = None,
        registrationConfig: RegistrationConfigTypeDef = None,
        removeAutoRegistration: bool = None,
    ) -> None:
        """
        [Client.update_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_ca_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_certificate(
        self,
        certificateId: str,
        newStatus: Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
    ) -> None:
        """
        [Client.update_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_domain_configuration(
        self,
        domainConfigurationName: str,
        authorizerConfig: AuthorizerConfigTypeDef = None,
        domainConfigurationStatus: Literal["ENABLED", "DISABLED"] = None,
        removeAuthorizerConfig: bool = None,
    ) -> UpdateDomainConfigurationResponseTypeDef:
        """
        [Client.update_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_domain_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_dynamic_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: ThingGroupPropertiesTypeDef,
        expectedVersion: int = None,
        indexName: str = None,
        queryString: str = None,
        queryVersion: str = None,
    ) -> UpdateDynamicThingGroupResponseTypeDef:
        """
        [Client.update_dynamic_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_dynamic_thing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_event_configurations(
        self,
        eventConfigurations: Dict[
            Literal[
                "THING",
                "THING_GROUP",
                "THING_TYPE",
                "THING_GROUP_MEMBERSHIP",
                "THING_GROUP_HIERARCHY",
                "THING_TYPE_ASSOCIATION",
                "JOB",
                "JOB_EXECUTION",
                "POLICY",
                "CERTIFICATE",
                "CA_CERTIFICATE",
            ],
            ConfigurationTypeDef,
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_event_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_event_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_indexing_configuration(
        self,
        thingIndexingConfiguration: ThingIndexingConfigurationTypeDef = None,
        thingGroupIndexingConfiguration: ThingGroupIndexingConfigurationTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_indexing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_indexing_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_job(
        self,
        jobId: str,
        description: str = None,
        presignedUrlConfig: PresignedUrlConfigTypeDef = None,
        jobExecutionsRolloutConfig: JobExecutionsRolloutConfigTypeDef = None,
        abortConfig: AbortConfigTypeDef = None,
        timeoutConfig: TimeoutConfigTypeDef = None,
    ) -> None:
        """
        [Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_mitigation_action(
        self,
        actionName: str,
        roleArn: str = None,
        actionParams: MitigationActionParamsTypeDef = None,
    ) -> UpdateMitigationActionResponseTypeDef:
        """
        [Client.update_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_mitigation_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_provisioning_template(
        self,
        templateName: str,
        description: str = None,
        enabled: bool = None,
        defaultVersionId: int = None,
        provisioningRoleArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_provisioning_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_role_alias(
        self, roleAlias: str, roleArn: str = None, credentialDurationSeconds: int = None
    ) -> UpdateRoleAliasResponseTypeDef:
        """
        [Client.update_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_role_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_scheduled_audit(
        self,
        scheduledAuditName: str,
        frequency: Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"] = None,
        dayOfMonth: str = None,
        dayOfWeek: Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"] = None,
        targetCheckNames: List[str] = None,
    ) -> UpdateScheduledAuditResponseTypeDef:
        """
        [Client.update_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_scheduled_audit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List[BehaviorTypeDef] = None,
        alertTargets: Dict[Literal["SNS"], AlertTargetTypeDef] = None,
        additionalMetricsToRetain: List[str] = None,
        deleteBehaviors: bool = None,
        deleteAlertTargets: bool = None,
        deleteAdditionalMetricsToRetain: bool = None,
        expectedVersion: int = None,
    ) -> UpdateSecurityProfileResponseTypeDef:
        """
        [Client.update_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_security_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_stream(
        self,
        streamId: str,
        description: str = None,
        files: List[StreamFileTypeDef] = None,
        roleArn: str = None,
    ) -> UpdateStreamResponseTypeDef:
        """
        [Client.update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_thing(
        self,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: AttributePayloadTypeDef = None,
        expectedVersion: int = None,
        removeThingType: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_thing)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: ThingGroupPropertiesTypeDef,
        expectedVersion: int = None,
    ) -> UpdateThingGroupResponseTypeDef:
        """
        [Client.update_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_thing_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_thing_groups_for_thing(
        self,
        thingName: str = None,
        thingGroupsToAdd: List[str] = None,
        thingGroupsToRemove: List[str] = None,
        overrideDynamicGroups: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_thing_groups_for_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_thing_groups_for_thing)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_topic_rule_destination(
        self, arn: str, status: Literal["ENABLED", "IN_PROGRESS", "DISABLED", "ERROR"]
    ) -> Dict[str, Any]:
        """
        [Client.update_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.update_topic_rule_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def validate_security_profile_behaviors(
        self, behaviors: List[BehaviorTypeDef]
    ) -> ValidateSecurityProfileBehaviorsResponseTypeDef:
        """
        [Client.validate_security_profile_behaviors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Client.validate_security_profile_behaviors)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_active_violations"]
    ) -> paginator_scope.ListActiveViolationsPaginator:
        """
        [Paginator.ListActiveViolations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListActiveViolations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_attached_policies"]
    ) -> paginator_scope.ListAttachedPoliciesPaginator:
        """
        [Paginator.ListAttachedPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_audit_findings"]
    ) -> paginator_scope.ListAuditFindingsPaginator:
        """
        [Paginator.ListAuditFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListAuditFindings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_audit_tasks"]
    ) -> paginator_scope.ListAuditTasksPaginator:
        """
        [Paginator.ListAuditTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListAuditTasks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_authorizers"]
    ) -> paginator_scope.ListAuthorizersPaginator:
        """
        [Paginator.ListAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListAuthorizers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_billing_groups"]
    ) -> paginator_scope.ListBillingGroupsPaginator:
        """
        [Paginator.ListBillingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListBillingGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_ca_certificates"]
    ) -> paginator_scope.ListCACertificatesPaginator:
        """
        [Paginator.ListCACertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListCACertificates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> paginator_scope.ListCertificatesPaginator:
        """
        [Paginator.ListCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListCertificates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_certificates_by_ca"]
    ) -> paginator_scope.ListCertificatesByCAPaginator:
        """
        [Paginator.ListCertificatesByCA documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_indices"]
    ) -> paginator_scope.ListIndicesPaginator:
        """
        [Paginator.ListIndices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListIndices)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_job_executions_for_job"]
    ) -> paginator_scope.ListJobExecutionsForJobPaginator:
        """
        [Paginator.ListJobExecutionsForJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_job_executions_for_thing"]
    ) -> paginator_scope.ListJobExecutionsForThingPaginator:
        """
        [Paginator.ListJobExecutionsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> paginator_scope.ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_ota_updates"]
    ) -> paginator_scope.ListOTAUpdatesPaginator:
        """
        [Paginator.ListOTAUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListOTAUpdates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_outgoing_certificates"]
    ) -> paginator_scope.ListOutgoingCertificatesPaginator:
        """
        [Paginator.ListOutgoingCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_policies"]
    ) -> paginator_scope.ListPoliciesPaginator:
        """
        [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListPolicies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_policy_principals"]
    ) -> paginator_scope.ListPolicyPrincipalsPaginator:
        """
        [Paginator.ListPolicyPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_principal_policies"]
    ) -> paginator_scope.ListPrincipalPoliciesPaginator:
        """
        [Paginator.ListPrincipalPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_principal_things"]
    ) -> paginator_scope.ListPrincipalThingsPaginator:
        """
        [Paginator.ListPrincipalThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListPrincipalThings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_role_aliases"]
    ) -> paginator_scope.ListRoleAliasesPaginator:
        """
        [Paginator.ListRoleAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListRoleAliases)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_scheduled_audits"]
    ) -> paginator_scope.ListScheduledAuditsPaginator:
        """
        [Paginator.ListScheduledAudits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListScheduledAudits)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_security_profiles"]
    ) -> paginator_scope.ListSecurityProfilesPaginator:
        """
        [Paginator.ListSecurityProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_security_profiles_for_target"]
    ) -> paginator_scope.ListSecurityProfilesForTargetPaginator:
        """
        [Paginator.ListSecurityProfilesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_streams"]
    ) -> paginator_scope.ListStreamsPaginator:
        """
        [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListStreams)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListTagsForResource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> paginator_scope.ListTargetsForPolicyPaginator:
        """
        [Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_targets_for_security_profile"]
    ) -> paginator_scope.ListTargetsForSecurityProfilePaginator:
        """
        [Paginator.ListTargetsForSecurityProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_thing_groups"]
    ) -> paginator_scope.ListThingGroupsPaginator:
        """
        [Paginator.ListThingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListThingGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_thing_groups_for_thing"]
    ) -> paginator_scope.ListThingGroupsForThingPaginator:
        """
        [Paginator.ListThingGroupsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_thing_registration_tasks"]
    ) -> paginator_scope.ListThingRegistrationTasksPaginator:
        """
        [Paginator.ListThingRegistrationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_thing_types"]
    ) -> paginator_scope.ListThingTypesPaginator:
        """
        [Paginator.ListThingTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListThingTypes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_things"]
    ) -> paginator_scope.ListThingsPaginator:
        """
        [Paginator.ListThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListThings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_things_in_billing_group"]
    ) -> paginator_scope.ListThingsInBillingGroupPaginator:
        """
        [Paginator.ListThingsInBillingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_things_in_thing_group"]
    ) -> paginator_scope.ListThingsInThingGroupPaginator:
        """
        [Paginator.ListThingsInThingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_topic_rules"]
    ) -> paginator_scope.ListTopicRulesPaginator:
        """
        [Paginator.ListTopicRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListTopicRules)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_v2_logging_levels"]
    ) -> paginator_scope.ListV2LoggingLevelsPaginator:
        """
        [Paginator.ListV2LoggingLevels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_violation_events"]
    ) -> paginator_scope.ListViolationEventsPaginator:
        """
        [Paginator.ListViolationEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot.html#IoT.Paginator.ListViolationEvents)
        """


class Exceptions:
    CertificateConflictException: Boto3ClientError
    CertificateStateException: Boto3ClientError
    CertificateValidationException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictingResourceUpdateException: Boto3ClientError
    DeleteConflictException: Boto3ClientError
    IndexNotReadyException: Boto3ClientError
    InternalException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidAggregationException: Boto3ClientError
    InvalidQueryException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    InvalidResponseException: Boto3ClientError
    InvalidStateTransitionException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MalformedPolicyException: Boto3ClientError
    NotConfiguredException: Boto3ClientError
    RegistrationCodeValidationException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceRegistrationFailureException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    SqlParseException: Boto3ClientError
    TaskAlreadyExistsException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    TransferAlreadyCompletedException: Boto3ClientError
    TransferConflictException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
    VersionConflictException: Boto3ClientError
    VersionsLimitExceededException: Boto3ClientError
