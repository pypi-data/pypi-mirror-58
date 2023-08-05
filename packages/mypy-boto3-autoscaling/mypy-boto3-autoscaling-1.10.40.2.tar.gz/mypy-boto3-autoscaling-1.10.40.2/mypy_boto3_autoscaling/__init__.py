"Main interface for autoscaling service"
from mypy_boto3_autoscaling.client import AutoScalingClient as Client, AutoScalingClient
from mypy_boto3_autoscaling.paginator import (
    DescribeAutoScalingGroupsPaginator,
    DescribeAutoScalingInstancesPaginator,
    DescribeLaunchConfigurationsPaginator,
    DescribeLoadBalancerTargetGroupsPaginator,
    DescribeLoadBalancersPaginator,
    DescribeNotificationConfigurationsPaginator,
    DescribePoliciesPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScheduledActionsPaginator,
    DescribeTagsPaginator,
)


__all__ = (
    "AutoScalingClient",
    "Client",
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
