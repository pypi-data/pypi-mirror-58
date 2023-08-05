"Main interface for kinesis service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_kinesis.type_defs import WaiterConfigTypeDef


__all__ = ("StreamExistsWaiter", "StreamNotExistsWaiter")


class StreamExistsWaiter(Boto3Waiter):
    """
    [Waiter.StreamExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/kinesis.html#Kinesis.Waiter.StreamExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [StreamExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/kinesis.html#Kinesis.Waiter.StreamExists.wait)
        """


class StreamNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.StreamNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StreamName: str,
        Limit: int = None,
        ExclusiveStartShardId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [StreamNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExists.wait)
        """
