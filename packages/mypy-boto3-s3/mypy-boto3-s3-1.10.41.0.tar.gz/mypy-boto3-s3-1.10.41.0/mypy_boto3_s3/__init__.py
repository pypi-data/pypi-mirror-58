"Main interface for s3 service"
from mypy_boto3_s3.client import S3Client, S3Client as Client
from mypy_boto3_s3.paginator import (
    ListMultipartUploadsPaginator,
    ListObjectVersionsPaginator,
    ListObjectsPaginator,
    ListObjectsV2Paginator,
    ListPartsPaginator,
)
from mypy_boto3_s3.service_resource import S3ServiceResource, S3ServiceResource as ServiceResource
from mypy_boto3_s3.waiter import (
    BucketExistsWaiter,
    BucketNotExistsWaiter,
    ObjectExistsWaiter,
    ObjectNotExistsWaiter,
)


__all__ = (
    "BucketExistsWaiter",
    "BucketNotExistsWaiter",
    "Client",
    "ListMultipartUploadsPaginator",
    "ListObjectVersionsPaginator",
    "ListObjectsPaginator",
    "ListObjectsV2Paginator",
    "ListPartsPaginator",
    "ObjectExistsWaiter",
    "ObjectNotExistsWaiter",
    "S3Client",
    "S3ServiceResource",
    "ServiceResource",
)
