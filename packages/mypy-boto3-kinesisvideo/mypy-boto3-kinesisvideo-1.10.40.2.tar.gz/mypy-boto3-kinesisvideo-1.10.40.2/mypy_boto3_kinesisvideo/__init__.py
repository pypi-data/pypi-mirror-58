"Main interface for kinesisvideo service"
from mypy_boto3_kinesisvideo.client import KinesisVideoClient as Client, KinesisVideoClient
from mypy_boto3_kinesisvideo.paginator import ListSignalingChannelsPaginator, ListStreamsPaginator


__all__ = ("Client", "KinesisVideoClient", "ListSignalingChannelsPaginator", "ListStreamsPaginator")
