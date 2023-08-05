"Main interface for gamelift service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


CertificateConfigurationTypeDef = TypedDict(
    "CertificateConfigurationTypeDef", {"CertificateType": Literal["DISABLED", "GENERATED"]}
)

RoutingStrategyTypeDef = TypedDict(
    "RoutingStrategyTypeDef",
    {"Type": Literal["SIMPLE", "TERMINAL"], "FleetId": str, "Message": str},
    total=False,
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": RoutingStrategyTypeDef,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

CreateAliasOutputTypeDef = TypedDict(
    "CreateAliasOutputTypeDef", {"Alias": AliasTypeDef}, total=False
)

AwsCredentialsTypeDef = TypedDict(
    "AwsCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str},
    total=False,
)

BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "BuildId": str,
        "Name": str,
        "Version": str,
        "Status": Literal["INITIALIZED", "READY", "FAILED"],
        "SizeOnDisk": int,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "CreationTime": datetime,
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)

CreateBuildOutputTypeDef = TypedDict(
    "CreateBuildOutputTypeDef",
    {
        "Build": BuildTypeDef,
        "UploadCredentials": AwsCredentialsTypeDef,
        "StorageLocation": S3LocationTypeDef,
    },
    total=False,
)

ResourceCreationLimitPolicyTypeDef = TypedDict(
    "ResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)

FleetAttributesTypeDef = TypedDict(
    "FleetAttributesTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "FleetType": Literal["ON_DEMAND", "SPOT"],
        "InstanceType": Literal[
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
        "Description": str,
        "Name": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": Literal[
            "NEW",
            "DOWNLOADING",
            "VALIDATING",
            "BUILDING",
            "ACTIVATING",
            "ACTIVE",
            "DELETING",
            "ERROR",
            "TERMINATED",
        ],
        "BuildId": str,
        "ScriptId": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "NewGameSessionProtectionPolicy": Literal["NoProtection", "FullProtection"],
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "ResourceCreationLimitPolicy": ResourceCreationLimitPolicyTypeDef,
        "MetricGroups": List[str],
        "StoppedActions": List[Literal["AUTO_SCALING"]],
        "InstanceRoleArn": str,
        "CertificateConfiguration": CertificateConfigurationTypeDef,
    },
    total=False,
)

CreateFleetOutputTypeDef = TypedDict(
    "CreateFleetOutputTypeDef", {"FleetAttributes": FleetAttributesTypeDef}, total=False
)

GamePropertyTypeDef = TypedDict("GamePropertyTypeDef", {"Key": str, "Value": str})

GameSessionTypeDef = TypedDict(
    "GameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": Literal["ACTIVE", "ACTIVATING", "TERMINATED", "TERMINATING", "ERROR"],
        "StatusReason": Literal["INTERRUPTED"],
        "GameProperties": List[GamePropertyTypeDef],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": Literal["ACCEPT_ALL", "DENY_ALL"],
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

CreateGameSessionOutputTypeDef = TypedDict(
    "CreateGameSessionOutputTypeDef", {"GameSession": GameSessionTypeDef}, total=False
)

GameSessionQueueDestinationTypeDef = TypedDict(
    "GameSessionQueueDestinationTypeDef", {"DestinationArn": str}, total=False
)

PlayerLatencyPolicyTypeDef = TypedDict(
    "PlayerLatencyPolicyTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)

GameSessionQueueTypeDef = TypedDict(
    "GameSessionQueueTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List[PlayerLatencyPolicyTypeDef],
        "Destinations": List[GameSessionQueueDestinationTypeDef],
    },
    total=False,
)

CreateGameSessionQueueOutputTypeDef = TypedDict(
    "CreateGameSessionQueueOutputTypeDef",
    {"GameSessionQueue": GameSessionQueueTypeDef},
    total=False,
)

MatchmakingConfigurationTypeDef = TypedDict(
    "MatchmakingConfigurationTypeDef",
    {
        "Name": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List[GamePropertyTypeDef],
        "GameSessionData": str,
        "BackfillMode": Literal["AUTOMATIC", "MANUAL"],
    },
    total=False,
)

CreateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "CreateMatchmakingConfigurationOutputTypeDef",
    {"Configuration": MatchmakingConfigurationTypeDef},
    total=False,
)

