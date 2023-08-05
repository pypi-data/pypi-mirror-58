"Main interface for quicksight service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_quicksight.client as client_scope
from mypy_boto3_quicksight.type_defs import (
    CancelIngestionResponseTypeDef,
    ColumnGroupTypeDef,
    CreateDashboardResponseTypeDef,
    CreateDataSetResponseTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateGroupMembershipResponseTypeDef,
    CreateGroupResponseTypeDef,
    CreateIAMPolicyAssignmentResponseTypeDef,
    CreateIngestionResponseTypeDef,
    CreateTemplateAliasResponseTypeDef,
    CreateTemplateResponseTypeDef,
    DashboardPublishOptionsTypeDef,
    DashboardSourceEntityTypeDef,
    DataSourceCredentialsTypeDef,
    DataSourceParametersTypeDef,
    DeleteDashboardResponseTypeDef,
    DeleteDataSetResponseTypeDef,
    DeleteDataSourceResponseTypeDef,
    DeleteGroupMembershipResponseTypeDef,
    DeleteGroupResponseTypeDef,
    DeleteIAMPolicyAssignmentResponseTypeDef,
    DeleteTemplateAliasResponseTypeDef,
    DeleteTemplateResponseTypeDef,
    DeleteUserByPrincipalIdResponseTypeDef,
    DeleteUserResponseTypeDef,
    DescribeDashboardPermissionsResponseTypeDef,
    DescribeDashboardResponseTypeDef,
    DescribeDataSetPermissionsResponseTypeDef,
    DescribeDataSetResponseTypeDef,
    DescribeDataSourcePermissionsResponseTypeDef,
    DescribeDataSourceResponseTypeDef,
    DescribeGroupResponseTypeDef,
    DescribeIAMPolicyAssignmentResponseTypeDef,
    DescribeIngestionResponseTypeDef,
    DescribeTemplateAliasResponseTypeDef,
    DescribeTemplatePermissionsResponseTypeDef,
    DescribeTemplateResponseTypeDef,
    DescribeUserResponseTypeDef,
    GetDashboardEmbedUrlResponseTypeDef,
    ListDashboardVersionsResponseTypeDef,
    ListDashboardsResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListGroupMembershipsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListIAMPolicyAssignmentsForUserResponseTypeDef,
    ListIAMPolicyAssignmentsResponseTypeDef,
    ListIngestionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateAliasesResponseTypeDef,
    ListTemplateVersionsResponseTypeDef,
    ListTemplatesResponseTypeDef,
    ListUserGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    LogicalTableTypeDef,
    ParametersTypeDef,
    PhysicalTableTypeDef,
    RegisterUserResponseTypeDef,
    ResourcePermissionTypeDef,
    RowLevelPermissionDataSetTypeDef,
    SslPropertiesTypeDef,
    TagResourceResponseTypeDef,
    TagTypeDef,
    TemplateSourceEntityTypeDef,
    UntagResourceResponseTypeDef,
    UpdateDashboardPermissionsResponseTypeDef,
    UpdateDashboardPublishedVersionResponseTypeDef,
    UpdateDashboardResponseTypeDef,
    UpdateDataSetPermissionsResponseTypeDef,
    UpdateDataSetResponseTypeDef,
    UpdateDataSourcePermissionsResponseTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateGroupResponseTypeDef,
    UpdateIAMPolicyAssignmentResponseTypeDef,
    UpdateTemplateAliasResponseTypeDef,
    UpdateTemplatePermissionsResponseTypeDef,
    UpdateTemplateResponseTypeDef,
    UpdateUserResponseTypeDef,
    VpcConnectionPropertiesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("QuickSightClient",)


class QuickSightClient(BaseClient):
    """
    [QuickSight.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_ingestion(
        self, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> CancelIngestionResponseTypeDef:
        """
        [Client.cancel_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.cancel_ingestion)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dashboard(
        self,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: DashboardSourceEntityTypeDef,
        Parameters: ParametersTypeDef = None,
        Permissions: List[ResourcePermissionTypeDef] = None,
        Tags: List[TagTypeDef] = None,
        VersionDescription: str = None,
        DashboardPublishOptions: DashboardPublishOptionsTypeDef = None,
    ) -> CreateDashboardResponseTypeDef:
        """
        [Client.create_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.create_dashboard)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_data_set(
        self,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: Dict[str, PhysicalTableTypeDef],
        ImportMode: Literal["SPICE", "DIRECT_QUERY"],
        LogicalTableMap: Dict[str, LogicalTableTypeDef] = None,
        ColumnGroups: List[ColumnGroupTypeDef] = None,
        Permissions: List[ResourcePermissionTypeDef] = None,
        RowLevelPermissionDataSet: RowLevelPermissionDataSetTypeDef = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDataSetResponseTypeDef:
        """
        [Client.create_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.create_data_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_data_source(
        self,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        Type: Literal[
            "ADOBE_ANALYTICS",
            "AMAZON_ELASTICSEARCH",
            "ATHENA",
            "AURORA",
            "AURORA_POSTGRESQL",
            "AWS_IOT_ANALYTICS",
            "GITHUB",
            "JIRA",
            "MARIADB",
            "MYSQL",
            "POSTGRESQL",
            "PRESTO",
            "REDSHIFT",
            "S3",
            "SALESFORCE",
            "SERVICENOW",
            "SNOWFLAKE",
            "SPARK",
            "SQLSERVER",
            "TERADATA",
            "TWITTER",
        ],
        DataSourceParameters: DataSourceParametersTypeDef = None,
        Credentials: DataSourceCredentialsTypeDef = None,
        Permissions: List[ResourcePermissionTypeDef] = None,
        VpcConnectionProperties: VpcConnectionPropertiesTypeDef = None,
        SslProperties: SslPropertiesTypeDef = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDataSourceResponseTypeDef:
        """
        [Client.create_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.create_data_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> CreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.create_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group_membership(
        self, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> CreateGroupMembershipResponseTypeDef:
        """
        [Client.create_group_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.create_group_membership)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_iam_policy_assignment(
        self,
        AwsAccountId: str,
        AssignmentName: str,
        AssignmentStatus: Literal["ENABLED", "DRAFT", "DISABLED"],
        Namespace: str,
        PolicyArn: str = None,
        Identities: Dict[str, List[str]] = None,
    ) -> CreateIAMPolicyAssignmentResponseTypeDef:
        """
        [Client.create_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.create_iam_policy_assignment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_ingestion(
        self, DataSetId: str, IngestionId: str, AwsAccountId: str
    ) -> CreateIngestionResponseTypeDef:
        """
        [Client.create_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.create_ingestion)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_template(
        self,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: TemplateSourceEntityTypeDef,
        Name: str = None,
        Permissions: List[ResourcePermissionTypeDef] = None,
        Tags: List[TagTypeDef] = None,
        VersionDescription: str = None,
    ) -> CreateTemplateResponseTypeDef:
        """
        [Client.create_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.create_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> CreateTemplateAliasResponseTypeDef:
        """
        [Client.create_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.create_template_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dashboard(
        self, AwsAccountId: str, DashboardId: str, VersionNumber: int = None
    ) -> DeleteDashboardResponseTypeDef:
        """
        [Client.delete_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.delete_dashboard)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_data_set(self, AwsAccountId: str, DataSetId: str) -> DeleteDataSetResponseTypeDef:
        """
        [Client.delete_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.delete_data_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_data_source(
        self, AwsAccountId: str, DataSourceId: str
    ) -> DeleteDataSourceResponseTypeDef:
        """
        [Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.delete_data_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteGroupResponseTypeDef:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.delete_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_group_membership(
        self, MemberName: str, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteGroupMembershipResponseTypeDef:
        """
        [Client.delete_group_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.delete_group_membership)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_iam_policy_assignment(
        self, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> DeleteIAMPolicyAssignmentResponseTypeDef:
        """
        [Client.delete_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.delete_iam_policy_assignment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_template(
        self, AwsAccountId: str, TemplateId: str, VersionNumber: int = None
    ) -> DeleteTemplateResponseTypeDef:
        """
        [Client.delete_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.delete_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> DeleteTemplateAliasResponseTypeDef:
        """
        [Client.delete_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.delete_template_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user(
        self, UserName: str, AwsAccountId: str, Namespace: str
    ) -> DeleteUserResponseTypeDef:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.delete_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user_by_principal_id(
        self, PrincipalId: str, AwsAccountId: str, Namespace: str
    ) -> DeleteUserByPrincipalIdResponseTypeDef:
        """
        [Client.delete_user_by_principal_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.delete_user_by_principal_id)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dashboard(
        self, AwsAccountId: str, DashboardId: str, VersionNumber: int = None, AliasName: str = None
    ) -> DescribeDashboardResponseTypeDef:
        """
        [Client.describe_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_dashboard)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dashboard_permissions(
        self, AwsAccountId: str, DashboardId: str
    ) -> DescribeDashboardPermissionsResponseTypeDef:
        """
        [Client.describe_dashboard_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_data_set(
        self, AwsAccountId: str, DataSetId: str
    ) -> DescribeDataSetResponseTypeDef:
        """
        [Client.describe_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_data_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_data_set_permissions(
        self, AwsAccountId: str, DataSetId: str
    ) -> DescribeDataSetPermissionsResponseTypeDef:
        """
        [Client.describe_data_set_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_data_set_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_data_source(
        self, AwsAccountId: str, DataSourceId: str
    ) -> DescribeDataSourceResponseTypeDef:
        """
        [Client.describe_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_data_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_data_source_permissions(
        self, AwsAccountId: str, DataSourceId: str
    ) -> DescribeDataSourcePermissionsResponseTypeDef:
        """
        [Client.describe_data_source_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_data_source_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str
    ) -> DescribeGroupResponseTypeDef:
        """
        [Client.describe_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_iam_policy_assignment(
        self, AwsAccountId: str, AssignmentName: str, Namespace: str
    ) -> DescribeIAMPolicyAssignmentResponseTypeDef:
        """
        [Client.describe_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_iam_policy_assignment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_ingestion(
        self, AwsAccountId: str, DataSetId: str, IngestionId: str
    ) -> DescribeIngestionResponseTypeDef:
        """
        [Client.describe_ingestion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_ingestion)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_template(
        self, AwsAccountId: str, TemplateId: str, VersionNumber: int = None, AliasName: str = None
    ) -> DescribeTemplateResponseTypeDef:
        """
        [Client.describe_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str
    ) -> DescribeTemplateAliasResponseTypeDef:
        """
        [Client.describe_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_template_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_template_permissions(
        self, AwsAccountId: str, TemplateId: str
    ) -> DescribeTemplatePermissionsResponseTypeDef:
        """
        [Client.describe_template_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_template_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user(
        self, UserName: str, AwsAccountId: str, Namespace: str
    ) -> DescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.describe_user)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dashboard_embed_url(
        self,
        AwsAccountId: str,
        DashboardId: str,
        IdentityType: Literal["IAM", "QUICKSIGHT"],
        SessionLifetimeInMinutes: int = None,
        UndoRedoDisabled: bool = None,
        ResetDisabled: bool = None,
        UserArn: str = None,
    ) -> GetDashboardEmbedUrlResponseTypeDef:
        """
        [Client.get_dashboard_embed_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.get_dashboard_embed_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dashboard_versions(
        self, AwsAccountId: str, DashboardId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDashboardVersionsResponseTypeDef:
        """
        [Client.list_dashboard_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_dashboard_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dashboards(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDashboardsResponseTypeDef:
        """
        [Client.list_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_dashboards)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_data_sets(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSetsResponseTypeDef:
        """
        [Client.list_data_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_data_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_data_sources(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        [Client.list_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_data_sources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_group_memberships(
        self,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListGroupMembershipsResponseTypeDef:
        """
        [Client.list_group_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_group_memberships)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_groups(
        self, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_iam_policy_assignments(
        self,
        AwsAccountId: str,
        Namespace: str,
        AssignmentStatus: Literal["ENABLED", "DRAFT", "DISABLED"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListIAMPolicyAssignmentsResponseTypeDef:
        """
        [Client.list_iam_policy_assignments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_iam_policy_assignments_for_user(
        self,
        AwsAccountId: str,
        UserName: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListIAMPolicyAssignmentsForUserResponseTypeDef:
        """
        [Client.list_iam_policy_assignments_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments_for_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_ingestions(
        self, DataSetId: str, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListIngestionsResponseTypeDef:
        """
        [Client.list_ingestions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_ingestions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_template_aliases(
        self, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplateAliasesResponseTypeDef:
        """
        [Client.list_template_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_template_aliases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_template_versions(
        self, AwsAccountId: str, TemplateId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplateVersionsResponseTypeDef:
        """
        [Client.list_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_template_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_templates(
        self, AwsAccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTemplatesResponseTypeDef:
        """
        [Client.list_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_templates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_user_groups(
        self,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListUserGroupsResponseTypeDef:
        """
        [Client.list_user_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_user_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_users(
        self, AwsAccountId: str, Namespace: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.list_users)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_user(
        self,
        IdentityType: Literal["IAM", "QUICKSIGHT"],
        Email: str,
        UserRole: Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
        AwsAccountId: str,
        Namespace: str,
        IamArn: str = None,
        SessionName: str = None,
        UserName: str = None,
    ) -> RegisterUserResponseTypeDef:
        """
        [Client.register_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.register_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: List[TagTypeDef]) -> TagResourceResponseTypeDef:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> UntagResourceResponseTypeDef:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_dashboard(
        self,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: DashboardSourceEntityTypeDef,
        Parameters: ParametersTypeDef = None,
        VersionDescription: str = None,
        DashboardPublishOptions: DashboardPublishOptionsTypeDef = None,
    ) -> UpdateDashboardResponseTypeDef:
        """
        [Client.update_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_dashboard)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_dashboard_permissions(
        self,
        AwsAccountId: str,
        DashboardId: str,
        GrantPermissions: List[ResourcePermissionTypeDef] = None,
        RevokePermissions: List[ResourcePermissionTypeDef] = None,
    ) -> UpdateDashboardPermissionsResponseTypeDef:
        """
        [Client.update_dashboard_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_dashboard_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_dashboard_published_version(
        self, AwsAccountId: str, DashboardId: str, VersionNumber: int
    ) -> UpdateDashboardPublishedVersionResponseTypeDef:
        """
        [Client.update_dashboard_published_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_dashboard_published_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_data_set(
        self,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: Dict[str, PhysicalTableTypeDef],
        ImportMode: Literal["SPICE", "DIRECT_QUERY"],
        LogicalTableMap: Dict[str, LogicalTableTypeDef] = None,
        ColumnGroups: List[ColumnGroupTypeDef] = None,
        RowLevelPermissionDataSet: RowLevelPermissionDataSetTypeDef = None,
    ) -> UpdateDataSetResponseTypeDef:
        """
        [Client.update_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_data_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_data_set_permissions(
        self,
        AwsAccountId: str,
        DataSetId: str,
        GrantPermissions: List[ResourcePermissionTypeDef] = None,
        RevokePermissions: List[ResourcePermissionTypeDef] = None,
    ) -> UpdateDataSetPermissionsResponseTypeDef:
        """
        [Client.update_data_set_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_data_set_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_data_source(
        self,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        DataSourceParameters: DataSourceParametersTypeDef = None,
        Credentials: DataSourceCredentialsTypeDef = None,
        VpcConnectionProperties: VpcConnectionPropertiesTypeDef = None,
        SslProperties: SslPropertiesTypeDef = None,
    ) -> UpdateDataSourceResponseTypeDef:
        """
        [Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_data_source)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_data_source_permissions(
        self,
        AwsAccountId: str,
        DataSourceId: str,
        GrantPermissions: List[ResourcePermissionTypeDef] = None,
        RevokePermissions: List[ResourcePermissionTypeDef] = None,
    ) -> UpdateDataSourcePermissionsResponseTypeDef:
        """
        [Client.update_data_source_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_data_source_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_group(
        self, GroupName: str, AwsAccountId: str, Namespace: str, Description: str = None
    ) -> UpdateGroupResponseTypeDef:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_iam_policy_assignment(
        self,
        AwsAccountId: str,
        AssignmentName: str,
        Namespace: str,
        AssignmentStatus: Literal["ENABLED", "DRAFT", "DISABLED"] = None,
        PolicyArn: str = None,
        Identities: Dict[str, List[str]] = None,
    ) -> UpdateIAMPolicyAssignmentResponseTypeDef:
        """
        [Client.update_iam_policy_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_iam_policy_assignment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_template(
        self,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: TemplateSourceEntityTypeDef,
        VersionDescription: str = None,
        Name: str = None,
    ) -> UpdateTemplateResponseTypeDef:
        """
        [Client.update_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_template_alias(
        self, AwsAccountId: str, TemplateId: str, AliasName: str, TemplateVersionNumber: int
    ) -> UpdateTemplateAliasResponseTypeDef:
        """
        [Client.update_template_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_template_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_template_permissions(
        self,
        AwsAccountId: str,
        TemplateId: str,
        GrantPermissions: List[ResourcePermissionTypeDef] = None,
        RevokePermissions: List[ResourcePermissionTypeDef] = None,
    ) -> UpdateTemplatePermissionsResponseTypeDef:
        """
        [Client.update_template_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_template_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user(
        self,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        Email: str,
        Role: Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"],
    ) -> UpdateUserResponseTypeDef:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/quicksight.html#QuickSight.Client.update_user)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentUpdatingException: Boto3ClientError
    ConflictException: Boto3ClientError
    DomainNotWhitelistedException: Boto3ClientError
    IdentityTypeNotSupportedException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    PreconditionNotMetException: Boto3ClientError
    QuickSightUserNotFoundException: Boto3ClientError
    ResourceExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceUnavailableException: Boto3ClientError
    SessionLifetimeInMinutesInvalidException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    UnsupportedUserEditionException: Boto3ClientError
