"Main interface for mediapackage-vod service"
from mypy_boto3_mediapackage_vod.client import (
    MediaPackageVodClient as Client,
    MediaPackageVodClient,
)
from mypy_boto3_mediapackage_vod.paginator import (
    ListAssetsPaginator,
    ListPackagingConfigurationsPaginator,
    ListPackagingGroupsPaginator,
)


__all__ = (
    "Client",
    "ListAssetsPaginator",
    "ListPackagingConfigurationsPaginator",
    "ListPackagingGroupsPaginator",
    "MediaPackageVodClient",
)
