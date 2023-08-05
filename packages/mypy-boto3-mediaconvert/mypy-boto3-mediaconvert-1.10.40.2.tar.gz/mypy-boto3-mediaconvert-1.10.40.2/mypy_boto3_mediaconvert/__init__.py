"Main interface for mediaconvert service"
from mypy_boto3_mediaconvert.client import MediaConvertClient, MediaConvertClient as Client
from mypy_boto3_mediaconvert.paginator import (
    DescribeEndpointsPaginator,
    ListJobTemplatesPaginator,
    ListJobsPaginator,
    ListPresetsPaginator,
    ListQueuesPaginator,
)


__all__ = (
    "Client",
    "DescribeEndpointsPaginator",
    "ListJobTemplatesPaginator",
    "ListJobsPaginator",
    "ListPresetsPaginator",
    "ListQueuesPaginator",
    "MediaConvertClient",
)
