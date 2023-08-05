"Main interface for kinesis-video-signaling service Client"
from __future__ import annotations

import sys
from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_kinesis_video_signaling.client as client_scope
from mypy_boto3_kinesis_video_signaling.type_defs import (
    GetIceServerConfigResponseTypeDef,
    SendAlexaOfferToMasterResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KinesisVideoSignalingChannelsClient",)


class KinesisVideoSignalingChannelsClient(BaseClient):
    """
    [KinesisVideoSignalingChannels.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ice_server_config(
        self,
        ChannelARN: str,
        ClientId: str = None,
        Service: Literal["TURN"] = None,
        Username: str = None,
    ) -> GetIceServerConfigResponseTypeDef:
        """
        [Client.get_ice_server_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.get_ice_server_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_alexa_offer_to_master(
        self, ChannelARN: str, SenderClientId: str, MessagePayload: str
    ) -> SendAlexaOfferToMasterResponseTypeDef:
        """
        [Client.send_alexa_offer_to_master documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.send_alexa_offer_to_master)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ClientLimitExceededException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidClientException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    SessionExpiredException: Boto3ClientError
