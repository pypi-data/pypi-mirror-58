"Main interface for workdocs service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_workdocs.type_defs import (
    DescribeActivitiesResponseTypeDef,
    DescribeCommentsResponseTypeDef,
    DescribeDocumentVersionsResponseTypeDef,
    DescribeFolderContentsResponseTypeDef,
    DescribeGroupsResponseTypeDef,
    DescribeNotificationSubscriptionsResponseTypeDef,
    DescribeResourcePermissionsResponseTypeDef,
    DescribeRootFoldersResponseTypeDef,
    DescribeUsersResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeActivitiesPaginator",
    "DescribeCommentsPaginator",
    "DescribeDocumentVersionsPaginator",
    "DescribeFolderContentsPaginator",
    "DescribeGroupsPaginator",
    "DescribeNotificationSubscriptionsPaginator",
    "DescribeResourcePermissionsPaginator",
    "DescribeRootFoldersPaginator",
    "DescribeUsersPaginator",
)


class DescribeActivitiesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AuthenticationToken: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OrganizationId: str = None,
        ActivityTypes: str = None,
        ResourceId: str = None,
        UserId: str = None,
        IncludeIndirectActivities: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeActivitiesResponseTypeDef, None, None]:
        """
        [DescribeActivities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities.paginate)
        """


class DescribeCommentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeComments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeCommentsResponseTypeDef, None, None]:
        """
        [DescribeComments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments.paginate)
        """


class DescribeDocumentVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Include: str = None,
        Fields: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeDocumentVersionsResponseTypeDef, None, None]:
        """
        [DescribeDocumentVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions.paginate)
        """


class DescribeFolderContentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFolderContents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Sort: Literal["DATE", "NAME"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Type: Literal["ALL", "DOCUMENT", "FOLDER"] = None,
        Include: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeFolderContentsResponseTypeDef, None, None]:
        """
        [DescribeFolderContents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents.paginate)
        """


class DescribeGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SearchQuery: str,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeGroupsResponseTypeDef, None, None]:
        """
        [DescribeGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups.paginate)
        """


class DescribeNotificationSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNotificationSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, OrganizationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeNotificationSubscriptionsResponseTypeDef, None, None]:
        """
        [DescribeNotificationSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions.paginate)
        """


class DescribeResourcePermissionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeResourcePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        PrincipalId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeResourcePermissionsResponseTypeDef, None, None]:
        """
        [DescribeResourcePermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions.paginate)
        """


class DescribeRootFoldersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRootFolders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, AuthenticationToken: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeRootFoldersResponseTypeDef, None, None]:
        """
        [DescribeRootFolders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders.paginate)
        """


class DescribeUsersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
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
        Fields: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeUsersResponseTypeDef, None, None]:
        """
        [DescribeUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers.paginate)
        """
