"Main interface for rekognition service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_rekognition.type_defs import (
    DescribeProjectVersionsResponseTypeDef,
    DescribeProjectsResponseTypeDef,
    ListCollectionsResponseTypeDef,
    ListFacesResponseTypeDef,
    ListStreamProcessorsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeProjectVersionsPaginator",
    "DescribeProjectsPaginator",
    "ListCollectionsPaginator",
    "ListFacesPaginator",
    "ListStreamProcessorsPaginator",
)


class DescribeProjectVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeProjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeProjectVersionsResponseTypeDef, None, None]:
        """
        [DescribeProjectVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions.paginate)
        """


class DescribeProjectsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeProjectsResponseTypeDef, None, None]:
        """
        [DescribeProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects.paginate)
        """


class ListCollectionsPaginator(Boto3Paginator):
    """
    [Paginator.ListCollections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.ListCollections)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListCollectionsResponseTypeDef, None, None]:
        """
        [ListCollections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.ListCollections.paginate)
        """


class ListFacesPaginator(Boto3Paginator):
    """
    [Paginator.ListFaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.ListFaces)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CollectionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFacesResponseTypeDef, None, None]:
        """
        [ListFaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.ListFaces.paginate)
        """


class ListStreamProcessorsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreamProcessors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListStreamProcessorsResponseTypeDef, None, None]:
        """
        [ListStreamProcessors.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors.paginate)
        """
