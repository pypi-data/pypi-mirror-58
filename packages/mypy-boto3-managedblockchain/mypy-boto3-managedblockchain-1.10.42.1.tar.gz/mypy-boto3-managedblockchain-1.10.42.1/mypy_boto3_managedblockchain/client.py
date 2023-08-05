"Main interface for managedblockchain service Client"
from __future__ import annotations

import sys
from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_managedblockchain.client as client_scope
from mypy_boto3_managedblockchain.type_defs import (
    CreateMemberOutputTypeDef,
    CreateNetworkOutputTypeDef,
    CreateNodeOutputTypeDef,
    CreateProposalOutputTypeDef,
    GetMemberOutputTypeDef,
    GetNetworkOutputTypeDef,
    GetNodeOutputTypeDef,
    GetProposalOutputTypeDef,
    ListInvitationsOutputTypeDef,
    ListMembersOutputTypeDef,
    ListNetworksOutputTypeDef,
    ListNodesOutputTypeDef,
    ListProposalVotesOutputTypeDef,
    ListProposalsOutputTypeDef,
    MemberConfigurationTypeDef,
    NetworkFrameworkConfigurationTypeDef,
    NodeConfigurationTypeDef,
    ProposalActionsTypeDef,
    VotingPolicyTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ManagedBlockchainClient",)


class ManagedBlockchainClient(BaseClient):
    """
    [ManagedBlockchain.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_member(
        self,
        ClientRequestToken: str,
        InvitationId: str,
        NetworkId: str,
        MemberConfiguration: MemberConfigurationTypeDef,
    ) -> CreateMemberOutputTypeDef:
        """
        [Client.create_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_member)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network(
        self,
        ClientRequestToken: str,
        Name: str,
        Framework: Literal["HYPERLEDGER_FABRIC"],
        FrameworkVersion: str,
        VotingPolicy: VotingPolicyTypeDef,
        MemberConfiguration: MemberConfigurationTypeDef,
        Description: str = None,
        FrameworkConfiguration: NetworkFrameworkConfigurationTypeDef = None,
    ) -> CreateNetworkOutputTypeDef:
        """
        [Client.create_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_network)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_node(
        self,
        ClientRequestToken: str,
        NetworkId: str,
        MemberId: str,
        NodeConfiguration: NodeConfigurationTypeDef,
    ) -> CreateNodeOutputTypeDef:
        """
        [Client.create_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_node)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_proposal(
        self,
        ClientRequestToken: str,
        NetworkId: str,
        MemberId: str,
        Actions: ProposalActionsTypeDef,
        Description: str = None,
    ) -> CreateProposalOutputTypeDef:
        """
        [Client.create_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_proposal)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_member(self, NetworkId: str, MemberId: str) -> Dict[str, Any]:
        """
        [Client.delete_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_member)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_node(self, NetworkId: str, MemberId: str, NodeId: str) -> Dict[str, Any]:
        """
        [Client.delete_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_node)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_member(self, NetworkId: str, MemberId: str) -> GetMemberOutputTypeDef:
        """
        [Client.get_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_member)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_network(self, NetworkId: str) -> GetNetworkOutputTypeDef:
        """
        [Client.get_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_network)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_node(self, NetworkId: str, MemberId: str, NodeId: str) -> GetNodeOutputTypeDef:
        """
        [Client.get_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_node)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_proposal(self, NetworkId: str, ProposalId: str) -> GetProposalOutputTypeDef:
        """
        [Client.get_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_proposal)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsOutputTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_invitations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_members(
        self,
        NetworkId: str,
        Name: str = None,
        Status: Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"] = None,
        IsOwned: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListMembersOutputTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_networks(
        self,
        Name: str = None,
        Framework: Literal["HYPERLEDGER_FABRIC"] = None,
        Status: Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListNetworksOutputTypeDef:
        """
        [Client.list_networks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_networks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_nodes(
        self,
        NetworkId: str,
        MemberId: str,
        Status: Literal[
            "CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED", "FAILED"
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListNodesOutputTypeDef:
        """
        [Client.list_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_nodes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_proposal_votes(
        self, NetworkId: str, ProposalId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListProposalVotesOutputTypeDef:
        """
        [Client.list_proposal_votes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposal_votes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_proposals(
        self, NetworkId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListProposalsOutputTypeDef:
        """
        [Client.list_proposals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposals)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_invitation(self, InvitationId: str) -> Dict[str, Any]:
        """
        [Client.reject_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.reject_invitation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def vote_on_proposal(
        self, NetworkId: str, ProposalId: str, VoterMemberId: str, Vote: Literal["YES", "NO"]
    ) -> Dict[str, Any]:
        """
        [Client.vote_on_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/managedblockchain.html#ManagedBlockchain.Client.vote_on_proposal)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    IllegalActionException: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceNotReadyException: Boto3ClientError
    ThrottlingException: Boto3ClientError
