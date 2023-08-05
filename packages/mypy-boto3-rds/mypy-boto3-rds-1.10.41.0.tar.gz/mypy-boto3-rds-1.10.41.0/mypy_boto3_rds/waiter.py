"Main interface for rds service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_rds.type_defs import FilterTypeDef, WaiterConfigTypeDef


__all__ = (
    "DBClusterSnapshotAvailableWaiter",
    "DBClusterSnapshotDeletedWaiter",
    "DBInstanceAvailableWaiter",
    "DBInstanceDeletedWaiter",
    "DBSnapshotAvailableWaiter",
    "DBSnapshotCompletedWaiter",
    "DBSnapshotDeletedWaiter",
)


class DBClusterSnapshotAvailableWaiter(Boto3Waiter):
    """
    [Waiter.DBClusterSnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DBClusterSnapshotAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotAvailable.wait)
        """


class DBClusterSnapshotDeletedWaiter(Boto3Waiter):
    """
    [Waiter.DBClusterSnapshotDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DBClusterSnapshotDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotDeleted.wait)
        """


class DBInstanceAvailableWaiter(Boto3Waiter):
    """
    [Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBInstanceAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DBInstanceAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBInstanceAvailable.wait)
        """


class DBInstanceDeletedWaiter(Boto3Waiter):
    """
    [Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBInstanceDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DBInstanceDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBInstanceDeleted.wait)
        """


class DBSnapshotAvailableWaiter(Boto3Waiter):
    """
    [Waiter.DBSnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBSnapshotAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
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
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DBSnapshotAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBSnapshotAvailable.wait)
        """


class DBSnapshotCompletedWaiter(Boto3Waiter):
    """
    [Waiter.DBSnapshotCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBSnapshotCompleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
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
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DBSnapshotCompleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBSnapshotCompleted.wait)
        """


class DBSnapshotDeletedWaiter(Boto3Waiter):
    """
    [Waiter.DBSnapshotDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBSnapshotDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
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
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DBSnapshotDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rds.html#RDS.Waiter.DBSnapshotDeleted.wait)
        """
