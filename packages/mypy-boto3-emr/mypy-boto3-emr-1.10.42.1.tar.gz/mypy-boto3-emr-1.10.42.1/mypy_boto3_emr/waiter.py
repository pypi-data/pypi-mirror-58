"Main interface for emr service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_emr.type_defs import WaiterConfigTypeDef


__all__ = ("ClusterRunningWaiter", "ClusterTerminatedWaiter", "StepCompleteWaiter")


class ClusterRunningWaiter(Boto3Waiter):
    """
    [Waiter.ClusterRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/emr.html#EMR.Waiter.ClusterRunning)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, ClusterId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ClusterRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/emr.html#EMR.Waiter.ClusterRunning.wait)
        """


class ClusterTerminatedWaiter(Boto3Waiter):
    """
    [Waiter.ClusterTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/emr.html#EMR.Waiter.ClusterTerminated)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, ClusterId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ClusterTerminated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/emr.html#EMR.Waiter.ClusterTerminated.wait)
        """


class StepCompleteWaiter(Boto3Waiter):
    """
    [Waiter.StepComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/emr.html#EMR.Waiter.StepComplete)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, ClusterId: str, StepId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [StepComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/emr.html#EMR.Waiter.StepComplete.wait)
        """
