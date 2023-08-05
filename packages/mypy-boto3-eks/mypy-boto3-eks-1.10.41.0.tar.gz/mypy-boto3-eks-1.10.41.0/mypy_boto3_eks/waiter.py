"Main interface for eks service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_eks.type_defs import WaiterConfigTypeDef


__all__ = (
    "ClusterActiveWaiter",
    "ClusterDeletedWaiter",
    "NodegroupActiveWaiter",
    "NodegroupDeletedWaiter",
)


class ClusterActiveWaiter(Boto3Waiter):
    """
    [Waiter.ClusterActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Waiter.ClusterActive)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ClusterActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Waiter.ClusterActive.wait)
        """


class ClusterDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Waiter.ClusterDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, name: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ClusterDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Waiter.ClusterDeleted.wait)
        """


class NodegroupActiveWaiter(Boto3Waiter):
    """
    [Waiter.NodegroupActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Waiter.NodegroupActive)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, clusterName: str, nodegroupName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [NodegroupActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Waiter.NodegroupActive.wait)
        """


class NodegroupDeletedWaiter(Boto3Waiter):
    """
    [Waiter.NodegroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Waiter.NodegroupDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, clusterName: str, nodegroupName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [NodegroupDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Waiter.NodegroupDeleted.wait)
        """
