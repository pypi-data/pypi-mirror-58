"Main interface for cloudfront service"
from mypy_boto3_cloudfront.client import CloudFrontClient, CloudFrontClient as Client
from mypy_boto3_cloudfront.paginator import (
    ListCloudFrontOriginAccessIdentitiesPaginator,
    ListDistributionsPaginator,
    ListInvalidationsPaginator,
    ListStreamingDistributionsPaginator,
)
from mypy_boto3_cloudfront.waiter import (
    DistributionDeployedWaiter,
    InvalidationCompletedWaiter,
    StreamingDistributionDeployedWaiter,
)


__all__ = (
    "Client",
    "CloudFrontClient",
    "DistributionDeployedWaiter",
    "InvalidationCompletedWaiter",
    "ListCloudFrontOriginAccessIdentitiesPaginator",
    "ListDistributionsPaginator",
    "ListInvalidationsPaginator",
    "ListStreamingDistributionsPaginator",
    "StreamingDistributionDeployedWaiter",
)
