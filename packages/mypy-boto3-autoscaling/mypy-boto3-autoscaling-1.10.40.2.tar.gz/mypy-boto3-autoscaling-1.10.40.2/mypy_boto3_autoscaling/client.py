"Main interface for autoscaling service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_autoscaling.client as client_scope

# pylint: disable=import-self
import mypy_boto3_autoscaling.paginator as paginator_scope
from mypy_boto3_autoscaling.type_defs import (
    ActivitiesTypeTypeDef,
    ActivityTypeTypeDef,
    AutoScalingGroupsTypeTypeDef,
    AutoScalingInstancesTypeTypeDef,
    BatchDeleteScheduledActionAnswerTypeDef,
    BatchPutScheduledUpdateGroupActionAnswerTypeDef,
    BlockDeviceMappingTypeDef,
    DescribeAccountLimitsAnswerTypeDef,
    DescribeAdjustmentTypesAnswerTypeDef,
    DescribeAutoScalingNotificationTypesAnswerTypeDef,
    DescribeLifecycleHookTypesAnswerTypeDef,
    DescribeLifecycleHooksAnswerTypeDef,
    DescribeLoadBalancerTargetGroupsResponseTypeDef,
    DescribeLoadBalancersResponseTypeDef,
    DescribeMetricCollectionTypesAnswerTypeDef,
    DescribeNotificationConfigurationsAnswerTypeDef,
    DescribeTerminationPolicyTypesAnswerTypeDef,
    DetachInstancesAnswerTypeDef,
    EnterStandbyAnswerTypeDef,
    ExitStandbyAnswerTypeDef,
    FilterTypeDef,
    InstanceMonitoringTypeDef,
    LaunchConfigurationsTypeTypeDef,
    LaunchTemplateSpecificationTypeDef,
    LifecycleHookSpecificationTypeDef,
    MixedInstancesPolicyTypeDef,
    PoliciesTypeTypeDef,
    PolicyARNTypeTypeDef,
    ProcessesTypeTypeDef,
    ScheduledActionsTypeTypeDef,
    ScheduledUpdateGroupActionRequestTypeDef,
    StepAdjustmentTypeDef,
    TagTypeDef,
    TagsTypeTypeDef,
    TargetTrackingConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AutoScalingClient",)


class AutoScalingClient(BaseClient):
    """
    [AutoScaling.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_instances(self, AutoScalingGroupName: str, InstanceIds: List[str] = None) -> None:
        """
        [Client.attach_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.attach_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_load_balancer_target_groups(
        self, AutoScalingGroupName: str, TargetGroupARNs: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.attach_load_balancer_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.attach_load_balancer_target_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_load_balancers(
        self, AutoScalingGroupName: str, LoadBalancerNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.attach_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.attach_load_balancers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_scheduled_action(
        self, AutoScalingGroupName: str, ScheduledActionNames: List[str]
    ) -> BatchDeleteScheduledActionAnswerTypeDef:
        """
        [Client.batch_delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.batch_delete_scheduled_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_put_scheduled_update_group_action(
        self,
        AutoScalingGroupName: str,
        ScheduledUpdateGroupActions: List[ScheduledUpdateGroupActionRequestTypeDef],
    ) -> BatchPutScheduledUpdateGroupActionAnswerTypeDef:
        """
        [Client.batch_put_scheduled_update_group_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.batch_put_scheduled_update_group_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def complete_lifecycle_action(
        self,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleActionResult: str,
        LifecycleActionToken: str = None,
        InstanceId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.complete_lifecycle_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.complete_lifecycle_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_auto_scaling_group(
        self,
        AutoScalingGroupName: str,
        MinSize: int,
        MaxSize: int,
        LaunchConfigurationName: str = None,
        LaunchTemplate: LaunchTemplateSpecificationTypeDef = None,
        MixedInstancesPolicy: MixedInstancesPolicyTypeDef = None,
        InstanceId: str = None,
        DesiredCapacity: int = None,
        DefaultCooldown: int = None,
        AvailabilityZones: List[str] = None,
        LoadBalancerNames: List[str] = None,
        TargetGroupARNs: List[str] = None,
        HealthCheckType: str = None,
        HealthCheckGracePeriod: int = None,
        PlacementGroup: str = None,
        VPCZoneIdentifier: str = None,
        TerminationPolicies: List[str] = None,
        NewInstancesProtectedFromScaleIn: bool = None,
        LifecycleHookSpecificationList: List[LifecycleHookSpecificationTypeDef] = None,
        Tags: List[TagTypeDef] = None,
        ServiceLinkedRoleARN: str = None,
        MaxInstanceLifetime: int = None,
    ) -> None:
        """
        [Client.create_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.create_auto_scaling_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_launch_configuration(
        self,
        LaunchConfigurationName: str,
        ImageId: str = None,
        KeyName: str = None,
        SecurityGroups: List[str] = None,
        ClassicLinkVPCId: str = None,
        ClassicLinkVPCSecurityGroups: List[str] = None,
        UserData: str = None,
        InstanceId: str = None,
        InstanceType: str = None,
        KernelId: str = None,
        RamdiskId: str = None,
        BlockDeviceMappings: List[BlockDeviceMappingTypeDef] = None,
        InstanceMonitoring: InstanceMonitoringTypeDef = None,
        SpotPrice: str = None,
        IamInstanceProfile: str = None,
        EbsOptimized: bool = None,
        AssociatePublicIpAddress: bool = None,
        PlacementTenancy: str = None,
    ) -> None:
        """
        [Client.create_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.create_launch_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_or_update_tags(self, Tags: List[TagTypeDef]) -> None:
        """
        [Client.create_or_update_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.create_or_update_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_auto_scaling_group(
        self, AutoScalingGroupName: str, ForceDelete: bool = None
    ) -> None:
        """
        [Client.delete_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.delete_auto_scaling_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_launch_configuration(self, LaunchConfigurationName: str) -> None:
        """
        [Client.delete_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.delete_launch_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_lifecycle_hook(
        self, LifecycleHookName: str, AutoScalingGroupName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_lifecycle_hook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.delete_lifecycle_hook)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_notification_configuration(self, AutoScalingGroupName: str, TopicARN: str) -> None:
        """
        [Client.delete_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.delete_notification_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_policy(self, PolicyName: str, AutoScalingGroupName: str = None) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.delete_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_scheduled_action(self, AutoScalingGroupName: str, ScheduledActionName: str) -> None:
        """
        [Client.delete_scheduled_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.delete_scheduled_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tags(self, Tags: List[TagTypeDef]) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.delete_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_limits(self) -> DescribeAccountLimitsAnswerTypeDef:
        """
        [Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_account_limits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_adjustment_types(self) -> DescribeAdjustmentTypesAnswerTypeDef:
        """
        [Client.describe_adjustment_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_adjustment_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_auto_scaling_groups(
        self, AutoScalingGroupNames: List[str] = None, NextToken: str = None, MaxRecords: int = None
    ) -> AutoScalingGroupsTypeTypeDef:
        """
        [Client.describe_auto_scaling_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_auto_scaling_instances(
        self, InstanceIds: List[str] = None, MaxRecords: int = None, NextToken: str = None
    ) -> AutoScalingInstancesTypeTypeDef:
        """
        [Client.describe_auto_scaling_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_auto_scaling_notification_types(
        self,
    ) -> DescribeAutoScalingNotificationTypesAnswerTypeDef:
        """
        [Client.describe_auto_scaling_notification_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_auto_scaling_notification_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_launch_configurations(
        self,
        LaunchConfigurationNames: List[str] = None,
        NextToken: str = None,
        MaxRecords: int = None,
    ) -> LaunchConfigurationsTypeTypeDef:
        """
        [Client.describe_launch_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_launch_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_lifecycle_hook_types(self) -> DescribeLifecycleHookTypesAnswerTypeDef:
        """
        [Client.describe_lifecycle_hook_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_lifecycle_hook_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_lifecycle_hooks(
        self, AutoScalingGroupName: str, LifecycleHookNames: List[str] = None
    ) -> DescribeLifecycleHooksAnswerTypeDef:
        """
        [Client.describe_lifecycle_hooks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_lifecycle_hooks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_load_balancer_target_groups(
        self, AutoScalingGroupName: str, NextToken: str = None, MaxRecords: int = None
    ) -> DescribeLoadBalancerTargetGroupsResponseTypeDef:
        """
        [Client.describe_load_balancer_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_load_balancer_target_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_load_balancers(
        self, AutoScalingGroupName: str, NextToken: str = None, MaxRecords: int = None
    ) -> DescribeLoadBalancersResponseTypeDef:
        """
        [Client.describe_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_load_balancers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_metric_collection_types(self) -> DescribeMetricCollectionTypesAnswerTypeDef:
        """
        [Client.describe_metric_collection_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_metric_collection_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_notification_configurations(
        self, AutoScalingGroupNames: List[str] = None, NextToken: str = None, MaxRecords: int = None
    ) -> DescribeNotificationConfigurationsAnswerTypeDef:
        """
        [Client.describe_notification_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_notification_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_policies(
        self,
        AutoScalingGroupName: str = None,
        PolicyNames: List[str] = None,
        PolicyTypes: List[str] = None,
        NextToken: str = None,
        MaxRecords: int = None,
    ) -> PoliciesTypeTypeDef:
        """
        [Client.describe_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scaling_activities(
        self,
        ActivityIds: List[str] = None,
        AutoScalingGroupName: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ActivitiesTypeTypeDef:
        """
        [Client.describe_scaling_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_scaling_activities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scaling_process_types(self) -> ProcessesTypeTypeDef:
        """
        [Client.describe_scaling_process_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_scaling_process_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scheduled_actions(
        self,
        AutoScalingGroupName: str = None,
        ScheduledActionNames: List[str] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        NextToken: str = None,
        MaxRecords: int = None,
    ) -> ScheduledActionsTypeTypeDef:
        """
        [Client.describe_scheduled_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_scheduled_actions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tags(
        self, Filters: List[FilterTypeDef] = None, NextToken: str = None, MaxRecords: int = None
    ) -> TagsTypeTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_termination_policy_types(self) -> DescribeTerminationPolicyTypesAnswerTypeDef:
        """
        [Client.describe_termination_policy_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.describe_termination_policy_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_instances(
        self,
        AutoScalingGroupName: str,
        ShouldDecrementDesiredCapacity: bool,
        InstanceIds: List[str] = None,
    ) -> DetachInstancesAnswerTypeDef:
        """
        [Client.detach_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.detach_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_load_balancer_target_groups(
        self, AutoScalingGroupName: str, TargetGroupARNs: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.detach_load_balancer_target_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.detach_load_balancer_target_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_load_balancers(
        self, AutoScalingGroupName: str, LoadBalancerNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.detach_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.detach_load_balancers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_metrics_collection(
        self, AutoScalingGroupName: str, Metrics: List[str] = None
    ) -> None:
        """
        [Client.disable_metrics_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.disable_metrics_collection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_metrics_collection(
        self, AutoScalingGroupName: str, Granularity: str, Metrics: List[str] = None
    ) -> None:
        """
        [Client.enable_metrics_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.enable_metrics_collection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enter_standby(
        self,
        AutoScalingGroupName: str,
        ShouldDecrementDesiredCapacity: bool,
        InstanceIds: List[str] = None,
    ) -> EnterStandbyAnswerTypeDef:
        """
        [Client.enter_standby documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.enter_standby)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def execute_policy(
        self,
        PolicyName: str,
        AutoScalingGroupName: str = None,
        HonorCooldown: bool = None,
        MetricValue: float = None,
        BreachThreshold: float = None,
    ) -> None:
        """
        [Client.execute_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.execute_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def exit_standby(
        self, AutoScalingGroupName: str, InstanceIds: List[str] = None
    ) -> ExitStandbyAnswerTypeDef:
        """
        [Client.exit_standby documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.exit_standby)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_lifecycle_hook(
        self,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleTransition: str = None,
        RoleARN: str = None,
        NotificationTargetARN: str = None,
        NotificationMetadata: str = None,
        HeartbeatTimeout: int = None,
        DefaultResult: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_lifecycle_hook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.put_lifecycle_hook)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_notification_configuration(
        self, AutoScalingGroupName: str, TopicARN: str, NotificationTypes: List[str]
    ) -> None:
        """
        [Client.put_notification_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.put_notification_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_scaling_policy(
        self,
        AutoScalingGroupName: str,
        PolicyName: str,
        PolicyType: str = None,
        AdjustmentType: str = None,
        MinAdjustmentStep: int = None,
        MinAdjustmentMagnitude: int = None,
        ScalingAdjustment: int = None,
        Cooldown: int = None,
        MetricAggregationType: str = None,
        StepAdjustments: List[StepAdjustmentTypeDef] = None,
        EstimatedInstanceWarmup: int = None,
        TargetTrackingConfiguration: TargetTrackingConfigurationTypeDef = None,
    ) -> PolicyARNTypeTypeDef:
        """
        [Client.put_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.put_scaling_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_scheduled_update_group_action(
        self,
        AutoScalingGroupName: str,
        ScheduledActionName: str,
        Time: datetime = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Recurrence: str = None,
        MinSize: int = None,
        MaxSize: int = None,
        DesiredCapacity: int = None,
    ) -> None:
        """
        [Client.put_scheduled_update_group_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.put_scheduled_update_group_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def record_lifecycle_action_heartbeat(
        self,
        LifecycleHookName: str,
        AutoScalingGroupName: str,
        LifecycleActionToken: str = None,
        InstanceId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.record_lifecycle_action_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.record_lifecycle_action_heartbeat)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resume_processes(
        self, AutoScalingGroupName: str, ScalingProcesses: List[str] = None
    ) -> None:
        """
        [Client.resume_processes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.resume_processes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_desired_capacity(
        self, AutoScalingGroupName: str, DesiredCapacity: int, HonorCooldown: bool = None
    ) -> None:
        """
        [Client.set_desired_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.set_desired_capacity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_instance_health(
        self, InstanceId: str, HealthStatus: str, ShouldRespectGracePeriod: bool = None
    ) -> None:
        """
        [Client.set_instance_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.set_instance_health)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_instance_protection(
        self, InstanceIds: List[str], AutoScalingGroupName: str, ProtectedFromScaleIn: bool
    ) -> Dict[str, Any]:
        """
        [Client.set_instance_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.set_instance_protection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def suspend_processes(
        self, AutoScalingGroupName: str, ScalingProcesses: List[str] = None
    ) -> None:
        """
        [Client.suspend_processes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.suspend_processes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate_instance_in_auto_scaling_group(
        self, InstanceId: str, ShouldDecrementDesiredCapacity: bool
    ) -> ActivityTypeTypeDef:
        """
        [Client.terminate_instance_in_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.terminate_instance_in_auto_scaling_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_auto_scaling_group(
        self,
        AutoScalingGroupName: str,
        LaunchConfigurationName: str = None,
        LaunchTemplate: LaunchTemplateSpecificationTypeDef = None,
        MixedInstancesPolicy: MixedInstancesPolicyTypeDef = None,
        MinSize: int = None,
        MaxSize: int = None,
        DesiredCapacity: int = None,
        DefaultCooldown: int = None,
        AvailabilityZones: List[str] = None,
        HealthCheckType: str = None,
        HealthCheckGracePeriod: int = None,
        PlacementGroup: str = None,
        VPCZoneIdentifier: str = None,
        TerminationPolicies: List[str] = None,
        NewInstancesProtectedFromScaleIn: bool = None,
        ServiceLinkedRoleARN: str = None,
        MaxInstanceLifetime: int = None,
    ) -> None:
        """
        [Client.update_auto_scaling_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Client.update_auto_scaling_group)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_auto_scaling_groups"]
    ) -> paginator_scope.DescribeAutoScalingGroupsPaginator:
        """
        [Paginator.DescribeAutoScalingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_auto_scaling_instances"]
    ) -> paginator_scope.DescribeAutoScalingInstancesPaginator:
        """
        [Paginator.DescribeAutoScalingInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_launch_configurations"]
    ) -> paginator_scope.DescribeLaunchConfigurationsPaginator:
        """
        [Paginator.DescribeLaunchConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLaunchConfigurations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_load_balancer_target_groups"]
    ) -> paginator_scope.DescribeLoadBalancerTargetGroupsPaginator:
        """
        [Paginator.DescribeLoadBalancerTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_load_balancers"]
    ) -> paginator_scope.DescribeLoadBalancersPaginator:
        """
        [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_notification_configurations"]
    ) -> paginator_scope.DescribeNotificationConfigurationsPaginator:
        """
        [Paginator.DescribeNotificationConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeNotificationConfigurations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_policies"]
    ) -> paginator_scope.DescribePoliciesPaginator:
        """
        [Paginator.DescribePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribePolicies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_scaling_activities"]
    ) -> paginator_scope.DescribeScalingActivitiesPaginator:
        """
        [Paginator.DescribeScalingActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScalingActivities)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> paginator_scope.DescribeScheduledActionsPaginator:
        """
        [Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScheduledActions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_tags"]
    ) -> paginator_scope.DescribeTagsPaginator:
        """
        [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeTags)
        """


class Exceptions:
    AlreadyExistsFault: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidNextToken: Boto3ClientError
    LimitExceededFault: Boto3ClientError
    ResourceContentionFault: Boto3ClientError
    ResourceInUseFault: Boto3ClientError
    ScalingActivityInProgressFault: Boto3ClientError
    ServiceLinkedRoleFailure: Boto3ClientError
