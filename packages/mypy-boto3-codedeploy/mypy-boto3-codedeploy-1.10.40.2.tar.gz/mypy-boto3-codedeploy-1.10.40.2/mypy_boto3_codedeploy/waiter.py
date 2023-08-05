"Main interface for codedeploy service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_codedeploy.type_defs import WaiterConfigTypeDef


__all__ = ("DeploymentSuccessfulWaiter",)


class DeploymentSuccessfulWaiter(Boto3Waiter):
    """
    [Waiter.DeploymentSuccessful documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Waiter.DeploymentSuccessful)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, deploymentId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [DeploymentSuccessful.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Waiter.DeploymentSuccessful.wait)
        """
