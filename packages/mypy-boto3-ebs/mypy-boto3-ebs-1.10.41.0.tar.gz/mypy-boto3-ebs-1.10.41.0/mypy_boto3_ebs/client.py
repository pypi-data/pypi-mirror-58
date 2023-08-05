"Main interface for ebs service Client"
from __future__ import annotations

from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_ebs.client as client_scope
from mypy_boto3_ebs.type_defs import (
    GetSnapshotBlockResponseTypeDef,
    ListChangedBlocksResponseTypeDef,
    ListSnapshotBlocksResponseTypeDef,
)


__all__ = ("EBSClient",)


class EBSClient(BaseClient):
    """
    [EBS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ebs.html#EBS.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ebs.html#EBS.Client.can_paginate)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ebs.html#EBS.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_snapshot_block(
        self, SnapshotId: str, BlockIndex: int, BlockToken: str
    ) -> GetSnapshotBlockResponseTypeDef:
        """
        [Client.get_snapshot_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ebs.html#EBS.Client.get_snapshot_block)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_changed_blocks(
        self,
        SecondSnapshotId: str,
        FirstSnapshotId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        StartingBlockIndex: int = None,
    ) -> ListChangedBlocksResponseTypeDef:
        """
        [Client.list_changed_blocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ebs.html#EBS.Client.list_changed_blocks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_snapshot_blocks(
        self,
        SnapshotId: str,
        NextToken: str = None,
        MaxResults: int = None,
        StartingBlockIndex: int = None,
    ) -> ListSnapshotBlocksResponseTypeDef:
        """
        [Client.list_snapshot_blocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ebs.html#EBS.Client.list_snapshot_blocks)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError
