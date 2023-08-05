"Main interface for robomaker service type defs"
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


S3KeyOutputTypeDef = TypedDict("S3KeyOutputTypeDef", {"s3Key": str, "etag": str}, total=False)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {"name": str, "s3Bucket": str, "s3Keys": List[S3KeyOutputTypeDef]},
    total=False,
)

LoggingConfigTypeDef = TypedDict("LoggingConfigTypeDef", {"recordAllRosTopics": bool})

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {"networkInterfaceId": str, "privateIpAddress": str, "publicIpAddress": str},
    total=False,
)

OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef", {"s3Bucket": str, "s3Prefix": str}, total=False
)

_RequiredPortMappingTypeDef = TypedDict(
    "_RequiredPortMappingTypeDef", {"jobPort": int, "applicationPort": int}
)
_OptionalPortMappingTypeDef = TypedDict(
    "_OptionalPortMappingTypeDef", {"enableOnPublicIp": bool}, total=False
)


class PortMappingTypeDef(_RequiredPortMappingTypeDef, _OptionalPortMappingTypeDef):
    pass


PortForwardingConfigTypeDef = TypedDict(
    "PortForwardingConfigTypeDef", {"portMappings": List[PortMappingTypeDef]}, total=False
)

_RequiredLaunchConfigTypeDef = TypedDict(
    "_RequiredLaunchConfigTypeDef", {"packageName": str, "launchFile": str}
)
_OptionalLaunchConfigTypeDef = TypedDict(
    "_OptionalLaunchConfigTypeDef",
    {"environmentVariables": Dict[str, str], "portForwardingConfig": PortForwardingConfigTypeDef},
    total=False,
)


class LaunchConfigTypeDef(_RequiredLaunchConfigTypeDef, _OptionalLaunchConfigTypeDef):
    pass


_RequiredRobotApplicationConfigTypeDef = TypedDict(
    "_RequiredRobotApplicationConfigTypeDef",
    {"application": str, "launchConfig": LaunchConfigTypeDef},
)
_OptionalRobotApplicationConfigTypeDef = TypedDict(
    "_OptionalRobotApplicationConfigTypeDef", {"applicationVersion": str}, total=False
)


class RobotApplicationConfigTypeDef(
    _RequiredRobotApplicationConfigTypeDef, _OptionalRobotApplicationConfigTypeDef
):
    pass


_RequiredSimulationApplicationConfigTypeDef = TypedDict(
    "_RequiredSimulationApplicationConfigTypeDef",
    {"application": str, "launchConfig": LaunchConfigTypeDef},
)
_OptionalSimulationApplicationConfigTypeDef = TypedDict(
    "_OptionalSimulationApplicationConfigTypeDef", {"applicationVersion": str}, total=False
)


class SimulationApplicationConfigTypeDef(
    _RequiredSimulationApplicationConfigTypeDef, _OptionalSimulationApplicationConfigTypeDef
):
    pass


VPCConfigResponseTypeDef = TypedDict(
    "VPCConfigResponseTypeDef",
    {"subnets": List[str], "securityGroups": List[str], "vpcId": str, "assignPublicIp": bool},
    total=False,
)

