"Main interface for rekognition service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_rekognition.type_defs import WaiterConfigTypeDef


__all__ = ("ProjectVersionRunningWaiter", "ProjectVersionTrainingCompletedWaiter")


class ProjectVersionRunningWaiter(Boto3Waiter):
    """
    [Waiter.ProjectVersionRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ProjectVersionRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning.wait)
        """


class ProjectVersionTrainingCompletedWaiter(Boto3Waiter):
    """
    [Waiter.ProjectVersionTrainingCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ProjectVersionTrainingCompleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted.wait)
        """
