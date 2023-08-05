"Main interface for ssm service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ssm.type_defs import (
    AssociationExecutionFilterTypeDef,
    AssociationExecutionTargetsFilterTypeDef,
    AssociationFilterTypeDef,
    AutomationExecutionFilterTypeDef,
    CommandFilterTypeDef,
    ComplianceStringFilterTypeDef,
    DescribeActivationsFilterTypeDef,
    DescribeActivationsResultTypeDef,
    DescribeAssociationExecutionTargetsResultTypeDef,
    DescribeAssociationExecutionsResultTypeDef,
    DescribeAutomationExecutionsResultTypeDef,
    DescribeAutomationStepExecutionsResultTypeDef,
    DescribeAvailablePatchesResultTypeDef,
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
    DescribeParametersResultTypeDef,
    DescribePatchBaselinesResultTypeDef,
    DescribePatchGroupsResultTypeDef,
    DescribeSessionsResponseTypeDef,
    DocumentFilterTypeDef,
    DocumentKeyValuesFilterTypeDef,
    GetInventoryResultTypeDef,
    GetInventorySchemaResultTypeDef,
    GetParameterHistoryResultTypeDef,
    GetParametersByPathResultTypeDef,
    InstanceInformationFilterTypeDef,
    InstanceInformationStringFilterTypeDef,
    InstancePatchStateFilterTypeDef,
    InventoryAggregatorTypeDef,
    InventoryFilterTypeDef,
    ListAssociationVersionsResultTypeDef,
    ListAssociationsResultTypeDef,
    ListCommandInvocationsResultTypeDef,
    ListCommandsResultTypeDef,
    ListComplianceItemsResultTypeDef,
    ListComplianceSummariesResultTypeDef,
    ListDocumentVersionsResultTypeDef,
    ListDocumentsResultTypeDef,
    ListResourceComplianceSummariesResultTypeDef,
    ListResourceDataSyncResultTypeDef,
    MaintenanceWindowFilterTypeDef,
    PaginatorConfigTypeDef,
    ParameterStringFilterTypeDef,
    ParametersFilterTypeDef,
    PatchOrchestratorFilterTypeDef,
    ResultAttributeTypeDef,
    SessionFilterTypeDef,
    StepExecutionFilterTypeDef,
    TargetTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeActivationsPaginator",
    "DescribeAssociationExecutionTargetsPaginator",
    "DescribeAssociationExecutionsPaginator",
    "DescribeAutomationExecutionsPaginator",
    "DescribeAutomationStepExecutionsPaginator",
    "DescribeAvailablePatchesPaginator",
    "DescribeEffectiveInstanceAssociationsPaginator",
    "DescribeEffectivePatchesForPatchBaselinePaginator",
    "DescribeInstanceAssociationsStatusPaginator",
    "DescribeInstanceInformationPaginator",
    "DescribeInstancePatchStatesPaginator",
    "DescribeInstancePatchStatesForPatchGroupPaginator",
    "DescribeInstancePatchesPaginator",
    "DescribeInventoryDeletionsPaginator",
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginator",
    "DescribeMaintenanceWindowExecutionTasksPaginator",
    "DescribeMaintenanceWindowExecutionsPaginator",
    "DescribeMaintenanceWindowSchedulePaginator",
    "DescribeMaintenanceWindowTargetsPaginator",
    "DescribeMaintenanceWindowTasksPaginator",
    "DescribeMaintenanceWindowsPaginator",
    "DescribeMaintenanceWindowsForTargetPaginator",
    "DescribeParametersPaginator",
    "DescribePatchBaselinesPaginator",
    "DescribePatchGroupsPaginator",
    "DescribeSessionsPaginator",
    "GetInventoryPaginator",
    "GetInventorySchemaPaginator",
    "GetParameterHistoryPaginator",
    "GetParametersByPathPaginator",
    "ListAssociationVersionsPaginator",
    "ListAssociationsPaginator",
    "ListCommandInvocationsPaginator",
    "ListCommandsPaginator",
    "ListComplianceItemsPaginator",
    "ListComplianceSummariesPaginator",
    "ListDocumentVersionsPaginator",
    "ListDocumentsPaginator",
    "ListResourceComplianceSummariesPaginator",
    "ListResourceDataSyncPaginator",
)


class DescribeActivationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeActivations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeActivations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeActivationsFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeActivationsResultTypeDef, None, None]:
        """
        [DescribeActivations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeActivations.paginate)
        """


class DescribeAssociationExecutionTargetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAssociationExecutionTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AssociationId: str,
        ExecutionId: str,
        Filters: List[AssociationExecutionTargetsFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAssociationExecutionTargetsResultTypeDef, None, None]:
        """
        [DescribeAssociationExecutionTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets.paginate)
        """


class DescribeAssociationExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAssociationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AssociationId: str,
        Filters: List[AssociationExecutionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAssociationExecutionsResultTypeDef, None, None]:
        """
        [DescribeAssociationExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions.paginate)
        """


class DescribeAutomationExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAutomationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[AutomationExecutionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAutomationExecutionsResultTypeDef, None, None]:
        """
        [DescribeAutomationExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions.paginate)
        """


class DescribeAutomationStepExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAutomationStepExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutomationExecutionId: str,
        Filters: List[StepExecutionFilterTypeDef] = None,
        ReverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAutomationStepExecutionsResultTypeDef, None, None]:
        """
        [DescribeAutomationStepExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions.paginate)
        """


class DescribeAvailablePatchesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAvailablePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeAvailablePatchesResultTypeDef, None, None]:
        """
        [DescribeAvailablePatches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches.paginate)
        """


class DescribeEffectiveInstanceAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEffectiveInstanceAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeEffectiveInstanceAssociationsResultTypeDef, None, None]:
        """
        [DescribeEffectiveInstanceAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations.paginate)
        """


class DescribeEffectivePatchesForPatchBaselinePaginator(Boto3Paginator):
    """
    [Paginator.DescribeEffectivePatchesForPatchBaseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, BaselineId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeEffectivePatchesForPatchBaselineResultTypeDef, None, None]:
        """
        [DescribeEffectivePatchesForPatchBaseline.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline.paginate)
        """


class DescribeInstanceAssociationsStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstanceAssociationsStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeInstanceAssociationsStatusResultTypeDef, None, None]:
        """
        [DescribeInstanceAssociationsStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus.paginate)
        """


class DescribeInstanceInformationPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstanceInformation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceInformationFilterList: List[InstanceInformationFilterTypeDef] = None,
        Filters: List[InstanceInformationStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeInstanceInformationResultTypeDef, None, None]:
        """
        [DescribeInstanceInformation.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation.paginate)
        """


class DescribeInstancePatchStatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstancePatchStates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, InstanceIds: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeInstancePatchStatesResultTypeDef, None, None]:
        """
        [DescribeInstancePatchStates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates.paginate)
        """


class DescribeInstancePatchStatesForPatchGroupPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstancePatchStatesForPatchGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PatchGroup: str,
        Filters: List[InstancePatchStateFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeInstancePatchStatesForPatchGroupResultTypeDef, None, None]:
        """
        [DescribeInstancePatchStatesForPatchGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup.paginate)
        """


class DescribeInstancePatchesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstancePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeInstancePatchesResultTypeDef, None, None]:
        """
        [DescribeInstancePatches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches.paginate)
        """


class DescribeInventoryDeletionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInventoryDeletions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DeletionId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeInventoryDeletionsResultTypeDef, None, None]:
        """
        [DescribeInventoryDeletions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions.paginate)
        """


class DescribeMaintenanceWindowExecutionTaskInvocationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowExecutionTaskInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowExecutionId: str,
        TaskId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef, None, None]:
        """
        [DescribeMaintenanceWindowExecutionTaskInvocations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations.paginate)
        """


class DescribeMaintenanceWindowExecutionTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowExecutionTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowExecutionId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMaintenanceWindowExecutionTasksResultTypeDef, None, None]:
        """
        [DescribeMaintenanceWindowExecutionTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks.paginate)
        """


class DescribeMaintenanceWindowExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMaintenanceWindowExecutionsResultTypeDef, None, None]:
        """
        [DescribeMaintenanceWindowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions.paginate)
        """


class DescribeMaintenanceWindowSchedulePaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowId: str = None,
        Targets: List[TargetTypeDef] = None,
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"] = None,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMaintenanceWindowScheduleResultTypeDef, None, None]:
        """
        [DescribeMaintenanceWindowSchedule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule.paginate)
        """


class DescribeMaintenanceWindowTargetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMaintenanceWindowTargetsResultTypeDef, None, None]:
        """
        [DescribeMaintenanceWindowTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets.paginate)
        """


class DescribeMaintenanceWindowTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMaintenanceWindowTasksResultTypeDef, None, None]:
        """
        [DescribeMaintenanceWindowTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks.paginate)
        """


class DescribeMaintenanceWindowsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMaintenanceWindowsResultTypeDef, None, None]:
        """
        [DescribeMaintenanceWindows.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows.paginate)
        """


class DescribeMaintenanceWindowsForTargetPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowsForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Targets: List[TargetTypeDef],
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMaintenanceWindowsForTargetResultTypeDef, None, None]:
        """
        [DescribeMaintenanceWindowsForTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget.paginate)
        """


class DescribeParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ParametersFilterTypeDef] = None,
        ParameterFilters: List[ParameterStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeParametersResultTypeDef, None, None]:
        """
        [DescribeParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeParameters.paginate)
        """


class DescribePatchBaselinesPaginator(Boto3Paginator):
    """
    [Paginator.DescribePatchBaselines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribePatchBaselinesResultTypeDef, None, None]:
        """
        [DescribePatchBaselines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines.paginate)
        """


class DescribePatchGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePatchGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribePatchGroupsResultTypeDef, None, None]:
        """
        [DescribePatchGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups.paginate)
        """


class DescribeSessionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeSessions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        State: Literal["Active", "History"],
        Filters: List[SessionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSessionsResponseTypeDef, None, None]:
        """
        [DescribeSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.DescribeSessions.paginate)
        """


class GetInventoryPaginator(Boto3Paginator):
    """
    [Paginator.GetInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.GetInventory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[InventoryFilterTypeDef] = None,
        Aggregators: List[InventoryAggregatorTypeDef] = None,
        ResultAttributes: List[ResultAttributeTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetInventoryResultTypeDef, None, None]:
        """
        [GetInventory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.GetInventory.paginate)
        """


class GetInventorySchemaPaginator(Boto3Paginator):
    """
    [Paginator.GetInventorySchema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.GetInventorySchema)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TypeName: str = None,
        Aggregator: bool = None,
        SubType: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetInventorySchemaResultTypeDef, None, None]:
        """
        [GetInventorySchema.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.GetInventorySchema.paginate)
        """


class GetParameterHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetParameterHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.GetParameterHistory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Name: str,
        WithDecryption: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetParameterHistoryResultTypeDef, None, None]:
        """
        [GetParameterHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.GetParameterHistory.paginate)
        """


class GetParametersByPathPaginator(Boto3Paginator):
    """
    [Paginator.GetParametersByPath documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.GetParametersByPath)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Path: str,
        Recursive: bool = None,
        ParameterFilters: List[ParameterStringFilterTypeDef] = None,
        WithDecryption: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetParametersByPathResultTypeDef, None, None]:
        """
        [GetParametersByPath.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.GetParametersByPath.paginate)
        """


class ListAssociationVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, AssociationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAssociationVersionsResultTypeDef, None, None]:
        """
        [ListAssociationVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions.paginate)
        """


class ListAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListAssociations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AssociationFilterList: List[AssociationFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAssociationsResultTypeDef, None, None]:
        """
        [ListAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListAssociations.paginate)
        """


class ListCommandInvocationsPaginator(Boto3Paginator):
    """
    [Paginator.ListCommandInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List[CommandFilterTypeDef] = None,
        Details: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListCommandInvocationsResultTypeDef, None, None]:
        """
        [ListCommandInvocations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations.paginate)
        """


class ListCommandsPaginator(Boto3Paginator):
    """
    [Paginator.ListCommands documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListCommands)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List[CommandFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListCommandsResultTypeDef, None, None]:
        """
        [ListCommands.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListCommands.paginate)
        """


class ListComplianceItemsPaginator(Boto3Paginator):
    """
    [Paginator.ListComplianceItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListComplianceItems)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        ResourceIds: List[str] = None,
        ResourceTypes: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListComplianceItemsResultTypeDef, None, None]:
        """
        [ListComplianceItems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListComplianceItems.paginate)
        """


class ListComplianceSummariesPaginator(Boto3Paginator):
    """
    [Paginator.ListComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListComplianceSummariesResultTypeDef, None, None]:
        """
        [ListComplianceSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries.paginate)
        """


class ListDocumentVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDocumentVersionsResultTypeDef, None, None]:
        """
        [ListDocumentVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions.paginate)
        """


class ListDocumentsPaginator(Boto3Paginator):
    """
    [Paginator.ListDocuments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListDocuments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DocumentFilterList: List[DocumentFilterTypeDef] = None,
        Filters: List[DocumentKeyValuesFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDocumentsResultTypeDef, None, None]:
        """
        [ListDocuments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListDocuments.paginate)
        """


class ListResourceComplianceSummariesPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListResourceComplianceSummariesResultTypeDef, None, None]:
        """
        [ListResourceComplianceSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries.paginate)
        """


class ListResourceDataSyncPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceDataSync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, SyncType: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListResourceDataSyncResultTypeDef, None, None]:
        """
        [ListResourceDataSync.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync.paginate)
        """
