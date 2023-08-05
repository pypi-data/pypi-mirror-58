"Main interface for resourcegroupstaggingapi service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_resourcegroupstaggingapi.client as client_scope

# pylint: disable=import-self
import mypy_boto3_resourcegroupstaggingapi.paginator as paginator_scope
from mypy_boto3_resourcegroupstaggingapi.type_defs import (
    DescribeReportCreationOutputTypeDef,
    GetComplianceSummaryOutputTypeDef,
    GetResourcesOutputTypeDef,
    GetTagKeysOutputTypeDef,
    GetTagValuesOutputTypeDef,
    TagFilterTypeDef,
    TagResourcesOutputTypeDef,
    UntagResourcesOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ResourceGroupsTaggingAPIClient",)


class ResourceGroupsTaggingAPIClient(BaseClient):
    """
    [ResourceGroupsTaggingAPI.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_report_creation(self) -> DescribeReportCreationOutputTypeDef:
        """
        [Client.describe_report_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.describe_report_creation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_compliance_summary(
        self,
        TargetIdFilters: List[str] = None,
        RegionFilters: List[str] = None,
        ResourceTypeFilters: List[str] = None,
        TagKeyFilters: List[str] = None,
        GroupBy: List[Literal["TARGET_ID", "REGION", "RESOURCE_TYPE"]] = None,
        MaxResults: int = None,
        PaginationToken: str = None,
    ) -> GetComplianceSummaryOutputTypeDef:
        """
        [Client.get_compliance_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_compliance_summary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resources(
        self,
        PaginationToken: str = None,
        TagFilters: List[TagFilterTypeDef] = None,
        ResourcesPerPage: int = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[str] = None,
        IncludeComplianceDetails: bool = None,
        ExcludeCompliantResources: bool = None,
    ) -> GetResourcesOutputTypeDef:
        """
        [Client.get_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_tag_keys(self, PaginationToken: str = None) -> GetTagKeysOutputTypeDef:
        """
        [Client.get_tag_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_tag_keys)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_tag_values(self, Key: str, PaginationToken: str = None) -> GetTagValuesOutputTypeDef:
        """
        [Client.get_tag_values documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.get_tag_values)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_report_creation(self, S3Bucket: str) -> Dict[str, Any]:
        """
        [Client.start_report_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.start_report_creation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resources(
        self, ResourceARNList: List[str], Tags: Dict[str, str]
    ) -> TagResourcesOutputTypeDef:
        """
        [Client.tag_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.tag_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resources(
        self, ResourceARNList: List[str], TagKeys: List[str]
    ) -> UntagResourcesOutputTypeDef:
        """
        [Client.untag_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Client.untag_resources)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_compliance_summary"]
    ) -> paginator_scope.GetComplianceSummaryPaginator:
        """
        [Paginator.GetComplianceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetComplianceSummary)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_resources"]
    ) -> paginator_scope.GetResourcesPaginator:
        """
        [Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetResources)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_tag_keys"]
    ) -> paginator_scope.GetTagKeysPaginator:
        """
        [Paginator.GetTagKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagKeys)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_tag_values"]
    ) -> paginator_scope.GetTagValuesPaginator:
        """
        [Paginator.GetTagValues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI.Paginator.GetTagValues)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    ConstraintViolationException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    PaginationTokenExpiredException: Boto3ClientError
    ThrottledException: Boto3ClientError
