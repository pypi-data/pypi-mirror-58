"Main interface for cloudfront service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudfront.type_defs import (
    ListCloudFrontOriginAccessIdentitiesResultTypeDef,
    ListDistributionsResultTypeDef,
    ListInvalidationsResultTypeDef,
    ListStreamingDistributionsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListCloudFrontOriginAccessIdentitiesPaginator",
    "ListDistributionsPaginator",
    "ListInvalidationsPaginator",
    "ListStreamingDistributionsPaginator",
)


class ListCloudFrontOriginAccessIdentitiesPaginator(Boto3Paginator):
    """
    [Paginator.ListCloudFrontOriginAccessIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cloudfront.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListCloudFrontOriginAccessIdentitiesResultTypeDef, None, None]:
        """
        [ListCloudFrontOriginAccessIdentities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cloudfront.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities.paginate)
        """


class ListDistributionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cloudfront.html#CloudFront.Paginator.ListDistributions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDistributionsResultTypeDef, None, None]:
        """
        [ListDistributions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cloudfront.html#CloudFront.Paginator.ListDistributions.paginate)
        """


class ListInvalidationsPaginator(Boto3Paginator):
    """
    [Paginator.ListInvalidations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cloudfront.html#CloudFront.Paginator.ListInvalidations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DistributionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListInvalidationsResultTypeDef, None, None]:
        """
        [ListInvalidations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cloudfront.html#CloudFront.Paginator.ListInvalidations.paginate)
        """


class ListStreamingDistributionsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreamingDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cloudfront.html#CloudFront.Paginator.ListStreamingDistributions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListStreamingDistributionsResultTypeDef, None, None]:
        """
        [ListStreamingDistributions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/cloudfront.html#CloudFront.Paginator.ListStreamingDistributions.paginate)
        """
