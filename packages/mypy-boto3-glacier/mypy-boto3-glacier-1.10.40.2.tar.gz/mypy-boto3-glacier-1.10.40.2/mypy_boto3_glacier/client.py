"Main interface for glacier service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, IO, List, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_glacier.client as client_scope

# pylint: disable=import-self
import mypy_boto3_glacier.paginator as paginator_scope
from mypy_boto3_glacier.type_defs import (
    ArchiveCreationOutputTypeDef,
    CreateVaultOutputTypeDef,
    DataRetrievalPolicyTypeDef,
    DescribeVaultOutputTypeDef,
    GetDataRetrievalPolicyOutputTypeDef,
    GetJobOutputOutputTypeDef,
    GetVaultAccessPolicyOutputTypeDef,
    GetVaultLockOutputTypeDef,
    GetVaultNotificationsOutputTypeDef,
    GlacierJobDescriptionTypeDef,
    InitiateJobOutputTypeDef,
    InitiateMultipartUploadOutputTypeDef,
    InitiateVaultLockOutputTypeDef,
    JobParametersTypeDef,
    ListJobsOutputTypeDef,
    ListMultipartUploadsOutputTypeDef,
    ListPartsOutputTypeDef,
    ListProvisionedCapacityOutputTypeDef,
    ListTagsForVaultOutputTypeDef,
    ListVaultsOutputTypeDef,
    PurchaseProvisionedCapacityOutputTypeDef,
    UploadMultipartPartOutputTypeDef,
    VaultAccessPolicyTypeDef,
    VaultLockPolicyTypeDef,
    VaultNotificationConfigTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_glacier.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlacierClient",)


class GlacierClient(BaseClient):
    """
    [Glacier.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def abort_multipart_upload(self, accountId: str, vaultName: str, uploadId: str) -> None:
        """
        [Client.abort_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.abort_multipart_upload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def abort_vault_lock(self, accountId: str, vaultName: str) -> None:
        """
        [Client.abort_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.abort_vault_lock)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_vault(
        self, accountId: str, vaultName: str, Tags: Dict[str, str] = None
    ) -> None:
        """
        [Client.add_tags_to_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.add_tags_to_vault)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def complete_multipart_upload(
        self,
        accountId: str,
        vaultName: str,
        uploadId: str,
        archiveSize: str = None,
        checksum: str = None,
    ) -> ArchiveCreationOutputTypeDef:
        """
        [Client.complete_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.complete_multipart_upload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def complete_vault_lock(self, accountId: str, vaultName: str, lockId: str) -> None:
        """
        [Client.complete_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.complete_vault_lock)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vault(self, accountId: str, vaultName: str) -> CreateVaultOutputTypeDef:
        """
        [Client.create_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.create_vault)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_archive(self, accountId: str, vaultName: str, archiveId: str) -> None:
        """
        [Client.delete_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.delete_archive)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vault(self, accountId: str, vaultName: str) -> None:
        """
        [Client.delete_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.delete_vault)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vault_access_policy(self, accountId: str, vaultName: str) -> None:
        """
        [Client.delete_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.delete_vault_access_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vault_notifications(self, accountId: str, vaultName: str) -> None:
        """
        [Client.delete_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.delete_vault_notifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_job(
        self, accountId: str, vaultName: str, jobId: str
    ) -> GlacierJobDescriptionTypeDef:
        """
        [Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.describe_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vault(self, accountId: str, vaultName: str) -> DescribeVaultOutputTypeDef:
        """
        [Client.describe_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.describe_vault)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_data_retrieval_policy(self, accountId: str) -> GetDataRetrievalPolicyOutputTypeDef:
        """
        [Client.get_data_retrieval_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.get_data_retrieval_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_output(
        self, accountId: str, vaultName: str, jobId: str, range: str = None
    ) -> GetJobOutputOutputTypeDef:
        """
        [Client.get_job_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.get_job_output)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_vault_access_policy(
        self, accountId: str, vaultName: str
    ) -> GetVaultAccessPolicyOutputTypeDef:
        """
        [Client.get_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.get_vault_access_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_vault_lock(self, accountId: str, vaultName: str) -> GetVaultLockOutputTypeDef:
        """
        [Client.get_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.get_vault_lock)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_vault_notifications(
        self, accountId: str, vaultName: str
    ) -> GetVaultNotificationsOutputTypeDef:
        """
        [Client.get_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.get_vault_notifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_job(
        self, accountId: str, vaultName: str, jobParameters: JobParametersTypeDef = None
    ) -> InitiateJobOutputTypeDef:
        """
        [Client.initiate_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.initiate_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_multipart_upload(
        self, accountId: str, vaultName: str, archiveDescription: str = None, partSize: str = None
    ) -> InitiateMultipartUploadOutputTypeDef:
        """
        [Client.initiate_multipart_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.initiate_multipart_upload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_vault_lock(
        self, accountId: str, vaultName: str, policy: VaultLockPolicyTypeDef = None
    ) -> InitiateVaultLockOutputTypeDef:
        """
        [Client.initiate_vault_lock documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.initiate_vault_lock)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(
        self,
        accountId: str,
        vaultName: str,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None,
    ) -> ListJobsOutputTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.list_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_multipart_uploads(
        self, accountId: str, vaultName: str, marker: str = None, limit: str = None
    ) -> ListMultipartUploadsOutputTypeDef:
        """
        [Client.list_multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.list_multipart_uploads)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_parts(
        self, accountId: str, vaultName: str, uploadId: str, marker: str = None, limit: str = None
    ) -> ListPartsOutputTypeDef:
        """
        [Client.list_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.list_parts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_provisioned_capacity(self, accountId: str) -> ListProvisionedCapacityOutputTypeDef:
        """
        [Client.list_provisioned_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.list_provisioned_capacity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_vault(self, accountId: str, vaultName: str) -> ListTagsForVaultOutputTypeDef:
        """
        [Client.list_tags_for_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.list_tags_for_vault)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_vaults(
        self, accountId: str, marker: str = None, limit: str = None
    ) -> ListVaultsOutputTypeDef:
        """
        [Client.list_vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.list_vaults)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purchase_provisioned_capacity(
        self, accountId: str
    ) -> PurchaseProvisionedCapacityOutputTypeDef:
        """
        [Client.purchase_provisioned_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.purchase_provisioned_capacity)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_vault(
        self, accountId: str, vaultName: str, TagKeys: List[str] = None
    ) -> None:
        """
        [Client.remove_tags_from_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.remove_tags_from_vault)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_data_retrieval_policy(
        self, accountId: str, Policy: DataRetrievalPolicyTypeDef = None
    ) -> None:
        """
        [Client.set_data_retrieval_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.set_data_retrieval_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_vault_access_policy(
        self, accountId: str, vaultName: str, policy: VaultAccessPolicyTypeDef = None
    ) -> None:
        """
        [Client.set_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.set_vault_access_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_vault_notifications(
        self,
        accountId: str,
        vaultName: str,
        vaultNotificationConfig: VaultNotificationConfigTypeDef = None,
    ) -> None:
        """
        [Client.set_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.set_vault_notifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_archive(
        self,
        vaultName: str,
        accountId: str,
        archiveDescription: str = None,
        checksum: str = None,
        body: Union[bytes, IO] = None,
    ) -> ArchiveCreationOutputTypeDef:
        """
        [Client.upload_archive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.upload_archive)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_multipart_part(
        self,
        accountId: str,
        vaultName: str,
        uploadId: str,
        checksum: str = None,
        range: str = None,
        body: Union[bytes, IO] = None,
    ) -> UploadMultipartPartOutputTypeDef:
        """
        [Client.upload_multipart_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Client.upload_multipart_part)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> paginator_scope.ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Paginator.ListJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_multipart_uploads"]
    ) -> paginator_scope.ListMultipartUploadsPaginator:
        """
        [Paginator.ListMultipartUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_parts"]
    ) -> paginator_scope.ListPartsPaginator:
        """
        [Paginator.ListParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Paginator.ListParts)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_vaults"]
    ) -> paginator_scope.ListVaultsPaginator:
        """
        [Paginator.ListVaults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Paginator.ListVaults)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: Literal["vault_exists"]) -> waiter_scope.VaultExistsWaiter:
        """
        [Waiter.VaultExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Waiter.VaultExists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["vault_not_exists"]
    ) -> waiter_scope.VaultNotExistsWaiter:
        """
        [Waiter.VaultNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Waiter.VaultNotExists)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InsufficientCapacityException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MissingParameterValueException: Boto3ClientError
    PolicyEnforcedException: Boto3ClientError
    RequestTimeoutException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
