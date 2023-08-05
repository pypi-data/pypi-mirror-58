"Main interface for backup service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_backup.client as client_scope
from mypy_boto3_backup.type_defs import (
    BackupPlanInputTypeDef,
    BackupSelectionTypeDef,
    CreateBackupPlanOutputTypeDef,
    CreateBackupSelectionOutputTypeDef,
    CreateBackupVaultOutputTypeDef,
    DeleteBackupPlanOutputTypeDef,
    DescribeBackupJobOutputTypeDef,
    DescribeBackupVaultOutputTypeDef,
    DescribeProtectedResourceOutputTypeDef,
    DescribeRecoveryPointOutputTypeDef,
    DescribeRestoreJobOutputTypeDef,
    ExportBackupPlanTemplateOutputTypeDef,
    GetBackupPlanFromJSONOutputTypeDef,
    GetBackupPlanFromTemplateOutputTypeDef,
    GetBackupPlanOutputTypeDef,
    GetBackupSelectionOutputTypeDef,
    GetBackupVaultAccessPolicyOutputTypeDef,
    GetBackupVaultNotificationsOutputTypeDef,
    GetRecoveryPointRestoreMetadataOutputTypeDef,
    GetSupportedResourceTypesOutputTypeDef,
    LifecycleTypeDef,
    ListBackupJobsOutputTypeDef,
    ListBackupPlanTemplatesOutputTypeDef,
    ListBackupPlanVersionsOutputTypeDef,
    ListBackupPlansOutputTypeDef,
    ListBackupSelectionsOutputTypeDef,
    ListBackupVaultsOutputTypeDef,
    ListProtectedResourcesOutputTypeDef,
    ListRecoveryPointsByBackupVaultOutputTypeDef,
    ListRecoveryPointsByResourceOutputTypeDef,
    ListRestoreJobsOutputTypeDef,
    ListTagsOutputTypeDef,
    StartBackupJobOutputTypeDef,
    StartRestoreJobOutputTypeDef,
    UpdateBackupPlanOutputTypeDef,
    UpdateRecoveryPointLifecycleOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BackupClient",)


class BackupClient(BaseClient):
    """
    [Backup.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_backup_plan(
        self,
        BackupPlan: BackupPlanInputTypeDef,
        BackupPlanTags: Dict[str, str] = None,
        CreatorRequestId: str = None,
    ) -> CreateBackupPlanOutputTypeDef:
        """
        [Client.create_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.create_backup_plan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_backup_selection(
        self,
        BackupPlanId: str,
        BackupSelection: BackupSelectionTypeDef,
        CreatorRequestId: str = None,
    ) -> CreateBackupSelectionOutputTypeDef:
        """
        [Client.create_backup_selection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.create_backup_selection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_backup_vault(
        self,
        BackupVaultName: str,
        BackupVaultTags: Dict[str, str] = None,
        EncryptionKeyArn: str = None,
        CreatorRequestId: str = None,
    ) -> CreateBackupVaultOutputTypeDef:
        """
        [Client.create_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.create_backup_vault)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_backup_plan(self, BackupPlanId: str) -> DeleteBackupPlanOutputTypeDef:
        """
        [Client.delete_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.delete_backup_plan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_backup_selection(self, BackupPlanId: str, SelectionId: str) -> None:
        """
        [Client.delete_backup_selection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.delete_backup_selection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_backup_vault(self, BackupVaultName: str) -> None:
        """
        [Client.delete_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.delete_backup_vault)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_backup_vault_access_policy(self, BackupVaultName: str) -> None:
        """
        [Client.delete_backup_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.delete_backup_vault_access_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_backup_vault_notifications(self, BackupVaultName: str) -> None:
        """
        [Client.delete_backup_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.delete_backup_vault_notifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_recovery_point(self, BackupVaultName: str, RecoveryPointArn: str) -> None:
        """
        [Client.delete_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.delete_recovery_point)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_backup_job(self, BackupJobId: str) -> DescribeBackupJobOutputTypeDef:
        """
        [Client.describe_backup_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.describe_backup_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_backup_vault(self, BackupVaultName: str) -> DescribeBackupVaultOutputTypeDef:
        """
        [Client.describe_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.describe_backup_vault)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_protected_resource(
        self, ResourceArn: str
    ) -> DescribeProtectedResourceOutputTypeDef:
        """
        [Client.describe_protected_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.describe_protected_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_recovery_point(
        self, BackupVaultName: str, RecoveryPointArn: str
    ) -> DescribeRecoveryPointOutputTypeDef:
        """
        [Client.describe_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.describe_recovery_point)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_restore_job(self, RestoreJobId: str) -> DescribeRestoreJobOutputTypeDef:
        """
        [Client.describe_restore_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.describe_restore_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_backup_plan_template(
        self, BackupPlanId: str
    ) -> ExportBackupPlanTemplateOutputTypeDef:
        """
        [Client.export_backup_plan_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.export_backup_plan_template)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_backup_plan(
        self, BackupPlanId: str, VersionId: str = None
    ) -> GetBackupPlanOutputTypeDef:
        """
        [Client.get_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.get_backup_plan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_backup_plan_from_json(
        self, BackupPlanTemplateJson: str
    ) -> GetBackupPlanFromJSONOutputTypeDef:
        """
        [Client.get_backup_plan_from_json documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.get_backup_plan_from_json)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_backup_plan_from_template(
        self, BackupPlanTemplateId: str
    ) -> GetBackupPlanFromTemplateOutputTypeDef:
        """
        [Client.get_backup_plan_from_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.get_backup_plan_from_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_backup_selection(
        self, BackupPlanId: str, SelectionId: str
    ) -> GetBackupSelectionOutputTypeDef:
        """
        [Client.get_backup_selection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.get_backup_selection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_backup_vault_access_policy(
        self, BackupVaultName: str
    ) -> GetBackupVaultAccessPolicyOutputTypeDef:
        """
        [Client.get_backup_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.get_backup_vault_access_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_backup_vault_notifications(
        self, BackupVaultName: str
    ) -> GetBackupVaultNotificationsOutputTypeDef:
        """
        [Client.get_backup_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.get_backup_vault_notifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_recovery_point_restore_metadata(
        self, BackupVaultName: str, RecoveryPointArn: str
    ) -> GetRecoveryPointRestoreMetadataOutputTypeDef:
        """
        [Client.get_recovery_point_restore_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.get_recovery_point_restore_metadata)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_supported_resource_types(self) -> GetSupportedResourceTypesOutputTypeDef:
        """
        [Client.get_supported_resource_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.get_supported_resource_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_backup_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        ByResourceArn: str = None,
        ByState: Literal[
            "CREATED", "PENDING", "RUNNING", "ABORTING", "ABORTED", "COMPLETED", "FAILED", "EXPIRED"
        ] = None,
        ByBackupVaultName: str = None,
        ByCreatedBefore: datetime = None,
        ByCreatedAfter: datetime = None,
        ByResourceType: str = None,
    ) -> ListBackupJobsOutputTypeDef:
        """
        [Client.list_backup_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.list_backup_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_backup_plan_templates(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupPlanTemplatesOutputTypeDef:
        """
        [Client.list_backup_plan_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.list_backup_plan_templates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_backup_plan_versions(
        self, BackupPlanId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupPlanVersionsOutputTypeDef:
        """
        [Client.list_backup_plan_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.list_backup_plan_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_backup_plans(
        self, NextToken: str = None, MaxResults: int = None, IncludeDeleted: bool = None
    ) -> ListBackupPlansOutputTypeDef:
        """
        [Client.list_backup_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.list_backup_plans)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_backup_selections(
        self, BackupPlanId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupSelectionsOutputTypeDef:
        """
        [Client.list_backup_selections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.list_backup_selections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_backup_vaults(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListBackupVaultsOutputTypeDef:
        """
        [Client.list_backup_vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.list_backup_vaults)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_protected_resources(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListProtectedResourcesOutputTypeDef:
        """
        [Client.list_protected_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.list_protected_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_recovery_points_by_backup_vault(
        self,
        BackupVaultName: str,
        NextToken: str = None,
        MaxResults: int = None,
        ByResourceArn: str = None,
        ByResourceType: str = None,
        ByBackupPlanId: str = None,
        ByCreatedBefore: datetime = None,
        ByCreatedAfter: datetime = None,
    ) -> ListRecoveryPointsByBackupVaultOutputTypeDef:
        """
        [Client.list_recovery_points_by_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.list_recovery_points_by_backup_vault)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_recovery_points_by_resource(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRecoveryPointsByResourceOutputTypeDef:
        """
        [Client.list_recovery_points_by_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.list_recovery_points_by_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_restore_jobs(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListRestoreJobsOutputTypeDef:
        """
        [Client.list_restore_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.list_restore_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsOutputTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.list_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_backup_vault_access_policy(self, BackupVaultName: str, Policy: str = None) -> None:
        """
        [Client.put_backup_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.put_backup_vault_access_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_backup_vault_notifications(
        self,
        BackupVaultName: str,
        SNSTopicArn: str,
        BackupVaultEvents: List[
            Literal[
                "BACKUP_JOB_STARTED",
                "BACKUP_JOB_COMPLETED",
                "RESTORE_JOB_STARTED",
                "RESTORE_JOB_COMPLETED",
                "RECOVERY_POINT_MODIFIED",
                "BACKUP_PLAN_CREATED",
                "BACKUP_PLAN_MODIFIED",
            ]
        ],
    ) -> None:
        """
        [Client.put_backup_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.put_backup_vault_notifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_backup_job(
        self,
        BackupVaultName: str,
        ResourceArn: str,
        IamRoleArn: str,
        IdempotencyToken: str = None,
        StartWindowMinutes: int = None,
        CompleteWindowMinutes: int = None,
        Lifecycle: LifecycleTypeDef = None,
        RecoveryPointTags: Dict[str, str] = None,
    ) -> StartBackupJobOutputTypeDef:
        """
        [Client.start_backup_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.start_backup_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_restore_job(
        self,
        RecoveryPointArn: str,
        Metadata: Dict[str, str],
        IamRoleArn: str,
        IdempotencyToken: str = None,
        ResourceType: str = None,
    ) -> StartRestoreJobOutputTypeDef:
        """
        [Client.start_restore_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.start_restore_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_backup_job(self, BackupJobId: str) -> None:
        """
        [Client.stop_backup_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.stop_backup_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeyList: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_backup_plan(
        self, BackupPlanId: str, BackupPlan: BackupPlanInputTypeDef
    ) -> UpdateBackupPlanOutputTypeDef:
        """
        [Client.update_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.update_backup_plan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_recovery_point_lifecycle(
        self, BackupVaultName: str, RecoveryPointArn: str, Lifecycle: LifecycleTypeDef = None
    ) -> UpdateRecoveryPointLifecycleOutputTypeDef:
        """
        [Client.update_recovery_point_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/backup.html#Backup.Client.update_recovery_point_lifecycle)
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    ClientError: Boto3ClientError
    DependencyFailureException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MissingParameterValueException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
