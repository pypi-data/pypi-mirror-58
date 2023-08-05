"Main interface for rekognition service"
from mypy_boto3_rekognition.client import RekognitionClient, RekognitionClient as Client
from mypy_boto3_rekognition.paginator import (
    DescribeProjectVersionsPaginator,
    DescribeProjectsPaginator,
    ListCollectionsPaginator,
    ListFacesPaginator,
    ListStreamProcessorsPaginator,
)
from mypy_boto3_rekognition.waiter import (
    ProjectVersionRunningWaiter,
    ProjectVersionTrainingCompletedWaiter,
)


__all__ = (
    "Client",
    "DescribeProjectVersionsPaginator",
    "DescribeProjectsPaginator",
    "ListCollectionsPaginator",
    "ListFacesPaginator",
    "ListStreamProcessorsPaginator",
    "ProjectVersionRunningWaiter",
    "ProjectVersionTrainingCompletedWaiter",
    "RekognitionClient",
)
