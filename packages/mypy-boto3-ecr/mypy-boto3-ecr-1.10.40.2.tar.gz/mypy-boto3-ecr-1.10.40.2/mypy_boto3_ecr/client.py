"Main interface for ecr service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, IO, List, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_ecr.client as client_scope

# pylint: disable=import-self
import mypy_boto3_ecr.paginator as paginator_scope
from mypy_boto3_ecr.type_defs import (
    BatchCheckLayerAvailabilityResponseTypeDef,
    BatchDeleteImageResponseTypeDef,
    BatchGetImageResponseTypeDef,
    CompleteLayerUploadResponseTypeDef,
    CreateRepositoryResponseTypeDef,
    DeleteLifecyclePolicyResponseTypeDef,
    DeleteRepositoryPolicyResponseTypeDef,
    DeleteRepositoryResponseTypeDef,
    DescribeImageScanFindingsResponseTypeDef,
    DescribeImagesFilterTypeDef,
    DescribeImagesResponseTypeDef,
    DescribeRepositoriesResponseTypeDef,
    GetAuthorizationTokenResponseTypeDef,
    GetDownloadUrlForLayerResponseTypeDef,
    GetLifecyclePolicyPreviewResponseTypeDef,
    GetLifecyclePolicyResponseTypeDef,
    GetRepositoryPolicyResponseTypeDef,
    ImageIdentifierTypeDef,
    ImageScanningConfigurationTypeDef,
    InitiateLayerUploadResponseTypeDef,
    LifecyclePolicyPreviewFilterTypeDef,
    ListImagesFilterTypeDef,
    ListImagesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutImageResponseTypeDef,
    PutImageScanningConfigurationResponseTypeDef,
    PutImageTagMutabilityResponseTypeDef,
    PutLifecyclePolicyResponseTypeDef,
    SetRepositoryPolicyResponseTypeDef,
    StartImageScanResponseTypeDef,
    StartLifecyclePolicyPreviewResponseTypeDef,
    TagTypeDef,
    UploadLayerPartResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ECRClient",)


class ECRClient(BaseClient):
    """
    [ECR.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_check_layer_availability(
        self, repositoryName: str, layerDigests: List[str], registryId: str = None
    ) -> BatchCheckLayerAvailabilityResponseTypeDef:
        """
        [Client.batch_check_layer_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.batch_check_layer_availability)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_image(
        self, repositoryName: str, imageIds: List[ImageIdentifierTypeDef], registryId: str = None
    ) -> BatchDeleteImageResponseTypeDef:
        """
        [Client.batch_delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.batch_delete_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_image(
        self,
        repositoryName: str,
        imageIds: List[ImageIdentifierTypeDef],
        registryId: str = None,
        acceptedMediaTypes: List[str] = None,
    ) -> BatchGetImageResponseTypeDef:
        """
        [Client.batch_get_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.batch_get_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def complete_layer_upload(
        self, repositoryName: str, uploadId: str, layerDigests: List[str], registryId: str = None
    ) -> CompleteLayerUploadResponseTypeDef:
        """
        [Client.complete_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.complete_layer_upload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_repository(
        self,
        repositoryName: str,
        tags: List[TagTypeDef] = None,
        imageTagMutability: Literal["MUTABLE", "IMMUTABLE"] = None,
        imageScanningConfiguration: ImageScanningConfigurationTypeDef = None,
    ) -> CreateRepositoryResponseTypeDef:
        """
        [Client.create_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.create_repository)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_lifecycle_policy(
        self, repositoryName: str, registryId: str = None
    ) -> DeleteLifecyclePolicyResponseTypeDef:
        """
        [Client.delete_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.delete_lifecycle_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_repository(
        self, repositoryName: str, registryId: str = None, force: bool = None
    ) -> DeleteRepositoryResponseTypeDef:
        """
        [Client.delete_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.delete_repository)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_repository_policy(
        self, repositoryName: str, registryId: str = None
    ) -> DeleteRepositoryPolicyResponseTypeDef:
        """
        [Client.delete_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.delete_repository_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_image_scan_findings(
        self,
        repositoryName: str,
        imageId: ImageIdentifierTypeDef,
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeImageScanFindingsResponseTypeDef:
        """
        [Client.describe_image_scan_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.describe_image_scan_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_images(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[ImageIdentifierTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: DescribeImagesFilterTypeDef = None,
    ) -> DescribeImagesResponseTypeDef:
        """
        [Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.describe_images)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_repositories(
        self,
        registryId: str = None,
        repositoryNames: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeRepositoriesResponseTypeDef:
        """
        [Client.describe_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.describe_repositories)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_authorization_token(
        self, registryIds: List[str] = None
    ) -> GetAuthorizationTokenResponseTypeDef:
        """
        [Client.get_authorization_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.get_authorization_token)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_download_url_for_layer(
        self, repositoryName: str, layerDigest: str, registryId: str = None
    ) -> GetDownloadUrlForLayerResponseTypeDef:
        """
        [Client.get_download_url_for_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.get_download_url_for_layer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_lifecycle_policy(
        self, repositoryName: str, registryId: str = None
    ) -> GetLifecyclePolicyResponseTypeDef:
        """
        [Client.get_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.get_lifecycle_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_lifecycle_policy_preview(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List[ImageIdentifierTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: LifecyclePolicyPreviewFilterTypeDef = None,
    ) -> GetLifecyclePolicyPreviewResponseTypeDef:
        """
        [Client.get_lifecycle_policy_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.get_lifecycle_policy_preview)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_repository_policy(
        self, repositoryName: str, registryId: str = None
    ) -> GetRepositoryPolicyResponseTypeDef:
        """
        [Client.get_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.get_repository_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_layer_upload(
        self, repositoryName: str, registryId: str = None
    ) -> InitiateLayerUploadResponseTypeDef:
        """
        [Client.initiate_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.initiate_layer_upload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_images(
        self,
        repositoryName: str,
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: ListImagesFilterTypeDef = None,
    ) -> ListImagesResponseTypeDef:
        """
        [Client.list_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.list_images)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_image(
        self, repositoryName: str, imageManifest: str, registryId: str = None, imageTag: str = None
    ) -> PutImageResponseTypeDef:
        """
        [Client.put_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.put_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_image_scanning_configuration(
        self,
        repositoryName: str,
        imageScanningConfiguration: ImageScanningConfigurationTypeDef,
        registryId: str = None,
    ) -> PutImageScanningConfigurationResponseTypeDef:
        """
        [Client.put_image_scanning_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.put_image_scanning_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_image_tag_mutability(
        self,
        repositoryName: str,
        imageTagMutability: Literal["MUTABLE", "IMMUTABLE"],
        registryId: str = None,
    ) -> PutImageTagMutabilityResponseTypeDef:
        """
        [Client.put_image_tag_mutability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.put_image_tag_mutability)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_lifecycle_policy(
        self, repositoryName: str, lifecyclePolicyText: str, registryId: str = None
    ) -> PutLifecyclePolicyResponseTypeDef:
        """
        [Client.put_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.put_lifecycle_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_repository_policy(
        self, repositoryName: str, policyText: str, registryId: str = None, force: bool = None
    ) -> SetRepositoryPolicyResponseTypeDef:
        """
        [Client.set_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.set_repository_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_image_scan(
        self, repositoryName: str, imageId: ImageIdentifierTypeDef, registryId: str = None
    ) -> StartImageScanResponseTypeDef:
        """
        [Client.start_image_scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.start_image_scan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_lifecycle_policy_preview(
        self, repositoryName: str, registryId: str = None, lifecyclePolicyText: str = None
    ) -> StartLifecyclePolicyPreviewResponseTypeDef:
        """
        [Client.start_lifecycle_policy_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.start_lifecycle_policy_preview)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_layer_part(
        self,
        repositoryName: str,
        uploadId: str,
        partFirstByte: int,
        partLastByte: int,
        layerPartBlob: Union[bytes, IO],
        registryId: str = None,
    ) -> UploadLayerPartResponseTypeDef:
        """
        [Client.upload_layer_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Client.upload_layer_part)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_image_scan_findings"]
    ) -> paginator_scope.DescribeImageScanFindingsPaginator:
        """
        [Paginator.DescribeImageScanFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_images"]
    ) -> paginator_scope.DescribeImagesPaginator:
        """
        [Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Paginator.DescribeImages)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_repositories"]
    ) -> paginator_scope.DescribeRepositoriesPaginator:
        """
        [Paginator.DescribeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Paginator.DescribeRepositories)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_lifecycle_policy_preview"]
    ) -> paginator_scope.GetLifecyclePolicyPreviewPaginator:
        """
        [Paginator.GetLifecyclePolicyPreview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_images"]
    ) -> paginator_scope.ListImagesPaginator:
        """
        [Paginator.ListImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ecr.html#ECR.Paginator.ListImages)
        """


class Exceptions:
    ClientError: Boto3ClientError
    EmptyUploadException: Boto3ClientError
    ImageAlreadyExistsException: Boto3ClientError
    ImageNotFoundException: Boto3ClientError
    ImageTagAlreadyExistsException: Boto3ClientError
    InvalidLayerException: Boto3ClientError
    InvalidLayerPartException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidTagParameterException: Boto3ClientError
    LayerAlreadyExistsException: Boto3ClientError
    LayerInaccessibleException: Boto3ClientError
    LayerPartTooSmallException: Boto3ClientError
    LayersNotFoundException: Boto3ClientError
    LifecyclePolicyNotFoundException: Boto3ClientError
    LifecyclePolicyPreviewInProgressException: Boto3ClientError
    LifecyclePolicyPreviewNotFoundException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    RepositoryAlreadyExistsException: Boto3ClientError
    RepositoryNotEmptyException: Boto3ClientError
    RepositoryNotFoundException: Boto3ClientError
    RepositoryPolicyNotFoundException: Boto3ClientError
    ScanNotFoundException: Boto3ClientError
    ServerException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    UploadNotFoundException: Boto3ClientError
