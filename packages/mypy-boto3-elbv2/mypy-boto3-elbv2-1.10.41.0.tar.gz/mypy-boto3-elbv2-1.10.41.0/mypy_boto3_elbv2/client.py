"Main interface for elbv2 service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_elbv2.client as client_scope

# pylint: disable=import-self
import mypy_boto3_elbv2.paginator as paginator_scope
from mypy_boto3_elbv2.type_defs import (
    ActionTypeDef,
    AddListenerCertificatesOutputTypeDef,
    CertificateTypeDef,
    CreateListenerOutputTypeDef,
    CreateLoadBalancerOutputTypeDef,
    CreateRuleOutputTypeDef,
    CreateTargetGroupOutputTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    DescribeListenerCertificatesOutputTypeDef,
    DescribeListenersOutputTypeDef,
    DescribeLoadBalancerAttributesOutputTypeDef,
    DescribeLoadBalancersOutputTypeDef,
    DescribeRulesOutputTypeDef,
    DescribeSSLPoliciesOutputTypeDef,
    DescribeTagsOutputTypeDef,
    DescribeTargetGroupAttributesOutputTypeDef,
    DescribeTargetGroupsOutputTypeDef,
    DescribeTargetHealthOutputTypeDef,
    LoadBalancerAttributeTypeDef,
    MatcherTypeDef,
    ModifyListenerOutputTypeDef,
    ModifyLoadBalancerAttributesOutputTypeDef,
    ModifyRuleOutputTypeDef,
    ModifyTargetGroupAttributesOutputTypeDef,
    ModifyTargetGroupOutputTypeDef,
    RuleConditionTypeDef,
    RulePriorityPairTypeDef,
    SetIpAddressTypeOutputTypeDef,
    SetRulePrioritiesOutputTypeDef,
    SetSecurityGroupsOutputTypeDef,
    SetSubnetsOutputTypeDef,
    SubnetMappingTypeDef,
    TagTypeDef,
    TargetDescriptionTypeDef,
    TargetGroupAttributeTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_elbv2.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticLoadBalancingv2Client",)


class ElasticLoadBalancingv2Client(BaseClient):
    """
    [ElasticLoadBalancingv2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_listener_certificates(
        self, ListenerArn: str, Certificates: List[CertificateTypeDef]
    ) -> AddListenerCertificatesOutputTypeDef:
        """
        [Client.add_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.add_listener_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags(self, ResourceArns: List[str], Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.add_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_listener(
        self,
        LoadBalancerArn: str,
        Protocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        Port: int,
        DefaultActions: List[ActionTypeDef],
        SslPolicy: str = None,
        Certificates: List[CertificateTypeDef] = None,
    ) -> CreateListenerOutputTypeDef:
        """
        [Client.create_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_listener)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_load_balancer(
        self,
        Name: str,
        Subnets: List[str] = None,
        SubnetMappings: List[SubnetMappingTypeDef] = None,
        SecurityGroups: List[str] = None,
        Scheme: Literal["internet-facing", "internal"] = None,
        Tags: List[TagTypeDef] = None,
        Type: Literal["application", "network"] = None,
        IpAddressType: Literal["ipv4", "dualstack"] = None,
    ) -> CreateLoadBalancerOutputTypeDef:
        """
        [Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_rule(
        self,
        ListenerArn: str,
        Conditions: List[RuleConditionTypeDef],
        Priority: int,
        Actions: List[ActionTypeDef],
    ) -> CreateRuleOutputTypeDef:
        """
        [Client.create_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_target_group(
        self,
        Name: str,
        Protocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"] = None,
        Port: int = None,
        VpcId: str = None,
        HealthCheckProtocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"] = None,
        HealthCheckPort: str = None,
        HealthCheckEnabled: bool = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        HealthCheckTimeoutSeconds: int = None,
        HealthyThresholdCount: int = None,
        UnhealthyThresholdCount: int = None,
        Matcher: MatcherTypeDef = None,
        TargetType: Literal["instance", "ip", "lambda"] = None,
    ) -> CreateTargetGroupOutputTypeDef:
        """
        [Client.create_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_target_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_listener(self, ListenerArn: str) -> Dict[str, Any]:
        """
        [Client.delete_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_listener)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_load_balancer(self, LoadBalancerArn: str) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_rule(self, RuleArn: str) -> Dict[str, Any]:
        """
        [Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_target_group(self, TargetGroupArn: str) -> Dict[str, Any]:
        """
        [Client.delete_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.delete_target_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_targets(
        self, TargetGroupArn: str, Targets: List[TargetDescriptionTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.deregister_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.deregister_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_limits(
        self, Marker: str = None, PageSize: int = None
    ) -> DescribeAccountLimitsOutputTypeDef:
        """
        [Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_account_limits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_listener_certificates(
        self, ListenerArn: str, Marker: str = None, PageSize: int = None
    ) -> DescribeListenerCertificatesOutputTypeDef:
        """
        [Client.describe_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_listener_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_listeners(
        self,
        LoadBalancerArn: str = None,
        ListenerArns: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> DescribeListenersOutputTypeDef:
        """
        [Client.describe_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_listeners)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_load_balancer_attributes(
        self, LoadBalancerArn: str
    ) -> DescribeLoadBalancerAttributesOutputTypeDef:
        """
        [Client.describe_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_load_balancer_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_load_balancers(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> DescribeLoadBalancersOutputTypeDef:
        """
        [Client.describe_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_load_balancers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_rules(
        self,
        ListenerArn: str = None,
        RuleArns: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> DescribeRulesOutputTypeDef:
        """
        [Client.describe_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_ssl_policies(
        self, Names: List[str] = None, Marker: str = None, PageSize: int = None
    ) -> DescribeSSLPoliciesOutputTypeDef:
        """
        [Client.describe_ssl_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_ssl_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tags(self, ResourceArns: List[str]) -> DescribeTagsOutputTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_target_group_attributes(
        self, TargetGroupArn: str
    ) -> DescribeTargetGroupAttributesOutputTypeDef:
        """
        [Client.describe_target_group_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_group_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_target_groups(
        self,
        LoadBalancerArn: str = None,
        TargetGroupArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> DescribeTargetGroupsOutputTypeDef:
        """
        [Client.describe_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_target_health(
        self, TargetGroupArn: str, Targets: List[TargetDescriptionTypeDef] = None
    ) -> DescribeTargetHealthOutputTypeDef:
        """
        [Client.describe_target_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.describe_target_health)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_listener(
        self,
        ListenerArn: str,
        Port: int = None,
        Protocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"] = None,
        SslPolicy: str = None,
        Certificates: List[CertificateTypeDef] = None,
        DefaultActions: List[ActionTypeDef] = None,
    ) -> ModifyListenerOutputTypeDef:
        """
        [Client.modify_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_listener)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_load_balancer_attributes(
        self, LoadBalancerArn: str, Attributes: List[LoadBalancerAttributeTypeDef]
    ) -> ModifyLoadBalancerAttributesOutputTypeDef:
        """
        [Client.modify_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_load_balancer_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_rule(
        self,
        RuleArn: str,
        Conditions: List[RuleConditionTypeDef] = None,
        Actions: List[ActionTypeDef] = None,
    ) -> ModifyRuleOutputTypeDef:
        """
        [Client.modify_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_target_group(
        self,
        TargetGroupArn: str,
        HealthCheckProtocol: Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"] = None,
        HealthCheckPort: str = None,
        HealthCheckPath: str = None,
        HealthCheckEnabled: bool = None,
        HealthCheckIntervalSeconds: int = None,
        HealthCheckTimeoutSeconds: int = None,
        HealthyThresholdCount: int = None,
        UnhealthyThresholdCount: int = None,
        Matcher: MatcherTypeDef = None,
    ) -> ModifyTargetGroupOutputTypeDef:
        """
        [Client.modify_target_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_target_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_target_group_attributes(
        self, TargetGroupArn: str, Attributes: List[TargetGroupAttributeTypeDef]
    ) -> ModifyTargetGroupAttributesOutputTypeDef:
        """
        [Client.modify_target_group_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.modify_target_group_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_targets(
        self, TargetGroupArn: str, Targets: List[TargetDescriptionTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.register_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.register_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_listener_certificates(
        self, ListenerArn: str, Certificates: List[CertificateTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.remove_listener_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.remove_listener_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags(self, ResourceArns: List[str], TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.remove_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_ip_address_type(
        self, LoadBalancerArn: str, IpAddressType: Literal["ipv4", "dualstack"]
    ) -> SetIpAddressTypeOutputTypeDef:
        """
        [Client.set_ip_address_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_ip_address_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_rule_priorities(
        self, RulePriorities: List[RulePriorityPairTypeDef]
    ) -> SetRulePrioritiesOutputTypeDef:
        """
        [Client.set_rule_priorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_rule_priorities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_security_groups(
        self, LoadBalancerArn: str, SecurityGroups: List[str]
    ) -> SetSecurityGroupsOutputTypeDef:
        """
        [Client.set_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_security_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_subnets(
        self,
        LoadBalancerArn: str,
        Subnets: List[str] = None,
        SubnetMappings: List[SubnetMappingTypeDef] = None,
    ) -> SetSubnetsOutputTypeDef:
        """
        [Client.set_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.set_subnets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> paginator_scope.DescribeAccountLimitsPaginator:
        """
        [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeAccountLimits)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_listener_certificates"]
    ) -> paginator_scope.DescribeListenerCertificatesPaginator:
        """
        [Paginator.DescribeListenerCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListenerCertificates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_listeners"]
    ) -> paginator_scope.DescribeListenersPaginator:
        """
        [Paginator.DescribeListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListeners)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_load_balancers"]
    ) -> paginator_scope.DescribeLoadBalancersPaginator:
        """
        [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_rules"]
    ) -> paginator_scope.DescribeRulesPaginator:
        """
        [Paginator.DescribeRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeRules)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_ssl_policies"]
    ) -> paginator_scope.DescribeSSLPoliciesPaginator:
        """
        [Paginator.DescribeSSLPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeSSLPolicies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_target_groups"]
    ) -> paginator_scope.DescribeTargetGroupsPaginator:
        """
        [Paginator.DescribeTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeTargetGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["load_balancer_available"]
    ) -> waiter_scope.LoadBalancerAvailableWaiter:
        """
        [Waiter.LoadBalancerAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["load_balancer_exists"]
    ) -> waiter_scope.LoadBalancerExistsWaiter:
        """
        [Waiter.LoadBalancerExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerExists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["load_balancers_deleted"]
    ) -> waiter_scope.LoadBalancersDeletedWaiter:
        """
        [Waiter.LoadBalancersDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancersDeleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["target_deregistered"]
    ) -> waiter_scope.TargetDeregisteredWaiter:
        """
        [Waiter.TargetDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetDeregistered)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["target_in_service"]
    ) -> waiter_scope.TargetInServiceWaiter:
        """
        [Waiter.TargetInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetInService)
        """


class Exceptions:
    AllocationIdNotFoundException: Boto3ClientError
    AvailabilityZoneNotSupportedException: Boto3ClientError
    CertificateNotFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    DuplicateListenerException: Boto3ClientError
    DuplicateLoadBalancerNameException: Boto3ClientError
    DuplicateTagKeysException: Boto3ClientError
    DuplicateTargetGroupNameException: Boto3ClientError
    HealthUnavailableException: Boto3ClientError
    IncompatibleProtocolsException: Boto3ClientError
    InvalidConfigurationRequestException: Boto3ClientError
    InvalidLoadBalancerActionException: Boto3ClientError
    InvalidSchemeException: Boto3ClientError
    InvalidSecurityGroupException: Boto3ClientError
    InvalidSubnetException: Boto3ClientError
    InvalidTargetException: Boto3ClientError
    ListenerNotFoundException: Boto3ClientError
    LoadBalancerNotFoundException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    PriorityInUseException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    RuleNotFoundException: Boto3ClientError
    SSLPolicyNotFoundException: Boto3ClientError
    SubnetNotFoundException: Boto3ClientError
    TargetGroupAssociationLimitException: Boto3ClientError
    TargetGroupNotFoundException: Boto3ClientError
    TooManyActionsException: Boto3ClientError
    TooManyCertificatesException: Boto3ClientError
    TooManyListenersException: Boto3ClientError
    TooManyLoadBalancersException: Boto3ClientError
    TooManyRegistrationsForTargetIdException: Boto3ClientError
    TooManyRulesException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    TooManyTargetGroupsException: Boto3ClientError
    TooManyTargetsException: Boto3ClientError
    TooManyUniqueTargetGroupsPerLoadBalancerException: Boto3ClientError
    UnsupportedProtocolException: Boto3ClientError
