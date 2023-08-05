"Main interface for ecr service"
from mypy_boto3_ecr.client import ECRClient, ECRClient as Client
from mypy_boto3_ecr.paginator import (
    DescribeImageScanFindingsPaginator,
    DescribeImagesPaginator,
    DescribeRepositoriesPaginator,
    GetLifecyclePolicyPreviewPaginator,
    ListImagesPaginator,
)


__all__ = (
    "Client",
    "DescribeImageScanFindingsPaginator",
    "DescribeImagesPaginator",
    "DescribeRepositoriesPaginator",
    "ECRClient",
    "GetLifecyclePolicyPreviewPaginator",
    "ListImagesPaginator",
)
