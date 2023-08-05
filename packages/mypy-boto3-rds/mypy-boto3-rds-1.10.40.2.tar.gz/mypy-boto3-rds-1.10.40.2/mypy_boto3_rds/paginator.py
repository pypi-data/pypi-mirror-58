"Main interface for rds service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_rds.type_defs import (
    CertificateMessageTypeDef,
    CustomAvailabilityZoneMessageTypeDef,
    DBClusterBacktrackMessageTypeDef,
    DBClusterEndpointMessageTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceAutomatedBackupMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBParameterGroupDetailsTypeDef,
    DBParameterGroupsMessageTypeDef,
    DBSecurityGroupMessageTypeDef,
    DBSnapshotMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DescribeDBLogFilesResponseTypeDef,
    DescribeDBProxiesResponseTypeDef,
    DescribeDBProxyTargetGroupsResponseTypeDef,
    DescribeDBProxyTargetsResponseTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DownloadDBLogFilePortionDetailsTypeDef,
    EventSubscriptionsMessageTypeDef,
    EventsMessageTypeDef,
    FilterTypeDef,
    GlobalClustersMessageTypeDef,
    InstallationMediaMessageTypeDef,
    OptionGroupOptionsMessageTypeDef,
    OptionGroupsTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    PaginatorConfigTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    ReservedDBInstanceMessageTypeDef,
    ReservedDBInstancesOfferingMessageTypeDef,
    SourceRegionMessageTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeCertificatesPaginator",
    "DescribeCustomAvailabilityZonesPaginator",
    "DescribeDBClusterBacktracksPaginator",
    "DescribeDBClusterEndpointsPaginator",
    "DescribeDBClusterParameterGroupsPaginator",
    "DescribeDBClusterParametersPaginator",
    "DescribeDBClusterSnapshotsPaginator",
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstanceAutomatedBackupsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBLogFilesPaginator",
    "DescribeDBParameterGroupsPaginator",
    "DescribeDBParametersPaginator",
    "DescribeDBProxiesPaginator",
    "DescribeDBProxyTargetGroupsPaginator",
    "DescribeDBProxyTargetsPaginator",
    "DescribeDBSecurityGroupsPaginator",
    "DescribeDBSnapshotsPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEngineDefaultClusterParametersPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeGlobalClustersPaginator",
    "DescribeInstallationMediaPaginator",
    "DescribeOptionGroupOptionsPaginator",
    "DescribeOptionGroupsPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
    "DescribePendingMaintenanceActionsPaginator",
    "DescribeReservedDBInstancesPaginator",
    "DescribeReservedDBInstancesOfferingsPaginator",
    "DescribeSourceRegionsPaginator",
    "DownloadDBLogFilePortionPaginator",
)


class DescribeCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeCertificates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CertificateIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[CertificateMessageTypeDef, None, None]:
        """
        [DescribeCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeCertificates.paginate)
        """


class DescribeCustomAvailabilityZonesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCustomAvailabilityZones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeCustomAvailabilityZones)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CustomAvailabilityZoneId: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[CustomAvailabilityZoneMessageTypeDef, None, None]:
        """
        [DescribeCustomAvailabilityZones.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeCustomAvailabilityZones.paginate)
        """


class DescribeDBClusterBacktracksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterBacktracks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterBacktracks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterIdentifier: str,
        BacktrackIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBClusterBacktrackMessageTypeDef, None, None]:
        """
        [DescribeDBClusterBacktracks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterBacktracks.paginate)
        """


class DescribeDBClusterEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterEndpoints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        DBClusterEndpointIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBClusterEndpointMessageTypeDef, None, None]:
        """
        [DescribeDBClusterEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterEndpoints.paginate)
        """


class DescribeDBClusterParameterGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameterGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBClusterParameterGroupsMessageTypeDef, None, None]:
        """
        [DescribeDBClusterParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameterGroups.paginate)
        """


class DescribeDBClusterParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBClusterParameterGroupDetailsTypeDef, None, None]:
        """
        [DescribeDBClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameters.paginate)
        """


class DescribeDBClusterSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterSnapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBClusterSnapshotMessageTypeDef, None, None]:
        """
        [DescribeDBClusterSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusterSnapshots.paginate)
        """


class DescribeDBClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        IncludeShared: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBClusterMessageTypeDef, None, None]:
        """
        [DescribeDBClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBClusters.paginate)
        """


class DescribeDBEngineVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBEngineVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[FilterTypeDef] = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
        IncludeAll: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBEngineVersionMessageTypeDef, None, None]:
        """
        [DescribeDBEngineVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBEngineVersions.paginate)
        """


class DescribeDBInstanceAutomatedBackupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBInstanceAutomatedBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBInstanceAutomatedBackups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DbiResourceId: str = None,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBInstanceAutomatedBackupMessageTypeDef, None, None]:
        """
        [DescribeDBInstanceAutomatedBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBInstanceAutomatedBackups.paginate)
        """


class DescribeDBInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBInstanceMessageTypeDef, None, None]:
        """
        [DescribeDBInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBInstances.paginate)
        """


class DescribeDBLogFilesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBLogFiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBLogFiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBInstanceIdentifier: str,
        FilenameContains: str = None,
        FileLastWritten: int = None,
        FileSize: int = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeDBLogFilesResponseTypeDef, None, None]:
        """
        [DescribeDBLogFiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBLogFiles.paginate)
        """


class DescribeDBParameterGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBParameterGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBParameterGroupsMessageTypeDef, None, None]:
        """
        [DescribeDBParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBParameterGroups.paginate)
        """


class DescribeDBParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBParameterGroupDetailsTypeDef, None, None]:
        """
        [DescribeDBParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBParameters.paginate)
        """


class DescribeDBProxiesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBProxies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBProxies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBProxyName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeDBProxiesResponseTypeDef, None, None]:
        """
        [DescribeDBProxies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBProxies.paginate)
        """


class DescribeDBProxyTargetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBProxyTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargetGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeDBProxyTargetGroupsResponseTypeDef, None, None]:
        """
        [DescribeDBProxyTargetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargetGroups.paginate)
        """


class DescribeDBProxyTargetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBProxyTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeDBProxyTargetsResponseTypeDef, None, None]:
        """
        [DescribeDBProxyTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargets.paginate)
        """


class DescribeDBSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBSecurityGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBSecurityGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBSecurityGroupMessageTypeDef, None, None]:
        """
        [DescribeDBSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBSecurityGroups.paginate)
        """


class DescribeDBSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBSnapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBSnapshotMessageTypeDef, None, None]:
        """
        [DescribeDBSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBSnapshots.paginate)
        """


class DescribeDBSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBSubnetGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBSubnetGroupMessageTypeDef, None, None]:
        """
        [DescribeDBSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeDBSubnetGroups.paginate)
        """


class DescribeEngineDefaultClusterParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEngineDefaultClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultClusterParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEngineDefaultClusterParametersResultTypeDef, None, None]:
        """
        [DescribeEngineDefaultClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultClusterParameters.paginate)
        """


class DescribeEngineDefaultParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEngineDefaultParametersResultTypeDef, None, None]:
        """
        [DescribeEngineDefaultParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultParameters.paginate)
        """


class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEventSubscriptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[EventSubscriptionsMessageTypeDef, None, None]:
        """
        [DescribeEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEventSubscriptions.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[EventsMessageTypeDef, None, None]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeEvents.paginate)
        """


class DescribeGlobalClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeGlobalClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeGlobalClusters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GlobalClustersMessageTypeDef, None, None]:
        """
        [DescribeGlobalClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeGlobalClusters.paginate)
        """


class DescribeInstallationMediaPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstallationMedia documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeInstallationMedia)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstallationMediaId: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[InstallationMediaMessageTypeDef, None, None]:
        """
        [DescribeInstallationMedia.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeInstallationMedia.paginate)
        """


class DescribeOptionGroupOptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOptionGroupOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeOptionGroupOptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EngineName: str,
        MajorEngineVersion: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[OptionGroupOptionsMessageTypeDef, None, None]:
        """
        [DescribeOptionGroupOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeOptionGroupOptions.paginate)
        """


class DescribeOptionGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOptionGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeOptionGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        OptionGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        EngineName: str = None,
        MajorEngineVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[OptionGroupsTypeDef, None, None]:
        """
        [DescribeOptionGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeOptionGroups.paginate)
        """


class DescribeOrderableDBInstanceOptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeOrderableDBInstanceOptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[OrderableDBInstanceOptionsMessageTypeDef, None, None]:
        """
        [DescribeOrderableDBInstanceOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeOrderableDBInstanceOptions.paginate)
        """


class DescribePendingMaintenanceActionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePendingMaintenanceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribePendingMaintenanceActions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[PendingMaintenanceActionsMessageTypeDef, None, None]:
        """
        [DescribePendingMaintenanceActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribePendingMaintenanceActions.paginate)
        """


class DescribeReservedDBInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ReservedDBInstanceMessageTypeDef, None, None]:
        """
        [DescribeReservedDBInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstances.paginate)
        """


class DescribeReservedDBInstancesOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedDBInstancesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstancesOfferings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ReservedDBInstancesOfferingMessageTypeDef, None, None]:
        """
        [DescribeReservedDBInstancesOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstancesOfferings.paginate)
        """


class DescribeSourceRegionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSourceRegions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeSourceRegions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RegionName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SourceRegionMessageTypeDef, None, None]:
        """
        [DescribeSourceRegions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DescribeSourceRegions.paginate)
        """


class DownloadDBLogFilePortionPaginator(Boto3Paginator):
    """
    [Paginator.DownloadDBLogFilePortion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DownloadDBLogFilePortion)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBInstanceIdentifier: str,
        LogFileName: str,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DownloadDBLogFilePortionDetailsTypeDef, None, None]:
        """
        [DownloadDBLogFilePortion.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rds.html#RDS.Paginator.DownloadDBLogFilePortion.paginate)
        """
