"Main interface for iot1click-projects service"
from mypy_boto3_iot1click_projects.client import (
    IoT1ClickProjectsClient,
    IoT1ClickProjectsClient as Client,
)
from mypy_boto3_iot1click_projects.paginator import ListPlacementsPaginator, ListProjectsPaginator


__all__ = ("Client", "IoT1ClickProjectsClient", "ListPlacementsPaginator", "ListProjectsPaginator")
