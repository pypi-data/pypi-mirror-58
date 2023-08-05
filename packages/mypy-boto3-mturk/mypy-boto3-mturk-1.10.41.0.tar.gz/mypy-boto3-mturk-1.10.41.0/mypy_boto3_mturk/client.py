"Main interface for mturk service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_mturk.client as client_scope

# pylint: disable=import-self
import mypy_boto3_mturk.paginator as paginator_scope
from mypy_boto3_mturk.type_defs import (
    CreateHITResponseTypeDef,
    CreateHITTypeResponseTypeDef,
    CreateHITWithHITTypeResponseTypeDef,
    CreateQualificationTypeResponseTypeDef,
    GetAccountBalanceResponseTypeDef,
    GetAssignmentResponseTypeDef,
    GetFileUploadURLResponseTypeDef,
    GetHITResponseTypeDef,
    GetQualificationScoreResponseTypeDef,
    GetQualificationTypeResponseTypeDef,
    HITLayoutParameterTypeDef,
    ListAssignmentsForHITResponseTypeDef,
    ListBonusPaymentsResponseTypeDef,
    ListHITsForQualificationTypeResponseTypeDef,
    ListHITsResponseTypeDef,
    ListQualificationRequestsResponseTypeDef,
    ListQualificationTypesResponseTypeDef,
    ListReviewPolicyResultsForHITResponseTypeDef,
    ListReviewableHITsResponseTypeDef,
    ListWorkerBlocksResponseTypeDef,
    ListWorkersWithQualificationTypeResponseTypeDef,
    NotificationSpecificationTypeDef,
    NotifyWorkersResponseTypeDef,
    QualificationRequirementTypeDef,
    ReviewPolicyTypeDef,
    UpdateQualificationTypeResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MTurkClient",)


class MTurkClient(BaseClient):
    """
    [MTurk.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_qualification_request(
        self, QualificationRequestId: str, IntegerValue: int = None
    ) -> Dict[str, Any]:
        """
        [Client.accept_qualification_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.accept_qualification_request)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def approve_assignment(
        self, AssignmentId: str, RequesterFeedback: str = None, OverrideRejection: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.approve_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.approve_assignment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_qualification_with_worker(
        self,
        QualificationTypeId: str,
        WorkerId: str,
        IntegerValue: int = None,
        SendNotification: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.associate_qualification_with_worker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.associate_qualification_with_worker)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_additional_assignments_for_hit(
        self, HITId: str, NumberOfAdditionalAssignments: int, UniqueRequestToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_additional_assignments_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.create_additional_assignments_for_hit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_hit(
        self,
        LifetimeInSeconds: int,
        AssignmentDurationInSeconds: int,
        Reward: str,
        Title: str,
        Description: str,
        MaxAssignments: int = None,
        AutoApprovalDelayInSeconds: int = None,
        Keywords: str = None,
        Question: str = None,
        RequesterAnnotation: str = None,
        QualificationRequirements: List[QualificationRequirementTypeDef] = None,
        UniqueRequestToken: str = None,
        AssignmentReviewPolicy: ReviewPolicyTypeDef = None,
        HITReviewPolicy: ReviewPolicyTypeDef = None,
        HITLayoutId: str = None,
        HITLayoutParameters: List[HITLayoutParameterTypeDef] = None,
    ) -> CreateHITResponseTypeDef:
        """
        [Client.create_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.create_hit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_hit_type(
        self,
        AssignmentDurationInSeconds: int,
        Reward: str,
        Title: str,
        Description: str,
        AutoApprovalDelayInSeconds: int = None,
        Keywords: str = None,
        QualificationRequirements: List[QualificationRequirementTypeDef] = None,
    ) -> CreateHITTypeResponseTypeDef:
        """
        [Client.create_hit_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.create_hit_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_hit_with_hit_type(
        self,
        HITTypeId: str,
        LifetimeInSeconds: int,
        MaxAssignments: int = None,
        Question: str = None,
        RequesterAnnotation: str = None,
        UniqueRequestToken: str = None,
        AssignmentReviewPolicy: ReviewPolicyTypeDef = None,
        HITReviewPolicy: ReviewPolicyTypeDef = None,
        HITLayoutId: str = None,
        HITLayoutParameters: List[HITLayoutParameterTypeDef] = None,
    ) -> CreateHITWithHITTypeResponseTypeDef:
        """
        [Client.create_hit_with_hit_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.create_hit_with_hit_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_qualification_type(
        self,
        Name: str,
        Description: str,
        QualificationTypeStatus: Literal["Active", "Inactive"],
        Keywords: str = None,
        RetryDelayInSeconds: int = None,
        Test: str = None,
        AnswerKey: str = None,
        TestDurationInSeconds: int = None,
        AutoGranted: bool = None,
        AutoGrantedValue: int = None,
    ) -> CreateQualificationTypeResponseTypeDef:
        """
        [Client.create_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.create_qualification_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_worker_block(self, WorkerId: str, Reason: str) -> Dict[str, Any]:
        """
        [Client.create_worker_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.create_worker_block)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_hit(self, HITId: str) -> Dict[str, Any]:
        """
        [Client.delete_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.delete_hit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_qualification_type(self, QualificationTypeId: str) -> Dict[str, Any]:
        """
        [Client.delete_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.delete_qualification_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_worker_block(self, WorkerId: str, Reason: str = None) -> Dict[str, Any]:
        """
        [Client.delete_worker_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.delete_worker_block)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_qualification_from_worker(
        self, WorkerId: str, QualificationTypeId: str, Reason: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_qualification_from_worker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.disassociate_qualification_from_worker)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_account_balance(self) -> GetAccountBalanceResponseTypeDef:
        """
        [Client.get_account_balance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.get_account_balance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_assignment(self, AssignmentId: str) -> GetAssignmentResponseTypeDef:
        """
        [Client.get_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.get_assignment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_file_upload_url(
        self, AssignmentId: str, QuestionIdentifier: str
    ) -> GetFileUploadURLResponseTypeDef:
        """
        [Client.get_file_upload_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.get_file_upload_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_hit(self, HITId: str) -> GetHITResponseTypeDef:
        """
        [Client.get_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.get_hit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_qualification_score(
        self, QualificationTypeId: str, WorkerId: str
    ) -> GetQualificationScoreResponseTypeDef:
        """
        [Client.get_qualification_score documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.get_qualification_score)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_qualification_type(
        self, QualificationTypeId: str
    ) -> GetQualificationTypeResponseTypeDef:
        """
        [Client.get_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.get_qualification_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_assignments_for_hit(
        self,
        HITId: str,
        NextToken: str = None,
        MaxResults: int = None,
        AssignmentStatuses: List[Literal["Submitted", "Approved", "Rejected"]] = None,
    ) -> ListAssignmentsForHITResponseTypeDef:
        """
        [Client.list_assignments_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.list_assignments_for_hit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bonus_payments(
        self,
        HITId: str = None,
        AssignmentId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListBonusPaymentsResponseTypeDef:
        """
        [Client.list_bonus_payments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.list_bonus_payments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_hits(self, NextToken: str = None, MaxResults: int = None) -> ListHITsResponseTypeDef:
        """
        [Client.list_hits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.list_hits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_hits_for_qualification_type(
        self, QualificationTypeId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListHITsForQualificationTypeResponseTypeDef:
        """
        [Client.list_hits_for_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.list_hits_for_qualification_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_qualification_requests(
        self, QualificationTypeId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListQualificationRequestsResponseTypeDef:
        """
        [Client.list_qualification_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.list_qualification_requests)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_qualification_types(
        self,
        MustBeRequestable: bool,
        Query: str = None,
        MustBeOwnedByCaller: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListQualificationTypesResponseTypeDef:
        """
        [Client.list_qualification_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.list_qualification_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_review_policy_results_for_hit(
        self,
        HITId: str,
        PolicyLevels: List[Literal["Assignment", "HIT"]] = None,
        RetrieveActions: bool = None,
        RetrieveResults: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListReviewPolicyResultsForHITResponseTypeDef:
        """
        [Client.list_review_policy_results_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.list_review_policy_results_for_hit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_reviewable_hits(
        self,
        HITTypeId: str = None,
        Status: Literal["Reviewable", "Reviewing"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListReviewableHITsResponseTypeDef:
        """
        [Client.list_reviewable_hits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.list_reviewable_hits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_worker_blocks(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListWorkerBlocksResponseTypeDef:
        """
        [Client.list_worker_blocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.list_worker_blocks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_workers_with_qualification_type(
        self,
        QualificationTypeId: str,
        Status: Literal["Granted", "Revoked"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListWorkersWithQualificationTypeResponseTypeDef:
        """
        [Client.list_workers_with_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.list_workers_with_qualification_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def notify_workers(
        self, Subject: str, MessageText: str, WorkerIds: List[str]
    ) -> NotifyWorkersResponseTypeDef:
        """
        [Client.notify_workers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.notify_workers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_assignment(self, AssignmentId: str, RequesterFeedback: str) -> Dict[str, Any]:
        """
        [Client.reject_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.reject_assignment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_qualification_request(
        self, QualificationRequestId: str, Reason: str = None
    ) -> Dict[str, Any]:
        """
        [Client.reject_qualification_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.reject_qualification_request)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_bonus(
        self,
        WorkerId: str,
        BonusAmount: str,
        AssignmentId: str,
        Reason: str,
        UniqueRequestToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.send_bonus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.send_bonus)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_test_event_notification(
        self,
        Notification: NotificationSpecificationTypeDef,
        TestEventType: Literal[
            "AssignmentAccepted",
            "AssignmentAbandoned",
            "AssignmentReturned",
            "AssignmentSubmitted",
            "AssignmentRejected",
            "AssignmentApproved",
            "HITCreated",
            "HITExpired",
            "HITReviewable",
            "HITExtended",
            "HITDisposed",
            "Ping",
        ],
    ) -> Dict[str, Any]:
        """
        [Client.send_test_event_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.send_test_event_notification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_expiration_for_hit(self, HITId: str, ExpireAt: datetime) -> Dict[str, Any]:
        """
        [Client.update_expiration_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.update_expiration_for_hit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_hit_review_status(self, HITId: str, Revert: bool = None) -> Dict[str, Any]:
        """
        [Client.update_hit_review_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.update_hit_review_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_hit_type_of_hit(self, HITId: str, HITTypeId: str) -> Dict[str, Any]:
        """
        [Client.update_hit_type_of_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.update_hit_type_of_hit)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_notification_settings(
        self,
        HITTypeId: str,
        Notification: NotificationSpecificationTypeDef = None,
        Active: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_notification_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.update_notification_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_qualification_type(
        self,
        QualificationTypeId: str,
        Description: str = None,
        QualificationTypeStatus: Literal["Active", "Inactive"] = None,
        Test: str = None,
        AnswerKey: str = None,
        TestDurationInSeconds: int = None,
        RetryDelayInSeconds: int = None,
        AutoGranted: bool = None,
        AutoGrantedValue: int = None,
    ) -> UpdateQualificationTypeResponseTypeDef:
        """
        [Client.update_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Client.update_qualification_type)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_assignments_for_hit"]
    ) -> paginator_scope.ListAssignmentsForHITPaginator:
        """
        [Paginator.ListAssignmentsForHIT documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_bonus_payments"]
    ) -> paginator_scope.ListBonusPaymentsPaginator:
        """
        [Paginator.ListBonusPayments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_hits"]
    ) -> paginator_scope.ListHITsPaginator:
        """
        [Paginator.ListHITs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListHITs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_hits_for_qualification_type"]
    ) -> paginator_scope.ListHITsForQualificationTypePaginator:
        """
        [Paginator.ListHITsForQualificationType documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_qualification_requests"]
    ) -> paginator_scope.ListQualificationRequestsPaginator:
        """
        [Paginator.ListQualificationRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_qualification_types"]
    ) -> paginator_scope.ListQualificationTypesPaginator:
        """
        [Paginator.ListQualificationTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_reviewable_hits"]
    ) -> paginator_scope.ListReviewableHITsPaginator:
        """
        [Paginator.ListReviewableHITs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_worker_blocks"]
    ) -> paginator_scope.ListWorkerBlocksPaginator:
        """
        [Paginator.ListWorkerBlocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_workers_with_qualification_type"]
    ) -> paginator_scope.ListWorkersWithQualificationTypePaginator:
        """
        [Paginator.ListWorkersWithQualificationType documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType)
        """


class Exceptions:
    ClientError: Boto3ClientError
    RequestError: Boto3ClientError
    ServiceFault: Boto3ClientError
