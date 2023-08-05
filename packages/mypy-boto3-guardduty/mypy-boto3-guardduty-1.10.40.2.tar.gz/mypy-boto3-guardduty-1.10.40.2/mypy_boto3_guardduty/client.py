"Main interface for guardduty service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_guardduty.client as client_scope

# pylint: disable=import-self
import mypy_boto3_guardduty.paginator as paginator_scope
from mypy_boto3_guardduty.type_defs import (
    AccountDetailTypeDef,
    CreateDetectorResponseTypeDef,
    CreateFilterResponseTypeDef,
    CreateIPSetResponseTypeDef,
    CreateMembersResponseTypeDef,
    CreatePublishingDestinationResponseTypeDef,
    CreateThreatIntelSetResponseTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteInvitationsResponseTypeDef,
    DeleteMembersResponseTypeDef,
    DescribePublishingDestinationResponseTypeDef,
    DestinationPropertiesTypeDef,
    DisassociateMembersResponseTypeDef,
    FindingCriteriaTypeDef,
    GetDetectorResponseTypeDef,
    GetFilterResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetFindingsStatisticsResponseTypeDef,
    GetIPSetResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMembersResponseTypeDef,
    GetThreatIntelSetResponseTypeDef,
    InviteMembersResponseTypeDef,
    ListDetectorsResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListPublishingDestinationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListThreatIntelSetsResponseTypeDef,
    SortCriteriaTypeDef,
    StartMonitoringMembersResponseTypeDef,
    StopMonitoringMembersResponseTypeDef,
    UpdateFilterResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GuardDutyClient",)


class GuardDutyClient(BaseClient):
    """
    [GuardDuty.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_invitation(
        self, DetectorId: str, MasterId: str, InvitationId: str
    ) -> Dict[str, Any]:
        """
        [Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.accept_invitation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def archive_findings(self, DetectorId: str, FindingIds: List[str]) -> Dict[str, Any]:
        """
        [Client.archive_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.archive_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_detector(
        self,
        Enable: bool,
        ClientToken: str = None,
        FindingPublishingFrequency: Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateDetectorResponseTypeDef:
        """
        [Client.create_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.create_detector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_filter(
        self,
        DetectorId: str,
        Name: str,
        FindingCriteria: FindingCriteriaTypeDef,
        Description: str = None,
        Action: Literal["NOOP", "ARCHIVE"] = None,
        Rank: int = None,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateFilterResponseTypeDef:
        """
        [Client.create_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.create_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_ip_set(
        self,
        DetectorId: str,
        Name: str,
        Format: Literal["TXT", "STIX", "OTX_CSV", "ALIEN_VAULT", "PROOF_POINT", "FIRE_EYE"],
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateIPSetResponseTypeDef:
        """
        [Client.create_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.create_ip_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_members(
        self, DetectorId: str, AccountDetails: List[AccountDetailTypeDef]
    ) -> CreateMembersResponseTypeDef:
        """
        [Client.create_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.create_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_publishing_destination(
        self,
        DetectorId: str,
        DestinationType: Literal["S3"],
        DestinationProperties: DestinationPropertiesTypeDef,
        ClientToken: str = None,
    ) -> CreatePublishingDestinationResponseTypeDef:
        """
        [Client.create_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.create_publishing_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_sample_findings(
        self, DetectorId: str, FindingTypes: List[str] = None
    ) -> Dict[str, Any]:
        """
        [Client.create_sample_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.create_sample_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_threat_intel_set(
        self,
        DetectorId: str,
        Name: str,
        Format: Literal["TXT", "STIX", "OTX_CSV", "ALIEN_VAULT", "PROOF_POINT", "FIRE_EYE"],
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateThreatIntelSetResponseTypeDef:
        """
        [Client.create_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.create_threat_intel_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def decline_invitations(self, AccountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        [Client.decline_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.decline_invitations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_detector(self, DetectorId: str) -> Dict[str, Any]:
        """
        [Client.delete_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.delete_detector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_filter(self, DetectorId: str, FilterName: str) -> Dict[str, Any]:
        """
        [Client.delete_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.delete_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_invitations(self, AccountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        [Client.delete_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.delete_invitations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_ip_set(self, DetectorId: str, IpSetId: str) -> Dict[str, Any]:
        """
        [Client.delete_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.delete_ip_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> DeleteMembersResponseTypeDef:
        """
        [Client.delete_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.delete_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_publishing_destination(self, DetectorId: str, DestinationId: str) -> Dict[str, Any]:
        """
        [Client.delete_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.delete_publishing_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_threat_intel_set(self, DetectorId: str, ThreatIntelSetId: str) -> Dict[str, Any]:
        """
        [Client.delete_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.delete_threat_intel_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_publishing_destination(
        self, DetectorId: str, DestinationId: str
    ) -> DescribePublishingDestinationResponseTypeDef:
        """
        [Client.describe_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.describe_publishing_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_from_master_account(self, DetectorId: str) -> Dict[str, Any]:
        """
        [Client.disassociate_from_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.disassociate_from_master_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> DisassociateMembersResponseTypeDef:
        """
        [Client.disassociate_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.disassociate_members)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_detector(self, DetectorId: str) -> GetDetectorResponseTypeDef:
        """
        [Client.get_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.get_detector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_filter(self, DetectorId: str, FilterName: str) -> GetFilterResponseTypeDef:
        """
        [Client.get_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.get_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_findings(
        self, DetectorId: str, FindingIds: List[str], SortCriteria: SortCriteriaTypeDef = None
    ) -> GetFindingsResponseTypeDef:
        """
        [Client.get_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.get_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_findings_statistics(
        self,
        DetectorId: str,
        FindingStatisticTypes: List[Literal["COUNT_BY_SEVERITY"]],
        FindingCriteria: FindingCriteriaTypeDef = None,
    ) -> GetFindingsStatisticsResponseTypeDef:
        """
        [Client.get_findings_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.get_findings_statistics)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        [Client.get_invitations_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.get_invitations_count)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ip_set(self, DetectorId: str, IpSetId: str) -> GetIPSetResponseTypeDef:
        """
        [Client.get_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.get_ip_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_master_account(self, DetectorId: str) -> GetMasterAccountResponseTypeDef:
        """
        [Client.get_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.get_master_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_members(self, DetectorId: str, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        [Client.get_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.get_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_threat_intel_set(
        self, DetectorId: str, ThreatIntelSetId: str
    ) -> GetThreatIntelSetResponseTypeDef:
        """
        [Client.get_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.get_threat_intel_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invite_members(
        self,
        DetectorId: str,
        AccountIds: List[str],
        DisableEmailNotification: bool = None,
        Message: str = None,
    ) -> InviteMembersResponseTypeDef:
        """
        [Client.invite_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.invite_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_detectors(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListDetectorsResponseTypeDef:
        """
        [Client.list_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.list_detectors)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_filters(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListFiltersResponseTypeDef:
        """
        [Client.list_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.list_filters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_findings(
        self,
        DetectorId: str,
        FindingCriteria: FindingCriteriaTypeDef = None,
        SortCriteria: SortCriteriaTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListFindingsResponseTypeDef:
        """
        [Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.list_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.list_invitations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_ip_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListIPSetsResponseTypeDef:
        """
        [Client.list_ip_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.list_ip_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_members(
        self,
        DetectorId: str,
        MaxResults: int = None,
        NextToken: str = None,
        OnlyAssociated: str = None,
    ) -> ListMembersResponseTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.list_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_publishing_destinations(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListPublishingDestinationsResponseTypeDef:
        """
        [Client.list_publishing_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.list_publishing_destinations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_threat_intel_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListThreatIntelSetsResponseTypeDef:
        """
        [Client.list_threat_intel_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.list_threat_intel_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_monitoring_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> StartMonitoringMembersResponseTypeDef:
        """
        [Client.start_monitoring_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.start_monitoring_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_monitoring_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> StopMonitoringMembersResponseTypeDef:
        """
        [Client.stop_monitoring_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.stop_monitoring_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unarchive_findings(self, DetectorId: str, FindingIds: List[str]) -> Dict[str, Any]:
        """
        [Client.unarchive_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.unarchive_findings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_detector(
        self,
        DetectorId: str,
        Enable: bool = None,
        FindingPublishingFrequency: Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.update_detector)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_filter(
        self,
        DetectorId: str,
        FilterName: str,
        Description: str = None,
        Action: Literal["NOOP", "ARCHIVE"] = None,
        Rank: int = None,
        FindingCriteria: FindingCriteriaTypeDef = None,
    ) -> UpdateFilterResponseTypeDef:
        """
        [Client.update_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.update_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_findings_feedback(
        self,
        DetectorId: str,
        FindingIds: List[str],
        Feedback: Literal["USEFUL", "NOT_USEFUL"],
        Comments: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_findings_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.update_findings_feedback)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_ip_set(
        self,
        DetectorId: str,
        IpSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.update_ip_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_publishing_destination(
        self,
        DetectorId: str,
        DestinationId: str,
        DestinationProperties: DestinationPropertiesTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.update_publishing_destination)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_threat_intel_set(
        self,
        DetectorId: str,
        ThreatIntelSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Client.update_threat_intel_set)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_detectors"]
    ) -> paginator_scope.ListDetectorsPaginator:
        """
        [Paginator.ListDetectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Paginator.ListDetectors)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_filters"]
    ) -> paginator_scope.ListFiltersPaginator:
        """
        [Paginator.ListFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Paginator.ListFilters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_findings"]
    ) -> paginator_scope.ListFindingsPaginator:
        """
        [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Paginator.ListFindings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_ip_sets"]
    ) -> paginator_scope.ListIPSetsPaginator:
        """
        [Paginator.ListIPSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Paginator.ListIPSets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> paginator_scope.ListInvitationsPaginator:
        """
        [Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Paginator.ListInvitations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_members"]
    ) -> paginator_scope.ListMembersPaginator:
        """
        [Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Paginator.ListMembers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_threat_intel_sets"]
    ) -> paginator_scope.ListThreatIntelSetsPaginator:
        """
        [Paginator.ListThreatIntelSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/guardduty.html#GuardDuty.Paginator.ListThreatIntelSets)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
