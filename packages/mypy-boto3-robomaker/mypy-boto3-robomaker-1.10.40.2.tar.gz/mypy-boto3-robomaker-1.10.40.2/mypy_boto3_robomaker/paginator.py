"Main interface for robomaker service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_robomaker.type_defs import (
    FilterTypeDef,
    ListDeploymentJobsResponseTypeDef,
    ListFleetsResponseTypeDef,
    ListRobotApplicationsResponseTypeDef,
    ListRobotsResponseTypeDef,
    ListSimulationApplicationsResponseTypeDef,
    ListSimulationJobsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListDeploymentJobsPaginator",
    "ListFleetsPaginator",
    "ListRobotApplicationsPaginator",
    "ListRobotsPaginator",
    "ListSimulationApplicationsPaginator",
    "ListSimulationJobsPaginator",
)


class ListDeploymentJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeploymentJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListDeploymentJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDeploymentJobsResponseTypeDef, None, None]:
        """
        [ListDeploymentJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListDeploymentJobs.paginate)
        """


class ListFleetsPaginator(Boto3Paginator):
    """
    [Paginator.ListFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListFleets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListFleetsResponseTypeDef, None, None]:
        """
        [ListFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListFleets.paginate)
        """


class ListRobotApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListRobotApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListRobotApplications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        versionQualifier: str = None,
        filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListRobotApplicationsResponseTypeDef, None, None]:
        """
        [ListRobotApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListRobotApplications.paginate)
        """


class ListRobotsPaginator(Boto3Paginator):
    """
    [Paginator.ListRobots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListRobots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListRobotsResponseTypeDef, None, None]:
        """
        [ListRobots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListRobots.paginate)
        """


class ListSimulationApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListSimulationApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationApplications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        versionQualifier: str = None,
        filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListSimulationApplicationsResponseTypeDef, None, None]:
        """
        [ListSimulationApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationApplications.paginate)
        """


class ListSimulationJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListSimulationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListSimulationJobsResponseTypeDef, None, None]:
        """
        [ListSimulationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobs.paginate)
        """
