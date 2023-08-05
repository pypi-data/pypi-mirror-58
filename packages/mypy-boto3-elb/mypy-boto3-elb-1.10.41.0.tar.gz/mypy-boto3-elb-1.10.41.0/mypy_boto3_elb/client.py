"Main interface for elb service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_elb.client as client_scope

# pylint: disable=import-self
import mypy_boto3_elb.paginator as paginator_scope
from mypy_boto3_elb.type_defs import (
    AddAvailabilityZonesOutputTypeDef,
    ApplySecurityGroupsToLoadBalancerOutputTypeDef,
    AttachLoadBalancerToSubnetsOutputTypeDef,
    ConfigureHealthCheckOutputTypeDef,
    CreateAccessPointOutputTypeDef,
    DeregisterEndPointsOutputTypeDef,
    DescribeAccessPointsOutputTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    DescribeEndPointStateOutputTypeDef,
    DescribeLoadBalancerAttributesOutputTypeDef,
    DescribeLoadBalancerPoliciesOutputTypeDef,
    DescribeLoadBalancerPolicyTypesOutputTypeDef,
    DescribeTagsOutputTypeDef,
    DetachLoadBalancerFromSubnetsOutputTypeDef,
    HealthCheckTypeDef,
    InstanceTypeDef,
    ListenerTypeDef,
    LoadBalancerAttributesTypeDef,
    ModifyLoadBalancerAttributesOutputTypeDef,
    PolicyAttributeTypeDef,
    RegisterEndPointsOutputTypeDef,
    RemoveAvailabilityZonesOutputTypeDef,
    TagKeyOnlyTypeDef,
    TagTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_elb.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticLoadBalancingClient",)


class ElasticLoadBalancingClient(BaseClient):
    """
    [ElasticLoadBalancing.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags(self, LoadBalancerNames: List[str], Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.add_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def apply_security_groups_to_load_balancer(
        self, LoadBalancerName: str, SecurityGroups: List[str]
    ) -> ApplySecurityGroupsToLoadBalancerOutputTypeDef:
        """
        [Client.apply_security_groups_to_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.apply_security_groups_to_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_load_balancer_to_subnets(
        self, LoadBalancerName: str, Subnets: List[str]
    ) -> AttachLoadBalancerToSubnetsOutputTypeDef:
        """
        [Client.attach_load_balancer_to_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.attach_load_balancer_to_subnets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def configure_health_check(
        self, LoadBalancerName: str, HealthCheck: HealthCheckTypeDef
    ) -> ConfigureHealthCheckOutputTypeDef:
        """
        [Client.configure_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.configure_health_check)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_app_cookie_stickiness_policy(
        self, LoadBalancerName: str, PolicyName: str, CookieName: str
    ) -> Dict[str, Any]:
        """
        [Client.create_app_cookie_stickiness_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.create_app_cookie_stickiness_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_lb_cookie_stickiness_policy(
        self, LoadBalancerName: str, PolicyName: str, CookieExpirationPeriod: int = None
    ) -> Dict[str, Any]:
        """
        [Client.create_lb_cookie_stickiness_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.create_lb_cookie_stickiness_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_load_balancer(
        self,
        LoadBalancerName: str,
        Listeners: List[ListenerTypeDef],
        AvailabilityZones: List[str] = None,
        Subnets: List[str] = None,
        SecurityGroups: List[str] = None,
        Scheme: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateAccessPointOutputTypeDef:
        """
        [Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_load_balancer_listeners(
        self, LoadBalancerName: str, Listeners: List[ListenerTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.create_load_balancer_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer_listeners)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_load_balancer_policy(
        self,
        LoadBalancerName: str,
        PolicyName: str,
        PolicyTypeName: str,
        PolicyAttributes: List[PolicyAttributeTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_load_balancer_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.create_load_balancer_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_load_balancer(self, LoadBalancerName: str) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_load_balancer_listeners(
        self, LoadBalancerName: str, LoadBalancerPorts: List[int]
    ) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer_listeners)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_load_balancer_policy(self, LoadBalancerName: str, PolicyName: str) -> Dict[str, Any]:
        """
        [Client.delete_load_balancer_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.delete_load_balancer_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_instances_from_load_balancer(
        self, LoadBalancerName: str, Instances: List[InstanceTypeDef]
    ) -> DeregisterEndPointsOutputTypeDef:
        """
        [Client.deregister_instances_from_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.deregister_instances_from_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_limits(
        self, Marker: str = None, PageSize: int = None
    ) -> DescribeAccountLimitsOutputTypeDef:
        """
        [Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.describe_account_limits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instance_health(
        self, LoadBalancerName: str, Instances: List[InstanceTypeDef] = None
    ) -> DescribeEndPointStateOutputTypeDef:
        """
        [Client.describe_instance_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.describe_instance_health)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_load_balancer_attributes(
        self, LoadBalancerName: str
    ) -> DescribeLoadBalancerAttributesOutputTypeDef:
        """
        [Client.describe_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_load_balancer_policies(
        self, LoadBalancerName: str = None, PolicyNames: List[str] = None
    ) -> DescribeLoadBalancerPoliciesOutputTypeDef:
        """
        [Client.describe_load_balancer_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_load_balancer_policy_types(
        self, PolicyTypeNames: List[str] = None
    ) -> DescribeLoadBalancerPolicyTypesOutputTypeDef:
        """
        [Client.describe_load_balancer_policy_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancer_policy_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_load_balancers(
        self, LoadBalancerNames: List[str] = None, Marker: str = None, PageSize: int = None
    ) -> DescribeAccessPointsOutputTypeDef:
        """
        [Client.describe_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.describe_load_balancers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tags(self, LoadBalancerNames: List[str]) -> DescribeTagsOutputTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.describe_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_load_balancer_from_subnets(
        self, LoadBalancerName: str, Subnets: List[str]
    ) -> DetachLoadBalancerFromSubnetsOutputTypeDef:
        """
        [Client.detach_load_balancer_from_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.detach_load_balancer_from_subnets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_availability_zones_for_load_balancer(
        self, LoadBalancerName: str, AvailabilityZones: List[str]
    ) -> RemoveAvailabilityZonesOutputTypeDef:
        """
        [Client.disable_availability_zones_for_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.disable_availability_zones_for_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_availability_zones_for_load_balancer(
        self, LoadBalancerName: str, AvailabilityZones: List[str]
    ) -> AddAvailabilityZonesOutputTypeDef:
        """
        [Client.enable_availability_zones_for_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.enable_availability_zones_for_load_balancer)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_load_balancer_attributes(
        self, LoadBalancerName: str, LoadBalancerAttributes: LoadBalancerAttributesTypeDef
    ) -> ModifyLoadBalancerAttributesOutputTypeDef:
        """
        [Client.modify_load_balancer_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.modify_load_balancer_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_instances_with_load_balancer(
        self, LoadBalancerName: str, Instances: List[InstanceTypeDef]
    ) -> RegisterEndPointsOutputTypeDef:
        """
        [Client.register_instances_with_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.register_instances_with_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags(
        self, LoadBalancerNames: List[str], Tags: List[TagKeyOnlyTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.remove_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_load_balancer_listener_ssl_certificate(
        self, LoadBalancerName: str, LoadBalancerPort: int, SSLCertificateId: str
    ) -> Dict[str, Any]:
        """
        [Client.set_load_balancer_listener_ssl_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_listener_ssl_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_load_balancer_policies_for_backend_server(
        self, LoadBalancerName: str, InstancePort: int, PolicyNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.set_load_balancer_policies_for_backend_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_policies_for_backend_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_load_balancer_policies_of_listener(
        self, LoadBalancerName: str, LoadBalancerPort: int, PolicyNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.set_load_balancer_policies_of_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Client.set_load_balancer_policies_of_listener)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> paginator_scope.DescribeAccountLimitsPaginator:
        """
        [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_load_balancers"]
    ) -> paginator_scope.DescribeLoadBalancersPaginator:
        """
        [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["any_instance_in_service"]
    ) -> waiter_scope.AnyInstanceInServiceWaiter:
        """
        [Waiter.AnyInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Waiter.AnyInstanceInService)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["instance_deregistered"]
    ) -> waiter_scope.InstanceDeregisteredWaiter:
        """
        [Waiter.InstanceDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceDeregistered)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["instance_in_service"]
    ) -> waiter_scope.InstanceInServiceWaiter:
        """
        [Waiter.InstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceInService)
        """


class Exceptions:
    AccessPointNotFoundException: Boto3ClientError
    CertificateNotFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    DependencyThrottleException: Boto3ClientError
    DuplicateAccessPointNameException: Boto3ClientError
    DuplicateListenerException: Boto3ClientError
    DuplicatePolicyNameException: Boto3ClientError
    DuplicateTagKeysException: Boto3ClientError
    InvalidConfigurationRequestException: Boto3ClientError
    InvalidEndPointException: Boto3ClientError
    InvalidSchemeException: Boto3ClientError
    InvalidSecurityGroupException: Boto3ClientError
    InvalidSubnetException: Boto3ClientError
    ListenerNotFoundException: Boto3ClientError
    LoadBalancerAttributeNotFoundException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    PolicyNotFoundException: Boto3ClientError
    PolicyTypeNotFoundException: Boto3ClientError
    SubnetNotFoundException: Boto3ClientError
    TooManyAccessPointsException: Boto3ClientError
    TooManyPoliciesException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    UnsupportedProtocolException: Boto3ClientError
