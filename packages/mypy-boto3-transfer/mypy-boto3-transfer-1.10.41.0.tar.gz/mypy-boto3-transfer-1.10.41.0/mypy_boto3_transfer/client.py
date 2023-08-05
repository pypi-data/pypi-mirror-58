"Main interface for transfer service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_transfer.client as client_scope

# pylint: disable=import-self
import mypy_boto3_transfer.paginator as paginator_scope
from mypy_boto3_transfer.type_defs import (
    CreateServerResponseTypeDef,
    CreateUserResponseTypeDef,
    DescribeServerResponseTypeDef,
    DescribeUserResponseTypeDef,
    EndpointDetailsTypeDef,
    HomeDirectoryMapEntryTypeDef,
    IdentityProviderDetailsTypeDef,
    ImportSshPublicKeyResponseTypeDef,
    ListServersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersResponseTypeDef,
    TagTypeDef,
    TestIdentityProviderResponseTypeDef,
    UpdateServerResponseTypeDef,
    UpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TransferClient",)


class TransferClient(BaseClient):
    """
    [Transfer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_server(
        self,
        EndpointDetails: EndpointDetailsTypeDef = None,
        EndpointType: Literal["PUBLIC", "VPC_ENDPOINT"] = None,
        HostKey: str = None,
        IdentityProviderDetails: IdentityProviderDetailsTypeDef = None,
        IdentityProviderType: Literal["SERVICE_MANAGED", "API_GATEWAY"] = None,
        LoggingRole: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateServerResponseTypeDef:
        """
        [Client.create_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.create_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user(
        self,
        Role: str,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: Literal["PATH", "LOGICAL"] = None,
        HomeDirectoryMappings: List[HomeDirectoryMapEntryTypeDef] = None,
        Policy: str = None,
        SshPublicKeyBody: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.create_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_server(self, ServerId: str) -> None:
        """
        [Client.delete_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.delete_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_ssh_public_key(self, ServerId: str, SshPublicKeyId: str, UserName: str) -> None:
        """
        [Client.delete_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.delete_ssh_public_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user(self, ServerId: str, UserName: str) -> None:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.delete_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_server(self, ServerId: str) -> DescribeServerResponseTypeDef:
        """
        [Client.describe_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.describe_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user(self, ServerId: str, UserName: str) -> DescribeUserResponseTypeDef:
        """
        [Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.describe_user)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_ssh_public_key(
        self, ServerId: str, SshPublicKeyBody: str, UserName: str
    ) -> ImportSshPublicKeyResponseTypeDef:
        """
        [Client.import_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.import_ssh_public_key)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_servers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListServersResponseTypeDef:
        """
        [Client.list_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.list_servers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, Arn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_users(
        self, ServerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListUsersResponseTypeDef:
        """
        [Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.list_users)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_server(self, ServerId: str) -> None:
        """
        [Client.start_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.start_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_server(self, ServerId: str) -> None:
        """
        [Client.stop_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.stop_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, Arn: str, Tags: List[TagTypeDef]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def test_identity_provider(
        self, ServerId: str, UserName: str, UserPassword: str = None
    ) -> TestIdentityProviderResponseTypeDef:
        """
        [Client.test_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.test_identity_provider)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, Arn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_server(
        self,
        ServerId: str,
        EndpointDetails: EndpointDetailsTypeDef = None,
        EndpointType: Literal["PUBLIC", "VPC_ENDPOINT"] = None,
        HostKey: str = None,
        IdentityProviderDetails: IdentityProviderDetailsTypeDef = None,
        LoggingRole: str = None,
    ) -> UpdateServerResponseTypeDef:
        """
        [Client.update_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.update_server)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user(
        self,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: Literal["PATH", "LOGICAL"] = None,
        HomeDirectoryMappings: List[HomeDirectoryMapEntryTypeDef] = None,
        Policy: str = None,
        Role: str = None,
    ) -> UpdateUserResponseTypeDef:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Client.update_user)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_servers"]
    ) -> paginator_scope.ListServersPaginator:
        """
        [Paginator.ListServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/transfer.html#Transfer.Paginator.ListServers)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServiceError: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    ThrottlingException: Boto3ClientError
