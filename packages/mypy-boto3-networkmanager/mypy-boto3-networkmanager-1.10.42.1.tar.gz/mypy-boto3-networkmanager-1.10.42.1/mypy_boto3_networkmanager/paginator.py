"Main interface for networkmanager service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_networkmanager.type_defs import (
    DescribeGlobalNetworksResponseTypeDef,
    GetCustomerGatewayAssociationsResponseTypeDef,
    GetDevicesResponseTypeDef,
    GetLinkAssociationsResponseTypeDef,
    GetLinksResponseTypeDef,
    GetSitesResponseTypeDef,
    GetTransitGatewayRegistrationsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeGlobalNetworksPaginator",
    "GetCustomerGatewayAssociationsPaginator",
    "GetDevicesPaginator",
    "GetLinkAssociationsPaginator",
    "GetLinksPaginator",
    "GetSitesPaginator",
    "GetTransitGatewayRegistrationsPaginator",
)


class DescribeGlobalNetworksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeGlobalNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GlobalNetworkIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeGlobalNetworksResponseTypeDef, None, None]:
        """
        [DescribeGlobalNetworks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks.paginate)
        """


class GetCustomerGatewayAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetCustomerGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        CustomerGatewayArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetCustomerGatewayAssociationsResponseTypeDef, None, None]:
        """
        [GetCustomerGatewayAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations.paginate)
        """


class GetDevicesPaginator(Boto3Paginator):
    """
    [Paginator.GetDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        DeviceIds: List[str] = None,
        SiteId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetDevicesResponseTypeDef, None, None]:
        """
        [GetDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices.paginate)
        """


class GetLinkAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetLinkAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        DeviceId: str = None,
        LinkId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetLinkAssociationsResponseTypeDef, None, None]:
        """
        [GetLinkAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations.paginate)
        """


class GetLinksPaginator(Boto3Paginator):
    """
    [Paginator.GetLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        LinkIds: List[str] = None,
        SiteId: str = None,
        Type: str = None,
        Provider: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetLinksResponseTypeDef, None, None]:
        """
        [GetLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks.paginate)
        """


class GetSitesPaginator(Boto3Paginator):
    """
    [Paginator.GetSites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        SiteIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetSitesResponseTypeDef, None, None]:
        """
        [GetSites.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites.paginate)
        """


class GetTransitGatewayRegistrationsPaginator(Boto3Paginator):
    """
    [Paginator.GetTransitGatewayRegistrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GlobalNetworkId: str,
        TransitGatewayArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetTransitGatewayRegistrationsResponseTypeDef, None, None]:
        """
        [GetTransitGatewayRegistrations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations.paginate)
        """
