"Main interface for cloudtrail service"
from mypy_boto3_cloudtrail.client import CloudTrailClient, CloudTrailClient as Client
from mypy_boto3_cloudtrail.paginator import (
    ListPublicKeysPaginator,
    ListTagsPaginator,
    ListTrailsPaginator,
    LookupEventsPaginator,
)


__all__ = (
    "Client",
    "CloudTrailClient",
    "ListPublicKeysPaginator",
    "ListTagsPaginator",
    "ListTrailsPaginator",
    "LookupEventsPaginator",
)
