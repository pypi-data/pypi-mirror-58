"Main interface for codedeploy service Paginators"
from __future__ import annotations

import sys
from typing import Dict, Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codedeploy.type_defs import (
    ListApplicationRevisionsOutputTypeDef,
    ListApplicationsOutputTypeDef,
    ListDeploymentConfigsOutputTypeDef,
    ListDeploymentGroupsOutputTypeDef,
    ListDeploymentInstancesOutputTypeDef,
    ListDeploymentTargetsOutputTypeDef,
    ListDeploymentsOutputTypeDef,
    ListGitHubAccountTokenNamesOutputTypeDef,
    ListOnPremisesInstancesOutputTypeDef,
    PaginatorConfigTypeDef,
    TagFilterTypeDef,
    TimeRangeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListApplicationRevisionsPaginator",
    "ListApplicationsPaginator",
    "ListDeploymentConfigsPaginator",
    "ListDeploymentGroupsPaginator",
    "ListDeploymentInstancesPaginator",
    "ListDeploymentTargetsPaginator",
    "ListDeploymentsPaginator",
    "ListGitHubAccountTokenNamesPaginator",
    "ListOnPremisesInstancesPaginator",
)


class ListApplicationRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.ListApplicationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplicationRevisions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        applicationName: str,
        sortBy: Literal["registerTime", "firstUsedTime", "lastUsedTime"] = None,
        sortOrder: Literal["ascending", "descending"] = None,
        s3Bucket: str = None,
        s3KeyPrefix: str = None,
        deployed: Literal["include", "exclude", "ignore"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListApplicationRevisionsOutputTypeDef, None, None]:
        """
        [ListApplicationRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplicationRevisions.paginate)
        """


class ListApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListApplicationsOutputTypeDef, None, None]:
        """
        [ListApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplications.paginate)
        """


class ListDeploymentConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeploymentConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentConfigs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDeploymentConfigsOutputTypeDef, None, None]:
        """
        [ListDeploymentConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentConfigs.paginate)
        """


class ListDeploymentGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeploymentGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, applicationName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListDeploymentGroupsOutputTypeDef, None, None]:
        """
        [ListDeploymentGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentGroups.paginate)
        """


class ListDeploymentInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListDeploymentInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        deploymentId: str,
        instanceStatusFilter: List[
            Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"]
        ] = None,
        instanceTypeFilter: List[Literal["Blue", "Green"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDeploymentInstancesOutputTypeDef, None, None]:
        """
        [ListDeploymentInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentInstances.paginate)
        """


class ListDeploymentTargetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeploymentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentTargets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        deploymentId: str = None,
        targetFilters: Dict[Literal["TargetStatus", "ServerInstanceLabel"], List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDeploymentTargetsOutputTypeDef, None, None]:
        """
        [ListDeploymentTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentTargets.paginate)
        """


class ListDeploymentsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeployments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        applicationName: str = None,
        deploymentGroupName: str = None,
        includeOnlyStatuses: List[
            Literal["Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"]
        ] = None,
        createTimeRange: TimeRangeTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDeploymentsOutputTypeDef, None, None]:
        """
        [ListDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeployments.paginate)
        """


class ListGitHubAccountTokenNamesPaginator(Boto3Paginator):
    """
    [Paginator.ListGitHubAccountTokenNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGitHubAccountTokenNamesOutputTypeDef, None, None]:
        """
        [ListGitHubAccountTokenNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames.paginate)
        """


class ListOnPremisesInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListOnPremisesInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListOnPremisesInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        registrationStatus: Literal["Registered", "Deregistered"] = None,
        tagFilters: List[TagFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListOnPremisesInstancesOutputTypeDef, None, None]:
        """
        [ListOnPremisesInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/codedeploy.html#CodeDeploy.Paginator.ListOnPremisesInstances.paginate)
        """
