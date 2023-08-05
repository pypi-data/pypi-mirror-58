"Main interface for acm-pca service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, IO, List, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_acm_pca.client as client_scope

# pylint: disable=import-self
import mypy_boto3_acm_pca.paginator as paginator_scope
from mypy_boto3_acm_pca.type_defs import (
    CertificateAuthorityConfigurationTypeDef,
    CreateCertificateAuthorityAuditReportResponseTypeDef,
    CreateCertificateAuthorityResponseTypeDef,
    DescribeCertificateAuthorityAuditReportResponseTypeDef,
    DescribeCertificateAuthorityResponseTypeDef,
    GetCertificateAuthorityCertificateResponseTypeDef,
    GetCertificateAuthorityCsrResponseTypeDef,
    GetCertificateResponseTypeDef,
    IssueCertificateResponseTypeDef,
    ListCertificateAuthoritiesResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListTagsResponseTypeDef,
    RevocationConfigurationTypeDef,
    TagTypeDef,
    ValidityTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_acm_pca.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ACMPCAClient",)


class ACMPCAClient(BaseClient):
    """
    [ACMPCA.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_certificate_authority(
        self,
        CertificateAuthorityConfiguration: CertificateAuthorityConfigurationTypeDef,
        CertificateAuthorityType: Literal["ROOT", "SUBORDINATE"],
        RevocationConfiguration: RevocationConfigurationTypeDef = None,
        IdempotencyToken: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateCertificateAuthorityResponseTypeDef:
        """
        [Client.create_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.create_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_certificate_authority_audit_report(
        self,
        CertificateAuthorityArn: str,
        S3BucketName: str,
        AuditReportResponseFormat: Literal["JSON", "CSV"],
    ) -> CreateCertificateAuthorityAuditReportResponseTypeDef:
        """
        [Client.create_certificate_authority_audit_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.create_certificate_authority_audit_report)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_permission(
        self,
        CertificateAuthorityArn: str,
        Principal: str,
        Actions: List[Literal["IssueCertificate", "GetCertificate", "ListPermissions"]],
        SourceAccount: str = None,
    ) -> None:
        """
        [Client.create_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.create_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_certificate_authority(
        self, CertificateAuthorityArn: str, PermanentDeletionTimeInDays: int = None
    ) -> None:
        """
        [Client.delete_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.delete_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_permission(
        self, CertificateAuthorityArn: str, Principal: str, SourceAccount: str = None
    ) -> None:
        """
        [Client.delete_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.delete_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_certificate_authority(
        self, CertificateAuthorityArn: str
    ) -> DescribeCertificateAuthorityResponseTypeDef:
        """
        [Client.describe_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.describe_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_certificate_authority_audit_report(
        self, CertificateAuthorityArn: str, AuditReportId: str
    ) -> DescribeCertificateAuthorityAuditReportResponseTypeDef:
        """
        [Client.describe_certificate_authority_audit_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.describe_certificate_authority_audit_report)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_certificate(
        self, CertificateAuthorityArn: str, CertificateArn: str
    ) -> GetCertificateResponseTypeDef:
        """
        [Client.get_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.get_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_certificate_authority_certificate(
        self, CertificateAuthorityArn: str
    ) -> GetCertificateAuthorityCertificateResponseTypeDef:
        """
        [Client.get_certificate_authority_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.get_certificate_authority_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_certificate_authority_csr(
        self, CertificateAuthorityArn: str
    ) -> GetCertificateAuthorityCsrResponseTypeDef:
        """
        [Client.get_certificate_authority_csr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.get_certificate_authority_csr)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_certificate_authority_certificate(
        self,
        CertificateAuthorityArn: str,
        Certificate: Union[bytes, IO],
        CertificateChain: Union[bytes, IO] = None,
    ) -> None:
        """
        [Client.import_certificate_authority_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.import_certificate_authority_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def issue_certificate(
        self,
        CertificateAuthorityArn: str,
        Csr: Union[bytes, IO],
        SigningAlgorithm: Literal[
            "SHA256WITHECDSA",
            "SHA384WITHECDSA",
            "SHA512WITHECDSA",
            "SHA256WITHRSA",
            "SHA384WITHRSA",
            "SHA512WITHRSA",
        ],
        Validity: ValidityTypeDef,
        TemplateArn: str = None,
        IdempotencyToken: str = None,
    ) -> IssueCertificateResponseTypeDef:
        """
        [Client.issue_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.issue_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_certificate_authorities(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListCertificateAuthoritiesResponseTypeDef:
        """
        [Client.list_certificate_authorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.list_certificate_authorities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_permissions(
        self, CertificateAuthorityArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPermissionsResponseTypeDef:
        """
        [Client.list_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.list_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags(
        self, CertificateAuthorityArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.list_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_certificate_authority(self, CertificateAuthorityArn: str) -> None:
        """
        [Client.restore_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.restore_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_certificate(
        self,
        CertificateAuthorityArn: str,
        CertificateSerial: str,
        RevocationReason: Literal[
            "UNSPECIFIED",
            "KEY_COMPROMISE",
            "CERTIFICATE_AUTHORITY_COMPROMISE",
            "AFFILIATION_CHANGED",
            "SUPERSEDED",
            "CESSATION_OF_OPERATION",
            "PRIVILEGE_WITHDRAWN",
            "A_A_COMPROMISE",
        ],
    ) -> None:
        """
        [Client.revoke_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.revoke_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_certificate_authority(
        self, CertificateAuthorityArn: str, Tags: List[TagTypeDef]
    ) -> None:
        """
        [Client.tag_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.tag_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_certificate_authority(
        self, CertificateAuthorityArn: str, Tags: List[TagTypeDef]
    ) -> None:
        """
        [Client.untag_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.untag_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_certificate_authority(
        self,
        CertificateAuthorityArn: str,
        RevocationConfiguration: RevocationConfigurationTypeDef = None,
        Status: Literal[
            "CREATING", "PENDING_CERTIFICATE", "ACTIVE", "DELETED", "DISABLED", "EXPIRED", "FAILED"
        ] = None,
    ) -> None:
        """
        [Client.update_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Client.update_certificate_authority)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_certificate_authorities"]
    ) -> paginator_scope.ListCertificateAuthoritiesPaginator:
        """
        [Paginator.ListCertificateAuthorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_permissions"]
    ) -> paginator_scope.ListPermissionsPaginator:
        """
        [Paginator.ListPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags"]
    ) -> paginator_scope.ListTagsPaginator:
        """
        [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["audit_report_created"]
    ) -> waiter_scope.AuditReportCreatedWaiter:
        """
        [Waiter.AuditReportCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Waiter.AuditReportCreated)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["certificate_authority_csr_created"]
    ) -> waiter_scope.CertificateAuthorityCSRCreatedWaiter:
        """
        [Waiter.CertificateAuthorityCSRCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateAuthorityCSRCreated)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["certificate_issued"]
    ) -> waiter_scope.CertificateIssuedWaiter:
        """
        [Waiter.CertificateIssued documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/acm-pca.html#ACMPCA.Waiter.CertificateIssued)
        """


class Exceptions:
    CertificateMismatchException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InvalidArgsException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidPolicyException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    InvalidStateException: Boto3ClientError
    InvalidTagException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MalformedCSRException: Boto3ClientError
    MalformedCertificateException: Boto3ClientError
    PermissionAlreadyExistsException: Boto3ClientError
    RequestAlreadyProcessedException: Boto3ClientError
    RequestFailedException: Boto3ClientError
    RequestInProgressException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
