"Main interface for workdocs service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_workdocs.client as client_scope

# pylint: disable=import-self
import mypy_boto3_workdocs.paginator as paginator_scope
from mypy_boto3_workdocs.type_defs import (
    ActivateUserResponseTypeDef,
    AddResourcePermissionsResponseTypeDef,
    CreateCommentResponseTypeDef,
    CreateFolderResponseTypeDef,
    CreateNotificationSubscriptionResponseTypeDef,
    CreateUserResponseTypeDef,
    DescribeActivitiesResponseTypeDef,
    DescribeCommentsResponseTypeDef,
    DescribeDocumentVersionsResponseTypeDef,
    DescribeFolderContentsResponseTypeDef,
    DescribeGroupsResponseTypeDef,
    DescribeNotificationSubscriptionsResponseTypeDef,
    DescribeResourcePermissionsResponseTypeDef,
    DescribeRootFoldersResponseTypeDef,
    DescribeUsersResponseTypeDef,
    GetCurrentUserResponseTypeDef,
    GetDocumentPathResponseTypeDef,
    GetDocumentResponseTypeDef,
    GetDocumentVersionResponseTypeDef,
    GetFolderPathResponseTypeDef,
    GetFolderResponseTypeDef,
    GetResourcesResponseTypeDef,
    InitiateDocumentVersionUploadResponseTypeDef,
    NotificationOptionsTypeDef,
    SharePrincipalTypeDef,
    StorageRuleTypeTypeDef,
    UpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WorkDocsClient",)


class WorkDocsClient(BaseClient):
    """
    [WorkDocs.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def abort_document_version_upload(
        self, DocumentId: str, VersionId: str, AuthenticationToken: str = None
    ) -> None:
        """
        [Client.abort_document_version_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.abort_document_version_upload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate_user(
        self, UserId: str, AuthenticationToken: str = None
    ) -> ActivateUserResponseTypeDef:
        """
        [Client.activate_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.activate_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_resource_permissions(
        self,
        ResourceId: str,
        Principals: List[SharePrincipalTypeDef],
        AuthenticationToken: str = None,
        NotificationOptions: NotificationOptionsTypeDef = None,
    ) -> AddResourcePermissionsResponseTypeDef:
        """
        [Client.add_resource_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.add_resource_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_comment(
        self,
        DocumentId: str,
        VersionId: str,
        Text: str,
        AuthenticationToken: str = None,
        ParentId: str = None,
        ThreadId: str = None,
        Visibility: Literal["PUBLIC", "PRIVATE"] = None,
        NotifyCollaborators: bool = None,
    ) -> CreateCommentResponseTypeDef:
        """
        [Client.create_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.create_comment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_custom_metadata(
        self,
        ResourceId: str,
        CustomMetadata: Dict[str, str],
        AuthenticationToken: str = None,
        VersionId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_custom_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.create_custom_metadata)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_folder(
        self, ParentFolderId: str, AuthenticationToken: str = None, Name: str = None
    ) -> CreateFolderResponseTypeDef:
        """
        [Client.create_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.create_folder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_labels(
        self, ResourceId: str, Labels: List[str], AuthenticationToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.create_labels)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_notification_subscription(
        self,
        OrganizationId: str,
        Endpoint: str,
        Protocol: Literal["HTTPS"],
        SubscriptionType: Literal["ALL"],
    ) -> CreateNotificationSubscriptionResponseTypeDef:
        """
        [Client.create_notification_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.create_notification_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user(
        self,
        Username: str,
        GivenName: str,
        Surname: str,
        Password: str,
        OrganizationId: str = None,
        EmailAddress: str = None,
        TimeZoneId: str = None,
        StorageRule: StorageRuleTypeTypeDef = None,
        AuthenticationToken: str = None,
    ) -> CreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.create_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate_user(self, UserId: str, AuthenticationToken: str = None) -> None:
        """
        [Client.deactivate_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.deactivate_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_comment(
        self, DocumentId: str, VersionId: str, CommentId: str, AuthenticationToken: str = None
    ) -> None:
        """
        [Client.delete_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.delete_comment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_custom_metadata(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        VersionId: str = None,
        Keys: List[str] = None,
        DeleteAll: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.delete_custom_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.delete_custom_metadata)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_document(self, DocumentId: str, AuthenticationToken: str = None) -> None:
        """
        [Client.delete_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.delete_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_folder(self, FolderId: str, AuthenticationToken: str = None) -> None:
        """
        [Client.delete_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.delete_folder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_folder_contents(self, FolderId: str, AuthenticationToken: str = None) -> None:
        """
        [Client.delete_folder_contents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.delete_folder_contents)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_labels(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        Labels: List[str] = None,
        DeleteAll: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.delete_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.delete_labels)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_notification_subscription(self, SubscriptionId: str, OrganizationId: str) -> None:
        """
        [Client.delete_notification_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.delete_notification_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user(self, UserId: str, AuthenticationToken: str = None) -> None:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.delete_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_activities(
        self,
        AuthenticationToken: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OrganizationId: str = None,
        ActivityTypes: str = None,
        ResourceId: str = None,
        UserId: str = None,
        IncludeIndirectActivities: bool = None,
        Limit: int = None,
        Marker: str = None,
    ) -> DescribeActivitiesResponseTypeDef:
        """
        [Client.describe_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.describe_activities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_comments(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Marker: str = None,
    ) -> DescribeCommentsResponseTypeDef:
        """
        [Client.describe_comments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.describe_comments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_document_versions(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Marker: str = None,
        Limit: int = None,
        Include: str = None,
        Fields: str = None,
    ) -> DescribeDocumentVersionsResponseTypeDef:
        """
        [Client.describe_document_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.describe_document_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_folder_contents(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Sort: Literal["DATE", "NAME"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Limit: int = None,
        Marker: str = None,
        Type: Literal["ALL", "DOCUMENT", "FOLDER"] = None,
        Include: str = None,
    ) -> DescribeFolderContentsResponseTypeDef:
        """
        [Client.describe_folder_contents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.describe_folder_contents)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_groups(
        self,
        SearchQuery: str,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        Marker: str = None,
        Limit: int = None,
    ) -> DescribeGroupsResponseTypeDef:
        """
        [Client.describe_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.describe_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_notification_subscriptions(
        self, OrganizationId: str, Marker: str = None, Limit: int = None
    ) -> DescribeNotificationSubscriptionsResponseTypeDef:
        """
        [Client.describe_notification_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.describe_notification_subscriptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_resource_permissions(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        PrincipalId: str = None,
        Limit: int = None,
        Marker: str = None,
    ) -> DescribeResourcePermissionsResponseTypeDef:
        """
        [Client.describe_resource_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.describe_resource_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_root_folders(
        self, AuthenticationToken: str, Limit: int = None, Marker: str = None
    ) -> DescribeRootFoldersResponseTypeDef:
        """
        [Client.describe_root_folders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.describe_root_folders)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_users(
        self,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        UserIds: str = None,
        Query: str = None,
        Include: Literal["ALL", "ACTIVE_PENDING"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Sort: Literal[
            "USER_NAME", "FULL_NAME", "STORAGE_LIMIT", "USER_STATUS", "STORAGE_USED"
        ] = None,
        Marker: str = None,
        Limit: int = None,
        Fields: str = None,
    ) -> DescribeUsersResponseTypeDef:
        """
        [Client.describe_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.describe_users)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_current_user(self, AuthenticationToken: str) -> GetCurrentUserResponseTypeDef:
        """
        [Client.get_current_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.get_current_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_document(
        self, DocumentId: str, AuthenticationToken: str = None, IncludeCustomMetadata: bool = None
    ) -> GetDocumentResponseTypeDef:
        """
        [Client.get_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.get_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_document_path(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Fields: str = None,
        Marker: str = None,
    ) -> GetDocumentPathResponseTypeDef:
        """
        [Client.get_document_path documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.get_document_path)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_document_version(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        Fields: str = None,
        IncludeCustomMetadata: bool = None,
    ) -> GetDocumentVersionResponseTypeDef:
        """
        [Client.get_document_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.get_document_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_folder(
        self, FolderId: str, AuthenticationToken: str = None, IncludeCustomMetadata: bool = None
    ) -> GetFolderResponseTypeDef:
        """
        [Client.get_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.get_folder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_folder_path(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Fields: str = None,
        Marker: str = None,
    ) -> GetFolderPathResponseTypeDef:
        """
        [Client.get_folder_path documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.get_folder_path)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resources(
        self,
        AuthenticationToken: str = None,
        UserId: str = None,
        CollectionType: Literal["SHARED_WITH_ME"] = None,
        Limit: int = None,
        Marker: str = None,
    ) -> GetResourcesResponseTypeDef:
        """
        [Client.get_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.get_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_document_version_upload(
        self,
        ParentFolderId: str,
        AuthenticationToken: str = None,
        Id: str = None,
        Name: str = None,
        ContentCreatedTimestamp: datetime = None,
        ContentModifiedTimestamp: datetime = None,
        ContentType: str = None,
        DocumentSizeInBytes: int = None,
    ) -> InitiateDocumentVersionUploadResponseTypeDef:
        """
        [Client.initiate_document_version_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.initiate_document_version_upload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_all_resource_permissions(
        self, ResourceId: str, AuthenticationToken: str = None
    ) -> None:
        """
        [Client.remove_all_resource_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.remove_all_resource_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_resource_permission(
        self,
        ResourceId: str,
        PrincipalId: str,
        AuthenticationToken: str = None,
        PrincipalType: Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"] = None,
    ) -> None:
        """
        [Client.remove_resource_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.remove_resource_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_document(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Name: str = None,
        ParentFolderId: str = None,
        ResourceState: Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"] = None,
    ) -> None:
        """
        [Client.update_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.update_document)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_document_version(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        VersionStatus: Literal["ACTIVE"] = None,
    ) -> None:
        """
        [Client.update_document_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.update_document_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_folder(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Name: str = None,
        ParentFolderId: str = None,
        ResourceState: Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"] = None,
    ) -> None:
        """
        [Client.update_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.update_folder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user(
        self,
        UserId: str,
        AuthenticationToken: str = None,
        GivenName: str = None,
        Surname: str = None,
        Type: Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"] = None,
        StorageRule: StorageRuleTypeTypeDef = None,
        TimeZoneId: str = None,
        Locale: Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ] = None,
        GrantPoweruserPrivileges: Literal["TRUE", "FALSE"] = None,
    ) -> UpdateUserResponseTypeDef:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Client.update_user)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_activities"]
    ) -> paginator_scope.DescribeActivitiesPaginator:
        """
        [Paginator.DescribeActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_comments"]
    ) -> paginator_scope.DescribeCommentsPaginator:
        """
        [Paginator.DescribeComments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_document_versions"]
    ) -> paginator_scope.DescribeDocumentVersionsPaginator:
        """
        [Paginator.DescribeDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_folder_contents"]
    ) -> paginator_scope.DescribeFolderContentsPaginator:
        """
        [Paginator.DescribeFolderContents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_groups"]
    ) -> paginator_scope.DescribeGroupsPaginator:
        """
        [Paginator.DescribeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_notification_subscriptions"]
    ) -> paginator_scope.DescribeNotificationSubscriptionsPaginator:
        """
        [Paginator.DescribeNotificationSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_resource_permissions"]
    ) -> paginator_scope.DescribeResourcePermissionsPaginator:
        """
        [Paginator.DescribeResourcePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_root_folders"]
    ) -> paginator_scope.DescribeRootFoldersPaginator:
        """
        [Paginator.DescribeRootFolders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_users"]
    ) -> paginator_scope.DescribeUsersPaginator:
        """
        [Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    ConflictingOperationException: Boto3ClientError
    CustomMetadataLimitExceededException: Boto3ClientError
    DeactivatingLastSystemUserException: Boto3ClientError
    DocumentLockedForCommentsException: Boto3ClientError
    DraftUploadOutOfSyncException: Boto3ClientError
    EntityAlreadyExistsException: Boto3ClientError
    EntityNotExistsException: Boto3ClientError
    FailedDependencyException: Boto3ClientError
    IllegalUserStateException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidCommentOperationException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    InvalidPasswordException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ProhibitedStateException: Boto3ClientError
    RequestedEntityTooLargeException: Boto3ClientError
    ResourceAlreadyCheckedOutException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    StorageLimitExceededException: Boto3ClientError
    StorageLimitWillExceedException: Boto3ClientError
    TooManyLabelsException: Boto3ClientError
    TooManySubscriptionsException: Boto3ClientError
    UnauthorizedOperationException: Boto3ClientError
    UnauthorizedResourceAccessException: Boto3ClientError