SimulationJobTypeDef = TypedDict(
    "SimulationJobTypeDef",
    {
        "arn": str,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": OutputLocationTypeDef,
        "loggingConfig": LoggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[RobotApplicationConfigTypeDef],
        "simulationApplications": List[SimulationApplicationConfigTypeDef],
        "dataSources": List[DataSourceTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": VPCConfigResponseTypeDef,
        "networkInterface": NetworkInterfaceTypeDef,
    },
    total=False,
)

BatchDescribeSimulationJobResponseTypeDef = TypedDict(
    "BatchDescribeSimulationJobResponseTypeDef",
    {"jobs": List[SimulationJobTypeDef], "unprocessedJobs": List[str]},
    total=False,
)

_RequiredDeploymentLaunchConfigTypeDef = TypedDict(
    "_RequiredDeploymentLaunchConfigTypeDef", {"packageName": str, "launchFile": str}
)
_OptionalDeploymentLaunchConfigTypeDef = TypedDict(
    "_OptionalDeploymentLaunchConfigTypeDef",
    {"preLaunchFile": str, "postLaunchFile": str, "environmentVariables": Dict[str, str]},
    total=False,
)


class DeploymentLaunchConfigTypeDef(
    _RequiredDeploymentLaunchConfigTypeDef, _OptionalDeploymentLaunchConfigTypeDef
):
    pass


DeploymentApplicationConfigTypeDef = TypedDict(
    "DeploymentApplicationConfigTypeDef",
    {"application": str, "applicationVersion": str, "launchConfig": DeploymentLaunchConfigTypeDef},
)

_RequiredS3ObjectTypeDef = TypedDict("_RequiredS3ObjectTypeDef", {"bucket": str, "key": str})
_OptionalS3ObjectTypeDef = TypedDict("_OptionalS3ObjectTypeDef", {"etag": str}, total=False)


class S3ObjectTypeDef(_RequiredS3ObjectTypeDef, _OptionalS3ObjectTypeDef):
    pass


DeploymentConfigTypeDef = TypedDict(
    "DeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": S3ObjectTypeDef,
    },
    total=False,
)

CreateDeploymentJobResponseTypeDef = TypedDict(
    "CreateDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentApplicationConfigs": List[DeploymentApplicationConfigTypeDef],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
        "deploymentConfig": DeploymentConfigTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {"arn": str, "name": str, "createdAt": datetime, "tags": Dict[str, str]},
    total=False,
)

RobotSoftwareSuiteTypeDef = TypedDict(
    "RobotSoftwareSuiteTypeDef",
    {"name": Literal["ROS", "ROS2"], "version": Literal["Kinetic", "Melodic", "Dashing"]},
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
    },
    total=False,
)

CreateRobotApplicationResponseTypeDef = TypedDict(
    "CreateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateRobotApplicationVersionResponseTypeDef = TypedDict(
    "CreateRobotApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

CreateRobotResponseTypeDef = TypedDict(
    "CreateRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "greengrassGroupId": str,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "tags": Dict[str, str],
    },
    total=False,
)

RenderingEngineTypeDef = TypedDict(
    "RenderingEngineTypeDef", {"name": Literal["OGRE"], "version": str}, total=False
)

SimulationSoftwareSuiteTypeDef = TypedDict(
    "SimulationSoftwareSuiteTypeDef",
    {"name": Literal["Gazebo", "RosbagPlay"], "version": str},
    total=False,
)

