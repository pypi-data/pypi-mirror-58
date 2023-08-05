"Main interface for kms service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_kms.type_defs import (
    ListAliasesResponseTypeDef,
    ListGrantsResponseTypeDef,
    ListKeyPoliciesResponseTypeDef,
    ListKeysResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListAliasesPaginator",
    "ListGrantsPaginator",
    "ListKeyPoliciesPaginator",
    "ListKeysPaginator",
)


class ListAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kms.html#KMS.Paginator.ListAliases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, KeyId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAliasesResponseTypeDef, None, None]:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kms.html#KMS.Paginator.ListAliases.paginate)
        """


class ListGrantsPaginator(Boto3Paginator):
    """
    [Paginator.ListGrants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kms.html#KMS.Paginator.ListGrants)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, KeyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListGrantsResponseTypeDef, None, None]:
        """
        [ListGrants.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kms.html#KMS.Paginator.ListGrants.paginate)
        """


class ListKeyPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListKeyPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kms.html#KMS.Paginator.ListKeyPolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, KeyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListKeyPoliciesResponseTypeDef, None, None]:
        """
        [ListKeyPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kms.html#KMS.Paginator.ListKeyPolicies.paginate)
        """


class ListKeysPaginator(Boto3Paginator):
    """
    [Paginator.ListKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kms.html#KMS.Paginator.ListKeys)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListKeysResponseTypeDef, None, None]:
        """
        [ListKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/kms.html#KMS.Paginator.ListKeys.paginate)
        """
