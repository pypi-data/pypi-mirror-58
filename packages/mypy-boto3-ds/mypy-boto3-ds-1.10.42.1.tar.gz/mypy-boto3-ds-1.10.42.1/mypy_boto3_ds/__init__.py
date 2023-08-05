"Main interface for ds service"
from mypy_boto3_ds.client import DirectoryServiceClient as Client, DirectoryServiceClient
from mypy_boto3_ds.paginator import (
    DescribeDirectoriesPaginator,
    DescribeDomainControllersPaginator,
    DescribeSharedDirectoriesPaginator,
    DescribeSnapshotsPaginator,
    DescribeTrustsPaginator,
    ListIpRoutesPaginator,
    ListLogSubscriptionsPaginator,
    ListSchemaExtensionsPaginator,
    ListTagsForResourcePaginator,
)


__all__ = (
    "Client",
    "DescribeDirectoriesPaginator",
    "DescribeDomainControllersPaginator",
    "DescribeSharedDirectoriesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeTrustsPaginator",
    "DirectoryServiceClient",
    "ListIpRoutesPaginator",
    "ListLogSubscriptionsPaginator",
    "ListSchemaExtensionsPaginator",
    "ListTagsForResourcePaginator",
)
