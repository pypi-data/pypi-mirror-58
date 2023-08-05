"Main interface for kinesis-video-archived-media service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kinesis_video_archived_media.type_defs import (
    FragmentSelectorTypeDef,
    ListFragmentsOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListFragmentsPaginator",)


class ListFragmentsPaginator(Boto3Paginator):
    """
    [Paginator.ListFragments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StreamName: str,
        FragmentSelector: FragmentSelectorTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListFragmentsOutputTypeDef, None, None]:
        """
        [ListFragments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments.paginate)
        """
