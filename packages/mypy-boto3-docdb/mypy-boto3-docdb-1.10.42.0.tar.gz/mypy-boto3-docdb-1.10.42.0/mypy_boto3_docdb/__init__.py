"Main interface for docdb service"
from mypy_boto3_docdb.client import DocDBClient as Client, DocDBClient
from mypy_boto3_docdb.paginator import (
    DescribeDBClustersPaginator,
    DescribeDBEngineVersionsPaginator,
    DescribeDBInstancesPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEventsPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
)
from mypy_boto3_docdb.waiter import DBInstanceAvailableWaiter, DBInstanceDeletedWaiter


__all__ = (
    "Client",
    "DBInstanceAvailableWaiter",
    "DBInstanceDeletedWaiter",
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
    "DocDBClient",
)
