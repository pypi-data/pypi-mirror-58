"Main interface for elastictranscoder service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elastictranscoder.type_defs import (
    ListJobsByPipelineResponseTypeDef,
    ListJobsByStatusResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListPresetsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListJobsByPipelinePaginator",
    "ListJobsByStatusPaginator",
    "ListPipelinesPaginator",
    "ListPresetsPaginator",
)


class ListJobsByPipelinePaginator(Boto3Paginator):
    """
    [Paginator.ListJobsByPipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PipelineId: str,
        Ascending: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListJobsByPipelineResponseTypeDef, None, None]:
        """
        [ListJobsByPipeline.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByPipeline.paginate)
        """


class ListJobsByStatusPaginator(Boto3Paginator):
    """
    [Paginator.ListJobsByStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Status: str, Ascending: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListJobsByStatusResponseTypeDef, None, None]:
        """
        [ListJobsByStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListJobsByStatus.paginate)
        """


class ListPipelinesPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Ascending: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPipelinesResponseTypeDef, None, None]:
        """
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPipelines.paginate)
        """


class ListPresetsPaginator(Boto3Paginator):
    """
    [Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Ascending: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPresetsResponseTypeDef, None, None]:
        """
        [ListPresets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elastictranscoder.html#ElasticTranscoder.Paginator.ListPresets.paginate)
        """
