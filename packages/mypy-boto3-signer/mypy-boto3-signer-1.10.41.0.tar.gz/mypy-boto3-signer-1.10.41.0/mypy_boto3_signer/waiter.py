"Main interface for signer service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_signer.type_defs import WaiterConfigTypeDef


__all__ = ("SuccessfulSigningJobWaiter",)


class SuccessfulSigningJobWaiter(Boto3Waiter):
    """
    [Waiter.SuccessfulSigningJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/signer.html#Signer.Waiter.SuccessfulSigningJob)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, jobId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [SuccessfulSigningJob.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/signer.html#Signer.Waiter.SuccessfulSigningJob.wait)
        """
