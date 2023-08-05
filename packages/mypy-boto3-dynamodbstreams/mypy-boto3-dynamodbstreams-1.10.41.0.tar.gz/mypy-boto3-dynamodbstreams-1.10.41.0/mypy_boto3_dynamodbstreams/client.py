"Main interface for dynamodbstreams service Client"
from __future__ import annotations

import sys
from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_dynamodbstreams.client as client_scope
from mypy_boto3_dynamodbstreams.type_defs import (
    DescribeStreamOutputTypeDef,
    GetRecordsOutputTypeDef,
    GetShardIteratorOutputTypeDef,
    ListStreamsOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DynamoDBStreamsClient",)


class DynamoDBStreamsClient(BaseClient):
    """
    [DynamoDBStreams.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodbstreams.html#DynamoDBStreams.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stream(
        self, StreamArn: str, Limit: int = None, ExclusiveStartShardId: str = None
    ) -> DescribeStreamOutputTypeDef:
        """
        [Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.describe_stream)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_records(self, ShardIterator: str, Limit: int = None) -> GetRecordsOutputTypeDef:
        """
        [Client.get_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_records)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_shard_iterator(
        self,
        StreamArn: str,
        ShardId: str,
        ShardIteratorType: Literal[
            "TRIM_HORIZON", "LATEST", "AT_SEQUENCE_NUMBER", "AFTER_SEQUENCE_NUMBER"
        ],
        SequenceNumber: str = None,
    ) -> GetShardIteratorOutputTypeDef:
        """
        [Client.get_shard_iterator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_shard_iterator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_streams(
        self, TableName: str = None, Limit: int = None, ExclusiveStartStreamArn: str = None
    ) -> ListStreamsOutputTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.list_streams)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ExpiredIteratorException: Boto3ClientError
    InternalServerError: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TrimmedDataAccessException: Boto3ClientError
