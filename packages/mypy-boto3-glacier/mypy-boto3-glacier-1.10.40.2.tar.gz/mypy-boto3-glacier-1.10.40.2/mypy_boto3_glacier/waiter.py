"Main interface for glacier service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_glacier.type_defs import WaiterConfigTypeDef


__all__ = ("VaultExistsWaiter", "VaultNotExistsWaiter")


class VaultExistsWaiter(Boto3Waiter):
    """
    [Waiter.VaultExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Waiter.VaultExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, accountId: str, vaultName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [VaultExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Waiter.VaultExists.wait)
        """


class VaultNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.VaultNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Waiter.VaultNotExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, accountId: str, vaultName: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [VaultNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/glacier.html#Glacier.Waiter.VaultNotExists.wait)
        """
