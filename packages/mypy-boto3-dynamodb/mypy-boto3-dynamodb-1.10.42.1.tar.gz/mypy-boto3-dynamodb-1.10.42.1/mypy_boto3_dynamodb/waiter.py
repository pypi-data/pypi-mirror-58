"Main interface for dynamodb service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_dynamodb.type_defs import WaiterConfigTypeDef


__all__ = ("TableExistsWaiter", "TableNotExistsWaiter")


class TableExistsWaiter(Boto3Waiter):
    """
    [Waiter.TableExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dynamodb.html#DynamoDB.Waiter.TableExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, TableName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [TableExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dynamodb.html#DynamoDB.Waiter.TableExists.wait)
        """


class TableNotExistsWaiter(Boto3Waiter):
    """
    [Waiter.TableNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dynamodb.html#DynamoDB.Waiter.TableNotExists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(self, TableName: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [TableNotExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/dynamodb.html#DynamoDB.Waiter.TableNotExists.wait)
        """
