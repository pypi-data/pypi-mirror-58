"Main interface for iot1click-projects service"
from mypy_boto3_iot1click_projects.client import (
    IoT1ClickProjectsClient as Client,
    IoT1ClickProjectsClient,
)
from mypy_boto3_iot1click_projects.paginator import ListPlacementsPaginator, ListProjectsPaginator


__all__ = ("Client", "IoT1ClickProjectsClient", "ListPlacementsPaginator", "ListProjectsPaginator")
