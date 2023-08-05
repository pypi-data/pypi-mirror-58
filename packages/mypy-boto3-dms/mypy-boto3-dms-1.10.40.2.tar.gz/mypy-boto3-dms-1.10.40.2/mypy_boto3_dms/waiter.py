"Main interface for dms service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_dms.type_defs import FilterTypeDef, WaiterConfigTypeDef


__all__ = (
    "EndpointDeletedWaiter",
    "ReplicationInstanceAvailableWaiter",
    "ReplicationInstanceDeletedWaiter",
    "ReplicationTaskDeletedWaiter",
    "ReplicationTaskReadyWaiter",
    "ReplicationTaskRunningWaiter",
    "ReplicationTaskStoppedWaiter",
    "TestConnectionSucceedsWaiter",
)


class EndpointDeletedWaiter(Boto3Waiter):
    """
    [Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.EndpointDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [EndpointDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.EndpointDeleted.wait)
        """


class ReplicationInstanceAvailableWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationInstanceAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable.wait)
        """


class ReplicationInstanceDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationInstanceDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted.wait)
        """


class ReplicationTaskDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationTaskDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationTaskDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted.wait)
        """


class ReplicationTaskReadyWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationTaskReady documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskReady)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationTaskReady.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskReady.wait)
        """


class ReplicationTaskRunningWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationTaskRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationTaskRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning.wait)
        """


class ReplicationTaskStoppedWaiter(Boto3Waiter):
    """
    [Waiter.ReplicationTaskStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ReplicationTaskStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped.wait)
        """


class TestConnectionSucceedsWaiter(Boto3Waiter):
    """
    [Waiter.TestConnectionSucceeds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [TestConnectionSucceeds.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds.wait)
        """
