"Main interface for opsworkscm service"
from mypy_boto3_opsworkscm.client import OpsWorksCMClient, OpsWorksCMClient as Client
from mypy_boto3_opsworkscm.paginator import (
    DescribeBackupsPaginator,
    DescribeEventsPaginator,
    DescribeServersPaginator,
)
from mypy_boto3_opsworkscm.waiter import NodeAssociatedWaiter


__all__ = (
    "Client",
    "DescribeBackupsPaginator",
    "DescribeEventsPaginator",
    "DescribeServersPaginator",
    "NodeAssociatedWaiter",
    "OpsWorksCMClient",
)
