"Main interface for application-autoscaling service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_application_autoscaling.type_defs import (
    DescribeScalableTargetsResponseTypeDef,
    DescribeScalingActivitiesResponseTypeDef,
    DescribeScalingPoliciesResponseTypeDef,
    DescribeScheduledActionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeScalableTargetsPaginator",
    "DescribeScalingActivitiesPaginator",
    "DescribeScalingPoliciesPaginator",
    "DescribeScheduledActionsPaginator",
)


class DescribeScalableTargetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalableTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalableTargets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ResourceIds: List[str] = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeScalableTargetsResponseTypeDef, None, None]:
        """
        [DescribeScalableTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalableTargets.paginate)
        """


class DescribeScalingActivitiesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalingActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingActivities)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ResourceId: str = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeScalingActivitiesResponseTypeDef, None, None]:
        """
        [DescribeScalingActivities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingActivities.paginate)
        """


class DescribeScalingPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalingPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        PolicyNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeScalingPoliciesResponseTypeDef, None, None]:
        """
        [DescribeScalingPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScalingPolicies.paginate)
        """


class DescribeScheduledActionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScheduledActions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ScheduledActionNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeScheduledActionsResponseTypeDef, None, None]:
        """
        [DescribeScheduledActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/application-autoscaling.html#ApplicationAutoScaling.Paginator.DescribeScheduledActions.paginate)
        """
