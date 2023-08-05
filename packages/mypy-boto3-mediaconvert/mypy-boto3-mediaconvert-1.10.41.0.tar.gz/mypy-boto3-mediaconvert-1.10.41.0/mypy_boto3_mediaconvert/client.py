"Main interface for mediaconvert service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_mediaconvert.client as client_scope

# pylint: disable=import-self
import mypy_boto3_mediaconvert.paginator as paginator_scope
from mypy_boto3_mediaconvert.type_defs import (
    AccelerationSettingsTypeDef,
    CreateJobResponseTypeDef,
    CreateJobTemplateResponseTypeDef,
    CreatePresetResponseTypeDef,
    CreateQueueResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    GetJobResponseTypeDef,
    GetJobTemplateResponseTypeDef,
    GetPresetResponseTypeDef,
    GetQueueResponseTypeDef,
    JobSettingsTypeDef,
    JobTemplateSettingsTypeDef,
    ListJobTemplatesResponseTypeDef,
    ListJobsResponseTypeDef,
    ListPresetsResponseTypeDef,
    ListQueuesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PresetSettingsTypeDef,
    ReservationPlanSettingsTypeDef,
    UpdateJobTemplateResponseTypeDef,
    UpdatePresetResponseTypeDef,
    UpdateQueueResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaConvertClient",)


class MediaConvertClient(BaseClient):
    """
    [MediaConvert.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_certificate(self, Arn: str) -> Dict[str, Any]:
        """
        [Client.associate_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.associate_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_job(self, Id: str) -> Dict[str, Any]:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.cancel_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_job(
        self,
        Role: str,
        Settings: JobSettingsTypeDef,
        AccelerationSettings: AccelerationSettingsTypeDef = None,
        BillingTagsSource: Literal["QUEUE", "PRESET", "JOB_TEMPLATE", "JOB"] = None,
        ClientRequestToken: str = None,
        JobTemplate: str = None,
        Priority: int = None,
        Queue: str = None,
        SimulateReservedQueue: Literal["DISABLED", "ENABLED"] = None,
        StatusUpdateInterval: Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_15",
            "SECONDS_20",
            "SECONDS_30",
            "SECONDS_60",
            "SECONDS_120",
            "SECONDS_180",
            "SECONDS_240",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_600",
        ] = None,
        Tags: Dict[str, str] = None,
        UserMetadata: Dict[str, str] = None,
    ) -> CreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.create_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_job_template(
        self,
        Name: str,
        Settings: JobTemplateSettingsTypeDef,
        AccelerationSettings: AccelerationSettingsTypeDef = None,
        Category: str = None,
        Description: str = None,
        Priority: int = None,
        Queue: str = None,
        StatusUpdateInterval: Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_15",
            "SECONDS_20",
            "SECONDS_30",
            "SECONDS_60",
            "SECONDS_120",
            "SECONDS_180",
            "SECONDS_240",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_600",
        ] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateJobTemplateResponseTypeDef:
        """
        [Client.create_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.create_job_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_preset(
        self,
        Name: str,
        Settings: PresetSettingsTypeDef,
        Category: str = None,
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreatePresetResponseTypeDef:
        """
        [Client.create_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.create_preset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_queue(
        self,
        Name: str,
        Description: str = None,
        PricingPlan: Literal["ON_DEMAND", "RESERVED"] = None,
        ReservationPlanSettings: ReservationPlanSettingsTypeDef = None,
        Status: Literal["ACTIVE", "PAUSED"] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateQueueResponseTypeDef:
        """
        [Client.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.create_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_job_template(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.delete_job_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_preset(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.delete_preset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_queue(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.delete_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_endpoints(
        self,
        MaxResults: int = None,
        Mode: Literal["DEFAULT", "GET_ONLY"] = None,
        NextToken: str = None,
    ) -> DescribeEndpointsResponseTypeDef:
        """
        [Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.describe_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_certificate(self, Arn: str) -> Dict[str, Any]:
        """
        [Client.disassociate_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.disassociate_certificate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job(self, Id: str) -> GetJobResponseTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.get_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_template(self, Name: str) -> GetJobTemplateResponseTypeDef:
        """
        [Client.get_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.get_job_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_preset(self, Name: str) -> GetPresetResponseTypeDef:
        """
        [Client.get_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.get_preset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_queue(self, Name: str) -> GetQueueResponseTypeDef:
        """
        [Client.get_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.get_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_job_templates(
        self,
        Category: str = None,
        ListBy: Literal["NAME", "CREATION_DATE", "SYSTEM"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
    ) -> ListJobTemplatesResponseTypeDef:
        """
        [Client.list_job_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.list_job_templates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Queue: str = None,
        Status: Literal["SUBMITTED", "PROGRESSING", "COMPLETE", "CANCELED", "ERROR"] = None,
    ) -> ListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.list_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_presets(
        self,
        Category: str = None,
        ListBy: Literal["NAME", "CREATION_DATE", "SYSTEM"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
    ) -> ListPresetsResponseTypeDef:
        """
        [Client.list_presets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.list_presets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_queues(
        self,
        ListBy: Literal["NAME", "CREATION_DATE"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
    ) -> ListQueuesResponseTypeDef:
        """
        [Client.list_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.list_queues)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, Arn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, Arn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, Arn: str, TagKeys: List[str] = None) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_job_template(
        self,
        Name: str,
        AccelerationSettings: AccelerationSettingsTypeDef = None,
        Category: str = None,
        Description: str = None,
        Priority: int = None,
        Queue: str = None,
        Settings: JobTemplateSettingsTypeDef = None,
        StatusUpdateInterval: Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_15",
            "SECONDS_20",
            "SECONDS_30",
            "SECONDS_60",
            "SECONDS_120",
            "SECONDS_180",
            "SECONDS_240",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_600",
        ] = None,
    ) -> UpdateJobTemplateResponseTypeDef:
        """
        [Client.update_job_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.update_job_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_preset(
        self,
        Name: str,
        Category: str = None,
        Description: str = None,
        Settings: PresetSettingsTypeDef = None,
    ) -> UpdatePresetResponseTypeDef:
        """
        [Client.update_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.update_preset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_queue(
        self,
        Name: str,
        Description: str = None,
        ReservationPlanSettings: ReservationPlanSettingsTypeDef = None,
        Status: Literal["ACTIVE", "PAUSED"] = None,
    ) -> UpdateQueueResponseTypeDef:
        """
        [Client.update_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Client.update_queue)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_endpoints"]
    ) -> paginator_scope.DescribeEndpointsPaginator:
        """
        [Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Paginator.DescribeEndpoints)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_job_templates"]
    ) -> paginator_scope.ListJobTemplatesPaginator:
        """
        [Paginator.ListJobTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobTemplates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> paginator_scope.ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_presets"]
    ) -> paginator_scope.ListPresetsPaginator:
        """
        [Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Paginator.ListPresets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_queues"]
    ) -> paginator_scope.ListQueuesPaginator:
        """
        [Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mediaconvert.html#MediaConvert.Paginator.ListQueues)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