_RequiredMatchmakingRuleSetTypeDef = TypedDict(
    "_RequiredMatchmakingRuleSetTypeDef", {"RuleSetBody": str}
)
_OptionalMatchmakingRuleSetTypeDef = TypedDict(
    "_OptionalMatchmakingRuleSetTypeDef",
    {"RuleSetName": str, "CreationTime": datetime},
    total=False,
)


class MatchmakingRuleSetTypeDef(
    _RequiredMatchmakingRuleSetTypeDef, _OptionalMatchmakingRuleSetTypeDef
):
    pass


CreateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "CreateMatchmakingRuleSetOutputTypeDef", {"RuleSet": MatchmakingRuleSetTypeDef}
)

PlayerSessionTypeDef = TypedDict(
    "PlayerSessionTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": Literal["RESERVED", "ACTIVE", "COMPLETED", "TIMEDOUT"],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)

CreatePlayerSessionOutputTypeDef = TypedDict(
    "CreatePlayerSessionOutputTypeDef", {"PlayerSession": PlayerSessionTypeDef}, total=False
)

CreatePlayerSessionsOutputTypeDef = TypedDict(
    "CreatePlayerSessionsOutputTypeDef", {"PlayerSessions": List[PlayerSessionTypeDef]}, total=False
)

ScriptTypeDef = TypedDict(
    "ScriptTypeDef",
    {
        "ScriptId": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": S3LocationTypeDef,
    },
    total=False,
)

CreateScriptOutputTypeDef = TypedDict(
    "CreateScriptOutputTypeDef", {"Script": ScriptTypeDef}, total=False
)

VpcPeeringAuthorizationTypeDef = TypedDict(
    "VpcPeeringAuthorizationTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
    },
    total=False,
)

CreateVpcPeeringAuthorizationOutputTypeDef = TypedDict(
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    {"VpcPeeringAuthorization": VpcPeeringAuthorizationTypeDef},
    total=False,
)

DescribeAliasOutputTypeDef = TypedDict(
    "DescribeAliasOutputTypeDef", {"Alias": AliasTypeDef}, total=False
)

DescribeBuildOutputTypeDef = TypedDict(
    "DescribeBuildOutputTypeDef", {"Build": BuildTypeDef}, total=False
)

