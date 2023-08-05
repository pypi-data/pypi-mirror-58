"Main interface for kinesis-video-archived-media service"
from mypy_boto3_kinesis_video_archived_media.client import (
    KinesisVideoArchivedMediaClient,
    KinesisVideoArchivedMediaClient as Client,
)
from mypy_boto3_kinesis_video_archived_media.paginator import ListFragmentsPaginator


__all__ = ("Client", "KinesisVideoArchivedMediaClient", "ListFragmentsPaginator")
