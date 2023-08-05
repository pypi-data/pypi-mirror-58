"Main interface for mediapackage service"
from mypy_boto3_mediapackage.client import MediaPackageClient, MediaPackageClient as Client
from mypy_boto3_mediapackage.paginator import (
    ListChannelsPaginator,
    ListHarvestJobsPaginator,
    ListOriginEndpointsPaginator,
)


__all__ = (
    "Client",
    "ListChannelsPaginator",
    "ListHarvestJobsPaginator",
    "ListOriginEndpointsPaginator",
    "MediaPackageClient",
)
