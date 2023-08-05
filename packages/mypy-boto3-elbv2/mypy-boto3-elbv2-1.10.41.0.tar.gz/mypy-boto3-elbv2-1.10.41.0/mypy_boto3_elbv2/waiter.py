"Main interface for elbv2 service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_elbv2.type_defs import TargetDescriptionTypeDef, WaiterConfigTypeDef


__all__ = (
    "LoadBalancerAvailableWaiter",
    "LoadBalancerExistsWaiter",
    "LoadBalancersDeletedWaiter",
    "TargetDeregisteredWaiter",
    "TargetInServiceWaiter",
)


class LoadBalancerAvailableWaiter(Boto3Waiter):
    """
    [Waiter.LoadBalancerAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [LoadBalancerAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerAvailable.wait)
        """


class LoadBalancerExistsWaiter(Boto3Waiter):
    """
    [Waiter.LoadBalancerExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [LoadBalancerExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancerExists.wait)
        """


class LoadBalancersDeletedWaiter(Boto3Waiter):
    """
    [Waiter.LoadBalancersDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancersDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [LoadBalancersDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.LoadBalancersDeleted.wait)
        """


class TargetDeregisteredWaiter(Boto3Waiter):
    """
    [Waiter.TargetDeregistered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetDeregistered)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        TargetGroupArn: str,
        Targets: List[TargetDescriptionTypeDef] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [TargetDeregistered.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetDeregistered.wait)
        """


class TargetInServiceWaiter(Boto3Waiter):
    """
    [Waiter.TargetInService documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetInService)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        TargetGroupArn: str,
        Targets: List[TargetDescriptionTypeDef] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [TargetInService.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/elbv2.html#ElasticLoadBalancingv2.Waiter.TargetInService.wait)
        """
