"Main interface for eks service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


CertificateTypeDef = TypedDict("CertificateTypeDef", {"data": str}, total=False)

OIDCTypeDef = TypedDict("OIDCTypeDef", {"issuer": str}, total=False)

IdentityTypeDef = TypedDict("IdentityTypeDef", {"oidc": OIDCTypeDef}, total=False)

LogSetupTypeDef = TypedDict(
    "LogSetupTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)

LoggingTypeDef = TypedDict("LoggingTypeDef", {"clusterLogging": List[LogSetupTypeDef]}, total=False)

VpcConfigResponseTypeDef = TypedDict(
    "VpcConfigResponseTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": VpcConfigResponseTypeDef,
        "logging": LoggingTypeDef,
        "identity": IdentityTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING"],
        "certificateAuthority": CertificateTypeDef,
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef", {"cluster": ClusterTypeDef}, total=False
)

FargateProfileSelectorTypeDef = TypedDict(
    "FargateProfileSelectorTypeDef", {"namespace": str, "labels": Dict[str, str]}, total=False
)

FargateProfileTypeDef = TypedDict(
    "FargateProfileTypeDef",
    {
        "fargateProfileName": str,
        "fargateProfileArn": str,
        "clusterName": str,
        "createdAt": datetime,
        "podExecutionRoleArn": str,
        "subnets": List[str],
        "selectors": List[FargateProfileSelectorTypeDef],
        "status": Literal["CREATING", "ACTIVE", "DELETING", "CREATE_FAILED", "DELETE_FAILED"],
        "tags": Dict[str, str],
    },
    total=False,
)

CreateFargateProfileResponseTypeDef = TypedDict(
    "CreateFargateProfileResponseTypeDef", {"fargateProfile": FargateProfileTypeDef}, total=False
)

IssueTypeDef = TypedDict(
    "IssueTypeDef",
    {
        "code": Literal[
            "AutoScalingGroupNotFound",
            "Ec2SecurityGroupNotFound",
            "Ec2SecurityGroupDeletionFailure",
            "Ec2LaunchTemplateNotFound",
            "Ec2LaunchTemplateVersionMismatch",
            "IamInstanceProfileNotFound",
            "IamNodeRoleNotFound",
            "AsgInstanceLaunchFailures",
            "InstanceLimitExceeded",
            "InsufficientFreeAddresses",
            "AccessDenied",
            "InternalFailure",
        ],
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)

NodegroupHealthTypeDef = TypedDict(
    "NodegroupHealthTypeDef", {"issues": List[IssueTypeDef]}, total=False
)

AutoScalingGroupTypeDef = TypedDict("AutoScalingGroupTypeDef", {"name": str}, total=False)

NodegroupResourcesTypeDef = TypedDict(
    "NodegroupResourcesTypeDef",
    {"autoScalingGroups": List[AutoScalingGroupTypeDef], "remoteAccessSecurityGroup": str},
    total=False,
)

NodegroupScalingConfigTypeDef = TypedDict(
    "NodegroupScalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)

RemoteAccessConfigTypeDef = TypedDict(
    "RemoteAccessConfigTypeDef", {"ec2SshKey": str, "sourceSecurityGroups": List[str]}, total=False
)

NodegroupTypeDef = TypedDict(
    "NodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": Literal[
            "CREATING",
            "ACTIVE",
            "UPDATING",
            "DELETING",
            "CREATE_FAILED",
            "DELETE_FAILED",
            "DEGRADED",
        ],
        "scalingConfig": NodegroupScalingConfigTypeDef,
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": RemoteAccessConfigTypeDef,
        "amiType": Literal["AL2_x86_64", "AL2_x86_64_GPU"],
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": NodegroupResourcesTypeDef,
        "diskSize": int,
        "health": NodegroupHealthTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateNodegroupResponseTypeDef = TypedDict(
    "CreateNodegroupResponseTypeDef", {"nodegroup": NodegroupTypeDef}, total=False
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef", {"cluster": ClusterTypeDef}, total=False
)

DeleteFargateProfileResponseTypeDef = TypedDict(
    "DeleteFargateProfileResponseTypeDef", {"fargateProfile": FargateProfileTypeDef}, total=False
)

DeleteNodegroupResponseTypeDef = TypedDict(
    "DeleteNodegroupResponseTypeDef", {"nodegroup": NodegroupTypeDef}, total=False
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef", {"cluster": ClusterTypeDef}, total=False
)

DescribeFargateProfileResponseTypeDef = TypedDict(
    "DescribeFargateProfileResponseTypeDef", {"fargateProfile": FargateProfileTypeDef}, total=False
)

DescribeNodegroupResponseTypeDef = TypedDict(
    "DescribeNodegroupResponseTypeDef", {"nodegroup": NodegroupTypeDef}, total=False
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)

UpdateParamTypeDef = TypedDict(
    "UpdateParamTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
        ],
        "value": str,
    },
    total=False,
)

UpdateTypeDef = TypedDict(
    "UpdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal["VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate"],
        "params": List[UpdateParamTypeDef],
        "createdAt": datetime,
        "errors": List[ErrorDetailTypeDef],
    },
    total=False,
)

DescribeUpdateResponseTypeDef = TypedDict(
    "DescribeUpdateResponseTypeDef", {"update": UpdateTypeDef}, total=False
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef", {"clusters": List[str], "nextToken": str}, total=False
)

ListFargateProfilesResponseTypeDef = TypedDict(
    "ListFargateProfilesResponseTypeDef",
    {"fargateProfileNames": List[str], "nextToken": str},
    total=False,
)

ListNodegroupsResponseTypeDef = TypedDict(
    "ListNodegroupsResponseTypeDef", {"nodegroups": List[str], "nextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ListUpdatesResponseTypeDef = TypedDict(
    "ListUpdatesResponseTypeDef", {"updateIds": List[str], "nextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateClusterConfigResponseTypeDef = TypedDict(
    "UpdateClusterConfigResponseTypeDef", {"update": UpdateTypeDef}, total=False
)

UpdateClusterVersionResponseTypeDef = TypedDict(
    "UpdateClusterVersionResponseTypeDef", {"update": UpdateTypeDef}, total=False
)

UpdateLabelsPayloadTypeDef = TypedDict(
    "UpdateLabelsPayloadTypeDef",
    {"addOrUpdateLabels": Dict[str, str], "removeLabels": List[str]},
    total=False,
)

UpdateNodegroupConfigResponseTypeDef = TypedDict(
    "UpdateNodegroupConfigResponseTypeDef", {"update": UpdateTypeDef}, total=False
)

UpdateNodegroupVersionResponseTypeDef = TypedDict(
    "UpdateNodegroupVersionResponseTypeDef", {"update": UpdateTypeDef}, total=False
)

VpcConfigRequestTypeDef = TypedDict(
    "VpcConfigRequestTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
