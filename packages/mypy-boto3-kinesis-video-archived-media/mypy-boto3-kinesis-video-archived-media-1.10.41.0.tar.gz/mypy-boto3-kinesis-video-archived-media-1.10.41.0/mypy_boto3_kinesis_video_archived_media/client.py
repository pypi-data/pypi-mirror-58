"Main interface for kinesis-video-archived-media service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_kinesis_video_archived_media.client as client_scope

# pylint: disable=import-self
import mypy_boto3_kinesis_video_archived_media.paginator as paginator_scope
from mypy_boto3_kinesis_video_archived_media.type_defs import (
    DASHFragmentSelectorTypeDef,
    FragmentSelectorTypeDef,
    GetDASHStreamingSessionURLOutputTypeDef,
    GetHLSStreamingSessionURLOutputTypeDef,
    GetMediaForFragmentListOutputTypeDef,
    HLSFragmentSelectorTypeDef,
    ListFragmentsOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KinesisVideoArchivedMediaClient",)


class KinesisVideoArchivedMediaClient(BaseClient):
    """
    [KinesisVideoArchivedMedia.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dash_streaming_session_url(
        self,
        StreamName: str = None,
        StreamARN: str = None,
        PlaybackMode: Literal["LIVE", "LIVE_REPLAY", "ON_DEMAND"] = None,
        DisplayFragmentTimestamp: Literal["ALWAYS", "NEVER"] = None,
        DisplayFragmentNumber: Literal["ALWAYS", "NEVER"] = None,
        DASHFragmentSelector: DASHFragmentSelectorTypeDef = None,
        Expires: int = None,
        MaxManifestFragmentResults: int = None,
    ) -> GetDASHStreamingSessionURLOutputTypeDef:
        """
        [Client.get_dash_streaming_session_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_dash_streaming_session_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_hls_streaming_session_url(
        self,
        StreamName: str = None,
        StreamARN: str = None,
        PlaybackMode: Literal["LIVE", "LIVE_REPLAY", "ON_DEMAND"] = None,
        HLSFragmentSelector: HLSFragmentSelectorTypeDef = None,
        ContainerFormat: Literal["FRAGMENTED_MP4", "MPEG_TS"] = None,
        DiscontinuityMode: Literal["ALWAYS", "NEVER", "ON_DISCONTINUITY"] = None,
        DisplayFragmentTimestamp: Literal["ALWAYS", "NEVER"] = None,
        Expires: int = None,
        MaxMediaPlaylistFragmentResults: int = None,
    ) -> GetHLSStreamingSessionURLOutputTypeDef:
        """
        [Client.get_hls_streaming_session_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_hls_streaming_session_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_media_for_fragment_list(
        self, StreamName: str, Fragments: List[str]
    ) -> GetMediaForFragmentListOutputTypeDef:
        """
        [Client.get_media_for_fragment_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_media_for_fragment_list)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_fragments(
        self,
        StreamName: str,
        MaxResults: int = None,
        NextToken: str = None,
        FragmentSelector: FragmentSelectorTypeDef = None,
    ) -> ListFragmentsOutputTypeDef:
        """
        [Client.list_fragments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.list_fragments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_fragments"]
    ) -> paginator_scope.ListFragmentsPaginator:
        """
        [Paginator.ListFragments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ClientLimitExceededException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidCodecPrivateDataException: Boto3ClientError
    MissingCodecPrivateDataException: Boto3ClientError
    NoDataRetentionException: Boto3ClientError
    NotAuthorizedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    UnsupportedStreamMediaTypeException: Boto3ClientError
