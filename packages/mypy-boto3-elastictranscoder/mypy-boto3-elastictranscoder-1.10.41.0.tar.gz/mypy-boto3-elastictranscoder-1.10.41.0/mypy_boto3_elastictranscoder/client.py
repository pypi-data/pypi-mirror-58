"Main interface for elastictranscoder service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_elastictranscoder.client as client_scope

# pylint: disable=import-self
import mypy_boto3_elastictranscoder.paginator as paginator_scope
from mypy_boto3_elastictranscoder.type_defs import (
    AudioParametersTypeDef,
    CreateJobOutputTypeDef,
    CreateJobPlaylistTypeDef,
    CreateJobResponseTypeDef,
    CreatePipelineResponseTypeDef,
    CreatePresetResponseTypeDef,
    JobInputTypeDef,
    ListJobsByPipelineResponseTypeDef,
    ListJobsByStatusResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListPresetsResponseTypeDef,
    NotificationsTypeDef,
    PipelineOutputConfigTypeDef,
    ReadJobResponseTypeDef,
    ReadPipelineResponseTypeDef,
    ReadPresetResponseTypeDef,
    TestRoleResponseTypeDef,
    ThumbnailsTypeDef,
    UpdatePipelineNotificationsResponseTypeDef,
    UpdatePipelineResponseTypeDef,
    UpdatePipelineStatusResponseTypeDef,
    VideoParametersTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_elastictranscoder.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticTranscoderClient",)


class ElasticTranscoderClient(BaseClient):
    """
    [ElasticTranscoder.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_job(self, Id: str) -> Dict[str, Any]:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.cancel_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_job(
        self,
        PipelineId: str,
        Input: JobInputTypeDef = None,
        Inputs: List[JobInputTypeDef] = None,
        Output: CreateJobOutputTypeDef = None,
        Outputs: List[CreateJobOutputTypeDef] = None,
        OutputKeyPrefix: str = None,
        Playlists: List[CreateJobPlaylistTypeDef] = None,
        UserMetadata: Dict[str, str] = None,
    ) -> CreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_pipeline(
        self,
        Name: str,
        InputBucket: str,
        Role: str,
        OutputBucket: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: NotificationsTypeDef = None,
        ContentConfig: PipelineOutputConfigTypeDef = None,
        ThumbnailConfig: PipelineOutputConfigTypeDef = None,
    ) -> CreatePipelineResponseTypeDef:
        """
        [Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_preset(
        self,
        Name: str,
        Container: str,
        Description: str = None,
        Video: VideoParametersTypeDef = None,
        Audio: AudioParametersTypeDef = None,
        Thumbnails: ThumbnailsTypeDef = None,
    ) -> CreatePresetResponseTypeDef:
        """
        [Client.create_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_preset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_pipeline(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_preset(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.delete_preset)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs_by_pipeline(
        self, PipelineId: str, Ascending: str = None, PageToken: str = None
    ) -> ListJobsByPipelineResponseTypeDef:
        """
        [Client.list_jobs_by_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs_by_status(
        self, Status: str, Ascending: str = None, PageToken: str = None
    ) -> ListJobsByStatusResponseTypeDef:
        """
        [Client.list_jobs_by_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_jobs_by_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_pipelines(
        self, Ascending: str = None, PageToken: str = None
    ) -> ListPipelinesResponseTypeDef:
        """
        [Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_pipelines)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_presets(
        self, Ascending: str = None, PageToken: str = None
    ) -> ListPresetsResponseTypeDef:
        """
        [Client.list_presets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.list_presets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def read_job(self, Id: str) -> ReadJobResponseTypeDef:
        """
        [Client.read_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def read_pipeline(self, Id: str) -> ReadPipelineResponseTypeDef:
        """
        [Client.read_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def read_preset(self, Id: str) -> ReadPresetResponseTypeDef:
        """
        [Client.read_preset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.read_preset)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def test_role(
        self, Role: str, InputBucket: str, OutputBucket: str, Topics: List[str]
    ) -> TestRoleResponseTypeDef:
        """
        [Client.test_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.test_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_pipeline(
        self,
        Id: str,
        Name: str = None,
        InputBucket: str = None,
        Role: str = None,
        AwsKmsKeyArn: str = None,
        Notifications: NotificationsTypeDef = None,
        ContentConfig: PipelineOutputConfigTypeDef = None,
        ThumbnailConfig: PipelineOutputConfigTypeDef = None,
    ) -> UpdatePipelineResponseTypeDef:
        """
        [Client.update_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_pipeline_notifications(
        self, Id: str, Notifications: NotificationsTypeDef
    ) -> UpdatePipelineNotificationsResponseTypeDef:
        """
        [Client.update_pipeline_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_notifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_pipeline_status(self, Id: str, Status: str) -> UpdatePipelineStatusResponseTypeDef:
        """
        [Client.update_pipeline_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Client.update_pipeline_status)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs_by_pipeline"]
    ) -> paginator_scope.ListJobsByPipelinePaginator:
        """
        [Paginator.ListJobsByPipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs_by_status"]
    ) -> paginator_scope.ListJobsByStatusPaginator:
        """
        [Paginator.ListJobsByStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_pipelines"]
    ) -> paginator_scope.ListPipelinesPaginator:
        """
        [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_presets"]
    ) -> paginator_scope.ListPresetsPaginator:
        """
        [Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: Literal["job_complete"]) -> waiter_scope.JobCompleteWaiter:
        """
        [Waiter.JobComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    IncompatibleVersionException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError
