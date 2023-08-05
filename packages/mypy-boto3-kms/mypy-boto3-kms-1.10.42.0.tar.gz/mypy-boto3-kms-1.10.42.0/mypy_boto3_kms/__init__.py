"Main interface for kms service"
from mypy_boto3_kms.client import KMSClient as Client, KMSClient
from mypy_boto3_kms.paginator import (
    ListAliasesPaginator,
    ListGrantsPaginator,
    ListKeyPoliciesPaginator,
    ListKeysPaginator,
)


__all__ = (
    "Client",
    "KMSClient",
    "ListAliasesPaginator",
    "ListGrantsPaginator",
    "ListKeyPoliciesPaginator",
    "ListKeysPaginator",
)
