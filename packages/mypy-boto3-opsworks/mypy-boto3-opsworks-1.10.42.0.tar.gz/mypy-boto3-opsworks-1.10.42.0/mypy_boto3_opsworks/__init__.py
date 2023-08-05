"Main interface for opsworks service"
from mypy_boto3_opsworks.client import OpsWorksClient, OpsWorksClient as Client
from mypy_boto3_opsworks.paginator import DescribeEcsClustersPaginator
from mypy_boto3_opsworks.service_resource import (
    OpsWorksServiceResource as ServiceResource,
    OpsWorksServiceResource,
)
from mypy_boto3_opsworks.waiter import (
    AppExistsWaiter,
    DeploymentSuccessfulWaiter,
    InstanceOnlineWaiter,
    InstanceRegisteredWaiter,
    InstanceStoppedWaiter,
    InstanceTerminatedWaiter,
)


__all__ = (
    "AppExistsWaiter",
    "Client",
    "DeploymentSuccessfulWaiter",
    "DescribeEcsClustersPaginator",
    "InstanceOnlineWaiter",
    "InstanceRegisteredWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
    "OpsWorksClient",
    "OpsWorksServiceResource",
    "ServiceResource",
)
