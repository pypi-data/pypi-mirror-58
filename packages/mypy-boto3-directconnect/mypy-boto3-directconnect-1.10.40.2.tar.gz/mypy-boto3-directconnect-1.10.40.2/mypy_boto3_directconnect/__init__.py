"Main interface for directconnect service"
from mypy_boto3_directconnect.client import DirectConnectClient, DirectConnectClient as Client
from mypy_boto3_directconnect.paginator import (
    DescribeDirectConnectGatewayAssociationsPaginator,
    DescribeDirectConnectGatewayAttachmentsPaginator,
    DescribeDirectConnectGatewaysPaginator,
)


__all__ = (
    "Client",
    "DescribeDirectConnectGatewayAssociationsPaginator",
    "DescribeDirectConnectGatewayAttachmentsPaginator",
    "DescribeDirectConnectGatewaysPaginator",
    "DirectConnectClient",
)
