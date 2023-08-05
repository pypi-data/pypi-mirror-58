"Main interface for eks service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_eks.type_defs import (
    ListClustersResponseTypeDef,
    ListFargateProfilesResponseTypeDef,
    ListNodegroupsResponseTypeDef,
    ListUpdatesResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListClustersPaginator",
    "ListFargateProfilesPaginator",
    "ListNodegroupsPaginator",
    "ListUpdatesPaginator",
)


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Paginator.ListClusters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListClustersResponseTypeDef, None, None]:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Paginator.ListClusters.paginate)
        """


class ListFargateProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListFargateProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Paginator.ListFargateProfiles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, clusterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFargateProfilesResponseTypeDef, None, None]:
        """
        [ListFargateProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Paginator.ListFargateProfiles.paginate)
        """


class ListNodegroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListNodegroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Paginator.ListNodegroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, clusterName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListNodegroupsResponseTypeDef, None, None]:
        """
        [ListNodegroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Paginator.ListNodegroups.paginate)
        """


class ListUpdatesPaginator(Boto3Paginator):
    """
    [Paginator.ListUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Paginator.ListUpdates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, name: str, nodegroupName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListUpdatesResponseTypeDef, None, None]:
        """
        [ListUpdates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS.Paginator.ListUpdates.paginate)
        """
