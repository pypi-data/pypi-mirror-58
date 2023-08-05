"Main interface for cloudfront service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_cloudfront.type_defs import WaiterConfigTypeDef


__all__ = (
    "DistributionDeployedWaiter",
    "InvalidationCompletedWaiter",
    "StreamingDistributionDeployedWaiter",
)


class DistributionDeployedWaiter(Boto3Waiter):
    """
    [Waiter.DistributionDeployed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudfront.html#CloudFront.Waiter.DistributionDeployed)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [DistributionDeployed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudfront.html#CloudFront.Waiter.DistributionDeployed.wait)
        """


class InvalidationCompletedWaiter(Boto3Waiter):
    """
    [Waiter.InvalidationCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudfront.html#CloudFront.Waiter.InvalidationCompleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, DistributionId: str, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [InvalidationCompleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudfront.html#CloudFront.Waiter.InvalidationCompleted.wait)
        """


class StreamingDistributionDeployedWaiter(Boto3Waiter):
    """
    [Waiter.StreamingDistributionDeployed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudfront.html#CloudFront.Waiter.StreamingDistributionDeployed)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, Id: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [StreamingDistributionDeployed.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/cloudfront.html#CloudFront.Waiter.StreamingDistributionDeployed.wait)
        """
