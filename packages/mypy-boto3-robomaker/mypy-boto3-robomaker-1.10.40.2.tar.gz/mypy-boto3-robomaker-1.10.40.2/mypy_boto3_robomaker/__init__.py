"Main interface for robomaker service"
from mypy_boto3_robomaker.client import RoboMakerClient as Client, RoboMakerClient
from mypy_boto3_robomaker.paginator import (
    ListDeploymentJobsPaginator,
    ListFleetsPaginator,
    ListRobotApplicationsPaginator,
    ListRobotsPaginator,
    ListSimulationApplicationsPaginator,
    ListSimulationJobsPaginator,
)


__all__ = (
    "Client",
    "ListDeploymentJobsPaginator",
    "ListFleetsPaginator",
    "ListRobotApplicationsPaginator",
    "ListRobotsPaginator",
    "ListSimulationApplicationsPaginator",
    "ListSimulationJobsPaginator",
    "RoboMakerClient",
)
