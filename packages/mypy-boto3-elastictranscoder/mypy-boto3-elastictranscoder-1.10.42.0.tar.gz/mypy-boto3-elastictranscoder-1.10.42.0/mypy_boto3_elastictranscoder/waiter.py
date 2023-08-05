"Main interface for elastictranscoder service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_elastictranscoder.type_defs import WaiterConfigTypeDef


__all__ = ("JobCompleteWaiter",)


class JobCompleteWaiter(Boto3Waiter):
    """
    [Waiter.JobComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [JobComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/elastictranscoder.html#ElasticTranscoder.Waiter.JobComplete.wait)
        """
