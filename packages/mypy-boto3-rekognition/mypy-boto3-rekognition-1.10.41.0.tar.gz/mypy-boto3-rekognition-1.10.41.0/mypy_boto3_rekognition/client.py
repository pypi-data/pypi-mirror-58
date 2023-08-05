"Main interface for rekognition service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_rekognition.client as client_scope

# pylint: disable=import-self
import mypy_boto3_rekognition.paginator as paginator_scope
from mypy_boto3_rekognition.type_defs import (
    CompareFacesResponseTypeDef,
    CreateCollectionResponseTypeDef,
    CreateProjectResponseTypeDef,
    CreateProjectVersionResponseTypeDef,
    CreateStreamProcessorResponseTypeDef,
    DeleteCollectionResponseTypeDef,
    DeleteFacesResponseTypeDef,
    DescribeCollectionResponseTypeDef,
    DescribeProjectVersionsResponseTypeDef,
    DescribeProjectsResponseTypeDef,
    DescribeStreamProcessorResponseTypeDef,
    DetectCustomLabelsResponseTypeDef,
    DetectFacesResponseTypeDef,
    DetectLabelsResponseTypeDef,
    DetectModerationLabelsResponseTypeDef,
    DetectTextResponseTypeDef,
    GetCelebrityInfoResponseTypeDef,
    GetCelebrityRecognitionResponseTypeDef,
    GetContentModerationResponseTypeDef,
    GetFaceDetectionResponseTypeDef,
    GetFaceSearchResponseTypeDef,
    GetLabelDetectionResponseTypeDef,
    GetPersonTrackingResponseTypeDef,
    HumanLoopConfigTypeDef,
    ImageTypeDef,
    IndexFacesResponseTypeDef,
    ListCollectionsResponseTypeDef,
    ListFacesResponseTypeDef,
    ListStreamProcessorsResponseTypeDef,
    NotificationChannelTypeDef,
    OutputConfigTypeDef,
    RecognizeCelebritiesResponseTypeDef,
    SearchFacesByImageResponseTypeDef,
    SearchFacesResponseTypeDef,
    StartCelebrityRecognitionResponseTypeDef,
    StartContentModerationResponseTypeDef,
    StartFaceDetectionResponseTypeDef,
    StartFaceSearchResponseTypeDef,
    StartLabelDetectionResponseTypeDef,
    StartPersonTrackingResponseTypeDef,
    StartProjectVersionResponseTypeDef,
    StopProjectVersionResponseTypeDef,
    StreamProcessorInputTypeDef,
    StreamProcessorOutputTypeDef,
    StreamProcessorSettingsTypeDef,
    TestingDataTypeDef,
    TrainingDataTypeDef,
    VideoTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_rekognition.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RekognitionClient",)


class RekognitionClient(BaseClient):
    """
    [Rekognition.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def compare_faces(
        self,
        SourceImage: ImageTypeDef,
        TargetImage: ImageTypeDef,
        SimilarityThreshold: float = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> CompareFacesResponseTypeDef:
        """
        [Client.compare_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.compare_faces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_collection(self, CollectionId: str) -> CreateCollectionResponseTypeDef:
        """
        [Client.create_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.create_collection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_project(self, ProjectName: str) -> CreateProjectResponseTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.create_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_project_version(
        self,
        ProjectArn: str,
        VersionName: str,
        OutputConfig: OutputConfigTypeDef,
        TrainingData: TrainingDataTypeDef,
        TestingData: TestingDataTypeDef,
    ) -> CreateProjectVersionResponseTypeDef:
        """
        [Client.create_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.create_project_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stream_processor(
        self,
        Input: StreamProcessorInputTypeDef,
        Output: StreamProcessorOutputTypeDef,
        Name: str,
        Settings: StreamProcessorSettingsTypeDef,
        RoleArn: str,
    ) -> CreateStreamProcessorResponseTypeDef:
        """
        [Client.create_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.create_stream_processor)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_collection(self, CollectionId: str) -> DeleteCollectionResponseTypeDef:
        """
        [Client.delete_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.delete_collection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_faces(self, CollectionId: str, FaceIds: List[str]) -> DeleteFacesResponseTypeDef:
        """
        [Client.delete_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.delete_faces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.delete_stream_processor)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_collection(self, CollectionId: str) -> DescribeCollectionResponseTypeDef:
        """
        [Client.describe_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.describe_collection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_project_versions(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeProjectVersionsResponseTypeDef:
        """
        [Client.describe_project_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.describe_project_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_projects(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeProjectsResponseTypeDef:
        """
        [Client.describe_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.describe_projects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stream_processor(self, Name: str) -> DescribeStreamProcessorResponseTypeDef:
        """
        [Client.describe_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.describe_stream_processor)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_custom_labels(
        self,
        ProjectVersionArn: str,
        Image: ImageTypeDef,
        MaxResults: int = None,
        MinConfidence: float = None,
    ) -> DetectCustomLabelsResponseTypeDef:
        """
        [Client.detect_custom_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.detect_custom_labels)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_faces(
        self, Image: ImageTypeDef, Attributes: List[Literal["DEFAULT", "ALL"]] = None
    ) -> DetectFacesResponseTypeDef:
        """
        [Client.detect_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.detect_faces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_labels(
        self, Image: ImageTypeDef, MaxLabels: int = None, MinConfidence: float = None
    ) -> DetectLabelsResponseTypeDef:
        """
        [Client.detect_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.detect_labels)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_moderation_labels(
        self,
        Image: ImageTypeDef,
        MinConfidence: float = None,
        HumanLoopConfig: HumanLoopConfigTypeDef = None,
    ) -> DetectModerationLabelsResponseTypeDef:
        """
        [Client.detect_moderation_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.detect_moderation_labels)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_text(self, Image: ImageTypeDef) -> DetectTextResponseTypeDef:
        """
        [Client.detect_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.detect_text)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_celebrity_info(self, Id: str) -> GetCelebrityInfoResponseTypeDef:
        """
        [Client.get_celebrity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.get_celebrity_info)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_celebrity_recognition(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["ID", "TIMESTAMP"] = None,
    ) -> GetCelebrityRecognitionResponseTypeDef:
        """
        [Client.get_celebrity_recognition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.get_celebrity_recognition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_content_moderation(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["NAME", "TIMESTAMP"] = None,
    ) -> GetContentModerationResponseTypeDef:
        """
        [Client.get_content_moderation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.get_content_moderation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_face_detection(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetFaceDetectionResponseTypeDef:
        """
        [Client.get_face_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.get_face_detection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_face_search(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["INDEX", "TIMESTAMP"] = None,
    ) -> GetFaceSearchResponseTypeDef:
        """
        [Client.get_face_search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.get_face_search)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_label_detection(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["NAME", "TIMESTAMP"] = None,
    ) -> GetLabelDetectionResponseTypeDef:
        """
        [Client.get_label_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.get_label_detection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_person_tracking(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["INDEX", "TIMESTAMP"] = None,
    ) -> GetPersonTrackingResponseTypeDef:
        """
        [Client.get_person_tracking documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.get_person_tracking)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def index_faces(
        self,
        CollectionId: str,
        Image: ImageTypeDef,
        ExternalImageId: str = None,
        DetectionAttributes: List[Literal["DEFAULT", "ALL"]] = None,
        MaxFaces: int = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> IndexFacesResponseTypeDef:
        """
        [Client.index_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.index_faces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_collections(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListCollectionsResponseTypeDef:
        """
        [Client.list_collections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.list_collections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_faces(
        self, CollectionId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFacesResponseTypeDef:
        """
        [Client.list_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.list_faces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_stream_processors(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListStreamProcessorsResponseTypeDef:
        """
        [Client.list_stream_processors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.list_stream_processors)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def recognize_celebrities(self, Image: ImageTypeDef) -> RecognizeCelebritiesResponseTypeDef:
        """
        [Client.recognize_celebrities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.recognize_celebrities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_faces(
        self, CollectionId: str, FaceId: str, MaxFaces: int = None, FaceMatchThreshold: float = None
    ) -> SearchFacesResponseTypeDef:
        """
        [Client.search_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.search_faces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_faces_by_image(
        self,
        CollectionId: str,
        Image: ImageTypeDef,
        MaxFaces: int = None,
        FaceMatchThreshold: float = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> SearchFacesByImageResponseTypeDef:
        """
        [Client.search_faces_by_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.search_faces_by_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_celebrity_recognition(
        self,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> StartCelebrityRecognitionResponseTypeDef:
        """
        [Client.start_celebrity_recognition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.start_celebrity_recognition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_content_moderation(
        self,
        Video: VideoTypeDef,
        MinConfidence: float = None,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> StartContentModerationResponseTypeDef:
        """
        [Client.start_content_moderation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.start_content_moderation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_face_detection(
        self,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        FaceAttributes: Literal["DEFAULT", "ALL"] = None,
        JobTag: str = None,
    ) -> StartFaceDetectionResponseTypeDef:
        """
        [Client.start_face_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.start_face_detection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_face_search(
        self,
        Video: VideoTypeDef,
        CollectionId: str,
        ClientRequestToken: str = None,
        FaceMatchThreshold: float = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> StartFaceSearchResponseTypeDef:
        """
        [Client.start_face_search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.start_face_search)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_label_detection(
        self,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        MinConfidence: float = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> StartLabelDetectionResponseTypeDef:
        """
        [Client.start_label_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.start_label_detection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_person_tracking(
        self,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> StartPersonTrackingResponseTypeDef:
        """
        [Client.start_person_tracking documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.start_person_tracking)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_project_version(
        self, ProjectVersionArn: str, MinInferenceUnits: int
    ) -> StartProjectVersionResponseTypeDef:
        """
        [Client.start_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.start_project_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.start_stream_processor)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_project_version(self, ProjectVersionArn: str) -> StopProjectVersionResponseTypeDef:
        """
        [Client.stop_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.stop_project_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Client.stop_stream_processor)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_project_versions"]
    ) -> paginator_scope.DescribeProjectVersionsPaginator:
        """
        [Paginator.DescribeProjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_projects"]
    ) -> paginator_scope.DescribeProjectsPaginator:
        """
        [Paginator.DescribeProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_collections"]
    ) -> paginator_scope.ListCollectionsPaginator:
        """
        [Paginator.ListCollections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.ListCollections)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_faces"]
    ) -> paginator_scope.ListFacesPaginator:
        """
        [Paginator.ListFaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.ListFaces)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_stream_processors"]
    ) -> paginator_scope.ListStreamProcessorsPaginator:
        """
        [Paginator.ListStreamProcessors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["project_version_running"]
    ) -> waiter_scope.ProjectVersionRunningWaiter:
        """
        [Waiter.ProjectVersionRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["project_version_training_completed"]
    ) -> waiter_scope.ProjectVersionTrainingCompletedWaiter:
        """
        [Waiter.ProjectVersionTrainingCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    HumanLoopQuotaExceededException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    ImageTooLargeException: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidImageFormatException: Boto3ClientError
    InvalidPaginationTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidS3ObjectException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ProvisionedThroughputExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceNotReadyException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    VideoTooLargeException: Boto3ClientError
