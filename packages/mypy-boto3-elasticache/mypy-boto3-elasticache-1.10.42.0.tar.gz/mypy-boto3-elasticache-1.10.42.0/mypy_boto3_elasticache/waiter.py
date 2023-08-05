"Main interface for elasticache service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_elasticache.type_defs import WaiterConfigTypeDef


__all__ = (
    "CacheClusterAvailableWaiter",
    "CacheClusterDeletedWaiter",
    "ReplicationGroupAvailableWaiter",
    "ReplicationGroupDeletedWaiter",
)


class CacheClusterAvailableWaiter(Boto3Waiter):
    """
    [Waiter.CacheClusterAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [CacheClusterAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterAvailable.wait)
        """


class CacheClusterDeletedWaiter(Boto3Waiter):
    """
    [Waiter.CacheClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [CacheClusterDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterDeleted.wait)
        """


class ReplicationGroupAvailableWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationGroupAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationGroupAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupAvailable.wait)
        """


class ReplicationGroupDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationGroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationGroupDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupDeleted.wait)
        """
