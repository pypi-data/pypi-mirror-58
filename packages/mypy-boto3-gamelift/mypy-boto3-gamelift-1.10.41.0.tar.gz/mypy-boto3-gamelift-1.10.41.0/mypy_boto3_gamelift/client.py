"Main interface for gamelift service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, IO, List, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_gamelift.client as client_scope

# pylint: disable=import-self
import mypy_boto3_gamelift.paginator as paginator_scope
from mypy_boto3_gamelift.type_defs import (
    CertificateConfigurationTypeDef,
    CreateAliasOutputTypeDef,
    CreateBuildOutputTypeDef,
    CreateFleetOutputTypeDef,
    CreateGameSessionOutputTypeDef,
    CreateGameSessionQueueOutputTypeDef,
    CreateMatchmakingConfigurationOutputTypeDef,
    CreateMatchmakingRuleSetOutputTypeDef,
    CreatePlayerSessionOutputTypeDef,
    CreatePlayerSessionsOutputTypeDef,
    CreateScriptOutputTypeDef,
    CreateVpcPeeringAuthorizationOutputTypeDef,
    DescribeAliasOutputTypeDef,
    DescribeBuildOutputTypeDef,
    DescribeEC2InstanceLimitsOutputTypeDef,
    DescribeFleetAttributesOutputTypeDef,
    DescribeFleetCapacityOutputTypeDef,
    DescribeFleetEventsOutputTypeDef,
    DescribeFleetPortSettingsOutputTypeDef,
    DescribeFleetUtilizationOutputTypeDef,
    DescribeGameSessionDetailsOutputTypeDef,
    DescribeGameSessionPlacementOutputTypeDef,
    DescribeGameSessionQueuesOutputTypeDef,
    DescribeGameSessionsOutputTypeDef,
    DescribeInstancesOutputTypeDef,
    DescribeMatchmakingConfigurationsOutputTypeDef,
    DescribeMatchmakingOutputTypeDef,
    DescribeMatchmakingRuleSetsOutputTypeDef,
    DescribePlayerSessionsOutputTypeDef,
    DescribeRuntimeConfigurationOutputTypeDef,
    DescribeScalingPoliciesOutputTypeDef,
    DescribeScriptOutputTypeDef,
    DescribeVpcPeeringAuthorizationsOutputTypeDef,
    DescribeVpcPeeringConnectionsOutputTypeDef,
    DesiredPlayerSessionTypeDef,
    GamePropertyTypeDef,
    GameSessionQueueDestinationTypeDef,
    GetGameSessionLogUrlOutputTypeDef,
    GetInstanceAccessOutputTypeDef,
    IpPermissionTypeDef,
    ListAliasesOutputTypeDef,
    ListBuildsOutputTypeDef,
    ListFleetsOutputTypeDef,
    ListScriptsOutputTypeDef,
    PlayerLatencyPolicyTypeDef,
    PlayerLatencyTypeDef,
    PlayerTypeDef,
    PutScalingPolicyOutputTypeDef,
    RequestUploadCredentialsOutputTypeDef,
    ResolveAliasOutputTypeDef,
    ResourceCreationLimitPolicyTypeDef,
    RoutingStrategyTypeDef,
    RuntimeConfigurationTypeDef,
    S3LocationTypeDef,
    SearchGameSessionsOutputTypeDef,
    StartGameSessionPlacementOutputTypeDef,
    StartMatchBackfillOutputTypeDef,
    StartMatchmakingOutputTypeDef,
    StopGameSessionPlacementOutputTypeDef,
    TargetConfigurationTypeDef,
    UpdateAliasOutputTypeDef,
    UpdateBuildOutputTypeDef,
    UpdateFleetAttributesOutputTypeDef,
    UpdateFleetCapacityOutputTypeDef,
    UpdateFleetPortSettingsOutputTypeDef,
    UpdateGameSessionOutputTypeDef,
    UpdateGameSessionQueueOutputTypeDef,
    UpdateMatchmakingConfigurationOutputTypeDef,
    UpdateRuntimeConfigurationOutputTypeDef,
    UpdateScriptOutputTypeDef,
    ValidateMatchmakingRuleSetOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GameLiftClient",)


class GameLiftClient(BaseClient):
    """
    [GameLift.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_match(
        self, TicketId: str, PlayerIds: List[str], AcceptanceType: Literal["ACCEPT", "REJECT"]
    ) -> Dict[str, Any]:
        """
        [Client.accept_match documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.accept_match)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_alias(
        self, Name: str, RoutingStrategy: RoutingStrategyTypeDef, Description: str = None
    ) -> CreateAliasOutputTypeDef:
        """
        [Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_build(
        self,
        Name: str = None,
        Version: str = None,
        StorageLocation: S3LocationTypeDef = None,
        OperatingSystem: Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"] = None,
    ) -> CreateBuildOutputTypeDef:
        """
        [Client.create_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_build)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_fleet(
        self,
        Name: str,
        EC2InstanceType: Literal[
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
        ],
        Description: str = None,
        BuildId: str = None,
        ScriptId: str = None,
        ServerLaunchPath: str = None,
        ServerLaunchParameters: str = None,
        LogPaths: List[str] = None,
        EC2InboundPermissions: List[IpPermissionTypeDef] = None,
        NewGameSessionProtectionPolicy: Literal["NoProtection", "FullProtection"] = None,
        RuntimeConfiguration: RuntimeConfigurationTypeDef = None,
        ResourceCreationLimitPolicy: ResourceCreationLimitPolicyTypeDef = None,
        MetricGroups: List[str] = None,
        PeerVpcAwsAccountId: str = None,
        PeerVpcId: str = None,
        FleetType: Literal["ON_DEMAND", "SPOT"] = None,
        InstanceRoleArn: str = None,
        CertificateConfiguration: CertificateConfigurationTypeDef = None,
    ) -> CreateFleetOutputTypeDef:
        """
        [Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_game_session(
        self,
        MaximumPlayerSessionCount: int,
        FleetId: str = None,
        AliasId: str = None,
        Name: str = None,
        GameProperties: List[GamePropertyTypeDef] = None,
        CreatorId: str = None,
        GameSessionId: str = None,
        IdempotencyToken: str = None,
        GameSessionData: str = None,
    ) -> CreateGameSessionOutputTypeDef:
        """
        [Client.create_game_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_game_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_game_session_queue(
        self,
        Name: str,
        TimeoutInSeconds: int = None,
        PlayerLatencyPolicies: List[PlayerLatencyPolicyTypeDef] = None,
        Destinations: List[GameSessionQueueDestinationTypeDef] = None,
    ) -> CreateGameSessionQueueOutputTypeDef:
        """
        [Client.create_game_session_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_game_session_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_matchmaking_configuration(
        self,
        Name: str,
        GameSessionQueueArns: List[str],
        RequestTimeoutSeconds: int,
        AcceptanceRequired: bool,
        RuleSetName: str,
        Description: str = None,
        AcceptanceTimeoutSeconds: int = None,
        NotificationTarget: str = None,
        AdditionalPlayerCount: int = None,
        CustomEventData: str = None,
        GameProperties: List[GamePropertyTypeDef] = None,
        GameSessionData: str = None,
        BackfillMode: Literal["AUTOMATIC", "MANUAL"] = None,
    ) -> CreateMatchmakingConfigurationOutputTypeDef:
        """
        [Client.create_matchmaking_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_matchmaking_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_matchmaking_rule_set(
        self, Name: str, RuleSetBody: str
    ) -> CreateMatchmakingRuleSetOutputTypeDef:
        """
        [Client.create_matchmaking_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_matchmaking_rule_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_player_session(
        self, GameSessionId: str, PlayerId: str, PlayerData: str = None
    ) -> CreatePlayerSessionOutputTypeDef:
        """
        [Client.create_player_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_player_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_player_sessions(
        self, GameSessionId: str, PlayerIds: List[str], PlayerDataMap: Dict[str, str] = None
    ) -> CreatePlayerSessionsOutputTypeDef:
        """
        [Client.create_player_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_player_sessions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_script(
        self,
        Name: str = None,
        Version: str = None,
        StorageLocation: S3LocationTypeDef = None,
        ZipFile: Union[bytes, IO] = None,
    ) -> CreateScriptOutputTypeDef:
        """
        [Client.create_script documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_script)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpc_peering_authorization(
        self, GameLiftAwsAccountId: str, PeerVpcId: str
    ) -> CreateVpcPeeringAuthorizationOutputTypeDef:
        """
        [Client.create_vpc_peering_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_vpc_peering_authorization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpc_peering_connection(
        self, FleetId: str, PeerVpcAwsAccountId: str, PeerVpcId: str
    ) -> Dict[str, Any]:
        """
        [Client.create_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.create_vpc_peering_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_alias(self, AliasId: str) -> None:
        """
        [Client.delete_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.delete_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_build(self, BuildId: str) -> None:
        """
        [Client.delete_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.delete_build)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_fleet(self, FleetId: str) -> None:
        """
        [Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.delete_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_game_session_queue(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_game_session_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.delete_game_session_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_matchmaking_configuration(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_matchmaking_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.delete_matchmaking_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_matchmaking_rule_set(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_matchmaking_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.delete_matchmaking_rule_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_scaling_policy(self, Name: str, FleetId: str) -> None:
        """
        [Client.delete_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.delete_scaling_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_script(self, ScriptId: str) -> None:
        """
        [Client.delete_script documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.delete_script)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vpc_peering_authorization(
        self, GameLiftAwsAccountId: str, PeerVpcId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_vpc_peering_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.delete_vpc_peering_authorization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vpc_peering_connection(
        self, FleetId: str, VpcPeeringConnectionId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.delete_vpc_peering_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_alias(self, AliasId: str) -> DescribeAliasOutputTypeDef:
        """
        [Client.describe_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_build(self, BuildId: str) -> DescribeBuildOutputTypeDef:
        """
        [Client.describe_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_build)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_ec2_instance_limits(
        self,
        EC2InstanceType: Literal[
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
        ] = None,
    ) -> DescribeEC2InstanceLimitsOutputTypeDef:
        """
        [Client.describe_ec2_instance_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_ec2_instance_limits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleet_attributes(
        self, FleetIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeFleetAttributesOutputTypeDef:
        """
        [Client.describe_fleet_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_fleet_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleet_capacity(
        self, FleetIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeFleetCapacityOutputTypeDef:
        """
        [Client.describe_fleet_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_fleet_capacity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleet_events(
        self,
        FleetId: str,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeFleetEventsOutputTypeDef:
        """
        [Client.describe_fleet_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_fleet_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleet_port_settings(self, FleetId: str) -> DescribeFleetPortSettingsOutputTypeDef:
        """
        [Client.describe_fleet_port_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_fleet_port_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleet_utilization(
        self, FleetIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeFleetUtilizationOutputTypeDef:
        """
        [Client.describe_fleet_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_fleet_utilization)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_game_session_details(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        StatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeGameSessionDetailsOutputTypeDef:
        """
        [Client.describe_game_session_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_game_session_details)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_game_session_placement(
        self, PlacementId: str
    ) -> DescribeGameSessionPlacementOutputTypeDef:
        """
        [Client.describe_game_session_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_game_session_placement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_game_session_queues(
        self, Names: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeGameSessionQueuesOutputTypeDef:
        """
        [Client.describe_game_session_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_game_session_queues)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_game_sessions(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        StatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeGameSessionsOutputTypeDef:
        """
        [Client.describe_game_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_game_sessions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instances(
        self, FleetId: str, InstanceId: str = None, Limit: int = None, NextToken: str = None
    ) -> DescribeInstancesOutputTypeDef:
        """
        [Client.describe_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_matchmaking(self, TicketIds: List[str]) -> DescribeMatchmakingOutputTypeDef:
        """
        [Client.describe_matchmaking documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_matchmaking)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_matchmaking_configurations(
        self,
        Names: List[str] = None,
        RuleSetName: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeMatchmakingConfigurationsOutputTypeDef:
        """
        [Client.describe_matchmaking_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_matchmaking_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_matchmaking_rule_sets(
        self, Names: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeMatchmakingRuleSetsOutputTypeDef:
        """
        [Client.describe_matchmaking_rule_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_matchmaking_rule_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_player_sessions(
        self,
        GameSessionId: str = None,
        PlayerId: str = None,
        PlayerSessionId: str = None,
        PlayerSessionStatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribePlayerSessionsOutputTypeDef:
        """
        [Client.describe_player_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_player_sessions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_runtime_configuration(
        self, FleetId: str
    ) -> DescribeRuntimeConfigurationOutputTypeDef:
        """
        [Client.describe_runtime_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_runtime_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scaling_policies(
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
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeScalingPoliciesOutputTypeDef:
        """
        [Client.describe_scaling_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_scaling_policies)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_script(self, ScriptId: str) -> DescribeScriptOutputTypeDef:
        """
        [Client.describe_script documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_script)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_peering_authorizations(self) -> DescribeVpcPeeringAuthorizationsOutputTypeDef:
        """
        [Client.describe_vpc_peering_authorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_vpc_peering_authorizations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_peering_connections(
        self, FleetId: str = None
    ) -> DescribeVpcPeeringConnectionsOutputTypeDef:
        """
        [Client.describe_vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.describe_vpc_peering_connections)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_game_session_log_url(self, GameSessionId: str) -> GetGameSessionLogUrlOutputTypeDef:
        """
        [Client.get_game_session_log_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.get_game_session_log_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instance_access(self, FleetId: str, InstanceId: str) -> GetInstanceAccessOutputTypeDef:
        """
        [Client.get_instance_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.get_instance_access)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_aliases(
        self,
        RoutingStrategyType: Literal["SIMPLE", "TERMINAL"] = None,
        Name: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ListAliasesOutputTypeDef:
        """
        [Client.list_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.list_aliases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_builds(
        self,
        Status: Literal["INITIALIZED", "READY", "FAILED"] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ListBuildsOutputTypeDef:
        """
        [Client.list_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.list_builds)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_fleets(
        self, BuildId: str = None, ScriptId: str = None, Limit: int = None, NextToken: str = None
    ) -> ListFleetsOutputTypeDef:
        """
        [Client.list_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.list_fleets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_scripts(self, Limit: int = None, NextToken: str = None) -> ListScriptsOutputTypeDef:
        """
        [Client.list_scripts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.list_scripts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_scaling_policy(
        self,
        Name: str,
        FleetId: str,
        MetricName: Literal[
            "ActivatingGameSessions",
            "ActiveGameSessions",
            "ActiveInstances",
            "AvailableGameSessions",
            "AvailablePlayerSessions",
            "CurrentPlayerSessions",
            "IdleInstances",
            "PercentAvailableGameSessions",
            "PercentIdleInstances",
            "QueueDepth",
            "WaitTime",
        ],
        ScalingAdjustment: int = None,
        ScalingAdjustmentType: Literal[
            "ChangeInCapacity", "ExactCapacity", "PercentChangeInCapacity"
        ] = None,
        Threshold: float = None,
        ComparisonOperator: Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ] = None,
        EvaluationPeriods: int = None,
        PolicyType: Literal["RuleBased", "TargetBased"] = None,
        TargetConfiguration: TargetConfigurationTypeDef = None,
    ) -> PutScalingPolicyOutputTypeDef:
        """
        [Client.put_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.put_scaling_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def request_upload_credentials(self, BuildId: str) -> RequestUploadCredentialsOutputTypeDef:
        """
        [Client.request_upload_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.request_upload_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resolve_alias(self, AliasId: str) -> ResolveAliasOutputTypeDef:
        """
        [Client.resolve_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.resolve_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_game_sessions(
        self,
        FleetId: str = None,
        AliasId: str = None,
        FilterExpression: str = None,
        SortExpression: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> SearchGameSessionsOutputTypeDef:
        """
        [Client.search_game_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.search_game_sessions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_fleet_actions(
        self, FleetId: str, Actions: List[Literal["AUTO_SCALING"]]
    ) -> Dict[str, Any]:
        """
        [Client.start_fleet_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.start_fleet_actions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_game_session_placement(
        self,
        PlacementId: str,
        GameSessionQueueName: str,
        MaximumPlayerSessionCount: int,
        GameProperties: List[GamePropertyTypeDef] = None,
        GameSessionName: str = None,
        PlayerLatencies: List[PlayerLatencyTypeDef] = None,
        DesiredPlayerSessions: List[DesiredPlayerSessionTypeDef] = None,
        GameSessionData: str = None,
    ) -> StartGameSessionPlacementOutputTypeDef:
        """
        [Client.start_game_session_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.start_game_session_placement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_match_backfill(
        self,
        ConfigurationName: str,
        GameSessionArn: str,
        Players: List[PlayerTypeDef],
        TicketId: str = None,
    ) -> StartMatchBackfillOutputTypeDef:
        """
        [Client.start_match_backfill documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.start_match_backfill)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_matchmaking(
        self, ConfigurationName: str, Players: List[PlayerTypeDef], TicketId: str = None
    ) -> StartMatchmakingOutputTypeDef:
        """
        [Client.start_matchmaking documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.start_matchmaking)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_fleet_actions(
        self, FleetId: str, Actions: List[Literal["AUTO_SCALING"]]
    ) -> Dict[str, Any]:
        """
        [Client.stop_fleet_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.stop_fleet_actions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_game_session_placement(
        self, PlacementId: str
    ) -> StopGameSessionPlacementOutputTypeDef:
        """
        [Client.stop_game_session_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.stop_game_session_placement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_matchmaking(self, TicketId: str) -> Dict[str, Any]:
        """
        [Client.stop_matchmaking documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.stop_matchmaking)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_alias(
        self,
        AliasId: str,
        Name: str = None,
        Description: str = None,
        RoutingStrategy: RoutingStrategyTypeDef = None,
    ) -> UpdateAliasOutputTypeDef:
        """
        [Client.update_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.update_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_build(
        self, BuildId: str, Name: str = None, Version: str = None
    ) -> UpdateBuildOutputTypeDef:
        """
        [Client.update_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.update_build)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_fleet_attributes(
        self,
        FleetId: str,
        Name: str = None,
        Description: str = None,
        NewGameSessionProtectionPolicy: Literal["NoProtection", "FullProtection"] = None,
        ResourceCreationLimitPolicy: ResourceCreationLimitPolicyTypeDef = None,
        MetricGroups: List[str] = None,
    ) -> UpdateFleetAttributesOutputTypeDef:
        """
        [Client.update_fleet_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.update_fleet_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_fleet_capacity(
        self, FleetId: str, DesiredInstances: int = None, MinSize: int = None, MaxSize: int = None
    ) -> UpdateFleetCapacityOutputTypeDef:
        """
        [Client.update_fleet_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.update_fleet_capacity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_fleet_port_settings(
        self,
        FleetId: str,
        InboundPermissionAuthorizations: List[IpPermissionTypeDef] = None,
        InboundPermissionRevocations: List[IpPermissionTypeDef] = None,
    ) -> UpdateFleetPortSettingsOutputTypeDef:
        """
        [Client.update_fleet_port_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.update_fleet_port_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_game_session(
        self,
        GameSessionId: str,
        MaximumPlayerSessionCount: int = None,
        Name: str = None,
        PlayerSessionCreationPolicy: Literal["ACCEPT_ALL", "DENY_ALL"] = None,
        ProtectionPolicy: Literal["NoProtection", "FullProtection"] = None,
    ) -> UpdateGameSessionOutputTypeDef:
        """
        [Client.update_game_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.update_game_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_game_session_queue(
        self,
        Name: str,
        TimeoutInSeconds: int = None,
        PlayerLatencyPolicies: List[PlayerLatencyPolicyTypeDef] = None,
        Destinations: List[GameSessionQueueDestinationTypeDef] = None,
    ) -> UpdateGameSessionQueueOutputTypeDef:
        """
        [Client.update_game_session_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.update_game_session_queue)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_matchmaking_configuration(
        self,
        Name: str,
        Description: str = None,
        GameSessionQueueArns: List[str] = None,
        RequestTimeoutSeconds: int = None,
        AcceptanceTimeoutSeconds: int = None,
        AcceptanceRequired: bool = None,
        RuleSetName: str = None,
        NotificationTarget: str = None,
        AdditionalPlayerCount: int = None,
        CustomEventData: str = None,
        GameProperties: List[GamePropertyTypeDef] = None,
        GameSessionData: str = None,
        BackfillMode: Literal["AUTOMATIC", "MANUAL"] = None,
    ) -> UpdateMatchmakingConfigurationOutputTypeDef:
        """
        [Client.update_matchmaking_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.update_matchmaking_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_runtime_configuration(
        self, FleetId: str, RuntimeConfiguration: RuntimeConfigurationTypeDef
    ) -> UpdateRuntimeConfigurationOutputTypeDef:
        """
        [Client.update_runtime_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.update_runtime_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_script(
        self,
        ScriptId: str,
        Name: str = None,
        Version: str = None,
        StorageLocation: S3LocationTypeDef = None,
        ZipFile: Union[bytes, IO] = None,
    ) -> UpdateScriptOutputTypeDef:
        """
        [Client.update_script documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.update_script)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def validate_matchmaking_rule_set(
        self, RuleSetBody: str
    ) -> ValidateMatchmakingRuleSetOutputTypeDef:
        """
        [Client.validate_matchmaking_rule_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Client.validate_matchmaking_rule_set)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_fleet_attributes"]
    ) -> paginator_scope.DescribeFleetAttributesPaginator:
        """
        [Paginator.DescribeFleetAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetAttributes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_fleet_capacity"]
    ) -> paginator_scope.DescribeFleetCapacityPaginator:
        """
        [Paginator.DescribeFleetCapacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetCapacity)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_fleet_events"]
    ) -> paginator_scope.DescribeFleetEventsPaginator:
        """
        [Paginator.DescribeFleetEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetEvents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_fleet_utilization"]
    ) -> paginator_scope.DescribeFleetUtilizationPaginator:
        """
        [Paginator.DescribeFleetUtilization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetUtilization)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_game_session_details"]
    ) -> paginator_scope.DescribeGameSessionDetailsPaginator:
        """
        [Paginator.DescribeGameSessionDetails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionDetails)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_game_session_queues"]
    ) -> paginator_scope.DescribeGameSessionQueuesPaginator:
        """
        [Paginator.DescribeGameSessionQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionQueues)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_game_sessions"]
    ) -> paginator_scope.DescribeGameSessionsPaginator:
        """
        [Paginator.DescribeGameSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_instances"]
    ) -> paginator_scope.DescribeInstancesPaginator:
        """
        [Paginator.DescribeInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_matchmaking_configurations"]
    ) -> paginator_scope.DescribeMatchmakingConfigurationsPaginator:
        """
        [Paginator.DescribeMatchmakingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingConfigurations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_matchmaking_rule_sets"]
    ) -> paginator_scope.DescribeMatchmakingRuleSetsPaginator:
        """
        [Paginator.DescribeMatchmakingRuleSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingRuleSets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_player_sessions"]
    ) -> paginator_scope.DescribePlayerSessionsPaginator:
        """
        [Paginator.DescribePlayerSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribePlayerSessions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_scaling_policies"]
    ) -> paginator_scope.DescribeScalingPoliciesPaginator:
        """
        [Paginator.DescribeScalingPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.DescribeScalingPolicies)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_aliases"]
    ) -> paginator_scope.ListAliasesPaginator:
        """
        [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.ListAliases)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_builds"]
    ) -> paginator_scope.ListBuildsPaginator:
        """
        [Paginator.ListBuilds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.ListBuilds)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_fleets"]
    ) -> paginator_scope.ListFleetsPaginator:
        """
        [Paginator.ListFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.ListFleets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["search_game_sessions"]
    ) -> paginator_scope.SearchGameSessionsPaginator:
        """
        [Paginator.SearchGameSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/gamelift.html#GameLift.Paginator.SearchGameSessions)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    FleetCapacityExceededException: Boto3ClientError
    GameSessionFullException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidFleetStatusException: Boto3ClientError
    InvalidGameSessionStatusException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TerminalRoutingStrategyException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
    UnsupportedRegionException: Boto3ClientError
