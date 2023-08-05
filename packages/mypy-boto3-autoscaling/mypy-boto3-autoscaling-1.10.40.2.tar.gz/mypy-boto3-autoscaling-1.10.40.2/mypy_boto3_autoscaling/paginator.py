"Main interface for autoscaling service Paginators"
from __future__ import annotations

from datetime import datetime
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_autoscaling.type_defs import (
    ActivitiesTypeTypeDef,
    AutoScalingGroupsTypeTypeDef,
    AutoScalingInstancesTypeTypeDef,
    DescribeLoadBalancerTargetGroupsResponseTypeDef,
    DescribeLoadBalancersResponseTypeDef,
    DescribeNotificationConfigurationsAnswerTypeDef,
    FilterTypeDef,
    LaunchConfigurationsTypeTypeDef,
    PaginatorConfigTypeDef,
    PoliciesTypeTypeDef,
    ScheduledActionsTypeTypeDef,
    TagsTypeTypeDef,
)


__all__ = (
    "DescribeAutoScalingGroupsPaginator",
    "DescribeAutoScalingInstancesPaginator",
    "DescribeLaunchConfigurationsPaginator",
    "DescribeLoadBalancerTargetGroupsPaginator",
    "DescribeLoadBalancersPaginator",
    "DescribeNotificationConfigurationsPaginator",
    "DescribePoliciesPaginator",
    "DescribeScalingActivitiesPaginator",
    "DescribeScheduledActionsPaginator",
    "DescribeTagsPaginator",
)


class DescribeAutoScalingGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAutoScalingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoScalingGroupNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[AutoScalingGroupsTypeTypeDef, None, None]:
        """
        [DescribeAutoScalingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingGroups.paginate)
        """


class DescribeAutoScalingInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAutoScalingInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, InstanceIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[AutoScalingInstancesTypeTypeDef, None, None]:
        """
        [DescribeAutoScalingInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingInstances.paginate)
        """


class DescribeLaunchConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLaunchConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLaunchConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LaunchConfigurationNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[LaunchConfigurationsTypeTypeDef, None, None]:
        """
        [DescribeLaunchConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLaunchConfigurations.paginate)
        """


class DescribeLoadBalancerTargetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLoadBalancerTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, AutoScalingGroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeLoadBalancerTargetGroupsResponseTypeDef, None, None]:
        """
        [DescribeLoadBalancerTargetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups.paginate)
        """


class DescribeLoadBalancersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, AutoScalingGroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeLoadBalancersResponseTypeDef, None, None]:
        """
        [DescribeLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancers.paginate)
        """


class DescribeNotificationConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNotificationConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeNotificationConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoScalingGroupNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeNotificationConfigurationsAnswerTypeDef, None, None]:
        """
        [DescribeNotificationConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeNotificationConfigurations.paginate)
        """


class DescribePoliciesPaginator(Boto3Paginator):
    """
    [Paginator.DescribePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribePolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoScalingGroupName: str = None,
        PolicyNames: List[str] = None,
        PolicyTypes: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[PoliciesTypeTypeDef, None, None]:
        """
        [DescribePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribePolicies.paginate)
        """


class DescribeScalingActivitiesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalingActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScalingActivities)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ActivityIds: List[str] = None,
        AutoScalingGroupName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ActivitiesTypeTypeDef, None, None]:
        """
        [DescribeScalingActivities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScalingActivities.paginate)
        """


class DescribeScheduledActionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScheduledActions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutoScalingGroupName: str = None,
        ScheduledActionNames: List[str] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ScheduledActionsTypeTypeDef, None, None]:
        """
        [DescribeScheduledActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScheduledActions.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeTags)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[TagsTypeTypeDef, None, None]:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeTags.paginate)
        """
