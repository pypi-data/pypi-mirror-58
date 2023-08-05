"Main interface for support service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_support.type_defs import (
    DescribeCasesResponseTypeDef,
    DescribeCommunicationsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("DescribeCasesPaginator", "DescribeCommunicationsPaginator")


class DescribeCasesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Paginator.DescribeCases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        caseIdList: List[str] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        language: str = None,
        includeCommunications: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeCasesResponseTypeDef, None, None]:
        """
        [DescribeCases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Paginator.DescribeCases.paginate)
        """


class DescribeCommunicationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCommunications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Paginator.DescribeCommunications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeCommunicationsResponseTypeDef, None, None]:
        """
        [DescribeCommunications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Paginator.DescribeCommunications.paginate)
        """
