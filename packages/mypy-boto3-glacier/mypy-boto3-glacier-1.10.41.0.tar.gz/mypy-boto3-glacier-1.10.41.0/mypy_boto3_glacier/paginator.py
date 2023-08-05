"Main interface for glacier service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_glacier.type_defs import (
    ListJobsOutputTypeDef,
    ListMultipartUploadsOutputTypeDef,
    ListPartsOutputTypeDef,
    ListVaultsOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListJobsPaginator",
    "ListMultipartUploadsPaginator",
    "ListPartsPaginator",
    "ListVaultsPaginator",
)


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/glacier.html#Glacier.Paginator.ListJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        accountId: str,
        vaultName: str,
        statuscode: str = None,
        completed: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListJobsOutputTypeDef, None, None]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/glacier.html#Glacier.Paginator.ListJobs.paginate)
        """


class ListMultipartUploadsPaginator(Boto3Paginator):
    """
    [Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, accountId: str, vaultName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMultipartUploadsOutputTypeDef, None, None]:
        """
        [ListMultipartUploads.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads.paginate)
        """


class ListPartsPaginator(Boto3Paginator):
    """
    [Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/glacier.html#Glacier.Paginator.ListParts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        accountId: str,
        vaultName: str,
        uploadId: str,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListPartsOutputTypeDef, None, None]:
        """
        [ListParts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/glacier.html#Glacier.Paginator.ListParts.paginate)
        """


class ListVaultsPaginator(Boto3Paginator):
    """
    [Paginator.ListVaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/glacier.html#Glacier.Paginator.ListVaults)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, accountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListVaultsOutputTypeDef, None, None]:
        """
        [ListVaults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/glacier.html#Glacier.Paginator.ListVaults.paginate)
        """
