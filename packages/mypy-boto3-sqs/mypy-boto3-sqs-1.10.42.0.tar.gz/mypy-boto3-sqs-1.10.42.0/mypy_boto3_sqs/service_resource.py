"Main interface for sqs service ServiceResource"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_sqs.service_resource as service_resource_scope
from mypy_boto3_sqs.type_defs import (
    ChangeMessageVisibilityBatchRequestEntryTypeDef,
    ChangeMessageVisibilityBatchResultTypeDef,
    CreateQueueResultTypeDef,
    DeleteMessageBatchRequestEntryTypeDef,
    DeleteMessageBatchResultTypeDef,
    GetQueueUrlResultTypeDef,
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


__all__ = (
    "SQSServiceResource",
    "Message",
    "Queue",
    "ServiceResourceQueuesCollection",
    "QueueDeadLetterSourceQueuesCollection",
)


class SQSServiceResource(Boto3ServiceResource):
    """
    [SQS.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.ServiceResource)
    """

    queues: service_resource_scope.ServiceResourceQueuesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Message(self, queue_url: str, receipt_handle: str) -> service_resource_scope.Message:
        """
        [ServiceResource.Message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.ServiceResource.Message)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Queue(self, url: str) -> service_resource_scope.Queue:
        """
        [ServiceResource.Queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.ServiceResource.Queue)
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
        [ServiceResource.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.ServiceResource.create_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.ServiceResource.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_queue_by_name(
        self, QueueName: str, QueueOwnerAWSAccountId: str = None
    ) -> GetQueueUrlResultTypeDef:
        """
        [ServiceResource.get_queue_by_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.ServiceResource.get_queue_by_name)
        """


class Message(Boto3ServiceResource):
    """
    [Message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.ServiceResource.Message)
    """

    message_id: str
    md5_of_body: str
    body: str
    attributes: Dict[str, Any]
    md5_of_message_attributes: str
    message_attributes: Dict[str, Any]
    queue_url: str
    receipt_handle: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def change_visibility(self, VisibilityTimeout: int) -> None:
        """
        [Message.change_visibility documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Message.change_visibility)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [Message.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Message.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Message.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Message.get_available_subresources)
        """


class Queue(Boto3ServiceResource):
    """
    [Queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.ServiceResource.Queue)
    """

    attributes: Dict[str, Any]
    url: str
    dead_letter_source_queues: service_resource_scope.QueueDeadLetterSourceQueuesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_permission(self, Label: str, AWSAccountIds: List[str], Actions: List[str]) -> None:
        """
        [Queue.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.add_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def change_message_visibility_batch(
        self, Entries: List[ChangeMessageVisibilityBatchRequestEntryTypeDef]
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        [Queue.change_message_visibility_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.change_message_visibility_batch)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        """
        [Queue.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_messages(
        self, Entries: List[DeleteMessageBatchRequestEntryTypeDef]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        [Queue.delete_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.delete_messages)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Queue.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Queue.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purge(self) -> None:
        """
        [Queue.purge documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.purge)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def receive_messages(
        self,
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
        [Queue.receive_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.receive_messages)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Queue.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_permission(self, Label: str) -> None:
        """
        [Queue.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.remove_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_message(
        self,
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
        [Queue.send_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.send_message)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_messages(
        self, Entries: List[SendMessageBatchRequestEntryTypeDef]
    ) -> SendMessageBatchResultTypeDef:
        """
        [Queue.send_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.send_messages)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_attributes(
        self,
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
        [Queue.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.set_attributes)
        """


class ServiceResourceQueuesCollection(ResourceCollection):
    """
    [ServiceResource.queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.ServiceResource.queues)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceQueuesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceQueuesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceQueuesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceQueuesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Queue]:
        pass


class QueueDeadLetterSourceQueuesCollection(ResourceCollection):
    """
    [Queue.dead_letter_source_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/sqs.html#SQS.Queue.dead_letter_source_queues)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.QueueDeadLetterSourceQueuesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.QueueDeadLetterSourceQueuesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.QueueDeadLetterSourceQueuesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.QueueDeadLetterSourceQueuesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Queue]:
        pass
