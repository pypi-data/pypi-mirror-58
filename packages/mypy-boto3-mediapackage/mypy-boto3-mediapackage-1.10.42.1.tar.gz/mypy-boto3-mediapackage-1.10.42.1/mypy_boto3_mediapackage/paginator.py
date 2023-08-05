"Main interface for mediapackage service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediapackage.type_defs import (
    ListChannelsResponseTypeDef,
    ListHarvestJobsResponseTypeDef,
    ListOriginEndpointsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListChannelsPaginator", "ListHarvestJobsPaginator", "ListOriginEndpointsPaginator")


class ListChannelsPaginator(Boto3Paginator):
    """
    [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediapackage.html#MediaPackage.Paginator.ListChannels)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListChannelsResponseTypeDef, None, None]:
        """
        [ListChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediapackage.html#MediaPackage.Paginator.ListChannels.paginate)
        """


class ListHarvestJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListHarvestJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediapackage.html#MediaPackage.Paginator.ListHarvestJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        IncludeChannelId: str = None,
        IncludeStatus: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListHarvestJobsResponseTypeDef, None, None]:
        """
        [ListHarvestJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediapackage.html#MediaPackage.Paginator.ListHarvestJobs.paginate)
        """


class ListOriginEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.ListOriginEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediapackage.html#MediaPackage.Paginator.ListOriginEndpoints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ChannelId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListOriginEndpointsResponseTypeDef, None, None]:
        """
        [ListOriginEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/mediapackage.html#MediaPackage.Paginator.ListOriginEndpoints.paginate)
        """
