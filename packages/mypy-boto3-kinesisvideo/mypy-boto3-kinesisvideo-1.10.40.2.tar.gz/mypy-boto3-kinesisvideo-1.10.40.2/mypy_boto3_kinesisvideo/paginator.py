"Main interface for kinesisvideo service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kinesisvideo.type_defs import (
    ChannelNameConditionTypeDef,
    ListSignalingChannelsOutputTypeDef,
    ListStreamsOutputTypeDef,
    PaginatorConfigTypeDef,
    StreamNameConditionTypeDef,
)


__all__ = ("ListSignalingChannelsPaginator", "ListStreamsPaginator")


class ListSignalingChannelsPaginator(Boto3Paginator):
    """
    [Paginator.ListSignalingChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ChannelNameCondition: ChannelNameConditionTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListSignalingChannelsOutputTypeDef, None, None]:
        """
        [ListSignalingChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels.paginate)
        """


class ListStreamsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StreamNameCondition: StreamNameConditionTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListStreamsOutputTypeDef, None, None]:
        """
        [ListStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams.paginate)
        """
