"Main interface for kinesis service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, IO, List, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_kinesis.client as client_scope

# pylint: disable=import-self
import mypy_boto3_kinesis.paginator as paginator_scope
from mypy_boto3_kinesis.type_defs import (
    DescribeLimitsOutputTypeDef,
    DescribeStreamConsumerOutputTypeDef,
    DescribeStreamOutputTypeDef,
    DescribeStreamSummaryOutputTypeDef,
    EnhancedMonitoringOutputTypeDef,
    GetRecordsOutputTypeDef,
    GetShardIteratorOutputTypeDef,
    ListShardsOutputTypeDef,
    ListStreamConsumersOutputTypeDef,
    ListStreamsOutputTypeDef,
    ListTagsForStreamOutputTypeDef,
    PutRecordOutputTypeDef,
    PutRecordsOutputTypeDef,
    PutRecordsRequestEntryTypeDef,
    RegisterStreamConsumerOutputTypeDef,
    StartingPositionTypeDef,
    SubscribeToShardOutputTypeDef,
    UpdateShardCountOutputTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_kinesis.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KinesisClient",)


class KinesisClient(BaseClient):
    """
    [Kinesis.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_stream(self, StreamName: str, Tags: Dict[str, str]) -> None:
        """
        [Client.add_tags_to_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.add_tags_to_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stream(self, StreamName: str, ShardCount: int) -> None:
        """
        [Client.create_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.create_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def decrease_stream_retention_period(self, StreamName: str, RetentionPeriodHours: int) -> None:
        """
        [Client.decrease_stream_retention_period documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.decrease_stream_retention_period)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_stream(self, StreamName: str, EnforceConsumerDeletion: bool = None) -> None:
        """
        [Client.delete_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.delete_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_stream_consumer(
        self, StreamARN: str = None, ConsumerName: str = None, ConsumerARN: str = None
    ) -> None:
        """
        [Client.deregister_stream_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.deregister_stream_consumer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_limits(self) -> DescribeLimitsOutputTypeDef:
        """
        [Client.describe_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.describe_limits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stream(
        self, StreamName: str, Limit: int = None, ExclusiveStartShardId: str = None
    ) -> DescribeStreamOutputTypeDef:
        """
        [Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.describe_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stream_consumer(
        self, StreamARN: str = None, ConsumerName: str = None, ConsumerARN: str = None
    ) -> DescribeStreamConsumerOutputTypeDef:
        """
        [Client.describe_stream_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.describe_stream_consumer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stream_summary(self, StreamName: str) -> DescribeStreamSummaryOutputTypeDef:
        """
        [Client.describe_stream_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.describe_stream_summary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_enhanced_monitoring(
        self,
        StreamName: str,
        ShardLevelMetrics: List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
    ) -> EnhancedMonitoringOutputTypeDef:
        """
        [Client.disable_enhanced_monitoring documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.disable_enhanced_monitoring)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_enhanced_monitoring(
        self,
        StreamName: str,
        ShardLevelMetrics: List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
    ) -> EnhancedMonitoringOutputTypeDef:
        """
        [Client.enable_enhanced_monitoring documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.enable_enhanced_monitoring)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_records(self, ShardIterator: str, Limit: int = None) -> GetRecordsOutputTypeDef:
        """
        [Client.get_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.get_records)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_shard_iterator(
        self,
        StreamName: str,
        ShardId: str,
        ShardIteratorType: Literal[
            "AT_SEQUENCE_NUMBER", "AFTER_SEQUENCE_NUMBER", "TRIM_HORIZON", "LATEST", "AT_TIMESTAMP"
        ],
        StartingSequenceNumber: str = None,
        Timestamp: datetime = None,
    ) -> GetShardIteratorOutputTypeDef:
        """
        [Client.get_shard_iterator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.get_shard_iterator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def increase_stream_retention_period(self, StreamName: str, RetentionPeriodHours: int) -> None:
        """
        [Client.increase_stream_retention_period documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.increase_stream_retention_period)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_shards(
        self,
        StreamName: str = None,
        NextToken: str = None,
        ExclusiveStartShardId: str = None,
        MaxResults: int = None,
        StreamCreationTimestamp: datetime = None,
    ) -> ListShardsOutputTypeDef:
        """
        [Client.list_shards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.list_shards)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_stream_consumers(
        self,
        StreamARN: str,
        NextToken: str = None,
        MaxResults: int = None,
        StreamCreationTimestamp: datetime = None,
    ) -> ListStreamConsumersOutputTypeDef:
        """
        [Client.list_stream_consumers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.list_stream_consumers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_streams(
        self, Limit: int = None, ExclusiveStartStreamName: str = None
    ) -> ListStreamsOutputTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.list_streams)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_stream(
        self, StreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None
    ) -> ListTagsForStreamOutputTypeDef:
        """
        [Client.list_tags_for_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.list_tags_for_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def merge_shards(self, StreamName: str, ShardToMerge: str, AdjacentShardToMerge: str) -> None:
        """
        [Client.merge_shards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.merge_shards)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_record(
        self,
        StreamName: str,
        Data: Union[bytes, IO],
        PartitionKey: str,
        ExplicitHashKey: str = None,
        SequenceNumberForOrdering: str = None,
    ) -> PutRecordOutputTypeDef:
        """
        [Client.put_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.put_record)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_records(
        self, Records: List[PutRecordsRequestEntryTypeDef], StreamName: str
    ) -> PutRecordsOutputTypeDef:
        """
        [Client.put_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.put_records)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_stream_consumer(
        self, StreamARN: str, ConsumerName: str
    ) -> RegisterStreamConsumerOutputTypeDef:
        """
        [Client.register_stream_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.register_stream_consumer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_stream(self, StreamName: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags_from_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.remove_tags_from_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def split_shard(self, StreamName: str, ShardToSplit: str, NewStartingHashKey: str) -> None:
        """
        [Client.split_shard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.split_shard)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_stream_encryption(
        self, StreamName: str, EncryptionType: Literal["NONE", "KMS"], KeyId: str
    ) -> None:
        """
        [Client.start_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.start_stream_encryption)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_stream_encryption(
        self, StreamName: str, EncryptionType: Literal["NONE", "KMS"], KeyId: str
    ) -> None:
        """
        [Client.stop_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.stop_stream_encryption)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def subscribe_to_shard(
        self, ConsumerARN: str, ShardId: str, StartingPosition: StartingPositionTypeDef
    ) -> SubscribeToShardOutputTypeDef:
        """
        [Client.subscribe_to_shard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.subscribe_to_shard)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_shard_count(
        self, StreamName: str, TargetShardCount: int, ScalingType: Literal["UNIFORM_SCALING"]
    ) -> UpdateShardCountOutputTypeDef:
        """
        [Client.update_shard_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Client.update_shard_count)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_stream"]
    ) -> paginator_scope.DescribeStreamPaginator:
        """
        [Paginator.DescribeStream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Paginator.DescribeStream)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_shards"]
    ) -> paginator_scope.ListShardsPaginator:
        """
        [Paginator.ListShards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Paginator.ListShards)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_stream_consumers"]
    ) -> paginator_scope.ListStreamConsumersPaginator:
        """
        [Paginator.ListStreamConsumers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Paginator.ListStreamConsumers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_streams"]
    ) -> paginator_scope.ListStreamsPaginator:
        """
        [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Paginator.ListStreams)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: Literal["stream_exists"]) -> waiter_scope.StreamExistsWaiter:
        """
        [Waiter.StreamExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Waiter.StreamExists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["stream_not_exists"]
    ) -> waiter_scope.StreamNotExistsWaiter:
        """
        [Waiter.StreamNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExists)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ExpiredIteratorException: Boto3ClientError
    ExpiredNextTokenException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    KMSAccessDeniedException: Boto3ClientError
    KMSDisabledException: Boto3ClientError
    KMSInvalidStateException: Boto3ClientError
    KMSNotFoundException: Boto3ClientError
    KMSOptInRequired: Boto3ClientError
    KMSThrottlingException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ProvisionedThroughputExceededException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
