"Main interface for medialive service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_medialive.type_defs import WaiterConfigTypeDef


__all__ = (
    "ChannelCreatedWaiter",
    "ChannelDeletedWaiter",
    "ChannelRunningWaiter",
    "ChannelStoppedWaiter",
    "MultiplexCreatedWaiter",
    "MultiplexDeletedWaiter",
    "MultiplexRunningWaiter",
    "MultiplexStoppedWaiter",
)


class ChannelCreatedWaiter(Boto3Waiter):
    """
    [Waiter.ChannelCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.ChannelCreated)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ChannelCreated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.ChannelCreated.wait)
        """


class ChannelDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ChannelDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.ChannelDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ChannelDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.ChannelDeleted.wait)
        """


class ChannelRunningWaiter(Boto3Waiter):
    """
    [Waiter.ChannelRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.ChannelRunning)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ChannelRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.ChannelRunning.wait)
        """


class ChannelStoppedWaiter(Boto3Waiter):
    """
    [Waiter.ChannelStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.ChannelStopped)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, ChannelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [ChannelStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.ChannelStopped.wait)
        """


class MultiplexCreatedWaiter(Boto3Waiter):
    """
    [Waiter.MultiplexCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreated)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [MultiplexCreated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreated.wait)
        """


class MultiplexDeletedWaiter(Boto3Waiter):
    """
    [Waiter.MultiplexDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [MultiplexDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeleted.wait)
        """


class MultiplexRunningWaiter(Boto3Waiter):
    """
    [Waiter.MultiplexRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunning)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [MultiplexRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunning.wait)
        """


class MultiplexStoppedWaiter(Boto3Waiter):
    """
    [Waiter.MultiplexStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.MultiplexStopped)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, MultiplexId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [MultiplexStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/medialive.html#MediaLive.Waiter.MultiplexStopped.wait)
        """
