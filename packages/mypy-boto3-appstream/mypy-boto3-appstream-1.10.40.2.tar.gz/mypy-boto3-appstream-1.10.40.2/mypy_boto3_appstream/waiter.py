"Main interface for appstream service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_appstream.type_defs import WaiterConfigTypeDef


__all__ = ("FleetStartedWaiter", "FleetStoppedWaiter")


class FleetStartedWaiter(Boto3Waiter):
    """
    [Waiter.FleetStarted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appstream.html#AppStream.Waiter.FleetStarted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Names: List[str] = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [FleetStarted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appstream.html#AppStream.Waiter.FleetStarted.wait)
        """


class FleetStoppedWaiter(Boto3Waiter):
    """
    [Waiter.FleetStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appstream.html#AppStream.Waiter.FleetStopped)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Names: List[str] = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [FleetStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/appstream.html#AppStream.Waiter.FleetStopped.wait)
        """
