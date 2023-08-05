"Main interface for cloudhsmv2 service Paginators"
from __future__ import annotations

from typing import Dict, Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudhsmv2.type_defs import (
    DescribeBackupsResponseTypeDef,
    DescribeClustersResponseTypeDef,
    ListTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("DescribeBackupsPaginator", "DescribeClustersPaginator", "ListTagsPaginator")


class DescribeBackupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeBackups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: Dict[str, List[str]] = None,
        SortAscending: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeBackupsResponseTypeDef, None, None]:
        """
        [DescribeBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeBackups.paginate)
        """


class DescribeClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeClusters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: Dict[str, List[str]] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeClustersResponseTypeDef, None, None]:
        """
        [DescribeClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeClusters.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.ListTags)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsResponseTypeDef, None, None]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.ListTags.paginate)
        """
