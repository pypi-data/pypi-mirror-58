"Main interface for kinesis service"
from mypy_boto3_kinesis.client import KinesisClient as Client, KinesisClient
from mypy_boto3_kinesis.paginator import (
    DescribeStreamPaginator,
    ListShardsPaginator,
    ListStreamConsumersPaginator,
    ListStreamsPaginator,
)
from mypy_boto3_kinesis.waiter import StreamExistsWaiter, StreamNotExistsWaiter


__all__ = (
    "Client",
    "DescribeStreamPaginator",
    "KinesisClient",
    "ListShardsPaginator",
    "ListStreamConsumersPaginator",
    "ListStreamsPaginator",
    "StreamExistsWaiter",
    "StreamNotExistsWaiter",
)
