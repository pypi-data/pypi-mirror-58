"Main interface for s3 service Waiters"
from __future__ import annotations

from datetime import datetime
import sys
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_s3.type_defs import WaiterConfigTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BucketExistsWaiter",
    "BucketNotExistsWaiter",
    "ObjectExistsWaiter",
    "ObjectNotExistsWaiter",
)


class BucketExistsWaiter(Boto3Waiter):
    """
    [Waiter.BucketExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/s3.html#S3.Waiter.BucketExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, Bucket: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [BucketExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/s3.html#S3.Waiter.BucketExists.wait)
        """


class BucketNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.BucketNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/s3.html#S3.Waiter.BucketNotExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, Bucket: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [BucketNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/s3.html#S3.Waiter.BucketNotExists.wait)
        """


class ObjectExistsWaiter(Boto3Waiter):
    """
    [Waiter.ObjectExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/s3.html#S3.Waiter.ObjectExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Bucket: str,
        Key: str,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ObjectExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/s3.html#S3.Waiter.ObjectExists.wait)
        """


class ObjectNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.ObjectNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/s3.html#S3.Waiter.ObjectNotExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Bucket: str,
        Key: str,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ObjectNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/s3.html#S3.Waiter.ObjectNotExists.wait)
        """
