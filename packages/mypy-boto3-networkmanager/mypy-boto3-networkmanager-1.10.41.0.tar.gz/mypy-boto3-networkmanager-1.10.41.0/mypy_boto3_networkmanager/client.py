"Main interface for networkmanager service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_networkmanager.client as client_scope

# pylint: disable=import-self
import mypy_boto3_networkmanager.paginator as paginator_scope
from mypy_boto3_networkmanager.type_defs import (
    AssociateCustomerGatewayResponseTypeDef,
    AssociateLinkResponseTypeDef,
    BandwidthTypeDef,
    CreateDeviceResponseTypeDef,
    CreateGlobalNetworkResponseTypeDef,
    CreateLinkResponseTypeDef,
    CreateSiteResponseTypeDef,
    DeleteDeviceResponseTypeDef,
    DeleteGlobalNetworkResponseTypeDef,
    DeleteLinkResponseTypeDef,
    DeleteSiteResponseTypeDef,
    DeregisterTransitGatewayResponseTypeDef,
    DescribeGlobalNetworksResponseTypeDef,
    DisassociateCustomerGatewayResponseTypeDef,
    DisassociateLinkResponseTypeDef,
    GetCustomerGatewayAssociationsResponseTypeDef,
    GetDevicesResponseTypeDef,
    GetLinkAssociationsResponseTypeDef,
    GetLinksResponseTypeDef,
    GetSitesResponseTypeDef,
    GetTransitGatewayRegistrationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LocationTypeDef,
    RegisterTransitGatewayResponseTypeDef,
    TagTypeDef,
    UpdateDeviceResponseTypeDef,
    UpdateGlobalNetworkResponseTypeDef,
    UpdateLinkResponseTypeDef,
    UpdateSiteResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("NetworkManagerClient",)


class NetworkManagerClient(BaseClient):
    """
    [NetworkManager.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_customer_gateway(
        self, CustomerGatewayArn: str, GlobalNetworkId: str, DeviceId: str, LinkId: str = None
    ) -> AssociateCustomerGatewayResponseTypeDef:
        """
        [Client.associate_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.associate_customer_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_link(
        self, GlobalNetworkId: str, DeviceId: str, LinkId: str
    ) -> AssociateLinkResponseTypeDef:
        """
        [Client.associate_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.associate_link)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_device(
        self,
        GlobalNetworkId: str,
        Description: str = None,
        Type: str = None,
        Vendor: str = None,
        Model: str = None,
        SerialNumber: str = None,
        Location: LocationTypeDef = None,
        SiteId: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDeviceResponseTypeDef:
        """
        [Client.create_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.create_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_global_network(
        self, Description: str = None, Tags: List[TagTypeDef] = None
    ) -> CreateGlobalNetworkResponseTypeDef:
        """
        [Client.create_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.create_global_network)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_link(
        self,
        GlobalNetworkId: str,
        Bandwidth: BandwidthTypeDef,
        SiteId: str,
        Description: str = None,
        Type: str = None,
        Provider: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateLinkResponseTypeDef:
        """
        [Client.create_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.create_link)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_site(
        self,
        GlobalNetworkId: str,
        Description: str = None,
        Location: LocationTypeDef = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateSiteResponseTypeDef:
        """
        [Client.create_site documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.create_site)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_device(self, GlobalNetworkId: str, DeviceId: str) -> DeleteDeviceResponseTypeDef:
        """
        [Client.delete_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.delete_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_global_network(self, GlobalNetworkId: str) -> DeleteGlobalNetworkResponseTypeDef:
        """
        [Client.delete_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.delete_global_network)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_link(self, GlobalNetworkId: str, LinkId: str) -> DeleteLinkResponseTypeDef:
        """
        [Client.delete_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.delete_link)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_site(self, GlobalNetworkId: str, SiteId: str) -> DeleteSiteResponseTypeDef:
        """
        [Client.delete_site documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.delete_site)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_transit_gateway(
        self, GlobalNetworkId: str, TransitGatewayArn: str
    ) -> DeregisterTransitGatewayResponseTypeDef:
        """
        [Client.deregister_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.deregister_transit_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_global_networks(
        self, GlobalNetworkIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeGlobalNetworksResponseTypeDef:
        """
        [Client.describe_global_networks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.describe_global_networks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_customer_gateway(
        self, GlobalNetworkId: str, CustomerGatewayArn: str
    ) -> DisassociateCustomerGatewayResponseTypeDef:
        """
        [Client.disassociate_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.disassociate_customer_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_link(
        self, GlobalNetworkId: str, DeviceId: str, LinkId: str
    ) -> DisassociateLinkResponseTypeDef:
        """
        [Client.disassociate_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.disassociate_link)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_customer_gateway_associations(
        self,
        GlobalNetworkId: str,
        CustomerGatewayArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetCustomerGatewayAssociationsResponseTypeDef:
        """
        [Client.get_customer_gateway_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.get_customer_gateway_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_devices(
        self,
        GlobalNetworkId: str,
        DeviceIds: List[str] = None,
        SiteId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetDevicesResponseTypeDef:
        """
        [Client.get_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.get_devices)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_link_associations(
        self,
        GlobalNetworkId: str,
        DeviceId: str = None,
        LinkId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetLinkAssociationsResponseTypeDef:
        """
        [Client.get_link_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.get_link_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_links(
        self,
        GlobalNetworkId: str,
        LinkIds: List[str] = None,
        SiteId: str = None,
        Type: str = None,
        Provider: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetLinksResponseTypeDef:
        """
        [Client.get_links documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.get_links)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_sites(
        self,
        GlobalNetworkId: str,
        SiteIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetSitesResponseTypeDef:
        """
        [Client.get_sites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.get_sites)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_transit_gateway_registrations(
        self,
        GlobalNetworkId: str,
        TransitGatewayArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetTransitGatewayRegistrationsResponseTypeDef:
        """
        [Client.get_transit_gateway_registrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.get_transit_gateway_registrations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_transit_gateway(
        self, GlobalNetworkId: str, TransitGatewayArn: str
    ) -> RegisterTransitGatewayResponseTypeDef:
        """
        [Client.register_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.register_transit_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_device(
        self,
        GlobalNetworkId: str,
        DeviceId: str,
        Description: str = None,
        Type: str = None,
        Vendor: str = None,
        Model: str = None,
        SerialNumber: str = None,
        Location: LocationTypeDef = None,
        SiteId: str = None,
    ) -> UpdateDeviceResponseTypeDef:
        """
        [Client.update_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.update_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_global_network(
        self, GlobalNetworkId: str, Description: str = None
    ) -> UpdateGlobalNetworkResponseTypeDef:
        """
        [Client.update_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.update_global_network)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_link(
        self,
        GlobalNetworkId: str,
        LinkId: str,
        Description: str = None,
        Type: str = None,
        Bandwidth: BandwidthTypeDef = None,
        Provider: str = None,
    ) -> UpdateLinkResponseTypeDef:
        """
        [Client.update_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.update_link)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_site(
        self,
        GlobalNetworkId: str,
        SiteId: str,
        Description: str = None,
        Location: LocationTypeDef = None,
    ) -> UpdateSiteResponseTypeDef:
        """
        [Client.update_site documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Client.update_site)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_global_networks"]
    ) -> paginator_scope.DescribeGlobalNetworksPaginator:
        """
        [Paginator.DescribeGlobalNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_customer_gateway_associations"]
    ) -> paginator_scope.GetCustomerGatewayAssociationsPaginator:
        """
        [Paginator.GetCustomerGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_devices"]
    ) -> paginator_scope.GetDevicesPaginator:
        """
        [Paginator.GetDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_link_associations"]
    ) -> paginator_scope.GetLinkAssociationsPaginator:
        """
        [Paginator.GetLinkAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_links"]
    ) -> paginator_scope.GetLinksPaginator:
        """
        [Paginator.GetLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_sites"]
    ) -> paginator_scope.GetSitesPaginator:
        """
        [Paginator.GetSites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_registrations"]
    ) -> paginator_scope.GetTransitGatewayRegistrationsPaginator:
        """
        [Paginator.GetTransitGatewayRegistrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceQuotaExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    ValidationException: Boto3ClientError
