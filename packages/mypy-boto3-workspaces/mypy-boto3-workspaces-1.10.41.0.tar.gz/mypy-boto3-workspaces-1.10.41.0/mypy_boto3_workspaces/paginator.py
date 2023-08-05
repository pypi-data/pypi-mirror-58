"Main interface for workspaces service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_workspaces.type_defs import (
    DescribeAccountModificationsResultTypeDef,
    DescribeIpGroupsResultTypeDef,
    DescribeWorkspaceBundlesResultTypeDef,
    DescribeWorkspaceDirectoriesResultTypeDef,
    DescribeWorkspaceImagesResultTypeDef,
    DescribeWorkspacesConnectionStatusResultTypeDef,
    DescribeWorkspacesResultTypeDef,
    ListAvailableManagementCidrRangesResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeAccountModificationsPaginator",
    "DescribeIpGroupsPaginator",
    "DescribeWorkspaceBundlesPaginator",
    "DescribeWorkspaceDirectoriesPaginator",
    "DescribeWorkspaceImagesPaginator",
    "DescribeWorkspacesPaginator",
    "DescribeWorkspacesConnectionStatusPaginator",
    "ListAvailableManagementCidrRangesPaginator",
)


class DescribeAccountModificationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAccountModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeAccountModificationsResultTypeDef, None, None]:
        """
        [DescribeAccountModifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications.paginate)
        """


class DescribeIpGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeIpGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GroupIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeIpGroupsResultTypeDef, None, None]:
        """
        [DescribeIpGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups.paginate)
        """


class DescribeWorkspaceBundlesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeWorkspaceBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        BundleIds: List[str] = None,
        Owner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeWorkspaceBundlesResultTypeDef, None, None]:
        """
        [DescribeWorkspaceBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles.paginate)
        """


class DescribeWorkspaceDirectoriesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeWorkspaceDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryIds: List[str] = None,
        Limit: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeWorkspaceDirectoriesResultTypeDef, None, None]:
        """
        [DescribeWorkspaceDirectories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories.paginate)
        """


class DescribeWorkspaceImagesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeWorkspaceImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ImageIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeWorkspaceImagesResultTypeDef, None, None]:
        """
        [DescribeWorkspaceImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages.paginate)
        """


class DescribeWorkspacesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeWorkspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WorkspaceIds: List[str] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeWorkspacesResultTypeDef, None, None]:
        """
        [DescribeWorkspaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces.paginate)
        """


class DescribeWorkspacesConnectionStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeWorkspacesConnectionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, WorkspaceIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeWorkspacesConnectionStatusResultTypeDef, None, None]:
        """
        [DescribeWorkspacesConnectionStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus.paginate)
        """


class ListAvailableManagementCidrRangesPaginator(Boto3Paginator):
    """
    [Paginator.ListAvailableManagementCidrRanges documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ManagementCidrRangeConstraint: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAvailableManagementCidrRangesResultTypeDef, None, None]:
        """
        [ListAvailableManagementCidrRanges.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges.paginate)
        """