EC2InstanceLimitTypeDef = TypedDict(
    "EC2InstanceLimitTypeDef",
    {
        "EC2InstanceType": Literal[
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
        "CurrentInstances": int,
        "InstanceLimit": int,
    },
    total=False,
)

DescribeEC2InstanceLimitsOutputTypeDef = TypedDict(
    "DescribeEC2InstanceLimitsOutputTypeDef",
    {"EC2InstanceLimits": List[EC2InstanceLimitTypeDef]},
    total=False,
)

DescribeFleetAttributesOutputTypeDef = TypedDict(
    "DescribeFleetAttributesOutputTypeDef",
    {"FleetAttributes": List[FleetAttributesTypeDef], "NextToken": str},
    total=False,
)

EC2InstanceCountsTypeDef = TypedDict(
    "EC2InstanceCountsTypeDef",
    {
        "DESIRED": int,
        "MINIMUM": int,
        "MAXIMUM": int,
        "PENDING": int,
        "ACTIVE": int,
        "IDLE": int,
        "TERMINATING": int,
    },
    total=False,
)

FleetCapacityTypeDef = TypedDict(
    "FleetCapacityTypeDef",
    {
        "FleetId": str,
        "InstanceType": Literal[
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
        "InstanceCounts": EC2InstanceCountsTypeDef,
    },
    total=False,
)

DescribeFleetCapacityOutputTypeDef = TypedDict(
    "DescribeFleetCapacityOutputTypeDef",
    {"FleetCapacity": List[FleetCapacityTypeDef], "NextToken": str},
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": str,
        "ResourceId": str,
        "EventCode": Literal[
            "GENERIC_EVENT",
            "FLEET_CREATED",
            "FLEET_DELETED",
            "FLEET_SCALING_EVENT",
            "FLEET_STATE_DOWNLOADING",
            "FLEET_STATE_VALIDATING",
            "FLEET_STATE_BUILDING",
            "FLEET_STATE_ACTIVATING",
            "FLEET_STATE_ACTIVE",
            "FLEET_STATE_ERROR",
            "FLEET_INITIALIZATION_FAILED",
            "FLEET_BINARY_DOWNLOAD_FAILED",
            "FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND",
            "FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE",
            "FLEET_VALIDATION_TIMED_OUT",
            "FLEET_ACTIVATION_FAILED",
            "FLEET_ACTIVATION_FAILED_NO_INSTANCES",
            "FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED",
            "SERVER_PROCESS_INVALID_PATH",
            "SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT",
            "SERVER_PROCESS_PROCESS_READY_TIMEOUT",
            "SERVER_PROCESS_CRASHED",
            "SERVER_PROCESS_TERMINATED_UNHEALTHY",
            "SERVER_PROCESS_FORCE_TERMINATED",
            "SERVER_PROCESS_PROCESS_EXIT_TIMEOUT",
            "GAME_SESSION_ACTIVATION_TIMEOUT",
            "FLEET_CREATION_EXTRACTING_BUILD",
            "FLEET_CREATION_RUNNING_INSTALLER",
            "FLEET_CREATION_VALIDATING_RUNTIME_CONFIG",
            "FLEET_VPC_PEERING_SUCCEEDED",
            "FLEET_VPC_PEERING_FAILED",
            "FLEET_VPC_PEERING_DELETED",
            "INSTANCE_INTERRUPTED",
        ],
        "Message": str,
        "EventTime": datetime,
        "PreSignedLogUrl": str,
    },
    total=False,
)

DescribeFleetEventsOutputTypeDef = TypedDict(
    "DescribeFleetEventsOutputTypeDef",
    {"Events": List[EventTypeDef], "NextToken": str},
    total=False,
)

IpPermissionTypeDef = TypedDict(
    "IpPermissionTypeDef",
    {"FromPort": int, "ToPort": int, "IpRange": str, "Protocol": Literal["TCP", "UDP"]},
)

DescribeFleetPortSettingsOutputTypeDef = TypedDict(
    "DescribeFleetPortSettingsOutputTypeDef",
    {"InboundPermissions": List[IpPermissionTypeDef]},
    total=False,
)

FleetUtilizationTypeDef = TypedDict(
    "FleetUtilizationTypeDef",
    {
        "FleetId": str,
        "ActiveServerProcessCount": int,
        "ActiveGameSessionCount": int,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
    },
    total=False,
)

DescribeFleetUtilizationOutputTypeDef = TypedDict(
    "DescribeFleetUtilizationOutputTypeDef",
    {"FleetUtilization": List[FleetUtilizationTypeDef], "NextToken": str},
    total=False,
)

GameSessionDetailTypeDef = TypedDict(
    "GameSessionDetailTypeDef",
    {
        "GameSession": GameSessionTypeDef,
        "ProtectionPolicy": Literal["NoProtection", "FullProtection"],
    },
    total=False,
)

DescribeGameSessionDetailsOutputTypeDef = TypedDict(
    "DescribeGameSessionDetailsOutputTypeDef",
    {"GameSessionDetails": List[GameSessionDetailTypeDef], "NextToken": str},
    total=False,
)

PlacedPlayerSessionTypeDef = TypedDict(
    "PlacedPlayerSessionTypeDef", {"PlayerId": str, "PlayerSessionId": str}, total=False
)

PlayerLatencyTypeDef = TypedDict(
    "PlayerLatencyTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": float},
    total=False,
)

