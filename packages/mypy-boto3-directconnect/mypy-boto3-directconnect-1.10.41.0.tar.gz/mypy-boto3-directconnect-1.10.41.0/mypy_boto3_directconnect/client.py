"Main interface for directconnect service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_directconnect.client as client_scope

# pylint: disable=import-self
import mypy_boto3_directconnect.paginator as paginator_scope
from mypy_boto3_directconnect.type_defs import (
    AcceptDirectConnectGatewayAssociationProposalResultTypeDef,
    AllocateTransitVirtualInterfaceResultTypeDef,
    ConfirmConnectionResponseTypeDef,
    ConfirmPrivateVirtualInterfaceResponseTypeDef,
    ConfirmPublicVirtualInterfaceResponseTypeDef,
    ConfirmTransitVirtualInterfaceResponseTypeDef,
    ConnectionTypeDef,
    ConnectionsTypeDef,
    CreateBGPPeerResponseTypeDef,
    CreateDirectConnectGatewayAssociationProposalResultTypeDef,
    CreateDirectConnectGatewayAssociationResultTypeDef,
    CreateDirectConnectGatewayResultTypeDef,
    CreateTransitVirtualInterfaceResultTypeDef,
    DeleteBGPPeerResponseTypeDef,
    DeleteDirectConnectGatewayAssociationProposalResultTypeDef,
    DeleteDirectConnectGatewayAssociationResultTypeDef,
    DeleteDirectConnectGatewayResultTypeDef,
    DeleteInterconnectResponseTypeDef,
    DeleteVirtualInterfaceResponseTypeDef,
    DescribeConnectionLoaResponseTypeDef,
    DescribeDirectConnectGatewayAssociationProposalsResultTypeDef,
    DescribeDirectConnectGatewayAssociationsResultTypeDef,
    DescribeDirectConnectGatewayAttachmentsResultTypeDef,
    DescribeDirectConnectGatewaysResultTypeDef,
    DescribeInterconnectLoaResponseTypeDef,
    DescribeTagsResponseTypeDef,
    InterconnectTypeDef,
    InterconnectsTypeDef,
    LagTypeDef,
    LagsTypeDef,
    LoaTypeDef,
    LocationsTypeDef,
    NewBGPPeerTypeDef,
    NewPrivateVirtualInterfaceAllocationTypeDef,
    NewPrivateVirtualInterfaceTypeDef,
    NewPublicVirtualInterfaceAllocationTypeDef,
    NewPublicVirtualInterfaceTypeDef,
    NewTransitVirtualInterfaceAllocationTypeDef,
    NewTransitVirtualInterfaceTypeDef,
    RouteFilterPrefixTypeDef,
    TagTypeDef,
    UpdateDirectConnectGatewayAssociationResultTypeDef,
    VirtualGatewaysTypeDef,
    VirtualInterfaceTypeDef,
    VirtualInterfacesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DirectConnectClient",)


class DirectConnectClient(BaseClient):
    """
    [DirectConnect.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_direct_connect_gateway_association_proposal(
        self,
        directConnectGatewayId: str,
        proposalId: str,
        associatedGatewayOwnerAccount: str,
        overrideAllowedPrefixesToDirectConnectGateway: List[RouteFilterPrefixTypeDef] = None,
    ) -> AcceptDirectConnectGatewayAssociationProposalResultTypeDef:
        """
        [Client.accept_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.accept_direct_connect_gateway_association_proposal)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def allocate_connection_on_interconnect(
        self, bandwidth: str, connectionName: str, ownerAccount: str, interconnectId: str, vlan: int
    ) -> ConnectionTypeDef:
        """
        [Client.allocate_connection_on_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.allocate_connection_on_interconnect)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def allocate_hosted_connection(
        self,
        connectionId: str,
        ownerAccount: str,
        bandwidth: str,
        connectionName: str,
        vlan: int,
        tags: List[TagTypeDef] = None,
    ) -> ConnectionTypeDef:
        """
        [Client.allocate_hosted_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.allocate_hosted_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def allocate_private_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newPrivateVirtualInterfaceAllocation: NewPrivateVirtualInterfaceAllocationTypeDef,
    ) -> VirtualInterfaceTypeDef:
        """
        [Client.allocate_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.allocate_private_virtual_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def allocate_public_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newPublicVirtualInterfaceAllocation: NewPublicVirtualInterfaceAllocationTypeDef,
    ) -> VirtualInterfaceTypeDef:
        """
        [Client.allocate_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.allocate_public_virtual_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def allocate_transit_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newTransitVirtualInterfaceAllocation: NewTransitVirtualInterfaceAllocationTypeDef,
    ) -> AllocateTransitVirtualInterfaceResultTypeDef:
        """
        [Client.allocate_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.allocate_transit_virtual_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_connection_with_lag(self, connectionId: str, lagId: str) -> ConnectionTypeDef:
        """
        [Client.associate_connection_with_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.associate_connection_with_lag)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_hosted_connection(
        self, connectionId: str, parentConnectionId: str
    ) -> ConnectionTypeDef:
        """
        [Client.associate_hosted_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.associate_hosted_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_virtual_interface(
        self, virtualInterfaceId: str, connectionId: str
    ) -> VirtualInterfaceTypeDef:
        """
        [Client.associate_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.associate_virtual_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_connection(self, connectionId: str) -> ConfirmConnectionResponseTypeDef:
        """
        [Client.confirm_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.confirm_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_private_virtual_interface(
        self,
        virtualInterfaceId: str,
        virtualGatewayId: str = None,
        directConnectGatewayId: str = None,
    ) -> ConfirmPrivateVirtualInterfaceResponseTypeDef:
        """
        [Client.confirm_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.confirm_private_virtual_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_public_virtual_interface(
        self, virtualInterfaceId: str
    ) -> ConfirmPublicVirtualInterfaceResponseTypeDef:
        """
        [Client.confirm_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.confirm_public_virtual_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_transit_virtual_interface(
        self, virtualInterfaceId: str, directConnectGatewayId: str
    ) -> ConfirmTransitVirtualInterfaceResponseTypeDef:
        """
        [Client.confirm_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.confirm_transit_virtual_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_bgp_peer(
        self, virtualInterfaceId: str = None, newBGPPeer: NewBGPPeerTypeDef = None
    ) -> CreateBGPPeerResponseTypeDef:
        """
        [Client.create_bgp_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.create_bgp_peer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_connection(
        self,
        location: str,
        bandwidth: str,
        connectionName: str,
        lagId: str = None,
        tags: List[TagTypeDef] = None,
        providerName: str = None,
    ) -> ConnectionTypeDef:
        """
        [Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.create_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_direct_connect_gateway(
        self, directConnectGatewayName: str, amazonSideAsn: int = None
    ) -> CreateDirectConnectGatewayResultTypeDef:
        """
        [Client.create_direct_connect_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_direct_connect_gateway_association(
        self,
        directConnectGatewayId: str,
        gatewayId: str = None,
        addAllowedPrefixesToDirectConnectGateway: List[RouteFilterPrefixTypeDef] = None,
        virtualGatewayId: str = None,
    ) -> CreateDirectConnectGatewayAssociationResultTypeDef:
        """
        [Client.create_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_direct_connect_gateway_association_proposal(
        self,
        directConnectGatewayId: str,
        directConnectGatewayOwnerAccount: str,
        gatewayId: str,
        addAllowedPrefixesToDirectConnectGateway: List[RouteFilterPrefixTypeDef] = None,
        removeAllowedPrefixesToDirectConnectGateway: List[RouteFilterPrefixTypeDef] = None,
    ) -> CreateDirectConnectGatewayAssociationProposalResultTypeDef:
        """
        [Client.create_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway_association_proposal)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_interconnect(
        self,
        interconnectName: str,
        bandwidth: str,
        location: str,
        lagId: str = None,
        tags: List[TagTypeDef] = None,
        providerName: str = None,
    ) -> InterconnectTypeDef:
        """
        [Client.create_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.create_interconnect)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_lag(
        self,
        numberOfConnections: int,
        location: str,
        connectionsBandwidth: str,
        lagName: str,
        connectionId: str = None,
        tags: List[TagTypeDef] = None,
        childConnectionTags: List[TagTypeDef] = None,
        providerName: str = None,
    ) -> LagTypeDef:
        """
        [Client.create_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.create_lag)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_private_virtual_interface(
        self, connectionId: str, newPrivateVirtualInterface: NewPrivateVirtualInterfaceTypeDef
    ) -> VirtualInterfaceTypeDef:
        """
        [Client.create_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.create_private_virtual_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_public_virtual_interface(
        self, connectionId: str, newPublicVirtualInterface: NewPublicVirtualInterfaceTypeDef
    ) -> VirtualInterfaceTypeDef:
        """
        [Client.create_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.create_public_virtual_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_transit_virtual_interface(
        self, connectionId: str, newTransitVirtualInterface: NewTransitVirtualInterfaceTypeDef
    ) -> CreateTransitVirtualInterfaceResultTypeDef:
        """
        [Client.create_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.create_transit_virtual_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bgp_peer(
        self,
        virtualInterfaceId: str = None,
        asn: int = None,
        customerAddress: str = None,
        bgpPeerId: str = None,
    ) -> DeleteBGPPeerResponseTypeDef:
        """
        [Client.delete_bgp_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.delete_bgp_peer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_connection(self, connectionId: str) -> ConnectionTypeDef:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.delete_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_direct_connect_gateway(
        self, directConnectGatewayId: str
    ) -> DeleteDirectConnectGatewayResultTypeDef:
        """
        [Client.delete_direct_connect_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_direct_connect_gateway_association(
        self,
        associationId: str = None,
        directConnectGatewayId: str = None,
        virtualGatewayId: str = None,
    ) -> DeleteDirectConnectGatewayAssociationResultTypeDef:
        """
        [Client.delete_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_direct_connect_gateway_association_proposal(
        self, proposalId: str
    ) -> DeleteDirectConnectGatewayAssociationProposalResultTypeDef:
        """
        [Client.delete_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway_association_proposal)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_interconnect(self, interconnectId: str) -> DeleteInterconnectResponseTypeDef:
        """
        [Client.delete_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.delete_interconnect)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_lag(self, lagId: str) -> LagTypeDef:
        """
        [Client.delete_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.delete_lag)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_virtual_interface(
        self, virtualInterfaceId: str
    ) -> DeleteVirtualInterfaceResponseTypeDef:
        """
        [Client.delete_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.delete_virtual_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_connection_loa(
        self,
        connectionId: str,
        providerName: str = None,
        loaContentType: Literal["application/pdf"] = None,
    ) -> DescribeConnectionLoaResponseTypeDef:
        """
        [Client.describe_connection_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_connection_loa)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_connections(self, connectionId: str = None) -> ConnectionsTypeDef:
        """
        [Client.describe_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_connections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_connections_on_interconnect(self, interconnectId: str) -> ConnectionsTypeDef:
        """
        [Client.describe_connections_on_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_connections_on_interconnect)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_direct_connect_gateway_association_proposals(
        self,
        directConnectGatewayId: str = None,
        proposalId: str = None,
        associatedGatewayId: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeDirectConnectGatewayAssociationProposalsResultTypeDef:
        """
        [Client.describe_direct_connect_gateway_association_proposals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_association_proposals)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_direct_connect_gateway_associations(
        self,
        associationId: str = None,
        associatedGatewayId: str = None,
        directConnectGatewayId: str = None,
        maxResults: int = None,
        nextToken: str = None,
        virtualGatewayId: str = None,
    ) -> DescribeDirectConnectGatewayAssociationsResultTypeDef:
        """
        [Client.describe_direct_connect_gateway_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_direct_connect_gateway_attachments(
        self,
        directConnectGatewayId: str = None,
        virtualInterfaceId: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeDirectConnectGatewayAttachmentsResultTypeDef:
        """
        [Client.describe_direct_connect_gateway_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_attachments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_direct_connect_gateways(
        self, directConnectGatewayId: str = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeDirectConnectGatewaysResultTypeDef:
        """
        [Client.describe_direct_connect_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateways)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_hosted_connections(self, connectionId: str) -> ConnectionsTypeDef:
        """
        [Client.describe_hosted_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_hosted_connections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_interconnect_loa(
        self,
        interconnectId: str,
        providerName: str = None,
        loaContentType: Literal["application/pdf"] = None,
    ) -> DescribeInterconnectLoaResponseTypeDef:
        """
        [Client.describe_interconnect_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_interconnect_loa)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_interconnects(self, interconnectId: str = None) -> InterconnectsTypeDef:
        """
        [Client.describe_interconnects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_interconnects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_lags(self, lagId: str = None) -> LagsTypeDef:
        """
        [Client.describe_lags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_lags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_loa(
        self,
        connectionId: str,
        providerName: str = None,
        loaContentType: Literal["application/pdf"] = None,
    ) -> LoaTypeDef:
        """
        [Client.describe_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_loa)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_locations(self) -> LocationsTypeDef:
        """
        [Client.describe_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_locations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tags(self, resourceArns: List[str]) -> DescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_virtual_gateways(self) -> VirtualGatewaysTypeDef:
        """
        [Client.describe_virtual_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_virtual_gateways)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_virtual_interfaces(
        self, connectionId: str = None, virtualInterfaceId: str = None
    ) -> VirtualInterfacesTypeDef:
        """
        [Client.describe_virtual_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.describe_virtual_interfaces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_connection_from_lag(self, connectionId: str, lagId: str) -> ConnectionTypeDef:
        """
        [Client.disassociate_connection_from_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.disassociate_connection_from_lag)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_direct_connect_gateway_association(
        self,
        associationId: str = None,
        addAllowedPrefixesToDirectConnectGateway: List[RouteFilterPrefixTypeDef] = None,
        removeAllowedPrefixesToDirectConnectGateway: List[RouteFilterPrefixTypeDef] = None,
    ) -> UpdateDirectConnectGatewayAssociationResultTypeDef:
        """
        [Client.update_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.update_direct_connect_gateway_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_lag(self, lagId: str, lagName: str = None, minimumLinks: int = None) -> LagTypeDef:
        """
        [Client.update_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.update_lag)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_virtual_interface_attributes(
        self, virtualInterfaceId: str, mtu: int = None
    ) -> VirtualInterfaceTypeDef:
        """
        [Client.update_virtual_interface_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Client.update_virtual_interface_attributes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateway_associations"]
    ) -> paginator_scope.DescribeDirectConnectGatewayAssociationsPaginator:
        """
        [Paginator.DescribeDirectConnectGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAssociations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateway_attachments"]
    ) -> paginator_scope.DescribeDirectConnectGatewayAttachmentsPaginator:
        """
        [Paginator.DescribeDirectConnectGatewayAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAttachments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateways"]
    ) -> paginator_scope.DescribeDirectConnectGatewaysPaginator:
        """
        [Paginator.DescribeDirectConnectGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGateways)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DirectConnectClientException: Boto3ClientError
    DirectConnectServerException: Boto3ClientError
    DuplicateTagKeysException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
