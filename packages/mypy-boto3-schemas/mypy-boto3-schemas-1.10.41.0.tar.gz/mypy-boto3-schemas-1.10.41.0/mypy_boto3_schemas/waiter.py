"Main interface for schemas service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_schemas.type_defs import WaiterConfigTypeDef


__all__ = ("CodeBindingExistsWaiter",)


class CodeBindingExistsWaiter(Boto3Waiter):
    """
    [Waiter.CodeBindingExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/schemas.html#Schemas.Waiter.CodeBindingExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        Language: str,
        RegistryName: str,
        SchemaName: str,
        SchemaVersion: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [CodeBindingExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/schemas.html#Schemas.Waiter.CodeBindingExists.wait)
        """
