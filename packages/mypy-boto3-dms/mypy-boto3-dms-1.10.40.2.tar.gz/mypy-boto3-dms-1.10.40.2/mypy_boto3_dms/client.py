"Main interface for dms service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, IO, List, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_dms.client as client_scope

# pylint: disable=import-self
import mypy_boto3_dms.paginator as paginator_scope
from mypy_boto3_dms.type_defs import (
    ApplyPendingMaintenanceActionResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreateEventSubscriptionResponseTypeDef,
    CreateReplicationInstanceResponseTypeDef,
    CreateReplicationSubnetGroupResponseTypeDef,
    CreateReplicationTaskResponseTypeDef,
    DeleteCertificateResponseTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteEndpointResponseTypeDef,
    DeleteEventSubscriptionResponseTypeDef,
    DeleteReplicationInstanceResponseTypeDef,
    DeleteReplicationTaskResponseTypeDef,
    DescribeAccountAttributesResponseTypeDef,
    DescribeCertificatesResponseTypeDef,
    DescribeConnectionsResponseTypeDef,
    DescribeEndpointTypesResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeEventCategoriesResponseTypeDef,
    DescribeEventSubscriptionsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeOrderableReplicationInstancesResponseTypeDef,
    DescribePendingMaintenanceActionsResponseTypeDef,
    DescribeRefreshSchemasStatusResponseTypeDef,
    DescribeReplicationInstanceTaskLogsResponseTypeDef,
    DescribeReplicationInstancesResponseTypeDef,
    DescribeReplicationSubnetGroupsResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsResponseTypeDef,
    DescribeReplicationTasksResponseTypeDef,
    DescribeSchemasResponseTypeDef,
    DescribeTableStatisticsResponseTypeDef,
    DmsTransferSettingsTypeDef,
    DynamoDbSettingsTypeDef,
    ElasticsearchSettingsTypeDef,
    FilterTypeDef,
    ImportCertificateResponseTypeDef,
    KinesisSettingsTypeDef,
    ListTagsForResourceResponseTypeDef,
    ModifyEndpointResponseTypeDef,
    ModifyEventSubscriptionResponseTypeDef,
    ModifyReplicationInstanceResponseTypeDef,
    ModifyReplicationSubnetGroupResponseTypeDef,
    ModifyReplicationTaskResponseTypeDef,
    MongoDbSettingsTypeDef,
    RebootReplicationInstanceResponseTypeDef,
    RedshiftSettingsTypeDef,
    RefreshSchemasResponseTypeDef,
    ReloadTablesResponseTypeDef,
    S3SettingsTypeDef,
    StartReplicationTaskAssessmentResponseTypeDef,
    StartReplicationTaskResponseTypeDef,
    StopReplicationTaskResponseTypeDef,
    TableToReloadTypeDef,
    TagTypeDef,
    TestConnectionResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_dms.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DatabaseMigrationServiceClient",)


class DatabaseMigrationServiceClient(BaseClient):
    """
    [DatabaseMigrationService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_resource(self, ResourceArn: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.add_tags_to_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def apply_pending_maintenance_action(
        self, ReplicationInstanceArn: str, ApplyAction: str, OptInType: str
    ) -> ApplyPendingMaintenanceActionResponseTypeDef:
        """
        [Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.apply_pending_maintenance_action)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_endpoint(
        self,
        EndpointIdentifier: str,
        EndpointType: Literal["source", "target"],
        EngineName: str,
        Username: str = None,
        Password: str = None,
        ServerName: str = None,
        Port: int = None,
        DatabaseName: str = None,
        ExtraConnectionAttributes: str = None,
        KmsKeyId: str = None,
        Tags: List[TagTypeDef] = None,
        CertificateArn: str = None,
        SslMode: Literal["none", "require", "verify-ca", "verify-full"] = None,
        ServiceAccessRoleArn: str = None,
        ExternalTableDefinition: str = None,
        DynamoDbSettings: DynamoDbSettingsTypeDef = None,
        S3Settings: S3SettingsTypeDef = None,
        DmsTransferSettings: DmsTransferSettingsTypeDef = None,
        MongoDbSettings: MongoDbSettingsTypeDef = None,
        KinesisSettings: KinesisSettingsTypeDef = None,
        ElasticsearchSettings: ElasticsearchSettingsTypeDef = None,
        RedshiftSettings: RedshiftSettingsTypeDef = None,
    ) -> CreateEndpointResponseTypeDef:
        """
        [Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.create_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        EventCategories: List[str] = None,
        SourceIds: List[str] = None,
        Enabled: bool = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateEventSubscriptionResponseTypeDef:
        """
        [Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.create_event_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_replication_instance(
        self,
        ReplicationInstanceIdentifier: str,
        ReplicationInstanceClass: str,
        AllocatedStorage: int = None,
        VpcSecurityGroupIds: List[str] = None,
        AvailabilityZone: str = None,
        ReplicationSubnetGroupIdentifier: str = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        Tags: List[TagTypeDef] = None,
        KmsKeyId: str = None,
        PubliclyAccessible: bool = None,
        DnsNameServers: str = None,
    ) -> CreateReplicationInstanceResponseTypeDef:
        """
        [Client.create_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        ReplicationSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List[TagTypeDef] = None,
    ) -> CreateReplicationSubnetGroupResponseTypeDef:
        """
        [Client.create_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_replication_task(
        self,
        ReplicationTaskIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ReplicationInstanceArn: str,
        MigrationType: Literal["full-load", "cdc", "full-load-and-cdc"],
        TableMappings: str,
        ReplicationTaskSettings: str = None,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateReplicationTaskResponseTypeDef:
        """
        [Client.create_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_certificate(self, CertificateArn: str) -> DeleteCertificateResponseTypeDef:
        """
        [Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.delete_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_connection(
        self, EndpointArn: str, ReplicationInstanceArn: str
    ) -> DeleteConnectionResponseTypeDef:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.delete_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_endpoint(self, EndpointArn: str) -> DeleteEndpointResponseTypeDef:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.delete_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_event_subscription(
        self, SubscriptionName: str
    ) -> DeleteEventSubscriptionResponseTypeDef:
        """
        [Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.delete_event_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_replication_instance(
        self, ReplicationInstanceArn: str
    ) -> DeleteReplicationInstanceResponseTypeDef:
        """
        [Client.delete_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_replication_subnet_group(
        self, ReplicationSubnetGroupIdentifier: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_replication_task(
        self, ReplicationTaskArn: str
    ) -> DeleteReplicationTaskResponseTypeDef:
        """
        [Client.delete_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_attributes(self) -> DescribeAccountAttributesResponseTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_account_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_certificates(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeCertificatesResponseTypeDef:
        """
        [Client.describe_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_connections(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeConnectionsResponseTypeDef:
        """
        [Client.describe_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_connections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_endpoint_types(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeEndpointTypesResponseTypeDef:
        """
        [Client.describe_endpoint_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoint_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_endpoints(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeEndpointsResponseTypeDef:
        """
        [Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_categories(
        self, SourceType: str = None, Filters: List[FilterTypeDef] = None
    ) -> DescribeEventCategoriesResponseTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_categories)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEventSubscriptionsResponseTypeDef:
        """
        [Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_subscriptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal["replication-instance"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_orderable_replication_instances(
        self, MaxRecords: int = None, Marker: str = None
    ) -> DescribeOrderableReplicationInstancesResponseTypeDef:
        """
        [Client.describe_orderable_replication_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_orderable_replication_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_pending_maintenance_actions(
        self,
        ReplicationInstanceArn: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> DescribePendingMaintenanceActionsResponseTypeDef:
        """
        [Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_pending_maintenance_actions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_refresh_schemas_status(
        self, EndpointArn: str
    ) -> DescribeRefreshSchemasStatusResponseTypeDef:
        """
        [Client.describe_refresh_schemas_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_refresh_schemas_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_replication_instance_task_logs(
        self, ReplicationInstanceArn: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationInstanceTaskLogsResponseTypeDef:
        """
        [Client.describe_replication_instance_task_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instance_task_logs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_replication_instances(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationInstancesResponseTypeDef:
        """
        [Client.describe_replication_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_replication_subnet_groups(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationSubnetGroupsResponseTypeDef:
        """
        [Client.describe_replication_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_subnet_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_replication_task_assessment_results(
        self, ReplicationTaskArn: str = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationTaskAssessmentResultsResponseTypeDef:
        """
        [Client.describe_replication_task_assessment_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_assessment_results)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_replication_tasks(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
    ) -> DescribeReplicationTasksResponseTypeDef:
        """
        [Client.describe_replication_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_schemas(
        self, EndpointArn: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeSchemasResponseTypeDef:
        """
        [Client.describe_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_schemas)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_table_statistics(
        self,
        ReplicationTaskArn: str,
        MaxRecords: int = None,
        Marker: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> DescribeTableStatisticsResponseTypeDef:
        """
        [Client.describe_table_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.describe_table_statistics)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_certificate(
        self,
        CertificateIdentifier: str,
        CertificatePem: str = None,
        CertificateWallet: Union[bytes, IO] = None,
        Tags: List[TagTypeDef] = None,
    ) -> ImportCertificateResponseTypeDef:
        """
        [Client.import_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.import_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_endpoint(
        self,
        EndpointArn: str,
        EndpointIdentifier: str = None,
        EndpointType: Literal["source", "target"] = None,
        EngineName: str = None,
        Username: str = None,
        Password: str = None,
        ServerName: str = None,
        Port: int = None,
        DatabaseName: str = None,
        ExtraConnectionAttributes: str = None,
        CertificateArn: str = None,
        SslMode: Literal["none", "require", "verify-ca", "verify-full"] = None,
        ServiceAccessRoleArn: str = None,
        ExternalTableDefinition: str = None,
        DynamoDbSettings: DynamoDbSettingsTypeDef = None,
        S3Settings: S3SettingsTypeDef = None,
        DmsTransferSettings: DmsTransferSettingsTypeDef = None,
        MongoDbSettings: MongoDbSettingsTypeDef = None,
        KinesisSettings: KinesisSettingsTypeDef = None,
        ElasticsearchSettings: ElasticsearchSettingsTypeDef = None,
        RedshiftSettings: RedshiftSettingsTypeDef = None,
    ) -> ModifyEndpointResponseTypeDef:
        """
        [Client.modify_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.modify_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[str] = None,
        Enabled: bool = None,
    ) -> ModifyEventSubscriptionResponseTypeDef:
        """
        [Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.modify_event_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_replication_instance(
        self,
        ReplicationInstanceArn: str,
        AllocatedStorage: int = None,
        ApplyImmediately: bool = None,
        ReplicationInstanceClass: str = None,
        VpcSecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        ReplicationInstanceIdentifier: str = None,
    ) -> ModifyReplicationInstanceResponseTypeDef:
        """
        [Client.modify_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        SubnetIds: List[str],
        ReplicationSubnetGroupDescription: str = None,
    ) -> ModifyReplicationSubnetGroupResponseTypeDef:
        """
        [Client.modify_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_subnet_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_replication_task(
        self,
        ReplicationTaskArn: str,
        ReplicationTaskIdentifier: str = None,
        MigrationType: Literal["full-load", "cdc", "full-load-and-cdc"] = None,
        TableMappings: str = None,
        ReplicationTaskSettings: str = None,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
    ) -> ModifyReplicationTaskResponseTypeDef:
        """
        [Client.modify_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot_replication_instance(
        self, ReplicationInstanceArn: str, ForceFailover: bool = None
    ) -> RebootReplicationInstanceResponseTypeDef:
        """
        [Client.reboot_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.reboot_replication_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def refresh_schemas(
        self, EndpointArn: str, ReplicationInstanceArn: str
    ) -> RefreshSchemasResponseTypeDef:
        """
        [Client.refresh_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.refresh_schemas)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload_tables(
        self,
        ReplicationTaskArn: str,
        TablesToReload: List[TableToReloadTypeDef],
        ReloadOption: Literal["data-reload", "validate-only"] = None,
    ) -> ReloadTablesResponseTypeDef:
        """
        [Client.reload_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.reload_tables)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.remove_tags_from_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_replication_task(
        self,
        ReplicationTaskArn: str,
        StartReplicationTaskType: Literal[
            "start-replication", "resume-processing", "reload-target"
        ],
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
    ) -> StartReplicationTaskResponseTypeDef:
        """
        [Client.start_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_replication_task_assessment(
        self, ReplicationTaskArn: str
    ) -> StartReplicationTaskAssessmentResponseTypeDef:
        """
        [Client.start_replication_task_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task_assessment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_replication_task(self, ReplicationTaskArn: str) -> StopReplicationTaskResponseTypeDef:
        """
        [Client.stop_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.stop_replication_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def test_connection(
        self, ReplicationInstanceArn: str, EndpointArn: str
    ) -> TestConnectionResponseTypeDef:
        """
        [Client.test_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Client.test_connection)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> paginator_scope.DescribeCertificatesPaginator:
        """
        [Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_connections"]
    ) -> paginator_scope.DescribeConnectionsPaginator:
        """
        [Paginator.DescribeConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_endpoint_types"]
    ) -> paginator_scope.DescribeEndpointTypesPaginator:
        """
        [Paginator.DescribeEndpointTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_endpoints"]
    ) -> paginator_scope.DescribeEndpointsPaginator:
        """
        [Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> paginator_scope.DescribeEventSubscriptionsPaginator:
        """
        [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> paginator_scope.DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_orderable_replication_instances"]
    ) -> paginator_scope.DescribeOrderableReplicationInstancesPaginator:
        """
        [Paginator.DescribeOrderableReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_replication_instances"]
    ) -> paginator_scope.DescribeReplicationInstancesPaginator:
        """
        [Paginator.DescribeReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_replication_subnet_groups"]
    ) -> paginator_scope.DescribeReplicationSubnetGroupsPaginator:
        """
        [Paginator.DescribeReplicationSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_replication_task_assessment_results"]
    ) -> paginator_scope.DescribeReplicationTaskAssessmentResultsPaginator:
        """
        [Paginator.DescribeReplicationTaskAssessmentResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_replication_tasks"]
    ) -> paginator_scope.DescribeReplicationTasksPaginator:
        """
        [Paginator.DescribeReplicationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_schemas"]
    ) -> paginator_scope.DescribeSchemasPaginator:
        """
        [Paginator.DescribeSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_table_statistics"]
    ) -> paginator_scope.DescribeTableStatisticsPaginator:
        """
        [Paginator.DescribeTableStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["endpoint_deleted"]
    ) -> waiter_scope.EndpointDeletedWaiter:
        """
        [Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.EndpointDeleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_instance_available"]
    ) -> waiter_scope.ReplicationInstanceAvailableWaiter:
        """
        [Waiter.ReplicationInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_instance_deleted"]
    ) -> waiter_scope.ReplicationInstanceDeletedWaiter:
        """
        [Waiter.ReplicationInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_task_deleted"]
    ) -> waiter_scope.ReplicationTaskDeletedWaiter:
        """
        [Waiter.ReplicationTaskDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_task_ready"]
    ) -> waiter_scope.ReplicationTaskReadyWaiter:
        """
        [Waiter.ReplicationTaskReady documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskReady)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_task_running"]
    ) -> waiter_scope.ReplicationTaskRunningWaiter:
        """
        [Waiter.ReplicationTaskRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_task_stopped"]
    ) -> waiter_scope.ReplicationTaskStoppedWaiter:
        """
        [Waiter.ReplicationTaskStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["test_connection_succeeds"]
    ) -> waiter_scope.TestConnectionSucceedsWaiter:
        """
        [Waiter.TestConnectionSucceeds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/dms.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds)
        """


class Exceptions:
    AccessDeniedFault: Boto3ClientError
    ClientError: Boto3ClientError
    InsufficientResourceCapacityFault: Boto3ClientError
    InvalidCertificateFault: Boto3ClientError
    InvalidResourceStateFault: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    KMSAccessDeniedFault: Boto3ClientError
    KMSDisabledFault: Boto3ClientError
    KMSInvalidStateFault: Boto3ClientError
    KMSKeyNotAccessibleFault: Boto3ClientError
    KMSNotFoundFault: Boto3ClientError
    KMSThrottlingFault: Boto3ClientError
    ReplicationSubnetGroupDoesNotCoverEnoughAZs: Boto3ClientError
    ResourceAlreadyExistsFault: Boto3ClientError
    ResourceNotFoundFault: Boto3ClientError
    ResourceQuotaExceededFault: Boto3ClientError
    SNSInvalidTopicFault: Boto3ClientError
    SNSNoAuthorizationFault: Boto3ClientError
    StorageQuotaExceededFault: Boto3ClientError
    SubnetAlreadyInUse: Boto3ClientError
    UpgradeDependencyFailureFault: Boto3ClientError
