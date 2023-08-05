"Main interface for cloudhsmv2 service"
from mypy_boto3_cloudhsmv2.client import CloudHSMV2Client, CloudHSMV2Client as Client
from mypy_boto3_cloudhsmv2.paginator import (
    DescribeBackupsPaginator,
    DescribeClustersPaginator,
    ListTagsPaginator,
)


__all__ = (
    "Client",
    "CloudHSMV2Client",
    "DescribeBackupsPaginator",
    "DescribeClustersPaginator",
    "ListTagsPaginator",
)
