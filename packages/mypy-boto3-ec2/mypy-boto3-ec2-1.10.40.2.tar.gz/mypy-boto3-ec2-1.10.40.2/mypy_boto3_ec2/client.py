"Main interface for ec2 service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, IO, List, Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_ec2.client as client_scope

# pylint: disable=import-self
import mypy_boto3_ec2.paginator as paginator_scope
from mypy_boto3_ec2.type_defs import (
    AcceptReservedInstancesExchangeQuoteResultTypeDef,
    AcceptTransitGatewayPeeringAttachmentResultTypeDef,
    AcceptTransitGatewayVpcAttachmentResultTypeDef,
    AcceptVpcEndpointConnectionsResultTypeDef,
    AcceptVpcPeeringConnectionResultTypeDef,
    AdvertiseByoipCidrResultTypeDef,
    AllocateAddressResultTypeDef,
    AllocateHostsResultTypeDef,
    ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef,
    AssignIpv6AddressesResultTypeDef,
    AssignPrivateIpAddressesResultTypeDef,
    AssociateAddressResultTypeDef,
    AssociateClientVpnTargetNetworkResultTypeDef,
    AssociateIamInstanceProfileResultTypeDef,
    AssociateRouteTableResultTypeDef,
    AssociateSubnetCidrBlockResultTypeDef,
    AssociateTransitGatewayMulticastDomainResultTypeDef,
    AssociateTransitGatewayRouteTableResultTypeDef,
    AssociateVpcCidrBlockResultTypeDef,
    AttachClassicLinkVpcResultTypeDef,
    AttachNetworkInterfaceResultTypeDef,
    AttachVpnGatewayResultTypeDef,
    AttributeBooleanValueTypeDef,
    AttributeValueTypeDef,
    AuthorizeClientVpnIngressResultTypeDef,
    BlobAttributeValueTypeDef,
    BlockDeviceMappingTypeDef,
    BundleInstanceResultTypeDef,
    CancelBundleTaskResultTypeDef,
    CancelCapacityReservationResultTypeDef,
    CancelImportTaskResultTypeDef,
    CancelReservedInstancesListingResultTypeDef,
    CancelSpotFleetRequestsResponseTypeDef,
    CancelSpotInstanceRequestsResultTypeDef,
    CapacityReservationSpecificationTypeDef,
    CidrAuthorizationContextTypeDef,
    ClientDataTypeDef,
    ClientVpnAuthenticationRequestTypeDef,
    ConfirmProductInstanceResultTypeDef,
    ConnectionLogOptionsTypeDef,
    CopyFpgaImageResultTypeDef,
    CopyImageResultTypeDef,
    CopySnapshotResultTypeDef,
    CpuOptionsRequestTypeDef,
    CreateCapacityReservationResultTypeDef,
    CreateClientVpnEndpointResultTypeDef,
    CreateClientVpnRouteResultTypeDef,
    CreateCustomerGatewayResultTypeDef,
    CreateDefaultSubnetResultTypeDef,
    CreateDefaultVpcResultTypeDef,
    CreateDhcpOptionsResultTypeDef,
    CreateEgressOnlyInternetGatewayResultTypeDef,
    CreateFleetResultTypeDef,
    CreateFlowLogsResultTypeDef,
    CreateFpgaImageResultTypeDef,
    CreateImageResultTypeDef,
    CreateInstanceExportTaskResultTypeDef,
    CreateInternetGatewayResultTypeDef,
    CreateLaunchTemplateResultTypeDef,
    CreateLaunchTemplateVersionResultTypeDef,
    CreateLocalGatewayRouteResultTypeDef,
    CreateLocalGatewayRouteTableVpcAssociationResultTypeDef,
    CreateNatGatewayResultTypeDef,
    CreateNetworkAclResultTypeDef,
    CreateNetworkInterfacePermissionResultTypeDef,
    CreateNetworkInterfaceResultTypeDef,
    CreateReservedInstancesListingResultTypeDef,
    CreateRouteResultTypeDef,
    CreateRouteTableResultTypeDef,
    CreateSecurityGroupResultTypeDef,
    CreateSnapshotsResultTypeDef,
    CreateSpotDatafeedSubscriptionResultTypeDef,
    CreateSubnetResultTypeDef,
    CreateTrafficMirrorFilterResultTypeDef,
    CreateTrafficMirrorFilterRuleResultTypeDef,
    CreateTrafficMirrorSessionResultTypeDef,
    CreateTrafficMirrorTargetResultTypeDef,
    CreateTransitGatewayMulticastDomainResultTypeDef,
    CreateTransitGatewayPeeringAttachmentResultTypeDef,
    CreateTransitGatewayResultTypeDef,
    CreateTransitGatewayRouteResultTypeDef,
    CreateTransitGatewayRouteTableResultTypeDef,
    CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef,
    CreateTransitGatewayVpcAttachmentResultTypeDef,
    CreateVolumePermissionModificationsTypeDef,
    CreateVpcEndpointConnectionNotificationResultTypeDef,
    CreateVpcEndpointResultTypeDef,
    CreateVpcEndpointServiceConfigurationResultTypeDef,
    CreateVpcPeeringConnectionResultTypeDef,
    CreateVpcResultTypeDef,
    CreateVpnConnectionResultTypeDef,
    CreateVpnGatewayResultTypeDef,
    CreditSpecificationRequestTypeDef,
    DeleteClientVpnEndpointResultTypeDef,
    DeleteClientVpnRouteResultTypeDef,
    DeleteEgressOnlyInternetGatewayResultTypeDef,
    DeleteFleetsResultTypeDef,
    DeleteFlowLogsResultTypeDef,
    DeleteFpgaImageResultTypeDef,
    DeleteLaunchTemplateResultTypeDef,
    DeleteLaunchTemplateVersionsResultTypeDef,
    DeleteLocalGatewayRouteResultTypeDef,
    DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef,
    DeleteNatGatewayResultTypeDef,
    DeleteNetworkInterfacePermissionResultTypeDef,
    DeleteQueuedReservedInstancesResultTypeDef,
    DeleteTrafficMirrorFilterResultTypeDef,
    DeleteTrafficMirrorFilterRuleResultTypeDef,
    DeleteTrafficMirrorSessionResultTypeDef,
    DeleteTrafficMirrorTargetResultTypeDef,
    DeleteTransitGatewayMulticastDomainResultTypeDef,
    DeleteTransitGatewayPeeringAttachmentResultTypeDef,
    DeleteTransitGatewayResultTypeDef,
    DeleteTransitGatewayRouteResultTypeDef,
    DeleteTransitGatewayRouteTableResultTypeDef,
    DeleteTransitGatewayVpcAttachmentResultTypeDef,
    DeleteVpcEndpointConnectionNotificationsResultTypeDef,
    DeleteVpcEndpointServiceConfigurationsResultTypeDef,
    DeleteVpcEndpointsResultTypeDef,
    DeleteVpcPeeringConnectionResultTypeDef,
    DeprovisionByoipCidrResultTypeDef,
    DeregisterTransitGatewayMulticastGroupMembersResultTypeDef,
    DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeAddressesResultTypeDef,
    DescribeAggregateIdFormatResultTypeDef,
    DescribeAvailabilityZonesResultTypeDef,
    DescribeBundleTasksResultTypeDef,
    DescribeByoipCidrsResultTypeDef,
    DescribeCapacityReservationsResultTypeDef,
    DescribeClassicLinkInstancesResultTypeDef,
    DescribeClientVpnAuthorizationRulesResultTypeDef,
    DescribeClientVpnConnectionsResultTypeDef,
    DescribeClientVpnEndpointsResultTypeDef,
    DescribeClientVpnRoutesResultTypeDef,
    DescribeClientVpnTargetNetworksResultTypeDef,
    DescribeCoipPoolsResultTypeDef,
    DescribeConversionTasksResultTypeDef,
    DescribeCustomerGatewaysResultTypeDef,
    DescribeDhcpOptionsResultTypeDef,
    DescribeEgressOnlyInternetGatewaysResultTypeDef,
    DescribeElasticGpusResultTypeDef,
    DescribeExportImageTasksResultTypeDef,
    DescribeExportTasksResultTypeDef,
    DescribeFastSnapshotRestoresResultTypeDef,
    DescribeFleetHistoryResultTypeDef,
    DescribeFleetInstancesResultTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeFlowLogsResultTypeDef,
    DescribeFpgaImageAttributeResultTypeDef,
    DescribeFpgaImagesResultTypeDef,
    DescribeHostReservationOfferingsResultTypeDef,
    DescribeHostReservationsResultTypeDef,
    DescribeHostsResultTypeDef,
    DescribeIamInstanceProfileAssociationsResultTypeDef,
    DescribeIdFormatResultTypeDef,
    DescribeIdentityIdFormatResultTypeDef,
    DescribeImagesResultTypeDef,
    DescribeImportImageTasksResultTypeDef,
    DescribeImportSnapshotTasksResultTypeDef,
    DescribeInstanceCreditSpecificationsResultTypeDef,
    DescribeInstanceStatusResultTypeDef,
    DescribeInstanceTypeOfferingsResultTypeDef,
    DescribeInstanceTypesResultTypeDef,
    DescribeInstancesResultTypeDef,
    DescribeInternetGatewaysResultTypeDef,
    DescribeKeyPairsResultTypeDef,
    DescribeLaunchTemplateVersionsResultTypeDef,
    DescribeLaunchTemplatesResultTypeDef,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef,
    DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef,
    DescribeLocalGatewayRouteTablesResultTypeDef,
    DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef,
    DescribeLocalGatewayVirtualInterfacesResultTypeDef,
    DescribeLocalGatewaysResultTypeDef,
    DescribeMovingAddressesResultTypeDef,
    DescribeNatGatewaysResultTypeDef,
    DescribeNetworkAclsResultTypeDef,
    DescribeNetworkInterfaceAttributeResultTypeDef,
    DescribeNetworkInterfacePermissionsResultTypeDef,
    DescribeNetworkInterfacesResultTypeDef,
    DescribePlacementGroupsResultTypeDef,
    DescribePrefixListsResultTypeDef,
    DescribePrincipalIdFormatResultTypeDef,
    DescribePublicIpv4PoolsResultTypeDef,
    DescribeRegionsResultTypeDef,
    DescribeReservedInstancesListingsResultTypeDef,
    DescribeReservedInstancesModificationsResultTypeDef,
    DescribeReservedInstancesOfferingsResultTypeDef,
    DescribeReservedInstancesResultTypeDef,
    DescribeRouteTablesResultTypeDef,
    DescribeScheduledInstanceAvailabilityResultTypeDef,
    DescribeScheduledInstancesResultTypeDef,
    DescribeSecurityGroupReferencesResultTypeDef,
    DescribeSecurityGroupsResultTypeDef,
    DescribeSnapshotAttributeResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeSpotDatafeedSubscriptionResultTypeDef,
    DescribeSpotFleetInstancesResponseTypeDef,
    DescribeSpotFleetRequestHistoryResponseTypeDef,
    DescribeSpotFleetRequestsResponseTypeDef,
    DescribeSpotInstanceRequestsResultTypeDef,
    DescribeSpotPriceHistoryResultTypeDef,
    DescribeStaleSecurityGroupsResultTypeDef,
    DescribeSubnetsResultTypeDef,
    DescribeTagsResultTypeDef,
    DescribeTrafficMirrorFiltersResultTypeDef,
    DescribeTrafficMirrorSessionsResultTypeDef,
    DescribeTrafficMirrorTargetsResultTypeDef,
    DescribeTransitGatewayAttachmentsResultTypeDef,
    DescribeTransitGatewayMulticastDomainsResultTypeDef,
    DescribeTransitGatewayPeeringAttachmentsResultTypeDef,
    DescribeTransitGatewayRouteTablesResultTypeDef,
    DescribeTransitGatewayVpcAttachmentsResultTypeDef,
    DescribeTransitGatewaysResultTypeDef,
    DescribeVolumeAttributeResultTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVolumesModificationsResultTypeDef,
    DescribeVolumesResultTypeDef,
    DescribeVpcAttributeResultTypeDef,
    DescribeVpcClassicLinkDnsSupportResultTypeDef,
    DescribeVpcClassicLinkResultTypeDef,
    DescribeVpcEndpointConnectionNotificationsResultTypeDef,
    DescribeVpcEndpointConnectionsResultTypeDef,
    DescribeVpcEndpointServiceConfigurationsResultTypeDef,
    DescribeVpcEndpointServicePermissionsResultTypeDef,
    DescribeVpcEndpointServicesResultTypeDef,
    DescribeVpcEndpointsResultTypeDef,
    DescribeVpcPeeringConnectionsResultTypeDef,
    DescribeVpcsResultTypeDef,
    DescribeVpnConnectionsResultTypeDef,
    DescribeVpnGatewaysResultTypeDef,
    DetachClassicLinkVpcResultTypeDef,
    DisableEbsEncryptionByDefaultResultTypeDef,
    DisableFastSnapshotRestoresResultTypeDef,
    DisableTransitGatewayRouteTablePropagationResultTypeDef,
    DisableVpcClassicLinkDnsSupportResultTypeDef,
    DisableVpcClassicLinkResultTypeDef,
    DisassociateClientVpnTargetNetworkResultTypeDef,
    DisassociateIamInstanceProfileResultTypeDef,
    DisassociateSubnetCidrBlockResultTypeDef,
    DisassociateTransitGatewayMulticastDomainResultTypeDef,
    DisassociateTransitGatewayRouteTableResultTypeDef,
    DisassociateVpcCidrBlockResultTypeDef,
    DiskImageDetailTypeDef,
    DiskImageTypeDef,
    DnsServersOptionsModifyStructureTypeDef,
    ElasticGpuSpecificationTypeDef,
    ElasticInferenceAcceleratorTypeDef,
    EnableEbsEncryptionByDefaultResultTypeDef,
    EnableFastSnapshotRestoresResultTypeDef,
    EnableTransitGatewayRouteTablePropagationResultTypeDef,
    EnableVpcClassicLinkDnsSupportResultTypeDef,
    EnableVpcClassicLinkResultTypeDef,
    ExportClientVpnClientCertificateRevocationListResultTypeDef,
    ExportClientVpnClientConfigurationResultTypeDef,
    ExportImageResultTypeDef,
    ExportTaskS3LocationRequestTypeDef,
    ExportToS3TaskSpecificationTypeDef,
    ExportTransitGatewayRoutesResultTypeDef,
    FilterTypeDef,
    FleetLaunchTemplateConfigRequestTypeDef,
    GetCapacityReservationUsageResultTypeDef,
    GetCoipPoolUsageResultTypeDef,
    GetConsoleOutputResultTypeDef,
    GetConsoleScreenshotResultTypeDef,
    GetDefaultCreditSpecificationResultTypeDef,
    GetEbsDefaultKmsKeyIdResultTypeDef,
    GetEbsEncryptionByDefaultResultTypeDef,
    GetHostReservationPurchasePreviewResultTypeDef,
    GetLaunchTemplateDataResultTypeDef,
    GetPasswordDataResultTypeDef,
    GetReservedInstancesExchangeQuoteResultTypeDef,
    GetTransitGatewayAttachmentPropagationsResultTypeDef,
    GetTransitGatewayMulticastDomainAssociationsResultTypeDef,
    GetTransitGatewayRouteTableAssociationsResultTypeDef,
    GetTransitGatewayRouteTablePropagationsResultTypeDef,
    HibernationOptionsRequestTypeDef,
    IamInstanceProfileSpecificationTypeDef,
    IcmpTypeCodeTypeDef,
    ImageAttributeTypeDef,
    ImageDiskContainerTypeDef,
    ImportClientVpnClientCertificateRevocationListResultTypeDef,
    ImportImageLicenseConfigurationRequestTypeDef,
    ImportImageResultTypeDef,
    ImportInstanceLaunchSpecificationTypeDef,
    ImportInstanceResultTypeDef,
    ImportKeyPairResultTypeDef,
    ImportSnapshotResultTypeDef,
    ImportVolumeResultTypeDef,
    InstanceAttributeTypeDef,
    InstanceBlockDeviceMappingSpecificationTypeDef,
    InstanceCreditSpecificationRequestTypeDef,
    InstanceIpv6AddressTypeDef,
    InstanceMarketOptionsRequestTypeDef,
    InstanceMetadataOptionsRequestTypeDef,
    InstanceNetworkInterfaceSpecificationTypeDef,
    InstanceSpecificationTypeDef,
    IpPermissionTypeDef,
    KeyPairTypeDef,
    LaunchPermissionModificationsTypeDef,
    LaunchTemplateSpecificationTypeDef,
    LicenseConfigurationRequestTypeDef,
    LoadPermissionModificationsTypeDef,
    ModifyCapacityReservationResultTypeDef,
    ModifyClientVpnEndpointResultTypeDef,
    ModifyDefaultCreditSpecificationResultTypeDef,
    ModifyEbsDefaultKmsKeyIdResultTypeDef,
    ModifyFleetResultTypeDef,
    ModifyFpgaImageAttributeResultTypeDef,
    ModifyHostsResultTypeDef,
    ModifyInstanceCapacityReservationAttributesResultTypeDef,
    ModifyInstanceCreditSpecificationResultTypeDef,
    ModifyInstanceEventStartTimeResultTypeDef,
    ModifyInstanceMetadataOptionsResultTypeDef,
    ModifyInstancePlacementResultTypeDef,
    ModifyLaunchTemplateResultTypeDef,
    ModifyReservedInstancesResultTypeDef,
    ModifySpotFleetRequestResponseTypeDef,
    ModifyTrafficMirrorFilterNetworkServicesResultTypeDef,
    ModifyTrafficMirrorFilterRuleResultTypeDef,
    ModifyTrafficMirrorSessionResultTypeDef,
    ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef,
    ModifyTransitGatewayVpcAttachmentResultTypeDef,
    ModifyVolumeResultTypeDef,
    ModifyVpcEndpointConnectionNotificationResultTypeDef,
    ModifyVpcEndpointResultTypeDef,
    ModifyVpcEndpointServiceConfigurationResultTypeDef,
    ModifyVpcEndpointServicePermissionsResultTypeDef,
    ModifyVpcPeeringConnectionOptionsResultTypeDef,
    ModifyVpcTenancyResultTypeDef,
    ModifyVpnConnectionResultTypeDef,
    ModifyVpnTunnelCertificateResultTypeDef,
    ModifyVpnTunnelOptionsResultTypeDef,
    ModifyVpnTunnelOptionsSpecificationTypeDef,
    MonitorInstancesResultTypeDef,
    MoveAddressToVpcResultTypeDef,
    NetworkInterfaceAttachmentChangesTypeDef,
    NewDhcpConfigurationTypeDef,
    OnDemandOptionsRequestTypeDef,
    PeeringConnectionOptionsRequestTypeDef,
    PlacementTypeDef,
    PortRangeTypeDef,
    PriceScheduleSpecificationTypeDef,
    PrivateIpAddressSpecificationTypeDef,
    ProvisionByoipCidrResultTypeDef,
    PurchaseHostReservationResultTypeDef,
    PurchaseRequestTypeDef,
    PurchaseReservedInstancesOfferingResultTypeDef,
    PurchaseScheduledInstancesResultTypeDef,
    RegisterImageResultTypeDef,
    RegisterTransitGatewayMulticastGroupMembersResultTypeDef,
    RegisterTransitGatewayMulticastGroupSourcesResultTypeDef,
    RejectTransitGatewayPeeringAttachmentResultTypeDef,
    RejectTransitGatewayVpcAttachmentResultTypeDef,
    RejectVpcEndpointConnectionsResultTypeDef,
    RejectVpcPeeringConnectionResultTypeDef,
    ReleaseHostsResultTypeDef,
    ReplaceIamInstanceProfileAssociationResultTypeDef,
    ReplaceNetworkAclAssociationResultTypeDef,
    ReplaceRouteTableAssociationResultTypeDef,
    ReplaceTransitGatewayRouteResultTypeDef,
    RequestLaunchTemplateDataTypeDef,
    RequestSpotFleetResponseTypeDef,
    RequestSpotInstancesResultTypeDef,
    RequestSpotLaunchSpecificationTypeDef,
    ReservationTypeDef,
    ReservedInstanceLimitPriceTypeDef,
    ReservedInstancesConfigurationTypeDef,
    ResetEbsDefaultKmsKeyIdResultTypeDef,
    ResetFpgaImageAttributeResultTypeDef,
    RestoreAddressToClassicResultTypeDef,
    RevokeClientVpnIngressResultTypeDef,
    RunInstancesMonitoringEnabledTypeDef,
    RunScheduledInstancesResultTypeDef,
    ScheduledInstanceRecurrenceRequestTypeDef,
    ScheduledInstancesLaunchSpecificationTypeDef,
    SearchLocalGatewayRoutesResultTypeDef,
    SearchTransitGatewayMulticastGroupsResultTypeDef,
    SearchTransitGatewayRoutesResultTypeDef,
    SlotDateTimeRangeRequestTypeDef,
    SlotStartTimeRangeRequestTypeDef,
    SnapshotDiskContainerTypeDef,
    SnapshotTypeDef,
    SpotFleetRequestConfigDataTypeDef,
    SpotOptionsRequestTypeDef,
    StartInstancesResultTypeDef,
    StopInstancesResultTypeDef,
    StorageLocationTypeDef,
    StorageTypeDef,
    TagSpecificationTypeDef,
    TagTypeDef,
    TargetCapacitySpecificationRequestTypeDef,
    TargetConfigurationRequestTypeDef,
    TerminateClientVpnConnectionsResultTypeDef,
    TerminateInstancesResultTypeDef,
    TrafficMirrorPortRangeRequestTypeDef,
    TransitGatewayRequestOptionsTypeDef,
    UnassignIpv6AddressesResultTypeDef,
    UnmonitorInstancesResultTypeDef,
    UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef,
    UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef,
    VolumeAttachmentTypeDef,
    VolumeDetailTypeDef,
    VolumeTypeDef,
    VpnConnectionOptionsSpecificationTypeDef,
    WithdrawByoipCidrResultTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_ec2.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EC2Client",)


class EC2Client(BaseClient):
    """
    [EC2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_reserved_instances_exchange_quote(
        self,
        ReservedInstanceIds: List[str],
        DryRun: bool = None,
        TargetConfigurations: List[TargetConfigurationRequestTypeDef] = None,
    ) -> AcceptReservedInstancesExchangeQuoteResultTypeDef:
        """
        [Client.accept_reserved_instances_exchange_quote documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.accept_reserved_instances_exchange_quote)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_transit_gateway_peering_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> AcceptTransitGatewayPeeringAttachmentResultTypeDef:
        """
        [Client.accept_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.accept_transit_gateway_peering_attachment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_transit_gateway_vpc_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> AcceptTransitGatewayVpcAttachmentResultTypeDef:
        """
        [Client.accept_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.accept_transit_gateway_vpc_attachment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_vpc_endpoint_connections(
        self, ServiceId: str, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> AcceptVpcEndpointConnectionsResultTypeDef:
        """
        [Client.accept_vpc_endpoint_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.accept_vpc_endpoint_connections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_vpc_peering_connection(
        self, DryRun: bool = None, VpcPeeringConnectionId: str = None
    ) -> AcceptVpcPeeringConnectionResultTypeDef:
        """
        [Client.accept_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.accept_vpc_peering_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def advertise_byoip_cidr(
        self, Cidr: str, DryRun: bool = None
    ) -> AdvertiseByoipCidrResultTypeDef:
        """
        [Client.advertise_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.advertise_byoip_cidr)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def allocate_address(
        self,
        Domain: Literal["vpc", "standard"] = None,
        Address: str = None,
        PublicIpv4Pool: str = None,
        NetworkBorderGroup: str = None,
        CustomerOwnedIpv4Pool: str = None,
        DryRun: bool = None,
    ) -> AllocateAddressResultTypeDef:
        """
        [Client.allocate_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.allocate_address)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def allocate_hosts(
        self,
        AvailabilityZone: str,
        Quantity: int,
        AutoPlacement: Literal["on", "off"] = None,
        ClientToken: str = None,
        InstanceType: str = None,
        InstanceFamily: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        HostRecovery: Literal["on", "off"] = None,
    ) -> AllocateHostsResultTypeDef:
        """
        [Client.allocate_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.allocate_hosts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def apply_security_groups_to_client_vpn_target_network(
        self, ClientVpnEndpointId: str, VpcId: str, SecurityGroupIds: List[str], DryRun: bool = None
    ) -> ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef:
        """
        [Client.apply_security_groups_to_client_vpn_target_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.apply_security_groups_to_client_vpn_target_network)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assign_ipv6_addresses(
        self, NetworkInterfaceId: str, Ipv6AddressCount: int = None, Ipv6Addresses: List[str] = None
    ) -> AssignIpv6AddressesResultTypeDef:
        """
        [Client.assign_ipv6_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.assign_ipv6_addresses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assign_private_ip_addresses(
        self,
        NetworkInterfaceId: str,
        AllowReassignment: bool = None,
        PrivateIpAddresses: List[str] = None,
        SecondaryPrivateIpAddressCount: int = None,
    ) -> AssignPrivateIpAddressesResultTypeDef:
        """
        [Client.assign_private_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.assign_private_ip_addresses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_address(
        self,
        AllocationId: str = None,
        InstanceId: str = None,
        PublicIp: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None,
    ) -> AssociateAddressResultTypeDef:
        """
        [Client.associate_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.associate_address)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_client_vpn_target_network(
        self, ClientVpnEndpointId: str, SubnetId: str, ClientToken: str = None, DryRun: bool = None
    ) -> AssociateClientVpnTargetNetworkResultTypeDef:
        """
        [Client.associate_client_vpn_target_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.associate_client_vpn_target_network)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_dhcp_options(self, DhcpOptionsId: str, VpcId: str, DryRun: bool = None) -> None:
        """
        [Client.associate_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.associate_dhcp_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_iam_instance_profile(
        self, IamInstanceProfile: IamInstanceProfileSpecificationTypeDef, InstanceId: str
    ) -> AssociateIamInstanceProfileResultTypeDef:
        """
        [Client.associate_iam_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.associate_iam_instance_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_route_table(
        self, RouteTableId: str, DryRun: bool = None, SubnetId: str = None, GatewayId: str = None
    ) -> AssociateRouteTableResultTypeDef:
        """
        [Client.associate_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.associate_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_subnet_cidr_block(
        self, Ipv6CidrBlock: str, SubnetId: str
    ) -> AssociateSubnetCidrBlockResultTypeDef:
        """
        [Client.associate_subnet_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.associate_subnet_cidr_block)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_transit_gateway_multicast_domain(
        self,
        TransitGatewayMulticastDomainId: str = None,
        TransitGatewayAttachmentId: str = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
    ) -> AssociateTransitGatewayMulticastDomainResultTypeDef:
        """
        [Client.associate_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.associate_transit_gateway_multicast_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_transit_gateway_route_table(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> AssociateTransitGatewayRouteTableResultTypeDef:
        """
        [Client.associate_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.associate_transit_gateway_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_vpc_cidr_block(
        self,
        VpcId: str,
        AmazonProvidedIpv6CidrBlock: bool = None,
        CidrBlock: str = None,
        Ipv6CidrBlockNetworkBorderGroup: str = None,
    ) -> AssociateVpcCidrBlockResultTypeDef:
        """
        [Client.associate_vpc_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.associate_vpc_cidr_block)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_classic_link_vpc(
        self, Groups: List[str], InstanceId: str, VpcId: str, DryRun: bool = None
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        [Client.attach_classic_link_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.attach_classic_link_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_internet_gateway(
        self, InternetGatewayId: str, VpcId: str, DryRun: bool = None
    ) -> None:
        """
        [Client.attach_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.attach_internet_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_network_interface(
        self, DeviceIndex: int, InstanceId: str, NetworkInterfaceId: str, DryRun: bool = None
    ) -> AttachNetworkInterfaceResultTypeDef:
        """
        [Client.attach_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.attach_network_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_volume(
        self, Device: str, InstanceId: str, VolumeId: str, DryRun: bool = None
    ) -> VolumeAttachmentTypeDef:
        """
        [Client.attach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.attach_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_vpn_gateway(
        self, VpcId: str, VpnGatewayId: str, DryRun: bool = None
    ) -> AttachVpnGatewayResultTypeDef:
        """
        [Client.attach_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.attach_vpn_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_client_vpn_ingress(
        self,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str = None,
        AuthorizeAllGroups: bool = None,
        Description: str = None,
        ClientToken: str = None,
        DryRun: bool = None,
    ) -> AuthorizeClientVpnIngressResultTypeDef:
        """
        [Client.authorize_client_vpn_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.authorize_client_vpn_ingress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_security_group_egress(
        self,
        GroupId: str,
        DryRun: bool = None,
        IpPermissions: List[IpPermissionTypeDef] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
    ) -> None:
        """
        [Client.authorize_security_group_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.authorize_security_group_egress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_security_group_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupId: str = None,
        GroupName: str = None,
        IpPermissions: List[IpPermissionTypeDef] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.authorize_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.authorize_security_group_ingress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def bundle_instance(
        self, InstanceId: str, Storage: StorageTypeDef, DryRun: bool = None
    ) -> BundleInstanceResultTypeDef:
        """
        [Client.bundle_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.bundle_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_bundle_task(
        self, BundleId: str, DryRun: bool = None
    ) -> CancelBundleTaskResultTypeDef:
        """
        [Client.cancel_bundle_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.cancel_bundle_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_capacity_reservation(
        self, CapacityReservationId: str, DryRun: bool = None
    ) -> CancelCapacityReservationResultTypeDef:
        """
        [Client.cancel_capacity_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.cancel_capacity_reservation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_conversion_task(
        self, ConversionTaskId: str, DryRun: bool = None, ReasonMessage: str = None
    ) -> None:
        """
        [Client.cancel_conversion_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.cancel_conversion_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_export_task(self, ExportTaskId: str) -> None:
        """
        [Client.cancel_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.cancel_export_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_import_task(
        self, CancelReason: str = None, DryRun: bool = None, ImportTaskId: str = None
    ) -> CancelImportTaskResultTypeDef:
        """
        [Client.cancel_import_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.cancel_import_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_reserved_instances_listing(
        self, ReservedInstancesListingId: str
    ) -> CancelReservedInstancesListingResultTypeDef:
        """
        [Client.cancel_reserved_instances_listing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.cancel_reserved_instances_listing)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_spot_fleet_requests(
        self, SpotFleetRequestIds: List[str], TerminateInstances: bool, DryRun: bool = None
    ) -> CancelSpotFleetRequestsResponseTypeDef:
        """
        [Client.cancel_spot_fleet_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.cancel_spot_fleet_requests)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_spot_instance_requests(
        self, SpotInstanceRequestIds: List[str], DryRun: bool = None
    ) -> CancelSpotInstanceRequestsResultTypeDef:
        """
        [Client.cancel_spot_instance_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.cancel_spot_instance_requests)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_product_instance(
        self, InstanceId: str, ProductCode: str, DryRun: bool = None
    ) -> ConfirmProductInstanceResultTypeDef:
        """
        [Client.confirm_product_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.confirm_product_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_fpga_image(
        self,
        SourceFpgaImageId: str,
        SourceRegion: str,
        DryRun: bool = None,
        Description: str = None,
        Name: str = None,
        ClientToken: str = None,
    ) -> CopyFpgaImageResultTypeDef:
        """
        [Client.copy_fpga_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.copy_fpga_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_image(
        self,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        ClientToken: str = None,
        Description: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        DryRun: bool = None,
    ) -> CopyImageResultTypeDef:
        """
        [Client.copy_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.copy_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_snapshot(
        self,
        SourceRegion: str,
        SourceSnapshotId: str,
        Description: str = None,
        DestinationRegion: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        PresignedUrl: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
    ) -> CopySnapshotResultTypeDef:
        """
        [Client.copy_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.copy_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_capacity_reservation(
        self,
        InstanceType: str,
        InstancePlatform: Literal[
            "Linux/UNIX",
            "Red Hat Enterprise Linux",
            "SUSE Linux",
            "Windows",
            "Windows with SQL Server",
            "Windows with SQL Server Enterprise",
            "Windows with SQL Server Standard",
            "Windows with SQL Server Web",
            "Linux with SQL Server Standard",
            "Linux with SQL Server Web",
            "Linux with SQL Server Enterprise",
        ],
        InstanceCount: int,
        ClientToken: str = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Tenancy: Literal["default", "dedicated"] = None,
        EbsOptimized: bool = None,
        EphemeralStorage: bool = None,
        EndDate: datetime = None,
        EndDateType: Literal["unlimited", "limited"] = None,
        InstanceMatchCriteria: Literal["open", "targeted"] = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
    ) -> CreateCapacityReservationResultTypeDef:
        """
        [Client.create_capacity_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_capacity_reservation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_client_vpn_endpoint(
        self,
        ClientCidrBlock: str,
        ServerCertificateArn: str,
        AuthenticationOptions: List[ClientVpnAuthenticationRequestTypeDef],
        ConnectionLogOptions: ConnectionLogOptionsTypeDef,
        DnsServers: List[str] = None,
        TransportProtocol: Literal["tcp", "udp"] = None,
        Description: str = None,
        SplitTunnel: bool = None,
        DryRun: bool = None,
        ClientToken: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
    ) -> CreateClientVpnEndpointResultTypeDef:
        """
        [Client.create_client_vpn_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_client_vpn_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_client_vpn_route(
        self,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str,
        Description: str = None,
        ClientToken: str = None,
        DryRun: bool = None,
    ) -> CreateClientVpnRouteResultTypeDef:
        """
        [Client.create_client_vpn_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_client_vpn_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_customer_gateway(
        self,
        BgpAsn: int,
        Type: Literal["ipsec.1"],
        PublicIp: str = None,
        CertificateArn: str = None,
        DeviceName: str = None,
        DryRun: bool = None,
    ) -> CreateCustomerGatewayResultTypeDef:
        """
        [Client.create_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_customer_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_default_subnet(
        self, AvailabilityZone: str, DryRun: bool = None
    ) -> CreateDefaultSubnetResultTypeDef:
        """
        [Client.create_default_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_default_subnet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_default_vpc(self, DryRun: bool = None) -> CreateDefaultVpcResultTypeDef:
        """
        [Client.create_default_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_default_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dhcp_options(
        self, DhcpConfigurations: List[NewDhcpConfigurationTypeDef], DryRun: bool = None
    ) -> CreateDhcpOptionsResultTypeDef:
        """
        [Client.create_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_dhcp_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_egress_only_internet_gateway(
        self, VpcId: str, ClientToken: str = None, DryRun: bool = None
    ) -> CreateEgressOnlyInternetGatewayResultTypeDef:
        """
        [Client.create_egress_only_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_egress_only_internet_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_fleet(
        self,
        LaunchTemplateConfigs: List[FleetLaunchTemplateConfigRequestTypeDef],
        TargetCapacitySpecification: TargetCapacitySpecificationRequestTypeDef,
        DryRun: bool = None,
        ClientToken: str = None,
        SpotOptions: SpotOptionsRequestTypeDef = None,
        OnDemandOptions: OnDemandOptionsRequestTypeDef = None,
        ExcessCapacityTerminationPolicy: Literal["no-termination", "termination"] = None,
        TerminateInstancesWithExpiration: bool = None,
        Type: Literal["request", "maintain", "instant"] = None,
        ValidFrom: datetime = None,
        ValidUntil: datetime = None,
        ReplaceUnhealthyInstances: bool = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
    ) -> CreateFleetResultTypeDef:
        """
        [Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_flow_logs(
        self,
        ResourceIds: List[str],
        ResourceType: Literal["VPC", "Subnet", "NetworkInterface"],
        TrafficType: Literal["ACCEPT", "REJECT", "ALL"],
        DryRun: bool = None,
        ClientToken: str = None,
        DeliverLogsPermissionArn: str = None,
        LogGroupName: str = None,
        LogDestinationType: Literal["cloud-watch-logs", "s3"] = None,
        LogDestination: str = None,
        LogFormat: str = None,
    ) -> CreateFlowLogsResultTypeDef:
        """
        [Client.create_flow_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_flow_logs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_fpga_image(
        self,
        InputStorageLocation: StorageLocationTypeDef,
        DryRun: bool = None,
        LogsStorageLocation: StorageLocationTypeDef = None,
        Description: str = None,
        Name: str = None,
        ClientToken: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
    ) -> CreateFpgaImageResultTypeDef:
        """
        [Client.create_fpga_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_fpga_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_image(
        self,
        InstanceId: str,
        Name: str,
        BlockDeviceMappings: List[BlockDeviceMappingTypeDef] = None,
        Description: str = None,
        DryRun: bool = None,
        NoReboot: bool = None,
    ) -> CreateImageResultTypeDef:
        """
        [Client.create_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instance_export_task(
        self,
        InstanceId: str,
        Description: str = None,
        ExportToS3Task: ExportToS3TaskSpecificationTypeDef = None,
        TargetEnvironment: Literal["citrix", "vmware", "microsoft"] = None,
    ) -> CreateInstanceExportTaskResultTypeDef:
        """
        [Client.create_instance_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_instance_export_task)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_internet_gateway(self, DryRun: bool = None) -> CreateInternetGatewayResultTypeDef:
        """
        [Client.create_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_internet_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_key_pair(self, KeyName: str, DryRun: bool = None) -> KeyPairTypeDef:
        """
        [Client.create_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_launch_template(
        self,
        LaunchTemplateName: str,
        LaunchTemplateData: RequestLaunchTemplateDataTypeDef,
        DryRun: bool = None,
        ClientToken: str = None,
        VersionDescription: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
    ) -> CreateLaunchTemplateResultTypeDef:
        """
        [Client.create_launch_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_launch_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_launch_template_version(
        self,
        LaunchTemplateData: RequestLaunchTemplateDataTypeDef,
        DryRun: bool = None,
        ClientToken: str = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        SourceVersion: str = None,
        VersionDescription: str = None,
    ) -> CreateLaunchTemplateVersionResultTypeDef:
        """
        [Client.create_launch_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_launch_template_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_local_gateway_route(
        self,
        DestinationCidrBlock: str,
        LocalGatewayRouteTableId: str,
        LocalGatewayVirtualInterfaceGroupId: str,
        DryRun: bool = None,
    ) -> CreateLocalGatewayRouteResultTypeDef:
        """
        [Client.create_local_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_local_gateway_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_local_gateway_route_table_vpc_association(
        self, LocalGatewayRouteTableId: str, VpcId: str, DryRun: bool = None
    ) -> CreateLocalGatewayRouteTableVpcAssociationResultTypeDef:
        """
        [Client.create_local_gateway_route_table_vpc_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_local_gateway_route_table_vpc_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_nat_gateway(
        self, AllocationId: str, SubnetId: str, ClientToken: str = None
    ) -> CreateNatGatewayResultTypeDef:
        """
        [Client.create_nat_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_nat_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_acl(self, VpcId: str, DryRun: bool = None) -> CreateNetworkAclResultTypeDef:
        """
        [Client.create_network_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_network_acl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_acl_entry(
        self,
        Egress: bool,
        NetworkAclId: str,
        Protocol: str,
        RuleAction: Literal["allow", "deny"],
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: IcmpTypeCodeTypeDef = None,
        Ipv6CidrBlock: str = None,
        PortRange: PortRangeTypeDef = None,
    ) -> None:
        """
        [Client.create_network_acl_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_network_acl_entry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_interface(
        self,
        SubnetId: str,
        Description: str = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List[InstanceIpv6AddressTypeDef] = None,
        PrivateIpAddress: str = None,
        PrivateIpAddresses: List[PrivateIpAddressSpecificationTypeDef] = None,
        SecondaryPrivateIpAddressCount: int = None,
        InterfaceType: Literal["efa"] = None,
    ) -> CreateNetworkInterfaceResultTypeDef:
        """
        [Client.create_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_network_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_interface_permission(
        self,
        NetworkInterfaceId: str,
        Permission: Literal["INSTANCE-ATTACH", "EIP-ASSOCIATE"],
        AwsAccountId: str = None,
        AwsService: str = None,
        DryRun: bool = None,
    ) -> CreateNetworkInterfacePermissionResultTypeDef:
        """
        [Client.create_network_interface_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_network_interface_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_placement_group(
        self,
        DryRun: bool = None,
        GroupName: str = None,
        Strategy: Literal["cluster", "spread", "partition"] = None,
        PartitionCount: int = None,
    ) -> None:
        """
        [Client.create_placement_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_placement_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_reserved_instances_listing(
        self,
        ClientToken: str,
        InstanceCount: int,
        PriceSchedules: List[PriceScheduleSpecificationTypeDef],
        ReservedInstancesId: str,
    ) -> CreateReservedInstancesListingResultTypeDef:
        """
        [Client.create_reserved_instances_listing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_reserved_instances_listing)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_route(
        self,
        RouteTableId: str,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DryRun: bool = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None,
    ) -> CreateRouteResultTypeDef:
        """
        [Client.create_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_route_table(self, VpcId: str, DryRun: bool = None) -> CreateRouteTableResultTypeDef:
        """
        [Client.create_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_security_group(
        self, Description: str, GroupName: str, VpcId: str = None, DryRun: bool = None
    ) -> CreateSecurityGroupResultTypeDef:
        """
        [Client.create_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_security_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot(
        self,
        VolumeId: str,
        Description: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
    ) -> SnapshotTypeDef:
        """
        [Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshots(
        self,
        InstanceSpecification: InstanceSpecificationTypeDef,
        Description: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
        CopyTagsFromSource: Literal["volume"] = None,
    ) -> CreateSnapshotsResultTypeDef:
        """
        [Client.create_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_spot_datafeed_subscription(
        self, Bucket: str, DryRun: bool = None, Prefix: str = None
    ) -> CreateSpotDatafeedSubscriptionResultTypeDef:
        """
        [Client.create_spot_datafeed_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_spot_datafeed_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subnet(
        self,
        CidrBlock: str,
        VpcId: str,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Ipv6CidrBlock: str = None,
        OutpostArn: str = None,
        DryRun: bool = None,
    ) -> CreateSubnetResultTypeDef:
        """
        [Client.create_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_subnet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> None:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_traffic_mirror_filter(
        self,
        Description: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> CreateTrafficMirrorFilterResultTypeDef:
        """
        [Client.create_traffic_mirror_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_traffic_mirror_filter_rule(
        self,
        TrafficMirrorFilterId: str,
        TrafficDirection: Literal["ingress", "egress"],
        RuleNumber: int,
        RuleAction: Literal["accept", "reject"],
        DestinationCidrBlock: str,
        SourceCidrBlock: str,
        DestinationPortRange: TrafficMirrorPortRangeRequestTypeDef = None,
        SourcePortRange: TrafficMirrorPortRangeRequestTypeDef = None,
        Protocol: int = None,
        Description: str = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> CreateTrafficMirrorFilterRuleResultTypeDef:
        """
        [Client.create_traffic_mirror_filter_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_traffic_mirror_session(
        self,
        NetworkInterfaceId: str,
        TrafficMirrorTargetId: str,
        TrafficMirrorFilterId: str,
        SessionNumber: int,
        PacketLength: int = None,
        VirtualNetworkId: int = None,
        Description: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> CreateTrafficMirrorSessionResultTypeDef:
        """
        [Client.create_traffic_mirror_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_traffic_mirror_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_traffic_mirror_target(
        self,
        NetworkInterfaceId: str = None,
        NetworkLoadBalancerArn: str = None,
        Description: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> CreateTrafficMirrorTargetResultTypeDef:
        """
        [Client.create_traffic_mirror_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_traffic_mirror_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_transit_gateway(
        self,
        Description: str = None,
        Options: TransitGatewayRequestOptionsTypeDef = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayResultTypeDef:
        """
        [Client.create_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_transit_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_transit_gateway_multicast_domain(
        self,
        TransitGatewayId: str,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayMulticastDomainResultTypeDef:
        """
        [Client.create_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_transit_gateway_multicast_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_transit_gateway_peering_attachment(
        self,
        TransitGatewayId: str,
        PeerTransitGatewayId: str,
        PeerAccountId: str,
        PeerRegion: str,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayPeeringAttachmentResultTypeDef:
        """
        [Client.create_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_transit_gateway_peering_attachment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_transit_gateway_route(
        self,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayRouteResultTypeDef:
        """
        [Client.create_transit_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_transit_gateway_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_transit_gateway_route_table(
        self,
        TransitGatewayId: str,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayRouteTableResultTypeDef:
        """
        [Client.create_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_transit_gateway_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_transit_gateway_vpc_attachment(
        self,
        TransitGatewayId: str,
        VpcId: str,
        SubnetIds: List[str],
        Options: CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayVpcAttachmentResultTypeDef:
        """
        [Client.create_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_transit_gateway_vpc_attachment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_volume(
        self,
        AvailabilityZone: str,
        Encrypted: bool = None,
        Iops: int = None,
        KmsKeyId: str = None,
        OutpostArn: str = None,
        Size: int = None,
        SnapshotId: str = None,
        VolumeType: Literal["standard", "io1", "gp2", "sc1", "st1"] = None,
        DryRun: bool = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
    ) -> VolumeTypeDef:
        """
        [Client.create_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpc(
        self,
        CidrBlock: str,
        AmazonProvidedIpv6CidrBlock: bool = None,
        DryRun: bool = None,
        InstanceTenancy: Literal["default", "dedicated", "host"] = None,
        Ipv6CidrBlockNetworkBorderGroup: str = None,
    ) -> CreateVpcResultTypeDef:
        """
        [Client.create_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpc_endpoint(
        self,
        VpcId: str,
        ServiceName: str,
        DryRun: bool = None,
        VpcEndpointType: Literal["Interface", "Gateway"] = None,
        PolicyDocument: str = None,
        RouteTableIds: List[str] = None,
        SubnetIds: List[str] = None,
        SecurityGroupIds: List[str] = None,
        ClientToken: str = None,
        PrivateDnsEnabled: bool = None,
    ) -> CreateVpcEndpointResultTypeDef:
        """
        [Client.create_vpc_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_vpc_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpc_endpoint_connection_notification(
        self,
        ConnectionNotificationArn: str,
        ConnectionEvents: List[str],
        DryRun: bool = None,
        ServiceId: str = None,
        VpcEndpointId: str = None,
        ClientToken: str = None,
    ) -> CreateVpcEndpointConnectionNotificationResultTypeDef:
        """
        [Client.create_vpc_endpoint_connection_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_connection_notification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpc_endpoint_service_configuration(
        self,
        NetworkLoadBalancerArns: List[str],
        DryRun: bool = None,
        AcceptanceRequired: bool = None,
        ClientToken: str = None,
    ) -> CreateVpcEndpointServiceConfigurationResultTypeDef:
        """
        [Client.create_vpc_endpoint_service_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_service_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpc_peering_connection(
        self,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        VpcId: str = None,
        PeerRegion: str = None,
    ) -> CreateVpcPeeringConnectionResultTypeDef:
        """
        [Client.create_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_vpc_peering_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpn_connection(
        self,
        CustomerGatewayId: str,
        Type: str,
        VpnGatewayId: str = None,
        TransitGatewayId: str = None,
        DryRun: bool = None,
        Options: VpnConnectionOptionsSpecificationTypeDef = None,
    ) -> CreateVpnConnectionResultTypeDef:
        """
        [Client.create_vpn_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_vpn_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpn_connection_route(self, DestinationCidrBlock: str, VpnConnectionId: str) -> None:
        """
        [Client.create_vpn_connection_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_vpn_connection_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_vpn_gateway(
        self,
        Type: Literal["ipsec.1"],
        AvailabilityZone: str = None,
        AmazonSideAsn: int = None,
        DryRun: bool = None,
    ) -> CreateVpnGatewayResultTypeDef:
        """
        [Client.create_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.create_vpn_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_client_vpn_endpoint(
        self, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> DeleteClientVpnEndpointResultTypeDef:
        """
        [Client.delete_client_vpn_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_client_vpn_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_client_vpn_route(
        self,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str = None,
        DryRun: bool = None,
    ) -> DeleteClientVpnRouteResultTypeDef:
        """
        [Client.delete_client_vpn_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_client_vpn_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_customer_gateway(self, CustomerGatewayId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_customer_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dhcp_options(self, DhcpOptionsId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_dhcp_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_egress_only_internet_gateway(
        self, EgressOnlyInternetGatewayId: str, DryRun: bool = None
    ) -> DeleteEgressOnlyInternetGatewayResultTypeDef:
        """
        [Client.delete_egress_only_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_egress_only_internet_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_fleets(
        self, FleetIds: List[str], TerminateInstances: bool, DryRun: bool = None
    ) -> DeleteFleetsResultTypeDef:
        """
        [Client.delete_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_fleets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_flow_logs(
        self, FlowLogIds: List[str], DryRun: bool = None
    ) -> DeleteFlowLogsResultTypeDef:
        """
        [Client.delete_flow_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_flow_logs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_fpga_image(
        self, FpgaImageId: str, DryRun: bool = None
    ) -> DeleteFpgaImageResultTypeDef:
        """
        [Client.delete_fpga_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_fpga_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_internet_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_key_pair(self, KeyName: str, DryRun: bool = None) -> None:
        """
        [Client.delete_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_launch_template(
        self, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None
    ) -> DeleteLaunchTemplateResultTypeDef:
        """
        [Client.delete_launch_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_launch_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_launch_template_versions(
        self,
        Versions: List[str],
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
    ) -> DeleteLaunchTemplateVersionsResultTypeDef:
        """
        [Client.delete_launch_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_launch_template_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_local_gateway_route(
        self, DestinationCidrBlock: str, LocalGatewayRouteTableId: str, DryRun: bool = None
    ) -> DeleteLocalGatewayRouteResultTypeDef:
        """
        [Client.delete_local_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_local_gateway_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_local_gateway_route_table_vpc_association(
        self, LocalGatewayRouteTableVpcAssociationId: str, DryRun: bool = None
    ) -> DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef:
        """
        [Client.delete_local_gateway_route_table_vpc_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_local_gateway_route_table_vpc_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_nat_gateway(self, NatGatewayId: str) -> DeleteNatGatewayResultTypeDef:
        """
        [Client.delete_nat_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_nat_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_network_acl(self, NetworkAclId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_network_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_network_acl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_network_acl_entry(
        self, Egress: bool, NetworkAclId: str, RuleNumber: int, DryRun: bool = None
    ) -> None:
        """
        [Client.delete_network_acl_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_network_acl_entry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_network_interface(self, NetworkInterfaceId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_network_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_network_interface_permission(
        self, NetworkInterfacePermissionId: str, Force: bool = None, DryRun: bool = None
    ) -> DeleteNetworkInterfacePermissionResultTypeDef:
        """
        [Client.delete_network_interface_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_network_interface_permission)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_placement_group(self, GroupName: str, DryRun: bool = None) -> None:
        """
        [Client.delete_placement_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_placement_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_queued_reserved_instances(
        self, ReservedInstancesIds: List[str], DryRun: bool = None
    ) -> DeleteQueuedReservedInstancesResultTypeDef:
        """
        [Client.delete_queued_reserved_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_queued_reserved_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_route(
        self,
        RouteTableId: str,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.delete_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_route_table(self, RouteTableId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_security_group(
        self, GroupId: str = None, GroupName: str = None, DryRun: bool = None
    ) -> None:
        """
        [Client.delete_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_security_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_snapshot(self, SnapshotId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_spot_datafeed_subscription(self, DryRun: bool = None) -> None:
        """
        [Client.delete_spot_datafeed_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_spot_datafeed_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_subnet(self, SubnetId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_subnet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tags(
        self, Resources: List[Any], DryRun: bool = None, Tags: List[TagTypeDef] = None
    ) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_traffic_mirror_filter(
        self, TrafficMirrorFilterId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorFilterResultTypeDef:
        """
        [Client.delete_traffic_mirror_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_traffic_mirror_filter_rule(
        self, TrafficMirrorFilterRuleId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorFilterRuleResultTypeDef:
        """
        [Client.delete_traffic_mirror_filter_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_traffic_mirror_session(
        self, TrafficMirrorSessionId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorSessionResultTypeDef:
        """
        [Client.delete_traffic_mirror_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_traffic_mirror_target(
        self, TrafficMirrorTargetId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorTargetResultTypeDef:
        """
        [Client.delete_traffic_mirror_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_target)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_transit_gateway(
        self, TransitGatewayId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayResultTypeDef:
        """
        [Client.delete_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_transit_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_transit_gateway_multicast_domain(
        self, TransitGatewayMulticastDomainId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayMulticastDomainResultTypeDef:
        """
        [Client.delete_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_transit_gateway_multicast_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_transit_gateway_peering_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayPeeringAttachmentResultTypeDef:
        """
        [Client.delete_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_transit_gateway_peering_attachment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_transit_gateway_route(
        self, TransitGatewayRouteTableId: str, DestinationCidrBlock: str, DryRun: bool = None
    ) -> DeleteTransitGatewayRouteResultTypeDef:
        """
        [Client.delete_transit_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_transit_gateway_route_table(
        self, TransitGatewayRouteTableId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayRouteTableResultTypeDef:
        """
        [Client.delete_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_transit_gateway_vpc_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayVpcAttachmentResultTypeDef:
        """
        [Client.delete_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_transit_gateway_vpc_attachment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_volume(self, VolumeId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vpc_endpoint_connection_notifications(
        self, ConnectionNotificationIds: List[str], DryRun: bool = None
    ) -> DeleteVpcEndpointConnectionNotificationsResultTypeDef:
        """
        [Client.delete_vpc_endpoint_connection_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_connection_notifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vpc_endpoint_service_configurations(
        self, ServiceIds: List[str], DryRun: bool = None
    ) -> DeleteVpcEndpointServiceConfigurationsResultTypeDef:
        """
        [Client.delete_vpc_endpoint_service_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_service_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vpc_endpoints(
        self, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> DeleteVpcEndpointsResultTypeDef:
        """
        [Client.delete_vpc_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_vpc_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vpc_peering_connection(
        self, VpcPeeringConnectionId: str, DryRun: bool = None
    ) -> DeleteVpcPeeringConnectionResultTypeDef:
        """
        [Client.delete_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_vpc_peering_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vpn_connection(self, VpnConnectionId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_vpn_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_vpn_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vpn_connection_route(self, DestinationCidrBlock: str, VpnConnectionId: str) -> None:
        """
        [Client.delete_vpn_connection_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_vpn_connection_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vpn_gateway(self, VpnGatewayId: str, DryRun: bool = None) -> None:
        """
        [Client.delete_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.delete_vpn_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deprovision_byoip_cidr(
        self, Cidr: str, DryRun: bool = None
    ) -> DeprovisionByoipCidrResultTypeDef:
        """
        [Client.deprovision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.deprovision_byoip_cidr)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_image(self, ImageId: str, DryRun: bool = None) -> None:
        """
        [Client.deregister_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.deregister_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_transit_gateway_multicast_group_members(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> DeregisterTransitGatewayMulticastGroupMembersResultTypeDef:
        """
        [Client.deregister_transit_gateway_multicast_group_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_transit_gateway_multicast_group_sources(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef:
        """
        [Client.deregister_transit_gateway_multicast_group_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_sources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_attributes(
        self,
        AttributeNames: List[Literal["supported-platforms", "default-vpc"]] = None,
        DryRun: bool = None,
    ) -> DescribeAccountAttributesResultTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_account_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_addresses(
        self,
        Filters: List[FilterTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeAddressesResultTypeDef:
        """
        [Client.describe_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_addresses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_aggregate_id_format(
        self, DryRun: bool = None
    ) -> DescribeAggregateIdFormatResultTypeDef:
        """
        [Client.describe_aggregate_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_aggregate_id_format)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_availability_zones(
        self,
        Filters: List[FilterTypeDef] = None,
        ZoneNames: List[str] = None,
        ZoneIds: List[str] = None,
        AllAvailabilityZones: bool = None,
        DryRun: bool = None,
    ) -> DescribeAvailabilityZonesResultTypeDef:
        """
        [Client.describe_availability_zones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_availability_zones)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_bundle_tasks(
        self, BundleIds: List[str] = None, Filters: List[FilterTypeDef] = None, DryRun: bool = None
    ) -> DescribeBundleTasksResultTypeDef:
        """
        [Client.describe_bundle_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_bundle_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_byoip_cidrs(
        self, MaxResults: int, DryRun: bool = None, NextToken: str = None
    ) -> DescribeByoipCidrsResultTypeDef:
        """
        [Client.describe_byoip_cidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_byoip_cidrs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_capacity_reservations(
        self,
        CapacityReservationIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
    ) -> DescribeCapacityReservationsResultTypeDef:
        """
        [Client.describe_capacity_reservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_capacity_reservations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_classic_link_instances(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeClassicLinkInstancesResultTypeDef:
        """
        [Client.describe_classic_link_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_classic_link_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_client_vpn_authorization_rules(
        self,
        ClientVpnEndpointId: str,
        DryRun: bool = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
    ) -> DescribeClientVpnAuthorizationRulesResultTypeDef:
        """
        [Client.describe_client_vpn_authorization_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_client_vpn_authorization_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_client_vpn_connections(
        self,
        ClientVpnEndpointId: str,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None,
    ) -> DescribeClientVpnConnectionsResultTypeDef:
        """
        [Client.describe_client_vpn_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_client_vpn_connections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_client_vpn_endpoints(
        self,
        ClientVpnEndpointIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
    ) -> DescribeClientVpnEndpointsResultTypeDef:
        """
        [Client.describe_client_vpn_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_client_vpn_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_client_vpn_routes(
        self,
        ClientVpnEndpointId: str,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeClientVpnRoutesResultTypeDef:
        """
        [Client.describe_client_vpn_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_client_vpn_routes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_client_vpn_target_networks(
        self,
        ClientVpnEndpointId: str,
        AssociationIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
    ) -> DescribeClientVpnTargetNetworksResultTypeDef:
        """
        [Client.describe_client_vpn_target_networks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_client_vpn_target_networks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_coip_pools(
        self,
        PoolIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeCoipPoolsResultTypeDef:
        """
        [Client.describe_coip_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_coip_pools)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_conversion_tasks(
        self, ConversionTaskIds: List[str] = None, DryRun: bool = None
    ) -> DescribeConversionTasksResultTypeDef:
        """
        [Client.describe_conversion_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_conversion_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_customer_gateways(
        self,
        CustomerGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
    ) -> DescribeCustomerGatewaysResultTypeDef:
        """
        [Client.describe_customer_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_customer_gateways)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dhcp_options(
        self,
        DhcpOptionsIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeDhcpOptionsResultTypeDef:
        """
        [Client.describe_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_dhcp_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_egress_only_internet_gateways(
        self,
        DryRun: bool = None,
        EgressOnlyInternetGatewayIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeEgressOnlyInternetGatewaysResultTypeDef:
        """
        [Client.describe_egress_only_internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_egress_only_internet_gateways)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_elastic_gpus(
        self,
        ElasticGpuIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeElasticGpusResultTypeDef:
        """
        [Client.describe_elastic_gpus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_elastic_gpus)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_export_image_tasks(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ExportImageTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeExportImageTasksResultTypeDef:
        """
        [Client.describe_export_image_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_export_image_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_export_tasks(
        self, ExportTaskIds: List[str] = None
    ) -> DescribeExportTasksResultTypeDef:
        """
        [Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_export_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fast_snapshot_restores(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeFastSnapshotRestoresResultTypeDef:
        """
        [Client.describe_fast_snapshot_restores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_fast_snapshot_restores)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleet_history(
        self,
        FleetId: str,
        StartTime: datetime,
        DryRun: bool = None,
        EventType: Literal["instance-change", "fleet-change", "service-error"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeFleetHistoryResultTypeDef:
        """
        [Client.describe_fleet_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_fleet_history)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleet_instances(
        self,
        FleetId: str,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> DescribeFleetInstancesResultTypeDef:
        """
        [Client.describe_fleet_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_fleet_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleets(
        self,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        FleetIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
    ) -> DescribeFleetsResultTypeDef:
        """
        [Client.describe_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_fleets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_flow_logs(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        FlowLogIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeFlowLogsResultTypeDef:
        """
        [Client.describe_flow_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_flow_logs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fpga_image_attribute(
        self,
        FpgaImageId: str,
        Attribute: Literal["description", "name", "loadPermission", "productCodes"],
        DryRun: bool = None,
    ) -> DescribeFpgaImageAttributeResultTypeDef:
        """
        [Client.describe_fpga_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_fpga_image_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fpga_images(
        self,
        DryRun: bool = None,
        FpgaImageIds: List[str] = None,
        Owners: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeFpgaImagesResultTypeDef:
        """
        [Client.describe_fpga_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_fpga_images)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_host_reservation_offerings(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxDuration: int = None,
        MaxResults: int = None,
        MinDuration: int = None,
        NextToken: str = None,
        OfferingId: str = None,
    ) -> DescribeHostReservationOfferingsResultTypeDef:
        """
        [Client.describe_host_reservation_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_host_reservation_offerings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_host_reservations(
        self,
        Filters: List[FilterTypeDef] = None,
        HostReservationIdSet: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeHostReservationsResultTypeDef:
        """
        [Client.describe_host_reservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_host_reservations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_hosts(
        self,
        Filters: List[FilterTypeDef] = None,
        HostIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeHostsResultTypeDef:
        """
        [Client.describe_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_hosts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_iam_instance_profile_associations(
        self,
        AssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeIamInstanceProfileAssociationsResultTypeDef:
        """
        [Client.describe_iam_instance_profile_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_iam_instance_profile_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_id_format(self, Resource: str = None) -> DescribeIdFormatResultTypeDef:
        """
        [Client.describe_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_id_format)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_identity_id_format(
        self, PrincipalArn: str, Resource: str = None
    ) -> DescribeIdentityIdFormatResultTypeDef:
        """
        [Client.describe_identity_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_identity_id_format)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_image_attribute(
        self,
        Attribute: Literal[
            "description",
            "kernel",
            "ramdisk",
            "launchPermission",
            "productCodes",
            "blockDeviceMapping",
            "sriovNetSupport",
        ],
        ImageId: str,
        DryRun: bool = None,
    ) -> ImageAttributeTypeDef:
        """
        [Client.describe_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_image_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_images(
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeImagesResultTypeDef:
        """
        [Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_images)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_import_image_tasks(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ImportTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeImportImageTasksResultTypeDef:
        """
        [Client.describe_import_image_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_import_image_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_import_snapshot_tasks(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ImportTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeImportSnapshotTasksResultTypeDef:
        """
        [Client.describe_import_snapshot_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_import_snapshot_tasks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instance_attribute(
        self,
        Attribute: Literal[
            "instanceType",
            "kernel",
            "ramdisk",
            "userData",
            "disableApiTermination",
            "instanceInitiatedShutdownBehavior",
            "rootDeviceName",
            "blockDeviceMapping",
            "productCodes",
            "sourceDestCheck",
            "groupSet",
            "ebsOptimized",
            "sriovNetSupport",
            "enaSupport",
        ],
        InstanceId: str,
        DryRun: bool = None,
    ) -> InstanceAttributeTypeDef:
        """
        [Client.describe_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_instance_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instance_credit_specifications(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeInstanceCreditSpecificationsResultTypeDef:
        """
        [Client.describe_instance_credit_specifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_instance_credit_specifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instance_status(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
    ) -> DescribeInstanceStatusResultTypeDef:
        """
        [Client.describe_instance_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_instance_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instance_type_offerings(
        self,
        DryRun: bool = None,
        LocationType: Literal["region", "availability-zone", "availability-zone-id"] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeInstanceTypeOfferingsResultTypeDef:
        """
        [Client.describe_instance_type_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_instance_type_offerings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instance_types(
        self,
        DryRun: bool = None,
        InstanceTypes: List[
            Literal[
                "t1.micro",
                "t2.nano",
                "t2.micro",
                "t2.small",
                "t2.medium",
                "t2.large",
                "t2.xlarge",
                "t2.2xlarge",
                "t3.nano",
                "t3.micro",
                "t3.small",
                "t3.medium",
                "t3.large",
                "t3.xlarge",
                "t3.2xlarge",
                "t3a.nano",
                "t3a.micro",
                "t3a.small",
                "t3a.medium",
                "t3a.large",
                "t3a.xlarge",
                "t3a.2xlarge",
                "m1.small",
                "m1.medium",
                "m1.large",
                "m1.xlarge",
                "m3.medium",
                "m3.large",
                "m3.xlarge",
                "m3.2xlarge",
                "m4.large",
                "m4.xlarge",
                "m4.2xlarge",
                "m4.4xlarge",
                "m4.10xlarge",
                "m4.16xlarge",
                "m2.xlarge",
                "m2.2xlarge",
                "m2.4xlarge",
                "cr1.8xlarge",
                "r3.large",
                "r3.xlarge",
                "r3.2xlarge",
                "r3.4xlarge",
                "r3.8xlarge",
                "r4.large",
                "r4.xlarge",
                "r4.2xlarge",
                "r4.4xlarge",
                "r4.8xlarge",
                "r4.16xlarge",
                "r5.large",
                "r5.xlarge",
                "r5.2xlarge",
                "r5.4xlarge",
                "r5.8xlarge",
                "r5.12xlarge",
                "r5.16xlarge",
                "r5.24xlarge",
                "r5.metal",
                "r5a.large",
                "r5a.xlarge",
                "r5a.2xlarge",
                "r5a.4xlarge",
                "r5a.8xlarge",
                "r5a.12xlarge",
                "r5a.16xlarge",
                "r5a.24xlarge",
                "r5d.large",
                "r5d.xlarge",
                "r5d.2xlarge",
                "r5d.4xlarge",
                "r5d.8xlarge",
                "r5d.12xlarge",
                "r5d.16xlarge",
                "r5d.24xlarge",
                "r5d.metal",
                "r5ad.large",
                "r5ad.xlarge",
                "r5ad.2xlarge",
                "r5ad.4xlarge",
                "r5ad.8xlarge",
                "r5ad.12xlarge",
                "r5ad.16xlarge",
                "r5ad.24xlarge",
                "x1.16xlarge",
                "x1.32xlarge",
                "x1e.xlarge",
                "x1e.2xlarge",
                "x1e.4xlarge",
                "x1e.8xlarge",
                "x1e.16xlarge",
                "x1e.32xlarge",
                "i2.xlarge",
                "i2.2xlarge",
                "i2.4xlarge",
                "i2.8xlarge",
                "i3.large",
                "i3.xlarge",
                "i3.2xlarge",
                "i3.4xlarge",
                "i3.8xlarge",
                "i3.16xlarge",
                "i3.metal",
                "i3en.large",
                "i3en.xlarge",
                "i3en.2xlarge",
                "i3en.3xlarge",
                "i3en.6xlarge",
                "i3en.12xlarge",
                "i3en.24xlarge",
                "i3en.metal",
                "hi1.4xlarge",
                "hs1.8xlarge",
                "c1.medium",
                "c1.xlarge",
                "c3.large",
                "c3.xlarge",
                "c3.2xlarge",
                "c3.4xlarge",
                "c3.8xlarge",
                "c4.large",
                "c4.xlarge",
                "c4.2xlarge",
                "c4.4xlarge",
                "c4.8xlarge",
                "c5.large",
                "c5.xlarge",
                "c5.2xlarge",
                "c5.4xlarge",
                "c5.9xlarge",
                "c5.12xlarge",
                "c5.18xlarge",
                "c5.24xlarge",
                "c5.metal",
                "c5d.large",
                "c5d.xlarge",
                "c5d.2xlarge",
                "c5d.4xlarge",
                "c5d.9xlarge",
                "c5d.12xlarge",
                "c5d.18xlarge",
                "c5d.24xlarge",
                "c5d.metal",
                "c5n.large",
                "c5n.xlarge",
                "c5n.2xlarge",
                "c5n.4xlarge",
                "c5n.9xlarge",
                "c5n.18xlarge",
                "cc1.4xlarge",
                "cc2.8xlarge",
                "g2.2xlarge",
                "g2.8xlarge",
                "g3.4xlarge",
                "g3.8xlarge",
                "g3.16xlarge",
                "g3s.xlarge",
                "g4dn.xlarge",
                "g4dn.2xlarge",
                "g4dn.4xlarge",
                "g4dn.8xlarge",
                "g4dn.12xlarge",
                "g4dn.16xlarge",
                "cg1.4xlarge",
                "p2.xlarge",
                "p2.8xlarge",
                "p2.16xlarge",
                "p3.2xlarge",
                "p3.8xlarge",
                "p3.16xlarge",
                "p3dn.24xlarge",
                "d2.xlarge",
                "d2.2xlarge",
                "d2.4xlarge",
                "d2.8xlarge",
                "f1.2xlarge",
                "f1.4xlarge",
                "f1.16xlarge",
                "m5.large",
                "m5.xlarge",
                "m5.2xlarge",
                "m5.4xlarge",
                "m5.8xlarge",
                "m5.12xlarge",
                "m5.16xlarge",
                "m5.24xlarge",
                "m5.metal",
                "m5a.large",
                "m5a.xlarge",
                "m5a.2xlarge",
                "m5a.4xlarge",
                "m5a.8xlarge",
                "m5a.12xlarge",
                "m5a.16xlarge",
                "m5a.24xlarge",
                "m5d.large",
                "m5d.xlarge",
                "m5d.2xlarge",
                "m5d.4xlarge",
                "m5d.8xlarge",
                "m5d.12xlarge",
                "m5d.16xlarge",
                "m5d.24xlarge",
                "m5d.metal",
                "m5ad.large",
                "m5ad.xlarge",
                "m5ad.2xlarge",
                "m5ad.4xlarge",
                "m5ad.8xlarge",
                "m5ad.12xlarge",
                "m5ad.16xlarge",
                "m5ad.24xlarge",
                "h1.2xlarge",
                "h1.4xlarge",
                "h1.8xlarge",
                "h1.16xlarge",
                "z1d.large",
                "z1d.xlarge",
                "z1d.2xlarge",
                "z1d.3xlarge",
                "z1d.6xlarge",
                "z1d.12xlarge",
                "z1d.metal",
                "u-6tb1.metal",
                "u-9tb1.metal",
                "u-12tb1.metal",
                "u-18tb1.metal",
                "u-24tb1.metal",
                "a1.medium",
                "a1.large",
                "a1.xlarge",
                "a1.2xlarge",
                "a1.4xlarge",
                "a1.metal",
                "m5dn.large",
                "m5dn.xlarge",
                "m5dn.2xlarge",
                "m5dn.4xlarge",
                "m5dn.8xlarge",
                "m5dn.12xlarge",
                "m5dn.16xlarge",
                "m5dn.24xlarge",
                "m5n.large",
                "m5n.xlarge",
                "m5n.2xlarge",
                "m5n.4xlarge",
                "m5n.8xlarge",
                "m5n.12xlarge",
                "m5n.16xlarge",
                "m5n.24xlarge",
                "r5dn.large",
                "r5dn.xlarge",
                "r5dn.2xlarge",
                "r5dn.4xlarge",
                "r5dn.8xlarge",
                "r5dn.12xlarge",
                "r5dn.16xlarge",
                "r5dn.24xlarge",
                "r5n.large",
                "r5n.xlarge",
                "r5n.2xlarge",
                "r5n.4xlarge",
                "r5n.8xlarge",
                "r5n.12xlarge",
                "r5n.16xlarge",
                "r5n.24xlarge",
                "inf1.xlarge",
                "inf1.2xlarge",
                "inf1.6xlarge",
                "inf1.24xlarge",
            ]
        ] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeInstanceTypesResultTypeDef:
        """
        [Client.describe_instance_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_instance_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_instances(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeInstancesResultTypeDef:
        """
        [Client.describe_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_internet_gateways(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeInternetGatewaysResultTypeDef:
        """
        [Client.describe_internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_internet_gateways)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_key_pairs(
        self, Filters: List[FilterTypeDef] = None, KeyNames: List[str] = None, DryRun: bool = None
    ) -> DescribeKeyPairsResultTypeDef:
        """
        [Client.describe_key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_key_pairs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_launch_template_versions(
        self,
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        Versions: List[str] = None,
        MinVersion: str = None,
        MaxVersion: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[FilterTypeDef] = None,
    ) -> DescribeLaunchTemplateVersionsResultTypeDef:
        """
        [Client.describe_launch_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_launch_template_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_launch_templates(
        self,
        DryRun: bool = None,
        LaunchTemplateIds: List[str] = None,
        LaunchTemplateNames: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeLaunchTemplatesResultTypeDef:
        """
        [Client.describe_launch_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_launch_templates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_local_gateway_route_table_virtual_interface_group_associations(
        self,
        LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef:
        """
        [Client.describe_local_gateway_route_table_virtual_interface_group_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_virtual_interface_group_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_local_gateway_route_table_vpc_associations(
        self,
        LocalGatewayRouteTableVpcAssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef:
        """
        [Client.describe_local_gateway_route_table_vpc_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_vpc_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_local_gateway_route_tables(
        self,
        LocalGatewayRouteTableIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewayRouteTablesResultTypeDef:
        """
        [Client.describe_local_gateway_route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_tables)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_local_gateway_virtual_interface_groups(
        self,
        LocalGatewayVirtualInterfaceGroupIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef:
        """
        [Client.describe_local_gateway_virtual_interface_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interface_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_local_gateway_virtual_interfaces(
        self,
        LocalGatewayVirtualInterfaceIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewayVirtualInterfacesResultTypeDef:
        """
        [Client.describe_local_gateway_virtual_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interfaces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_local_gateways(
        self,
        LocalGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewaysResultTypeDef:
        """
        [Client.describe_local_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_local_gateways)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_moving_addresses(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        PublicIps: List[str] = None,
    ) -> DescribeMovingAddressesResultTypeDef:
        """
        [Client.describe_moving_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_moving_addresses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_nat_gateways(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NatGatewayIds: List[str] = None,
        NextToken: str = None,
    ) -> DescribeNatGatewaysResultTypeDef:
        """
        [Client.describe_nat_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_nat_gateways)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_network_acls(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeNetworkAclsResultTypeDef:
        """
        [Client.describe_network_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_network_acls)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_network_interface_attribute(
        self,
        NetworkInterfaceId: str,
        Attribute: Literal["description", "groupSet", "sourceDestCheck", "attachment"] = None,
        DryRun: bool = None,
    ) -> DescribeNetworkInterfaceAttributeResultTypeDef:
        """
        [Client.describe_network_interface_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_network_interface_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_network_interface_permissions(
        self,
        NetworkInterfacePermissionIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeNetworkInterfacePermissionsResultTypeDef:
        """
        [Client.describe_network_interface_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_network_interface_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_network_interfaces(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeNetworkInterfacesResultTypeDef:
        """
        [Client.describe_network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_network_interfaces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_placement_groups(
        self, Filters: List[FilterTypeDef] = None, DryRun: bool = None, GroupNames: List[str] = None
    ) -> DescribePlacementGroupsResultTypeDef:
        """
        [Client.describe_placement_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_placement_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_prefix_lists(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        PrefixListIds: List[str] = None,
    ) -> DescribePrefixListsResultTypeDef:
        """
        [Client.describe_prefix_lists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_prefix_lists)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_principal_id_format(
        self,
        DryRun: bool = None,
        Resources: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribePrincipalIdFormatResultTypeDef:
        """
        [Client.describe_principal_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_principal_id_format)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_public_ipv4_pools(
        self, PoolIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribePublicIpv4PoolsResultTypeDef:
        """
        [Client.describe_public_ipv4_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_public_ipv4_pools)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_regions(
        self,
        Filters: List[FilterTypeDef] = None,
        RegionNames: List[str] = None,
        DryRun: bool = None,
        AllRegions: bool = None,
    ) -> DescribeRegionsResultTypeDef:
        """
        [Client.describe_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_regions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_instances(
        self,
        Filters: List[FilterTypeDef] = None,
        OfferingClass: Literal["standard", "convertible"] = None,
        ReservedInstancesIds: List[str] = None,
        DryRun: bool = None,
        OfferingType: Literal[
            "Heavy Utilization",
            "Medium Utilization",
            "Light Utilization",
            "No Upfront",
            "Partial Upfront",
            "All Upfront",
        ] = None,
    ) -> DescribeReservedInstancesResultTypeDef:
        """
        [Client.describe_reserved_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_reserved_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_instances_listings(
        self,
        Filters: List[FilterTypeDef] = None,
        ReservedInstancesId: str = None,
        ReservedInstancesListingId: str = None,
    ) -> DescribeReservedInstancesListingsResultTypeDef:
        """
        [Client.describe_reserved_instances_listings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_reserved_instances_listings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_instances_modifications(
        self,
        Filters: List[FilterTypeDef] = None,
        ReservedInstancesModificationIds: List[str] = None,
        NextToken: str = None,
    ) -> DescribeReservedInstancesModificationsResultTypeDef:
        """
        [Client.describe_reserved_instances_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_reserved_instances_modifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_instances_offerings(
        self,
        AvailabilityZone: str = None,
        Filters: List[FilterTypeDef] = None,
        IncludeMarketplace: bool = None,
        InstanceType: Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
        ] = None,
        MaxDuration: int = None,
        MaxInstanceCount: int = None,
        MinDuration: int = None,
        OfferingClass: Literal["standard", "convertible"] = None,
        ProductDescription: Literal[
            "Linux/UNIX", "Linux/UNIX (Amazon VPC)", "Windows", "Windows (Amazon VPC)"
        ] = None,
        ReservedInstancesOfferingIds: List[str] = None,
        DryRun: bool = None,
        InstanceTenancy: Literal["default", "dedicated", "host"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OfferingType: Literal[
            "Heavy Utilization",
            "Medium Utilization",
            "Light Utilization",
            "No Upfront",
            "Partial Upfront",
            "All Upfront",
        ] = None,
    ) -> DescribeReservedInstancesOfferingsResultTypeDef:
        """
        [Client.describe_reserved_instances_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_reserved_instances_offerings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_route_tables(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeRouteTablesResultTypeDef:
        """
        [Client.describe_route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_route_tables)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scheduled_instance_availability(
        self,
        FirstSlotStartTimeRange: SlotDateTimeRangeRequestTypeDef,
        Recurrence: ScheduledInstanceRecurrenceRequestTypeDef,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        MaxSlotDurationInHours: int = None,
        MinSlotDurationInHours: int = None,
        NextToken: str = None,
    ) -> DescribeScheduledInstanceAvailabilityResultTypeDef:
        """
        [Client.describe_scheduled_instance_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_scheduled_instance_availability)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scheduled_instances(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ScheduledInstanceIds: List[str] = None,
        SlotStartTimeRange: SlotStartTimeRangeRequestTypeDef = None,
    ) -> DescribeScheduledInstancesResultTypeDef:
        """
        [Client.describe_scheduled_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_scheduled_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_security_group_references(
        self, GroupId: List[str], DryRun: bool = None
    ) -> DescribeSecurityGroupReferencesResultTypeDef:
        """
        [Client.describe_security_group_references documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_security_group_references)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_security_groups(
        self,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeSecurityGroupsResultTypeDef:
        """
        [Client.describe_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_security_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_snapshot_attribute(
        self,
        Attribute: Literal["productCodes", "createVolumePermission"],
        SnapshotId: str,
        DryRun: bool = None,
    ) -> DescribeSnapshotAttributeResultTypeDef:
        """
        [Client.describe_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_snapshot_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_snapshots(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeSnapshotsResultTypeDef:
        """
        [Client.describe_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_spot_datafeed_subscription(
        self, DryRun: bool = None
    ) -> DescribeSpotDatafeedSubscriptionResultTypeDef:
        """
        [Client.describe_spot_datafeed_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_spot_datafeed_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_spot_fleet_instances(
        self,
        SpotFleetRequestId: str,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeSpotFleetInstancesResponseTypeDef:
        """
        [Client.describe_spot_fleet_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_spot_fleet_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_spot_fleet_request_history(
        self,
        SpotFleetRequestId: str,
        StartTime: datetime,
        DryRun: bool = None,
        EventType: Literal["instanceChange", "fleetRequestChange", "error", "information"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeSpotFleetRequestHistoryResponseTypeDef:
        """
        [Client.describe_spot_fleet_request_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_spot_fleet_request_history)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_spot_fleet_requests(
        self,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        SpotFleetRequestIds: List[str] = None,
    ) -> DescribeSpotFleetRequestsResponseTypeDef:
        """
        [Client.describe_spot_fleet_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_spot_fleet_requests)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_spot_instance_requests(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeSpotInstanceRequestsResultTypeDef:
        """
        [Client.describe_spot_instance_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_spot_instance_requests)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_spot_price_history(
        self,
        Filters: List[FilterTypeDef] = None,
        AvailabilityZone: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        InstanceTypes: List[
            Literal[
                "t1.micro",
                "t2.nano",
                "t2.micro",
                "t2.small",
                "t2.medium",
                "t2.large",
                "t2.xlarge",
                "t2.2xlarge",
                "t3.nano",
                "t3.micro",
                "t3.small",
                "t3.medium",
                "t3.large",
                "t3.xlarge",
                "t3.2xlarge",
                "t3a.nano",
                "t3a.micro",
                "t3a.small",
                "t3a.medium",
                "t3a.large",
                "t3a.xlarge",
                "t3a.2xlarge",
                "m1.small",
                "m1.medium",
                "m1.large",
                "m1.xlarge",
                "m3.medium",
                "m3.large",
                "m3.xlarge",
                "m3.2xlarge",
                "m4.large",
                "m4.xlarge",
                "m4.2xlarge",
                "m4.4xlarge",
                "m4.10xlarge",
                "m4.16xlarge",
                "m2.xlarge",
                "m2.2xlarge",
                "m2.4xlarge",
                "cr1.8xlarge",
                "r3.large",
                "r3.xlarge",
                "r3.2xlarge",
                "r3.4xlarge",
                "r3.8xlarge",
                "r4.large",
                "r4.xlarge",
                "r4.2xlarge",
                "r4.4xlarge",
                "r4.8xlarge",
                "r4.16xlarge",
                "r5.large",
                "r5.xlarge",
                "r5.2xlarge",
                "r5.4xlarge",
                "r5.8xlarge",
                "r5.12xlarge",
                "r5.16xlarge",
                "r5.24xlarge",
                "r5.metal",
                "r5a.large",
                "r5a.xlarge",
                "r5a.2xlarge",
                "r5a.4xlarge",
                "r5a.8xlarge",
                "r5a.12xlarge",
                "r5a.16xlarge",
                "r5a.24xlarge",
                "r5d.large",
                "r5d.xlarge",
                "r5d.2xlarge",
                "r5d.4xlarge",
                "r5d.8xlarge",
                "r5d.12xlarge",
                "r5d.16xlarge",
                "r5d.24xlarge",
                "r5d.metal",
                "r5ad.large",
                "r5ad.xlarge",
                "r5ad.2xlarge",
                "r5ad.4xlarge",
                "r5ad.8xlarge",
                "r5ad.12xlarge",
                "r5ad.16xlarge",
                "r5ad.24xlarge",
                "x1.16xlarge",
                "x1.32xlarge",
                "x1e.xlarge",
                "x1e.2xlarge",
                "x1e.4xlarge",
                "x1e.8xlarge",
                "x1e.16xlarge",
                "x1e.32xlarge",
                "i2.xlarge",
                "i2.2xlarge",
                "i2.4xlarge",
                "i2.8xlarge",
                "i3.large",
                "i3.xlarge",
                "i3.2xlarge",
                "i3.4xlarge",
                "i3.8xlarge",
                "i3.16xlarge",
                "i3.metal",
                "i3en.large",
                "i3en.xlarge",
                "i3en.2xlarge",
                "i3en.3xlarge",
                "i3en.6xlarge",
                "i3en.12xlarge",
                "i3en.24xlarge",
                "i3en.metal",
                "hi1.4xlarge",
                "hs1.8xlarge",
                "c1.medium",
                "c1.xlarge",
                "c3.large",
                "c3.xlarge",
                "c3.2xlarge",
                "c3.4xlarge",
                "c3.8xlarge",
                "c4.large",
                "c4.xlarge",
                "c4.2xlarge",
                "c4.4xlarge",
                "c4.8xlarge",
                "c5.large",
                "c5.xlarge",
                "c5.2xlarge",
                "c5.4xlarge",
                "c5.9xlarge",
                "c5.12xlarge",
                "c5.18xlarge",
                "c5.24xlarge",
                "c5.metal",
                "c5d.large",
                "c5d.xlarge",
                "c5d.2xlarge",
                "c5d.4xlarge",
                "c5d.9xlarge",
                "c5d.12xlarge",
                "c5d.18xlarge",
                "c5d.24xlarge",
                "c5d.metal",
                "c5n.large",
                "c5n.xlarge",
                "c5n.2xlarge",
                "c5n.4xlarge",
                "c5n.9xlarge",
                "c5n.18xlarge",
                "cc1.4xlarge",
                "cc2.8xlarge",
                "g2.2xlarge",
                "g2.8xlarge",
                "g3.4xlarge",
                "g3.8xlarge",
                "g3.16xlarge",
                "g3s.xlarge",
                "g4dn.xlarge",
                "g4dn.2xlarge",
                "g4dn.4xlarge",
                "g4dn.8xlarge",
                "g4dn.12xlarge",
                "g4dn.16xlarge",
                "cg1.4xlarge",
                "p2.xlarge",
                "p2.8xlarge",
                "p2.16xlarge",
                "p3.2xlarge",
                "p3.8xlarge",
                "p3.16xlarge",
                "p3dn.24xlarge",
                "d2.xlarge",
                "d2.2xlarge",
                "d2.4xlarge",
                "d2.8xlarge",
                "f1.2xlarge",
                "f1.4xlarge",
                "f1.16xlarge",
                "m5.large",
                "m5.xlarge",
                "m5.2xlarge",
                "m5.4xlarge",
                "m5.8xlarge",
                "m5.12xlarge",
                "m5.16xlarge",
                "m5.24xlarge",
                "m5.metal",
                "m5a.large",
                "m5a.xlarge",
                "m5a.2xlarge",
                "m5a.4xlarge",
                "m5a.8xlarge",
                "m5a.12xlarge",
                "m5a.16xlarge",
                "m5a.24xlarge",
                "m5d.large",
                "m5d.xlarge",
                "m5d.2xlarge",
                "m5d.4xlarge",
                "m5d.8xlarge",
                "m5d.12xlarge",
                "m5d.16xlarge",
                "m5d.24xlarge",
                "m5d.metal",
                "m5ad.large",
                "m5ad.xlarge",
                "m5ad.2xlarge",
                "m5ad.4xlarge",
                "m5ad.8xlarge",
                "m5ad.12xlarge",
                "m5ad.16xlarge",
                "m5ad.24xlarge",
                "h1.2xlarge",
                "h1.4xlarge",
                "h1.8xlarge",
                "h1.16xlarge",
                "z1d.large",
                "z1d.xlarge",
                "z1d.2xlarge",
                "z1d.3xlarge",
                "z1d.6xlarge",
                "z1d.12xlarge",
                "z1d.metal",
                "u-6tb1.metal",
                "u-9tb1.metal",
                "u-12tb1.metal",
                "u-18tb1.metal",
                "u-24tb1.metal",
                "a1.medium",
                "a1.large",
                "a1.xlarge",
                "a1.2xlarge",
                "a1.4xlarge",
                "a1.metal",
                "m5dn.large",
                "m5dn.xlarge",
                "m5dn.2xlarge",
                "m5dn.4xlarge",
                "m5dn.8xlarge",
                "m5dn.12xlarge",
                "m5dn.16xlarge",
                "m5dn.24xlarge",
                "m5n.large",
                "m5n.xlarge",
                "m5n.2xlarge",
                "m5n.4xlarge",
                "m5n.8xlarge",
                "m5n.12xlarge",
                "m5n.16xlarge",
                "m5n.24xlarge",
                "r5dn.large",
                "r5dn.xlarge",
                "r5dn.2xlarge",
                "r5dn.4xlarge",
                "r5dn.8xlarge",
                "r5dn.12xlarge",
                "r5dn.16xlarge",
                "r5dn.24xlarge",
                "r5n.large",
                "r5n.xlarge",
                "r5n.2xlarge",
                "r5n.4xlarge",
                "r5n.8xlarge",
                "r5n.12xlarge",
                "r5n.16xlarge",
                "r5n.24xlarge",
                "inf1.xlarge",
                "inf1.2xlarge",
                "inf1.6xlarge",
                "inf1.24xlarge",
            ]
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ProductDescriptions: List[str] = None,
        StartTime: datetime = None,
    ) -> DescribeSpotPriceHistoryResultTypeDef:
        """
        [Client.describe_spot_price_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_spot_price_history)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stale_security_groups(
        self, VpcId: str, DryRun: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeStaleSecurityGroupsResultTypeDef:
        """
        [Client.describe_stale_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_stale_security_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_subnets(
        self,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeSubnetsResultTypeDef:
        """
        [Client.describe_subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_subnets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tags(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeTagsResultTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_traffic_mirror_filters(
        self,
        TrafficMirrorFilterIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeTrafficMirrorFiltersResultTypeDef:
        """
        [Client.describe_traffic_mirror_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_filters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_traffic_mirror_sessions(
        self,
        TrafficMirrorSessionIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeTrafficMirrorSessionsResultTypeDef:
        """
        [Client.describe_traffic_mirror_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_sessions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_traffic_mirror_targets(
        self,
        TrafficMirrorTargetIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeTrafficMirrorTargetsResultTypeDef:
        """
        [Client.describe_traffic_mirror_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_transit_gateway_attachments(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayAttachmentsResultTypeDef:
        """
        [Client.describe_transit_gateway_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_transit_gateway_attachments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_transit_gateway_multicast_domains(
        self,
        TransitGatewayMulticastDomainIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayMulticastDomainsResultTypeDef:
        """
        [Client.describe_transit_gateway_multicast_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_transit_gateway_multicast_domains)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_transit_gateway_peering_attachments(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayPeeringAttachmentsResultTypeDef:
        """
        [Client.describe_transit_gateway_peering_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_transit_gateway_peering_attachments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_transit_gateway_route_tables(
        self,
        TransitGatewayRouteTableIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayRouteTablesResultTypeDef:
        """
        [Client.describe_transit_gateway_route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_transit_gateway_route_tables)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_transit_gateway_vpc_attachments(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayVpcAttachmentsResultTypeDef:
        """
        [Client.describe_transit_gateway_vpc_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_transit_gateway_vpc_attachments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_transit_gateways(
        self,
        TransitGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewaysResultTypeDef:
        """
        [Client.describe_transit_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_transit_gateways)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_volume_attribute(
        self, Attribute: Literal["autoEnableIO", "productCodes"], VolumeId: str, DryRun: bool = None
    ) -> DescribeVolumeAttributeResultTypeDef:
        """
        [Client.describe_volume_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_volume_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_volume_status(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeVolumeStatusResultTypeDef:
        """
        [Client.describe_volume_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_volume_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_volumes(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVolumesResultTypeDef:
        """
        [Client.describe_volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_volumes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_volumes_modifications(
        self,
        DryRun: bool = None,
        VolumeIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeVolumesModificationsResultTypeDef:
        """
        [Client.describe_volumes_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_volumes_modifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_attribute(
        self,
        Attribute: Literal["enableDnsSupport", "enableDnsHostnames"],
        VpcId: str,
        DryRun: bool = None,
    ) -> DescribeVpcAttributeResultTypeDef:
        """
        [Client.describe_vpc_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpc_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_classic_link(
        self, Filters: List[FilterTypeDef] = None, DryRun: bool = None, VpcIds: List[str] = None
    ) -> DescribeVpcClassicLinkResultTypeDef:
        """
        [Client.describe_vpc_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_classic_link_dns_support(
        self, MaxResults: int = None, NextToken: str = None, VpcIds: List[str] = None
    ) -> DescribeVpcClassicLinkDnsSupportResultTypeDef:
        """
        [Client.describe_vpc_classic_link_dns_support documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link_dns_support)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_endpoint_connection_notifications(
        self,
        DryRun: bool = None,
        ConnectionNotificationId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointConnectionNotificationsResultTypeDef:
        """
        [Client.describe_vpc_endpoint_connection_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connection_notifications)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_endpoint_connections(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointConnectionsResultTypeDef:
        """
        [Client.describe_vpc_endpoint_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_endpoint_service_configurations(
        self,
        DryRun: bool = None,
        ServiceIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointServiceConfigurationsResultTypeDef:
        """
        [Client.describe_vpc_endpoint_service_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_endpoint_service_permissions(
        self,
        ServiceId: str,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointServicePermissionsResultTypeDef:
        """
        [Client.describe_vpc_endpoint_service_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_endpoint_services(
        self,
        DryRun: bool = None,
        ServiceNames: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointServicesResultTypeDef:
        """
        [Client.describe_vpc_endpoint_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_services)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_endpoints(
        self,
        DryRun: bool = None,
        VpcEndpointIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointsResultTypeDef:
        """
        [Client.describe_vpc_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpc_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpc_peering_connections(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeVpcPeeringConnectionsResultTypeDef:
        """
        [Client.describe_vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpc_peering_connections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpcs(
        self,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeVpcsResultTypeDef:
        """
        [Client.describe_vpcs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpcs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpn_connections(
        self,
        Filters: List[FilterTypeDef] = None,
        VpnConnectionIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeVpnConnectionsResultTypeDef:
        """
        [Client.describe_vpn_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpn_connections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vpn_gateways(
        self,
        Filters: List[FilterTypeDef] = None,
        VpnGatewayIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeVpnGatewaysResultTypeDef:
        """
        [Client.describe_vpn_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.describe_vpn_gateways)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_classic_link_vpc(
        self, InstanceId: str, VpcId: str, DryRun: bool = None
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        [Client.detach_classic_link_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.detach_classic_link_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_internet_gateway(
        self, InternetGatewayId: str, VpcId: str, DryRun: bool = None
    ) -> None:
        """
        [Client.detach_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.detach_internet_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_network_interface(
        self, AttachmentId: str, DryRun: bool = None, Force: bool = None
    ) -> None:
        """
        [Client.detach_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.detach_network_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_volume(
        self,
        VolumeId: str,
        Device: str = None,
        Force: bool = None,
        InstanceId: str = None,
        DryRun: bool = None,
    ) -> VolumeAttachmentTypeDef:
        """
        [Client.detach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.detach_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_vpn_gateway(self, VpcId: str, VpnGatewayId: str, DryRun: bool = None) -> None:
        """
        [Client.detach_vpn_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.detach_vpn_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_ebs_encryption_by_default(
        self, DryRun: bool = None
    ) -> DisableEbsEncryptionByDefaultResultTypeDef:
        """
        [Client.disable_ebs_encryption_by_default documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disable_ebs_encryption_by_default)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_fast_snapshot_restores(
        self, AvailabilityZones: List[str], SourceSnapshotIds: List[str], DryRun: bool = None
    ) -> DisableFastSnapshotRestoresResultTypeDef:
        """
        [Client.disable_fast_snapshot_restores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disable_fast_snapshot_restores)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_transit_gateway_route_table_propagation(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DisableTransitGatewayRouteTablePropagationResultTypeDef:
        """
        [Client.disable_transit_gateway_route_table_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disable_transit_gateway_route_table_propagation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_vgw_route_propagation(self, GatewayId: str, RouteTableId: str) -> None:
        """
        [Client.disable_vgw_route_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disable_vgw_route_propagation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_vpc_classic_link(
        self, VpcId: str, DryRun: bool = None
    ) -> DisableVpcClassicLinkResultTypeDef:
        """
        [Client.disable_vpc_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_vpc_classic_link_dns_support(
        self, VpcId: str = None
    ) -> DisableVpcClassicLinkDnsSupportResultTypeDef:
        """
        [Client.disable_vpc_classic_link_dns_support documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link_dns_support)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_address(
        self, AssociationId: str = None, PublicIp: str = None, DryRun: bool = None
    ) -> None:
        """
        [Client.disassociate_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disassociate_address)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_client_vpn_target_network(
        self, ClientVpnEndpointId: str, AssociationId: str, DryRun: bool = None
    ) -> DisassociateClientVpnTargetNetworkResultTypeDef:
        """
        [Client.disassociate_client_vpn_target_network documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disassociate_client_vpn_target_network)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_iam_instance_profile(
        self, AssociationId: str
    ) -> DisassociateIamInstanceProfileResultTypeDef:
        """
        [Client.disassociate_iam_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disassociate_iam_instance_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_route_table(self, AssociationId: str, DryRun: bool = None) -> None:
        """
        [Client.disassociate_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disassociate_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_subnet_cidr_block(
        self, AssociationId: str
    ) -> DisassociateSubnetCidrBlockResultTypeDef:
        """
        [Client.disassociate_subnet_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disassociate_subnet_cidr_block)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_transit_gateway_multicast_domain(
        self,
        TransitGatewayMulticastDomainId: str = None,
        TransitGatewayAttachmentId: str = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
    ) -> DisassociateTransitGatewayMulticastDomainResultTypeDef:
        """
        [Client.disassociate_transit_gateway_multicast_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_multicast_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_transit_gateway_route_table(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DisassociateTransitGatewayRouteTableResultTypeDef:
        """
        [Client.disassociate_transit_gateway_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_vpc_cidr_block(
        self, AssociationId: str
    ) -> DisassociateVpcCidrBlockResultTypeDef:
        """
        [Client.disassociate_vpc_cidr_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.disassociate_vpc_cidr_block)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_ebs_encryption_by_default(
        self, DryRun: bool = None
    ) -> EnableEbsEncryptionByDefaultResultTypeDef:
        """
        [Client.enable_ebs_encryption_by_default documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.enable_ebs_encryption_by_default)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_fast_snapshot_restores(
        self, AvailabilityZones: List[str], SourceSnapshotIds: List[str], DryRun: bool = None
    ) -> EnableFastSnapshotRestoresResultTypeDef:
        """
        [Client.enable_fast_snapshot_restores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.enable_fast_snapshot_restores)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_transit_gateway_route_table_propagation(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> EnableTransitGatewayRouteTablePropagationResultTypeDef:
        """
        [Client.enable_transit_gateway_route_table_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.enable_transit_gateway_route_table_propagation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_vgw_route_propagation(self, GatewayId: str, RouteTableId: str) -> None:
        """
        [Client.enable_vgw_route_propagation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.enable_vgw_route_propagation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_volume_io(self, VolumeId: str, DryRun: bool = None) -> None:
        """
        [Client.enable_volume_io documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.enable_volume_io)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_vpc_classic_link(
        self, VpcId: str, DryRun: bool = None
    ) -> EnableVpcClassicLinkResultTypeDef:
        """
        [Client.enable_vpc_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_vpc_classic_link_dns_support(
        self, VpcId: str = None
    ) -> EnableVpcClassicLinkDnsSupportResultTypeDef:
        """
        [Client.enable_vpc_classic_link_dns_support documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link_dns_support)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_client_vpn_client_certificate_revocation_list(
        self, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> ExportClientVpnClientCertificateRevocationListResultTypeDef:
        """
        [Client.export_client_vpn_client_certificate_revocation_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.export_client_vpn_client_certificate_revocation_list)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_client_vpn_client_configuration(
        self, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> ExportClientVpnClientConfigurationResultTypeDef:
        """
        [Client.export_client_vpn_client_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.export_client_vpn_client_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_image(
        self,
        DiskImageFormat: Literal["VMDK", "RAW", "VHD"],
        ImageId: str,
        S3ExportLocation: ExportTaskS3LocationRequestTypeDef,
        ClientToken: str = None,
        Description: str = None,
        DryRun: bool = None,
        RoleName: str = None,
    ) -> ExportImageResultTypeDef:
        """
        [Client.export_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.export_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_transit_gateway_routes(
        self,
        TransitGatewayRouteTableId: str,
        S3Bucket: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
    ) -> ExportTransitGatewayRoutesResultTypeDef:
        """
        [Client.export_transit_gateway_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.export_transit_gateway_routes)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_capacity_reservation_usage(
        self,
        CapacityReservationId: str,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None,
    ) -> GetCapacityReservationUsageResultTypeDef:
        """
        [Client.get_capacity_reservation_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_capacity_reservation_usage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_coip_pool_usage(
        self,
        PoolId: str,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> GetCoipPoolUsageResultTypeDef:
        """
        [Client.get_coip_pool_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_coip_pool_usage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_console_output(
        self, InstanceId: str, DryRun: bool = None, Latest: bool = None
    ) -> GetConsoleOutputResultTypeDef:
        """
        [Client.get_console_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_console_output)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_console_screenshot(
        self, InstanceId: str, DryRun: bool = None, WakeUp: bool = None
    ) -> GetConsoleScreenshotResultTypeDef:
        """
        [Client.get_console_screenshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_console_screenshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_default_credit_specification(
        self, InstanceFamily: Literal["t2", "t3", "t3a"], DryRun: bool = None
    ) -> GetDefaultCreditSpecificationResultTypeDef:
        """
        [Client.get_default_credit_specification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_default_credit_specification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ebs_default_kms_key_id(self, DryRun: bool = None) -> GetEbsDefaultKmsKeyIdResultTypeDef:
        """
        [Client.get_ebs_default_kms_key_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_ebs_default_kms_key_id)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_ebs_encryption_by_default(
        self, DryRun: bool = None
    ) -> GetEbsEncryptionByDefaultResultTypeDef:
        """
        [Client.get_ebs_encryption_by_default documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_ebs_encryption_by_default)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_host_reservation_purchase_preview(
        self, HostIdSet: List[str], OfferingId: str
    ) -> GetHostReservationPurchasePreviewResultTypeDef:
        """
        [Client.get_host_reservation_purchase_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_host_reservation_purchase_preview)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_launch_template_data(
        self, InstanceId: str, DryRun: bool = None
    ) -> GetLaunchTemplateDataResultTypeDef:
        """
        [Client.get_launch_template_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_launch_template_data)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_password_data(
        self, InstanceId: str, DryRun: bool = None
    ) -> GetPasswordDataResultTypeDef:
        """
        [Client.get_password_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_password_data)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_reserved_instances_exchange_quote(
        self,
        ReservedInstanceIds: List[str],
        DryRun: bool = None,
        TargetConfigurations: List[TargetConfigurationRequestTypeDef] = None,
    ) -> GetReservedInstancesExchangeQuoteResultTypeDef:
        """
        [Client.get_reserved_instances_exchange_quote documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_reserved_instances_exchange_quote)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_transit_gateway_attachment_propagations(
        self,
        TransitGatewayAttachmentId: str,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> GetTransitGatewayAttachmentPropagationsResultTypeDef:
        """
        [Client.get_transit_gateway_attachment_propagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_transit_gateway_attachment_propagations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_transit_gateway_multicast_domain_associations(
        self,
        TransitGatewayMulticastDomainId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> GetTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        [Client.get_transit_gateway_multicast_domain_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_transit_gateway_multicast_domain_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_transit_gateway_route_table_associations(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> GetTransitGatewayRouteTableAssociationsResultTypeDef:
        """
        [Client.get_transit_gateway_route_table_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_associations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_transit_gateway_route_table_propagations(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> GetTransitGatewayRouteTablePropagationsResultTypeDef:
        """
        [Client.get_transit_gateway_route_table_propagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_propagations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_client_vpn_client_certificate_revocation_list(
        self, ClientVpnEndpointId: str, CertificateRevocationList: str, DryRun: bool = None
    ) -> ImportClientVpnClientCertificateRevocationListResultTypeDef:
        """
        [Client.import_client_vpn_client_certificate_revocation_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.import_client_vpn_client_certificate_revocation_list)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_image(
        self,
        Architecture: str = None,
        ClientData: ClientDataTypeDef = None,
        ClientToken: str = None,
        Description: str = None,
        DiskContainers: List[ImageDiskContainerTypeDef] = None,
        DryRun: bool = None,
        Encrypted: bool = None,
        Hypervisor: str = None,
        KmsKeyId: str = None,
        LicenseType: str = None,
        Platform: str = None,
        RoleName: str = None,
        LicenseSpecifications: List[ImportImageLicenseConfigurationRequestTypeDef] = None,
    ) -> ImportImageResultTypeDef:
        """
        [Client.import_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.import_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_instance(
        self,
        Platform: Literal["Windows"],
        Description: str = None,
        DiskImages: List[DiskImageTypeDef] = None,
        DryRun: bool = None,
        LaunchSpecification: ImportInstanceLaunchSpecificationTypeDef = None,
    ) -> ImportInstanceResultTypeDef:
        """
        [Client.import_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.import_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_key_pair(
        self, KeyName: str, PublicKeyMaterial: Union[bytes, IO], DryRun: bool = None
    ) -> ImportKeyPairResultTypeDef:
        """
        [Client.import_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.import_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_snapshot(
        self,
        ClientData: ClientDataTypeDef = None,
        ClientToken: str = None,
        Description: str = None,
        DiskContainer: SnapshotDiskContainerTypeDef = None,
        DryRun: bool = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        RoleName: str = None,
    ) -> ImportSnapshotResultTypeDef:
        """
        [Client.import_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.import_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_volume(
        self,
        AvailabilityZone: str,
        Image: DiskImageDetailTypeDef,
        Volume: VolumeDetailTypeDef,
        Description: str = None,
        DryRun: bool = None,
    ) -> ImportVolumeResultTypeDef:
        """
        [Client.import_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.import_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_capacity_reservation(
        self,
        CapacityReservationId: str,
        InstanceCount: int = None,
        EndDate: datetime = None,
        EndDateType: Literal["unlimited", "limited"] = None,
        DryRun: bool = None,
    ) -> ModifyCapacityReservationResultTypeDef:
        """
        [Client.modify_capacity_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_capacity_reservation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_client_vpn_endpoint(
        self,
        ClientVpnEndpointId: str,
        ServerCertificateArn: str = None,
        ConnectionLogOptions: ConnectionLogOptionsTypeDef = None,
        DnsServers: DnsServersOptionsModifyStructureTypeDef = None,
        Description: str = None,
        SplitTunnel: bool = None,
        DryRun: bool = None,
    ) -> ModifyClientVpnEndpointResultTypeDef:
        """
        [Client.modify_client_vpn_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_client_vpn_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_default_credit_specification(
        self, InstanceFamily: Literal["t2", "t3", "t3a"], CpuCredits: str, DryRun: bool = None
    ) -> ModifyDefaultCreditSpecificationResultTypeDef:
        """
        [Client.modify_default_credit_specification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_default_credit_specification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_ebs_default_kms_key_id(
        self, KmsKeyId: str, DryRun: bool = None
    ) -> ModifyEbsDefaultKmsKeyIdResultTypeDef:
        """
        [Client.modify_ebs_default_kms_key_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_ebs_default_kms_key_id)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_fleet(
        self,
        FleetId: str,
        TargetCapacitySpecification: TargetCapacitySpecificationRequestTypeDef,
        DryRun: bool = None,
        ExcessCapacityTerminationPolicy: Literal["no-termination", "termination"] = None,
    ) -> ModifyFleetResultTypeDef:
        """
        [Client.modify_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_fpga_image_attribute(
        self,
        FpgaImageId: str,
        DryRun: bool = None,
        Attribute: Literal["description", "name", "loadPermission", "productCodes"] = None,
        OperationType: Literal["add", "remove"] = None,
        UserIds: List[str] = None,
        UserGroups: List[str] = None,
        ProductCodes: List[str] = None,
        LoadPermission: LoadPermissionModificationsTypeDef = None,
        Description: str = None,
        Name: str = None,
    ) -> ModifyFpgaImageAttributeResultTypeDef:
        """
        [Client.modify_fpga_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_fpga_image_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_hosts(
        self,
        HostIds: List[str],
        AutoPlacement: Literal["on", "off"] = None,
        HostRecovery: Literal["on", "off"] = None,
        InstanceType: str = None,
        InstanceFamily: str = None,
    ) -> ModifyHostsResultTypeDef:
        """
        [Client.modify_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_hosts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_id_format(self, Resource: str, UseLongIds: bool) -> None:
        """
        [Client.modify_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_id_format)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_identity_id_format(self, PrincipalArn: str, Resource: str, UseLongIds: bool) -> None:
        """
        [Client.modify_identity_id_format documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_identity_id_format)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_image_attribute(
        self,
        ImageId: str,
        Attribute: str = None,
        Description: AttributeValueTypeDef = None,
        LaunchPermission: LaunchPermissionModificationsTypeDef = None,
        OperationType: Literal["add", "remove"] = None,
        ProductCodes: List[str] = None,
        UserGroups: List[str] = None,
        UserIds: List[str] = None,
        Value: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.modify_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_image_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_instance_attribute(
        self,
        InstanceId: str,
        SourceDestCheck: AttributeBooleanValueTypeDef = None,
        Attribute: Literal[
            "instanceType",
            "kernel",
            "ramdisk",
            "userData",
            "disableApiTermination",
            "instanceInitiatedShutdownBehavior",
            "rootDeviceName",
            "blockDeviceMapping",
            "productCodes",
            "sourceDestCheck",
            "groupSet",
            "ebsOptimized",
            "sriovNetSupport",
            "enaSupport",
        ] = None,
        BlockDeviceMappings: List[InstanceBlockDeviceMappingSpecificationTypeDef] = None,
        DisableApiTermination: AttributeBooleanValueTypeDef = None,
        DryRun: bool = None,
        EbsOptimized: AttributeBooleanValueTypeDef = None,
        EnaSupport: AttributeBooleanValueTypeDef = None,
        Groups: List[str] = None,
        InstanceInitiatedShutdownBehavior: AttributeValueTypeDef = None,
        InstanceType: AttributeValueTypeDef = None,
        Kernel: AttributeValueTypeDef = None,
        Ramdisk: AttributeValueTypeDef = None,
        SriovNetSupport: AttributeValueTypeDef = None,
        UserData: BlobAttributeValueTypeDef = None,
        Value: str = None,
    ) -> None:
        """
        [Client.modify_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_instance_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_instance_capacity_reservation_attributes(
        self,
        InstanceId: str,
        CapacityReservationSpecification: CapacityReservationSpecificationTypeDef,
        DryRun: bool = None,
    ) -> ModifyInstanceCapacityReservationAttributesResultTypeDef:
        """
        [Client.modify_instance_capacity_reservation_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_instance_capacity_reservation_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_instance_credit_specification(
        self,
        InstanceCreditSpecifications: List[InstanceCreditSpecificationRequestTypeDef],
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> ModifyInstanceCreditSpecificationResultTypeDef:
        """
        [Client.modify_instance_credit_specification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_instance_credit_specification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_instance_event_start_time(
        self, InstanceId: str, InstanceEventId: str, NotBefore: datetime, DryRun: bool = None
    ) -> ModifyInstanceEventStartTimeResultTypeDef:
        """
        [Client.modify_instance_event_start_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_instance_event_start_time)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_instance_metadata_options(
        self,
        InstanceId: str,
        HttpTokens: Literal["optional", "required"] = None,
        HttpPutResponseHopLimit: int = None,
        HttpEndpoint: Literal["disabled", "enabled"] = None,
        DryRun: bool = None,
    ) -> ModifyInstanceMetadataOptionsResultTypeDef:
        """
        [Client.modify_instance_metadata_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_instance_metadata_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_instance_placement(
        self,
        InstanceId: str,
        Affinity: Literal["default", "host"] = None,
        GroupName: str = None,
        HostId: str = None,
        Tenancy: Literal["dedicated", "host"] = None,
        PartitionNumber: int = None,
        HostResourceGroupArn: str = None,
    ) -> ModifyInstancePlacementResultTypeDef:
        """
        [Client.modify_instance_placement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_instance_placement)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_launch_template(
        self,
        DryRun: bool = None,
        ClientToken: str = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        DefaultVersion: str = None,
    ) -> ModifyLaunchTemplateResultTypeDef:
        """
        [Client.modify_launch_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_launch_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_network_interface_attribute(
        self,
        NetworkInterfaceId: str,
        Attachment: NetworkInterfaceAttachmentChangesTypeDef = None,
        Description: AttributeValueTypeDef = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        SourceDestCheck: AttributeBooleanValueTypeDef = None,
    ) -> None:
        """
        [Client.modify_network_interface_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_network_interface_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_reserved_instances(
        self,
        ReservedInstancesIds: List[str],
        TargetConfigurations: List[ReservedInstancesConfigurationTypeDef],
        ClientToken: str = None,
    ) -> ModifyReservedInstancesResultTypeDef:
        """
        [Client.modify_reserved_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_reserved_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_snapshot_attribute(
        self,
        SnapshotId: str,
        Attribute: Literal["productCodes", "createVolumePermission"] = None,
        CreateVolumePermission: CreateVolumePermissionModificationsTypeDef = None,
        GroupNames: List[str] = None,
        OperationType: Literal["add", "remove"] = None,
        UserIds: List[str] = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.modify_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_snapshot_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_spot_fleet_request(
        self,
        SpotFleetRequestId: str,
        ExcessCapacityTerminationPolicy: Literal["noTermination", "default"] = None,
        TargetCapacity: int = None,
        OnDemandTargetCapacity: int = None,
    ) -> ModifySpotFleetRequestResponseTypeDef:
        """
        [Client.modify_spot_fleet_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_spot_fleet_request)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_subnet_attribute(
        self,
        SubnetId: str,
        AssignIpv6AddressOnCreation: AttributeBooleanValueTypeDef = None,
        MapPublicIpOnLaunch: AttributeBooleanValueTypeDef = None,
    ) -> None:
        """
        [Client.modify_subnet_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_subnet_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_traffic_mirror_filter_network_services(
        self,
        TrafficMirrorFilterId: str,
        AddNetworkServices: List[Literal["amazon-dns"]] = None,
        RemoveNetworkServices: List[Literal["amazon-dns"]] = None,
        DryRun: bool = None,
    ) -> ModifyTrafficMirrorFilterNetworkServicesResultTypeDef:
        """
        [Client.modify_traffic_mirror_filter_network_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_network_services)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_traffic_mirror_filter_rule(
        self,
        TrafficMirrorFilterRuleId: str,
        TrafficDirection: Literal["ingress", "egress"] = None,
        RuleNumber: int = None,
        RuleAction: Literal["accept", "reject"] = None,
        DestinationPortRange: TrafficMirrorPortRangeRequestTypeDef = None,
        SourcePortRange: TrafficMirrorPortRangeRequestTypeDef = None,
        Protocol: int = None,
        DestinationCidrBlock: str = None,
        SourceCidrBlock: str = None,
        Description: str = None,
        RemoveFields: List[
            Literal["destination-port-range", "source-port-range", "protocol", "description"]
        ] = None,
        DryRun: bool = None,
    ) -> ModifyTrafficMirrorFilterRuleResultTypeDef:
        """
        [Client.modify_traffic_mirror_filter_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_traffic_mirror_session(
        self,
        TrafficMirrorSessionId: str,
        TrafficMirrorTargetId: str = None,
        TrafficMirrorFilterId: str = None,
        PacketLength: int = None,
        SessionNumber: int = None,
        VirtualNetworkId: int = None,
        Description: str = None,
        RemoveFields: List[Literal["packet-length", "description", "virtual-network-id"]] = None,
        DryRun: bool = None,
    ) -> ModifyTrafficMirrorSessionResultTypeDef:
        """
        [Client.modify_traffic_mirror_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_session)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_transit_gateway_vpc_attachment(
        self,
        TransitGatewayAttachmentId: str,
        AddSubnetIds: List[str] = None,
        RemoveSubnetIds: List[str] = None,
        Options: ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef = None,
        DryRun: bool = None,
    ) -> ModifyTransitGatewayVpcAttachmentResultTypeDef:
        """
        [Client.modify_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_transit_gateway_vpc_attachment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_volume(
        self,
        VolumeId: str,
        DryRun: bool = None,
        Size: int = None,
        VolumeType: Literal["standard", "io1", "gp2", "sc1", "st1"] = None,
        Iops: int = None,
    ) -> ModifyVolumeResultTypeDef:
        """
        [Client.modify_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_volume_attribute(
        self, VolumeId: str, AutoEnableIO: AttributeBooleanValueTypeDef = None, DryRun: bool = None
    ) -> None:
        """
        [Client.modify_volume_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_volume_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_vpc_attribute(
        self,
        VpcId: str,
        EnableDnsHostnames: AttributeBooleanValueTypeDef = None,
        EnableDnsSupport: AttributeBooleanValueTypeDef = None,
    ) -> None:
        """
        [Client.modify_vpc_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_vpc_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_vpc_endpoint(
        self,
        VpcEndpointId: str,
        DryRun: bool = None,
        ResetPolicy: bool = None,
        PolicyDocument: str = None,
        AddRouteTableIds: List[str] = None,
        RemoveRouteTableIds: List[str] = None,
        AddSubnetIds: List[str] = None,
        RemoveSubnetIds: List[str] = None,
        AddSecurityGroupIds: List[str] = None,
        RemoveSecurityGroupIds: List[str] = None,
        PrivateDnsEnabled: bool = None,
    ) -> ModifyVpcEndpointResultTypeDef:
        """
        [Client.modify_vpc_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_vpc_endpoint_connection_notification(
        self,
        ConnectionNotificationId: str,
        DryRun: bool = None,
        ConnectionNotificationArn: str = None,
        ConnectionEvents: List[str] = None,
    ) -> ModifyVpcEndpointConnectionNotificationResultTypeDef:
        """
        [Client.modify_vpc_endpoint_connection_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_connection_notification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_vpc_endpoint_service_configuration(
        self,
        ServiceId: str,
        DryRun: bool = None,
        AcceptanceRequired: bool = None,
        AddNetworkLoadBalancerArns: List[str] = None,
        RemoveNetworkLoadBalancerArns: List[str] = None,
    ) -> ModifyVpcEndpointServiceConfigurationResultTypeDef:
        """
        [Client.modify_vpc_endpoint_service_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_vpc_endpoint_service_permissions(
        self,
        ServiceId: str,
        DryRun: bool = None,
        AddAllowedPrincipals: List[str] = None,
        RemoveAllowedPrincipals: List[str] = None,
    ) -> ModifyVpcEndpointServicePermissionsResultTypeDef:
        """
        [Client.modify_vpc_endpoint_service_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_permissions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_vpc_peering_connection_options(
        self,
        VpcPeeringConnectionId: str,
        AccepterPeeringConnectionOptions: PeeringConnectionOptionsRequestTypeDef = None,
        DryRun: bool = None,
        RequesterPeeringConnectionOptions: PeeringConnectionOptionsRequestTypeDef = None,
    ) -> ModifyVpcPeeringConnectionOptionsResultTypeDef:
        """
        [Client.modify_vpc_peering_connection_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_vpc_peering_connection_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_vpc_tenancy(
        self, VpcId: str, InstanceTenancy: Literal["default"], DryRun: bool = None
    ) -> ModifyVpcTenancyResultTypeDef:
        """
        [Client.modify_vpc_tenancy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_vpc_tenancy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_vpn_connection(
        self,
        VpnConnectionId: str,
        TransitGatewayId: str = None,
        CustomerGatewayId: str = None,
        VpnGatewayId: str = None,
        DryRun: bool = None,
    ) -> ModifyVpnConnectionResultTypeDef:
        """
        [Client.modify_vpn_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_vpn_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_vpn_tunnel_certificate(
        self, VpnConnectionId: str, VpnTunnelOutsideIpAddress: str, DryRun: bool = None
    ) -> ModifyVpnTunnelCertificateResultTypeDef:
        """
        [Client.modify_vpn_tunnel_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_vpn_tunnel_options(
        self,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        TunnelOptions: ModifyVpnTunnelOptionsSpecificationTypeDef,
        DryRun: bool = None,
    ) -> ModifyVpnTunnelOptionsResultTypeDef:
        """
        [Client.modify_vpn_tunnel_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def monitor_instances(
        self, InstanceIds: List[str], DryRun: bool = None
    ) -> MonitorInstancesResultTypeDef:
        """
        [Client.monitor_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.monitor_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def move_address_to_vpc(
        self, PublicIp: str, DryRun: bool = None
    ) -> MoveAddressToVpcResultTypeDef:
        """
        [Client.move_address_to_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.move_address_to_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def provision_byoip_cidr(
        self,
        Cidr: str,
        CidrAuthorizationContext: CidrAuthorizationContextTypeDef = None,
        Description: str = None,
        DryRun: bool = None,
    ) -> ProvisionByoipCidrResultTypeDef:
        """
        [Client.provision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.provision_byoip_cidr)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purchase_host_reservation(
        self,
        HostIdSet: List[str],
        OfferingId: str,
        ClientToken: str = None,
        CurrencyCode: Literal["USD"] = None,
        LimitPrice: str = None,
    ) -> PurchaseHostReservationResultTypeDef:
        """
        [Client.purchase_host_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.purchase_host_reservation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purchase_reserved_instances_offering(
        self,
        InstanceCount: int,
        ReservedInstancesOfferingId: str,
        DryRun: bool = None,
        LimitPrice: ReservedInstanceLimitPriceTypeDef = None,
        PurchaseTime: datetime = None,
    ) -> PurchaseReservedInstancesOfferingResultTypeDef:
        """
        [Client.purchase_reserved_instances_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.purchase_reserved_instances_offering)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purchase_scheduled_instances(
        self,
        PurchaseRequests: List[PurchaseRequestTypeDef],
        ClientToken: str = None,
        DryRun: bool = None,
    ) -> PurchaseScheduledInstancesResultTypeDef:
        """
        [Client.purchase_scheduled_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.purchase_scheduled_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot_instances(self, InstanceIds: List[str], DryRun: bool = None) -> None:
        """
        [Client.reboot_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.reboot_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_image(
        self,
        Name: str,
        ImageLocation: str = None,
        Architecture: Literal["i386", "x86_64", "arm64"] = None,
        BlockDeviceMappings: List[BlockDeviceMappingTypeDef] = None,
        Description: str = None,
        DryRun: bool = None,
        EnaSupport: bool = None,
        KernelId: str = None,
        BillingProducts: List[str] = None,
        RamdiskId: str = None,
        RootDeviceName: str = None,
        SriovNetSupport: str = None,
        VirtualizationType: str = None,
    ) -> RegisterImageResultTypeDef:
        """
        [Client.register_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.register_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_transit_gateway_multicast_group_members(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> RegisterTransitGatewayMulticastGroupMembersResultTypeDef:
        """
        [Client.register_transit_gateway_multicast_group_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_members)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_transit_gateway_multicast_group_sources(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> RegisterTransitGatewayMulticastGroupSourcesResultTypeDef:
        """
        [Client.register_transit_gateway_multicast_group_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_sources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_transit_gateway_peering_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> RejectTransitGatewayPeeringAttachmentResultTypeDef:
        """
        [Client.reject_transit_gateway_peering_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.reject_transit_gateway_peering_attachment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_transit_gateway_vpc_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> RejectTransitGatewayVpcAttachmentResultTypeDef:
        """
        [Client.reject_transit_gateway_vpc_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.reject_transit_gateway_vpc_attachment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_vpc_endpoint_connections(
        self, ServiceId: str, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> RejectVpcEndpointConnectionsResultTypeDef:
        """
        [Client.reject_vpc_endpoint_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.reject_vpc_endpoint_connections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_vpc_peering_connection(
        self, VpcPeeringConnectionId: str, DryRun: bool = None
    ) -> RejectVpcPeeringConnectionResultTypeDef:
        """
        [Client.reject_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.reject_vpc_peering_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def release_address(
        self,
        AllocationId: str = None,
        PublicIp: str = None,
        NetworkBorderGroup: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.release_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.release_address)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def release_hosts(self, HostIds: List[str]) -> ReleaseHostsResultTypeDef:
        """
        [Client.release_hosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.release_hosts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_iam_instance_profile_association(
        self, IamInstanceProfile: IamInstanceProfileSpecificationTypeDef, AssociationId: str
    ) -> ReplaceIamInstanceProfileAssociationResultTypeDef:
        """
        [Client.replace_iam_instance_profile_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.replace_iam_instance_profile_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_network_acl_association(
        self, AssociationId: str, NetworkAclId: str, DryRun: bool = None
    ) -> ReplaceNetworkAclAssociationResultTypeDef:
        """
        [Client.replace_network_acl_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.replace_network_acl_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_network_acl_entry(
        self,
        Egress: bool,
        NetworkAclId: str,
        Protocol: str,
        RuleAction: Literal["allow", "deny"],
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: IcmpTypeCodeTypeDef = None,
        Ipv6CidrBlock: str = None,
        PortRange: PortRangeTypeDef = None,
    ) -> None:
        """
        [Client.replace_network_acl_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.replace_network_acl_entry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_route(
        self,
        RouteTableId: str,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DryRun: bool = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        LocalTarget: bool = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None,
    ) -> None:
        """
        [Client.replace_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.replace_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_route_table_association(
        self, AssociationId: str, RouteTableId: str, DryRun: bool = None
    ) -> ReplaceRouteTableAssociationResultTypeDef:
        """
        [Client.replace_route_table_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.replace_route_table_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_transit_gateway_route(
        self,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None,
    ) -> ReplaceTransitGatewayRouteResultTypeDef:
        """
        [Client.replace_transit_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.replace_transit_gateway_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def report_instance_status(
        self,
        Instances: List[str],
        ReasonCodes: List[
            Literal[
                "instance-stuck-in-state",
                "unresponsive",
                "not-accepting-credentials",
                "password-not-available",
                "performance-network",
                "performance-instance-store",
                "performance-ebs-volume",
                "performance-other",
                "other",
            ]
        ],
        Status: Literal["ok", "impaired"],
        Description: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        StartTime: datetime = None,
    ) -> None:
        """
        [Client.report_instance_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.report_instance_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def request_spot_fleet(
        self, SpotFleetRequestConfig: SpotFleetRequestConfigDataTypeDef, DryRun: bool = None
    ) -> RequestSpotFleetResponseTypeDef:
        """
        [Client.request_spot_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.request_spot_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def request_spot_instances(
        self,
        AvailabilityZoneGroup: str = None,
        BlockDurationMinutes: int = None,
        ClientToken: str = None,
        DryRun: bool = None,
        InstanceCount: int = None,
        LaunchGroup: str = None,
        LaunchSpecification: RequestSpotLaunchSpecificationTypeDef = None,
        SpotPrice: str = None,
        Type: Literal["one-time", "persistent"] = None,
        ValidFrom: datetime = None,
        ValidUntil: datetime = None,
        InstanceInterruptionBehavior: Literal["hibernate", "stop", "terminate"] = None,
    ) -> RequestSpotInstancesResultTypeDef:
        """
        [Client.request_spot_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.request_spot_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_ebs_default_kms_key_id(
        self, DryRun: bool = None
    ) -> ResetEbsDefaultKmsKeyIdResultTypeDef:
        """
        [Client.reset_ebs_default_kms_key_id documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.reset_ebs_default_kms_key_id)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_fpga_image_attribute(
        self, FpgaImageId: str, DryRun: bool = None, Attribute: Literal["loadPermission"] = None
    ) -> ResetFpgaImageAttributeResultTypeDef:
        """
        [Client.reset_fpga_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.reset_fpga_image_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_image_attribute(
        self, Attribute: Literal["launchPermission"], ImageId: str, DryRun: bool = None
    ) -> None:
        """
        [Client.reset_image_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.reset_image_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_instance_attribute(
        self,
        Attribute: Literal[
            "instanceType",
            "kernel",
            "ramdisk",
            "userData",
            "disableApiTermination",
            "instanceInitiatedShutdownBehavior",
            "rootDeviceName",
            "blockDeviceMapping",
            "productCodes",
            "sourceDestCheck",
            "groupSet",
            "ebsOptimized",
            "sriovNetSupport",
            "enaSupport",
        ],
        InstanceId: str,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.reset_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.reset_instance_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_network_interface_attribute(
        self, NetworkInterfaceId: str, DryRun: bool = None, SourceDestCheck: str = None
    ) -> None:
        """
        [Client.reset_network_interface_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.reset_network_interface_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_snapshot_attribute(
        self,
        Attribute: Literal["productCodes", "createVolumePermission"],
        SnapshotId: str,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.reset_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.reset_snapshot_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_address_to_classic(
        self, PublicIp: str, DryRun: bool = None
    ) -> RestoreAddressToClassicResultTypeDef:
        """
        [Client.restore_address_to_classic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.restore_address_to_classic)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_client_vpn_ingress(
        self,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str = None,
        RevokeAllGroups: bool = None,
        DryRun: bool = None,
    ) -> RevokeClientVpnIngressResultTypeDef:
        """
        [Client.revoke_client_vpn_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.revoke_client_vpn_ingress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_security_group_egress(
        self,
        GroupId: str,
        DryRun: bool = None,
        IpPermissions: List[IpPermissionTypeDef] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
    ) -> None:
        """
        [Client.revoke_security_group_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.revoke_security_group_egress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_security_group_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupId: str = None,
        GroupName: str = None,
        IpPermissions: List[IpPermissionTypeDef] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Client.revoke_security_group_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.revoke_security_group_ingress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def run_instances(
        self,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: List[BlockDeviceMappingTypeDef] = None,
        ImageId: str = None,
        InstanceType: Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
        ] = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List[InstanceIpv6AddressTypeDef] = None,
        KernelId: str = None,
        KeyName: str = None,
        Monitoring: RunInstancesMonitoringEnabledTypeDef = None,
        Placement: PlacementTypeDef = None,
        RamdiskId: str = None,
        SecurityGroupIds: List[str] = None,
        SecurityGroups: List[str] = None,
        SubnetId: str = None,
        UserData: str = None,
        AdditionalInfo: str = None,
        ClientToken: str = None,
        DisableApiTermination: bool = None,
        DryRun: bool = None,
        EbsOptimized: bool = None,
        IamInstanceProfile: IamInstanceProfileSpecificationTypeDef = None,
        InstanceInitiatedShutdownBehavior: Literal["stop", "terminate"] = None,
        NetworkInterfaces: List[InstanceNetworkInterfaceSpecificationTypeDef] = None,
        PrivateIpAddress: str = None,
        ElasticGpuSpecification: List[ElasticGpuSpecificationTypeDef] = None,
        ElasticInferenceAccelerators: List[ElasticInferenceAcceleratorTypeDef] = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        LaunchTemplate: LaunchTemplateSpecificationTypeDef = None,
        InstanceMarketOptions: InstanceMarketOptionsRequestTypeDef = None,
        CreditSpecification: CreditSpecificationRequestTypeDef = None,
        CpuOptions: CpuOptionsRequestTypeDef = None,
        CapacityReservationSpecification: CapacityReservationSpecificationTypeDef = None,
        HibernationOptions: HibernationOptionsRequestTypeDef = None,
        LicenseSpecifications: List[LicenseConfigurationRequestTypeDef] = None,
        MetadataOptions: InstanceMetadataOptionsRequestTypeDef = None,
    ) -> ReservationTypeDef:
        """
        [Client.run_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.run_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def run_scheduled_instances(
        self,
        LaunchSpecification: ScheduledInstancesLaunchSpecificationTypeDef,
        ScheduledInstanceId: str,
        ClientToken: str = None,
        DryRun: bool = None,
        InstanceCount: int = None,
    ) -> RunScheduledInstancesResultTypeDef:
        """
        [Client.run_scheduled_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.run_scheduled_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_local_gateway_routes(
        self,
        LocalGatewayRouteTableId: str,
        Filters: List[FilterTypeDef],
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> SearchLocalGatewayRoutesResultTypeDef:
        """
        [Client.search_local_gateway_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.search_local_gateway_routes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_transit_gateway_multicast_groups(
        self,
        TransitGatewayMulticastDomainId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> SearchTransitGatewayMulticastGroupsResultTypeDef:
        """
        [Client.search_transit_gateway_multicast_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.search_transit_gateway_multicast_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_transit_gateway_routes(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef],
        MaxResults: int = None,
        DryRun: bool = None,
    ) -> SearchTransitGatewayRoutesResultTypeDef:
        """
        [Client.search_transit_gateway_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.search_transit_gateway_routes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def send_diagnostic_interrupt(self, InstanceId: str, DryRun: bool = None) -> None:
        """
        [Client.send_diagnostic_interrupt documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.send_diagnostic_interrupt)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_instances(
        self, InstanceIds: List[str], AdditionalInfo: str = None, DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        """
        [Client.start_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.start_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_instances(
        self,
        InstanceIds: List[str],
        Hibernate: bool = None,
        DryRun: bool = None,
        Force: bool = None,
    ) -> StopInstancesResultTypeDef:
        """
        [Client.stop_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.stop_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate_client_vpn_connections(
        self,
        ClientVpnEndpointId: str,
        ConnectionId: str = None,
        Username: str = None,
        DryRun: bool = None,
    ) -> TerminateClientVpnConnectionsResultTypeDef:
        """
        [Client.terminate_client_vpn_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.terminate_client_vpn_connections)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate_instances(
        self, InstanceIds: List[str], DryRun: bool = None
    ) -> TerminateInstancesResultTypeDef:
        """
        [Client.terminate_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.terminate_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unassign_ipv6_addresses(
        self, Ipv6Addresses: List[str], NetworkInterfaceId: str
    ) -> UnassignIpv6AddressesResultTypeDef:
        """
        [Client.unassign_ipv6_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.unassign_ipv6_addresses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unassign_private_ip_addresses(
        self, NetworkInterfaceId: str, PrivateIpAddresses: List[str]
    ) -> None:
        """
        [Client.unassign_private_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.unassign_private_ip_addresses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unmonitor_instances(
        self, InstanceIds: List[str], DryRun: bool = None
    ) -> UnmonitorInstancesResultTypeDef:
        """
        [Client.unmonitor_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.unmonitor_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_security_group_rule_descriptions_egress(
        self,
        IpPermissions: List[IpPermissionTypeDef],
        DryRun: bool = None,
        GroupId: str = None,
        GroupName: str = None,
    ) -> UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef:
        """
        [Client.update_security_group_rule_descriptions_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_egress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_security_group_rule_descriptions_ingress(
        self,
        IpPermissions: List[IpPermissionTypeDef],
        DryRun: bool = None,
        GroupId: str = None,
        GroupName: str = None,
    ) -> UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef:
        """
        [Client.update_security_group_rule_descriptions_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_ingress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def withdraw_byoip_cidr(self, Cidr: str, DryRun: bool = None) -> WithdrawByoipCidrResultTypeDef:
        """
        [Client.withdraw_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Client.withdraw_byoip_cidr)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_byoip_cidrs"]
    ) -> paginator_scope.DescribeByoipCidrsPaginator:
        """
        [Paginator.DescribeByoipCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_capacity_reservations"]
    ) -> paginator_scope.DescribeCapacityReservationsPaginator:
        """
        [Paginator.DescribeCapacityReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_classic_link_instances"]
    ) -> paginator_scope.DescribeClassicLinkInstancesPaginator:
        """
        [Paginator.DescribeClassicLinkInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_authorization_rules"]
    ) -> paginator_scope.DescribeClientVpnAuthorizationRulesPaginator:
        """
        [Paginator.DescribeClientVpnAuthorizationRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_connections"]
    ) -> paginator_scope.DescribeClientVpnConnectionsPaginator:
        """
        [Paginator.DescribeClientVpnConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_endpoints"]
    ) -> paginator_scope.DescribeClientVpnEndpointsPaginator:
        """
        [Paginator.DescribeClientVpnEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_routes"]
    ) -> paginator_scope.DescribeClientVpnRoutesPaginator:
        """
        [Paginator.DescribeClientVpnRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_target_networks"]
    ) -> paginator_scope.DescribeClientVpnTargetNetworksPaginator:
        """
        [Paginator.DescribeClientVpnTargetNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_dhcp_options"]
    ) -> paginator_scope.DescribeDhcpOptionsPaginator:
        """
        [Paginator.DescribeDhcpOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_egress_only_internet_gateways"]
    ) -> paginator_scope.DescribeEgressOnlyInternetGatewaysPaginator:
        """
        [Paginator.DescribeEgressOnlyInternetGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_export_image_tasks"]
    ) -> paginator_scope.DescribeExportImageTasksPaginator:
        """
        [Paginator.DescribeExportImageTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_fast_snapshot_restores"]
    ) -> paginator_scope.DescribeFastSnapshotRestoresPaginator:
        """
        [Paginator.DescribeFastSnapshotRestores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_fleets"]
    ) -> paginator_scope.DescribeFleetsPaginator:
        """
        [Paginator.DescribeFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFleets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_flow_logs"]
    ) -> paginator_scope.DescribeFlowLogsPaginator:
        """
        [Paginator.DescribeFlowLogs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_fpga_images"]
    ) -> paginator_scope.DescribeFpgaImagesPaginator:
        """
        [Paginator.DescribeFpgaImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_host_reservation_offerings"]
    ) -> paginator_scope.DescribeHostReservationOfferingsPaginator:
        """
        [Paginator.DescribeHostReservationOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_host_reservations"]
    ) -> paginator_scope.DescribeHostReservationsPaginator:
        """
        [Paginator.DescribeHostReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_hosts"]
    ) -> paginator_scope.DescribeHostsPaginator:
        """
        [Paginator.DescribeHosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeHosts)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_iam_instance_profile_associations"]
    ) -> paginator_scope.DescribeIamInstanceProfileAssociationsPaginator:
        """
        [Paginator.DescribeIamInstanceProfileAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_import_image_tasks"]
    ) -> paginator_scope.DescribeImportImageTasksPaginator:
        """
        [Paginator.DescribeImportImageTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_import_snapshot_tasks"]
    ) -> paginator_scope.DescribeImportSnapshotTasksPaginator:
        """
        [Paginator.DescribeImportSnapshotTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_instance_credit_specifications"]
    ) -> paginator_scope.DescribeInstanceCreditSpecificationsPaginator:
        """
        [Paginator.DescribeInstanceCreditSpecifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_instance_status"]
    ) -> paginator_scope.DescribeInstanceStatusPaginator:
        """
        [Paginator.DescribeInstanceStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_instances"]
    ) -> paginator_scope.DescribeInstancesPaginator:
        """
        [Paginator.DescribeInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_internet_gateways"]
    ) -> paginator_scope.DescribeInternetGatewaysPaginator:
        """
        [Paginator.DescribeInternetGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_launch_template_versions"]
    ) -> paginator_scope.DescribeLaunchTemplateVersionsPaginator:
        """
        [Paginator.DescribeLaunchTemplateVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_launch_templates"]
    ) -> paginator_scope.DescribeLaunchTemplatesPaginator:
        """
        [Paginator.DescribeLaunchTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_moving_addresses"]
    ) -> paginator_scope.DescribeMovingAddressesPaginator:
        """
        [Paginator.DescribeMovingAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_nat_gateways"]
    ) -> paginator_scope.DescribeNatGatewaysPaginator:
        """
        [Paginator.DescribeNatGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_network_acls"]
    ) -> paginator_scope.DescribeNetworkAclsPaginator:
        """
        [Paginator.DescribeNetworkAcls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_network_interface_permissions"]
    ) -> paginator_scope.DescribeNetworkInterfacePermissionsPaginator:
        """
        [Paginator.DescribeNetworkInterfacePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_network_interfaces"]
    ) -> paginator_scope.DescribeNetworkInterfacesPaginator:
        """
        [Paginator.DescribeNetworkInterfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_prefix_lists"]
    ) -> paginator_scope.DescribePrefixListsPaginator:
        """
        [Paginator.DescribePrefixLists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_principal_id_format"]
    ) -> paginator_scope.DescribePrincipalIdFormatPaginator:
        """
        [Paginator.DescribePrincipalIdFormat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_public_ipv4_pools"]
    ) -> paginator_scope.DescribePublicIpv4PoolsPaginator:
        """
        [Paginator.DescribePublicIpv4Pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_reserved_instances_modifications"]
    ) -> paginator_scope.DescribeReservedInstancesModificationsPaginator:
        """
        [Paginator.DescribeReservedInstancesModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_reserved_instances_offerings"]
    ) -> paginator_scope.DescribeReservedInstancesOfferingsPaginator:
        """
        [Paginator.DescribeReservedInstancesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_route_tables"]
    ) -> paginator_scope.DescribeRouteTablesPaginator:
        """
        [Paginator.DescribeRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_instance_availability"]
    ) -> paginator_scope.DescribeScheduledInstanceAvailabilityPaginator:
        """
        [Paginator.DescribeScheduledInstanceAvailability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_instances"]
    ) -> paginator_scope.DescribeScheduledInstancesPaginator:
        """
        [Paginator.DescribeScheduledInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_security_groups"]
    ) -> paginator_scope.DescribeSecurityGroupsPaginator:
        """
        [Paginator.DescribeSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> paginator_scope.DescribeSnapshotsPaginator:
        """
        [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_spot_fleet_instances"]
    ) -> paginator_scope.DescribeSpotFleetInstancesPaginator:
        """
        [Paginator.DescribeSpotFleetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_spot_fleet_requests"]
    ) -> paginator_scope.DescribeSpotFleetRequestsPaginator:
        """
        [Paginator.DescribeSpotFleetRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_spot_instance_requests"]
    ) -> paginator_scope.DescribeSpotInstanceRequestsPaginator:
        """
        [Paginator.DescribeSpotInstanceRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_spot_price_history"]
    ) -> paginator_scope.DescribeSpotPriceHistoryPaginator:
        """
        [Paginator.DescribeSpotPriceHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_stale_security_groups"]
    ) -> paginator_scope.DescribeStaleSecurityGroupsPaginator:
        """
        [Paginator.DescribeStaleSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_subnets"]
    ) -> paginator_scope.DescribeSubnetsPaginator:
        """
        [Paginator.DescribeSubnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSubnets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_tags"]
    ) -> paginator_scope.DescribeTagsPaginator:
        """
        [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTags)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_filters"]
    ) -> paginator_scope.DescribeTrafficMirrorFiltersPaginator:
        """
        [Paginator.DescribeTrafficMirrorFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_sessions"]
    ) -> paginator_scope.DescribeTrafficMirrorSessionsPaginator:
        """
        [Paginator.DescribeTrafficMirrorSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_targets"]
    ) -> paginator_scope.DescribeTrafficMirrorTargetsPaginator:
        """
        [Paginator.DescribeTrafficMirrorTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_attachments"]
    ) -> paginator_scope.DescribeTransitGatewayAttachmentsPaginator:
        """
        [Paginator.DescribeTransitGatewayAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_route_tables"]
    ) -> paginator_scope.DescribeTransitGatewayRouteTablesPaginator:
        """
        [Paginator.DescribeTransitGatewayRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_vpc_attachments"]
    ) -> paginator_scope.DescribeTransitGatewayVpcAttachmentsPaginator:
        """
        [Paginator.DescribeTransitGatewayVpcAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateways"]
    ) -> paginator_scope.DescribeTransitGatewaysPaginator:
        """
        [Paginator.DescribeTransitGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_volume_status"]
    ) -> paginator_scope.DescribeVolumeStatusPaginator:
        """
        [Paginator.DescribeVolumeStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_volumes"]
    ) -> paginator_scope.DescribeVolumesPaginator:
        """
        [Paginator.DescribeVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVolumes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_volumes_modifications"]
    ) -> paginator_scope.DescribeVolumesModificationsPaginator:
        """
        [Paginator.DescribeVolumesModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_vpc_classic_link_dns_support"]
    ) -> paginator_scope.DescribeVpcClassicLinkDnsSupportPaginator:
        """
        [Paginator.DescribeVpcClassicLinkDnsSupport documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_connection_notifications"]
    ) -> paginator_scope.DescribeVpcEndpointConnectionNotificationsPaginator:
        """
        [Paginator.DescribeVpcEndpointConnectionNotifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_connections"]
    ) -> paginator_scope.DescribeVpcEndpointConnectionsPaginator:
        """
        [Paginator.DescribeVpcEndpointConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_service_configurations"]
    ) -> paginator_scope.DescribeVpcEndpointServiceConfigurationsPaginator:
        """
        [Paginator.DescribeVpcEndpointServiceConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_service_permissions"]
    ) -> paginator_scope.DescribeVpcEndpointServicePermissionsPaginator:
        """
        [Paginator.DescribeVpcEndpointServicePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_services"]
    ) -> paginator_scope.DescribeVpcEndpointServicesPaginator:
        """
        [Paginator.DescribeVpcEndpointServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoints"]
    ) -> paginator_scope.DescribeVpcEndpointsPaginator:
        """
        [Paginator.DescribeVpcEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_vpc_peering_connections"]
    ) -> paginator_scope.DescribeVpcPeeringConnectionsPaginator:
        """
        [Paginator.DescribeVpcPeeringConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_vpcs"]
    ) -> paginator_scope.DescribeVpcsPaginator:
        """
        [Paginator.DescribeVpcs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_attachment_propagations"]
    ) -> paginator_scope.GetTransitGatewayAttachmentPropagationsPaginator:
        """
        [Paginator.GetTransitGatewayAttachmentPropagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_route_table_associations"]
    ) -> paginator_scope.GetTransitGatewayRouteTableAssociationsPaginator:
        """
        [Paginator.GetTransitGatewayRouteTableAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_route_table_propagations"]
    ) -> paginator_scope.GetTransitGatewayRouteTablePropagationsPaginator:
        """
        [Paginator.GetTransitGatewayRouteTablePropagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["bundle_task_complete"]
    ) -> waiter_scope.BundleTaskCompleteWaiter:
        """
        [Waiter.BundleTaskComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.BundleTaskComplete)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["conversion_task_cancelled"]
    ) -> waiter_scope.ConversionTaskCancelledWaiter:
        """
        [Waiter.ConversionTaskCancelled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.ConversionTaskCancelled)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["conversion_task_completed"]
    ) -> waiter_scope.ConversionTaskCompletedWaiter:
        """
        [Waiter.ConversionTaskCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.ConversionTaskCompleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["conversion_task_deleted"]
    ) -> waiter_scope.ConversionTaskDeletedWaiter:
        """
        [Waiter.ConversionTaskDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.ConversionTaskDeleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["customer_gateway_available"]
    ) -> waiter_scope.CustomerGatewayAvailableWaiter:
        """
        [Waiter.CustomerGatewayAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.CustomerGatewayAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["export_task_cancelled"]
    ) -> waiter_scope.ExportTaskCancelledWaiter:
        """
        [Waiter.ExportTaskCancelled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.ExportTaskCancelled)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["export_task_completed"]
    ) -> waiter_scope.ExportTaskCompletedWaiter:
        """
        [Waiter.ExportTaskCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.ExportTaskCompleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["image_available"]
    ) -> waiter_scope.ImageAvailableWaiter:
        """
        [Waiter.ImageAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.ImageAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: Literal["image_exists"]) -> waiter_scope.ImageExistsWaiter:
        """
        [Waiter.ImageExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.ImageExists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["instance_exists"]
    ) -> waiter_scope.InstanceExistsWaiter:
        """
        [Waiter.InstanceExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.InstanceExists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["instance_running"]
    ) -> waiter_scope.InstanceRunningWaiter:
        """
        [Waiter.InstanceRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.InstanceRunning)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["instance_status_ok"]
    ) -> waiter_scope.InstanceStatusOkWaiter:
        """
        [Waiter.InstanceStatusOk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.InstanceStatusOk)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["instance_stopped"]
    ) -> waiter_scope.InstanceStoppedWaiter:
        """
        [Waiter.InstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.InstanceStopped)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["instance_terminated"]
    ) -> waiter_scope.InstanceTerminatedWaiter:
        """
        [Waiter.InstanceTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.InstanceTerminated)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["key_pair_exists"]
    ) -> waiter_scope.KeyPairExistsWaiter:
        """
        [Waiter.KeyPairExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.KeyPairExists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["nat_gateway_available"]
    ) -> waiter_scope.NatGatewayAvailableWaiter:
        """
        [Waiter.NatGatewayAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.NatGatewayAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["network_interface_available"]
    ) -> waiter_scope.NetworkInterfaceAvailableWaiter:
        """
        [Waiter.NetworkInterfaceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.NetworkInterfaceAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["password_data_available"]
    ) -> waiter_scope.PasswordDataAvailableWaiter:
        """
        [Waiter.PasswordDataAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.PasswordDataAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["security_group_exists"]
    ) -> waiter_scope.SecurityGroupExistsWaiter:
        """
        [Waiter.SecurityGroupExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.SecurityGroupExists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["snapshot_completed"]
    ) -> waiter_scope.SnapshotCompletedWaiter:
        """
        [Waiter.SnapshotCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.SnapshotCompleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["spot_instance_request_fulfilled"]
    ) -> waiter_scope.SpotInstanceRequestFulfilledWaiter:
        """
        [Waiter.SpotInstanceRequestFulfilled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.SpotInstanceRequestFulfilled)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["subnet_available"]
    ) -> waiter_scope.SubnetAvailableWaiter:
        """
        [Waiter.SubnetAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.SubnetAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["system_status_ok"]
    ) -> waiter_scope.SystemStatusOkWaiter:
        """
        [Waiter.SystemStatusOk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.SystemStatusOk)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["volume_available"]
    ) -> waiter_scope.VolumeAvailableWaiter:
        """
        [Waiter.VolumeAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.VolumeAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["volume_deleted"]
    ) -> waiter_scope.VolumeDeletedWaiter:
        """
        [Waiter.VolumeDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.VolumeDeleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: Literal["volume_in_use"]) -> waiter_scope.VolumeInUseWaiter:
        """
        [Waiter.VolumeInUse documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.VolumeInUse)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: Literal["vpc_available"]) -> waiter_scope.VpcAvailableWaiter:
        """
        [Waiter.VpcAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.VpcAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: Literal["vpc_exists"]) -> waiter_scope.VpcExistsWaiter:
        """
        [Waiter.VpcExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.VpcExists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["vpc_peering_connection_deleted"]
    ) -> waiter_scope.VpcPeeringConnectionDeletedWaiter:
        """
        [Waiter.VpcPeeringConnectionDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionDeleted)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["vpc_peering_connection_exists"]
    ) -> waiter_scope.VpcPeeringConnectionExistsWaiter:
        """
        [Waiter.VpcPeeringConnectionExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionExists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["vpn_connection_available"]
    ) -> waiter_scope.VpnConnectionAvailableWaiter:
        """
        [Waiter.VpnConnectionAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.VpnConnectionAvailable)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["vpn_connection_deleted"]
    ) -> waiter_scope.VpnConnectionDeletedWaiter:
        """
        [Waiter.VpnConnectionDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Waiter.VpnConnectionDeleted)
        """


class Exceptions:
    ClientError: Boto3ClientError
