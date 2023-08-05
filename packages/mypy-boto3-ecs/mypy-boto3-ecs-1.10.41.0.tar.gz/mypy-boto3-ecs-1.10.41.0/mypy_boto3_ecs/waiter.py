"Main interface for ecs service Waiters"
from __future__ import annotations

import sys
from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_ecs.type_defs import WaiterConfigTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ServicesInactiveWaiter",
    "ServicesStableWaiter",
    "TasksRunningWaiter",
    "TasksStoppedWaiter",
)


class ServicesInactiveWaiter(Boto3Waiter):
    """
    [Waiter.ServicesInactive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ecs.html#ECS.Waiter.ServicesInactive)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        services: List[str],
        cluster: str = None,
        include: List[Literal["TAGS"]] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ServicesInactive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ecs.html#ECS.Waiter.ServicesInactive.wait)
        """


class ServicesStableWaiter(Boto3Waiter):
    """
    [Waiter.ServicesStable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ecs.html#ECS.Waiter.ServicesStable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        services: List[str],
        cluster: str = None,
        include: List[Literal["TAGS"]] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ServicesStable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ecs.html#ECS.Waiter.ServicesStable.wait)
        """


class TasksRunningWaiter(Boto3Waiter):
    """
    [Waiter.TasksRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ecs.html#ECS.Waiter.TasksRunning)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        tasks: List[str],
        cluster: str = None,
        include: List[Literal["TAGS"]] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [TasksRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ecs.html#ECS.Waiter.TasksRunning.wait)
        """


class TasksStoppedWaiter(Boto3Waiter):
    """
    [Waiter.TasksStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ecs.html#ECS.Waiter.TasksStopped)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        tasks: List[str],
        cluster: str = None,
        include: List[Literal["TAGS"]] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [TasksStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ecs.html#ECS.Waiter.TasksStopped.wait)
        """
