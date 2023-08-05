"Main interface for ecr service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ecr.type_defs import (
    DescribeImageScanFindingsResponseTypeDef,
    DescribeImagesFilterTypeDef,
    DescribeImagesResponseTypeDef,
    DescribeRepositoriesResponseTypeDef,
    GetLifecyclePolicyPreviewResponseTypeDef,
    ImageIdentifierTypeDef,
    LifecyclePolicyPreviewFilterTypeDef,
    ListImagesFilterTypeDef,
    ListImagesResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeImageScanFindingsPaginator",
    "DescribeImagesPaginator",
    "DescribeRepositoriesPaginator",
    "GetLifecyclePolicyPreviewPaginator",
    "ListImagesPaginator",
)


class DescribeImageScanFindingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImageScanFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        imageId: ImageIdentifierTypeDef,
        registryId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeImageScanFindingsResponseTypeDef, None, None]:
        """
        [DescribeImageScanFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings.paginate)
        """


class DescribeImagesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecr.html#ECR.Paginator.DescribeImages)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[ImageIdentifierTypeDef] = None,
        filter: DescribeImagesFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeImagesResponseTypeDef, None, None]:
        """
        [DescribeImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecr.html#ECR.Paginator.DescribeImages.paginate)
        """


class DescribeRepositoriesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecr.html#ECR.Paginator.DescribeRepositories)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        registryId: str = None,
        repositoryNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeRepositoriesResponseTypeDef, None, None]:
        """
        [DescribeRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecr.html#ECR.Paginator.DescribeRepositories.paginate)
        """


class GetLifecyclePolicyPreviewPaginator(Boto3Paginator):
    """
    [Paginator.GetLifecyclePolicyPreview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[ImageIdentifierTypeDef] = None,
        filter: LifecyclePolicyPreviewFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetLifecyclePolicyPreviewResponseTypeDef, None, None]:
        """
        [GetLifecyclePolicyPreview.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview.paginate)
        """


class ListImagesPaginator(Boto3Paginator):
    """
    [Paginator.ListImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecr.html#ECR.Paginator.ListImages)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        registryId: str = None,
        filter: ListImagesFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListImagesResponseTypeDef, None, None]:
        """
        [ListImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/ecr.html#ECR.Paginator.ListImages.paginate)
        """
