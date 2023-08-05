"Main interface for s3 service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_s3.type_defs import (
    ListMultipartUploadsOutputTypeDef,
    ListObjectVersionsOutputTypeDef,
    ListObjectsOutputTypeDef,
    ListObjectsV2OutputTypeDef,
    ListPartsOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListMultipartUploadsPaginator",
    "ListObjectVersionsPaginator",
    "ListObjectsPaginator",
    "ListObjectsV2Paginator",
    "ListPartsPaginator",
)


class ListMultipartUploadsPaginator(Boto3Paginator):
    """
    [Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/s3.html#S3.Paginator.ListMultipartUploads)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListMultipartUploadsOutputTypeDef, None, None]:
        """
        [ListMultipartUploads.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/s3.html#S3.Paginator.ListMultipartUploads.paginate)
        """


class ListObjectVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListObjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/s3.html#S3.Paginator.ListObjectVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListObjectVersionsOutputTypeDef, None, None]:
        """
        [ListObjectVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/s3.html#S3.Paginator.ListObjectVersions.paginate)
        """


class ListObjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListObjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/s3.html#S3.Paginator.ListObjects)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        RequestPayer: Literal["requester"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListObjectsOutputTypeDef, None, None]:
        """
        [ListObjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/s3.html#S3.Paginator.ListObjects.paginate)
        """


class ListObjectsV2Paginator(Boto3Paginator):
    """
    [Paginator.ListObjectsV2 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/s3.html#S3.Paginator.ListObjectsV2)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: Literal["url"] = None,
        Prefix: str = None,
        FetchOwner: bool = None,
        StartAfter: str = None,
        RequestPayer: Literal["requester"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListObjectsV2OutputTypeDef, None, None]:
        """
        [ListObjectsV2.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/s3.html#S3.Paginator.ListObjectsV2.paginate)
        """


class ListPartsPaginator(Boto3Paginator):
    """
    [Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/s3.html#S3.Paginator.ListParts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: Literal["requester"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPartsOutputTypeDef, None, None]:
        """
        [ListParts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/s3.html#S3.Paginator.ListParts.paginate)
        """
