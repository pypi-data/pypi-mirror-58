"Main interface for gamelift service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_gamelift.type_defs import (
    DescribeFleetAttributesOutputTypeDef,
    DescribeFleetCapacityOutputTypeDef,
    DescribeFleetEventsOutputTypeDef,
    DescribeFleetUtilizationOutputTypeDef,
    DescribeGameSessionDetailsOutputTypeDef,
    DescribeGameSessionQueuesOutputTypeDef,
    DescribeGameSessionsOutputTypeDef,
    DescribeInstancesOutputTypeDef,
    DescribeMatchmakingConfigurationsOutputTypeDef,
    DescribeMatchmakingRuleSetsOutputTypeDef,
    DescribePlayerSessionsOutputTypeDef,
    DescribeScalingPoliciesOutputTypeDef,
    ListAliasesOutputTypeDef,
    ListBuildsOutputTypeDef,
    ListFleetsOutputTypeDef,
    PaginatorConfigTypeDef,
    SearchGameSessionsOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeFleetAttributesPaginator",
    "DescribeFleetCapacityPaginator",
    "DescribeFleetEventsPaginator",
    "DescribeFleetUtilizationPaginator",
    "DescribeGameSessionDetailsPaginator",
    "DescribeGameSessionQueuesPaginator",
    "DescribeGameSessionsPaginator",
    "DescribeInstancesPaginator",
    "DescribeMatchmakingConfigurationsPaginator",
    "DescribeMatchmakingRuleSetsPaginator",
    "DescribePlayerSessionsPaginator",
    "DescribeScalingPoliciesPaginator",
    "ListAliasesPaginator",
    "ListBuildsPaginator",
    "ListFleetsPaginator",
    "SearchGameSessionsPaginator",
)


class DescribeFleetAttributesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFleetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetAttributes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, FleetIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeFleetAttributesOutputTypeDef, None, None]:
        """
        [DescribeFleetAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetAttributes.paginate)
        """


class DescribeFleetCapacityPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFleetCapacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetCapacity)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, FleetIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeFleetCapacityOutputTypeDef, None, None]:
        """
        [DescribeFleetCapacity.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetCapacity.paginate)
        """


class DescribeFleetEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFleetEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetId: str,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeFleetEventsOutputTypeDef, None, None]:
        """
        [DescribeFleetEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetEvents.paginate)
        """


class DescribeFleetUtilizationPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFleetUtilization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetUtilization)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, FleetIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeFleetUtilizationOutputTypeDef, None, None]:
        """
        [DescribeFleetUtilization.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetUtilization.paginate)
        """


class DescribeGameSessionDetailsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeGameSessionDetails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionDetails)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        StatusFilter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeGameSessionDetailsOutputTypeDef, None, None]:
        """
        [DescribeGameSessionDetails.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionDetails.paginate)
        """


class DescribeGameSessionQueuesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeGameSessionQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionQueues)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeGameSessionQueuesOutputTypeDef, None, None]:
        """
        [DescribeGameSessionQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionQueues.paginate)
        """


class DescribeGameSessionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeGameSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        StatusFilter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeGameSessionsOutputTypeDef, None, None]:
        """
        [DescribeGameSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessions.paginate)
        """


class DescribeInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, FleetId: str, InstanceId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeInstancesOutputTypeDef, None, None]:
        """
        [DescribeInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeInstances.paginate)
        """


class DescribeMatchmakingConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMatchmakingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Names: List[str] = None,
        RuleSetName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMatchmakingConfigurationsOutputTypeDef, None, None]:
        """
        [DescribeMatchmakingConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingConfigurations.paginate)
        """


class DescribeMatchmakingRuleSetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMatchmakingRuleSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingRuleSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Names: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeMatchmakingRuleSetsOutputTypeDef, None, None]:
        """
        [DescribeMatchmakingRuleSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingRuleSets.paginate)
        """


class DescribePlayerSessionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePlayerSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribePlayerSessions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GameSessionId: str = None,
        PlayerId: str = None,
        PlayerSessionId: str = None,
        PlayerSessionStatusFilter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribePlayerSessionsOutputTypeDef, None, None]:
        """
        [DescribePlayerSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribePlayerSessions.paginate)
        """


class DescribeScalingPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalingPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeScalingPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetId: str,
        StatusFilter: Literal[
            "ACTIVE",
            "UPDATE_REQUESTED",
            "UPDATING",
            "DELETE_REQUESTED",
            "DELETING",
            "DELETED",
            "ERROR",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeScalingPoliciesOutputTypeDef, None, None]:
        """
        [DescribeScalingPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeScalingPolicies.paginate)
        """


class ListAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.ListAliases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RoutingStrategyType: Literal["SIMPLE", "TERMINAL"] = None,
        Name: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAliasesOutputTypeDef, None, None]:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.ListAliases.paginate)
        """


class ListBuildsPaginator(Boto3Paginator):
    """
    [Paginator.ListBuilds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.ListBuilds)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Status: Literal["INITIALIZED", "READY", "FAILED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListBuildsOutputTypeDef, None, None]:
        """
        [ListBuilds.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.ListBuilds.paginate)
        """


class ListFleetsPaginator(Boto3Paginator):
    """
    [Paginator.ListFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.ListFleets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        BuildId: str = None,
        ScriptId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListFleetsOutputTypeDef, None, None]:
        """
        [ListFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.ListFleets.paginate)
        """


class SearchGameSessionsPaginator(Boto3Paginator):
    """
    [Paginator.SearchGameSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.SearchGameSessions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FleetId: str = None,
        AliasId: str = None,
        FilterExpression: str = None,
        SortExpression: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[SearchGameSessionsOutputTypeDef, None, None]:
        """
        [SearchGameSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.SearchGameSessions.paginate)
        """
