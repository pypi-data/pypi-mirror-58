"Main interface for elastictranscoder service"
from mypy_boto3_elastictranscoder.client import (
    ElasticTranscoderClient,
    ElasticTranscoderClient as Client,
)
from mypy_boto3_elastictranscoder.paginator import (
    ListJobsByPipelinePaginator,
    ListJobsByStatusPaginator,
    ListPipelinesPaginator,
    ListPresetsPaginator,
)
from mypy_boto3_elastictranscoder.waiter import JobCompleteWaiter


__all__ = (
    "Client",
    "ElasticTranscoderClient",
    "JobCompleteWaiter",
    "ListJobsByPipelinePaginator",
    "ListJobsByStatusPaginator",
    "ListPipelinesPaginator",
    "ListPresetsPaginator",
)
