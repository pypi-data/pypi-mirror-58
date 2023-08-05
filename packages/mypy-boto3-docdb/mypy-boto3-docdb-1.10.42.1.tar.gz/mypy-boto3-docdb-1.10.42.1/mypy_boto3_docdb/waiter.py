"Main interface for docdb service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_docdb.type_defs import FilterTypeDef, WaiterConfigTypeDef


__all__ = ("DBInstanceAvailableWaiter", "DBInstanceDeletedWaiter")


class DBInstanceAvailableWaiter(Boto3Waiter):
    """
    [Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/docdb.html#DocDB.Waiter.DBInstanceAvailable)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DBInstanceAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/docdb.html#DocDB.Waiter.DBInstanceAvailable.wait)
        """


class DBInstanceDeletedWaiter(Boto3Waiter):
    """
    [Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/docdb.html#DocDB.Waiter.DBInstanceDeleted)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DBInstanceDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/docdb.html#DocDB.Waiter.DBInstanceDeleted.wait)
        """
