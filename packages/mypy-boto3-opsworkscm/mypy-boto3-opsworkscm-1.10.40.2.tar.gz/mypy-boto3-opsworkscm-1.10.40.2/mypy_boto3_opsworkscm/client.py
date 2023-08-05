"Main interface for opsworkscm service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_opsworkscm.client as client_scope

# pylint: disable=import-self
import mypy_boto3_opsworkscm.paginator as paginator_scope
from mypy_boto3_opsworkscm.type_defs import (
    AssociateNodeResponseTypeDef,
    CreateBackupResponseTypeDef,
    CreateServerResponseTypeDef,
    DescribeAccountAttributesResponseTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeNodeAssociationStatusResponseTypeDef,
    DescribeServersResponseTypeDef,
    DisassociateNodeResponseTypeDef,
    EngineAttributeTypeDef,
    ExportServerEngineAttributeResponseTypeDef,
    StartMaintenanceResponseTypeDef,
    UpdateServerEngineAttributesResponseTypeDef,
    UpdateServerResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_opsworkscm.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("OpsWorksCMClient",)


class OpsWorksCMClient(BaseClient):
    """
    [OpsWorksCM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_node(
        self, ServerName: str, NodeName: str, EngineAttributes: List[EngineAttributeTypeDef]
    ) -> AssociateNodeResponseTypeDef:
        """
        [Client.associate_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.associate_node)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_backup(
        self, ServerName: str, Description: str = None
    ) -> CreateBackupResponseTypeDef:
        """
        [Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.create_backup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_server(
        self,
        ServerName: str,
        InstanceProfileArn: str,
        InstanceType: str,
        ServiceRoleArn: str,
        AssociatePublicIpAddress: bool = None,
        CustomDomain: str = None,
        CustomCertificate: str = None,
        CustomPrivateKey: str = None,
        DisableAutomatedBackup: bool = None,
        Engine: str = None,
        EngineModel: str = None,
        EngineVersion: str = None,
        EngineAttributes: List[EngineAttributeTypeDef] = None,
        BackupRetentionCount: int = None,
        KeyPair: str = None,
        PreferredMaintenanceWindow: str = None,
        PreferredBackupWindow: str = None,
        SecurityGroupIds: List[str] = None,
        SubnetIds: List[str] = None,
        BackupId: str = None,
    ) -> CreateServerResponseTypeDef:
        """
        [Client.create_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.create_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_backup(self, BackupId: str) -> Dict[str, Any]:
        """
        [Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_backup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_server(self, ServerName: str) -> Dict[str, Any]:
        """
        [Client.delete_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_attributes(self) -> DescribeAccountAttributesResponseTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_account_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_backups(
        self,
        BackupId: str = None,
        ServerName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeBackupsResponseTypeDef:
        """
        [Client.describe_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_backups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_events(
        self, ServerName: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_node_association_status(
        self, NodeAssociationStatusToken: str, ServerName: str
    ) -> DescribeNodeAssociationStatusResponseTypeDef:
        """
        [Client.describe_node_association_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_node_association_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_servers(
        self, ServerName: str = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeServersResponseTypeDef:
        """
        [Client.describe_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_servers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_node(
        self, ServerName: str, NodeName: str, EngineAttributes: List[EngineAttributeTypeDef] = None
    ) -> DisassociateNodeResponseTypeDef:
        """
        [Client.disassociate_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.disassociate_node)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_server_engine_attribute(
        self,
        ExportAttributeName: str,
        ServerName: str,
        InputAttributes: List[EngineAttributeTypeDef] = None,
    ) -> ExportServerEngineAttributeResponseTypeDef:
        """
        [Client.export_server_engine_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.export_server_engine_attribute)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_server(
        self, BackupId: str, ServerName: str, InstanceType: str = None, KeyPair: str = None
    ) -> Dict[str, Any]:
        """
        [Client.restore_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.restore_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_maintenance(
        self, ServerName: str, EngineAttributes: List[EngineAttributeTypeDef] = None
    ) -> StartMaintenanceResponseTypeDef:
        """
        [Client.start_maintenance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.start_maintenance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_server(
        self,
        ServerName: str,
        DisableAutomatedBackup: bool = None,
        BackupRetentionCount: int = None,
        PreferredMaintenanceWindow: str = None,
        PreferredBackupWindow: str = None,
    ) -> UpdateServerResponseTypeDef:
        """
        [Client.update_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_server_engine_attributes(
        self, ServerName: str, AttributeName: str, AttributeValue: str = None
    ) -> UpdateServerEngineAttributesResponseTypeDef:
        """
        [Client.update_server_engine_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server_engine_attributes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> paginator_scope.DescribeBackupsPaginator:
        """
        [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> paginator_scope.DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_servers"]
    ) -> paginator_scope.DescribeServersPaginator:
        """
        [Paginator.DescribeServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["node_associated"]
    ) -> waiter_scope.NodeAssociatedWaiter:
        """
        [Waiter.NodeAssociated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/opsworkscm.html#OpsWorksCM.Waiter.NodeAssociated)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidStateException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError
