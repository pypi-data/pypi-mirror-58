"Main interface for neptune service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_neptune.type_defs import (
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBParameterGroupDetailsTypeDef,
    DBParameterGroupsMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    EventSubscriptionsMessageTypeDef,
    EventsMessageTypeDef,
    FilterTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    PaginatorConfigTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeDBClusterParameterGroupsPaginator",
    "DescribeDBClusterParametersPaginator",
    "DescribeDBClusterSnapshotsPaginator",
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBParameterGroupsPaginator",
    "DescribeDBParametersPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
    "DescribePendingMaintenanceActionsPaginator",
)


class DescribeDBClusterParameterGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameterGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBClusterParameterGroupsMessageTypeDef, None, None]:
        """
        [DescribeDBClusterParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameterGroups.paginate)
        """


class DescribeDBClusterParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameters)
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
        [DescribeDBClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameters.paginate)
        """


class DescribeDBClusterSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterSnapshots)
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
        [DescribeDBClusterSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterSnapshots.paginate)
        """


class DescribeDBClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBClusterMessageTypeDef, None, None]:
        """
        [DescribeDBClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusters.paginate)
        """


class DescribeDBEngineVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBEngineVersions)
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBEngineVersionMessageTypeDef, None, None]:
        """
        [DescribeDBEngineVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBEngineVersions.paginate)
        """


class DescribeDBInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBInstanceMessageTypeDef, None, None]:
        """
        [DescribeDBInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBInstances.paginate)
        """


class DescribeDBParameterGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameterGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBParameterGroupsMessageTypeDef, None, None]:
        """
        [DescribeDBParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameterGroups.paginate)
        """


class DescribeDBParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameters)
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
        [DescribeDBParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameters.paginate)
        """


class DescribeDBSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBSubnetGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DBSubnetGroupMessageTypeDef, None, None]:
        """
        [DescribeDBSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeDBSubnetGroups.paginate)
        """


class DescribeEngineDefaultParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeEngineDefaultParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEngineDefaultParametersResultTypeDef, None, None]:
        """
        [DescribeEngineDefaultParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeEngineDefaultParameters.paginate)
        """


class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeEventSubscriptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[EventSubscriptionsMessageTypeDef, None, None]:
        """
        [DescribeEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeEventSubscriptions.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeEvents)
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
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeEvents.paginate)
        """


class DescribeOrderableDBInstanceOptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeOrderableDBInstanceOptions)
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
        [DescribeOrderableDBInstanceOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribeOrderableDBInstanceOptions.paginate)
        """


class DescribePendingMaintenanceActionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePendingMaintenanceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribePendingMaintenanceActions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[PendingMaintenanceActionsMessageTypeDef, None, None]:
        """
        [DescribePendingMaintenanceActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/neptune.html#Neptune.Paginator.DescribePendingMaintenanceActions.paginate)
        """
