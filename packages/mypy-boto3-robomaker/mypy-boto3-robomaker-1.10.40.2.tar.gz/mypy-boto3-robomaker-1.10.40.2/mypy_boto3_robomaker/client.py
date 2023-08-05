"Main interface for robomaker service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_robomaker.client as client_scope

# pylint: disable=import-self
import mypy_boto3_robomaker.paginator as paginator_scope
from mypy_boto3_robomaker.type_defs import (
    BatchDescribeSimulationJobResponseTypeDef,
    CreateDeploymentJobResponseTypeDef,
    CreateFleetResponseTypeDef,
    CreateRobotApplicationResponseTypeDef,
    CreateRobotApplicationVersionResponseTypeDef,
    CreateRobotResponseTypeDef,
    CreateSimulationApplicationResponseTypeDef,
    CreateSimulationApplicationVersionResponseTypeDef,
    CreateSimulationJobResponseTypeDef,
    DataSourceConfigTypeDef,
    DeploymentApplicationConfigTypeDef,
    DeploymentConfigTypeDef,
    DeregisterRobotResponseTypeDef,
    DescribeDeploymentJobResponseTypeDef,
    DescribeFleetResponseTypeDef,
    DescribeRobotApplicationResponseTypeDef,
    DescribeRobotResponseTypeDef,
    DescribeSimulationApplicationResponseTypeDef,
    DescribeSimulationJobResponseTypeDef,
    FilterTypeDef,
    ListDeploymentJobsResponseTypeDef,
    ListFleetsResponseTypeDef,
    ListRobotApplicationsResponseTypeDef,
    ListRobotsResponseTypeDef,
    ListSimulationApplicationsResponseTypeDef,
    ListSimulationJobsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingConfigTypeDef,
    OutputLocationTypeDef,
    RegisterRobotResponseTypeDef,
    RenderingEngineTypeDef,
    RobotApplicationConfigTypeDef,
    RobotSoftwareSuiteTypeDef,
    SimulationApplicationConfigTypeDef,
    SimulationSoftwareSuiteTypeDef,
    SourceConfigTypeDef,
    SyncDeploymentJobResponseTypeDef,
    UpdateRobotApplicationResponseTypeDef,
    UpdateSimulationApplicationResponseTypeDef,
    VPCConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RoboMakerClient",)


class RoboMakerClient(BaseClient):
    """
    [RoboMaker.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_describe_simulation_job(
        self, jobs: List[str]
    ) -> BatchDescribeSimulationJobResponseTypeDef:
        """
        [Client.batch_describe_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.batch_describe_simulation_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_deployment_job(self, job: str) -> Dict[str, Any]:
        """
        [Client.cancel_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.cancel_deployment_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_simulation_job(self, job: str) -> Dict[str, Any]:
        """
        [Client.cancel_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.cancel_simulation_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_deployment_job(
        self,
        clientRequestToken: str,
        fleet: str,
        deploymentApplicationConfigs: List[DeploymentApplicationConfigTypeDef],
        deploymentConfig: DeploymentConfigTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> CreateDeploymentJobResponseTypeDef:
        """
        [Client.create_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.create_deployment_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_fleet(self, name: str, tags: Dict[str, str] = None) -> CreateFleetResponseTypeDef:
        """
        [Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.create_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_robot(
        self,
        name: str,
        architecture: Literal["X86_64", "ARM64", "ARMHF"],
        greengrassGroupId: str,
        tags: Dict[str, str] = None,
    ) -> CreateRobotResponseTypeDef:
        """
        [Client.create_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.create_robot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_robot_application(
        self,
        name: str,
        sources: List[SourceConfigTypeDef],
        robotSoftwareSuite: RobotSoftwareSuiteTypeDef,
        tags: Dict[str, str] = None,
    ) -> CreateRobotApplicationResponseTypeDef:
        """
        [Client.create_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.create_robot_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_robot_application_version(
        self, application: str, currentRevisionId: str = None
    ) -> CreateRobotApplicationVersionResponseTypeDef:
        """
        [Client.create_robot_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.create_robot_application_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_simulation_application(
        self,
        name: str,
        sources: List[SourceConfigTypeDef],
        simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef,
        robotSoftwareSuite: RobotSoftwareSuiteTypeDef,
        renderingEngine: RenderingEngineTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> CreateSimulationApplicationResponseTypeDef:
        """
        [Client.create_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_simulation_application_version(
        self, application: str, currentRevisionId: str = None
    ) -> CreateSimulationApplicationVersionResponseTypeDef:
        """
        [Client.create_simulation_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_simulation_job(
        self,
        maxJobDurationInSeconds: int,
        iamRole: str,
        clientRequestToken: str = None,
        outputLocation: OutputLocationTypeDef = None,
        loggingConfig: LoggingConfigTypeDef = None,
        failureBehavior: Literal["Fail", "Continue"] = None,
        robotApplications: List[RobotApplicationConfigTypeDef] = None,
        simulationApplications: List[SimulationApplicationConfigTypeDef] = None,
        dataSources: List[DataSourceConfigTypeDef] = None,
        tags: Dict[str, str] = None,
        vpcConfig: VPCConfigTypeDef = None,
    ) -> CreateSimulationJobResponseTypeDef:
        """
        [Client.create_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.create_simulation_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_fleet(self, fleet: str) -> Dict[str, Any]:
        """
        [Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.delete_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_robot(self, robot: str) -> Dict[str, Any]:
        """
        [Client.delete_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.delete_robot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_robot_application(
        self, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.delete_robot_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_simulation_application(
        self, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.delete_simulation_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_robot(self, fleet: str, robot: str) -> DeregisterRobotResponseTypeDef:
        """
        [Client.deregister_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.deregister_robot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_deployment_job(self, job: str) -> DescribeDeploymentJobResponseTypeDef:
        """
        [Client.describe_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.describe_deployment_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleet(self, fleet: str) -> DescribeFleetResponseTypeDef:
        """
        [Client.describe_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.describe_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_robot(self, robot: str) -> DescribeRobotResponseTypeDef:
        """
        [Client.describe_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.describe_robot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_robot_application(
        self, application: str, applicationVersion: str = None
    ) -> DescribeRobotApplicationResponseTypeDef:
        """
        [Client.describe_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.describe_robot_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_simulation_application(
        self, application: str, applicationVersion: str = None
    ) -> DescribeSimulationApplicationResponseTypeDef:
        """
        [Client.describe_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_simulation_job(self, job: str) -> DescribeSimulationJobResponseTypeDef:
        """
        [Client.describe_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deployment_jobs(
        self, filters: List[FilterTypeDef] = None, nextToken: str = None, maxResults: int = None
    ) -> ListDeploymentJobsResponseTypeDef:
        """
        [Client.list_deployment_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.list_deployment_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_fleets(
        self, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListFleetsResponseTypeDef:
        """
        [Client.list_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.list_fleets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_robot_applications(
        self,
        versionQualifier: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[FilterTypeDef] = None,
    ) -> ListRobotApplicationsResponseTypeDef:
        """
        [Client.list_robot_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.list_robot_applications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_robots(
        self, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListRobotsResponseTypeDef:
        """
        [Client.list_robots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.list_robots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_simulation_applications(
        self,
        versionQualifier: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[FilterTypeDef] = None,
    ) -> ListSimulationApplicationsResponseTypeDef:
        """
        [Client.list_simulation_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.list_simulation_applications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_simulation_jobs(
        self, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListSimulationJobsResponseTypeDef:
        """
        [Client.list_simulation_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.list_simulation_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_robot(self, fleet: str, robot: str) -> RegisterRobotResponseTypeDef:
        """
        [Client.register_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.register_robot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restart_simulation_job(self, job: str) -> Dict[str, Any]:
        """
        [Client.restart_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.restart_simulation_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def sync_deployment_job(
        self, clientRequestToken: str, fleet: str
    ) -> SyncDeploymentJobResponseTypeDef:
        """
        [Client.sync_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.sync_deployment_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_robot_application(
        self,
        application: str,
        sources: List[SourceConfigTypeDef],
        robotSoftwareSuite: RobotSoftwareSuiteTypeDef,
        currentRevisionId: str = None,
    ) -> UpdateRobotApplicationResponseTypeDef:
        """
        [Client.update_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.update_robot_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_simulation_application(
        self,
        application: str,
        sources: List[SourceConfigTypeDef],
        simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef,
        robotSoftwareSuite: RobotSoftwareSuiteTypeDef,
        renderingEngine: RenderingEngineTypeDef = None,
        currentRevisionId: str = None,
    ) -> UpdateSimulationApplicationResponseTypeDef:
        """
        [Client.update_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Client.update_simulation_application)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_deployment_jobs"]
    ) -> paginator_scope.ListDeploymentJobsPaginator:
        """
        [Paginator.ListDeploymentJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListDeploymentJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_fleets"]
    ) -> paginator_scope.ListFleetsPaginator:
        """
        [Paginator.ListFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListFleets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_robot_applications"]
    ) -> paginator_scope.ListRobotApplicationsPaginator:
        """
        [Paginator.ListRobotApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListRobotApplications)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_robots"]
    ) -> paginator_scope.ListRobotsPaginator:
        """
        [Paginator.ListRobots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListRobots)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_simulation_applications"]
    ) -> paginator_scope.ListSimulationApplicationsPaginator:
        """
        [Paginator.ListSimulationApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationApplications)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_simulation_jobs"]
    ) -> paginator_scope.ListSimulationJobsPaginator:
        """
        [Paginator.ListSimulationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobs)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentDeploymentException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError
