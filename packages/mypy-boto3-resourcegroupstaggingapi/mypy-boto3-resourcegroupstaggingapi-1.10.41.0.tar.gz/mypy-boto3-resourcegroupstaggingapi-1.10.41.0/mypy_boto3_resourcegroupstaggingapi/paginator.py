"Main interface for resourcegroupstaggingapi service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_resourcegroupstaggingapi.type_defs import (
    GetComplianceSummaryOutputTypeDef,
    GetResourcesOutputTypeDef,
    GetTagKeysOutputTypeDef,
    GetTagValuesOutputTypeDef,
    PaginatorConfigTypeDef,
    TagFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetComplianceSummaryPaginator",
    "GetResourcesPaginator",
    "GetTagKeysPaginator",
    "GetTagValuesPaginator",
)


class GetComplianceSummaryPaginator(Boto3Paginator):
    """
    [Paginator.GetComplianceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TargetIdFilters: List[str] = None,
        RegionFilters: List[str] = None,
        ResourceTypeFilters: List[str] = None,
        TagKeyFilters: List[str] = None,
        GroupBy: List[Literal["TARGET_ID", "REGION", "RESOURCE_TYPE"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetComplianceSummaryOutputTypeDef, None, None]:
        """
        [GetComplianceSummary.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary.paginate)
        """


class GetResourcesPaginator(Boto3Paginator):
    """
    [Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TagFilters: List[TagFilterTypeDef] = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[str] = None,
        IncludeComplianceDetails: bool = None,
        ExcludeCompliantResources: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetResourcesOutputTypeDef, None, None]:
        """
        [GetResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources.paginate)
        """


class GetTagKeysPaginator(Boto3Paginator):
    """
    [Paginator.GetTagKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetTagKeysOutputTypeDef, None, None]:
        """
        [GetTagKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys.paginate)
        """


class GetTagValuesPaginator(Boto3Paginator):
    """
    [Paginator.GetTagValues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Key: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetTagValuesOutputTypeDef, None, None]:
        """
        [GetTagValues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues.paginate)
        """
