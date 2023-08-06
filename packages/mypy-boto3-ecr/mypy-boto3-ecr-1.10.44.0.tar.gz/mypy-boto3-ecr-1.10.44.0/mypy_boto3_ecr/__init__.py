"""
Main interface for ecr service.

Usage::

    import boto3
    from mypy_boto3.ecr import (
        Client,
        DescribeImageScanFindingsPaginator,
        DescribeImagesPaginator,
        DescribeRepositoriesPaginator,
        ECRClient,
        GetLifecyclePolicyPreviewPaginator,
        ListImagesPaginator,
        )

    session = boto3.Session()

    client: ECRClient = boto3.client("ecr")
    session_client: ECRClient = session.client("ecr")

    describe_image_scan_findings_paginator: DescribeImageScanFindingsPaginator = client.get_paginator("describe_image_scan_findings")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_repositories_paginator: DescribeRepositoriesPaginator = client.get_paginator("describe_repositories")
    get_lifecycle_policy_preview_paginator: GetLifecyclePolicyPreviewPaginator = client.get_paginator("get_lifecycle_policy_preview")
    list_images_paginator: ListImagesPaginator = client.get_paginator("list_images")
"""
from mypy_boto3_ecr.client import ECRClient as Client, ECRClient
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
