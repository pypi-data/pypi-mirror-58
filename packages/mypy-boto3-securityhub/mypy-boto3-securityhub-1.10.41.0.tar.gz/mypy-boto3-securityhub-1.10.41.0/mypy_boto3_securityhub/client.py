"Main interface for securityhub service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_securityhub.client as client_scope

# pylint: disable=import-self
import mypy_boto3_securityhub.paginator as paginator_scope
from mypy_boto3_securityhub.type_defs import (
    AccountDetailsTypeDef,
    AwsSecurityFindingFiltersTypeDef,
    AwsSecurityFindingTypeDef,
    BatchDisableStandardsResponseTypeDef,
    BatchEnableStandardsResponseTypeDef,
    BatchImportFindingsResponseTypeDef,
    CreateActionTargetResponseTypeDef,
    CreateInsightResponseTypeDef,
    CreateMembersResponseTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteActionTargetResponseTypeDef,
    DeleteInsightResponseTypeDef,
    DeleteInvitationsResponseTypeDef,
    DeleteMembersResponseTypeDef,
    DescribeActionTargetsResponseTypeDef,
    DescribeHubResponseTypeDef,
    DescribeProductsResponseTypeDef,
    EnableImportFindingsForProductResponseTypeDef,
    GetEnabledStandardsResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetInsightResultsResponseTypeDef,
    GetInsightsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMembersResponseTypeDef,
    InviteMembersResponseTypeDef,
    ListEnabledProductsForImportResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NoteUpdateTypeDef,
    SortCriterionTypeDef,
    StandardsSubscriptionRequestTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SecurityHubClient",)


class SecurityHubClient(BaseClient):
    """
    [SecurityHub.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_invitation(self, MasterId: str, InvitationId: str) -> Dict[str, Any]:
        """
        [Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.accept_invitation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_disable_standards(
        self, StandardsSubscriptionArns: List[str]
    ) -> BatchDisableStandardsResponseTypeDef:
        """
        [Client.batch_disable_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.batch_disable_standards)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_enable_standards(
        self, StandardsSubscriptionRequests: List[StandardsSubscriptionRequestTypeDef]
    ) -> BatchEnableStandardsResponseTypeDef:
        """
        [Client.batch_enable_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.batch_enable_standards)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_import_findings(
        self, Findings: List[AwsSecurityFindingTypeDef]
    ) -> BatchImportFindingsResponseTypeDef:
        """
        [Client.batch_import_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.batch_import_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_action_target(
        self, Name: str, Description: str, Id: str
    ) -> CreateActionTargetResponseTypeDef:
        """
        [Client.create_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.create_action_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_insight(
        self, Name: str, Filters: AwsSecurityFindingFiltersTypeDef, GroupByAttribute: str
    ) -> CreateInsightResponseTypeDef:
        """
        [Client.create_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.create_insight)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_members(
        self, AccountDetails: List[AccountDetailsTypeDef] = None
    ) -> CreateMembersResponseTypeDef:
        """
        [Client.create_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.create_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def decline_invitations(self, AccountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        [Client.decline_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.decline_invitations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_action_target(self, ActionTargetArn: str) -> DeleteActionTargetResponseTypeDef:
        """
        [Client.delete_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.delete_action_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_insight(self, InsightArn: str) -> DeleteInsightResponseTypeDef:
        """
        [Client.delete_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.delete_insight)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_invitations(self, AccountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        [Client.delete_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.delete_invitations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_members(self, AccountIds: List[str] = None) -> DeleteMembersResponseTypeDef:
        """
        [Client.delete_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.delete_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_action_targets(
        self, ActionTargetArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeActionTargetsResponseTypeDef:
        """
        [Client.describe_action_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.describe_action_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_hub(self, HubArn: str = None) -> DescribeHubResponseTypeDef:
        """
        [Client.describe_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.describe_hub)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_products(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeProductsResponseTypeDef:
        """
        [Client.describe_products documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.describe_products)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_import_findings_for_product(self, ProductSubscriptionArn: str) -> Dict[str, Any]:
        """
        [Client.disable_import_findings_for_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.disable_import_findings_for_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_security_hub(self) -> Dict[str, Any]:
        """
        [Client.disable_security_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.disable_security_hub)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_from_master_account(self) -> Dict[str, Any]:
        """
        [Client.disassociate_from_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.disassociate_from_master_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_members(self, AccountIds: List[str] = None) -> Dict[str, Any]:
        """
        [Client.disassociate_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.disassociate_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_import_findings_for_product(
        self, ProductArn: str
    ) -> EnableImportFindingsForProductResponseTypeDef:
        """
        [Client.enable_import_findings_for_product documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.enable_import_findings_for_product)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_security_hub(self, Tags: Dict[str, str] = None) -> Dict[str, Any]:
        """
        [Client.enable_security_hub documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.enable_security_hub)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_enabled_standards(
        self,
        StandardsSubscriptionArns: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetEnabledStandardsResponseTypeDef:
        """
        [Client.get_enabled_standards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.get_enabled_standards)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_findings(
        self,
        Filters: AwsSecurityFindingFiltersTypeDef = None,
        SortCriteria: List[SortCriterionTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetFindingsResponseTypeDef:
        """
        [Client.get_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.get_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_insight_results(self, InsightArn: str) -> GetInsightResultsResponseTypeDef:
        """
        [Client.get_insight_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.get_insight_results)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_insights(
        self, InsightArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> GetInsightsResponseTypeDef:
        """
        [Client.get_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.get_insights)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        [Client.get_invitations_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.get_invitations_count)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_master_account(self) -> GetMasterAccountResponseTypeDef:
        """
        [Client.get_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.get_master_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_members(self, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        [Client.get_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.get_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invite_members(self, AccountIds: List[str] = None) -> InviteMembersResponseTypeDef:
        """
        [Client.invite_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.invite_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_enabled_products_for_import(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListEnabledProductsForImportResponseTypeDef:
        """
        [Client.list_enabled_products_for_import documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.list_enabled_products_for_import)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.list_invitations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_members(
        self, OnlyAssociated: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> ListMembersResponseTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.list_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_action_target(
        self, ActionTargetArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_action_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.update_action_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_findings(
        self,
        Filters: AwsSecurityFindingFiltersTypeDef,
        Note: NoteUpdateTypeDef = None,
        RecordState: Literal["ACTIVE", "ARCHIVED"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.update_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_insight(
        self,
        InsightArn: str,
        Name: str = None,
        Filters: AwsSecurityFindingFiltersTypeDef = None,
        GroupByAttribute: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Client.update_insight)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_enabled_standards"]
    ) -> paginator_scope.GetEnabledStandardsPaginator:
        """
        [Paginator.GetEnabledStandards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_findings"]
    ) -> paginator_scope.GetFindingsPaginator:
        """
        [Paginator.GetFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_insights"]
    ) -> paginator_scope.GetInsightsPaginator:
        """
        [Paginator.GetInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_enabled_products_for_import"]
    ) -> paginator_scope.ListEnabledProductsForImportPaginator:
        """
        [Paginator.ListEnabledProductsForImport documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> paginator_scope.ListInvitationsPaginator:
        """
        [Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_members"]
    ) -> paginator_scope.ListMembersPaginator:
        """
        [Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidAccessException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
