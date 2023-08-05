"Main interface for sqs service"
from mypy_boto3_sqs.client import SQSClient as Client, SQSClient
from mypy_boto3_sqs.service_resource import (
    SQSServiceResource,
    SQSServiceResource as ServiceResource,
)


__all__ = ("Client", "SQSClient", "SQSServiceResource", "ServiceResource")
