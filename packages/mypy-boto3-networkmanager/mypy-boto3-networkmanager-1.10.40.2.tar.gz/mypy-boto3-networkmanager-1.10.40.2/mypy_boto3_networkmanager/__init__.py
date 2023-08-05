"Main interface for networkmanager service"
from mypy_boto3_networkmanager.client import NetworkManagerClient as Client, NetworkManagerClient
from mypy_boto3_networkmanager.paginator import (
    DescribeGlobalNetworksPaginator,
    GetCustomerGatewayAssociationsPaginator,
    GetDevicesPaginator,
    GetLinkAssociationsPaginator,
    GetLinksPaginator,
    GetSitesPaginator,
    GetTransitGatewayRegistrationsPaginator,
)


__all__ = (
    "Client",
    "DescribeGlobalNetworksPaginator",
    "GetCustomerGatewayAssociationsPaginator",
    "GetDevicesPaginator",
    "GetLinkAssociationsPaginator",
    "GetLinksPaginator",
    "GetSitesPaginator",
    "GetTransitGatewayRegistrationsPaginator",
    "NetworkManagerClient",
)
