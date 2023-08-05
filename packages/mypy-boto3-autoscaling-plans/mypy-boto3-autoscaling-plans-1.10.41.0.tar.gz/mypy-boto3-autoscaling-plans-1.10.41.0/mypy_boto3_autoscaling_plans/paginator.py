"Main interface for autoscaling-plans service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_autoscaling_plans.type_defs import (
    ApplicationSourceTypeDef,
    DescribeScalingPlanResourcesResponseTypeDef,
    DescribeScalingPlansResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("DescribeScalingPlanResourcesPaginator", "DescribeScalingPlansPaginator")


class DescribeScalingPlanResourcesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalingPlanResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeScalingPlanResourcesResponseTypeDef, None, None]:
        """
        [DescribeScalingPlanResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources.paginate)
        """


class DescribeScalingPlansPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalingPlans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ScalingPlanNames: List[str] = None,
        ScalingPlanVersion: int = None,
        ApplicationSources: List[ApplicationSourceTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeScalingPlansResponseTypeDef, None, None]:
        """
        [DescribeScalingPlans.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans.paginate)
        """
