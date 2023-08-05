"Main interface for resourcegroupstaggingapi service"
from mypy_boto3_resourcegroupstaggingapi.client import (
    ResourceGroupsTaggingAPIClient,
    ResourceGroupsTaggingAPIClient as Client,
)
from mypy_boto3_resourcegroupstaggingapi.paginator import (
    GetComplianceSummaryPaginator,
    GetResourcesPaginator,
    GetTagKeysPaginator,
    GetTagValuesPaginator,
)


__all__ = (
    "Client",
    "GetComplianceSummaryPaginator",
    "GetResourcesPaginator",
    "GetTagKeysPaginator",
    "GetTagValuesPaginator",
    "ResourceGroupsTaggingAPIClient",
)
