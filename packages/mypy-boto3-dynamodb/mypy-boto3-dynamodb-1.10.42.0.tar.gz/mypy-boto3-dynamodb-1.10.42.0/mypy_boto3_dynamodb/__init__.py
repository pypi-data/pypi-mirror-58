"Main interface for dynamodb service"
from mypy_boto3_dynamodb.client import DynamoDBClient as Client, DynamoDBClient
from mypy_boto3_dynamodb.paginator import (
    ListBackupsPaginator,
    ListTablesPaginator,
    ListTagsOfResourcePaginator,
    QueryPaginator,
    ScanPaginator,
)
from mypy_boto3_dynamodb.service_resource import (
    DynamoDBServiceResource as ServiceResource,
    DynamoDBServiceResource,
)
from mypy_boto3_dynamodb.waiter import TableExistsWaiter, TableNotExistsWaiter


__all__ = (
    "Client",
    "DynamoDBClient",
    "DynamoDBServiceResource",
    "ListBackupsPaginator",
    "ListTablesPaginator",
    "ListTagsOfResourcePaginator",
    "QueryPaginator",
    "ScanPaginator",
    "ServiceResource",
    "TableExistsWaiter",
    "TableNotExistsWaiter",
)
