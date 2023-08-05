"Main interface for mturk service Paginators"
from __future__ import annotations

import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mturk.type_defs import (
    ListAssignmentsForHITResponseTypeDef,
    ListBonusPaymentsResponseTypeDef,
    ListHITsForQualificationTypeResponseTypeDef,
    ListHITsResponseTypeDef,
    ListQualificationRequestsResponseTypeDef,
    ListQualificationTypesResponseTypeDef,
    ListReviewableHITsResponseTypeDef,
    ListWorkerBlocksResponseTypeDef,
    ListWorkersWithQualificationTypeResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAssignmentsForHITPaginator",
    "ListBonusPaymentsPaginator",
    "ListHITsPaginator",
    "ListHITsForQualificationTypePaginator",
    "ListQualificationRequestsPaginator",
    "ListQualificationTypesPaginator",
    "ListReviewableHITsPaginator",
    "ListWorkerBlocksPaginator",
    "ListWorkersWithQualificationTypePaginator",
)


class ListAssignmentsForHITPaginator(Boto3Paginator):
    """
    [Paginator.ListAssignmentsForHIT documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HITId: str,
        AssignmentStatuses: List[Literal["Submitted", "Approved", "Rejected"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListAssignmentsForHITResponseTypeDef, None, None]:
        """
        [ListAssignmentsForHIT.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT.paginate)
        """


class ListBonusPaymentsPaginator(Boto3Paginator):
    """
    [Paginator.ListBonusPayments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HITId: str = None,
        AssignmentId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListBonusPaymentsResponseTypeDef, None, None]:
        """
        [ListBonusPayments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments.paginate)
        """


class ListHITsPaginator(Boto3Paginator):
    """
    [Paginator.ListHITs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListHITs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListHITsResponseTypeDef, None, None]:
        """
        [ListHITs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListHITs.paginate)
        """


class ListHITsForQualificationTypePaginator(Boto3Paginator):
    """
    [Paginator.ListHITsForQualificationType documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, QualificationTypeId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListHITsForQualificationTypeResponseTypeDef, None, None]:
        """
        [ListHITsForQualificationType.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType.paginate)
        """


class ListQualificationRequestsPaginator(Boto3Paginator):
    """
    [Paginator.ListQualificationRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, QualificationTypeId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListQualificationRequestsResponseTypeDef, None, None]:
        """
        [ListQualificationRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests.paginate)
        """


class ListQualificationTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListQualificationTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        MustBeRequestable: bool,
        Query: str = None,
        MustBeOwnedByCaller: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListQualificationTypesResponseTypeDef, None, None]:
        """
        [ListQualificationTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes.paginate)
        """


class ListReviewableHITsPaginator(Boto3Paginator):
    """
    [Paginator.ListReviewableHITs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HITTypeId: str = None,
        Status: Literal["Reviewable", "Reviewing"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListReviewableHITsResponseTypeDef, None, None]:
        """
        [ListReviewableHITs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs.paginate)
        """


class ListWorkerBlocksPaginator(Boto3Paginator):
    """
    [Paginator.ListWorkerBlocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListWorkerBlocksResponseTypeDef, None, None]:
        """
        [ListWorkerBlocks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks.paginate)
        """


class ListWorkersWithQualificationTypePaginator(Boto3Paginator):
    """
    [Paginator.ListWorkersWithQualificationType documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        QualificationTypeId: str,
        Status: Literal["Granted", "Revoked"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListWorkersWithQualificationTypeResponseTypeDef, None, None]:
        """
        [ListWorkersWithQualificationType.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType.paginate)
        """
