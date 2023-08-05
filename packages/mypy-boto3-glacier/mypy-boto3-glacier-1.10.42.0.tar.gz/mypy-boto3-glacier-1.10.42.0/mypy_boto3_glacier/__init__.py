"Main interface for glacier service"
from mypy_boto3_glacier.client import GlacierClient as Client, GlacierClient
from mypy_boto3_glacier.paginator import (
    ListJobsPaginator,
    ListMultipartUploadsPaginator,
    ListPartsPaginator,
    ListVaultsPaginator,
)
from mypy_boto3_glacier.service_resource import (
    GlacierServiceResource,
    GlacierServiceResource as ServiceResource,
)
from mypy_boto3_glacier.waiter import VaultExistsWaiter, VaultNotExistsWaiter


__all__ = (
    "Client",
    "GlacierClient",
    "GlacierServiceResource",
    "ListJobsPaginator",
    "ListMultipartUploadsPaginator",
    "ListPartsPaginator",
    "ListVaultsPaginator",
    "ServiceResource",
    "VaultExistsWaiter",
    "VaultNotExistsWaiter",
)
