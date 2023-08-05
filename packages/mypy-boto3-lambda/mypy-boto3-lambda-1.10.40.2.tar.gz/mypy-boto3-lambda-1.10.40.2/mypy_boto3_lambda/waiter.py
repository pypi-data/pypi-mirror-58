"Main interface for lambda service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_lambda.type_defs import WaiterConfigTypeDef


__all__ = ("FunctionActiveWaiter", "FunctionExistsWaiter", "FunctionUpdatedWaiter")


class FunctionActiveWaiter(Boto3Waiter):
    """
    [Waiter.FunctionActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Waiter.FunctionActive)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, FunctionName: str, Qualifier: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [FunctionActive.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Waiter.FunctionActive.wait)
        """


class FunctionExistsWaiter(Boto3Waiter):
    """
    [Waiter.FunctionExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Waiter.FunctionExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, FunctionName: str, Qualifier: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [FunctionExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Waiter.FunctionExists.wait)
        """


class FunctionUpdatedWaiter(Boto3Waiter):
    """
    [Waiter.FunctionUpdated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Waiter.FunctionUpdated)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, FunctionName: str, Qualifier: str = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [FunctionUpdated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lambda.html#Lambda.Waiter.FunctionUpdated.wait)
        """
