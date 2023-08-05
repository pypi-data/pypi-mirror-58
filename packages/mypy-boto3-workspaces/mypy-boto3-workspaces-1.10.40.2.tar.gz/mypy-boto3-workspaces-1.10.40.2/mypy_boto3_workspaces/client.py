"Main interface for workspaces service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_workspaces.client as client_scope

# pylint: disable=import-self
import mypy_boto3_workspaces.paginator as paginator_scope
from mypy_boto3_workspaces.type_defs import (
    ClientPropertiesTypeDef,
    CopyWorkspaceImageResultTypeDef,
    CreateIpGroupResultTypeDef,
    CreateWorkspacesResultTypeDef,
    DescribeAccountModificationsResultTypeDef,
    DescribeAccountResultTypeDef,
    DescribeClientPropertiesResultTypeDef,
    DescribeIpGroupsResultTypeDef,
    DescribeTagsResultTypeDef,
    DescribeWorkspaceBundlesResultTypeDef,
    DescribeWorkspaceDirectoriesResultTypeDef,
    DescribeWorkspaceImagesResultTypeDef,
    DescribeWorkspaceSnapshotsResultTypeDef,
    DescribeWorkspacesConnectionStatusResultTypeDef,
    DescribeWorkspacesResultTypeDef,
    ImportWorkspaceImageResultTypeDef,
    IpRuleItemTypeDef,
    ListAvailableManagementCidrRangesResultTypeDef,
    RebootRequestTypeDef,
    RebootWorkspacesResultTypeDef,
    RebuildRequestTypeDef,
    RebuildWorkspacesResultTypeDef,
    SelfservicePermissionsTypeDef,
    StartRequestTypeDef,
    StartWorkspacesResultTypeDef,
    StopRequestTypeDef,
    StopWorkspacesResultTypeDef,
    TagTypeDef,
    TerminateRequestTypeDef,
    TerminateWorkspacesResultTypeDef,
    WorkspaceAccessPropertiesTypeDef,
    WorkspaceCreationPropertiesTypeDef,
    WorkspacePropertiesTypeDef,
    WorkspaceRequestTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WorkSpacesClient",)


class WorkSpacesClient(BaseClient):
    """
    [WorkSpaces.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_ip_groups(self, DirectoryId: str, GroupIds: List[str]) -> Dict[str, Any]:
        """
        [Client.associate_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.associate_ip_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_ip_rules(
        self, GroupId: str, UserRules: List[IpRuleItemTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.authorize_ip_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.authorize_ip_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_workspace_image(
        self,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        Description: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CopyWorkspaceImageResultTypeDef:
        """
        [Client.copy_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.copy_workspace_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_ip_group(
        self,
        GroupName: str,
        GroupDesc: str = None,
        UserRules: List[IpRuleItemTypeDef] = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateIpGroupResultTypeDef:
        """
        [Client.create_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.create_ip_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(self, ResourceId: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_workspaces(
        self, Workspaces: List[WorkspaceRequestTypeDef]
    ) -> CreateWorkspacesResultTypeDef:
        """
        [Client.create_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.create_workspaces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_ip_group(self, GroupId: str) -> Dict[str, Any]:
        """
        [Client.delete_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.delete_ip_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tags(self, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.delete_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_workspace_image(self, ImageId: str) -> Dict[str, Any]:
        """
        [Client.delete_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.delete_workspace_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_workspace_directory(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Client.deregister_workspace_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.deregister_workspace_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account(self) -> DescribeAccountResultTypeDef:
        """
        [Client.describe_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.describe_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_modifications(
        self, NextToken: str = None
    ) -> DescribeAccountModificationsResultTypeDef:
        """
        [Client.describe_account_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.describe_account_modifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_client_properties(
        self, ResourceIds: List[str]
    ) -> DescribeClientPropertiesResultTypeDef:
        """
        [Client.describe_client_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.describe_client_properties)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_ip_groups(
        self, GroupIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeIpGroupsResultTypeDef:
        """
        [Client.describe_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.describe_ip_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tags(self, ResourceId: str) -> DescribeTagsResultTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.describe_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_workspace_bundles(
        self, BundleIds: List[str] = None, Owner: str = None, NextToken: str = None
    ) -> DescribeWorkspaceBundlesResultTypeDef:
        """
        [Client.describe_workspace_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_bundles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_workspace_directories(
        self, DirectoryIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeWorkspaceDirectoriesResultTypeDef:
        """
        [Client.describe_workspace_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_directories)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_workspace_images(
        self, ImageIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeWorkspaceImagesResultTypeDef:
        """
        [Client.describe_workspace_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_images)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_workspace_snapshots(
        self, WorkspaceId: str
    ) -> DescribeWorkspaceSnapshotsResultTypeDef:
        """
        [Client.describe_workspace_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_workspaces(
        self,
        WorkspaceIds: List[str] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeWorkspacesResultTypeDef:
        """
        [Client.describe_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_workspaces_connection_status(
        self, WorkspaceIds: List[str] = None, NextToken: str = None
    ) -> DescribeWorkspacesConnectionStatusResultTypeDef:
        """
        [Client.describe_workspaces_connection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces_connection_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_ip_groups(self, DirectoryId: str, GroupIds: List[str]) -> Dict[str, Any]:
        """
        [Client.disassociate_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.disassociate_ip_groups)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_workspace_image(
        self,
        Ec2ImageId: str,
        IngestionProcess: Literal["BYOL_REGULAR", "BYOL_GRAPHICS", "BYOL_GRAPHICSPRO"],
        ImageName: str,
        ImageDescription: str,
        Tags: List[TagTypeDef] = None,
    ) -> ImportWorkspaceImageResultTypeDef:
        """
        [Client.import_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.import_workspace_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_available_management_cidr_ranges(
        self, ManagementCidrRangeConstraint: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAvailableManagementCidrRangesResultTypeDef:
        """
        [Client.list_available_management_cidr_ranges documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.list_available_management_cidr_ranges)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_account(
        self,
        DedicatedTenancySupport: Literal["ENABLED"] = None,
        DedicatedTenancyManagementCidrRange: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.modify_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.modify_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_client_properties(
        self, ResourceId: str, ClientProperties: ClientPropertiesTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.modify_client_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.modify_client_properties)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_selfservice_permissions(
        self, ResourceId: str, SelfservicePermissions: SelfservicePermissionsTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.modify_selfservice_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.modify_selfservice_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_workspace_access_properties(
        self, ResourceId: str, WorkspaceAccessProperties: WorkspaceAccessPropertiesTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_access_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_access_properties)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_workspace_creation_properties(
        self, ResourceId: str, WorkspaceCreationProperties: WorkspaceCreationPropertiesTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_creation_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_creation_properties)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_workspace_properties(
        self, WorkspaceId: str, WorkspaceProperties: WorkspacePropertiesTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_properties)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_workspace_state(
        self, WorkspaceId: str, WorkspaceState: Literal["AVAILABLE", "ADMIN_MAINTENANCE"]
    ) -> Dict[str, Any]:
        """
        [Client.modify_workspace_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_state)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot_workspaces(
        self, RebootWorkspaceRequests: List[RebootRequestTypeDef]
    ) -> RebootWorkspacesResultTypeDef:
        """
        [Client.reboot_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.reboot_workspaces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def rebuild_workspaces(
        self, RebuildWorkspaceRequests: List[RebuildRequestTypeDef]
    ) -> RebuildWorkspacesResultTypeDef:
        """
        [Client.rebuild_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.rebuild_workspaces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_workspace_directory(
        self,
        DirectoryId: str,
        EnableWorkDocs: bool,
        SubnetIds: List[str] = None,
        EnableSelfService: bool = None,
        Tenancy: Literal["DEDICATED", "SHARED"] = None,
        Tags: List[TagTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.register_workspace_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.register_workspace_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_workspace(self, WorkspaceId: str) -> Dict[str, Any]:
        """
        [Client.restore_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.restore_workspace)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_ip_rules(self, GroupId: str, UserRules: List[str]) -> Dict[str, Any]:
        """
        [Client.revoke_ip_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.revoke_ip_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_workspaces(
        self, StartWorkspaceRequests: List[StartRequestTypeDef]
    ) -> StartWorkspacesResultTypeDef:
        """
        [Client.start_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.start_workspaces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_workspaces(
        self, StopWorkspaceRequests: List[StopRequestTypeDef]
    ) -> StopWorkspacesResultTypeDef:
        """
        [Client.stop_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.stop_workspaces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate_workspaces(
        self, TerminateWorkspaceRequests: List[TerminateRequestTypeDef]
    ) -> TerminateWorkspacesResultTypeDef:
        """
        [Client.terminate_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.terminate_workspaces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_rules_of_ip_group(
        self, GroupId: str, UserRules: List[IpRuleItemTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.update_rules_of_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Client.update_rules_of_ip_group)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_account_modifications"]
    ) -> paginator_scope.DescribeAccountModificationsPaginator:
        """
        [Paginator.DescribeAccountModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_ip_groups"]
    ) -> paginator_scope.DescribeIpGroupsPaginator:
        """
        [Paginator.DescribeIpGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_workspace_bundles"]
    ) -> paginator_scope.DescribeWorkspaceBundlesPaginator:
        """
        [Paginator.DescribeWorkspaceBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_workspace_directories"]
    ) -> paginator_scope.DescribeWorkspaceDirectoriesPaginator:
        """
        [Paginator.DescribeWorkspaceDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_workspace_images"]
    ) -> paginator_scope.DescribeWorkspaceImagesPaginator:
        """
        [Paginator.DescribeWorkspaceImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_workspaces"]
    ) -> paginator_scope.DescribeWorkspacesPaginator:
        """
        [Paginator.DescribeWorkspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_workspaces_connection_status"]
    ) -> paginator_scope.DescribeWorkspacesConnectionStatusPaginator:
        """
        [Paginator.DescribeWorkspacesConnectionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_available_management_cidr_ranges"]
    ) -> paginator_scope.ListAvailableManagementCidrRangesPaginator:
        """
        [Paginator.ListAvailableManagementCidrRanges documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidParameterValuesException: Boto3ClientError
    InvalidResourceStateException: Boto3ClientError
    OperationInProgressException: Boto3ClientError
    OperationNotSupportedException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceAssociatedException: Boto3ClientError
    ResourceCreationFailedException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceUnavailableException: Boto3ClientError
    UnsupportedNetworkConfigurationException: Boto3ClientError
    UnsupportedWorkspaceConfigurationException: Boto3ClientError
    WorkspacesDefaultRoleNotFoundException: Boto3ClientError
