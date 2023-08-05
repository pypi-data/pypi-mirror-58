"Main interface for kinesisvideo service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_kinesisvideo.client as client_scope

# pylint: disable=import-self
import mypy_boto3_kinesisvideo.paginator as paginator_scope
from mypy_boto3_kinesisvideo.type_defs import (
    ChannelNameConditionTypeDef,
    CreateSignalingChannelOutputTypeDef,
    CreateStreamOutputTypeDef,
    DescribeSignalingChannelOutputTypeDef,
    DescribeStreamOutputTypeDef,
    GetDataEndpointOutputTypeDef,
    GetSignalingChannelEndpointOutputTypeDef,
    ListSignalingChannelsOutputTypeDef,
    ListStreamsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTagsForStreamOutputTypeDef,
    SingleMasterChannelEndpointConfigurationTypeDef,
    SingleMasterConfigurationTypeDef,
    StreamNameConditionTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KinesisVideoClient",)


class KinesisVideoClient(BaseClient):
    """
    [KinesisVideo.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_signaling_channel(
        self,
        ChannelName: str,
        ChannelType: Literal["SINGLE_MASTER"] = None,
        SingleMasterConfiguration: SingleMasterConfigurationTypeDef = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateSignalingChannelOutputTypeDef:
        """
        [Client.create_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.create_signaling_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stream(
        self,
        StreamName: str,
        DeviceName: str = None,
        MediaType: str = None,
        KmsKeyId: str = None,
        DataRetentionInHours: int = None,
        Tags: Dict[str, str] = None,
    ) -> CreateStreamOutputTypeDef:
        """
        [Client.create_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.create_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_signaling_channel(
        self, ChannelARN: str, CurrentVersion: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_signaling_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_stream(self, StreamARN: str, CurrentVersion: str = None) -> Dict[str, Any]:
        """
        [Client.delete_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_signaling_channel(
        self, ChannelName: str = None, ChannelARN: str = None
    ) -> DescribeSignalingChannelOutputTypeDef:
        """
        [Client.describe_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_signaling_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stream(
        self, StreamName: str = None, StreamARN: str = None
    ) -> DescribeStreamOutputTypeDef:
        """
        [Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_stream)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_data_endpoint(
        self,
        APIName: Literal[
            "PUT_MEDIA",
            "GET_MEDIA",
            "LIST_FRAGMENTS",
            "GET_MEDIA_FOR_FRAGMENT_LIST",
            "GET_HLS_STREAMING_SESSION_URL",
            "GET_DASH_STREAMING_SESSION_URL",
        ],
        StreamName: str = None,
        StreamARN: str = None,
    ) -> GetDataEndpointOutputTypeDef:
        """
        [Client.get_data_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.get_data_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_signaling_channel_endpoint(
        self,
        ChannelARN: str,
        SingleMasterChannelEndpointConfiguration: SingleMasterChannelEndpointConfigurationTypeDef = None,
    ) -> GetSignalingChannelEndpointOutputTypeDef:
        """
        [Client.get_signaling_channel_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.get_signaling_channel_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_signaling_channels(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        ChannelNameCondition: ChannelNameConditionTypeDef = None,
    ) -> ListSignalingChannelsOutputTypeDef:
        """
        [Client.list_signaling_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.list_signaling_channels)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_streams(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        StreamNameCondition: StreamNameConditionTypeDef = None,
    ) -> ListStreamsOutputTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.list_streams)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceARN: str, NextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_stream(
        self, NextToken: str = None, StreamARN: str = None, StreamName: str = None
    ) -> ListTagsForStreamOutputTypeDef:
        """
        [Client.list_tags_for_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceARN: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_stream(
        self, Tags: Dict[str, str], StreamARN: str = None, StreamName: str = None
    ) -> Dict[str, Any]:
        """
        [Client.tag_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceARN: str, TagKeyList: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_stream(
        self, TagKeyList: List[str], StreamARN: str = None, StreamName: str = None
    ) -> Dict[str, Any]:
        """
        [Client.untag_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_stream)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_data_retention(
        self,
        CurrentVersion: str,
        Operation: Literal["INCREASE_DATA_RETENTION", "DECREASE_DATA_RETENTION"],
        DataRetentionChangeInHours: int,
        StreamName: str = None,
        StreamARN: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_data_retention documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.update_data_retention)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_signaling_channel(
        self,
        ChannelARN: str,
        CurrentVersion: str,
        SingleMasterConfiguration: SingleMasterConfigurationTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.update_signaling_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_stream(
        self,
        CurrentVersion: str,
        StreamName: str = None,
        StreamARN: str = None,
        DeviceName: str = None,
        MediaType: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Client.update_stream)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_signaling_channels"]
    ) -> paginator_scope.ListSignalingChannelsPaginator:
        """
        [Paginator.ListSignalingChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_streams"]
    ) -> paginator_scope.ListStreamsPaginator:
        """
        [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AccountChannelLimitExceededException: Boto3ClientError
    AccountStreamLimitExceededException: Boto3ClientError
    ClientError: Boto3ClientError
    ClientLimitExceededException: Boto3ClientError
    DeviceStreamLimitExceededException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidDeviceException: Boto3ClientError
    InvalidResourceFormatException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TagsPerResourceExceededLimitException: Boto3ClientError
    VersionMismatchException: Boto3ClientError
