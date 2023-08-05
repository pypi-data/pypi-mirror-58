"Main interface for acm-pca service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_acm_pca.type_defs import (
    ListCertificateAuthoritiesResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListCertificateAuthoritiesPaginator", "ListPermissionsPaginator", "ListTagsPaginator")


class ListCertificateAuthoritiesPaginator(Boto3Paginator):
    """
    [Paginator.ListCertificateAuthorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListCertificateAuthoritiesResponseTypeDef, None, None]:
        """
        [ListCertificateAuthorities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities.paginate)
        """


class ListPermissionsPaginator(Boto3Paginator):
    """
    [Paginator.ListPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CertificateAuthorityArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListPermissionsResponseTypeDef, None, None]:
        """
        [ListPermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CertificateAuthorityArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListTagsResponseTypeDef, None, None]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags.paginate)
        """
