"Main interface for sqs service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sqs.client as client_scope
from mypy_boto3_sqs.type_defs import (
    ChangeMessageVisibilityBatchRequestEntryTypeDef,
    ChangeMessageVisibilityBatchResultTypeDef,
    CreateQueueResultTypeDef,
    DeleteMessageBatchRequestEntryTypeDef,
    DeleteMessageBatchResultTypeDef,
    GetQueueAttributesResultTypeDef,
    GetQueueUrlResultTypeDef,
    ListDeadLetterSourceQueuesResultTypeDef,
    ListQueueTagsResultTypeDef,
    ListQueuesResultTypeDef,
    MessageAttributeValueTypeDef,
    MessageSystemAttributeValueTypeDef,
    ReceiveMessageResultTypeDef,
    SendMessageBatchRequestEntryTypeDef,
    SendMessageBatchResultTypeDef,
    SendMessageResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SQSClient",)


class SQSClient(BaseClient):
    """
    [SQS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_permission(
        self, QueueUrl: str, Label: str, AWSAccountIds: List[str], Actions: List[str]
    ) -> None:
        """
        [Client.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.add_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def change_message_visibility(
        self, QueueUrl: str, ReceiptHandle: str, VisibilityTimeout: int
    ) -> None:
        """
        [Client.change_message_visibility documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.change_message_visibility)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def change_message_visibility_batch(
        self, QueueUrl: str, Entries: List[ChangeMessageVisibilityBatchRequestEntryTypeDef]
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        [Client.change_message_visibility_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.change_message_visibility_batch)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_queue(
        self,
        QueueName: str,
        Attributes: Dict[
            Literal[
                "All",
                "Policy",
                "VisibilityTimeout",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesNotVisible",
                "CreatedTimestamp",
                "LastModifiedTimestamp",
                "QueueArn",
                "ApproximateNumberOfMessagesDelayed",
                "DelaySeconds",
                "ReceiveMessageWaitTimeSeconds",
                "RedrivePolicy",
                "FifoQueue",
                "ContentBasedDeduplication",
                "KmsMasterKeyId",
                "KmsDataKeyReusePeriodSeconds",
            ],
            str,
        ] = None,
        tags: Dict[str, str] = None,
    ) -> CreateQueueResultTypeDef:
        """
        [Client.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.create_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_message(self, QueueUrl: str, ReceiptHandle: str) -> None:
        """
        [Client.delete_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.delete_message)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_message_batch(
        self, QueueUrl: str, Entries: List[DeleteMessageBatchRequestEntryTypeDef]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        [Client.delete_message_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.delete_message_batch)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_queue(self, QueueUrl: str) -> None:
        """
        [Client.delete_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.delete_queue)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_queue_attributes(
        self,
        QueueUrl: str,
        AttributeNames: List[
            Literal[
                "All",
                "Policy",
                "VisibilityTimeout",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesNotVisible",
                "CreatedTimestamp",
                "LastModifiedTimestamp",
                "QueueArn",
                "ApproximateNumberOfMessagesDelayed",
                "DelaySeconds",
                "ReceiveMessageWaitTimeSeconds",
                "RedrivePolicy",
                "FifoQueue",
                "ContentBasedDeduplication",
                "KmsMasterKeyId",
                "KmsDataKeyReusePeriodSeconds",
            ]
        ] = None,
    ) -> GetQueueAttributesResultTypeDef:
        """
        [Client.get_queue_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.get_queue_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_queue_url(
        self, QueueName: str, QueueOwnerAWSAccountId: str = None
    ) -> GetQueueUrlResultTypeDef:
        """
        [Client.get_queue_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.get_queue_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dead_letter_source_queues(
        self, QueueUrl: str
    ) -> ListDeadLetterSourceQueuesResultTypeDef:
        """
        [Client.list_dead_letter_source_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.list_dead_letter_source_queues)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_queue_tags(self, QueueUrl: str) -> ListQueueTagsResultTypeDef:
        """
        [Client.list_queue_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.list_queue_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_queues(self, QueueNamePrefix: str = None) -> ListQueuesResultTypeDef:
        """
        [Client.list_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.list_queues)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purge_queue(self, QueueUrl: str) -> None:
        """
        [Client.purge_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.purge_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def receive_message(
        self,
        QueueUrl: str,
        AttributeNames: List[
            Literal[
                "All",
                "Policy",
                "VisibilityTimeout",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesNotVisible",
                "CreatedTimestamp",
                "LastModifiedTimestamp",
                "QueueArn",
                "ApproximateNumberOfMessagesDelayed",
                "DelaySeconds",
                "ReceiveMessageWaitTimeSeconds",
                "RedrivePolicy",
                "FifoQueue",
                "ContentBasedDeduplication",
                "KmsMasterKeyId",
                "KmsDataKeyReusePeriodSeconds",
            ]
        ] = None,
        MessageAttributeNames: List[str] = None,
        MaxNumberOfMessages: int = None,
        VisibilityTimeout: int = None,
        WaitTimeSeconds: int = None,
        ReceiveRequestAttemptId: str = None,
    ) -> ReceiveMessageResultTypeDef:
        """
        [Client.receive_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.receive_message)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_permission(self, QueueUrl: str, Label: str) -> None:
        """
        [Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.remove_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_message(
        self,
        QueueUrl: str,
        MessageBody: str,
        DelaySeconds: int = None,
        MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
        MessageSystemAttributes: Dict[
            Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef
        ] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> SendMessageResultTypeDef:
        """
        [Client.send_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.send_message)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_message_batch(
        self, QueueUrl: str, Entries: List[SendMessageBatchRequestEntryTypeDef]
    ) -> SendMessageBatchResultTypeDef:
        """
        [Client.send_message_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.send_message_batch)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_queue_attributes(
        self,
        QueueUrl: str,
        Attributes: Dict[
            Literal[
                "All",
                "Policy",
                "VisibilityTimeout",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesNotVisible",
                "CreatedTimestamp",
                "LastModifiedTimestamp",
                "QueueArn",
                "ApproximateNumberOfMessagesDelayed",
                "DelaySeconds",
                "ReceiveMessageWaitTimeSeconds",
                "RedrivePolicy",
                "FifoQueue",
                "ContentBasedDeduplication",
                "KmsMasterKeyId",
                "KmsDataKeyReusePeriodSeconds",
            ],
            str,
        ],
    ) -> None:
        """
        [Client.set_queue_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.set_queue_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_queue(self, QueueUrl: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.tag_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_queue(self, QueueUrl: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/sqs.html#SQS.Client.untag_queue)
        """


class Exceptions:
    BatchEntryIdsNotDistinct: Boto3ClientError
    BatchRequestTooLong: Boto3ClientError
    ClientError: Boto3ClientError
    EmptyBatchRequest: Boto3ClientError
    InvalidAttributeName: Boto3ClientError
    InvalidBatchEntryId: Boto3ClientError
    InvalidIdFormat: Boto3ClientError
    InvalidMessageContents: Boto3ClientError
    MessageNotInflight: Boto3ClientError
    OverLimit: Boto3ClientError
    PurgeQueueInProgress: Boto3ClientError
    QueueDeletedRecently: Boto3ClientError
    QueueDoesNotExist: Boto3ClientError
    QueueNameExists: Boto3ClientError
    ReceiptHandleIsInvalid: Boto3ClientError
    TooManyEntriesInBatchRequest: Boto3ClientError
    UnsupportedOperation: Boto3ClientError