GameSessionPlacementTypeDef = TypedDict(
    "GameSessionPlacementTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "Status": Literal["PENDING", "FULFILLED", "CANCELLED", "TIMED_OUT", "FAILED"],
        "GameProperties": List[GamePropertyTypeDef],
        "MaximumPlayerSessionCount": int,
        "GameSessionName": str,
        "GameSessionId": str,
        "GameSessionArn": str,
        "GameSessionRegion": str,
        "PlayerLatencies": List[PlayerLatencyTypeDef],
        "StartTime": datetime,
        "EndTime": datetime,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlacedPlayerSessions": List[PlacedPlayerSessionTypeDef],
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

DescribeGameSessionPlacementOutputTypeDef = TypedDict(
    "DescribeGameSessionPlacementOutputTypeDef",
    {"GameSessionPlacement": GameSessionPlacementTypeDef},
    total=False,
)

DescribeGameSessionQueuesOutputTypeDef = TypedDict(
    "DescribeGameSessionQueuesOutputTypeDef",
    {"GameSessionQueues": List[GameSessionQueueTypeDef], "NextToken": str},
    total=False,
)

DescribeGameSessionsOutputTypeDef = TypedDict(
    "DescribeGameSessionsOutputTypeDef",
    {"GameSessions": List[GameSessionTypeDef], "NextToken": str},
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "DnsName": str,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "Type": Literal[
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
        "Status": Literal["PENDING", "ACTIVE", "TERMINATING"],
        "CreationTime": datetime,
    },
    total=False,
)

DescribeInstancesOutputTypeDef = TypedDict(
    "DescribeInstancesOutputTypeDef",
    {"Instances": List[InstanceTypeDef], "NextToken": str},
    total=False,
)

DescribeMatchmakingConfigurationsOutputTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    {"Configurations": List[MatchmakingConfigurationTypeDef], "NextToken": str},
    total=False,
)

MatchedPlayerSessionTypeDef = TypedDict(
    "MatchedPlayerSessionTypeDef", {"PlayerId": str, "PlayerSessionId": str}, total=False
)

GameSessionConnectionInfoTypeDef = TypedDict(
    "GameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "MatchedPlayerSessions": List[MatchedPlayerSessionTypeDef],
    },
    total=False,
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)

