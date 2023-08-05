"Main interface for autoscaling-plans service"
from mypy_boto3_autoscaling_plans.client import (
    AutoScalingPlansClient as Client,
    AutoScalingPlansClient,
)
from mypy_boto3_autoscaling_plans.paginator import (
    DescribeScalingPlanResourcesPaginator,
    DescribeScalingPlansPaginator,
)


__all__ = (
    "AutoScalingPlansClient",
    "Client",
    "DescribeScalingPlanResourcesPaginator",
    "DescribeScalingPlansPaginator",
)
