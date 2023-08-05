"Main interface for kinesis-video-media service Client"
from __future__ import annotations

from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_kinesis_video_media.client as client_scope
from mypy_boto3_kinesis_video_media.type_defs import GetMediaOutputTypeDef, StartSelectorTypeDef


__all__ = ("KinesisVideoMediaClient",)


class KinesisVideoMediaClient(BaseClient):
    """
    [KinesisVideoMedia.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_media(
        self, StartSelector: StartSelectorTypeDef, StreamName: str = None, StreamARN: str = None
    ) -> GetMediaOutputTypeDef:
        """
        [Client.get_media documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.get_media)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ClientLimitExceededException: Boto3ClientError
    ConnectionLimitExceededException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidEndpointException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
