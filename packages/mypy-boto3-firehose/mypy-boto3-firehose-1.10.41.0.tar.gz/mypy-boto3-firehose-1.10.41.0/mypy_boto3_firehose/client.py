"Main interface for firehose service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_firehose.client as client_scope
from mypy_boto3_firehose.type_defs import (
    CreateDeliveryStreamOutputTypeDef,
    DeliveryStreamEncryptionConfigurationInputTypeDef,
    DescribeDeliveryStreamOutputTypeDef,
    ElasticsearchDestinationConfigurationTypeDef,
    ElasticsearchDestinationUpdateTypeDef,
    ExtendedS3DestinationConfigurationTypeDef,
    ExtendedS3DestinationUpdateTypeDef,
    KinesisStreamSourceConfigurationTypeDef,
    ListDeliveryStreamsOutputTypeDef,
    ListTagsForDeliveryStreamOutputTypeDef,
    PutRecordBatchOutputTypeDef,
    PutRecordOutputTypeDef,
    RecordTypeDef,
    RedshiftDestinationConfigurationTypeDef,
    RedshiftDestinationUpdateTypeDef,
    S3DestinationConfigurationTypeDef,
    S3DestinationUpdateTypeDef,
    SplunkDestinationConfigurationTypeDef,
    SplunkDestinationUpdateTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FirehoseClient",)


class FirehoseClient(BaseClient):
    """
    [Firehose.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_delivery_stream(
        self,
        DeliveryStreamName: str,
        DeliveryStreamType: Literal["DirectPut", "KinesisStreamAsSource"] = None,
        KinesisStreamSourceConfiguration: KinesisStreamSourceConfigurationTypeDef = None,
        DeliveryStreamEncryptionConfigurationInput: DeliveryStreamEncryptionConfigurationInputTypeDef = None,
        S3DestinationConfiguration: S3DestinationConfigurationTypeDef = None,
        ExtendedS3DestinationConfiguration: ExtendedS3DestinationConfigurationTypeDef = None,
        RedshiftDestinationConfiguration: RedshiftDestinationConfigurationTypeDef = None,
        ElasticsearchDestinationConfiguration: ElasticsearchDestinationConfigurationTypeDef = None,
        SplunkDestinationConfiguration: SplunkDestinationConfigurationTypeDef = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDeliveryStreamOutputTypeDef:
        """
        [Client.create_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.create_delivery_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_delivery_stream(
        self, DeliveryStreamName: str, AllowForceDelete: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.delete_delivery_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_delivery_stream(
        self, DeliveryStreamName: str, Limit: int = None, ExclusiveStartDestinationId: str = None
    ) -> DescribeDeliveryStreamOutputTypeDef:
        """
        [Client.describe_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.describe_delivery_stream)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_delivery_streams(
        self,
        Limit: int = None,
        DeliveryStreamType: Literal["DirectPut", "KinesisStreamAsSource"] = None,
        ExclusiveStartDeliveryStreamName: str = None,
    ) -> ListDeliveryStreamsOutputTypeDef:
        """
        [Client.list_delivery_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.list_delivery_streams)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_delivery_stream(
        self, DeliveryStreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None
    ) -> ListTagsForDeliveryStreamOutputTypeDef:
        """
        [Client.list_tags_for_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.list_tags_for_delivery_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_record(self, DeliveryStreamName: str, Record: RecordTypeDef) -> PutRecordOutputTypeDef:
        """
        [Client.put_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.put_record)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_record_batch(
        self, DeliveryStreamName: str, Records: List[RecordTypeDef]
    ) -> PutRecordBatchOutputTypeDef:
        """
        [Client.put_record_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.put_record_batch)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_delivery_stream_encryption(
        self,
        DeliveryStreamName: str,
        DeliveryStreamEncryptionConfigurationInput: DeliveryStreamEncryptionConfigurationInputTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.start_delivery_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.start_delivery_stream_encryption)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_delivery_stream_encryption(self, DeliveryStreamName: str) -> Dict[str, Any]:
        """
        [Client.stop_delivery_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.stop_delivery_stream_encryption)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_delivery_stream(
        self, DeliveryStreamName: str, Tags: List[TagTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.tag_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.tag_delivery_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_delivery_stream(self, DeliveryStreamName: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.untag_delivery_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_destination(
        self,
        DeliveryStreamName: str,
        CurrentDeliveryStreamVersionId: str,
        DestinationId: str,
        S3DestinationUpdate: S3DestinationUpdateTypeDef = None,
        ExtendedS3DestinationUpdate: ExtendedS3DestinationUpdateTypeDef = None,
        RedshiftDestinationUpdate: RedshiftDestinationUpdateTypeDef = None,
        ElasticsearchDestinationUpdate: ElasticsearchDestinationUpdateTypeDef = None,
        SplunkDestinationUpdate: SplunkDestinationUpdateTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/firehose.html#Firehose.Client.update_destination)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidKMSResourceException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
