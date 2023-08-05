"Main interface for rds service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_rds.client as client_scope

# pylint: disable=import-self
import mypy_boto3_rds.paginator as paginator_scope
from mypy_boto3_rds.type_defs import (
    AccountAttributesMessageTypeDef,
    AddSourceIdentifierToSubscriptionResultTypeDef,
    ApplyPendingMaintenanceActionResultTypeDef,
    AuthorizeDBSecurityGroupIngressResultTypeDef,
    CertificateMessageTypeDef,
    CloudwatchLogsExportConfigurationTypeDef,
    ConnectionPoolConfigurationTypeDef,
    CopyDBClusterParameterGroupResultTypeDef,
    CopyDBClusterSnapshotResultTypeDef,
    CopyDBParameterGroupResultTypeDef,
    CopyDBSnapshotResultTypeDef,
    CopyOptionGroupResultTypeDef,
    CreateCustomAvailabilityZoneResultTypeDef,
    CreateDBClusterParameterGroupResultTypeDef,
    CreateDBClusterResultTypeDef,
    CreateDBClusterSnapshotResultTypeDef,
    CreateDBInstanceReadReplicaResultTypeDef,
    CreateDBInstanceResultTypeDef,
    CreateDBParameterGroupResultTypeDef,
    CreateDBProxyResponseTypeDef,
    CreateDBSecurityGroupResultTypeDef,
    CreateDBSnapshotResultTypeDef,
    CreateDBSubnetGroupResultTypeDef,
    CreateEventSubscriptionResultTypeDef,
    CreateGlobalClusterResultTypeDef,
    CreateOptionGroupResultTypeDef,
    CustomAvailabilityZoneMessageTypeDef,
    DBClusterBacktrackMessageTypeDef,
    DBClusterBacktrackTypeDef,
    DBClusterCapacityInfoTypeDef,
    DBClusterEndpointMessageTypeDef,
    DBClusterEndpointTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupNameMessageTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceAutomatedBackupMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBParameterGroupDetailsTypeDef,
    DBParameterGroupNameMessageTypeDef,
    DBParameterGroupsMessageTypeDef,
    DBSecurityGroupMessageTypeDef,
    DBSnapshotMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DeleteCustomAvailabilityZoneResultTypeDef,
    DeleteDBClusterResultTypeDef,
    DeleteDBClusterSnapshotResultTypeDef,
    DeleteDBInstanceAutomatedBackupResultTypeDef,
    DeleteDBInstanceResultTypeDef,
    DeleteDBProxyResponseTypeDef,
    DeleteDBSnapshotResultTypeDef,
    DeleteEventSubscriptionResultTypeDef,
    DeleteGlobalClusterResultTypeDef,
    DescribeDBClusterSnapshotAttributesResultTypeDef,
    DescribeDBLogFilesResponseTypeDef,
    DescribeDBProxiesResponseTypeDef,
    DescribeDBProxyTargetGroupsResponseTypeDef,
    DescribeDBProxyTargetsResponseTypeDef,
    DescribeDBSnapshotAttributesResultTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeValidDBInstanceModificationsResultTypeDef,
    DownloadDBLogFilePortionDetailsTypeDef,
    EventCategoriesMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    EventsMessageTypeDef,
    FailoverDBClusterResultTypeDef,
    FilterTypeDef,
    GlobalClustersMessageTypeDef,
    InstallationMediaMessageTypeDef,
    InstallationMediaTypeDef,
    ModifyDBClusterResultTypeDef,
    ModifyDBClusterSnapshotAttributeResultTypeDef,
    ModifyDBInstanceResultTypeDef,
    ModifyDBProxyResponseTypeDef,
    ModifyDBProxyTargetGroupResponseTypeDef,
    ModifyDBSnapshotAttributeResultTypeDef,
    ModifyDBSnapshotResultTypeDef,
    ModifyDBSubnetGroupResultTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    ModifyGlobalClusterResultTypeDef,
    ModifyOptionGroupResultTypeDef,
    OptionConfigurationTypeDef,
    OptionGroupOptionsMessageTypeDef,
    OptionGroupsTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    ParameterTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    ProcessorFeatureTypeDef,
    PromoteReadReplicaDBClusterResultTypeDef,
    PromoteReadReplicaResultTypeDef,
    PurchaseReservedDBInstancesOfferingResultTypeDef,
    RebootDBInstanceResultTypeDef,
    RegisterDBProxyTargetsResponseTypeDef,
    RemoveFromGlobalClusterResultTypeDef,
    RemoveSourceIdentifierFromSubscriptionResultTypeDef,
    ReservedDBInstanceMessageTypeDef,
    ReservedDBInstancesOfferingMessageTypeDef,
    RestoreDBClusterFromS3ResultTypeDef,
    RestoreDBClusterFromSnapshotResultTypeDef,
    RestoreDBClusterToPointInTimeResultTypeDef,
    RestoreDBInstanceFromDBSnapshotResultTypeDef,
    RestoreDBInstanceFromS3ResultTypeDef,
    RestoreDBInstanceToPointInTimeResultTypeDef,
    RevokeDBSecurityGroupIngressResultTypeDef,
    ScalingConfigurationTypeDef,
    SourceRegionMessageTypeDef,
    StartActivityStreamResponseTypeDef,
    StartDBClusterResultTypeDef,
    StartDBInstanceResultTypeDef,
    StopActivityStreamResponseTypeDef,
    StopDBClusterResultTypeDef,
    StopDBInstanceResultTypeDef,
    TagListMessageTypeDef,
    TagTypeDef,
    UserAuthConfigTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_rds.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RDSClient",)


class RDSClient(BaseClient):
    """
    [RDS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_role_to_db_cluster(
        self, DBClusterIdentifier: str, RoleArn: str, FeatureName: str = None
    ) -> None:
        """
        [Client.add_role_to_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.add_role_to_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_role_to_db_instance(
        self, DBInstanceIdentifier: str, RoleArn: str, FeatureName: str
    ) -> None:
        """
        [Client.add_role_to_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.add_role_to_db_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_source_identifier_to_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> AddSourceIdentifierToSubscriptionResultTypeDef:
        """
        [Client.add_source_identifier_to_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.add_source_identifier_to_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_resource(self, ResourceName: str, Tags: List[TagTypeDef]) -> None:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.add_tags_to_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def apply_pending_maintenance_action(
        self, ResourceIdentifier: str, ApplyAction: str, OptInType: str
    ) -> ApplyPendingMaintenanceActionResultTypeDef:
        """
        [Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.apply_pending_maintenance_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_db_security_group_ingress(
        self,
        DBSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupId: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> AuthorizeDBSecurityGroupIngressResultTypeDef:
        """
        [Client.authorize_db_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.authorize_db_security_group_ingress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def backtrack_db_cluster(
        self,
        DBClusterIdentifier: str,
        BacktrackTo: datetime,
        Force: bool = None,
        UseEarliestTimeOnPointInTimeUnavailable: bool = None,
    ) -> DBClusterBacktrackTypeDef:
        """
        [Client.backtrack_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.backtrack_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_db_cluster_parameter_group(
        self,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: List[TagTypeDef] = None,
    ) -> CopyDBClusterParameterGroupResultTypeDef:
        """
        [Client.copy_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.copy_db_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_db_cluster_snapshot(
        self,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        CopyTags: bool = None,
        Tags: List[TagTypeDef] = None,
        SourceRegion: str = None,
    ) -> CopyDBClusterSnapshotResultTypeDef:
        """
        [Client.copy_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.copy_db_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_db_parameter_group(
        self,
        SourceDBParameterGroupIdentifier: str,
        TargetDBParameterGroupIdentifier: str,
        TargetDBParameterGroupDescription: str,
        Tags: List[TagTypeDef] = None,
    ) -> CopyDBParameterGroupResultTypeDef:
        """
        [Client.copy_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.copy_db_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_db_snapshot(
        self,
        SourceDBSnapshotIdentifier: str,
        TargetDBSnapshotIdentifier: str,
        KmsKeyId: str = None,
        Tags: List[TagTypeDef] = None,
        CopyTags: bool = None,
        PreSignedUrl: str = None,
        OptionGroupName: str = None,
        SourceRegion: str = None,
    ) -> CopyDBSnapshotResultTypeDef:
        """
        [Client.copy_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.copy_db_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_option_group(
        self,
        SourceOptionGroupIdentifier: str,
        TargetOptionGroupIdentifier: str,
        TargetOptionGroupDescription: str,
        Tags: List[TagTypeDef] = None,
    ) -> CopyOptionGroupResultTypeDef:
        """
        [Client.copy_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.copy_option_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_custom_availability_zone(
        self,
        CustomAvailabilityZoneName: str,
        ExistingVpnId: str = None,
        NewVpnTunnelName: str = None,
        VpnTunnelOriginatorIP: str = None,
    ) -> CreateCustomAvailabilityZoneResultTypeDef:
        """
        [Client.create_custom_availability_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_custom_availability_zone)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_cluster(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        BackupRetentionPeriod: int = None,
        CharacterSetName: str = None,
        DatabaseName: str = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        ReplicationSourceIdentifier: str = None,
        Tags: List[TagTypeDef] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        EngineMode: str = None,
        ScalingConfiguration: ScalingConfigurationTypeDef = None,
        DeletionProtection: bool = None,
        GlobalClusterIdentifier: str = None,
        EnableHttpEndpoint: bool = None,
        CopyTagsToSnapshot: bool = None,
        SourceRegion: str = None,
    ) -> CreateDBClusterResultTypeDef:
        """
        [Client.create_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_cluster_endpoint(
        self,
        DBClusterIdentifier: str,
        DBClusterEndpointIdentifier: str,
        EndpointType: str,
        StaticMembers: List[str] = None,
        ExcludedMembers: List[str] = None,
        Tags: List[TagTypeDef] = None,
    ) -> DBClusterEndpointTypeDef:
        """
        [Client.create_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_db_cluster_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDBClusterParameterGroupResultTypeDef:
        """
        [Client.create_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_db_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_cluster_snapshot(
        self,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDBClusterSnapshotResultTypeDef:
        """
        [Client.create_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_db_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBName: str = None,
        AllocatedStorage: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        DBSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        PreferredMaintenanceWindow: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        CharacterSetName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List[TagTypeDef] = None,
        DBClusterIdentifier: str = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        DomainIAMRoleName: str = None,
        PromotionTier: int = None,
        Timezone: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List[ProcessorFeatureTypeDef] = None,
        DeletionProtection: bool = None,
        MaxAllocatedStorage: int = None,
    ) -> CreateDBInstanceResultTypeDef:
        """
        [Client.create_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_db_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_instance_read_replica(
        self,
        DBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str,
        DBInstanceClass: str = None,
        AvailabilityZone: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        Iops: int = None,
        OptionGroupName: str = None,
        DBParameterGroupName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List[TagTypeDef] = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        StorageType: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List[ProcessorFeatureTypeDef] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
        SourceRegion: str = None,
    ) -> CreateDBInstanceReadReplicaResultTypeDef:
        """
        [Client.create_db_instance_read_replica documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_db_instance_read_replica)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_parameter_group(
        self,
        DBParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDBParameterGroupResultTypeDef:
        """
        [Client.create_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_db_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_proxy(
        self,
        DBProxyName: str,
        EngineFamily: Literal["MYSQL"],
        Auth: List[UserAuthConfigTypeDef],
        RoleArn: str,
        VpcSubnetIds: List[str],
        VpcSecurityGroupIds: List[str] = None,
        RequireTLS: bool = None,
        IdleClientTimeout: int = None,
        DebugLogging: bool = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDBProxyResponseTypeDef:
        """
        [Client.create_db_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_db_proxy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_security_group(
        self,
        DBSecurityGroupName: str,
        DBSecurityGroupDescription: str,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDBSecurityGroupResultTypeDef:
        """
        [Client.create_db_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_db_security_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_snapshot(
        self, DBSnapshotIdentifier: str, DBInstanceIdentifier: str, Tags: List[TagTypeDef] = None
    ) -> CreateDBSnapshotResultTypeDef:
        """
        [Client.create_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_db_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List[TagTypeDef] = None,
    ) -> CreateDBSubnetGroupResultTypeDef:
        """
        [Client.create_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_db_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        EventCategories: List[str] = None,
        SourceIds: List[str] = None,
        Enabled: bool = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        [Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_event_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_global_cluster(
        self,
        GlobalClusterIdentifier: str = None,
        SourceDBClusterIdentifier: str = None,
        Engine: str = None,
        EngineVersion: str = None,
        DeletionProtection: bool = None,
        DatabaseName: str = None,
        StorageEncrypted: bool = None,
    ) -> CreateGlobalClusterResultTypeDef:
        """
        [Client.create_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_global_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_option_group(
        self,
        OptionGroupName: str,
        EngineName: str,
        MajorEngineVersion: str,
        OptionGroupDescription: str,
        Tags: List[TagTypeDef] = None,
    ) -> CreateOptionGroupResultTypeDef:
        """
        [Client.create_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.create_option_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_custom_availability_zone(
        self, CustomAvailabilityZoneId: str
    ) -> DeleteCustomAvailabilityZoneResultTypeDef:
        """
        [Client.delete_custom_availability_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_custom_availability_zone)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
    ) -> DeleteDBClusterResultTypeDef:
        """
        [Client.delete_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_cluster_endpoint(
        self, DBClusterEndpointIdentifier: str
    ) -> DBClusterEndpointTypeDef:
        """
        [Client.delete_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_db_cluster_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str) -> None:
        """
        [Client.delete_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_db_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_cluster_snapshot(
        self, DBClusterSnapshotIdentifier: str
    ) -> DeleteDBClusterSnapshotResultTypeDef:
        """
        [Client.delete_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_db_cluster_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_instance(
        self,
        DBInstanceIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
        DeleteAutomatedBackups: bool = None,
    ) -> DeleteDBInstanceResultTypeDef:
        """
        [Client.delete_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_db_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_instance_automated_backup(
        self, DbiResourceId: str
    ) -> DeleteDBInstanceAutomatedBackupResultTypeDef:
        """
        [Client.delete_db_instance_automated_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_db_instance_automated_backup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_parameter_group(self, DBParameterGroupName: str) -> None:
        """
        [Client.delete_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_db_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_proxy(self, DBProxyName: str) -> DeleteDBProxyResponseTypeDef:
        """
        [Client.delete_db_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_db_proxy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_security_group(self, DBSecurityGroupName: str) -> None:
        """
        [Client.delete_db_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_db_security_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_snapshot(self, DBSnapshotIdentifier: str) -> DeleteDBSnapshotResultTypeDef:
        """
        [Client.delete_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_db_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_db_subnet_group(self, DBSubnetGroupName: str) -> None:
        """
        [Client.delete_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_db_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_event_subscription(
        self, SubscriptionName: str
    ) -> DeleteEventSubscriptionResultTypeDef:
        """
        [Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_event_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_global_cluster(
        self, GlobalClusterIdentifier: str
    ) -> DeleteGlobalClusterResultTypeDef:
        """
        [Client.delete_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_global_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_installation_media(self, InstallationMediaId: str) -> InstallationMediaTypeDef:
        """
        [Client.delete_installation_media documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_installation_media)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_option_group(self, OptionGroupName: str) -> None:
        """
        [Client.delete_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.delete_option_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_db_proxy_targets(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        DBInstanceIdentifiers: List[str] = None,
        DBClusterIdentifiers: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.deregister_db_proxy_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.deregister_db_proxy_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_attributes(self) -> AccountAttributesMessageTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_account_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_certificates(
        self,
        CertificateIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> CertificateMessageTypeDef:
        """
        [Client.describe_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_custom_availability_zones(
        self,
        CustomAvailabilityZoneId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> CustomAvailabilityZoneMessageTypeDef:
        """
        [Client.describe_custom_availability_zones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_custom_availability_zones)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_cluster_backtracks(
        self,
        DBClusterIdentifier: str,
        BacktrackIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterBacktrackMessageTypeDef:
        """
        [Client.describe_db_cluster_backtracks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_cluster_backtracks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_cluster_endpoints(
        self,
        DBClusterIdentifier: str = None,
        DBClusterEndpointIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterEndpointMessageTypeDef:
        """
        [Client.describe_db_cluster_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_cluster_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_cluster_parameter_groups(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterParameterGroupsMessageTypeDef:
        """
        [Client.describe_db_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_cluster_parameter_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_cluster_parameters(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterParameterGroupDetailsTypeDef:
        """
        [Client.describe_db_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_cluster_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_cluster_snapshot_attributes(
        self, DBClusterSnapshotIdentifier: str
    ) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
        """
        [Client.describe_db_cluster_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshot_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_cluster_snapshots(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
    ) -> DBClusterSnapshotMessageTypeDef:
        """
        [Client.describe_db_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_clusters(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
    ) -> DBClusterMessageTypeDef:
        """
        [Client.describe_db_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_clusters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
        IncludeAll: bool = None,
    ) -> DBEngineVersionMessageTypeDef:
        """
        [Client.describe_db_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_engine_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_instance_automated_backups(
        self,
        DbiResourceId: str = None,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBInstanceAutomatedBackupMessageTypeDef:
        """
        [Client.describe_db_instance_automated_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_instance_automated_backups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_instances(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBInstanceMessageTypeDef:
        """
        [Client.describe_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_log_files(
        self,
        DBInstanceIdentifier: str,
        FilenameContains: str = None,
        FileLastWritten: int = None,
        FileSize: int = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeDBLogFilesResponseTypeDef:
        """
        [Client.describe_db_log_files documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_log_files)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_parameter_groups(
        self,
        DBParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBParameterGroupsMessageTypeDef:
        """
        [Client.describe_db_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_parameter_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_parameters(
        self,
        DBParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBParameterGroupDetailsTypeDef:
        """
        [Client.describe_db_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_proxies(
        self,
        DBProxyName: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> DescribeDBProxiesResponseTypeDef:
        """
        [Client.describe_db_proxies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_proxies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_proxy_target_groups(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> DescribeDBProxyTargetGroupsResponseTypeDef:
        """
        [Client.describe_db_proxy_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_proxy_target_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_proxy_targets(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> DescribeDBProxyTargetsResponseTypeDef:
        """
        [Client.describe_db_proxy_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_proxy_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_security_groups(
        self,
        DBSecurityGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBSecurityGroupMessageTypeDef:
        """
        [Client.describe_db_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_security_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_snapshot_attributes(
        self, DBSnapshotIdentifier: str
    ) -> DescribeDBSnapshotAttributesResultTypeDef:
        """
        [Client.describe_db_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_snapshot_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_snapshots(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
    ) -> DBSnapshotMessageTypeDef:
        """
        [Client.describe_db_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_db_subnet_groups(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBSubnetGroupMessageTypeDef:
        """
        [Client.describe_db_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_db_subnet_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_engine_default_cluster_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEngineDefaultClusterParametersResultTypeDef:
        """
        [Client.describe_engine_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_engine_default_cluster_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_engine_default_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEngineDefaultParametersResultTypeDef:
        """
        [Client.describe_engine_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_engine_default_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_categories(
        self, SourceType: str = None, Filters: List[FilterTypeDef] = None
    ) -> EventCategoriesMessageTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_event_categories)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventSubscriptionsMessageTypeDef:
        """
        [Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_event_subscriptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventsMessageTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_global_clusters(
        self,
        GlobalClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> GlobalClustersMessageTypeDef:
        """
        [Client.describe_global_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_global_clusters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_installation_media(
        self,
        InstallationMediaId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> InstallationMediaMessageTypeDef:
        """
        [Client.describe_installation_media documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_installation_media)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_option_group_options(
        self,
        EngineName: str,
        MajorEngineVersion: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> OptionGroupOptionsMessageTypeDef:
        """
        [Client.describe_option_group_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_option_group_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_option_groups(
        self,
        OptionGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
        EngineName: str = None,
        MajorEngineVersion: str = None,
    ) -> OptionGroupsTypeDef:
        """
        [Client.describe_option_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_option_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_orderable_db_instance_options(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> OrderableDBInstanceOptionsMessageTypeDef:
        """
        [Client.describe_orderable_db_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_orderable_db_instance_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_pending_maintenance_actions(
        self,
        ResourceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> PendingMaintenanceActionsMessageTypeDef:
        """
        [Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_pending_maintenance_actions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_db_instances(
        self,
        ReservedDBInstanceId: str = None,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        LeaseId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ReservedDBInstanceMessageTypeDef:
        """
        [Client.describe_reserved_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_reserved_db_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_db_instances_offerings(
        self,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ReservedDBInstancesOfferingMessageTypeDef:
        """
        [Client.describe_reserved_db_instances_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_reserved_db_instances_offerings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_source_regions(
        self,
        RegionName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> SourceRegionMessageTypeDef:
        """
        [Client.describe_source_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_source_regions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_valid_db_instance_modifications(
        self, DBInstanceIdentifier: str
    ) -> DescribeValidDBInstanceModificationsResultTypeDef:
        """
        [Client.describe_valid_db_instance_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.describe_valid_db_instance_modifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def download_db_log_file_portion(
        self,
        DBInstanceIdentifier: str,
        LogFileName: str,
        Marker: str = None,
        NumberOfLines: int = None,
    ) -> DownloadDBLogFilePortionDetailsTypeDef:
        """
        [Client.download_db_log_file_portion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.download_db_log_file_portion)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def failover_db_cluster(
        self, DBClusterIdentifier: str, TargetDBInstanceIdentifier: str = None
    ) -> FailoverDBClusterResultTypeDef:
        """
        [Client.failover_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.failover_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_db_auth_token(
        self, DBHostname: str, Port: int, DBUsername: str, Region: str = None
    ) -> None:
        """
        [Client.generate_db_auth_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.generate_db_auth_token)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_installation_media(
        self,
        CustomAvailabilityZoneId: str,
        Engine: str,
        EngineVersion: str,
        EngineInstallationMediaPath: str,
        OSInstallationMediaPath: str,
    ) -> InstallationMediaTypeDef:
        """
        [Client.import_installation_media documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.import_installation_media)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceName: str, Filters: List[FilterTypeDef] = None
    ) -> TagListMessageTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_current_db_cluster_capacity(
        self,
        DBClusterIdentifier: str,
        Capacity: int = None,
        SecondsBeforeTimeout: int = None,
        TimeoutAction: str = None,
    ) -> DBClusterCapacityInfoTypeDef:
        """
        [Client.modify_current_db_cluster_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_current_db_cluster_capacity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_cluster(
        self,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: str = None,
        ApplyImmediately: bool = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Port: int = None,
        MasterUserPassword: str = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        DBInstanceParameterGroupName: str = None,
        ScalingConfiguration: ScalingConfigurationTypeDef = None,
        DeletionProtection: bool = None,
        EnableHttpEndpoint: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> ModifyDBClusterResultTypeDef:
        """
        [Client.modify_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_cluster_endpoint(
        self,
        DBClusterEndpointIdentifier: str,
        EndpointType: str = None,
        StaticMembers: List[str] = None,
        ExcludedMembers: List[str] = None,
    ) -> DBClusterEndpointTypeDef:
        """
        [Client.modify_db_cluster_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_db_cluster_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_cluster_parameter_group(
        self, DBClusterParameterGroupName: str, Parameters: List[ParameterTypeDef]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        [Client.modify_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_db_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_cluster_snapshot_attribute(
        self,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None,
    ) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
        """
        [Client.modify_db_cluster_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_db_cluster_snapshot_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_instance(
        self,
        DBInstanceIdentifier: str,
        AllocatedStorage: int = None,
        DBInstanceClass: str = None,
        DBSubnetGroupName: str = None,
        DBSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        ApplyImmediately: bool = None,
        MasterUserPassword: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        NewDBInstanceIdentifier: str = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        CACertificateIdentifier: str = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        DBPortNumber: int = None,
        PubliclyAccessible: bool = None,
        MonitoringRoleArn: str = None,
        DomainIAMRoleName: str = None,
        PromotionTier: int = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
        ProcessorFeatures: List[ProcessorFeatureTypeDef] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
        MaxAllocatedStorage: int = None,
    ) -> ModifyDBInstanceResultTypeDef:
        """
        [Client.modify_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_db_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_parameter_group(
        self, DBParameterGroupName: str, Parameters: List[ParameterTypeDef]
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        [Client.modify_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_db_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_proxy(
        self,
        DBProxyName: str,
        NewDBProxyName: str = None,
        Auth: List[UserAuthConfigTypeDef] = None,
        RequireTLS: bool = None,
        IdleClientTimeout: int = None,
        DebugLogging: bool = None,
        RoleArn: str = None,
        SecurityGroups: List[str] = None,
    ) -> ModifyDBProxyResponseTypeDef:
        """
        [Client.modify_db_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_db_proxy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_proxy_target_group(
        self,
        TargetGroupName: str,
        DBProxyName: str,
        ConnectionPoolConfig: ConnectionPoolConfigurationTypeDef = None,
        NewName: str = None,
    ) -> ModifyDBProxyTargetGroupResponseTypeDef:
        """
        [Client.modify_db_proxy_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_db_proxy_target_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_snapshot(
        self, DBSnapshotIdentifier: str, EngineVersion: str = None, OptionGroupName: str = None
    ) -> ModifyDBSnapshotResultTypeDef:
        """
        [Client.modify_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_db_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_snapshot_attribute(
        self,
        DBSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None,
    ) -> ModifyDBSnapshotAttributeResultTypeDef:
        """
        [Client.modify_db_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_db_snapshot_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_db_subnet_group(
        self, DBSubnetGroupName: str, SubnetIds: List[str], DBSubnetGroupDescription: str = None
    ) -> ModifyDBSubnetGroupResultTypeDef:
        """
        [Client.modify_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_db_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[str] = None,
        Enabled: bool = None,
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        [Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_event_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_global_cluster(
        self,
        GlobalClusterIdentifier: str = None,
        NewGlobalClusterIdentifier: str = None,
        DeletionProtection: bool = None,
    ) -> ModifyGlobalClusterResultTypeDef:
        """
        [Client.modify_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_global_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_option_group(
        self,
        OptionGroupName: str,
        OptionsToInclude: List[OptionConfigurationTypeDef] = None,
        OptionsToRemove: List[str] = None,
        ApplyImmediately: bool = None,
    ) -> ModifyOptionGroupResultTypeDef:
        """
        [Client.modify_option_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.modify_option_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def promote_read_replica(
        self,
        DBInstanceIdentifier: str,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
    ) -> PromoteReadReplicaResultTypeDef:
        """
        [Client.promote_read_replica documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.promote_read_replica)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def promote_read_replica_db_cluster(
        self, DBClusterIdentifier: str
    ) -> PromoteReadReplicaDBClusterResultTypeDef:
        """
        [Client.promote_read_replica_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.promote_read_replica_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purchase_reserved_db_instances_offering(
        self,
        ReservedDBInstancesOfferingId: str,
        ReservedDBInstanceId: str = None,
        DBInstanceCount: int = None,
        Tags: List[TagTypeDef] = None,
    ) -> PurchaseReservedDBInstancesOfferingResultTypeDef:
        """
        [Client.purchase_reserved_db_instances_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.purchase_reserved_db_instances_offering)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot_db_instance(
        self, DBInstanceIdentifier: str, ForceFailover: bool = None
    ) -> RebootDBInstanceResultTypeDef:
        """
        [Client.reboot_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.reboot_db_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_db_proxy_targets(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        DBInstanceIdentifiers: List[str] = None,
        DBClusterIdentifiers: List[str] = None,
    ) -> RegisterDBProxyTargetsResponseTypeDef:
        """
        [Client.register_db_proxy_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.register_db_proxy_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_from_global_cluster(
        self, GlobalClusterIdentifier: str = None, DbClusterIdentifier: str = None
    ) -> RemoveFromGlobalClusterResultTypeDef:
        """
        [Client.remove_from_global_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.remove_from_global_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_role_from_db_cluster(
        self, DBClusterIdentifier: str, RoleArn: str, FeatureName: str = None
    ) -> None:
        """
        [Client.remove_role_from_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.remove_role_from_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_role_from_db_instance(
        self, DBInstanceIdentifier: str, RoleArn: str, FeatureName: str
    ) -> None:
        """
        [Client.remove_role_from_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.remove_role_from_db_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_source_identifier_from_subscription(
        self, SubscriptionName: str, SourceIdentifier: str
    ) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
        """
        [Client.remove_source_identifier_from_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.remove_source_identifier_from_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.remove_tags_from_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[ParameterTypeDef] = None,
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        [Client.reset_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.reset_db_cluster_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_db_parameter_group(
        self,
        DBParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[ParameterTypeDef] = None,
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        [Client.reset_db_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.reset_db_parameter_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_db_cluster_from_s3(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        MasterUsername: str,
        MasterUserPassword: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
        AvailabilityZones: List[str] = None,
        BackupRetentionPeriod: int = None,
        CharacterSetName: str = None,
        DatabaseName: str = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        OptionGroupName: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        Tags: List[TagTypeDef] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        S3Prefix: str = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> RestoreDBClusterFromS3ResultTypeDef:
        """
        [Client.restore_db_cluster_from_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.restore_db_cluster_from_s3)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_db_cluster_from_snapshot(
        self,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        EngineVersion: str = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        DatabaseName: str = None,
        OptionGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List[TagTypeDef] = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        EngineMode: str = None,
        ScalingConfiguration: ScalingConfigurationTypeDef = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> RestoreDBClusterFromSnapshotResultTypeDef:
        """
        [Client.restore_db_cluster_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.restore_db_cluster_from_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_db_cluster_to_point_in_time(
        self,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreType: str = None,
        RestoreToTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        OptionGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List[TagTypeDef] = None,
        KmsKeyId: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        BacktrackWindow: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DBClusterParameterGroupName: str = None,
        DeletionProtection: bool = None,
        CopyTagsToSnapshot: bool = None,
    ) -> RestoreDBClusterToPointInTimeResultTypeDef:
        """
        [Client.restore_db_cluster_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.restore_db_cluster_to_point_in_time)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_db_instance_from_db_snapshot(
        self,
        DBInstanceIdentifier: str,
        DBSnapshotIdentifier: str,
        DBInstanceClass: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        MultiAZ: bool = None,
        PubliclyAccessible: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        DBName: str = None,
        Engine: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        Tags: List[TagTypeDef] = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Domain: str = None,
        CopyTagsToSnapshot: bool = None,
        DomainIAMRoleName: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List[ProcessorFeatureTypeDef] = None,
        UseDefaultProcessorFeatures: bool = None,
        DBParameterGroupName: str = None,
        DeletionProtection: bool = None,
    ) -> RestoreDBInstanceFromDBSnapshotResultTypeDef:
        """
        [Client.restore_db_instance_from_db_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.restore_db_instance_from_db_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_db_instance_from_s3(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        SourceEngine: str,
        SourceEngineVersion: str,
        S3BucketName: str,
        S3IngestionRoleArn: str,
        DBName: str = None,
        AllocatedStorage: int = None,
        MasterUsername: str = None,
        MasterUserPassword: str = None,
        DBSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        PreferredMaintenanceWindow: str = None,
        DBParameterGroupName: str = None,
        BackupRetentionPeriod: int = None,
        PreferredBackupWindow: str = None,
        Port: int = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        PubliclyAccessible: bool = None,
        Tags: List[TagTypeDef] = None,
        StorageType: str = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        CopyTagsToSnapshot: bool = None,
        MonitoringInterval: int = None,
        MonitoringRoleArn: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        S3Prefix: str = None,
        EnablePerformanceInsights: bool = None,
        PerformanceInsightsKMSKeyId: str = None,
        PerformanceInsightsRetentionPeriod: int = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List[ProcessorFeatureTypeDef] = None,
        UseDefaultProcessorFeatures: bool = None,
        DeletionProtection: bool = None,
    ) -> RestoreDBInstanceFromS3ResultTypeDef:
        """
        [Client.restore_db_instance_from_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.restore_db_instance_from_s3)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_db_instance_to_point_in_time(
        self,
        TargetDBInstanceIdentifier: str,
        SourceDBInstanceIdentifier: str = None,
        RestoreTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        DBInstanceClass: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        DBSubnetGroupName: str = None,
        MultiAZ: bool = None,
        PubliclyAccessible: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        LicenseModel: str = None,
        DBName: str = None,
        Engine: str = None,
        Iops: int = None,
        OptionGroupName: str = None,
        CopyTagsToSnapshot: bool = None,
        Tags: List[TagTypeDef] = None,
        StorageType: str = None,
        TdeCredentialArn: str = None,
        TdeCredentialPassword: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Domain: str = None,
        DomainIAMRoleName: str = None,
        EnableIAMDatabaseAuthentication: bool = None,
        EnableCloudwatchLogsExports: List[str] = None,
        ProcessorFeatures: List[ProcessorFeatureTypeDef] = None,
        UseDefaultProcessorFeatures: bool = None,
        DBParameterGroupName: str = None,
        DeletionProtection: bool = None,
        SourceDbiResourceId: str = None,
    ) -> RestoreDBInstanceToPointInTimeResultTypeDef:
        """
        [Client.restore_db_instance_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.restore_db_instance_to_point_in_time)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_db_security_group_ingress(
        self,
        DBSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupId: str = None,
        EC2SecurityGroupOwnerId: str = None,
    ) -> RevokeDBSecurityGroupIngressResultTypeDef:
        """
        [Client.revoke_db_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.revoke_db_security_group_ingress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_activity_stream(
        self,
        ResourceArn: str,
        Mode: Literal["sync", "async"],
        KmsKeyId: str,
        ApplyImmediately: bool = None,
    ) -> StartActivityStreamResponseTypeDef:
        """
        [Client.start_activity_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.start_activity_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_db_cluster(self, DBClusterIdentifier: str) -> StartDBClusterResultTypeDef:
        """
        [Client.start_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.start_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_db_instance(self, DBInstanceIdentifier: str) -> StartDBInstanceResultTypeDef:
        """
        [Client.start_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.start_db_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_activity_stream(
        self, ResourceArn: str, ApplyImmediately: bool = None
    ) -> StopActivityStreamResponseTypeDef:
        """
        [Client.stop_activity_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.stop_activity_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_db_cluster(self, DBClusterIdentifier: str) -> StopDBClusterResultTypeDef:
        """
        [Client.stop_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.stop_db_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_db_instance(
        self, DBInstanceIdentifier: str, DBSnapshotIdentifier: str = None
    ) -> StopDBInstanceResultTypeDef:
        """
        [Client.stop_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Client.stop_db_instance)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> paginator_scope.DescribeCertificatesPaginator:
        """
        [Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeCertificates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_custom_availability_zones"]
    ) -> paginator_scope.DescribeCustomAvailabilityZonesPaginator:
        """
        [Paginator.DescribeCustomAvailabilityZones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeCustomAvailabilityZones)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_backtracks"]
    ) -> paginator_scope.DescribeDBClusterBacktracksPaginator:
        """
        [Paginator.DescribeDBClusterBacktracks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterBacktracks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_endpoints"]
    ) -> paginator_scope.DescribeDBClusterEndpointsPaginator:
        """
        [Paginator.DescribeDBClusterEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterEndpoints)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameter_groups"]
    ) -> paginator_scope.DescribeDBClusterParameterGroupsPaginator:
        """
        [Paginator.DescribeDBClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameterGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameters"]
    ) -> paginator_scope.DescribeDBClusterParametersPaginator:
        """
        [Paginator.DescribeDBClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_snapshots"]
    ) -> paginator_scope.DescribeDBClusterSnapshotsPaginator:
        """
        [Paginator.DescribeDBClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterSnapshots)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_clusters"]
    ) -> paginator_scope.DescribeDBClustersPaginator:
        """
        [Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> paginator_scope.DescribeDBEngineVersionsPaginator:
        """
        [Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBEngineVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_instance_automated_backups"]
    ) -> paginator_scope.DescribeDBInstanceAutomatedBackupsPaginator:
        """
        [Paginator.DescribeDBInstanceAutomatedBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBInstanceAutomatedBackups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_instances"]
    ) -> paginator_scope.DescribeDBInstancesPaginator:
        """
        [Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_log_files"]
    ) -> paginator_scope.DescribeDBLogFilesPaginator:
        """
        [Paginator.DescribeDBLogFiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBLogFiles)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_parameter_groups"]
    ) -> paginator_scope.DescribeDBParameterGroupsPaginator:
        """
        [Paginator.DescribeDBParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBParameterGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_parameters"]
    ) -> paginator_scope.DescribeDBParametersPaginator:
        """
        [Paginator.DescribeDBParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBParameters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_proxies"]
    ) -> paginator_scope.DescribeDBProxiesPaginator:
        """
        [Paginator.DescribeDBProxies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBProxies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_target_groups"]
    ) -> paginator_scope.DescribeDBProxyTargetGroupsPaginator:
        """
        [Paginator.DescribeDBProxyTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargetGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_targets"]
    ) -> paginator_scope.DescribeDBProxyTargetsPaginator:
        """
        [Paginator.DescribeDBProxyTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_security_groups"]
    ) -> paginator_scope.DescribeDBSecurityGroupsPaginator:
        """
        [Paginator.DescribeDBSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBSecurityGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_snapshots"]
    ) -> paginator_scope.DescribeDBSnapshotsPaginator:
        """
        [Paginator.DescribeDBSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBSnapshots)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> paginator_scope.DescribeDBSubnetGroupsPaginator:
        """
        [Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBSubnetGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_cluster_parameters"]
    ) -> paginator_scope.DescribeEngineDefaultClusterParametersPaginator:
        """
        [Paginator.DescribeEngineDefaultClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultClusterParameters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> paginator_scope.DescribeEngineDefaultParametersPaginator:
        """
        [Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultParameters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> paginator_scope.DescribeEventSubscriptionsPaginator:
        """
        [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEventSubscriptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> paginator_scope.DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEvents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_global_clusters"]
    ) -> paginator_scope.DescribeGlobalClustersPaginator:
        """
        [Paginator.DescribeGlobalClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeGlobalClusters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_installation_media"]
    ) -> paginator_scope.DescribeInstallationMediaPaginator:
        """
        [Paginator.DescribeInstallationMedia documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeInstallationMedia)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_option_group_options"]
    ) -> paginator_scope.DescribeOptionGroupOptionsPaginator:
        """
        [Paginator.DescribeOptionGroupOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeOptionGroupOptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_option_groups"]
    ) -> paginator_scope.DescribeOptionGroupsPaginator:
        """
        [Paginator.DescribeOptionGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeOptionGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> paginator_scope.DescribeOrderableDBInstanceOptionsPaginator:
        """
        [Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeOrderableDBInstanceOptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_pending_maintenance_actions"]
    ) -> paginator_scope.DescribePendingMaintenanceActionsPaginator:
        """
        [Paginator.DescribePendingMaintenanceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribePendingMaintenanceActions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_reserved_db_instances"]
    ) -> paginator_scope.DescribeReservedDBInstancesPaginator:
        """
        [Paginator.DescribeReservedDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_reserved_db_instances_offerings"]
    ) -> paginator_scope.DescribeReservedDBInstancesOfferingsPaginator:
        """
        [Paginator.DescribeReservedDBInstancesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstancesOfferings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_source_regions"]
    ) -> paginator_scope.DescribeSourceRegionsPaginator:
        """
        [Paginator.DescribeSourceRegions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeSourceRegions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["download_db_log_file_portion"]
    ) -> paginator_scope.DownloadDBLogFilePortionPaginator:
        """
        [Paginator.DownloadDBLogFilePortion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DownloadDBLogFilePortion)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["db_cluster_snapshot_available"]
    ) -> waiter_scope.DBClusterSnapshotAvailableWaiter:
        """
        [Waiter.DBClusterSnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["db_cluster_snapshot_deleted"]
    ) -> waiter_scope.DBClusterSnapshotDeletedWaiter:
        """
        [Waiter.DBClusterSnapshotDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotDeleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["db_instance_available"]
    ) -> waiter_scope.DBInstanceAvailableWaiter:
        """
        [Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Waiter.DBInstanceAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["db_instance_deleted"]
    ) -> waiter_scope.DBInstanceDeletedWaiter:
        """
        [Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Waiter.DBInstanceDeleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_available"]
    ) -> waiter_scope.DBSnapshotAvailableWaiter:
        """
        [Waiter.DBSnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Waiter.DBSnapshotAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_completed"]
    ) -> waiter_scope.DBSnapshotCompletedWaiter:
        """
        [Waiter.DBSnapshotCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Waiter.DBSnapshotCompleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_deleted"]
    ) -> waiter_scope.DBSnapshotDeletedWaiter:
        """
        [Waiter.DBSnapshotDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Waiter.DBSnapshotDeleted)
        """


class Exceptions:
    AuthorizationAlreadyExistsFault: Boto3ClientError
    AuthorizationNotFoundFault: Boto3ClientError
    AuthorizationQuotaExceededFault: Boto3ClientError
    BackupPolicyNotFoundFault: Boto3ClientError
    CertificateNotFoundFault: Boto3ClientError
    ClientError: Boto3ClientError
    CustomAvailabilityZoneAlreadyExistsFault: Boto3ClientError
    CustomAvailabilityZoneNotFoundFault: Boto3ClientError
    CustomAvailabilityZoneQuotaExceededFault: Boto3ClientError
    DBClusterAlreadyExistsFault: Boto3ClientError
    DBClusterBacktrackNotFoundFault: Boto3ClientError
    DBClusterEndpointAlreadyExistsFault: Boto3ClientError
    DBClusterEndpointNotFoundFault: Boto3ClientError
    DBClusterEndpointQuotaExceededFault: Boto3ClientError
    DBClusterNotFoundFault: Boto3ClientError
    DBClusterParameterGroupNotFoundFault: Boto3ClientError
    DBClusterQuotaExceededFault: Boto3ClientError
    DBClusterRoleAlreadyExistsFault: Boto3ClientError
    DBClusterRoleNotFoundFault: Boto3ClientError
    DBClusterRoleQuotaExceededFault: Boto3ClientError
    DBClusterSnapshotAlreadyExistsFault: Boto3ClientError
    DBClusterSnapshotNotFoundFault: Boto3ClientError
    DBInstanceAlreadyExistsFault: Boto3ClientError
    DBInstanceAutomatedBackupNotFoundFault: Boto3ClientError
    DBInstanceAutomatedBackupQuotaExceededFault: Boto3ClientError
    DBInstanceNotFoundFault: Boto3ClientError
    DBInstanceRoleAlreadyExistsFault: Boto3ClientError
    DBInstanceRoleNotFoundFault: Boto3ClientError
    DBInstanceRoleQuotaExceededFault: Boto3ClientError
    DBLogFileNotFoundFault: Boto3ClientError
    DBParameterGroupAlreadyExistsFault: Boto3ClientError
    DBParameterGroupNotFoundFault: Boto3ClientError
    DBParameterGroupQuotaExceededFault: Boto3ClientError
    DBProxyAlreadyExistsFault: Boto3ClientError
    DBProxyNotFoundFault: Boto3ClientError
    DBProxyQuotaExceededFault: Boto3ClientError
    DBProxyTargetAlreadyRegisteredFault: Boto3ClientError
    DBProxyTargetGroupNotFoundFault: Boto3ClientError
    DBProxyTargetNotFoundFault: Boto3ClientError
    DBSecurityGroupAlreadyExistsFault: Boto3ClientError
    DBSecurityGroupNotFoundFault: Boto3ClientError
    DBSecurityGroupNotSupportedFault: Boto3ClientError
    DBSecurityGroupQuotaExceededFault: Boto3ClientError
    DBSnapshotAlreadyExistsFault: Boto3ClientError
    DBSnapshotNotFoundFault: Boto3ClientError
    DBSubnetGroupAlreadyExistsFault: Boto3ClientError
    DBSubnetGroupDoesNotCoverEnoughAZs: Boto3ClientError
    DBSubnetGroupNotAllowedFault: Boto3ClientError
    DBSubnetGroupNotFoundFault: Boto3ClientError
    DBSubnetGroupQuotaExceededFault: Boto3ClientError
    DBSubnetQuotaExceededFault: Boto3ClientError
    DBUpgradeDependencyFailureFault: Boto3ClientError
    DomainNotFoundFault: Boto3ClientError
    EventSubscriptionQuotaExceededFault: Boto3ClientError
    GlobalClusterAlreadyExistsFault: Boto3ClientError
    GlobalClusterNotFoundFault: Boto3ClientError
    GlobalClusterQuotaExceededFault: Boto3ClientError
    InstallationMediaAlreadyExistsFault: Boto3ClientError
    InstallationMediaNotFoundFault: Boto3ClientError
    InstanceQuotaExceededFault: Boto3ClientError
    InsufficientDBClusterCapacityFault: Boto3ClientError
    InsufficientDBInstanceCapacityFault: Boto3ClientError
    InsufficientStorageClusterCapacityFault: Boto3ClientError
    InvalidDBClusterCapacityFault: Boto3ClientError
    InvalidDBClusterEndpointStateFault: Boto3ClientError
    InvalidDBClusterSnapshotStateFault: Boto3ClientError
    InvalidDBClusterStateFault: Boto3ClientError
    InvalidDBInstanceAutomatedBackupStateFault: Boto3ClientError
    InvalidDBInstanceStateFault: Boto3ClientError
    InvalidDBParameterGroupStateFault: Boto3ClientError
    InvalidDBProxyStateFault: Boto3ClientError
    InvalidDBSecurityGroupStateFault: Boto3ClientError
    InvalidDBSnapshotStateFault: Boto3ClientError
    InvalidDBSubnetGroupFault: Boto3ClientError
    InvalidDBSubnetGroupStateFault: Boto3ClientError
    InvalidDBSubnetStateFault: Boto3ClientError
    InvalidEventSubscriptionStateFault: Boto3ClientError
    InvalidGlobalClusterStateFault: Boto3ClientError
    InvalidOptionGroupStateFault: Boto3ClientError
    InvalidRestoreFault: Boto3ClientError
    InvalidS3BucketFault: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    InvalidVPCNetworkStateFault: Boto3ClientError
    KMSKeyNotAccessibleFault: Boto3ClientError
    OptionGroupAlreadyExistsFault: Boto3ClientError
    OptionGroupNotFoundFault: Boto3ClientError
    OptionGroupQuotaExceededFault: Boto3ClientError
    PointInTimeRestoreNotEnabledFault: Boto3ClientError
    ProvisionedIopsNotAvailableInAZFault: Boto3ClientError
    ReservedDBInstanceAlreadyExistsFault: Boto3ClientError
    ReservedDBInstanceNotFoundFault: Boto3ClientError
    ReservedDBInstanceQuotaExceededFault: Boto3ClientError
    ReservedDBInstancesOfferingNotFoundFault: Boto3ClientError
    ResourceNotFoundFault: Boto3ClientError
    SNSInvalidTopicFault: Boto3ClientError
    SNSNoAuthorizationFault: Boto3ClientError
    SNSTopicArnNotFoundFault: Boto3ClientError
    SharedSnapshotQuotaExceededFault: Boto3ClientError
    SnapshotQuotaExceededFault: Boto3ClientError
    SourceNotFoundFault: Boto3ClientError
    StorageQuotaExceededFault: Boto3ClientError
    StorageTypeNotSupportedFault: Boto3ClientError
    SubnetAlreadyInUse: Boto3ClientError
    SubscriptionAlreadyExistFault: Boto3ClientError
    SubscriptionCategoryNotFoundFault: Boto3ClientError
    SubscriptionNotFoundFault: Boto3ClientError
