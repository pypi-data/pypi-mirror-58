"Main interface for wafv2 service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_wafv2.client as client_scope
from mypy_boto3_wafv2.type_defs import (
    CheckCapacityResponseTypeDef,
    CreateIPSetResponseTypeDef,
    CreateRegexPatternSetResponseTypeDef,
    CreateRuleGroupResponseTypeDef,
    CreateWebACLResponseTypeDef,
    DefaultActionTypeDef,
    DescribeManagedRuleGroupResponseTypeDef,
    GetIPSetResponseTypeDef,
    GetLoggingConfigurationResponseTypeDef,
    GetRateBasedStatementManagedKeysResponseTypeDef,
    GetRegexPatternSetResponseTypeDef,
    GetRuleGroupResponseTypeDef,
    GetSampledRequestsResponseTypeDef,
    GetWebACLForResourceResponseTypeDef,
    GetWebACLResponseTypeDef,
    ListAvailableManagedRuleGroupsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListRegexPatternSetsResponseTypeDef,
    ListResourcesForWebACLResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebACLsResponseTypeDef,
    LoggingConfigurationTypeDef,
    PutLoggingConfigurationResponseTypeDef,
    RegexTypeDef,
    RuleTypeDef,
    TagTypeDef,
    TimeWindowTypeDef,
    UpdateIPSetResponseTypeDef,
    UpdateRegexPatternSetResponseTypeDef,
    UpdateRuleGroupResponseTypeDef,
    UpdateWebACLResponseTypeDef,
    VisibilityConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WAFV2Client",)


class WAFV2Client(BaseClient):
    """
    [WAFV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_web_acl(self, WebACLArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.associate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.associate_web_acl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def check_capacity(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], Rules: List[RuleTypeDef]
    ) -> CheckCapacityResponseTypeDef:
        """
        [Client.check_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.check_capacity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_ip_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        IPAddressVersion: Literal["IPV4", "IPV6"],
        Addresses: List[str],
        Description: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateIPSetResponseTypeDef:
        """
        [Client.create_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.create_ip_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_regex_pattern_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        RegularExpressionList: List[RegexTypeDef],
        Description: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateRegexPatternSetResponseTypeDef:
        """
        [Client.create_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.create_regex_pattern_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_rule_group(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Capacity: int,
        VisibilityConfig: VisibilityConfigTypeDef,
        Description: str = None,
        Rules: List[RuleTypeDef] = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateRuleGroupResponseTypeDef:
        """
        [Client.create_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.create_rule_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_web_acl(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        DefaultAction: DefaultActionTypeDef,
        VisibilityConfig: VisibilityConfigTypeDef,
        Description: str = None,
        Rules: List[RuleTypeDef] = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateWebACLResponseTypeDef:
        """
        [Client.create_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.create_web_acl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_ip_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.delete_ip_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_logging_configuration(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.delete_logging_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_regex_pattern_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.delete_regex_pattern_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_rule_group(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.delete_rule_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_web_acl(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.delete_web_acl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_managed_rule_group(
        self, VendorName: str, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"]
    ) -> DescribeManagedRuleGroupResponseTypeDef:
        """
        [Client.describe_managed_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.describe_managed_rule_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_web_acl(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.disassociate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.disassociate_web_acl)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ip_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> GetIPSetResponseTypeDef:
        """
        [Client.get_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.get_ip_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_logging_configuration(self, ResourceArn: str) -> GetLoggingConfigurationResponseTypeDef:
        """
        [Client.get_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.get_logging_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_rate_based_statement_managed_keys(
        self,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        WebACLName: str,
        WebACLId: str,
        RuleName: str,
    ) -> GetRateBasedStatementManagedKeysResponseTypeDef:
        """
        [Client.get_rate_based_statement_managed_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.get_rate_based_statement_managed_keys)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_regex_pattern_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> GetRegexPatternSetResponseTypeDef:
        """
        [Client.get_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.get_regex_pattern_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_rule_group(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> GetRuleGroupResponseTypeDef:
        """
        [Client.get_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.get_rule_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_sampled_requests(
        self,
        WebAclArn: str,
        RuleMetricName: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        TimeWindow: TimeWindowTypeDef,
        MaxItems: int,
    ) -> GetSampledRequestsResponseTypeDef:
        """
        [Client.get_sampled_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.get_sampled_requests)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_web_acl(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> GetWebACLResponseTypeDef:
        """
        [Client.get_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.get_web_acl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_web_acl_for_resource(self, ResourceArn: str) -> GetWebACLForResourceResponseTypeDef:
        """
        [Client.get_web_acl_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.get_web_acl_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_available_managed_rule_groups(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ListAvailableManagedRuleGroupsResponseTypeDef:
        """
        [Client.list_available_managed_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.list_available_managed_rule_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_ip_sets(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ListIPSetsResponseTypeDef:
        """
        [Client.list_ip_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.list_ip_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_logging_configurations(
        self,
        Scope: Literal["CLOUDFRONT", "REGIONAL"] = None,
        NextMarker: str = None,
        Limit: int = None,
    ) -> ListLoggingConfigurationsResponseTypeDef:
        """
        [Client.list_logging_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.list_logging_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_regex_pattern_sets(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ListRegexPatternSetsResponseTypeDef:
        """
        [Client.list_regex_pattern_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.list_regex_pattern_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resources_for_web_acl(
        self,
        WebACLArn: str,
        ResourceType: Literal["APPLICATION_LOAD_BALANCER", "API_GATEWAY"] = None,
    ) -> ListResourcesForWebACLResponseTypeDef:
        """
        [Client.list_resources_for_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.list_resources_for_web_acl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_rule_groups(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ListRuleGroupsResponseTypeDef:
        """
        [Client.list_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.list_rule_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceARN: str, NextMarker: str = None, Limit: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_web_acls(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ListWebACLsResponseTypeDef:
        """
        [Client.list_web_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.list_web_acls)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_logging_configuration(
        self, LoggingConfiguration: LoggingConfigurationTypeDef
    ) -> PutLoggingConfigurationResponseTypeDef:
        """
        [Client.put_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.put_logging_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceARN: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_ip_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        Addresses: List[str],
        LockToken: str,
        Description: str = None,
    ) -> UpdateIPSetResponseTypeDef:
        """
        [Client.update_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.update_ip_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_regex_pattern_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        RegularExpressionList: List[RegexTypeDef],
        LockToken: str,
        Description: str = None,
    ) -> UpdateRegexPatternSetResponseTypeDef:
        """
        [Client.update_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.update_regex_pattern_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_rule_group(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        VisibilityConfig: VisibilityConfigTypeDef,
        LockToken: str,
        Description: str = None,
        Rules: List[RuleTypeDef] = None,
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        [Client.update_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.update_rule_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_web_acl(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        DefaultAction: DefaultActionTypeDef,
        VisibilityConfig: VisibilityConfigTypeDef,
        LockToken: str,
        Description: str = None,
        Rules: List[RuleTypeDef] = None,
    ) -> UpdateWebACLResponseTypeDef:
        """
        [Client.update_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/wafv2.html#WAFV2.Client.update_web_acl)
        """


class Exceptions:
    ClientError: Boto3ClientError
    WAFAssociatedItemException: Boto3ClientError
    WAFDuplicateItemException: Boto3ClientError
    WAFInternalErrorException: Boto3ClientError
    WAFInvalidParameterException: Boto3ClientError
    WAFInvalidResourceException: Boto3ClientError
    WAFLimitsExceededException: Boto3ClientError
    WAFNonexistentItemException: Boto3ClientError
    WAFOptimisticLockException: Boto3ClientError
    WAFServiceLinkedRoleErrorException: Boto3ClientError
    WAFTagOperationException: Boto3ClientError
    WAFTagOperationInternalErrorException: Boto3ClientError
    WAFUnavailableEntityException: Boto3ClientError
