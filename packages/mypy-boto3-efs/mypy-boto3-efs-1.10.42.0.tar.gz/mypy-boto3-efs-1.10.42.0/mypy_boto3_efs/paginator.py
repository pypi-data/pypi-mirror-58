"Main interface for efs service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_efs.type_defs import (
    DescribeFileSystemsResponseTypeDef,
    DescribeMountTargetsResponseTypeDef,
    DescribeTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("DescribeFileSystemsPaginator", "DescribeMountTargetsPaginator", "DescribeTagsPaginator")


class DescribeFileSystemsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFileSystems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/efs.html#EFS.Paginator.DescribeFileSystems)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreationToken: str = None,
        FileSystemId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeFileSystemsResponseTypeDef, None, None]:
        """
        [DescribeFileSystems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/efs.html#EFS.Paginator.DescribeFileSystems.paginate)
        """


class DescribeMountTargetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMountTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/efs.html#EFS.Paginator.DescribeMountTargets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FileSystemId: str = None,
        MountTargetId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMountTargetsResponseTypeDef, None, None]:
        """
        [DescribeMountTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/efs.html#EFS.Paginator.DescribeMountTargets.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/efs.html#EFS.Paginator.DescribeTags)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, FileSystemId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeTagsResponseTypeDef, None, None]:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/efs.html#EFS.Paginator.DescribeTags.paginate)
        """