CreateSimulationApplicationResponseTypeDef = TypedDict(
    "CreateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "renderingEngine": RenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSimulationApplicationVersionResponseTypeDef = TypedDict(
    "CreateSimulationApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "renderingEngine": RenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

CreateSimulationJobResponseTypeDef = TypedDict(
    "CreateSimulationJobResponseTypeDef",
    {
        "arn": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "clientRequestToken": str,
        "outputLocation": OutputLocationTypeDef,
        "loggingConfig": LoggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[RobotApplicationConfigTypeDef],
        "simulationApplications": List[SimulationApplicationConfigTypeDef],
        "dataSources": List[DataSourceTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": VPCConfigResponseTypeDef,
    },
    total=False,
)

DataSourceConfigTypeDef = TypedDict(
    "DataSourceConfigTypeDef", {"name": str, "s3Bucket": str, "s3Keys": List[str]}
)

DeregisterRobotResponseTypeDef = TypedDict(
    "DeregisterRobotResponseTypeDef", {"fleet": str, "robot": str}, total=False
)

ProgressDetailTypeDef = TypedDict(
    "ProgressDetailTypeDef",
    {
        "currentProgress": Literal[
            "Validating",
            "DownloadingExtracting",
            "ExecutingDownloadCondition",
            "ExecutingPreLaunch",
            "Launching",
            "ExecutingPostLaunch",
            "Finished",
        ],
        "percentDone": float,
        "estimatedTimeRemainingSeconds": int,
        "targetResource": str,
    },
    total=False,
)

RobotDeploymentTypeDef = TypedDict(
    "RobotDeploymentTypeDef",
    {
        "arn": str,
        "deploymentStartTime": datetime,
        "deploymentFinishTime": datetime,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "progressDetail": ProgressDetailTypeDef,
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
    },
    total=False,
)

DescribeDeploymentJobResponseTypeDef = TypedDict(
    "DescribeDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentConfig": DeploymentConfigTypeDef,
        "deploymentApplicationConfigs": List[DeploymentApplicationConfigTypeDef],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
        "robotDeploymentSummary": List[RobotDeploymentTypeDef],
        "tags": Dict[str, str],
    },
    total=False,
)

RobotTypeDef = TypedDict(
    "RobotTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

DescribeFleetResponseTypeDef = TypedDict(
    "DescribeFleetResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "robots": List[RobotTypeDef],
        "createdAt": datetime,
        "lastDeploymentStatus": Literal[
            "Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"
        ],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeRobotApplicationResponseTypeDef = TypedDict(
    "DescribeRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeRobotResponseTypeDef = TypedDict(
    "DescribeRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": Literal[
            "Available",
            "Registered",
            "PendingNewDeployment",
            "Deploying",
            "Failed",
            "InSync",
            "NoResponse",
        ],
        "greengrassGroupId": str,
        "createdAt": datetime,
        "architecture": Literal["X86_64", "ARM64", "ARMHF"],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeSimulationApplicationResponseTypeDef = TypedDict(
    "DescribeSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "renderingEngine": RenderingEngineTypeDef,
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeSimulationJobResponseTypeDef = TypedDict(
    "DescribeSimulationJobResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": Literal["Fail", "Continue"],
        "failureCode": Literal[
            "InternalServiceError",
            "RobotApplicationCrash",
            "SimulationApplicationCrash",
            "BadPermissionsRobotApplication",
            "BadPermissionsSimulationApplication",
            "BadPermissionsS3Object",
            "BadPermissionsS3Output",
            "BadPermissionsCloudwatchLogs",
            "SubnetIpLimitExceeded",
            "ENILimitExceeded",
            "BadPermissionsUserCredentials",
            "InvalidBundleRobotApplication",
            "InvalidBundleSimulationApplication",
            "InvalidS3Resource",
            "MismatchedEtag",
            "RobotApplicationVersionMismatchedEtag",
            "SimulationApplicationVersionMismatchedEtag",
            "ResourceNotFound",
            "InvalidInput",
            "WrongRegionS3Bucket",
            "WrongRegionS3Output",
            "WrongRegionRobotApplication",
            "WrongRegionSimulationApplication",
        ],
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": OutputLocationTypeDef,
        "loggingConfig": LoggingConfigTypeDef,
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List[RobotApplicationConfigTypeDef],
        "simulationApplications": List[SimulationApplicationConfigTypeDef],
        "dataSources": List[DataSourceTypeDef],
        "tags": Dict[str, str],
        "vpcConfig": VPCConfigResponseTypeDef,
        "networkInterface": NetworkInterfaceTypeDef,
    },
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"name": str, "values": List[str]}, total=False)

DeploymentJobTypeDef = TypedDict(
    "DeploymentJobTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentApplicationConfigs": List[DeploymentApplicationConfigTypeDef],
        "deploymentConfig": DeploymentConfigTypeDef,
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
    },
    total=False,
)

ListDeploymentJobsResponseTypeDef = TypedDict(
    "ListDeploymentJobsResponseTypeDef",
    {"deploymentJobs": List[DeploymentJobTypeDef], "nextToken": str},
    total=False,
)

FleetTypeDef = TypedDict(
    "FleetTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "lastDeploymentStatus": Literal[
            "Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"
        ],
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef", {"fleetDetails": List[FleetTypeDef], "nextToken": str}, total=False
)

RobotApplicationSummaryTypeDef = TypedDict(
    "RobotApplicationSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
    },
    total=False,
)

ListRobotApplicationsResponseTypeDef = TypedDict(
    "ListRobotApplicationsResponseTypeDef",
    {"robotApplicationSummaries": List[RobotApplicationSummaryTypeDef], "nextToken": str},
    total=False,
)

