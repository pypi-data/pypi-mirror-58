"Main interface for elasticache service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elasticache.type_defs import (
    CacheClusterMessageTypeDef,
    CacheEngineVersionMessageTypeDef,
    CacheParameterGroupDetailsTypeDef,
    CacheParameterGroupsMessageTypeDef,
    CacheSecurityGroupMessageTypeDef,
    CacheSubnetGroupMessageTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeSnapshotsListMessageTypeDef,
    EventsMessageTypeDef,
    PaginatorConfigTypeDef,
    ReplicationGroupMessageTypeDef,
    ReservedCacheNodeMessageTypeDef,
    ReservedCacheNodesOfferingMessageTypeDef,
    ServiceUpdatesMessageTypeDef,
    TimeRangeFilterTypeDef,
    UpdateActionsMessageTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeCacheClustersPaginator",
    "DescribeCacheEngineVersionsPaginator",
    "DescribeCacheParameterGroupsPaginator",
    "DescribeCacheParametersPaginator",
    "DescribeCacheSecurityGroupsPaginator",
    "DescribeCacheSubnetGroupsPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventsPaginator",
    "DescribeReplicationGroupsPaginator",
    "DescribeReservedCacheNodesPaginator",
    "DescribeReservedCacheNodesOfferingsPaginator",
    "DescribeServiceUpdatesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeUpdateActionsPaginator",
)


class DescribeCacheClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheClusters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CacheClusterId: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[CacheClusterMessageTypeDef, None, None]:
        """
        [DescribeCacheClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheClusters.paginate)
        """


class DescribeCacheEngineVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheEngineVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupFamily: str = None,
        DefaultOnly: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[CacheEngineVersionMessageTypeDef, None, None]:
        """
        [DescribeCacheEngineVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheEngineVersions.paginate)
        """


class DescribeCacheParameterGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameterGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CacheParameterGroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[CacheParameterGroupsMessageTypeDef, None, None]:
        """
        [DescribeCacheParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameterGroups.paginate)
        """


class DescribeCacheParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CacheParameterGroupName: str,
        Source: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[CacheParameterGroupDetailsTypeDef, None, None]:
        """
        [DescribeCacheParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameters.paginate)
        """


class DescribeCacheSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSecurityGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CacheSecurityGroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[CacheSecurityGroupMessageTypeDef, None, None]:
        """
        [DescribeCacheSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSecurityGroups.paginate)
        """


class DescribeCacheSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCacheSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSubnetGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CacheSubnetGroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[CacheSubnetGroupMessageTypeDef, None, None]:
        """
        [DescribeCacheSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSubnetGroups.paginate)
        """


class DescribeEngineDefaultParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEngineDefaultParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CacheParameterGroupFamily: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeEngineDefaultParametersResultTypeDef, None, None]:
        """
        [DescribeEngineDefaultParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEngineDefaultParameters.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "cache-cluster",
            "cache-parameter-group",
            "cache-security-group",
            "cache-subnet-group",
            "replication-group",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[EventsMessageTypeDef, None, None]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEvents.paginate)
        """


class DescribeReplicationGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReplicationGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ReplicationGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ReplicationGroupMessageTypeDef, None, None]:
        """
        [DescribeReplicationGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReplicationGroups.paginate)
        """


class DescribeReservedCacheNodesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedCacheNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedCacheNodeId: str = None,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ReservedCacheNodeMessageTypeDef, None, None]:
        """
        [DescribeReservedCacheNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodes.paginate)
        """


class DescribeReservedCacheNodesOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedCacheNodesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ReservedCacheNodesOfferingMessageTypeDef, None, None]:
        """
        [DescribeReservedCacheNodesOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings.paginate)
        """


class DescribeServiceUpdatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeServiceUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeServiceUpdates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceUpdateName: str = None,
        ServiceUpdateStatus: List[Literal["available", "cancelled", "expired"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ServiceUpdatesMessageTypeDef, None, None]:
        """
        [DescribeServiceUpdates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeServiceUpdates.paginate)
        """


class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeSnapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        SnapshotName: str = None,
        SnapshotSource: str = None,
        ShowNodeGroupConfig: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSnapshotsListMessageTypeDef, None, None]:
        """
        [DescribeSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeSnapshots.paginate)
        """


class DescribeUpdateActionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeUpdateActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUpdateActions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceUpdateName: str = None,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
        Engine: str = None,
        ServiceUpdateStatus: List[Literal["available", "cancelled", "expired"]] = None,
        ServiceUpdateTimeRange: TimeRangeFilterTypeDef = None,
        UpdateActionStatus: List[
            Literal[
                "not-applied", "waiting-to-start", "in-progress", "stopping", "stopped", "complete"
            ]
        ] = None,
        ShowNodeLevelUpdateStatus: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[UpdateActionsMessageTypeDef, None, None]:
        """
        [DescribeUpdateActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUpdateActions.paginate)
        """
