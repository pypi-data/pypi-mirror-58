"Main interface for detective service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_detective.client as client_scope
from mypy_boto3_detective.type_defs import (
    AccountTypeDef,
    CreateGraphResponseTypeDef,
    CreateMembersResponseTypeDef,
    DeleteMembersResponseTypeDef,
    GetMembersResponseTypeDef,
    ListGraphsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
)


__all__ = ("DetectiveClient",)


class DetectiveClient(BaseClient):
    """
    [Detective.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_invitation(self, GraphArn: str) -> None:
        """
        [Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.accept_invitation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_graph(self) -> CreateGraphResponseTypeDef:
        """
        [Client.create_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.create_graph)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_members(
        self, GraphArn: str, Accounts: List[AccountTypeDef], Message: str = None
    ) -> CreateMembersResponseTypeDef:
        """
        [Client.create_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.create_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_graph(self, GraphArn: str) -> None:
        """
        [Client.delete_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.delete_graph)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_members(self, GraphArn: str, AccountIds: List[str]) -> DeleteMembersResponseTypeDef:
        """
        [Client.delete_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.delete_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_membership(self, GraphArn: str) -> None:
        """
        [Client.disassociate_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.disassociate_membership)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_members(self, GraphArn: str, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        [Client.get_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.get_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_graphs(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListGraphsResponseTypeDef:
        """
        [Client.list_graphs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.list_graphs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_invitations(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.list_invitations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_members(
        self, GraphArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMembersResponseTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.list_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_invitation(self, GraphArn: str) -> None:
        """
        [Client.reject_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/detective.html#Detective.Client.reject_invitation)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ValidationException: Boto3ClientError