ListRobotsResponseTypeDef = TypedDict(
    "ListRobotsResponseTypeDef", {"robots": List[RobotTypeDef], "nextToken": str}, total=False
)

SimulationApplicationSummaryTypeDef = TypedDict(
    "SimulationApplicationSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
    },
    total=False,
)

ListSimulationApplicationsResponseTypeDef = TypedDict(
    "ListSimulationApplicationsResponseTypeDef",
    {"simulationApplicationSummaries": List[SimulationApplicationSummaryTypeDef], "nextToken": str},
    total=False,
)

SimulationJobSummaryTypeDef = TypedDict(
    "SimulationJobSummaryTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": Literal[
            "Pending",
            "Preparing",
            "Running",
            "Restarting",
            "Completed",
            "Failed",
            "RunningFailed",
            "Terminating",
            "Terminated",
            "Canceled",
        ],
        "simulationApplicationNames": List[str],
        "robotApplicationNames": List[str],
        "dataSourceNames": List[str],
    },
    total=False,
)

_RequiredListSimulationJobsResponseTypeDef = TypedDict(
    "_RequiredListSimulationJobsResponseTypeDef",
    {"simulationJobSummaries": List[SimulationJobSummaryTypeDef]},
)
_OptionalListSimulationJobsResponseTypeDef = TypedDict(
    "_OptionalListSimulationJobsResponseTypeDef", {"nextToken": str}, total=False
)


class ListSimulationJobsResponseTypeDef(
    _RequiredListSimulationJobsResponseTypeDef, _OptionalListSimulationJobsResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterRobotResponseTypeDef = TypedDict(
    "RegisterRobotResponseTypeDef", {"fleet": str, "robot": str}, total=False
)

SourceConfigTypeDef = TypedDict(
    "SourceConfigTypeDef",
    {"s3Bucket": str, "s3Key": str, "architecture": Literal["X86_64", "ARM64", "ARMHF"]},
    total=False,
)

SyncDeploymentJobResponseTypeDef = TypedDict(
    "SyncDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": Literal["Pending", "Preparing", "InProgress", "Failed", "Succeeded", "Canceled"],
        "deploymentConfig": DeploymentConfigTypeDef,
        "deploymentApplicationConfigs": List[DeploymentApplicationConfigTypeDef],
        "failureReason": str,
        "failureCode": Literal[
            "ResourceNotFound",
            "EnvironmentSetupError",
            "EtagMismatch",
            "FailureThresholdBreached",
            "RobotDeploymentAborted",
            "RobotDeploymentNoResponse",
            "RobotAgentConnectionTimeout",
            "GreengrassDeploymentFailed",
            "MissingRobotArchitecture",
            "MissingRobotApplicationArchitecture",
            "MissingRobotDeploymentResource",
            "GreengrassGroupVersionDoesNotExist",
            "ExtractingBundleFailure",
            "PreLaunchFileFailure",
            "PostLaunchFileFailure",
            "BadPermissionError",
            "DownloadConditionFailed",
            "InternalServerError",
        ],
        "createdAt": datetime,
    },
    total=False,
)

UpdateRobotApplicationResponseTypeDef = TypedDict(
    "UpdateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

UpdateSimulationApplicationResponseTypeDef = TypedDict(
    "UpdateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List[SourceTypeDef],
        "simulationSoftwareSuite": SimulationSoftwareSuiteTypeDef,
        "robotSoftwareSuite": RobotSoftwareSuiteTypeDef,
        "renderingEngine": RenderingEngineTypeDef,
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

_RequiredVPCConfigTypeDef = TypedDict("_RequiredVPCConfigTypeDef", {"subnets": List[str]})
_OptionalVPCConfigTypeDef = TypedDict(
    "_OptionalVPCConfigTypeDef", {"securityGroups": List[str], "assignPublicIp": bool}, total=False
)


class VPCConfigTypeDef(_RequiredVPCConfigTypeDef, _OptionalVPCConfigTypeDef):
    pass
