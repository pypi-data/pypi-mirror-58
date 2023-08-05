# mypy-boto3-eks

Type annotations for
[boto3.EKS 1.10.41](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/eks.html#EKS) service
compatible with [mypy](https://github.com/python/mypy), [VSCode](https://code.visualstudio.com/),
[PyCharm](https://www.jetbrains.com/pycharm/) and other tools.

More information can be found [here](https://vemel.github.io/mypy_boto3/).

- [mypy-boto3-eks](#mypy-boto3-eks)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `EKS` service.

```bash
python -m pip install boto3-stubs[mypy-boto3-eks]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking and auto-complete.

```python
import boto3

from mypy_boto3 import eks
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_eks as eks

# Use this client as usual, now mypy can check if your code is valid.
# Check if your IDE supports function overloads,
# you probably do not need explicit type annotations
# client = boto3.client("eks")
client: eks.EKSClient = boto3.client("eks")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: eks.EKSClient = session.client("eks")


# Waiters need type annotation on creation
cluster_active_waiter: eks.ClusterActiveWaiter = client.get_waiter("cluster_active")
cluster_deleted_waiter: eks.ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
nodegroup_active_waiter: eks.NodegroupActiveWaiter = client.get_waiter("nodegroup_active")
nodegroup_deleted_waiter: eks.NodegroupDeletedWaiter = client.get_waiter("nodegroup_deleted")

# Paginators need type annotation on creation
list_clusters_paginator: eks.ListClustersPaginator = client.get_paginator("list_clusters")
list_fargate_profiles_paginator: eks.ListFargateProfilesPaginator = client.get_paginator("list_fargate_profiles")
list_nodegroups_paginator: eks.ListNodegroupsPaginator = client.get_paginator("list_nodegroups")
list_updates_paginator: eks.ListUpdatesPaginator = client.get_paginator("list_updates")
```

## How it works

Fully automated [builder](https://github.com/vemel/mypy_boto3) carefully generates
type annotations for each service, patiently waiting for `boto3` updates. It delivers
a drop-in type annotations for you and makes sure that:

- All available `boto3` services are covered.
- Each public class and method of every `boto3` service gets valid type annotations
  extracted from the documentation (blame `botocore` docs if types are incorrect).
- Type annotations include up-to-date documentation.
- Link to documentation is provided for every method.
- Code is processed by [black](https://github.com/psf/black) for readability.