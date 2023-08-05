"Main interface for iot1click-projects service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_iot1click_projects.client as client_scope

# pylint: disable=import-self
import mypy_boto3_iot1click_projects.paginator as paginator_scope
from mypy_boto3_iot1click_projects.type_defs import (
    DescribePlacementResponseTypeDef,
    DescribeProjectResponseTypeDef,
    GetDevicesInPlacementResponseTypeDef,
    ListPlacementsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PlacementTemplateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoT1ClickProjectsClient",)


class IoT1ClickProjectsClient(BaseClient):
    """
    [IoT1ClickProjects.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_device_with_placement(
        self, projectName: str, placementName: str, deviceId: str, deviceTemplateName: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_device_with_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.associate_device_with_placement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_placement(
        self, placementName: str, projectName: str, attributes: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Client.create_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.create_placement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_project(
        self,
        projectName: str,
        description: str = None,
        placementTemplate: PlacementTemplateTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.create_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_placement(self, placementName: str, projectName: str) -> Dict[str, Any]:
        """
        [Client.delete_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.delete_placement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_project(self, projectName: str) -> Dict[str, Any]:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.delete_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_placement(
        self, placementName: str, projectName: str
    ) -> DescribePlacementResponseTypeDef:
        """
        [Client.describe_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.describe_placement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_project(self, projectName: str) -> DescribeProjectResponseTypeDef:
        """
        [Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.describe_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_device_from_placement(
        self, projectName: str, placementName: str, deviceTemplateName: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_device_from_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.disassociate_device_from_placement)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_devices_in_placement(
        self, projectName: str, placementName: str
    ) -> GetDevicesInPlacementResponseTypeDef:
        """
        [Client.get_devices_in_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.get_devices_in_placement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_placements(
        self, projectName: str, nextToken: str = None, maxResults: int = None
    ) -> ListPlacementsResponseTypeDef:
        """
        [Client.list_placements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_placements)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_projects(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListProjectsResponseTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_projects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_placement(
        self, placementName: str, projectName: str, attributes: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Client.update_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.update_placement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_project(
        self,
        projectName: str,
        description: str = None,
        placementTemplate: PlacementTemplateTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.update_project)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_placements"]
    ) -> paginator_scope.ListPlacementsPaginator:
        """
        [Paginator.ListPlacements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListPlacements)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_projects"]
    ) -> paginator_scope.ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListProjects)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
