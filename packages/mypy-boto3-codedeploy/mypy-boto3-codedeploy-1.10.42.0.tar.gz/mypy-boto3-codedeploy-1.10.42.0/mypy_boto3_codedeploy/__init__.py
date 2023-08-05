"Main interface for codedeploy service"
from mypy_boto3_codedeploy.client import CodeDeployClient as Client, CodeDeployClient
from mypy_boto3_codedeploy.paginator import (
    ListApplicationRevisionsPaginator,
    ListApplicationsPaginator,
    ListDeploymentConfigsPaginator,
    ListDeploymentGroupsPaginator,
    ListDeploymentInstancesPaginator,
    ListDeploymentTargetsPaginator,
    ListDeploymentsPaginator,
    ListGitHubAccountTokenNamesPaginator,
    ListOnPremisesInstancesPaginator,
)
from mypy_boto3_codedeploy.waiter import DeploymentSuccessfulWaiter


__all__ = (
    "Client",
    "CodeDeployClient",
    "DeploymentSuccessfulWaiter",
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