PlayerTypeDef = TypedDict(
    "PlayerTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[str, AttributeValueTypeDef],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)

MatchmakingTicketTypeDef = TypedDict(
    "MatchmakingTicketTypeDef",
    {
        "TicketId": str,
        "ConfigurationName": str,
        "Status": Literal[
            "CANCELLED",
            "COMPLETED",
            "FAILED",
            "PLACING",
            "QUEUED",
            "REQUIRES_ACCEPTANCE",
            "SEARCHING",
            "TIMED_OUT",
        ],
        "StatusReason": str,
        "StatusMessage": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Players": List[PlayerTypeDef],
        "GameSessionConnectionInfo": GameSessionConnectionInfoTypeDef,
        "EstimatedWaitTime": int,
    },
    total=False,
)

DescribeMatchmakingOutputTypeDef = TypedDict(
    "DescribeMatchmakingOutputTypeDef", {"TicketList": List[MatchmakingTicketTypeDef]}, total=False
)

_RequiredDescribeMatchmakingRuleSetsOutputTypeDef = TypedDict(
    "_RequiredDescribeMatchmakingRuleSetsOutputTypeDef",
    {"RuleSets": List[MatchmakingRuleSetTypeDef]},
)
_OptionalDescribeMatchmakingRuleSetsOutputTypeDef = TypedDict(
    "_OptionalDescribeMatchmakingRuleSetsOutputTypeDef", {"NextToken": str}, total=False
)


class DescribeMatchmakingRuleSetsOutputTypeDef(
    _RequiredDescribeMatchmakingRuleSetsOutputTypeDef,
    _OptionalDescribeMatchmakingRuleSetsOutputTypeDef,
):
    pass


DescribePlayerSessionsOutputTypeDef = TypedDict(
    "DescribePlayerSessionsOutputTypeDef",
    {"PlayerSessions": List[PlayerSessionTypeDef], "NextToken": str},
    total=False,
)

_RequiredServerProcessTypeDef = TypedDict(
    "_RequiredServerProcessTypeDef", {"LaunchPath": str, "ConcurrentExecutions": int}
)
_OptionalServerProcessTypeDef = TypedDict(
    "_OptionalServerProcessTypeDef", {"Parameters": str}, total=False
)


class ServerProcessTypeDef(_RequiredServerProcessTypeDef, _OptionalServerProcessTypeDef):
    pass


RuntimeConfigurationTypeDef = TypedDict(
    "RuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List[ServerProcessTypeDef],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)

DescribeRuntimeConfigurationOutputTypeDef = TypedDict(
    "DescribeRuntimeConfigurationOutputTypeDef",
    {"RuntimeConfiguration": RuntimeConfigurationTypeDef},
    total=False,
)

TargetConfigurationTypeDef = TypedDict("TargetConfigurationTypeDef", {"TargetValue": float})

ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "FleetId": str,
        "Name": str,
        "Status": Literal[
            "ACTIVE",
            "UPDATE_REQUESTED",
            "UPDATING",
            "DELETE_REQUESTED",
            "DELETING",
            "DELETED",
            "ERROR",
        ],
        "ScalingAdjustment": int,
        "ScalingAdjustmentType": Literal[
            "ChangeInCapacity", "ExactCapacity", "PercentChangeInCapacity"
        ],
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Threshold": float,
        "EvaluationPeriods": int,
        "MetricName": Literal[
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
        "PolicyType": Literal["RuleBased", "TargetBased"],
        "TargetConfiguration": TargetConfigurationTypeDef,
    },
    total=False,
)

DescribeScalingPoliciesOutputTypeDef = TypedDict(
    "DescribeScalingPoliciesOutputTypeDef",
    {"ScalingPolicies": List[ScalingPolicyTypeDef], "NextToken": str},
    total=False,
)

DescribeScriptOutputTypeDef = TypedDict(
    "DescribeScriptOutputTypeDef", {"Script": ScriptTypeDef}, total=False
)

DescribeVpcPeeringAuthorizationsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    {"VpcPeeringAuthorizations": List[VpcPeeringAuthorizationTypeDef]},
    total=False,
)

VpcPeeringConnectionStatusTypeDef = TypedDict(
    "VpcPeeringConnectionStatusTypeDef", {"Code": str, "Message": str}, total=False
)

VpcPeeringConnectionTypeDef = TypedDict(
    "VpcPeeringConnectionTypeDef",
    {
        "FleetId": str,
        "IpV4CidrBlock": str,
        "VpcPeeringConnectionId": str,
        "Status": VpcPeeringConnectionStatusTypeDef,
        "PeerVpcId": str,
        "GameLiftVpcId": str,
    },
    total=False,
)

DescribeVpcPeeringConnectionsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsOutputTypeDef",
    {"VpcPeeringConnections": List[VpcPeeringConnectionTypeDef]},
    total=False,
)

DesiredPlayerSessionTypeDef = TypedDict(
    "DesiredPlayerSessionTypeDef", {"PlayerId": str, "PlayerData": str}, total=False
)

GetGameSessionLogUrlOutputTypeDef = TypedDict(
    "GetGameSessionLogUrlOutputTypeDef", {"PreSignedUrl": str}, total=False
)

InstanceCredentialsTypeDef = TypedDict(
    "InstanceCredentialsTypeDef", {"UserName": str, "Secret": str}, total=False
)

InstanceAccessTypeDef = TypedDict(
    "InstanceAccessTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "OperatingSystem": Literal["WINDOWS_2012", "AMAZON_LINUX", "AMAZON_LINUX_2"],
        "Credentials": InstanceCredentialsTypeDef,
    },
    total=False,
)

GetInstanceAccessOutputTypeDef = TypedDict(
    "GetInstanceAccessOutputTypeDef", {"InstanceAccess": InstanceAccessTypeDef}, total=False
)

ListAliasesOutputTypeDef = TypedDict(
    "ListAliasesOutputTypeDef", {"Aliases": List[AliasTypeDef], "NextToken": str}, total=False
)

ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef", {"Builds": List[BuildTypeDef], "NextToken": str}, total=False
)

ListFleetsOutputTypeDef = TypedDict(
    "ListFleetsOutputTypeDef", {"FleetIds": List[str], "NextToken": str}, total=False
)

ListScriptsOutputTypeDef = TypedDict(
    "ListScriptsOutputTypeDef", {"Scripts": List[ScriptTypeDef], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutScalingPolicyOutputTypeDef = TypedDict(
    "PutScalingPolicyOutputTypeDef", {"Name": str}, total=False
)

RequestUploadCredentialsOutputTypeDef = TypedDict(
    "RequestUploadCredentialsOutputTypeDef",
    {"UploadCredentials": AwsCredentialsTypeDef, "StorageLocation": S3LocationTypeDef},
    total=False,
)

ResolveAliasOutputTypeDef = TypedDict("ResolveAliasOutputTypeDef", {"FleetId": str}, total=False)

SearchGameSessionsOutputTypeDef = TypedDict(
    "SearchGameSessionsOutputTypeDef",
    {"GameSessions": List[GameSessionTypeDef], "NextToken": str},
    total=False,
)

StartGameSessionPlacementOutputTypeDef = TypedDict(
    "StartGameSessionPlacementOutputTypeDef",
    {"GameSessionPlacement": GameSessionPlacementTypeDef},
    total=False,
)

StartMatchBackfillOutputTypeDef = TypedDict(
    "StartMatchBackfillOutputTypeDef", {"MatchmakingTicket": MatchmakingTicketTypeDef}, total=False
)

StartMatchmakingOutputTypeDef = TypedDict(
    "StartMatchmakingOutputTypeDef", {"MatchmakingTicket": MatchmakingTicketTypeDef}, total=False
)

StopGameSessionPlacementOutputTypeDef = TypedDict(
    "StopGameSessionPlacementOutputTypeDef",
    {"GameSessionPlacement": GameSessionPlacementTypeDef},
    total=False,
)

UpdateAliasOutputTypeDef = TypedDict(
    "UpdateAliasOutputTypeDef", {"Alias": AliasTypeDef}, total=False
)

UpdateBuildOutputTypeDef = TypedDict(
    "UpdateBuildOutputTypeDef", {"Build": BuildTypeDef}, total=False
)

UpdateFleetAttributesOutputTypeDef = TypedDict(
    "UpdateFleetAttributesOutputTypeDef", {"FleetId": str}, total=False
)

UpdateFleetCapacityOutputTypeDef = TypedDict(
    "UpdateFleetCapacityOutputTypeDef", {"FleetId": str}, total=False
)

UpdateFleetPortSettingsOutputTypeDef = TypedDict(
    "UpdateFleetPortSettingsOutputTypeDef", {"FleetId": str}, total=False
)

UpdateGameSessionOutputTypeDef = TypedDict(
    "UpdateGameSessionOutputTypeDef", {"GameSession": GameSessionTypeDef}, total=False
)

UpdateGameSessionQueueOutputTypeDef = TypedDict(
    "UpdateGameSessionQueueOutputTypeDef",
    {"GameSessionQueue": GameSessionQueueTypeDef},
    total=False,
)

UpdateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "UpdateMatchmakingConfigurationOutputTypeDef",
    {"Configuration": MatchmakingConfigurationTypeDef},
    total=False,
)

UpdateRuntimeConfigurationOutputTypeDef = TypedDict(
    "UpdateRuntimeConfigurationOutputTypeDef",
    {"RuntimeConfiguration": RuntimeConfigurationTypeDef},
    total=False,
)

UpdateScriptOutputTypeDef = TypedDict(
    "UpdateScriptOutputTypeDef", {"Script": ScriptTypeDef}, total=False
)

ValidateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "ValidateMatchmakingRuleSetOutputTypeDef", {"Valid": bool}, total=False
)
