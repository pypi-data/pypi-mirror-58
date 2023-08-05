"Main interface for efs service"
from mypy_boto3_efs.client import EFSClient, EFSClient as Client
from mypy_boto3_efs.paginator import (
    DescribeFileSystemsPaginator,
    DescribeMountTargetsPaginator,
    DescribeTagsPaginator,
)


__all__ = (
    "Client",
    "DescribeFileSystemsPaginator",
    "DescribeMountTargetsPaginator",
    "DescribeTagsPaginator",
    "EFSClient",
)
