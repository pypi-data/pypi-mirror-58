"Main interface for redshift service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_redshift.client as client_scope

# pylint: disable=import-self
import mypy_boto3_redshift.paginator as paginator_scope
from mypy_boto3_redshift.type_defs import (
    AcceptReservedNodeExchangeOutputMessageTypeDef,
    AccountAttributeListTypeDef,
    AuthorizeClusterSecurityGroupIngressResultTypeDef,
    AuthorizeSnapshotAccessResultTypeDef,
    BatchDeleteClusterSnapshotsResultTypeDef,
    BatchModifyClusterSnapshotsOutputMessageTypeDef,
    ClusterCredentialsTypeDef,
    ClusterDbRevisionsMessageTypeDef,
    ClusterParameterGroupDetailsTypeDef,
    ClusterParameterGroupNameMessageTypeDef,
    ClusterParameterGroupsMessageTypeDef,
    ClusterSecurityGroupMessageTypeDef,
    ClusterSubnetGroupMessageTypeDef,
    ClusterVersionsMessageTypeDef,
    ClustersMessageTypeDef,
    CopyClusterSnapshotResultTypeDef,
    CreateClusterParameterGroupResultTypeDef,
    CreateClusterResultTypeDef,
    CreateClusterSecurityGroupResultTypeDef,
    CreateClusterSnapshotResultTypeDef,
    CreateClusterSubnetGroupResultTypeDef,
    CreateEventSubscriptionResultTypeDef,
    CreateHsmClientCertificateResultTypeDef,
    CreateHsmConfigurationResultTypeDef,
    CreateSnapshotCopyGrantResultTypeDef,
    CustomerStorageMessageTypeDef,
    DeleteClusterResultTypeDef,
    DeleteClusterSnapshotMessageTypeDef,
    DeleteClusterSnapshotResultTypeDef,
    DescribeDefaultClusterParametersResultTypeDef,
    DescribeSnapshotSchedulesOutputMessageTypeDef,
    DisableSnapshotCopyResultTypeDef,
    EnableSnapshotCopyResultTypeDef,
    EventCategoriesMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    EventsMessageTypeDef,
    GetReservedNodeExchangeOfferingsOutputMessageTypeDef,
    HsmClientCertificateMessageTypeDef,
    HsmConfigurationMessageTypeDef,
    LoggingStatusTypeDef,
    ModifyClusterDbRevisionResultTypeDef,
    ModifyClusterIamRolesResultTypeDef,
    ModifyClusterMaintenanceResultTypeDef,
    ModifyClusterResultTypeDef,
    ModifyClusterSnapshotResultTypeDef,
    ModifyClusterSubnetGroupResultTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    ModifySnapshotCopyRetentionPeriodResultTypeDef,
    NodeConfigurationOptionsFilterTypeDef,
    NodeConfigurationOptionsMessageTypeDef,
    OrderableClusterOptionsMessageTypeDef,
    ParameterTypeDef,
    PurchaseReservedNodeOfferingResultTypeDef,
    RebootClusterResultTypeDef,
    ReservedNodeOfferingsMessageTypeDef,
    ReservedNodesMessageTypeDef,
    ResizeClusterResultTypeDef,
    ResizeProgressMessageTypeDef,
    RestoreFromClusterSnapshotResultTypeDef,
    RestoreTableFromClusterSnapshotResultTypeDef,
    RevokeClusterSecurityGroupIngressResultTypeDef,
    RevokeSnapshotAccessResultTypeDef,
    RotateEncryptionKeyResultTypeDef,
    ScheduledActionFilterTypeDef,
    ScheduledActionTypeDef,
    ScheduledActionTypeTypeDef,
    ScheduledActionsMessageTypeDef,
    SnapshotCopyGrantMessageTypeDef,
    SnapshotMessageTypeDef,
    SnapshotScheduleTypeDef,
    SnapshotSortingEntityTypeDef,
    TableRestoreStatusMessageTypeDef,
    TagTypeDef,
    TaggedResourceListMessageTypeDef,
    TrackListMessageTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_redshift.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RedshiftClient",)


class RedshiftClient(BaseClient):
    """
    [Redshift.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_reserved_node_exchange(
        self, ReservedNodeId: str, TargetReservedNodeOfferingId: str
    ) -> AcceptReservedNodeExchangeOutputMessageTypeDef:
        """
        [Client.accept_reserved_node_exchange documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.accept_reserved_node_exchange)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_cluster_security_group_ingress(
        self,
        ClusterSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> AuthorizeClusterSecurityGroupIngressResultTypeDef:
        """
        [Client.authorize_cluster_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.authorize_cluster_security_group_ingress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_snapshot_access(
        self,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: str = None,
    ) -> AuthorizeSnapshotAccessResultTypeDef:
        """
        [Client.authorize_snapshot_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.authorize_snapshot_access)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_cluster_snapshots(
        self, Identifiers: List[DeleteClusterSnapshotMessageTypeDef]
    ) -> BatchDeleteClusterSnapshotsResultTypeDef:
        """
        [Client.batch_delete_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.batch_delete_cluster_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_modify_cluster_snapshots(
        self,
        SnapshotIdentifierList: List[str],
        ManualSnapshotRetentionPeriod: int = None,
        Force: bool = None,
    ) -> BatchModifyClusterSnapshotsOutputMessageTypeDef:
        """
        [Client.batch_modify_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.batch_modify_cluster_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_resize(self, ClusterIdentifier: str) -> ResizeProgressMessageTypeDef:
        """
        [Client.cancel_resize documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.cancel_resize)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_cluster_snapshot(
        self,
        SourceSnapshotIdentifier: str,
        TargetSnapshotIdentifier: str,
        SourceSnapshotClusterIdentifier: str = None,
        ManualSnapshotRetentionPeriod: int = None,
    ) -> CopyClusterSnapshotResultTypeDef:
        """
        [Client.copy_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.copy_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cluster(
        self,
        ClusterIdentifier: str,
        NodeType: str,
        MasterUsername: str,
        MasterUserPassword: str,
        DBName: str = None,
        ClusterType: str = None,
        ClusterSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        ClusterSubnetGroupName: str = None,
        AvailabilityZone: str = None,
        PreferredMaintenanceWindow: str = None,
        ClusterParameterGroupName: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        Port: int = None,
        ClusterVersion: str = None,
        AllowVersionUpgrade: bool = None,
        NumberOfNodes: int = None,
        PubliclyAccessible: bool = None,
        Encrypted: bool = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        ElasticIp: str = None,
        Tags: List[TagTypeDef] = None,
        KmsKeyId: str = None,
        EnhancedVpcRouting: bool = None,
        AdditionalInfo: str = None,
        IamRoles: List[str] = None,
        MaintenanceTrackName: str = None,
        SnapshotScheduleIdentifier: str = None,
    ) -> CreateClusterResultTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cluster_parameter_group(
        self,
        ParameterGroupName: str,
        ParameterGroupFamily: str,
        Description: str,
        Tags: List[TagTypeDef] = None,
    ) -> CreateClusterParameterGroupResultTypeDef:
        """
        [Client.create_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cluster_security_group(
        self, ClusterSecurityGroupName: str, Description: str, Tags: List[TagTypeDef] = None
    ) -> CreateClusterSecurityGroupResultTypeDef:
        """
        [Client.create_cluster_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_cluster_security_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cluster_snapshot(
        self,
        SnapshotIdentifier: str,
        ClusterIdentifier: str,
        ManualSnapshotRetentionPeriod: int = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateClusterSnapshotResultTypeDef:
        """
        [Client.create_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cluster_subnet_group(
        self,
        ClusterSubnetGroupName: str,
        Description: str,
        SubnetIds: List[str],
        Tags: List[TagTypeDef] = None,
    ) -> CreateClusterSubnetGroupResultTypeDef:
        """
        [Client.create_cluster_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_cluster_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        SourceIds: List[str] = None,
        EventCategories: List[str] = None,
        Severity: str = None,
        Enabled: bool = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        [Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_event_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_hsm_client_certificate(
        self, HsmClientCertificateIdentifier: str, Tags: List[TagTypeDef] = None
    ) -> CreateHsmClientCertificateResultTypeDef:
        """
        [Client.create_hsm_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_hsm_client_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_hsm_configuration(
        self,
        HsmConfigurationIdentifier: str,
        Description: str,
        HsmIpAddress: str,
        HsmPartitionName: str,
        HsmPartitionPassword: str,
        HsmServerPublicCertificate: str,
        Tags: List[TagTypeDef] = None,
    ) -> CreateHsmConfigurationResultTypeDef:
        """
        [Client.create_hsm_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_hsm_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_scheduled_action(
        self,
        ScheduledActionName: str,
        TargetAction: ScheduledActionTypeTypeDef,
        Schedule: str,
        IamRole: str,
        ScheduledActionDescription: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Enable: bool = None,
    ) -> ScheduledActionTypeDef:
        """
        [Client.create_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_scheduled_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot_copy_grant(
        self, SnapshotCopyGrantName: str, KmsKeyId: str = None, Tags: List[TagTypeDef] = None
    ) -> CreateSnapshotCopyGrantResultTypeDef:
        """
        [Client.create_snapshot_copy_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_snapshot_copy_grant)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot_schedule(
        self,
        ScheduleDefinitions: List[str] = None,
        ScheduleIdentifier: str = None,
        ScheduleDescription: str = None,
        Tags: List[TagTypeDef] = None,
        DryRun: bool = None,
        NextInvocations: int = None,
    ) -> SnapshotScheduleTypeDef:
        """
        [Client.create_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_snapshot_schedule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(self, ResourceName: str, Tags: List[TagTypeDef]) -> None:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cluster(
        self,
        ClusterIdentifier: str,
        SkipFinalClusterSnapshot: bool = None,
        FinalClusterSnapshotIdentifier: str = None,
        FinalClusterSnapshotRetentionPeriod: int = None,
    ) -> DeleteClusterResultTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cluster_parameter_group(self, ParameterGroupName: str) -> None:
        """
        [Client.delete_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cluster_security_group(self, ClusterSecurityGroupName: str) -> None:
        """
        [Client.delete_cluster_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_cluster_security_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cluster_snapshot(
        self, SnapshotIdentifier: str, SnapshotClusterIdentifier: str = None
    ) -> DeleteClusterSnapshotResultTypeDef:
        """
        [Client.delete_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cluster_subnet_group(self, ClusterSubnetGroupName: str) -> None:
        """
        [Client.delete_cluster_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_cluster_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_event_subscription(self, SubscriptionName: str) -> None:
        """
        [Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_event_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_hsm_client_certificate(self, HsmClientCertificateIdentifier: str) -> None:
        """
        [Client.delete_hsm_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_hsm_client_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_hsm_configuration(self, HsmConfigurationIdentifier: str) -> None:
        """
        [Client.delete_hsm_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_hsm_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_scheduled_action(self, ScheduledActionName: str) -> None:
        """
        [Client.delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_scheduled_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_snapshot_copy_grant(self, SnapshotCopyGrantName: str) -> None:
        """
        [Client.delete_snapshot_copy_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_snapshot_copy_grant)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_snapshot_schedule(self, ScheduleIdentifier: str) -> None:
        """
        [Client.delete_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_snapshot_schedule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tags(self, ResourceName: str, TagKeys: List[str]) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.delete_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_attributes(
        self, AttributeNames: List[str] = None
    ) -> AccountAttributeListTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_account_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster_db_revisions(
        self, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ClusterDbRevisionsMessageTypeDef:
        """
        [Client.describe_cluster_db_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_cluster_db_revisions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster_parameter_groups(
        self,
        ParameterGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> ClusterParameterGroupsMessageTypeDef:
        """
        [Client.describe_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_cluster_parameter_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster_parameters(
        self,
        ParameterGroupName: str,
        Source: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClusterParameterGroupDetailsTypeDef:
        """
        [Client.describe_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_cluster_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster_security_groups(
        self,
        ClusterSecurityGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> ClusterSecurityGroupMessageTypeDef:
        """
        [Client.describe_cluster_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_cluster_security_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster_snapshots(
        self,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        Marker: str = None,
        OwnerAccount: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        ClusterExists: bool = None,
        SortingEntities: List[SnapshotSortingEntityTypeDef] = None,
    ) -> SnapshotMessageTypeDef:
        """
        [Client.describe_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_cluster_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster_subnet_groups(
        self,
        ClusterSubnetGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> ClusterSubnetGroupMessageTypeDef:
        """
        [Client.describe_cluster_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_cluster_subnet_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster_tracks(
        self, MaintenanceTrackName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> TrackListMessageTypeDef:
        """
        [Client.describe_cluster_tracks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_cluster_tracks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster_versions(
        self,
        ClusterVersion: str = None,
        ClusterParameterGroupFamily: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClusterVersionsMessageTypeDef:
        """
        [Client.describe_cluster_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_cluster_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_clusters(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> ClustersMessageTypeDef:
        """
        [Client.describe_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_clusters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_default_cluster_parameters(
        self, ParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeDefaultClusterParametersResultTypeDef:
        """
        [Client.describe_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_default_cluster_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_categories(self, SourceType: str = None) -> EventCategoriesMessageTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_event_categories)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> EventSubscriptionsMessageTypeDef:
        """
        [Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_event_subscriptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventsMessageTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_hsm_client_certificates(
        self,
        HsmClientCertificateIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> HsmClientCertificateMessageTypeDef:
        """
        [Client.describe_hsm_client_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_hsm_client_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_hsm_configurations(
        self,
        HsmConfigurationIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> HsmConfigurationMessageTypeDef:
        """
        [Client.describe_hsm_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_hsm_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_logging_status(self, ClusterIdentifier: str) -> LoggingStatusTypeDef:
        """
        [Client.describe_logging_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_logging_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_node_configuration_options(
        self,
        ActionType: Literal["restore-cluster", "recommend-node-config"],
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        OwnerAccount: str = None,
        Filters: List[NodeConfigurationOptionsFilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> NodeConfigurationOptionsMessageTypeDef:
        """
        [Client.describe_node_configuration_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_node_configuration_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_orderable_cluster_options(
        self,
        ClusterVersion: str = None,
        NodeType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> OrderableClusterOptionsMessageTypeDef:
        """
        [Client.describe_orderable_cluster_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_orderable_cluster_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_node_offerings(
        self, ReservedNodeOfferingId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ReservedNodeOfferingsMessageTypeDef:
        """
        [Client.describe_reserved_node_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_reserved_node_offerings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_nodes(
        self, ReservedNodeId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ReservedNodesMessageTypeDef:
        """
        [Client.describe_reserved_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_reserved_nodes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_resize(self, ClusterIdentifier: str) -> ResizeProgressMessageTypeDef:
        """
        [Client.describe_resize documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_resize)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scheduled_actions(
        self,
        ScheduledActionName: str = None,
        TargetActionType: Literal["ResizeCluster"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Active: bool = None,
        Filters: List[ScheduledActionFilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> ScheduledActionsMessageTypeDef:
        """
        [Client.describe_scheduled_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_scheduled_actions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_snapshot_copy_grants(
        self,
        SnapshotCopyGrantName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> SnapshotCopyGrantMessageTypeDef:
        """
        [Client.describe_snapshot_copy_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_snapshot_copy_grants)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_snapshot_schedules(
        self,
        ClusterIdentifier: str = None,
        ScheduleIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> DescribeSnapshotSchedulesOutputMessageTypeDef:
        """
        [Client.describe_snapshot_schedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_snapshot_schedules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_storage(self) -> CustomerStorageMessageTypeDef:
        """
        [Client.describe_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_storage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_table_restore_status(
        self,
        ClusterIdentifier: str = None,
        TableRestoreRequestId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> TableRestoreStatusMessageTypeDef:
        """
        [Client.describe_table_restore_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_table_restore_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tags(
        self,
        ResourceName: str = None,
        ResourceType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
    ) -> TaggedResourceListMessageTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.describe_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_logging(self, ClusterIdentifier: str) -> LoggingStatusTypeDef:
        """
        [Client.disable_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.disable_logging)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_snapshot_copy(self, ClusterIdentifier: str) -> DisableSnapshotCopyResultTypeDef:
        """
        [Client.disable_snapshot_copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.disable_snapshot_copy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_logging(
        self, ClusterIdentifier: str, BucketName: str, S3KeyPrefix: str = None
    ) -> LoggingStatusTypeDef:
        """
        [Client.enable_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.enable_logging)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_snapshot_copy(
        self,
        ClusterIdentifier: str,
        DestinationRegion: str,
        RetentionPeriod: int = None,
        SnapshotCopyGrantName: str = None,
        ManualSnapshotRetentionPeriod: int = None,
    ) -> EnableSnapshotCopyResultTypeDef:
        """
        [Client.enable_snapshot_copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.enable_snapshot_copy)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cluster_credentials(
        self,
        DbUser: str,
        ClusterIdentifier: str,
        DbName: str = None,
        DurationSeconds: int = None,
        AutoCreate: bool = None,
        DbGroups: List[str] = None,
    ) -> ClusterCredentialsTypeDef:
        """
        [Client.get_cluster_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.get_cluster_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_reserved_node_exchange_offerings(
        self, ReservedNodeId: str, MaxRecords: int = None, Marker: str = None
    ) -> GetReservedNodeExchangeOfferingsOutputMessageTypeDef:
        """
        [Client.get_reserved_node_exchange_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.get_reserved_node_exchange_offerings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cluster(
        self,
        ClusterIdentifier: str,
        ClusterType: str = None,
        NodeType: str = None,
        NumberOfNodes: int = None,
        ClusterSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        MasterUserPassword: str = None,
        ClusterParameterGroupName: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        PreferredMaintenanceWindow: str = None,
        ClusterVersion: str = None,
        AllowVersionUpgrade: bool = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        NewClusterIdentifier: str = None,
        PubliclyAccessible: bool = None,
        ElasticIp: str = None,
        EnhancedVpcRouting: bool = None,
        MaintenanceTrackName: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
    ) -> ModifyClusterResultTypeDef:
        """
        [Client.modify_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cluster_db_revision(
        self, ClusterIdentifier: str, RevisionTarget: str
    ) -> ModifyClusterDbRevisionResultTypeDef:
        """
        [Client.modify_cluster_db_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_cluster_db_revision)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cluster_iam_roles(
        self,
        ClusterIdentifier: str,
        AddIamRoles: List[str] = None,
        RemoveIamRoles: List[str] = None,
    ) -> ModifyClusterIamRolesResultTypeDef:
        """
        [Client.modify_cluster_iam_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_cluster_iam_roles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cluster_maintenance(
        self,
        ClusterIdentifier: str,
        DeferMaintenance: bool = None,
        DeferMaintenanceIdentifier: str = None,
        DeferMaintenanceStartTime: datetime = None,
        DeferMaintenanceEndTime: datetime = None,
        DeferMaintenanceDuration: int = None,
    ) -> ModifyClusterMaintenanceResultTypeDef:
        """
        [Client.modify_cluster_maintenance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_cluster_maintenance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cluster_parameter_group(
        self, ParameterGroupName: str, Parameters: List[ParameterTypeDef]
    ) -> ClusterParameterGroupNameMessageTypeDef:
        """
        [Client.modify_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cluster_snapshot(
        self, SnapshotIdentifier: str, ManualSnapshotRetentionPeriod: int = None, Force: bool = None
    ) -> ModifyClusterSnapshotResultTypeDef:
        """
        [Client.modify_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cluster_snapshot_schedule(
        self,
        ClusterIdentifier: str,
        ScheduleIdentifier: str = None,
        DisassociateSchedule: bool = None,
    ) -> None:
        """
        [Client.modify_cluster_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_cluster_snapshot_schedule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_cluster_subnet_group(
        self, ClusterSubnetGroupName: str, SubnetIds: List[str], Description: str = None
    ) -> ModifyClusterSubnetGroupResultTypeDef:
        """
        [Client.modify_cluster_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_cluster_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        SourceIds: List[str] = None,
        EventCategories: List[str] = None,
        Severity: str = None,
        Enabled: bool = None,
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        [Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_event_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_scheduled_action(
        self,
        ScheduledActionName: str,
        TargetAction: ScheduledActionTypeTypeDef = None,
        Schedule: str = None,
        IamRole: str = None,
        ScheduledActionDescription: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Enable: bool = None,
    ) -> ScheduledActionTypeDef:
        """
        [Client.modify_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_scheduled_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_snapshot_copy_retention_period(
        self, ClusterIdentifier: str, RetentionPeriod: int, Manual: bool = None
    ) -> ModifySnapshotCopyRetentionPeriodResultTypeDef:
        """
        [Client.modify_snapshot_copy_retention_period documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_snapshot_copy_retention_period)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_snapshot_schedule(
        self, ScheduleIdentifier: str, ScheduleDefinitions: List[str]
    ) -> SnapshotScheduleTypeDef:
        """
        [Client.modify_snapshot_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.modify_snapshot_schedule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purchase_reserved_node_offering(
        self, ReservedNodeOfferingId: str, NodeCount: int = None
    ) -> PurchaseReservedNodeOfferingResultTypeDef:
        """
        [Client.purchase_reserved_node_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.purchase_reserved_node_offering)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot_cluster(self, ClusterIdentifier: str) -> RebootClusterResultTypeDef:
        """
        [Client.reboot_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.reboot_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_cluster_parameter_group(
        self,
        ParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[ParameterTypeDef] = None,
    ) -> ClusterParameterGroupNameMessageTypeDef:
        """
        [Client.reset_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.reset_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resize_cluster(
        self,
        ClusterIdentifier: str,
        NumberOfNodes: int,
        ClusterType: str = None,
        NodeType: str = None,
        Classic: bool = None,
    ) -> ResizeClusterResultTypeDef:
        """
        [Client.resize_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.resize_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_from_cluster_snapshot(
        self,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SnapshotClusterIdentifier: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        AllowVersionUpgrade: bool = None,
        ClusterSubnetGroupName: str = None,
        PubliclyAccessible: bool = None,
        OwnerAccount: str = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        ElasticIp: str = None,
        ClusterParameterGroupName: str = None,
        ClusterSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        KmsKeyId: str = None,
        NodeType: str = None,
        EnhancedVpcRouting: bool = None,
        AdditionalInfo: str = None,
        IamRoles: List[str] = None,
        MaintenanceTrackName: str = None,
        SnapshotScheduleIdentifier: str = None,
        NumberOfNodes: int = None,
    ) -> RestoreFromClusterSnapshotResultTypeDef:
        """
        [Client.restore_from_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.restore_from_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_table_from_cluster_snapshot(
        self,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SourceDatabaseName: str,
        SourceTableName: str,
        NewTableName: str,
        SourceSchemaName: str = None,
        TargetDatabaseName: str = None,
        TargetSchemaName: str = None,
    ) -> RestoreTableFromClusterSnapshotResultTypeDef:
        """
        [Client.restore_table_from_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.restore_table_from_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_cluster_security_group_ingress(
        self,
        ClusterSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> RevokeClusterSecurityGroupIngressResultTypeDef:
        """
        [Client.revoke_cluster_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.revoke_cluster_security_group_ingress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_snapshot_access(
        self,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: str = None,
    ) -> RevokeSnapshotAccessResultTypeDef:
        """
        [Client.revoke_snapshot_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.revoke_snapshot_access)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def rotate_encryption_key(self, ClusterIdentifier: str) -> RotateEncryptionKeyResultTypeDef:
        """
        [Client.rotate_encryption_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Client.rotate_encryption_key)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cluster_db_revisions"]
    ) -> paginator_scope.DescribeClusterDbRevisionsPaginator:
        """
        [Paginator.DescribeClusterDbRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeClusterDbRevisions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cluster_parameter_groups"]
    ) -> paginator_scope.DescribeClusterParameterGroupsPaginator:
        """
        [Paginator.DescribeClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameterGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cluster_parameters"]
    ) -> paginator_scope.DescribeClusterParametersPaginator:
        """
        [Paginator.DescribeClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cluster_security_groups"]
    ) -> paginator_scope.DescribeClusterSecurityGroupsPaginator:
        """
        [Paginator.DescribeClusterSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSecurityGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cluster_snapshots"]
    ) -> paginator_scope.DescribeClusterSnapshotsPaginator:
        """
        [Paginator.DescribeClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSnapshots)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cluster_subnet_groups"]
    ) -> paginator_scope.DescribeClusterSubnetGroupsPaginator:
        """
        [Paginator.DescribeClusterSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSubnetGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cluster_tracks"]
    ) -> paginator_scope.DescribeClusterTracksPaginator:
        """
        [Paginator.DescribeClusterTracks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeClusterTracks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cluster_versions"]
    ) -> paginator_scope.DescribeClusterVersionsPaginator:
        """
        [Paginator.DescribeClusterVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeClusterVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_clusters"]
    ) -> paginator_scope.DescribeClustersPaginator:
        """
        [Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeClusters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_default_cluster_parameters"]
    ) -> paginator_scope.DescribeDefaultClusterParametersPaginator:
        """
        [Paginator.DescribeDefaultClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeDefaultClusterParameters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> paginator_scope.DescribeEventSubscriptionsPaginator:
        """
        [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeEventSubscriptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> paginator_scope.DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeEvents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_hsm_client_certificates"]
    ) -> paginator_scope.DescribeHsmClientCertificatesPaginator:
        """
        [Paginator.DescribeHsmClientCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeHsmClientCertificates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_hsm_configurations"]
    ) -> paginator_scope.DescribeHsmConfigurationsPaginator:
        """
        [Paginator.DescribeHsmConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeHsmConfigurations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_node_configuration_options"]
    ) -> paginator_scope.DescribeNodeConfigurationOptionsPaginator:
        """
        [Paginator.DescribeNodeConfigurationOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeNodeConfigurationOptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_orderable_cluster_options"]
    ) -> paginator_scope.DescribeOrderableClusterOptionsPaginator:
        """
        [Paginator.DescribeOrderableClusterOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeOrderableClusterOptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_reserved_node_offerings"]
    ) -> paginator_scope.DescribeReservedNodeOfferingsPaginator:
        """
        [Paginator.DescribeReservedNodeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeOfferings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_reserved_nodes"]
    ) -> paginator_scope.DescribeReservedNodesPaginator:
        """
        [Paginator.DescribeReservedNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> paginator_scope.DescribeScheduledActionsPaginator:
        """
        [Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeScheduledActions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_snapshot_copy_grants"]
    ) -> paginator_scope.DescribeSnapshotCopyGrantsPaginator:
        """
        [Paginator.DescribeSnapshotCopyGrants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotCopyGrants)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_snapshot_schedules"]
    ) -> paginator_scope.DescribeSnapshotSchedulesPaginator:
        """
        [Paginator.DescribeSnapshotSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotSchedules)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_table_restore_status"]
    ) -> paginator_scope.DescribeTableRestoreStatusPaginator:
        """
        [Paginator.DescribeTableRestoreStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeTableRestoreStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_tags"]
    ) -> paginator_scope.DescribeTagsPaginator:
        """
        [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.DescribeTags)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_reserved_node_exchange_offerings"]
    ) -> paginator_scope.GetReservedNodeExchangeOfferingsPaginator:
        """
        [Paginator.GetReservedNodeExchangeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeOfferings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["cluster_available"]
    ) -> waiter_scope.ClusterAvailableWaiter:
        """
        [Waiter.ClusterAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Waiter.ClusterAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["cluster_deleted"]
    ) -> waiter_scope.ClusterDeletedWaiter:
        """
        [Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Waiter.ClusterDeleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["cluster_restored"]
    ) -> waiter_scope.ClusterRestoredWaiter:
        """
        [Waiter.ClusterRestored documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Waiter.ClusterRestored)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["snapshot_available"]
    ) -> waiter_scope.SnapshotAvailableWaiter:
        """
        [Waiter.SnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/redshift.html#Redshift.Waiter.SnapshotAvailable)
        """


class Exceptions:
    AccessToSnapshotDeniedFault: Boto3ClientError
    AuthorizationAlreadyExistsFault: Boto3ClientError
    AuthorizationNotFoundFault: Boto3ClientError
    AuthorizationQuotaExceededFault: Boto3ClientError
    BatchDeleteRequestSizeExceededFault: Boto3ClientError
    BatchModifyClusterSnapshotsLimitExceededFault: Boto3ClientError
    BucketNotFoundFault: Boto3ClientError
    ClientError: Boto3ClientError
    ClusterAlreadyExistsFault: Boto3ClientError
    ClusterNotFoundFault: Boto3ClientError
    ClusterOnLatestRevisionFault: Boto3ClientError
    ClusterParameterGroupAlreadyExistsFault: Boto3ClientError
    ClusterParameterGroupNotFoundFault: Boto3ClientError
    ClusterParameterGroupQuotaExceededFault: Boto3ClientError
    ClusterQuotaExceededFault: Boto3ClientError
    ClusterSecurityGroupAlreadyExistsFault: Boto3ClientError
    ClusterSecurityGroupNotFoundFault: Boto3ClientError
    ClusterSecurityGroupQuotaExceededFault: Boto3ClientError
    ClusterSnapshotAlreadyExistsFault: Boto3ClientError
    ClusterSnapshotNotFoundFault: Boto3ClientError
    ClusterSnapshotQuotaExceededFault: Boto3ClientError
    ClusterSubnetGroupAlreadyExistsFault: Boto3ClientError
    ClusterSubnetGroupNotFoundFault: Boto3ClientError
    ClusterSubnetGroupQuotaExceededFault: Boto3ClientError
    ClusterSubnetQuotaExceededFault: Boto3ClientError
    CopyToRegionDisabledFault: Boto3ClientError
    DependentServiceRequestThrottlingFault: Boto3ClientError
    DependentServiceUnavailableFault: Boto3ClientError
    EventSubscriptionQuotaExceededFault: Boto3ClientError
    HsmClientCertificateAlreadyExistsFault: Boto3ClientError
    HsmClientCertificateNotFoundFault: Boto3ClientError
    HsmClientCertificateQuotaExceededFault: Boto3ClientError
    HsmConfigurationAlreadyExistsFault: Boto3ClientError
    HsmConfigurationNotFoundFault: Boto3ClientError
    HsmConfigurationQuotaExceededFault: Boto3ClientError
    InProgressTableRestoreQuotaExceededFault: Boto3ClientError
    IncompatibleOrderableOptions: Boto3ClientError
    InsufficientClusterCapacityFault: Boto3ClientError
    InsufficientS3BucketPolicyFault: Boto3ClientError
    InvalidClusterParameterGroupStateFault: Boto3ClientError
    InvalidClusterSecurityGroupStateFault: Boto3ClientError
    InvalidClusterSnapshotScheduleStateFault: Boto3ClientError
    InvalidClusterSnapshotStateFault: Boto3ClientError
    InvalidClusterStateFault: Boto3ClientError
    InvalidClusterSubnetGroupStateFault: Boto3ClientError
    InvalidClusterSubnetStateFault: Boto3ClientError
    InvalidClusterTrackFault: Boto3ClientError
    InvalidElasticIpFault: Boto3ClientError
    InvalidHsmClientCertificateStateFault: Boto3ClientError
    InvalidHsmConfigurationStateFault: Boto3ClientError
    InvalidReservedNodeStateFault: Boto3ClientError
    InvalidRestoreFault: Boto3ClientError
    InvalidRetentionPeriodFault: Boto3ClientError
    InvalidS3BucketNameFault: Boto3ClientError
    InvalidS3KeyPrefixFault: Boto3ClientError
    InvalidScheduleFault: Boto3ClientError
    InvalidScheduledActionFault: Boto3ClientError
    InvalidSnapshotCopyGrantStateFault: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    InvalidSubscriptionStateFault: Boto3ClientError
    InvalidTableRestoreArgumentFault: Boto3ClientError
    InvalidTagFault: Boto3ClientError
    InvalidVPCNetworkStateFault: Boto3ClientError
    LimitExceededFault: Boto3ClientError
    NumberOfNodesPerClusterLimitExceededFault: Boto3ClientError
    NumberOfNodesQuotaExceededFault: Boto3ClientError
    ReservedNodeAlreadyExistsFault: Boto3ClientError
    ReservedNodeAlreadyMigratedFault: Boto3ClientError
    ReservedNodeNotFoundFault: Boto3ClientError
    ReservedNodeOfferingNotFoundFault: Boto3ClientError
    ReservedNodeQuotaExceededFault: Boto3ClientError
    ResizeNotFoundFault: Boto3ClientError
    ResourceNotFoundFault: Boto3ClientError
    SNSInvalidTopicFault: Boto3ClientError
    SNSNoAuthorizationFault: Boto3ClientError
    SNSTopicArnNotFoundFault: Boto3ClientError
    ScheduleDefinitionTypeUnsupportedFault: Boto3ClientError
    ScheduledActionAlreadyExistsFault: Boto3ClientError
    ScheduledActionNotFoundFault: Boto3ClientError
    ScheduledActionQuotaExceededFault: Boto3ClientError
    ScheduledActionTypeUnsupportedFault: Boto3ClientError
    SnapshotCopyAlreadyDisabledFault: Boto3ClientError
    SnapshotCopyAlreadyEnabledFault: Boto3ClientError
    SnapshotCopyDisabledFault: Boto3ClientError
    SnapshotCopyGrantAlreadyExistsFault: Boto3ClientError
    SnapshotCopyGrantNotFoundFault: Boto3ClientError
    SnapshotCopyGrantQuotaExceededFault: Boto3ClientError
    SnapshotScheduleAlreadyExistsFault: Boto3ClientError
    SnapshotScheduleNotFoundFault: Boto3ClientError
    SnapshotScheduleQuotaExceededFault: Boto3ClientError
    SnapshotScheduleUpdateInProgressFault: Boto3ClientError
    SourceNotFoundFault: Boto3ClientError
    SubnetAlreadyInUse: Boto3ClientError
    SubscriptionAlreadyExistFault: Boto3ClientError
    SubscriptionCategoryNotFoundFault: Boto3ClientError
    SubscriptionEventIdNotFoundFault: Boto3ClientError
    SubscriptionNotFoundFault: Boto3ClientError
    SubscriptionSeverityNotFoundFault: Boto3ClientError
    TableLimitExceededFault: Boto3ClientError
    TableRestoreNotFoundFault: Boto3ClientError
    TagLimitExceededFault: Boto3ClientError
    UnauthorizedOperation: Boto3ClientError
    UnknownSnapshotCopyRegionFault: Boto3ClientError
    UnsupportedOperationFault: Boto3ClientError
    UnsupportedOptionFault: Boto3ClientError
