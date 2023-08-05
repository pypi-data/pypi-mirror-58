"Main interface for inspector service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_inspector.client as client_scope

# pylint: disable=import-self
import mypy_boto3_inspector.paginator as paginator_scope
from mypy_boto3_inspector.type_defs import (
    AddAttributesToFindingsResponseTypeDef,
    AgentFilterTypeDef,
    AssessmentRunFilterTypeDef,
    AssessmentTargetFilterTypeDef,
    AssessmentTemplateFilterTypeDef,
    AttributeTypeDef,
    CreateAssessmentTargetResponseTypeDef,
    CreateAssessmentTemplateResponseTypeDef,
    CreateExclusionsPreviewResponseTypeDef,
    CreateResourceGroupResponseTypeDef,
    DescribeAssessmentRunsResponseTypeDef,
    DescribeAssessmentTargetsResponseTypeDef,
    DescribeAssessmentTemplatesResponseTypeDef,
    DescribeCrossAccountAccessRoleResponseTypeDef,
    DescribeExclusionsResponseTypeDef,
    DescribeFindingsResponseTypeDef,
    DescribeResourceGroupsResponseTypeDef,
    DescribeRulesPackagesResponseTypeDef,
    FindingFilterTypeDef,
    GetAssessmentReportResponseTypeDef,
    GetExclusionsPreviewResponseTypeDef,
    GetTelemetryMetadataResponseTypeDef,
    ListAssessmentRunAgentsResponseTypeDef,
    ListAssessmentRunsResponseTypeDef,
    ListAssessmentTargetsResponseTypeDef,
    ListAssessmentTemplatesResponseTypeDef,
    ListEventSubscriptionsResponseTypeDef,
    ListExclusionsResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListRulesPackagesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PreviewAgentsResponseTypeDef,
    RemoveAttributesFromFindingsResponseTypeDef,
    ResourceGroupTagTypeDef,
    StartAssessmentRunResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("InspectorClient",)


class InspectorClient(BaseClient):
    """
    [Inspector.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_attributes_to_findings(
        self, findingArns: List[str], attributes: List[AttributeTypeDef]
    ) -> AddAttributesToFindingsResponseTypeDef:
        """
        [Client.add_attributes_to_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.add_attributes_to_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_assessment_target(
        self, assessmentTargetName: str, resourceGroupArn: str = None
    ) -> CreateAssessmentTargetResponseTypeDef:
        """
        [Client.create_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.create_assessment_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_assessment_template(
        self,
        assessmentTargetArn: str,
        assessmentTemplateName: str,
        durationInSeconds: int,
        rulesPackageArns: List[str],
        userAttributesForFindings: List[AttributeTypeDef] = None,
    ) -> CreateAssessmentTemplateResponseTypeDef:
        """
        [Client.create_assessment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.create_assessment_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_exclusions_preview(
        self, assessmentTemplateArn: str
    ) -> CreateExclusionsPreviewResponseTypeDef:
        """
        [Client.create_exclusions_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.create_exclusions_preview)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resource_group(
        self, resourceGroupTags: List[ResourceGroupTagTypeDef]
    ) -> CreateResourceGroupResponseTypeDef:
        """
        [Client.create_resource_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.create_resource_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_assessment_run(self, assessmentRunArn: str) -> None:
        """
        [Client.delete_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.delete_assessment_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_assessment_target(self, assessmentTargetArn: str) -> None:
        """
        [Client.delete_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.delete_assessment_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_assessment_template(self, assessmentTemplateArn: str) -> None:
        """
        [Client.delete_assessment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.delete_assessment_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_assessment_runs(
        self, assessmentRunArns: List[str]
    ) -> DescribeAssessmentRunsResponseTypeDef:
        """
        [Client.describe_assessment_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.describe_assessment_runs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_assessment_targets(
        self, assessmentTargetArns: List[str]
    ) -> DescribeAssessmentTargetsResponseTypeDef:
        """
        [Client.describe_assessment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.describe_assessment_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_assessment_templates(
        self, assessmentTemplateArns: List[str]
    ) -> DescribeAssessmentTemplatesResponseTypeDef:
        """
        [Client.describe_assessment_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.describe_assessment_templates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cross_account_access_role(self) -> DescribeCrossAccountAccessRoleResponseTypeDef:
        """
        [Client.describe_cross_account_access_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.describe_cross_account_access_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_exclusions(
        self, exclusionArns: List[str], locale: Literal["EN_US"] = None
    ) -> DescribeExclusionsResponseTypeDef:
        """
        [Client.describe_exclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.describe_exclusions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_findings(
        self, findingArns: List[str], locale: Literal["EN_US"] = None
    ) -> DescribeFindingsResponseTypeDef:
        """
        [Client.describe_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.describe_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_resource_groups(
        self, resourceGroupArns: List[str]
    ) -> DescribeResourceGroupsResponseTypeDef:
        """
        [Client.describe_resource_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.describe_resource_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_rules_packages(
        self, rulesPackageArns: List[str], locale: Literal["EN_US"] = None
    ) -> DescribeRulesPackagesResponseTypeDef:
        """
        [Client.describe_rules_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.describe_rules_packages)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_assessment_report(
        self,
        assessmentRunArn: str,
        reportFileFormat: Literal["HTML", "PDF"],
        reportType: Literal["FINDING", "FULL"],
    ) -> GetAssessmentReportResponseTypeDef:
        """
        [Client.get_assessment_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.get_assessment_report)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_exclusions_preview(
        self,
        assessmentTemplateArn: str,
        previewToken: str,
        nextToken: str = None,
        maxResults: int = None,
        locale: Literal["EN_US"] = None,
    ) -> GetExclusionsPreviewResponseTypeDef:
        """
        [Client.get_exclusions_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.get_exclusions_preview)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_telemetry_metadata(self, assessmentRunArn: str) -> GetTelemetryMetadataResponseTypeDef:
        """
        [Client.get_telemetry_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.get_telemetry_metadata)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_assessment_run_agents(
        self,
        assessmentRunArn: str,
        filter: AgentFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAssessmentRunAgentsResponseTypeDef:
        """
        [Client.list_assessment_run_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.list_assessment_run_agents)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_assessment_runs(
        self,
        assessmentTemplateArns: List[str] = None,
        filter: AssessmentRunFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAssessmentRunsResponseTypeDef:
        """
        [Client.list_assessment_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.list_assessment_runs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_assessment_targets(
        self,
        filter: AssessmentTargetFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAssessmentTargetsResponseTypeDef:
        """
        [Client.list_assessment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.list_assessment_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_assessment_templates(
        self,
        assessmentTargetArns: List[str] = None,
        filter: AssessmentTemplateFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAssessmentTemplatesResponseTypeDef:
        """
        [Client.list_assessment_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.list_assessment_templates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_event_subscriptions(
        self, resourceArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListEventSubscriptionsResponseTypeDef:
        """
        [Client.list_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.list_event_subscriptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_exclusions(
        self, assessmentRunArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListExclusionsResponseTypeDef:
        """
        [Client.list_exclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.list_exclusions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_findings(
        self,
        assessmentRunArns: List[str] = None,
        filter: FindingFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListFindingsResponseTypeDef:
        """
        [Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.list_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_rules_packages(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListRulesPackagesResponseTypeDef:
        """
        [Client.list_rules_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.list_rules_packages)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def preview_agents(
        self, previewAgentsArn: str, nextToken: str = None, maxResults: int = None
    ) -> PreviewAgentsResponseTypeDef:
        """
        [Client.preview_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.preview_agents)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_cross_account_access_role(self, roleArn: str) -> None:
        """
        [Client.register_cross_account_access_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.register_cross_account_access_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_attributes_from_findings(
        self, findingArns: List[str], attributeKeys: List[str]
    ) -> RemoveAttributesFromFindingsResponseTypeDef:
        """
        [Client.remove_attributes_from_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.remove_attributes_from_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_tags_for_resource(self, resourceArn: str, tags: List[TagTypeDef] = None) -> None:
        """
        [Client.set_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.set_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_assessment_run(
        self, assessmentTemplateArn: str, assessmentRunName: str = None
    ) -> StartAssessmentRunResponseTypeDef:
        """
        [Client.start_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.start_assessment_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_assessment_run(
        self,
        assessmentRunArn: str,
        stopAction: Literal["START_EVALUATION", "SKIP_EVALUATION"] = None,
    ) -> None:
        """
        [Client.stop_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.stop_assessment_run)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def subscribe_to_event(
        self,
        resourceArn: str,
        event: Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        topicArn: str,
    ) -> None:
        """
        [Client.subscribe_to_event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.subscribe_to_event)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unsubscribe_from_event(
        self,
        resourceArn: str,
        event: Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        topicArn: str,
    ) -> None:
        """
        [Client.unsubscribe_from_event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.unsubscribe_from_event)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_assessment_target(
        self, assessmentTargetArn: str, assessmentTargetName: str, resourceGroupArn: str = None
    ) -> None:
        """
        [Client.update_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Client.update_assessment_target)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_assessment_run_agents"]
    ) -> paginator_scope.ListAssessmentRunAgentsPaginator:
        """
        [Paginator.ListAssessmentRunAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRunAgents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_assessment_runs"]
    ) -> paginator_scope.ListAssessmentRunsPaginator:
        """
        [Paginator.ListAssessmentRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRuns)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_assessment_targets"]
    ) -> paginator_scope.ListAssessmentTargetsPaginator:
        """
        [Paginator.ListAssessmentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTargets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_assessment_templates"]
    ) -> paginator_scope.ListAssessmentTemplatesPaginator:
        """
        [Paginator.ListAssessmentTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTemplates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_event_subscriptions"]
    ) -> paginator_scope.ListEventSubscriptionsPaginator:
        """
        [Paginator.ListEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Paginator.ListEventSubscriptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_exclusions"]
    ) -> paginator_scope.ListExclusionsPaginator:
        """
        [Paginator.ListExclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Paginator.ListExclusions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_findings"]
    ) -> paginator_scope.ListFindingsPaginator:
        """
        [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Paginator.ListFindings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_rules_packages"]
    ) -> paginator_scope.ListRulesPackagesPaginator:
        """
        [Paginator.ListRulesPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Paginator.ListRulesPackages)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["preview_agents"]
    ) -> paginator_scope.PreviewAgentsPaginator:
        """
        [Paginator.PreviewAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/inspector.html#Inspector.Paginator.PreviewAgents)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AgentsAlreadyRunningAssessmentException: Boto3ClientError
    AssessmentRunInProgressException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidCrossAccountRoleException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NoSuchEntityException: Boto3ClientError
    PreviewGenerationInProgressException: Boto3ClientError
    ServiceTemporarilyUnavailableException: Boto3ClientError
    UnsupportedFeatureException: Boto3ClientError
