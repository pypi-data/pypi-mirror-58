"Main interface for dms service"
from mypy_boto3_dms.client import (
    DatabaseMigrationServiceClient,
    DatabaseMigrationServiceClient as Client,
)
from mypy_boto3_dms.paginator import (
    DescribeCertificatesPaginator,
    DescribeConnectionsPaginator,
    DescribeEndpointTypesPaginator,
    DescribeEndpointsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeEventsPaginator,
    DescribeOrderableReplicationInstancesPaginator,
    DescribeReplicationInstancesPaginator,
    DescribeReplicationSubnetGroupsPaginator,
    DescribeReplicationTaskAssessmentResultsPaginator,
    DescribeReplicationTasksPaginator,
    DescribeSchemasPaginator,
    DescribeTableStatisticsPaginator,
)
from mypy_boto3_dms.waiter import (
    EndpointDeletedWaiter,
    ReplicationInstanceAvailableWaiter,
    ReplicationInstanceDeletedWaiter,
    ReplicationTaskDeletedWaiter,
    ReplicationTaskReadyWaiter,
    ReplicationTaskRunningWaiter,
    ReplicationTaskStoppedWaiter,
    TestConnectionSucceedsWaiter,
)


__all__ = (
    "Client",
    "DatabaseMigrationServiceClient",
    "DescribeCertificatesPaginator",
    "DescribeConnectionsPaginator",
    "DescribeEndpointTypesPaginator",
    "DescribeEndpointsPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableReplicationInstancesPaginator",
    "DescribeReplicationInstancesPaginator",
    "DescribeReplicationSubnetGroupsPaginator",
    "DescribeReplicationTaskAssessmentResultsPaginator",
    "DescribeReplicationTasksPaginator",
    "DescribeSchemasPaginator",
    "DescribeTableStatisticsPaginator",
    "EndpointDeletedWaiter",
    "ReplicationInstanceAvailableWaiter",
    "ReplicationInstanceDeletedWaiter",
    "ReplicationTaskDeletedWaiter",
    "ReplicationTaskReadyWaiter",
    "ReplicationTaskRunningWaiter",
    "ReplicationTaskStoppedWaiter",
    "TestConnectionSucceedsWaiter",
)
