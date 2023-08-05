"Main interface for eks service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_eks.client as client_scope

# pylint: disable=import-self
import mypy_boto3_eks.paginator as paginator_scope
from mypy_boto3_eks.type_defs import (
    CreateClusterResponseTypeDef,
    CreateFargateProfileResponseTypeDef,
    CreateNodegroupResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteFargateProfileResponseTypeDef,
    DeleteNodegroupResponseTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeFargateProfileResponseTypeDef,
    DescribeNodegroupResponseTypeDef,
    DescribeUpdateResponseTypeDef,
    FargateProfileSelectorTypeDef,
    ListClustersResponseTypeDef,
    ListFargateProfilesResponseTypeDef,
    ListNodegroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUpdatesResponseTypeDef,
    LoggingTypeDef,
    NodegroupScalingConfigTypeDef,
    RemoteAccessConfigTypeDef,
    UpdateClusterConfigResponseTypeDef,
    UpdateClusterVersionResponseTypeDef,
    UpdateLabelsPayloadTypeDef,
    UpdateNodegroupConfigResponseTypeDef,
    UpdateNodegroupVersionResponseTypeDef,
    VpcConfigRequestTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_eks.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EKSClient",)


class EKSClient(BaseClient):
    """
    [EKS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cluster(
        self,
        name: str,
        roleArn: str,
        resourcesVpcConfig: VpcConfigRequestTypeDef,
        version: str = None,
        logging: LoggingTypeDef = None,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateClusterResponseTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.create_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_fargate_profile(
        self,
        fargateProfileName: str,
        clusterName: str,
        podExecutionRoleArn: str,
        subnets: List[str] = None,
        selectors: List[FargateProfileSelectorTypeDef] = None,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateFargateProfileResponseTypeDef:
        """
        [Client.create_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.create_fargate_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_nodegroup(
        self,
        clusterName: str,
        nodegroupName: str,
        subnets: List[str],
        nodeRole: str,
        scalingConfig: NodegroupScalingConfigTypeDef = None,
        diskSize: int = None,
        instanceTypes: List[str] = None,
        amiType: Literal["AL2_x86_64", "AL2_x86_64_GPU"] = None,
        remoteAccess: RemoteAccessConfigTypeDef = None,
        labels: Dict[str, str] = None,
        tags: Dict[str, str] = None,
        clientRequestToken: str = None,
        version: str = None,
        releaseVersion: str = None,
    ) -> CreateNodegroupResponseTypeDef:
        """
        [Client.create_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.create_nodegroup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cluster(self, name: str) -> DeleteClusterResponseTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.delete_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_fargate_profile(
        self, clusterName: str, fargateProfileName: str
    ) -> DeleteFargateProfileResponseTypeDef:
        """
        [Client.delete_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.delete_fargate_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_nodegroup(
        self, clusterName: str, nodegroupName: str
    ) -> DeleteNodegroupResponseTypeDef:
        """
        [Client.delete_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.delete_nodegroup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster(self, name: str) -> DescribeClusterResponseTypeDef:
        """
        [Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.describe_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fargate_profile(
        self, clusterName: str, fargateProfileName: str
    ) -> DescribeFargateProfileResponseTypeDef:
        """
        [Client.describe_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.describe_fargate_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_nodegroup(
        self, clusterName: str, nodegroupName: str
    ) -> DescribeNodegroupResponseTypeDef:
        """
        [Client.describe_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.describe_nodegroup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_update(
        self, name: str, updateId: str, nodegroupName: str = None
    ) -> DescribeUpdateResponseTypeDef:
        """
        [Client.describe_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.describe_update)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_clusters(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListClustersResponseTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.list_clusters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_fargate_profiles(
        self, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListFargateProfilesResponseTypeDef:
        """
        [Client.list_fargate_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.list_fargate_profiles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_nodegroups(
        self, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListNodegroupsResponseTypeDef:
        """
        [Client.list_nodegroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.list_nodegroups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_updates(
        self, name: str, nodegroupName: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListUpdatesResponseTypeDef:
        """
        [Client.list_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.list_updates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_cluster_config(
        self,
        name: str,
        resourcesVpcConfig: VpcConfigRequestTypeDef = None,
        logging: LoggingTypeDef = None,
        clientRequestToken: str = None,
    ) -> UpdateClusterConfigResponseTypeDef:
        """
        [Client.update_cluster_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.update_cluster_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_cluster_version(
        self, name: str, version: str, clientRequestToken: str = None
    ) -> UpdateClusterVersionResponseTypeDef:
        """
        [Client.update_cluster_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.update_cluster_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_nodegroup_config(
        self,
        clusterName: str,
        nodegroupName: str,
        labels: UpdateLabelsPayloadTypeDef = None,
        scalingConfig: NodegroupScalingConfigTypeDef = None,
        clientRequestToken: str = None,
    ) -> UpdateNodegroupConfigResponseTypeDef:
        """
        [Client.update_nodegroup_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.update_nodegroup_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_nodegroup_version(
        self,
        clusterName: str,
        nodegroupName: str,
        version: str = None,
        releaseVersion: str = None,
        force: bool = None,
        clientRequestToken: str = None,
    ) -> UpdateNodegroupVersionResponseTypeDef:
        """
        [Client.update_nodegroup_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Client.update_nodegroup_version)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_clusters"]
    ) -> paginator_scope.ListClustersPaginator:
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Paginator.ListClusters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_fargate_profiles"]
    ) -> paginator_scope.ListFargateProfilesPaginator:
        """
        [Paginator.ListFargateProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Paginator.ListFargateProfiles)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_nodegroups"]
    ) -> paginator_scope.ListNodegroupsPaginator:
        """
        [Paginator.ListNodegroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Paginator.ListNodegroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_updates"]
    ) -> paginator_scope.ListUpdatesPaginator:
        """
        [Paginator.ListUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Paginator.ListUpdates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["cluster_active"]
    ) -> waiter_scope.ClusterActiveWaiter:
        """
        [Waiter.ClusterActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Waiter.ClusterActive)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["cluster_deleted"]
    ) -> waiter_scope.ClusterDeletedWaiter:
        """
        [Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Waiter.ClusterDeleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["nodegroup_active"]
    ) -> waiter_scope.NodegroupActiveWaiter:
        """
        [Waiter.NodegroupActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Waiter.NodegroupActive)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["nodegroup_deleted"]
    ) -> waiter_scope.NodegroupDeletedWaiter:
        """
        [Waiter.NodegroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/eks.html#EKS.Waiter.NodegroupDeleted)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ClientException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServerException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    UnsupportedAvailabilityZoneException: Boto3ClientError
