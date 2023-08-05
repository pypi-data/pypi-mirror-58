"Main interface for dynamodb service ServiceResource"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from boto3.dynamodb.table import BatchWriter
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_dynamodb.service_resource as service_resource_scope
from mypy_boto3_dynamodb.type_defs import (
    AttributeDefinitionTypeDef,
    AttributeValueTypeDef,
    AttributeValueUpdateTypeDef,
    BatchGetItemOutputTypeDef,
    BatchWriteItemOutputTypeDef,
    ConditionTypeDef,
    CreateTableOutputTypeDef,
    DeleteItemOutputTypeDef,
    DeleteTableOutputTypeDef,
    ExpectedAttributeValueTypeDef,
    GetItemOutputTypeDef,
    GlobalSecondaryIndexTypeDef,
    GlobalSecondaryIndexUpdateTypeDef,
    KeySchemaElementTypeDef,
    KeysAndAttributesTypeDef,
    LocalSecondaryIndexTypeDef,
    ProvisionedThroughputTypeDef,
    PutItemOutputTypeDef,
    QueryOutputTypeDef,
    ReplicationGroupUpdateTypeDef,
    SSESpecificationTypeDef,
    ScanOutputTypeDef,
    StreamSpecificationTypeDef,
    TagTypeDef,
    UpdateItemOutputTypeDef,
    UpdateTableOutputTypeDef,
    WriteRequestTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DynamoDBServiceResource", "Table", "ServiceResourceTablesCollection")


class DynamoDBServiceResource(Boto3ServiceResource):
    """
    [DynamoDB.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.ServiceResource)
    """

    tables: service_resource_scope.ServiceResourceTablesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Table(self, name: str) -> service_resource_scope.Table:
        """
        [ServiceResource.Table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.ServiceResource.Table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_item(
        self,
        RequestItems: Dict[str, KeysAndAttributesTypeDef],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
    ) -> BatchGetItemOutputTypeDef:
        """
        [ServiceResource.batch_get_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.ServiceResource.batch_get_item)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_write_item(
        self,
        RequestItems: Dict[str, List[WriteRequestTypeDef]],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
    ) -> BatchWriteItemOutputTypeDef:
        """
        [ServiceResource.batch_write_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.ServiceResource.batch_write_item)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_table(
        self,
        AttributeDefinitions: List[AttributeDefinitionTypeDef],
        TableName: str,
        KeySchema: List[KeySchemaElementTypeDef],
        LocalSecondaryIndexes: List[LocalSecondaryIndexTypeDef] = None,
        GlobalSecondaryIndexes: List[GlobalSecondaryIndexTypeDef] = None,
        BillingMode: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        ProvisionedThroughput: ProvisionedThroughputTypeDef = None,
        StreamSpecification: StreamSpecificationTypeDef = None,
        SSESpecification: SSESpecificationTypeDef = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateTableOutputTypeDef:
        """
        [ServiceResource.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.ServiceResource.create_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.ServiceResource.get_available_subresources)
        """


class Table(Boto3ServiceResource):
    """
    [Table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.ServiceResource.Table)
    """

    attribute_definitions: List[Any]
    table_name: str
    key_schema: List[Any]
    table_status: str
    creation_date_time: datetime
    provisioned_throughput: Dict[str, Any]
    table_size_bytes: int
    item_count: int
    table_arn: str
    table_id: str
    billing_mode_summary: Dict[str, Any]
    local_secondary_indexes: List[Any]
    global_secondary_indexes: List[Any]
    stream_specification: Dict[str, Any]
    latest_stream_label: str
    latest_stream_arn: str
    global_table_version: str
    replicas: List[Any]
    restore_summary: Dict[str, Any]
    sse_description: Dict[str, Any]
    archival_summary: Dict[str, Any]
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_writer(self, overwrite_by_pkeys: List[str] = None) -> BatchWriter:
        """
        [Table.batch_writer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.batch_writer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> DeleteTableOutputTypeDef:
        """
        [Table.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_item(
        self,
        Key: Dict[str, AttributeValueTypeDef],
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, AttributeValueTypeDef] = None,
    ) -> DeleteItemOutputTypeDef:
        """
        [Table.delete_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.delete_item)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Table.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_item(
        self,
        Key: Dict[str, AttributeValueTypeDef],
        AttributesToGet: List[str] = None,
        ConsistentRead: bool = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ProjectionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
    ) -> GetItemOutputTypeDef:
        """
        [Table.get_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.get_item)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Table.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_item(
        self,
        Item: Dict[str, AttributeValueTypeDef],
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, AttributeValueTypeDef] = None,
    ) -> PutItemOutputTypeDef:
        """
        [Table.put_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.put_item)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def query(
        self,
        IndexName: str = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        ConsistentRead: bool = None,
        KeyConditions: Dict[str, ConditionTypeDef] = None,
        QueryFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ScanIndexForward: bool = None,
        ExclusiveStartKey: Dict[str, AttributeValueTypeDef] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        KeyConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, AttributeValueTypeDef] = None,
    ) -> QueryOutputTypeDef:
        """
        [Table.query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.query)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Table.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def scan(
        self,
        IndexName: str = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        ScanFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ExclusiveStartKey: Dict[str, AttributeValueTypeDef] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        TotalSegments: int = None,
        Segment: int = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, AttributeValueTypeDef] = None,
        ConsistentRead: bool = None,
    ) -> ScanOutputTypeDef:
        """
        [Table.scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.scan)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(
        self,
        AttributeDefinitions: List[AttributeDefinitionTypeDef] = None,
        BillingMode: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        ProvisionedThroughput: ProvisionedThroughputTypeDef = None,
        GlobalSecondaryIndexUpdates: List[GlobalSecondaryIndexUpdateTypeDef] = None,
        StreamSpecification: StreamSpecificationTypeDef = None,
        SSESpecification: SSESpecificationTypeDef = None,
        ReplicaUpdates: List[ReplicationGroupUpdateTypeDef] = None,
    ) -> UpdateTableOutputTypeDef:
        """
        [Table.update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.update)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_item(
        self,
        Key: Dict[str, AttributeValueTypeDef],
        AttributeUpdates: Dict[str, AttributeValueUpdateTypeDef] = None,
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        UpdateExpression: str = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[str, AttributeValueTypeDef] = None,
    ) -> UpdateItemOutputTypeDef:
        """
        [Table.update_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.update_item)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(self) -> None:
        """
        [Table.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.wait_until_exists)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_not_exists(self) -> None:
        """
        [Table.wait_until_not_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.Table.wait_until_not_exists)
        """


class ServiceResourceTablesCollection(ResourceCollection):
    """
    [ServiceResource.tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/dynamodb.html#DynamoDB.ServiceResource.tables)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Table]:
        pass
