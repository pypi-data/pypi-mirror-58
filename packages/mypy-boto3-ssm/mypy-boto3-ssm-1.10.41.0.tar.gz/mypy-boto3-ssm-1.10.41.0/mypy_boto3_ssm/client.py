"Main interface for ssm service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_ssm.client as client_scope

# pylint: disable=import-self
import mypy_boto3_ssm.paginator as paginator_scope
from mypy_boto3_ssm.type_defs import (
    AssociationExecutionFilterTypeDef,
    AssociationExecutionTargetsFilterTypeDef,
    AssociationFilterTypeDef,
    AssociationStatusTypeDef,
    AttachmentsSourceTypeDef,
    AutomationExecutionFilterTypeDef,
    CancelMaintenanceWindowExecutionResultTypeDef,
    CloudWatchOutputConfigTypeDef,
    CommandFilterTypeDef,
    ComplianceExecutionSummaryTypeDef,
    ComplianceItemEntryTypeDef,
    ComplianceStringFilterTypeDef,
    CreateActivationResultTypeDef,
    CreateAssociationBatchRequestEntryTypeDef,
    CreateAssociationBatchResultTypeDef,
    CreateAssociationResultTypeDef,
    CreateDocumentResultTypeDef,
    CreateMaintenanceWindowResultTypeDef,
    CreateOpsItemResponseTypeDef,
    CreatePatchBaselineResultTypeDef,
    DeleteInventoryResultTypeDef,
    DeleteMaintenanceWindowResultTypeDef,
    DeleteParametersResultTypeDef,
    DeletePatchBaselineResultTypeDef,
    DeregisterPatchBaselineForPatchGroupResultTypeDef,
    DeregisterTargetFromMaintenanceWindowResultTypeDef,
    DeregisterTaskFromMaintenanceWindowResultTypeDef,
    DescribeActivationsFilterTypeDef,
    DescribeActivationsResultTypeDef,
    DescribeAssociationExecutionTargetsResultTypeDef,
    DescribeAssociationExecutionsResultTypeDef,
    DescribeAssociationResultTypeDef,
    DescribeAutomationExecutionsResultTypeDef,
    DescribeAutomationStepExecutionsResultTypeDef,
    DescribeAvailablePatchesResultTypeDef,
    DescribeDocumentPermissionResponseTypeDef,
    DescribeDocumentResultTypeDef,
    DescribeEffectiveInstanceAssociationsResultTypeDef,
    DescribeEffectivePatchesForPatchBaselineResultTypeDef,
    DescribeInstanceAssociationsStatusResultTypeDef,
    DescribeInstanceInformationResultTypeDef,
    DescribeInstancePatchStatesForPatchGroupResultTypeDef,
    DescribeInstancePatchStatesResultTypeDef,
    DescribeInstancePatchesResultTypeDef,
    DescribeInventoryDeletionsResultTypeDef,
    DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef,
    DescribeMaintenanceWindowExecutionTasksResultTypeDef,
    DescribeMaintenanceWindowExecutionsResultTypeDef,
    DescribeMaintenanceWindowScheduleResultTypeDef,
    DescribeMaintenanceWindowTargetsResultTypeDef,
    DescribeMaintenanceWindowTasksResultTypeDef,
    DescribeMaintenanceWindowsForTargetResultTypeDef,
    DescribeMaintenanceWindowsResultTypeDef,
    DescribeOpsItemsResponseTypeDef,
    DescribeParametersResultTypeDef,
    DescribePatchBaselinesResultTypeDef,
    DescribePatchGroupStateResultTypeDef,
    DescribePatchGroupsResultTypeDef,
    DescribePatchPropertiesResultTypeDef,
    DescribeSessionsResponseTypeDef,
    DocumentFilterTypeDef,
    DocumentKeyValuesFilterTypeDef,
    DocumentRequiresTypeDef,
    GetAutomationExecutionResultTypeDef,
    GetCalendarStateResponseTypeDef,
    GetCommandInvocationResultTypeDef,
    GetConnectionStatusResponseTypeDef,
    GetDefaultPatchBaselineResultTypeDef,
    GetDeployablePatchSnapshotForInstanceResultTypeDef,
    GetDocumentResultTypeDef,
    GetInventoryResultTypeDef,
    GetInventorySchemaResultTypeDef,
    GetMaintenanceWindowExecutionResultTypeDef,
    GetMaintenanceWindowExecutionTaskInvocationResultTypeDef,
    GetMaintenanceWindowExecutionTaskResultTypeDef,
    GetMaintenanceWindowResultTypeDef,
    GetMaintenanceWindowTaskResultTypeDef,
    GetOpsItemResponseTypeDef,
    GetOpsSummaryResultTypeDef,
    GetParameterHistoryResultTypeDef,
    GetParameterResultTypeDef,
    GetParametersByPathResultTypeDef,
    GetParametersResultTypeDef,
    GetPatchBaselineForPatchGroupResultTypeDef,
    GetPatchBaselineResultTypeDef,
    GetServiceSettingResultTypeDef,
    InstanceAssociationOutputLocationTypeDef,
    InstanceInformationFilterTypeDef,
    InstanceInformationStringFilterTypeDef,
    InstancePatchStateFilterTypeDef,
    InventoryAggregatorTypeDef,
    InventoryFilterTypeDef,
    InventoryItemTypeDef,
    LabelParameterVersionResultTypeDef,
    ListAssociationVersionsResultTypeDef,
    ListAssociationsResultTypeDef,
    ListCommandInvocationsResultTypeDef,
    ListCommandsResultTypeDef,
    ListComplianceItemsResultTypeDef,
    ListComplianceSummariesResultTypeDef,
    ListDocumentVersionsResultTypeDef,
    ListDocumentsResultTypeDef,
    ListInventoryEntriesResultTypeDef,
    ListResourceComplianceSummariesResultTypeDef,
    ListResourceDataSyncResultTypeDef,
    ListTagsForResourceResultTypeDef,
    LoggingInfoTypeDef,
    MaintenanceWindowFilterTypeDef,
    MaintenanceWindowTaskInvocationParametersTypeDef,
    MaintenanceWindowTaskParameterValueExpressionTypeDef,
    NotificationConfigTypeDef,
    OpsAggregatorTypeDef,
    OpsFilterTypeDef,
    OpsItemDataValueTypeDef,
    OpsItemFilterTypeDef,
    OpsItemNotificationTypeDef,
    OpsResultAttributeTypeDef,
    ParameterStringFilterTypeDef,
    ParametersFilterTypeDef,
    PatchFilterGroupTypeDef,
    PatchOrchestratorFilterTypeDef,
    PatchRuleGroupTypeDef,
    PatchSourceTypeDef,
    PutInventoryResultTypeDef,
    PutParameterResultTypeDef,
    RegisterDefaultPatchBaselineResultTypeDef,
    RegisterPatchBaselineForPatchGroupResultTypeDef,
    RegisterTargetWithMaintenanceWindowResultTypeDef,
    RegisterTaskWithMaintenanceWindowResultTypeDef,
    RelatedOpsItemTypeDef,
    ResetServiceSettingResultTypeDef,
    ResourceDataSyncS3DestinationTypeDef,
    ResourceDataSyncSourceTypeDef,
    ResultAttributeTypeDef,
    ResumeSessionResponseTypeDef,
    SendCommandResultTypeDef,
    SessionFilterTypeDef,
    StartAutomationExecutionResultTypeDef,
    StartSessionResponseTypeDef,
    StepExecutionFilterTypeDef,
    TagTypeDef,
    TargetLocationTypeDef,
    TargetTypeDef,
    TerminateSessionResponseTypeDef,
    UpdateAssociationResultTypeDef,
    UpdateAssociationStatusResultTypeDef,
    UpdateDocumentDefaultVersionResultTypeDef,
    UpdateDocumentResultTypeDef,
    UpdateMaintenanceWindowResultTypeDef,
    UpdateMaintenanceWindowTargetResultTypeDef,
    UpdateMaintenanceWindowTaskResultTypeDef,
    UpdatePatchBaselineResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SSMClient",)


class SSMClient(BaseClient):
    """
    [SSM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_resource(
        self,
        ResourceType: Literal[
            "Document",
            "ManagedInstance",
            "MaintenanceWindow",
            "Parameter",
            "PatchBaseline",
            "OpsItem",
        ],
        ResourceId: str,
        Tags: List[TagTypeDef],
    ) -> Dict[str, Any]:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.add_tags_to_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_command(self, CommandId: str, InstanceIds: List[str] = None) -> Dict[str, Any]:
        """
        [Client.cancel_command documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.cancel_command)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_maintenance_window_execution(
        self, WindowExecutionId: str
    ) -> CancelMaintenanceWindowExecutionResultTypeDef:
        """
        [Client.cancel_maintenance_window_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.cancel_maintenance_window_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_activation(
        self,
        IamRole: str,
        Description: str = None,
        DefaultInstanceName: str = None,
        RegistrationLimit: int = None,
        ExpirationDate: datetime = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateActivationResultTypeDef:
        """
        [Client.create_activation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.create_activation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_association(
        self,
        Name: str,
        DocumentVersion: str = None,
        InstanceId: str = None,
        Parameters: Dict[str, List[str]] = None,
        Targets: List[TargetTypeDef] = None,
        ScheduleExpression: str = None,
        OutputLocation: InstanceAssociationOutputLocationTypeDef = None,
        AssociationName: str = None,
        AutomationTargetParameterName: str = None,
        MaxErrors: str = None,
        MaxConcurrency: str = None,
        ComplianceSeverity: Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"] = None,
    ) -> CreateAssociationResultTypeDef:
        """
        [Client.create_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.create_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_association_batch(
        self, Entries: List[CreateAssociationBatchRequestEntryTypeDef]
    ) -> CreateAssociationBatchResultTypeDef:
        """
        [Client.create_association_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.create_association_batch)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_document(
        self,
        Content: str,
        Name: str,
        Requires: List[DocumentRequiresTypeDef] = None,
        Attachments: List[AttachmentsSourceTypeDef] = None,
        VersionName: str = None,
        DocumentType: Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ] = None,
        DocumentFormat: Literal["YAML", "JSON", "TEXT"] = None,
        TargetType: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDocumentResultTypeDef:
        """
        [Client.create_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.create_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_maintenance_window(
        self,
        Name: str,
        Schedule: str,
        Duration: int,
        Cutoff: int,
        AllowUnassociatedTargets: bool,
        Description: str = None,
        StartDate: str = None,
        EndDate: str = None,
        ScheduleTimezone: str = None,
        ClientToken: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateMaintenanceWindowResultTypeDef:
        """
        [Client.create_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.create_maintenance_window)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_ops_item(
        self,
        Description: str,
        Source: str,
        Title: str,
        OperationalData: Dict[str, OpsItemDataValueTypeDef] = None,
        Notifications: List[OpsItemNotificationTypeDef] = None,
        Priority: int = None,
        RelatedOpsItems: List[RelatedOpsItemTypeDef] = None,
        Tags: List[TagTypeDef] = None,
        Category: str = None,
        Severity: str = None,
    ) -> CreateOpsItemResponseTypeDef:
        """
        [Client.create_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.create_ops_item)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_patch_baseline(
        self,
        Name: str,
        OperatingSystem: Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ] = None,
        GlobalFilters: PatchFilterGroupTypeDef = None,
        ApprovalRules: PatchRuleGroupTypeDef = None,
        ApprovedPatches: List[str] = None,
        ApprovedPatchesComplianceLevel: Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ] = None,
        ApprovedPatchesEnableNonSecurity: bool = None,
        RejectedPatches: List[str] = None,
        RejectedPatchesAction: Literal["ALLOW_AS_DEPENDENCY", "BLOCK"] = None,
        Description: str = None,
        Sources: List[PatchSourceTypeDef] = None,
        ClientToken: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreatePatchBaselineResultTypeDef:
        """
        [Client.create_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.create_patch_baseline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resource_data_sync(
        self,
        SyncName: str,
        S3Destination: ResourceDataSyncS3DestinationTypeDef = None,
        SyncType: str = None,
        SyncSource: ResourceDataSyncSourceTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.create_resource_data_sync)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_activation(self, ActivationId: str) -> Dict[str, Any]:
        """
        [Client.delete_activation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.delete_activation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_association(
        self, Name: str = None, InstanceId: str = None, AssociationId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.delete_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_document(
        self, Name: str, DocumentVersion: str = None, VersionName: str = None, Force: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.delete_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_inventory(
        self,
        TypeName: str,
        SchemaDeleteOption: Literal["DisableSchema", "DeleteSchema"] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> DeleteInventoryResultTypeDef:
        """
        [Client.delete_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.delete_inventory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_maintenance_window(self, WindowId: str) -> DeleteMaintenanceWindowResultTypeDef:
        """
        [Client.delete_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.delete_maintenance_window)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_parameter(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.delete_parameter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_parameters(self, Names: List[str]) -> DeleteParametersResultTypeDef:
        """
        [Client.delete_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.delete_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_patch_baseline(self, BaselineId: str) -> DeletePatchBaselineResultTypeDef:
        """
        [Client.delete_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.delete_patch_baseline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource_data_sync(self, SyncName: str, SyncType: str = None) -> Dict[str, Any]:
        """
        [Client.delete_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.delete_resource_data_sync)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_managed_instance(self, InstanceId: str) -> Dict[str, Any]:
        """
        [Client.deregister_managed_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.deregister_managed_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_patch_baseline_for_patch_group(
        self, BaselineId: str, PatchGroup: str
    ) -> DeregisterPatchBaselineForPatchGroupResultTypeDef:
        """
        [Client.deregister_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.deregister_patch_baseline_for_patch_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_target_from_maintenance_window(
        self, WindowId: str, WindowTargetId: str, Safe: bool = None
    ) -> DeregisterTargetFromMaintenanceWindowResultTypeDef:
        """
        [Client.deregister_target_from_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.deregister_target_from_maintenance_window)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_task_from_maintenance_window(
        self, WindowId: str, WindowTaskId: str
    ) -> DeregisterTaskFromMaintenanceWindowResultTypeDef:
        """
        [Client.deregister_task_from_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.deregister_task_from_maintenance_window)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_activations(
        self,
        Filters: List[DescribeActivationsFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeActivationsResultTypeDef:
        """
        [Client.describe_activations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_activations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_association(
        self,
        Name: str = None,
        InstanceId: str = None,
        AssociationId: str = None,
        AssociationVersion: str = None,
    ) -> DescribeAssociationResultTypeDef:
        """
        [Client.describe_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_association_execution_targets(
        self,
        AssociationId: str,
        ExecutionId: str,
        Filters: List[AssociationExecutionTargetsFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeAssociationExecutionTargetsResultTypeDef:
        """
        [Client.describe_association_execution_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_association_execution_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_association_executions(
        self,
        AssociationId: str,
        Filters: List[AssociationExecutionFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeAssociationExecutionsResultTypeDef:
        """
        [Client.describe_association_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_association_executions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_automation_executions(
        self,
        Filters: List[AutomationExecutionFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeAutomationExecutionsResultTypeDef:
        """
        [Client.describe_automation_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_automation_executions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_automation_step_executions(
        self,
        AutomationExecutionId: str,
        Filters: List[StepExecutionFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
        ReverseOrder: bool = None,
    ) -> DescribeAutomationStepExecutionsResultTypeDef:
        """
        [Client.describe_automation_step_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_automation_step_executions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_available_patches(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeAvailablePatchesResultTypeDef:
        """
        [Client.describe_available_patches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_available_patches)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_document(
        self, Name: str, DocumentVersion: str = None, VersionName: str = None
    ) -> DescribeDocumentResultTypeDef:
        """
        [Client.describe_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_document_permission(
        self, Name: str, PermissionType: Literal["Share"]
    ) -> DescribeDocumentPermissionResponseTypeDef:
        """
        [Client.describe_document_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_document_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_effective_instance_associations(
        self, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeEffectiveInstanceAssociationsResultTypeDef:
        """
        [Client.describe_effective_instance_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_effective_instance_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_effective_patches_for_patch_baseline(
        self, BaselineId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeEffectivePatchesForPatchBaselineResultTypeDef:
        """
        [Client.describe_effective_patches_for_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_effective_patches_for_patch_baseline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instance_associations_status(
        self, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeInstanceAssociationsStatusResultTypeDef:
        """
        [Client.describe_instance_associations_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_instance_associations_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instance_information(
        self,
        InstanceInformationFilterList: List[InstanceInformationFilterTypeDef] = None,
        Filters: List[InstanceInformationStringFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeInstanceInformationResultTypeDef:
        """
        [Client.describe_instance_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_instance_information)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instance_patch_states(
        self, InstanceIds: List[str], NextToken: str = None, MaxResults: int = None
    ) -> DescribeInstancePatchStatesResultTypeDef:
        """
        [Client.describe_instance_patch_states documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_instance_patch_states)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instance_patch_states_for_patch_group(
        self,
        PatchGroup: str,
        Filters: List[InstancePatchStateFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeInstancePatchStatesForPatchGroupResultTypeDef:
        """
        [Client.describe_instance_patch_states_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_instance_patch_states_for_patch_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instance_patches(
        self,
        InstanceId: str,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeInstancePatchesResultTypeDef:
        """
        [Client.describe_instance_patches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_instance_patches)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_inventory_deletions(
        self, DeletionId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeInventoryDeletionsResultTypeDef:
        """
        [Client.describe_inventory_deletions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_inventory_deletions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_maintenance_window_execution_task_invocations(
        self,
        WindowExecutionId: str,
        TaskId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef:
        """
        [Client.describe_maintenance_window_execution_task_invocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_maintenance_window_execution_task_invocations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_maintenance_window_execution_tasks(
        self,
        WindowExecutionId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowExecutionTasksResultTypeDef:
        """
        [Client.describe_maintenance_window_execution_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_maintenance_window_execution_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_maintenance_window_executions(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowExecutionsResultTypeDef:
        """
        [Client.describe_maintenance_window_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_maintenance_window_executions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_maintenance_window_schedule(
        self,
        WindowId: str = None,
        Targets: List[TargetTypeDef] = None,
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"] = None,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowScheduleResultTypeDef:
        """
        [Client.describe_maintenance_window_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_maintenance_window_schedule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_maintenance_window_targets(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowTargetsResultTypeDef:
        """
        [Client.describe_maintenance_window_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_maintenance_window_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_maintenance_window_tasks(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowTasksResultTypeDef:
        """
        [Client.describe_maintenance_window_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_maintenance_window_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_maintenance_windows(
        self,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowsResultTypeDef:
        """
        [Client.describe_maintenance_windows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_maintenance_windows)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_maintenance_windows_for_target(
        self,
        Targets: List[TargetTypeDef],
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"],
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowsForTargetResultTypeDef:
        """
        [Client.describe_maintenance_windows_for_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_maintenance_windows_for_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_ops_items(
        self,
        OpsItemFilters: List[OpsItemFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeOpsItemsResponseTypeDef:
        """
        [Client.describe_ops_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_ops_items)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_parameters(
        self,
        Filters: List[ParametersFilterTypeDef] = None,
        ParameterFilters: List[ParameterStringFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeParametersResultTypeDef:
        """
        [Client.describe_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_patch_baselines(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribePatchBaselinesResultTypeDef:
        """
        [Client.describe_patch_baselines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_patch_baselines)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_patch_group_state(self, PatchGroup: str) -> DescribePatchGroupStateResultTypeDef:
        """
        [Client.describe_patch_group_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_patch_group_state)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_patch_groups(
        self,
        MaxResults: int = None,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        NextToken: str = None,
    ) -> DescribePatchGroupsResultTypeDef:
        """
        [Client.describe_patch_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_patch_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_patch_properties(
        self,
        OperatingSystem: Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ],
        Property: Literal[
            "PRODUCT", "PRODUCT_FAMILY", "CLASSIFICATION", "MSRC_SEVERITY", "PRIORITY", "SEVERITY"
        ],
        PatchSet: Literal["OS", "APPLICATION"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribePatchPropertiesResultTypeDef:
        """
        [Client.describe_patch_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_patch_properties)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_sessions(
        self,
        State: Literal["Active", "History"],
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[SessionFilterTypeDef] = None,
    ) -> DescribeSessionsResponseTypeDef:
        """
        [Client.describe_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.describe_sessions)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_automation_execution(
        self, AutomationExecutionId: str
    ) -> GetAutomationExecutionResultTypeDef:
        """
        [Client.get_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_automation_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_calendar_state(
        self, CalendarNames: List[str], AtTime: str = None
    ) -> GetCalendarStateResponseTypeDef:
        """
        [Client.get_calendar_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_calendar_state)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_command_invocation(
        self, CommandId: str, InstanceId: str, PluginName: str = None
    ) -> GetCommandInvocationResultTypeDef:
        """
        [Client.get_command_invocation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_command_invocation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connection_status(self, Target: str) -> GetConnectionStatusResponseTypeDef:
        """
        [Client.get_connection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_connection_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_default_patch_baseline(
        self,
        OperatingSystem: Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ] = None,
    ) -> GetDefaultPatchBaselineResultTypeDef:
        """
        [Client.get_default_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_default_patch_baseline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deployable_patch_snapshot_for_instance(
        self, InstanceId: str, SnapshotId: str
    ) -> GetDeployablePatchSnapshotForInstanceResultTypeDef:
        """
        [Client.get_deployable_patch_snapshot_for_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_deployable_patch_snapshot_for_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_document(
        self,
        Name: str,
        VersionName: str = None,
        DocumentVersion: str = None,
        DocumentFormat: Literal["YAML", "JSON", "TEXT"] = None,
    ) -> GetDocumentResultTypeDef:
        """
        [Client.get_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_inventory(
        self,
        Filters: List[InventoryFilterTypeDef] = None,
        Aggregators: List[InventoryAggregatorTypeDef] = None,
        ResultAttributes: List[ResultAttributeTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetInventoryResultTypeDef:
        """
        [Client.get_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_inventory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_inventory_schema(
        self,
        TypeName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Aggregator: bool = None,
        SubType: bool = None,
    ) -> GetInventorySchemaResultTypeDef:
        """
        [Client.get_inventory_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_inventory_schema)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_maintenance_window(self, WindowId: str) -> GetMaintenanceWindowResultTypeDef:
        """
        [Client.get_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_maintenance_window)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_maintenance_window_execution(
        self, WindowExecutionId: str
    ) -> GetMaintenanceWindowExecutionResultTypeDef:
        """
        [Client.get_maintenance_window_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_maintenance_window_execution_task(
        self, WindowExecutionId: str, TaskId: str
    ) -> GetMaintenanceWindowExecutionTaskResultTypeDef:
        """
        [Client.get_maintenance_window_execution_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_maintenance_window_execution_task_invocation(
        self, WindowExecutionId: str, TaskId: str, InvocationId: str
    ) -> GetMaintenanceWindowExecutionTaskInvocationResultTypeDef:
        """
        [Client.get_maintenance_window_execution_task_invocation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution_task_invocation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_maintenance_window_task(
        self, WindowId: str, WindowTaskId: str
    ) -> GetMaintenanceWindowTaskResultTypeDef:
        """
        [Client.get_maintenance_window_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_maintenance_window_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ops_item(self, OpsItemId: str) -> GetOpsItemResponseTypeDef:
        """
        [Client.get_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_ops_item)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ops_summary(
        self,
        SyncName: str = None,
        Filters: List[OpsFilterTypeDef] = None,
        Aggregators: List[OpsAggregatorTypeDef] = None,
        ResultAttributes: List[OpsResultAttributeTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetOpsSummaryResultTypeDef:
        """
        [Client.get_ops_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_ops_summary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_parameter(self, Name: str, WithDecryption: bool = None) -> GetParameterResultTypeDef:
        """
        [Client.get_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_parameter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_parameter_history(
        self, Name: str, WithDecryption: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> GetParameterHistoryResultTypeDef:
        """
        [Client.get_parameter_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_parameter_history)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_parameters(
        self, Names: List[str], WithDecryption: bool = None
    ) -> GetParametersResultTypeDef:
        """
        [Client.get_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_parameters_by_path(
        self,
        Path: str,
        Recursive: bool = None,
        ParameterFilters: List[ParameterStringFilterTypeDef] = None,
        WithDecryption: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetParametersByPathResultTypeDef:
        """
        [Client.get_parameters_by_path documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_parameters_by_path)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_patch_baseline(self, BaselineId: str) -> GetPatchBaselineResultTypeDef:
        """
        [Client.get_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_patch_baseline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_patch_baseline_for_patch_group(
        self,
        PatchGroup: str,
        OperatingSystem: Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
        ] = None,
    ) -> GetPatchBaselineForPatchGroupResultTypeDef:
        """
        [Client.get_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_patch_baseline_for_patch_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service_setting(self, SettingId: str) -> GetServiceSettingResultTypeDef:
        """
        [Client.get_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.get_service_setting)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def label_parameter_version(
        self, Name: str, Labels: List[str], ParameterVersion: int = None
    ) -> LabelParameterVersionResultTypeDef:
        """
        [Client.label_parameter_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.label_parameter_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_association_versions(
        self, AssociationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAssociationVersionsResultTypeDef:
        """
        [Client.list_association_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_association_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_associations(
        self,
        AssociationFilterList: List[AssociationFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListAssociationsResultTypeDef:
        """
        [Client.list_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_command_invocations(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[CommandFilterTypeDef] = None,
        Details: bool = None,
    ) -> ListCommandInvocationsResultTypeDef:
        """
        [Client.list_command_invocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_command_invocations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_commands(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[CommandFilterTypeDef] = None,
    ) -> ListCommandsResultTypeDef:
        """
        [Client.list_commands documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_commands)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_compliance_items(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        ResourceIds: List[str] = None,
        ResourceTypes: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListComplianceItemsResultTypeDef:
        """
        [Client.list_compliance_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_compliance_items)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_compliance_summaries(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListComplianceSummariesResultTypeDef:
        """
        [Client.list_compliance_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_compliance_summaries)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_document_versions(
        self, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListDocumentVersionsResultTypeDef:
        """
        [Client.list_document_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_document_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_documents(
        self,
        DocumentFilterList: List[DocumentFilterTypeDef] = None,
        Filters: List[DocumentKeyValuesFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListDocumentsResultTypeDef:
        """
        [Client.list_documents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_documents)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_inventory_entries(
        self,
        InstanceId: str,
        TypeName: str,
        Filters: List[InventoryFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListInventoryEntriesResultTypeDef:
        """
        [Client.list_inventory_entries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_inventory_entries)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_compliance_summaries(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListResourceComplianceSummariesResultTypeDef:
        """
        [Client.list_resource_compliance_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_resource_compliance_summaries)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_data_sync(
        self, SyncType: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListResourceDataSyncResultTypeDef:
        """
        [Client.list_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_resource_data_sync)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self,
        ResourceType: Literal[
            "Document",
            "ManagedInstance",
            "MaintenanceWindow",
            "Parameter",
            "PatchBaseline",
            "OpsItem",
        ],
        ResourceId: str,
    ) -> ListTagsForResourceResultTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_document_permission(
        self,
        Name: str,
        PermissionType: Literal["Share"],
        AccountIdsToAdd: List[str] = None,
        AccountIdsToRemove: List[str] = None,
        SharedDocumentVersion: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.modify_document_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.modify_document_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_compliance_items(
        self,
        ResourceId: str,
        ResourceType: str,
        ComplianceType: str,
        ExecutionSummary: ComplianceExecutionSummaryTypeDef,
        Items: List[ComplianceItemEntryTypeDef],
        ItemContentHash: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_compliance_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.put_compliance_items)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_inventory(
        self, InstanceId: str, Items: List[InventoryItemTypeDef]
    ) -> PutInventoryResultTypeDef:
        """
        [Client.put_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.put_inventory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_parameter(
        self,
        Name: str,
        Value: str,
        Type: Literal["String", "StringList", "SecureString"],
        Description: str = None,
        KeyId: str = None,
        Overwrite: bool = None,
        AllowedPattern: str = None,
        Tags: List[TagTypeDef] = None,
        Tier: Literal["Standard", "Advanced", "Intelligent-Tiering"] = None,
        Policies: str = None,
    ) -> PutParameterResultTypeDef:
        """
        [Client.put_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.put_parameter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_default_patch_baseline(
        self, BaselineId: str
    ) -> RegisterDefaultPatchBaselineResultTypeDef:
        """
        [Client.register_default_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.register_default_patch_baseline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_patch_baseline_for_patch_group(
        self, BaselineId: str, PatchGroup: str
    ) -> RegisterPatchBaselineForPatchGroupResultTypeDef:
        """
        [Client.register_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.register_patch_baseline_for_patch_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_target_with_maintenance_window(
        self,
        WindowId: str,
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"],
        Targets: List[TargetTypeDef],
        OwnerInformation: str = None,
        Name: str = None,
        Description: str = None,
        ClientToken: str = None,
    ) -> RegisterTargetWithMaintenanceWindowResultTypeDef:
        """
        [Client.register_target_with_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.register_target_with_maintenance_window)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_task_with_maintenance_window(
        self,
        WindowId: str,
        Targets: List[TargetTypeDef],
        TaskArn: str,
        TaskType: Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        MaxConcurrency: str,
        MaxErrors: str,
        ServiceRoleArn: str = None,
        TaskParameters: Dict[str, MaintenanceWindowTaskParameterValueExpressionTypeDef] = None,
        TaskInvocationParameters: MaintenanceWindowTaskInvocationParametersTypeDef = None,
        Priority: int = None,
        LoggingInfo: LoggingInfoTypeDef = None,
        Name: str = None,
        Description: str = None,
        ClientToken: str = None,
    ) -> RegisterTaskWithMaintenanceWindowResultTypeDef:
        """
        [Client.register_task_with_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.register_task_with_maintenance_window)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_resource(
        self,
        ResourceType: Literal[
            "Document",
            "ManagedInstance",
            "MaintenanceWindow",
            "Parameter",
            "PatchBaseline",
            "OpsItem",
        ],
        ResourceId: str,
        TagKeys: List[str],
    ) -> Dict[str, Any]:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.remove_tags_from_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_service_setting(self, SettingId: str) -> ResetServiceSettingResultTypeDef:
        """
        [Client.reset_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.reset_service_setting)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resume_session(self, SessionId: str) -> ResumeSessionResponseTypeDef:
        """
        [Client.resume_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.resume_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_automation_signal(
        self,
        AutomationExecutionId: str,
        SignalType: Literal["Approve", "Reject", "StartStep", "StopStep", "Resume"],
        Payload: Dict[str, List[str]] = None,
    ) -> Dict[str, Any]:
        """
        [Client.send_automation_signal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.send_automation_signal)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_command(
        self,
        DocumentName: str,
        InstanceIds: List[str] = None,
        Targets: List[TargetTypeDef] = None,
        DocumentVersion: str = None,
        DocumentHash: str = None,
        DocumentHashType: Literal["Sha256", "Sha1"] = None,
        TimeoutSeconds: int = None,
        Comment: str = None,
        Parameters: Dict[str, List[str]] = None,
        OutputS3Region: str = None,
        OutputS3BucketName: str = None,
        OutputS3KeyPrefix: str = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        ServiceRoleArn: str = None,
        NotificationConfig: NotificationConfigTypeDef = None,
        CloudWatchOutputConfig: CloudWatchOutputConfigTypeDef = None,
    ) -> SendCommandResultTypeDef:
        """
        [Client.send_command documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.send_command)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_associations_once(self, AssociationIds: List[str]) -> Dict[str, Any]:
        """
        [Client.start_associations_once documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.start_associations_once)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_automation_execution(
        self,
        DocumentName: str,
        DocumentVersion: str = None,
        Parameters: Dict[str, List[str]] = None,
        ClientToken: str = None,
        Mode: Literal["Auto", "Interactive"] = None,
        TargetParameterName: str = None,
        Targets: List[TargetTypeDef] = None,
        TargetMaps: List[Dict[str, List[str]]] = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        TargetLocations: List[TargetLocationTypeDef] = None,
    ) -> StartAutomationExecutionResultTypeDef:
        """
        [Client.start_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.start_automation_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_session(
        self, Target: str, DocumentName: str = None, Parameters: Dict[str, List[str]] = None
    ) -> StartSessionResponseTypeDef:
        """
        [Client.start_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.start_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_automation_execution(
        self, AutomationExecutionId: str, Type: Literal["Complete", "Cancel"] = None
    ) -> Dict[str, Any]:
        """
        [Client.stop_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.stop_automation_execution)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate_session(self, SessionId: str) -> TerminateSessionResponseTypeDef:
        """
        [Client.terminate_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.terminate_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_association(
        self,
        AssociationId: str,
        Parameters: Dict[str, List[str]] = None,
        DocumentVersion: str = None,
        ScheduleExpression: str = None,
        OutputLocation: InstanceAssociationOutputLocationTypeDef = None,
        Name: str = None,
        Targets: List[TargetTypeDef] = None,
        AssociationName: str = None,
        AssociationVersion: str = None,
        AutomationTargetParameterName: str = None,
        MaxErrors: str = None,
        MaxConcurrency: str = None,
        ComplianceSeverity: Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"] = None,
    ) -> UpdateAssociationResultTypeDef:
        """
        [Client.update_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_association_status(
        self, Name: str, InstanceId: str, AssociationStatus: AssociationStatusTypeDef
    ) -> UpdateAssociationStatusResultTypeDef:
        """
        [Client.update_association_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_association_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_document(
        self,
        Content: str,
        Name: str,
        Attachments: List[AttachmentsSourceTypeDef] = None,
        VersionName: str = None,
        DocumentVersion: str = None,
        DocumentFormat: Literal["YAML", "JSON", "TEXT"] = None,
        TargetType: str = None,
    ) -> UpdateDocumentResultTypeDef:
        """
        [Client.update_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_document_default_version(
        self, Name: str, DocumentVersion: str
    ) -> UpdateDocumentDefaultVersionResultTypeDef:
        """
        [Client.update_document_default_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_document_default_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_maintenance_window(
        self,
        WindowId: str,
        Name: str = None,
        Description: str = None,
        StartDate: str = None,
        EndDate: str = None,
        Schedule: str = None,
        ScheduleTimezone: str = None,
        Duration: int = None,
        Cutoff: int = None,
        AllowUnassociatedTargets: bool = None,
        Enabled: bool = None,
        Replace: bool = None,
    ) -> UpdateMaintenanceWindowResultTypeDef:
        """
        [Client.update_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_maintenance_window)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_maintenance_window_target(
        self,
        WindowId: str,
        WindowTargetId: str,
        Targets: List[TargetTypeDef] = None,
        OwnerInformation: str = None,
        Name: str = None,
        Description: str = None,
        Replace: bool = None,
    ) -> UpdateMaintenanceWindowTargetResultTypeDef:
        """
        [Client.update_maintenance_window_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_maintenance_window_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_maintenance_window_task(
        self,
        WindowId: str,
        WindowTaskId: str,
        Targets: List[TargetTypeDef] = None,
        TaskArn: str = None,
        ServiceRoleArn: str = None,
        TaskParameters: Dict[str, MaintenanceWindowTaskParameterValueExpressionTypeDef] = None,
        TaskInvocationParameters: MaintenanceWindowTaskInvocationParametersTypeDef = None,
        Priority: int = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        LoggingInfo: LoggingInfoTypeDef = None,
        Name: str = None,
        Description: str = None,
        Replace: bool = None,
    ) -> UpdateMaintenanceWindowTaskResultTypeDef:
        """
        [Client.update_maintenance_window_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_maintenance_window_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_managed_instance_role(self, InstanceId: str, IamRole: str) -> Dict[str, Any]:
        """
        [Client.update_managed_instance_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_managed_instance_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_ops_item(
        self,
        OpsItemId: str,
        Description: str = None,
        OperationalData: Dict[str, OpsItemDataValueTypeDef] = None,
        OperationalDataToDelete: List[str] = None,
        Notifications: List[OpsItemNotificationTypeDef] = None,
        Priority: int = None,
        RelatedOpsItems: List[RelatedOpsItemTypeDef] = None,
        Status: Literal["Open", "InProgress", "Resolved"] = None,
        Title: str = None,
        Category: str = None,
        Severity: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_ops_item)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_patch_baseline(
        self,
        BaselineId: str,
        Name: str = None,
        GlobalFilters: PatchFilterGroupTypeDef = None,
        ApprovalRules: PatchRuleGroupTypeDef = None,
        ApprovedPatches: List[str] = None,
        ApprovedPatchesComplianceLevel: Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ] = None,
        ApprovedPatchesEnableNonSecurity: bool = None,
        RejectedPatches: List[str] = None,
        RejectedPatchesAction: Literal["ALLOW_AS_DEPENDENCY", "BLOCK"] = None,
        Description: str = None,
        Sources: List[PatchSourceTypeDef] = None,
        Replace: bool = None,
    ) -> UpdatePatchBaselineResultTypeDef:
        """
        [Client.update_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_patch_baseline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_resource_data_sync(
        self, SyncName: str, SyncType: str, SyncSource: ResourceDataSyncSourceTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.update_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_resource_data_sync)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_service_setting(self, SettingId: str, SettingValue: str) -> Dict[str, Any]:
        """
        [Client.update_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Client.update_service_setting)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_activations"]
    ) -> paginator_scope.DescribeActivationsPaginator:
        """
        [Paginator.DescribeActivations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeActivations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_association_execution_targets"]
    ) -> paginator_scope.DescribeAssociationExecutionTargetsPaginator:
        """
        [Paginator.DescribeAssociationExecutionTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_association_executions"]
    ) -> paginator_scope.DescribeAssociationExecutionsPaginator:
        """
        [Paginator.DescribeAssociationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_automation_executions"]
    ) -> paginator_scope.DescribeAutomationExecutionsPaginator:
        """
        [Paginator.DescribeAutomationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_automation_step_executions"]
    ) -> paginator_scope.DescribeAutomationStepExecutionsPaginator:
        """
        [Paginator.DescribeAutomationStepExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_available_patches"]
    ) -> paginator_scope.DescribeAvailablePatchesPaginator:
        """
        [Paginator.DescribeAvailablePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_effective_instance_associations"]
    ) -> paginator_scope.DescribeEffectiveInstanceAssociationsPaginator:
        """
        [Paginator.DescribeEffectiveInstanceAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_effective_patches_for_patch_baseline"]
    ) -> paginator_scope.DescribeEffectivePatchesForPatchBaselinePaginator:
        """
        [Paginator.DescribeEffectivePatchesForPatchBaseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_instance_associations_status"]
    ) -> paginator_scope.DescribeInstanceAssociationsStatusPaginator:
        """
        [Paginator.DescribeInstanceAssociationsStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_instance_information"]
    ) -> paginator_scope.DescribeInstanceInformationPaginator:
        """
        [Paginator.DescribeInstanceInformation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_instance_patch_states"]
    ) -> paginator_scope.DescribeInstancePatchStatesPaginator:
        """
        [Paginator.DescribeInstancePatchStates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_instance_patch_states_for_patch_group"]
    ) -> paginator_scope.DescribeInstancePatchStatesForPatchGroupPaginator:
        """
        [Paginator.DescribeInstancePatchStatesForPatchGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_instance_patches"]
    ) -> paginator_scope.DescribeInstancePatchesPaginator:
        """
        [Paginator.DescribeInstancePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_inventory_deletions"]
    ) -> paginator_scope.DescribeInventoryDeletionsPaginator:
        """
        [Paginator.DescribeInventoryDeletions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_execution_task_invocations"]
    ) -> paginator_scope.DescribeMaintenanceWindowExecutionTaskInvocationsPaginator:
        """
        [Paginator.DescribeMaintenanceWindowExecutionTaskInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_execution_tasks"]
    ) -> paginator_scope.DescribeMaintenanceWindowExecutionTasksPaginator:
        """
        [Paginator.DescribeMaintenanceWindowExecutionTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_executions"]
    ) -> paginator_scope.DescribeMaintenanceWindowExecutionsPaginator:
        """
        [Paginator.DescribeMaintenanceWindowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_schedule"]
    ) -> paginator_scope.DescribeMaintenanceWindowSchedulePaginator:
        """
        [Paginator.DescribeMaintenanceWindowSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_targets"]
    ) -> paginator_scope.DescribeMaintenanceWindowTargetsPaginator:
        """
        [Paginator.DescribeMaintenanceWindowTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_tasks"]
    ) -> paginator_scope.DescribeMaintenanceWindowTasksPaginator:
        """
        [Paginator.DescribeMaintenanceWindowTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_windows"]
    ) -> paginator_scope.DescribeMaintenanceWindowsPaginator:
        """
        [Paginator.DescribeMaintenanceWindows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_windows_for_target"]
    ) -> paginator_scope.DescribeMaintenanceWindowsForTargetPaginator:
        """
        [Paginator.DescribeMaintenanceWindowsForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_parameters"]
    ) -> paginator_scope.DescribeParametersPaginator:
        """
        [Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeParameters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_patch_baselines"]
    ) -> paginator_scope.DescribePatchBaselinesPaginator:
        """
        [Paginator.DescribePatchBaselines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_patch_groups"]
    ) -> paginator_scope.DescribePatchGroupsPaginator:
        """
        [Paginator.DescribePatchGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_sessions"]
    ) -> paginator_scope.DescribeSessionsPaginator:
        """
        [Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.DescribeSessions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_inventory"]
    ) -> paginator_scope.GetInventoryPaginator:
        """
        [Paginator.GetInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.GetInventory)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_inventory_schema"]
    ) -> paginator_scope.GetInventorySchemaPaginator:
        """
        [Paginator.GetInventorySchema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.GetInventorySchema)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_parameter_history"]
    ) -> paginator_scope.GetParameterHistoryPaginator:
        """
        [Paginator.GetParameterHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.GetParameterHistory)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_parameters_by_path"]
    ) -> paginator_scope.GetParametersByPathPaginator:
        """
        [Paginator.GetParametersByPath documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.GetParametersByPath)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_association_versions"]
    ) -> paginator_scope.ListAssociationVersionsPaginator:
        """
        [Paginator.ListAssociationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_associations"]
    ) -> paginator_scope.ListAssociationsPaginator:
        """
        [Paginator.ListAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.ListAssociations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_command_invocations"]
    ) -> paginator_scope.ListCommandInvocationsPaginator:
        """
        [Paginator.ListCommandInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_commands"]
    ) -> paginator_scope.ListCommandsPaginator:
        """
        [Paginator.ListCommands documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.ListCommands)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_compliance_items"]
    ) -> paginator_scope.ListComplianceItemsPaginator:
        """
        [Paginator.ListComplianceItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.ListComplianceItems)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_compliance_summaries"]
    ) -> paginator_scope.ListComplianceSummariesPaginator:
        """
        [Paginator.ListComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_document_versions"]
    ) -> paginator_scope.ListDocumentVersionsPaginator:
        """
        [Paginator.ListDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_documents"]
    ) -> paginator_scope.ListDocumentsPaginator:
        """
        [Paginator.ListDocuments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.ListDocuments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_compliance_summaries"]
    ) -> paginator_scope.ListResourceComplianceSummariesPaginator:
        """
        [Paginator.ListResourceComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_data_sync"]
    ) -> paginator_scope.ListResourceDataSyncPaginator:
        """
        [Paginator.ListResourceDataSync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync)
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    AssociatedInstances: Boto3ClientError
    AssociationAlreadyExists: Boto3ClientError
    AssociationDoesNotExist: Boto3ClientError
    AssociationExecutionDoesNotExist: Boto3ClientError
    AssociationLimitExceeded: Boto3ClientError
    AssociationVersionLimitExceeded: Boto3ClientError
    AutomationDefinitionNotFoundException: Boto3ClientError
    AutomationDefinitionVersionNotFoundException: Boto3ClientError
    AutomationExecutionLimitExceededException: Boto3ClientError
    AutomationExecutionNotFoundException: Boto3ClientError
    AutomationStepNotFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    ComplianceTypeCountLimitExceededException: Boto3ClientError
    CustomSchemaCountLimitExceededException: Boto3ClientError
    DocumentAlreadyExists: Boto3ClientError
    DocumentLimitExceeded: Boto3ClientError
    DocumentPermissionLimit: Boto3ClientError
    DocumentVersionLimitExceeded: Boto3ClientError
    DoesNotExistException: Boto3ClientError
    DuplicateDocumentContent: Boto3ClientError
    DuplicateDocumentVersionName: Boto3ClientError
    DuplicateInstanceId: Boto3ClientError
    FeatureNotAvailableException: Boto3ClientError
    HierarchyLevelLimitExceededException: Boto3ClientError
    HierarchyTypeMismatchException: Boto3ClientError
    IdempotentParameterMismatch: Boto3ClientError
    IncompatiblePolicyException: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidActivation: Boto3ClientError
    InvalidActivationId: Boto3ClientError
    InvalidAggregatorException: Boto3ClientError
    InvalidAllowedPatternException: Boto3ClientError
    InvalidAssociation: Boto3ClientError
    InvalidAssociationVersion: Boto3ClientError
    InvalidAutomationExecutionParametersException: Boto3ClientError
    InvalidAutomationSignalException: Boto3ClientError
    InvalidAutomationStatusUpdateException: Boto3ClientError
    InvalidCommandId: Boto3ClientError
    InvalidDeleteInventoryParametersException: Boto3ClientError
    InvalidDeletionIdException: Boto3ClientError
    InvalidDocument: Boto3ClientError
    InvalidDocumentContent: Boto3ClientError
    InvalidDocumentOperation: Boto3ClientError
    InvalidDocumentSchemaVersion: Boto3ClientError
    InvalidDocumentType: Boto3ClientError
    InvalidDocumentVersion: Boto3ClientError
    InvalidFilter: Boto3ClientError
    InvalidFilterKey: Boto3ClientError
    InvalidFilterOption: Boto3ClientError
    InvalidFilterValue: Boto3ClientError
    InvalidInstanceId: Boto3ClientError
    InvalidInstanceInformationFilterValue: Boto3ClientError
    InvalidInventoryGroupException: Boto3ClientError
    InvalidInventoryItemContextException: Boto3ClientError
    InvalidInventoryRequestException: Boto3ClientError
    InvalidItemContentException: Boto3ClientError
    InvalidKeyId: Boto3ClientError
    InvalidNextToken: Boto3ClientError
    InvalidNotificationConfig: Boto3ClientError
    InvalidOptionException: Boto3ClientError
    InvalidOutputFolder: Boto3ClientError
    InvalidOutputLocation: Boto3ClientError
    InvalidParameters: Boto3ClientError
    InvalidPermissionType: Boto3ClientError
    InvalidPluginName: Boto3ClientError
    InvalidPolicyAttributeException: Boto3ClientError
    InvalidPolicyTypeException: Boto3ClientError
    InvalidResourceId: Boto3ClientError
    InvalidResourceType: Boto3ClientError
    InvalidResultAttributeException: Boto3ClientError
    InvalidRole: Boto3ClientError
    InvalidSchedule: Boto3ClientError
    InvalidTarget: Boto3ClientError
    InvalidTypeNameException: Boto3ClientError
    InvalidUpdate: Boto3ClientError
    InvocationDoesNotExist: Boto3ClientError
    ItemContentMismatchException: Boto3ClientError
    ItemSizeLimitExceededException: Boto3ClientError
    MaxDocumentSizeExceeded: Boto3ClientError
    OpsItemAlreadyExistsException: Boto3ClientError
    OpsItemInvalidParameterException: Boto3ClientError
    OpsItemLimitExceededException: Boto3ClientError
    OpsItemNotFoundException: Boto3ClientError
    ParameterAlreadyExists: Boto3ClientError
    ParameterLimitExceeded: Boto3ClientError
    ParameterMaxVersionLimitExceeded: Boto3ClientError
    ParameterNotFound: Boto3ClientError
    ParameterPatternMismatchException: Boto3ClientError
    ParameterVersionLabelLimitExceeded: Boto3ClientError
    ParameterVersionNotFound: Boto3ClientError
    PoliciesLimitExceededException: Boto3ClientError
    ResourceDataSyncAlreadyExistsException: Boto3ClientError
    ResourceDataSyncConflictException: Boto3ClientError
    ResourceDataSyncCountExceededException: Boto3ClientError
    ResourceDataSyncInvalidConfigurationException: Boto3ClientError
    ResourceDataSyncNotFoundException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ServiceSettingNotFound: Boto3ClientError
    StatusUnchanged: Boto3ClientError
    SubTypeCountLimitExceededException: Boto3ClientError
    TargetInUseException: Boto3ClientError
    TargetNotConnected: Boto3ClientError
    TooManyTagsError: Boto3ClientError
    TooManyUpdates: Boto3ClientError
    TotalSizeLimitExceededException: Boto3ClientError
    UnsupportedCalendarException: Boto3ClientError
    UnsupportedFeatureRequiredException: Boto3ClientError
    UnsupportedInventoryItemContextException: Boto3ClientError
    UnsupportedInventorySchemaVersionException: Boto3ClientError
    UnsupportedOperatingSystem: Boto3ClientError
    UnsupportedParameterType: Boto3ClientError
    UnsupportedPlatformType: Boto3ClientError
