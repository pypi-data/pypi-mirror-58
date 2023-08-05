"Main interface for support service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_support.client as client_scope

# pylint: disable=import-self
import mypy_boto3_support.paginator as paginator_scope
from mypy_boto3_support.type_defs import (
    AddAttachmentsToSetResponseTypeDef,
    AddCommunicationToCaseResponseTypeDef,
    AttachmentTypeDef,
    CreateCaseResponseTypeDef,
    DescribeAttachmentResponseTypeDef,
    DescribeCasesResponseTypeDef,
    DescribeCommunicationsResponseTypeDef,
    DescribeServicesResponseTypeDef,
    DescribeSeverityLevelsResponseTypeDef,
    DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef,
    DescribeTrustedAdvisorCheckResultResponseTypeDef,
    DescribeTrustedAdvisorCheckSummariesResponseTypeDef,
    DescribeTrustedAdvisorChecksResponseTypeDef,
    RefreshTrustedAdvisorCheckResponseTypeDef,
    ResolveCaseResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SupportClient",)


class SupportClient(BaseClient):
    """
    [Support.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_attachments_to_set(
        self, attachments: List[AttachmentTypeDef], attachmentSetId: str = None
    ) -> AddAttachmentsToSetResponseTypeDef:
        """
        [Client.add_attachments_to_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.add_attachments_to_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_communication_to_case(
        self,
        communicationBody: str,
        caseId: str = None,
        ccEmailAddresses: List[str] = None,
        attachmentSetId: str = None,
    ) -> AddCommunicationToCaseResponseTypeDef:
        """
        [Client.add_communication_to_case documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.add_communication_to_case)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_case(
        self,
        subject: str,
        communicationBody: str,
        serviceCode: str = None,
        severityCode: str = None,
        categoryCode: str = None,
        ccEmailAddresses: List[str] = None,
        language: str = None,
        issueType: str = None,
        attachmentSetId: str = None,
    ) -> CreateCaseResponseTypeDef:
        """
        [Client.create_case documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.create_case)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attachment(self, attachmentId: str) -> DescribeAttachmentResponseTypeDef:
        """
        [Client.describe_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.describe_attachment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cases(
        self,
        caseIdList: List[str] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        nextToken: str = None,
        maxResults: int = None,
        language: str = None,
        includeCommunications: bool = None,
    ) -> DescribeCasesResponseTypeDef:
        """
        [Client.describe_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.describe_cases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_communications(
        self,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeCommunicationsResponseTypeDef:
        """
        [Client.describe_communications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.describe_communications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_services(
        self, serviceCodeList: List[str] = None, language: str = None
    ) -> DescribeServicesResponseTypeDef:
        """
        [Client.describe_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.describe_services)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_severity_levels(
        self, language: str = None
    ) -> DescribeSeverityLevelsResponseTypeDef:
        """
        [Client.describe_severity_levels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.describe_severity_levels)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_trusted_advisor_check_refresh_statuses(
        self, checkIds: List[str]
    ) -> DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef:
        """
        [Client.describe_trusted_advisor_check_refresh_statuses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.describe_trusted_advisor_check_refresh_statuses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_trusted_advisor_check_result(
        self, checkId: str, language: str = None
    ) -> DescribeTrustedAdvisorCheckResultResponseTypeDef:
        """
        [Client.describe_trusted_advisor_check_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.describe_trusted_advisor_check_result)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_trusted_advisor_check_summaries(
        self, checkIds: List[str]
    ) -> DescribeTrustedAdvisorCheckSummariesResponseTypeDef:
        """
        [Client.describe_trusted_advisor_check_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.describe_trusted_advisor_check_summaries)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_trusted_advisor_checks(
        self, language: str
    ) -> DescribeTrustedAdvisorChecksResponseTypeDef:
        """
        [Client.describe_trusted_advisor_checks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.describe_trusted_advisor_checks)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def refresh_trusted_advisor_check(
        self, checkId: str
    ) -> RefreshTrustedAdvisorCheckResponseTypeDef:
        """
        [Client.refresh_trusted_advisor_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.refresh_trusted_advisor_check)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resolve_case(self, caseId: str = None) -> ResolveCaseResponseTypeDef:
        """
        [Client.resolve_case documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Client.resolve_case)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_cases"]
    ) -> paginator_scope.DescribeCasesPaginator:
        """
        [Paginator.DescribeCases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Paginator.DescribeCases)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_communications"]
    ) -> paginator_scope.DescribeCommunicationsPaginator:
        """
        [Paginator.DescribeCommunications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/support.html#Support.Paginator.DescribeCommunications)
        """


class Exceptions:
    AttachmentIdNotFound: Boto3ClientError
    AttachmentLimitExceeded: Boto3ClientError
    AttachmentSetExpired: Boto3ClientError
    AttachmentSetIdNotFound: Boto3ClientError
    AttachmentSetSizeLimitExceeded: Boto3ClientError
    CaseCreationLimitExceeded: Boto3ClientError
    CaseIdNotFound: Boto3ClientError
    ClientError: Boto3ClientError
    DescribeAttachmentLimitExceeded: Boto3ClientError
    InternalServerError: Boto3ClientError
