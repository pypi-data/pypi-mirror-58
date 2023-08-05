"Main interface for opsworks service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_opsworks.type_defs import WaiterConfigTypeDef


__all__ = (
    "AppExistsWaiter",
    "DeploymentSuccessfulWaiter",
    "InstanceOnlineWaiter",
    "InstanceRegisteredWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
)


class AppExistsWaiter(Boto3Waiter):
    """
    [Waiter.AppExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.AppExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        AppIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [AppExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.AppExists.wait)
        """


class DeploymentSuccessfulWaiter(Boto3Waiter):
    """
    [Waiter.DeploymentSuccessful documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.DeploymentSuccessful)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        AppId: str = None,
        DeploymentIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DeploymentSuccessful.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.DeploymentSuccessful.wait)
        """


class InstanceOnlineWaiter(Boto3Waiter):
    """
    [Waiter.InstanceOnline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.InstanceOnline)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceOnline.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.InstanceOnline.wait)
        """


class InstanceRegisteredWaiter(Boto3Waiter):
    """
    [Waiter.InstanceRegistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.InstanceRegistered)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceRegistered.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.InstanceRegistered.wait)
        """


class InstanceStoppedWaiter(Boto3Waiter):
    """
    [Waiter.InstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.InstanceStopped)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.InstanceStopped.wait)
        """


class InstanceTerminatedWaiter(Boto3Waiter):
    """
    [Waiter.InstanceTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.InstanceTerminated)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceTerminated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/opsworks.html#OpsWorks.Waiter.InstanceTerminated.wait)
        """
