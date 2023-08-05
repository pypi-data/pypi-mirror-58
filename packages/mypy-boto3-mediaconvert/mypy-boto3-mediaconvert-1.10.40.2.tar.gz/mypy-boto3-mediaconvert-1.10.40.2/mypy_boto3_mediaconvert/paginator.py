"Main interface for mediaconvert service Paginators"
from __future__ import annotations

import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediaconvert.type_defs import (
    DescribeEndpointsResponseTypeDef,
    ListJobTemplatesResponseTypeDef,
    ListJobsResponseTypeDef,
    ListPresetsResponseTypeDef,
    ListQueuesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeEndpointsPaginator",
    "ListJobTemplatesPaginator",
    "ListJobsPaginator",
    "ListPresetsPaginator",
    "ListQueuesPaginator",
)


class DescribeEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/mediaconvert.html#MediaConvert.Paginator.DescribeEndpoints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Mode: Literal["DEFAULT", "GET_ONLY"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEndpointsResponseTypeDef, None, None]:
        """
        [DescribeEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/mediaconvert.html#MediaConvert.Paginator.DescribeEndpoints.paginate)
        """


class ListJobTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.ListJobTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobTemplates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Category: str = None,
        ListBy: Literal["NAME", "CREATION_DATE", "SYSTEM"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListJobTemplatesResponseTypeDef, None, None]:
        """
        [ListJobTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobTemplates.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Queue: str = None,
        Status: Literal["SUBMITTED", "PROGRESSING", "COMPLETE", "CANCELED", "ERROR"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListJobsResponseTypeDef, None, None]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobs.paginate)
        """


class ListPresetsPaginator(Boto3Paginator):
    """
    [Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/mediaconvert.html#MediaConvert.Paginator.ListPresets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Category: str = None,
        ListBy: Literal["NAME", "CREATION_DATE", "SYSTEM"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPresetsResponseTypeDef, None, None]:
        """
        [ListPresets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/mediaconvert.html#MediaConvert.Paginator.ListPresets.paginate)
        """


class ListQueuesPaginator(Boto3Paginator):
    """
    [Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/mediaconvert.html#MediaConvert.Paginator.ListQueues)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ListBy: Literal["NAME", "CREATION_DATE"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListQueuesResponseTypeDef, None, None]:
        """
        [ListQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/mediaconvert.html#MediaConvert.Paginator.ListQueues.paginate)
        """
