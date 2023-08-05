"Main interface for iot1click-projects service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iot1click_projects.type_defs import (
    ListPlacementsResponseTypeDef,
    ListProjectsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListPlacementsPaginator", "ListProjectsPaginator")


class ListPlacementsPaginator(Boto3Paginator):
    """
    [Paginator.ListPlacements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListPlacements)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, projectName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPlacementsResponseTypeDef, None, None]:
        """
        [ListPlacements.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListPlacements.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListProjects)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListProjectsResponseTypeDef, None, None]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListProjects.paginate)
        """
