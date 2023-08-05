"Main interface for elb service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_elb.type_defs import InstanceTypeDef, WaiterConfigTypeDef


__all__ = ("AnyInstanceInServiceWaiter", "InstanceDeregisteredWaiter", "InstanceInServiceWaiter")


class AnyInstanceInServiceWaiter(Boto3Waiter):
    """
    [Waiter.AnyInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elb.html#ElasticLoadBalancing.Waiter.AnyInstanceInService)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List[InstanceTypeDef] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [AnyInstanceInService.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elb.html#ElasticLoadBalancing.Waiter.AnyInstanceInService.wait)
        """


class InstanceDeregisteredWaiter(Boto3Waiter):
    """
    [Waiter.InstanceDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceDeregistered)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List[InstanceTypeDef] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceDeregistered.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceDeregistered.wait)
        """


class InstanceInServiceWaiter(Boto3Waiter):
    """
    [Waiter.InstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceInService)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerName: str,
        Instances: List[InstanceTypeDef] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceInService.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceInService.wait)
        """
