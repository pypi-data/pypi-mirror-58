"Main interface for eks service"
from mypy_boto3_eks.client import EKSClient as Client, EKSClient
from mypy_boto3_eks.paginator import (
    ListClustersPaginator,
    ListFargateProfilesPaginator,
    ListNodegroupsPaginator,
    ListUpdatesPaginator,
)
from mypy_boto3_eks.waiter import (
    ClusterActiveWaiter,
    ClusterDeletedWaiter,
    NodegroupActiveWaiter,
    NodegroupDeletedWaiter,
)


__all__ = (
    "Client",
    "ClusterActiveWaiter",
    "ClusterDeletedWaiter",
    "EKSClient",
    "ListClustersPaginator",
    "ListFargateProfilesPaginator",
    "ListNodegroupsPaginator",
    "ListUpdatesPaginator",
    "NodegroupActiveWaiter",
    "NodegroupDeletedWaiter",
)
