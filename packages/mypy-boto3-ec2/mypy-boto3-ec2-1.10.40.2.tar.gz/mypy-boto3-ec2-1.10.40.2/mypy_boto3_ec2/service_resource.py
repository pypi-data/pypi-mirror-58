"Main interface for ec2 service ServiceResource"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, IO, List, Union
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_ec2.service_resource as service_resource_scope
from mypy_boto3_ec2.type_defs import (
    AcceptVpcPeeringConnectionResultTypeDef,
    AssignPrivateIpAddressesResultTypeDef,
    AssociateAddressResultTypeDef,
    AssociateRouteTableResultTypeDef,
    AttachClassicLinkVpcResultTypeDef,
    AttachNetworkInterfaceResultTypeDef,
    AttributeBooleanValueTypeDef,
    AttributeValueTypeDef,
    BlobAttributeValueTypeDef,
    BlockDeviceMappingTypeDef,
    CapacityReservationSpecificationTypeDef,
    CopySnapshotResultTypeDef,
    CpuOptionsRequestTypeDef,
    CreateDhcpOptionsResultTypeDef,
    CreateImageResultTypeDef,
    CreateInternetGatewayResultTypeDef,
    CreateNetworkAclResultTypeDef,
    CreateNetworkInterfaceResultTypeDef,
    CreateRouteResultTypeDef,
    CreateRouteTableResultTypeDef,
    CreateSecurityGroupResultTypeDef,
    CreateSubnetResultTypeDef,
    CreateVolumePermissionModificationsTypeDef,
    CreateVpcPeeringConnectionResultTypeDef,
    CreateVpcResultTypeDef,
    CreditSpecificationRequestTypeDef,
    DeleteVpcPeeringConnectionResultTypeDef,
    DescribeNetworkInterfaceAttributeResultTypeDef,
    DescribeSnapshotAttributeResultTypeDef,
    DescribeVolumeAttributeResultTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcAttributeResultTypeDef,
    DetachClassicLinkVpcResultTypeDef,
    DisableVpcClassicLinkResultTypeDef,
    ElasticGpuSpecificationTypeDef,
    ElasticInferenceAcceleratorTypeDef,
    EnableVpcClassicLinkResultTypeDef,
    FilterTypeDef,
    GetConsoleOutputResultTypeDef,
    GetPasswordDataResultTypeDef,
    HibernationOptionsRequestTypeDef,
    IamInstanceProfileSpecificationTypeDef,
    IcmpTypeCodeTypeDef,
    ImageAttributeTypeDef,
    ImportKeyPairResultTypeDef,
    InstanceAttributeTypeDef,
    InstanceBlockDeviceMappingSpecificationTypeDef,
    InstanceIpv6AddressTypeDef,
    InstanceMarketOptionsRequestTypeDef,
    InstanceMetadataOptionsRequestTypeDef,
    InstanceNetworkInterfaceSpecificationTypeDef,
    IpPermissionTypeDef,
    KeyPairTypeDef,
    LaunchPermissionModificationsTypeDef,
    LaunchTemplateSpecificationTypeDef,
    LicenseConfigurationRequestTypeDef,
    MonitorInstancesResultTypeDef,
    NetworkInterfaceAttachmentChangesTypeDef,
    NewDhcpConfigurationTypeDef,
    PlacementTypeDef,
    PortRangeTypeDef,
    PrivateIpAddressSpecificationTypeDef,
    RegisterImageResultTypeDef,
    RejectVpcPeeringConnectionResultTypeDef,
    ReplaceNetworkAclAssociationResultTypeDef,
    ReplaceRouteTableAssociationResultTypeDef,
    ReservationTypeDef,
    RunInstancesMonitoringEnabledTypeDef,
    SnapshotTypeDef,
    StartInstancesResultTypeDef,
    StopInstancesResultTypeDef,
    TagSpecificationTypeDef,
    TagTypeDef,
    TerminateInstancesResultTypeDef,
    UnmonitorInstancesResultTypeDef,
    VolumeAttachmentTypeDef,
    VolumeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "EC2ServiceResource",
    "ClassicAddress",
    "DhcpOptions",
    "Image",
    "Instance",
    "InternetGateway",
    "KeyPair",
    "KeyPairInfo",
    "NetworkAcl",
    "NetworkInterface",
    "NetworkInterfaceAssociation",
    "PlacementGroup",
    "Route",
    "RouteTable",
    "RouteTableAssociation",
    "SecurityGroup",
    "Snapshot",
    "Subnet",
    "Tag",
    "Volume",
    "Vpc",
    "VpcPeeringConnection",
    "VpcAddress",
    "ServiceResourceClassicAddressesCollection",
    "ServiceResourceDhcpOptionsSetsCollection",
    "ServiceResourceImagesCollection",
    "ServiceResourceInstancesCollection",
    "ServiceResourceInternetGatewaysCollection",
    "ServiceResourceKeyPairsCollection",
    "ServiceResourceNetworkAclsCollection",
    "ServiceResourceNetworkInterfacesCollection",
    "ServiceResourcePlacementGroupsCollection",
    "ServiceResourceRouteTablesCollection",
    "ServiceResourceSecurityGroupsCollection",
    "ServiceResourceSnapshotsCollection",
    "ServiceResourceSubnetsCollection",
    "ServiceResourceVolumesCollection",
    "ServiceResourceVpcAddressesCollection",
    "ServiceResourceVpcPeeringConnectionsCollection",
    "ServiceResourceVpcsCollection",
    "InstanceVolumesCollection",
    "InstanceVpcAddressesCollection",
    "PlacementGroupInstancesCollection",
    "SubnetInstancesCollection",
    "SubnetNetworkInterfacesCollection",
    "VolumeSnapshotsCollection",
    "VpcAcceptedVpcPeeringConnectionsCollection",
    "VpcInstancesCollection",
    "VpcInternetGatewaysCollection",
    "VpcNetworkAclsCollection",
    "VpcNetworkInterfacesCollection",
    "VpcRequestedVpcPeeringConnectionsCollection",
    "VpcRouteTablesCollection",
    "VpcSecurityGroupsCollection",
    "VpcSubnetsCollection",
)


class EC2ServiceResource(Boto3ServiceResource):
    """
    [EC2.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource)
    """

    classic_addresses: service_resource_scope.ServiceResourceClassicAddressesCollection
    dhcp_options_sets: service_resource_scope.ServiceResourceDhcpOptionsSetsCollection
    images: service_resource_scope.ServiceResourceImagesCollection
    instances: service_resource_scope.ServiceResourceInstancesCollection
    internet_gateways: service_resource_scope.ServiceResourceInternetGatewaysCollection
    key_pairs: service_resource_scope.ServiceResourceKeyPairsCollection
    network_acls: service_resource_scope.ServiceResourceNetworkAclsCollection
    network_interfaces: service_resource_scope.ServiceResourceNetworkInterfacesCollection
    placement_groups: service_resource_scope.ServiceResourcePlacementGroupsCollection
    route_tables: service_resource_scope.ServiceResourceRouteTablesCollection
    security_groups: service_resource_scope.ServiceResourceSecurityGroupsCollection
    snapshots: service_resource_scope.ServiceResourceSnapshotsCollection
    subnets: service_resource_scope.ServiceResourceSubnetsCollection
    volumes: service_resource_scope.ServiceResourceVolumesCollection
    vpc_addresses: service_resource_scope.ServiceResourceVpcAddressesCollection
    vpc_peering_connections: service_resource_scope.ServiceResourceVpcPeeringConnectionsCollection
    vpcs: service_resource_scope.ServiceResourceVpcsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def ClassicAddress(self, public_ip: str) -> service_resource_scope.ClassicAddress:
        """
        [ServiceResource.ClassicAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def DhcpOptions(self, id: str) -> service_resource_scope.DhcpOptions:
        """
        [ServiceResource.DhcpOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Image(self, id: str) -> service_resource_scope.Image:
        """
        [ServiceResource.Image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Instance(self, id: str) -> service_resource_scope.Instance:
        """
        [ServiceResource.Instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def InternetGateway(self, id: str) -> service_resource_scope.InternetGateway:
        """
        [ServiceResource.InternetGateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def KeyPair(self, name: str) -> service_resource_scope.KeyPairInfo:
        """
        [ServiceResource.KeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.KeyPair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def NetworkAcl(self, id: str) -> service_resource_scope.NetworkAcl:
        """
        [ServiceResource.NetworkAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def NetworkInterface(self, id: str) -> service_resource_scope.NetworkInterface:
        """
        [ServiceResource.NetworkInterface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def NetworkInterfaceAssociation(
        self, id: str
    ) -> service_resource_scope.NetworkInterfaceAssociation:
        """
        [ServiceResource.NetworkInterfaceAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def PlacementGroup(self, name: str) -> service_resource_scope.PlacementGroup:
        """
        [ServiceResource.PlacementGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Route(
        self, route_table_id: str, destination_cidr_block: str
    ) -> service_resource_scope.Route:
        """
        [ServiceResource.Route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def RouteTable(self, id: str) -> service_resource_scope.RouteTable:
        """
        [ServiceResource.RouteTable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.RouteTable)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def RouteTableAssociation(self, id: str) -> service_resource_scope.RouteTableAssociation:
        """
        [ServiceResource.RouteTableAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def SecurityGroup(self, id: str) -> service_resource_scope.SecurityGroup:
        """
        [ServiceResource.SecurityGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Snapshot(self, id: str) -> service_resource_scope.Snapshot:
        """
        [ServiceResource.Snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Subnet(self, id: str) -> service_resource_scope.Subnet:
        """
        [ServiceResource.Subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Subnet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Tag(self, resource_id: str, key: str, value: str) -> service_resource_scope.Tag:
        """
        [ServiceResource.Tag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Tag)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Volume(self, id: str) -> service_resource_scope.Volume:
        """
        [ServiceResource.Volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Vpc(self, id: str) -> service_resource_scope.Vpc:
        """
        [ServiceResource.Vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def VpcAddress(self, allocation_id: str) -> service_resource_scope.VpcAddress:
        """
        [ServiceResource.VpcAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def VpcPeeringConnection(self, id: str) -> service_resource_scope.VpcPeeringConnection:
        """
        [ServiceResource.VpcPeeringConnection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dhcp_options(
        self, DhcpConfigurations: List[NewDhcpConfigurationTypeDef], DryRun: bool = None
    ) -> CreateDhcpOptionsResultTypeDef:
        """
        [ServiceResource.create_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_dhcp_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instances(
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
        [ServiceResource.create_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_internet_gateway(self, DryRun: bool = None) -> CreateInternetGatewayResultTypeDef:
        """
        [ServiceResource.create_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_internet_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_key_pair(self, KeyName: str, DryRun: bool = None) -> KeyPairTypeDef:
        """
        [ServiceResource.create_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_acl(self, VpcId: str, DryRun: bool = None) -> CreateNetworkAclResultTypeDef:
        """
        [ServiceResource.create_network_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_network_acl)
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
        [ServiceResource.create_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_network_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_placement_group(
        self,
        DryRun: bool = None,
        GroupName: str = None,
        Strategy: Literal["cluster", "spread", "partition"] = None,
        PartitionCount: int = None,
    ) -> service_resource_scope.PlacementGroup:
        """
        [ServiceResource.create_placement_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_placement_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_route_table(self, VpcId: str, DryRun: bool = None) -> CreateRouteTableResultTypeDef:
        """
        [ServiceResource.create_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_security_group(
        self, Description: str, GroupName: str, VpcId: str = None, DryRun: bool = None
    ) -> CreateSecurityGroupResultTypeDef:
        """
        [ServiceResource.create_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_security_group)
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
        [ServiceResource.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_snapshot)
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
        [ServiceResource.create_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_subnet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> None:
        """
        [ServiceResource.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_tags)
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
        [ServiceResource.create_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_volume)
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
        [ServiceResource.create_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_vpc)
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
        [ServiceResource.create_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.create_vpc_peering_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_route_table(self, AssociationId: str, DryRun: bool = None) -> None:
        """
        [ServiceResource.disassociate_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.disassociate_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_key_pair(
        self, KeyName: str, PublicKeyMaterial: Union[bytes, IO], DryRun: bool = None
    ) -> ImportKeyPairResultTypeDef:
        """
        [ServiceResource.import_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.import_key_pair)
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
        [ServiceResource.register_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.register_image)
        """


class ClassicAddress(Boto3ServiceResource):
    """
    [ClassicAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)
    """

    instance_id: str
    allocation_id: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List[Any]
    public_ipv4_pool: str
    network_border_group: str
    customer_owned_ip: str
    customer_owned_ipv4_pool: str
    public_ip: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate(
        self,
        AllocationId: str = None,
        InstanceId: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None,
    ) -> AssociateAddressResultTypeDef:
        """
        [ClassicAddress.associate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ClassicAddress.associate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate(
        self, AssociationId: str = None, PublicIp: str = None, DryRun: bool = None
    ) -> None:
        """
        [ClassicAddress.disassociate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ClassicAddress.disassociate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ClassicAddress.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ClassicAddress.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [ClassicAddress.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ClassicAddress.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def release(
        self,
        AllocationId: str = None,
        PublicIp: str = None,
        NetworkBorderGroup: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [ClassicAddress.release documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ClassicAddress.release)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [ClassicAddress.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ClassicAddress.reload)
        """


class DhcpOptions(Boto3ServiceResource):
    """
    [DhcpOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)
    """

    dhcp_configurations: List[Any]
    dhcp_options_id: str
    owner_id: str
    tags: List[Any]
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_with_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        """
        [DhcpOptions.associate_with_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.DhcpOptions.associate_with_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [DhcpOptions.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [DhcpOptions.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.DhcpOptions.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [DhcpOptions.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.DhcpOptions.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [DhcpOptions.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.DhcpOptions.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [DhcpOptions.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.DhcpOptions.reload)
        """


class Image(Boto3ServiceResource):
    """
    [Image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Image)
    """

    architecture: str
    creation_date: str
    image_id: str
    image_location: str
    image_type: str
    public: bool
    kernel_id: str
    owner_id: str
    platform: str
    product_codes: List[Any]
    ramdisk_id: str
    state: str
    block_device_mappings: List[Any]
    description: str
    ena_support: bool
    hypervisor: str
    image_owner_alias: str
    name: str
    root_device_name: str
    root_device_type: str
    sriov_net_support: str
    state_reason: Dict[str, Any]
    tags: List[Any]
    virtualization_type: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [Image.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Image.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister(self, DryRun: bool = None) -> None:
        """
        [Image.deregister documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Image.deregister)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
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
        DryRun: bool = None,
    ) -> ImageAttributeTypeDef:
        """
        [Image.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Image.describe_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Image.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Image.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Image.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Image.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self,
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
        [Image.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Image.modify_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Image.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Image.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_attribute(self, Attribute: Literal["launchPermission"], DryRun: bool = None) -> None:
        """
        [Image.reset_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Image.reset_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(self) -> None:
        """
        [Image.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Image.wait_until_exists)
        """


class Instance(Boto3ServiceResource):
    """
    [Instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Instance)
    """

    ami_launch_index: int
    image_id: str
    instance_id: str
    instance_type: str
    kernel_id: str
    key_name: str
    launch_time: datetime
    monitoring: Dict[str, Any]
    placement: Dict[str, Any]
    platform: str
    private_dns_name: str
    private_ip_address: str
    product_codes: List[Any]
    public_dns_name: str
    public_ip_address: str
    ramdisk_id: str
    state: Dict[str, Any]
    state_transition_reason: str
    subnet_id: str
    vpc_id: str
    architecture: str
    block_device_mappings: List[Any]
    client_token: str
    ebs_optimized: bool
    ena_support: bool
    hypervisor: str
    iam_instance_profile: Dict[str, Any]
    instance_lifecycle: str
    elastic_gpu_associations: List[Any]
    elastic_inference_accelerator_associations: List[Any]
    network_interfaces_attribute: List[Any]
    outpost_arn: str
    root_device_name: str
    root_device_type: str
    security_groups: List[Any]
    source_dest_check: bool
    spot_instance_request_id: str
    sriov_net_support: str
    state_reason: Dict[str, Any]
    tags: List[Any]
    virtualization_type: str
    cpu_options: Dict[str, Any]
    capacity_reservation_id: str
    capacity_reservation_specification: Dict[str, Any]
    hibernation_options: Dict[str, Any]
    licenses: List[Any]
    metadata_options: Dict[str, Any]
    id: str
    volumes: service_resource_scope.InstanceVolumesCollection
    vpc_addresses: service_resource_scope.InstanceVpcAddressesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_classic_link_vpc(
        self, Groups: List[str], VpcId: str, DryRun: bool = None
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        [Instance.attach_classic_link_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.attach_classic_link_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_volume(
        self, Device: str, VolumeId: str, DryRun: bool = None
    ) -> VolumeAttachmentTypeDef:
        """
        [Instance.attach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.attach_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def console_output(
        self, DryRun: bool = None, Latest: bool = None
    ) -> GetConsoleOutputResultTypeDef:
        """
        [Instance.console_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.console_output)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_image(
        self,
        Name: str,
        BlockDeviceMappings: List[BlockDeviceMappingTypeDef] = None,
        Description: str = None,
        DryRun: bool = None,
        NoReboot: bool = None,
    ) -> CreateImageResultTypeDef:
        """
        [Instance.create_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.create_image)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [Instance.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tags(
        Resources: List[Any], Tags: List[TagTypeDef] = None, DryRun: bool = None
    ) -> None:
        """
        [Instance.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.delete_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
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
        DryRun: bool = None,
    ) -> InstanceAttributeTypeDef:
        """
        [Instance.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.describe_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_classic_link_vpc(
        self, VpcId: str, DryRun: bool = None
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        [Instance.detach_classic_link_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.detach_classic_link_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_volume(
        self, VolumeId: str, Device: str = None, Force: bool = None, DryRun: bool = None
    ) -> VolumeAttachmentTypeDef:
        """
        [Instance.detach_volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.detach_volume)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Instance.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Instance.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self,
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
        [Instance.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.modify_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def monitor(self, InstanceIds: List[str], DryRun: bool = None) -> MonitorInstancesResultTypeDef:
        """
        [Instance.monitor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.monitor)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def password_data(self, DryRun: bool = None) -> GetPasswordDataResultTypeDef:
        """
        [Instance.password_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.password_data)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot(self, InstanceIds: List[str], DryRun: bool = None) -> None:
        """
        [Instance.reboot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.reboot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Instance.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def report_status(
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
        [Instance.report_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.report_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_attribute(
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
        DryRun: bool = None,
    ) -> None:
        """
        [Instance.reset_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.reset_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_kernel(
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
        DryRun: bool = None,
    ) -> None:
        """
        [Instance.reset_kernel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.reset_kernel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_ramdisk(
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
        DryRun: bool = None,
    ) -> None:
        """
        [Instance.reset_ramdisk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.reset_ramdisk)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_source_dest_check(
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
        DryRun: bool = None,
    ) -> None:
        """
        [Instance.reset_source_dest_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.reset_source_dest_check)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start(
        self, InstanceIds: List[str], AdditionalInfo: str = None, DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        """
        [Instance.start documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.start)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop(
        self,
        InstanceIds: List[str],
        Hibernate: bool = None,
        DryRun: bool = None,
        Force: bool = None,
    ) -> StopInstancesResultTypeDef:
        """
        [Instance.stop documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.stop)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def terminate(
        self, InstanceIds: List[str], DryRun: bool = None
    ) -> TerminateInstancesResultTypeDef:
        """
        [Instance.terminate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.terminate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unmonitor(
        self, InstanceIds: List[str], DryRun: bool = None
    ) -> UnmonitorInstancesResultTypeDef:
        """
        [Instance.unmonitor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.unmonitor)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(self) -> None:
        """
        [Instance.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.wait_until_exists)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_running(self) -> None:
        """
        [Instance.wait_until_running documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.wait_until_running)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_stopped(self) -> None:
        """
        [Instance.wait_until_stopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.wait_until_stopped)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_terminated(self) -> None:
        """
        [Instance.wait_until_terminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.wait_until_terminated)
        """


class InternetGateway(Boto3ServiceResource):
    """
    [InternetGateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)
    """

    attachments: List[Any]
    internet_gateway_id: str
    owner_id: str
    tags: List[Any]
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_to_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        """
        [InternetGateway.attach_to_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.InternetGateway.attach_to_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [InternetGateway.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [InternetGateway.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.InternetGateway.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_from_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        """
        [InternetGateway.detach_from_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.InternetGateway.detach_from_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [InternetGateway.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.InternetGateway.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [InternetGateway.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.InternetGateway.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [InternetGateway.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.InternetGateway.reload)
        """


class KeyPair(Boto3ServiceResource):
    """
    [KeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.KeyPair)
    """

    key_fingerprint: str
    key_material: str
    key_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [KeyPair.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.KeyPair.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [KeyPair.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.KeyPair.get_available_subresources)
        """


class KeyPairInfo(Boto3ServiceResource):
    """
    [KeyPairInfo documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.KeyPairInfo)
    """

    key_fingerprint: str
    key_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [KeyPairInfo.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.KeyPairInfo.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [KeyPairInfo.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.KeyPairInfo.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [KeyPairInfo.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.KeyPairInfo.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [KeyPairInfo.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.KeyPairInfo.reload)
        """


class NetworkAcl(Boto3ServiceResource):
    """
    [NetworkAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)
    """

    associations: List[Any]
    entries: List[Any]
    is_default: bool
    network_acl_id: str
    tags: List[Any]
    vpc_id: str
    owner_id: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_entry(
        self,
        Egress: bool,
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
        [NetworkAcl.create_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkAcl.create_entry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [NetworkAcl.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [NetworkAcl.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkAcl.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_entry(self, Egress: bool, RuleNumber: int, DryRun: bool = None) -> None:
        """
        [NetworkAcl.delete_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkAcl.delete_entry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [NetworkAcl.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkAcl.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [NetworkAcl.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkAcl.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [NetworkAcl.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkAcl.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_association(
        self, AssociationId: str, DryRun: bool = None
    ) -> ReplaceNetworkAclAssociationResultTypeDef:
        """
        [NetworkAcl.replace_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkAcl.replace_association)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_entry(
        self,
        Egress: bool,
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
        [NetworkAcl.replace_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkAcl.replace_entry)
        """


class NetworkInterface(Boto3ServiceResource):
    """
    [NetworkInterface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)
    """

    association_attribute: Dict[str, Any]
    attachment: Dict[str, Any]
    availability_zone: str
    description: str
    groups: List[Any]
    interface_type: str
    ipv6_addresses: List[Any]
    mac_address: str
    network_interface_id: str
    outpost_arn: str
    owner_id: str
    private_dns_name: str
    private_ip_address: str
    private_ip_addresses: List[Any]
    requester_id: str
    requester_managed: bool
    source_dest_check: bool
    status: str
    subnet_id: str
    tag_set: List[Any]
    vpc_id: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assign_private_ip_addresses(
        self,
        AllowReassignment: bool = None,
        PrivateIpAddresses: List[str] = None,
        SecondaryPrivateIpAddressCount: int = None,
    ) -> AssignPrivateIpAddressesResultTypeDef:
        """
        [NetworkInterface.assign_private_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.assign_private_ip_addresses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach(
        self, DeviceIndex: int, InstanceId: str, DryRun: bool = None
    ) -> AttachNetworkInterfaceResultTypeDef:
        """
        [NetworkInterface.attach documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.attach)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [NetworkInterface.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [NetworkInterface.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
        self,
        Attribute: Literal["description", "groupSet", "sourceDestCheck", "attachment"] = None,
        DryRun: bool = None,
    ) -> DescribeNetworkInterfaceAttributeResultTypeDef:
        """
        [NetworkInterface.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.describe_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach(self, AttachmentId: str, DryRun: bool = None, Force: bool = None) -> None:
        """
        [NetworkInterface.detach documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.detach)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [NetworkInterface.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [NetworkInterface.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self,
        Attachment: NetworkInterfaceAttachmentChangesTypeDef = None,
        Description: AttributeValueTypeDef = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        SourceDestCheck: AttributeBooleanValueTypeDef = None,
    ) -> None:
        """
        [NetworkInterface.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.modify_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [NetworkInterface.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_attribute(self, DryRun: bool = None, SourceDestCheck: str = None) -> None:
        """
        [NetworkInterface.reset_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.reset_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unassign_private_ip_addresses(self, PrivateIpAddresses: List[str]) -> None:
        """
        [NetworkInterface.unassign_private_ip_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterface.unassign_private_ip_addresses)
        """


class NetworkInterfaceAssociation(Boto3ServiceResource):
    """
    [NetworkInterfaceAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)
    """

    ip_owner_id: str
    public_dns_name: str
    public_ip: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, PublicIp: str = None, DryRun: bool = None) -> None:
        """
        [NetworkInterfaceAssociation.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [NetworkInterfaceAssociation.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [NetworkInterfaceAssociation.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [NetworkInterfaceAssociation.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.reload)
        """


class PlacementGroup(Boto3ServiceResource):
    """
    [PlacementGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)
    """

    group_name: str
    state: str
    strategy: str
    partition_count: int
    name: str
    instances: service_resource_scope.PlacementGroupInstancesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [PlacementGroup.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.PlacementGroup.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [PlacementGroup.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.PlacementGroup.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [PlacementGroup.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.PlacementGroup.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [PlacementGroup.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.PlacementGroup.reload)
        """


class Route(Boto3ServiceResource):
    """
    [Route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Route)
    """

    destination_ipv6_cidr_block: str
    destination_prefix_list_id: str
    egress_only_internet_gateway_id: str
    gateway_id: str
    instance_id: str
    instance_owner_id: str
    nat_gateway_id: str
    transit_gateway_id: str
    local_gateway_id: str
    network_interface_id: str
    origin: str
    state: str
    vpc_peering_connection_id: str
    route_table_id: str
    destination_cidr_block: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DestinationIpv6CidrBlock: str = None, DryRun: bool = None) -> None:
        """
        [Route.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Route.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Route.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Route.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace(
        self,
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
        [Route.replace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Route.replace)
        """


class RouteTable(Boto3ServiceResource):
    """
    [RouteTable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.RouteTable)
    """

    associations_attribute: List[Any]
    propagating_vgws: List[Any]
    route_table_id: str
    routes_attribute: List[Any]
    tags: List[Any]
    vpc_id: str
    owner_id: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_with_subnet(
        self, DryRun: bool = None, SubnetId: str = None, GatewayId: str = None
    ) -> AssociateRouteTableResultTypeDef:
        """
        [RouteTable.associate_with_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.RouteTable.associate_with_subnet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_route(
        self,
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
        [RouteTable.create_route documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.RouteTable.create_route)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [RouteTable.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.RouteTable.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [RouteTable.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.RouteTable.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [RouteTable.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.RouteTable.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [RouteTable.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.RouteTable.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [RouteTable.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.RouteTable.reload)
        """


class RouteTableAssociation(Boto3ServiceResource):
    """
    [RouteTableAssociation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)
    """

    main: bool
    route_table_association_id: str
    route_table_id: str
    subnet_id: str
    gateway_id: str
    association_state: Dict[str, Any]
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [RouteTableAssociation.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.RouteTableAssociation.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [RouteTableAssociation.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.RouteTableAssociation.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def replace_subnet(
        self, RouteTableId: str, DryRun: bool = None
    ) -> ReplaceRouteTableAssociationResultTypeDef:
        """
        [RouteTableAssociation.replace_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.RouteTableAssociation.replace_subnet)
        """


class SecurityGroup(Boto3ServiceResource):
    """
    [SecurityGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)
    """

    description: str
    group_name: str
    ip_permissions: List[Any]
    owner_id: str
    group_id: str
    ip_permissions_egress: List[Any]
    tags: List[Any]
    vpc_id: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_egress(
        self,
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
        [SecurityGroup.authorize_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.SecurityGroup.authorize_egress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def authorize_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupName: str = None,
        IpPermissions: List[IpPermissionTypeDef] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> None:
        """
        [SecurityGroup.authorize_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.SecurityGroup.authorize_ingress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [SecurityGroup.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, GroupName: str = None, DryRun: bool = None) -> None:
        """
        [SecurityGroup.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.SecurityGroup.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [SecurityGroup.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.SecurityGroup.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [SecurityGroup.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.SecurityGroup.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [SecurityGroup.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.SecurityGroup.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_egress(
        self,
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
        [SecurityGroup.revoke_egress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.SecurityGroup.revoke_egress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupName: str = None,
        IpPermissions: List[IpPermissionTypeDef] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> None:
        """
        [SecurityGroup.revoke_ingress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.SecurityGroup.revoke_ingress)
        """


class Snapshot(Boto3ServiceResource):
    """
    [Snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Snapshot)
    """

    data_encryption_key_id: str
    description: str
    encrypted: bool
    kms_key_id: str
    owner_id: str
    progress: str
    snapshot_id: str
    start_time: datetime
    state: str
    state_message: str
    volume_id: str
    volume_size: int
    owner_alias: str
    tags: List[Any]
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy(
        self,
        SourceRegion: str,
        Description: str = None,
        DestinationRegion: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        PresignedUrl: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
    ) -> CopySnapshotResultTypeDef:
        """
        [Snapshot.copy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Snapshot.copy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [Snapshot.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Snapshot.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [Snapshot.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Snapshot.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
        self, Attribute: Literal["productCodes", "createVolumePermission"], DryRun: bool = None
    ) -> DescribeSnapshotAttributeResultTypeDef:
        """
        [Snapshot.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Snapshot.describe_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Snapshot.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Snapshot.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Snapshot.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Snapshot.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self,
        Attribute: Literal["productCodes", "createVolumePermission"] = None,
        CreateVolumePermission: CreateVolumePermissionModificationsTypeDef = None,
        GroupNames: List[str] = None,
        OperationType: Literal["add", "remove"] = None,
        UserIds: List[str] = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Snapshot.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Snapshot.modify_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Snapshot.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Snapshot.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_attribute(
        self, Attribute: Literal["productCodes", "createVolumePermission"], DryRun: bool = None
    ) -> None:
        """
        [Snapshot.reset_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Snapshot.reset_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_completed(self) -> None:
        """
        [Snapshot.wait_until_completed documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Snapshot.wait_until_completed)
        """


class Subnet(Boto3ServiceResource):
    """
    [Subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Subnet)
    """

    availability_zone: str
    availability_zone_id: str
    available_ip_address_count: int
    cidr_block: str
    default_for_az: bool
    map_public_ip_on_launch: bool
    state: str
    subnet_id: str
    vpc_id: str
    owner_id: str
    assign_ipv6_address_on_creation: bool
    ipv6_cidr_block_association_set: List[Any]
    tags: List[Any]
    subnet_arn: str
    outpost_arn: str
    id: str
    instances: service_resource_scope.SubnetInstancesCollection
    network_interfaces: service_resource_scope.SubnetNetworkInterfacesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instances(
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
        [Subnet.create_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Subnet.create_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_interface(
        self,
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
        [Subnet.create_network_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Subnet.create_network_interface)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [Subnet.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Subnet.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [Subnet.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Subnet.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Subnet.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Subnet.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Subnet.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Subnet.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Subnet.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Subnet.reload)
        """


class Tag(Boto3ServiceResource):
    """
    [Tag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Tag)
    """

    resource_type: str
    resource_id: str
    key: str
    value: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(
        self, Resources: List[str], DryRun: bool = None, Tags: List[TagTypeDef] = None
    ) -> None:
        """
        [Tag.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Tag.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Tag.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Tag.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Tag.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Tag.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Tag.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Tag.reload)
        """


class Volume(Boto3ServiceResource):
    """
    [Volume documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Volume)
    """

    attachments: List[Any]
    availability_zone: str
    create_time: datetime
    encrypted: bool
    kms_key_id: str
    outpost_arn: str
    size: int
    snapshot_id: str
    state: str
    volume_id: str
    iops: int
    tags: List[Any]
    volume_type: str
    fast_restored: bool
    id: str
    snapshots: service_resource_scope.VolumeSnapshotsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_to_instance(
        self, Device: str, InstanceId: str, DryRun: bool = None
    ) -> VolumeAttachmentTypeDef:
        """
        [Volume.attach_to_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.attach_to_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot(
        self,
        Description: str = None,
        TagSpecifications: List[TagSpecificationTypeDef] = None,
        DryRun: bool = None,
    ) -> SnapshotTypeDef:
        """
        [Volume.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.create_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [Volume.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [Volume.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
        self, Attribute: Literal["autoEnableIO", "productCodes"], DryRun: bool = None
    ) -> DescribeVolumeAttributeResultTypeDef:
        """
        [Volume.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.describe_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_status(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeVolumeStatusResultTypeDef:
        """
        [Volume.describe_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.describe_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_from_instance(
        self, Device: str = None, Force: bool = None, InstanceId: str = None, DryRun: bool = None
    ) -> VolumeAttachmentTypeDef:
        """
        [Volume.detach_from_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.detach_from_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_io(self, DryRun: bool = None) -> None:
        """
        [Volume.enable_io documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.enable_io)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Volume.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Volume.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self, AutoEnableIO: AttributeBooleanValueTypeDef = None, DryRun: bool = None
    ) -> None:
        """
        [Volume.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.modify_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Volume.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.reload)
        """


class Vpc(Boto3ServiceResource):
    """
    [Vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.Vpc)
    """

    cidr_block: str
    dhcp_options_id: str
    state: str
    vpc_id: str
    owner_id: str
    instance_tenancy: str
    ipv6_cidr_block_association_set: List[Any]
    cidr_block_association_set: List[Any]
    is_default: bool
    tags: List[Any]
    id: str
    accepted_vpc_peering_connections: service_resource_scope.VpcAcceptedVpcPeeringConnectionsCollection
    instances: service_resource_scope.VpcInstancesCollection
    internet_gateways: service_resource_scope.VpcInternetGatewaysCollection
    network_acls: service_resource_scope.VpcNetworkAclsCollection
    network_interfaces: service_resource_scope.VpcNetworkInterfacesCollection
    requested_vpc_peering_connections: service_resource_scope.VpcRequestedVpcPeeringConnectionsCollection
    route_tables: service_resource_scope.VpcRouteTablesCollection
    security_groups: service_resource_scope.VpcSecurityGroupsCollection
    subnets: service_resource_scope.VpcSubnetsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_dhcp_options(self, DhcpOptionsId: str, DryRun: bool = None) -> None:
        """
        [Vpc.associate_dhcp_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.associate_dhcp_options)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_classic_link_instance(
        self, Groups: List[str], InstanceId: str, DryRun: bool = None
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        [Vpc.attach_classic_link_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.attach_classic_link_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None) -> None:
        """
        [Vpc.attach_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.attach_internet_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_network_acl(self, DryRun: bool = None) -> CreateNetworkAclResultTypeDef:
        """
        [Vpc.create_network_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.create_network_acl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_route_table(self, DryRun: bool = None) -> CreateRouteTableResultTypeDef:
        """
        [Vpc.create_route_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.create_route_table)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_security_group(
        self, Description: str, GroupName: str, DryRun: bool = None
    ) -> CreateSecurityGroupResultTypeDef:
        """
        [Vpc.create_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.create_security_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subnet(
        self,
        CidrBlock: str,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Ipv6CidrBlock: str = None,
        OutpostArn: str = None,
        DryRun: bool = None,
    ) -> CreateSubnetResultTypeDef:
        """
        [Vpc.create_subnet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.create_subnet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tags(
        self, Resources: List[Any], Tags: List[TagTypeDef], DryRun: bool = None
    ) -> service_resource_scope.Tag:
        """
        [Vpc.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.create_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> None:
        """
        [Vpc.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_attribute(
        self, Attribute: Literal["enableDnsSupport", "enableDnsHostnames"], DryRun: bool = None
    ) -> DescribeVpcAttributeResultTypeDef:
        """
        [Vpc.describe_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.describe_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_classic_link_instance(
        self, InstanceId: str, DryRun: bool = None
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        [Vpc.detach_classic_link_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.detach_classic_link_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None) -> None:
        """
        [Vpc.detach_internet_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.detach_internet_gateway)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_classic_link(self, DryRun: bool = None) -> DisableVpcClassicLinkResultTypeDef:
        """
        [Vpc.disable_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.disable_classic_link)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_classic_link(self, DryRun: bool = None) -> EnableVpcClassicLinkResultTypeDef:
        """
        [Vpc.enable_classic_link documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.enable_classic_link)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [Vpc.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [Vpc.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_attribute(
        self,
        EnableDnsHostnames: AttributeBooleanValueTypeDef = None,
        EnableDnsSupport: AttributeBooleanValueTypeDef = None,
    ) -> None:
        """
        [Vpc.modify_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.modify_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [Vpc.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def request_vpc_peering_connection(
        self,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        PeerRegion: str = None,
    ) -> CreateVpcPeeringConnectionResultTypeDef:
        """
        [Vpc.request_vpc_peering_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.request_vpc_peering_connection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_available(self) -> None:
        """
        [Vpc.wait_until_available documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.wait_until_available)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(self) -> None:
        """
        [Vpc.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.wait_until_exists)
        """


class VpcPeeringConnection(Boto3ServiceResource):
    """
    [VpcPeeringConnection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)
    """

    accepter_vpc_info: Dict[str, Any]
    expiration_time: datetime
    requester_vpc_info: Dict[str, Any]
    status: Dict[str, Any]
    tags: List[Any]
    vpc_peering_connection_id: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept(self, DryRun: bool = None) -> AcceptVpcPeeringConnectionResultTypeDef:
        """
        [VpcPeeringConnection.accept documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcPeeringConnection.accept)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, DryRun: bool = None) -> DeleteVpcPeeringConnectionResultTypeDef:
        """
        [VpcPeeringConnection.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcPeeringConnection.delete)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [VpcPeeringConnection.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcPeeringConnection.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [VpcPeeringConnection.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcPeeringConnection.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject(self, DryRun: bool = None) -> RejectVpcPeeringConnectionResultTypeDef:
        """
        [VpcPeeringConnection.reject documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcPeeringConnection.reject)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [VpcPeeringConnection.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcPeeringConnection.reload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(self) -> None:
        """
        [VpcPeeringConnection.wait_until_exists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcPeeringConnection.wait_until_exists)
        """


class VpcAddress(Boto3ServiceResource):
    """
    [VpcAddress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)
    """

    instance_id: str
    public_ip: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List[Any]
    public_ipv4_pool: str
    network_border_group: str
    customer_owned_ip: str
    customer_owned_ipv4_pool: str
    allocation_id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate(
        self,
        InstanceId: str = None,
        PublicIp: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None,
    ) -> AssociateAddressResultTypeDef:
        """
        [VpcAddress.associate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcAddress.associate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [VpcAddress.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcAddress.get_available_subresources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        """
        [VpcAddress.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcAddress.load)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def release(
        self,
        AllocationId: str = None,
        PublicIp: str = None,
        NetworkBorderGroup: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [VpcAddress.release documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcAddress.release)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        """
        [VpcAddress.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.VpcAddress.reload)
        """


class ServiceResourceClassicAddressesCollection(ResourceCollection):
    """
    [ServiceResource.classic_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceClassicAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceClassicAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceClassicAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.ServiceResourceClassicAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.ClassicAddress]:
        pass


class ServiceResourceDhcpOptionsSetsCollection(ResourceCollection):
    """
    [ServiceResource.dhcp_options_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceDhcpOptionsSetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceDhcpOptionsSetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceDhcpOptionsSetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.ServiceResourceDhcpOptionsSetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.DhcpOptions]:
        pass


class ServiceResourceImagesCollection(ResourceCollection):
    """
    [ServiceResource.images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.images)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceImagesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceImagesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceImagesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceImagesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Image]:
        pass


class ServiceResourceInstancesCollection(ResourceCollection):
    """
    [ServiceResource.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.instances)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Instance]:
        pass


class ServiceResourceInternetGatewaysCollection(ResourceCollection):
    """
    [ServiceResource.internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceInternetGatewaysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceInternetGatewaysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceInternetGatewaysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.ServiceResourceInternetGatewaysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.InternetGateway]:
        pass


class ServiceResourceKeyPairsCollection(ResourceCollection):
    """
    [ServiceResource.key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceKeyPairsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceKeyPairsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceKeyPairsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceKeyPairsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.KeyPairInfo]:
        pass


class ServiceResourceNetworkAclsCollection(ResourceCollection):
    """
    [ServiceResource.network_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.network_acls)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceNetworkAclsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceNetworkAclsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceNetworkAclsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceNetworkAclsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.NetworkAcl]:
        pass


class ServiceResourceNetworkInterfacesCollection(ResourceCollection):
    """
    [ServiceResource.network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.ServiceResourceNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.NetworkInterface]:
        pass


class ServiceResourcePlacementGroupsCollection(ResourceCollection):
    """
    [ServiceResource.placement_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourcePlacementGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourcePlacementGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourcePlacementGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.ServiceResourcePlacementGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.PlacementGroup]:
        pass


class ServiceResourceRouteTablesCollection(ResourceCollection):
    """
    [ServiceResource.route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.route_tables)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceRouteTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceRouteTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceRouteTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceRouteTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.RouteTable]:
        pass


class ServiceResourceSecurityGroupsCollection(ResourceCollection):
    """
    [ServiceResource.security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.security_groups)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceSecurityGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceSecurityGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceSecurityGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.ServiceResourceSecurityGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.SecurityGroup]:
        pass


class ServiceResourceSnapshotsCollection(ResourceCollection):
    """
    [ServiceResource.snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.snapshots)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceSnapshotsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceSnapshotsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceSnapshotsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceSnapshotsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Snapshot]:
        pass


class ServiceResourceSubnetsCollection(ResourceCollection):
    """
    [ServiceResource.subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.subnets)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceSubnetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceSubnetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceSubnetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceSubnetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Subnet]:
        pass


class ServiceResourceVolumesCollection(ResourceCollection):
    """
    [ServiceResource.volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.volumes)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceVolumesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceVolumesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceVolumesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceVolumesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Volume]:
        pass


class ServiceResourceVpcAddressesCollection(ResourceCollection):
    """
    [ServiceResource.vpc_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceVpcAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceVpcAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceVpcAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceVpcAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.VpcAddress]:
        pass


class ServiceResourceVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [ServiceResource.vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(
        cls, count: int
    ) -> service_resource_scope.ServiceResourceVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.ServiceResourceVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.VpcPeeringConnection]:
        pass


class ServiceResourceVpcsCollection(ResourceCollection):
    """
    [ServiceResource.vpcs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.ServiceResource.vpcs)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceVpcsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceVpcsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceVpcsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceVpcsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Vpc]:
        pass


class InstanceVolumesCollection(ResourceCollection):
    """
    [Instance.volumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.volumes)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.InstanceVolumesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.InstanceVolumesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.InstanceVolumesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.InstanceVolumesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Volume]:
        pass


class InstanceVpcAddressesCollection(ResourceCollection):
    """
    [Instance.vpc_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Instance.vpc_addresses)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.InstanceVpcAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.InstanceVpcAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.InstanceVpcAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.InstanceVpcAddressesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.VpcAddress]:
        pass


class PlacementGroupInstancesCollection(ResourceCollection):
    """
    [PlacementGroup.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.PlacementGroup.instances)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.PlacementGroupInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.PlacementGroupInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.PlacementGroupInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.PlacementGroupInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Instance]:
        pass


class SubnetInstancesCollection(ResourceCollection):
    """
    [Subnet.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Subnet.instances)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.SubnetInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.SubnetInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.SubnetInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.SubnetInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Instance]:
        pass


class SubnetNetworkInterfacesCollection(ResourceCollection):
    """
    [Subnet.network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Subnet.network_interfaces)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.SubnetNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.SubnetNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.SubnetNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.SubnetNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.NetworkInterface]:
        pass


class VolumeSnapshotsCollection(ResourceCollection):
    """
    [Volume.snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Volume.snapshots)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.VolumeSnapshotsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.VolumeSnapshotsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.VolumeSnapshotsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.VolumeSnapshotsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Snapshot]:
        pass


class VpcAcceptedVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Vpc.accepted_vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.accepted_vpc_peering_connections)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.VpcAcceptedVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.VpcAcceptedVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.VpcAcceptedVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.VpcAcceptedVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.VpcPeeringConnection]:
        pass


class VpcInstancesCollection(ResourceCollection):
    """
    [Vpc.instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.instances)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.VpcInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.VpcInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.VpcInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.VpcInstancesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Instance]:
        pass


class VpcInternetGatewaysCollection(ResourceCollection):
    """
    [Vpc.internet_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.internet_gateways)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.VpcInternetGatewaysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.VpcInternetGatewaysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.VpcInternetGatewaysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.VpcInternetGatewaysCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.InternetGateway]:
        pass


class VpcNetworkAclsCollection(ResourceCollection):
    """
    [Vpc.network_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.network_acls)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.VpcNetworkAclsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.VpcNetworkAclsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.VpcNetworkAclsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.VpcNetworkAclsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.NetworkAcl]:
        pass


class VpcNetworkInterfacesCollection(ResourceCollection):
    """
    [Vpc.network_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.network_interfaces)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.VpcNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.VpcNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.VpcNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.VpcNetworkInterfacesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.NetworkInterface]:
        pass


class VpcRequestedVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Vpc.requested_vpc_peering_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.requested_vpc_peering_connections)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.VpcRequestedVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.VpcRequestedVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(
        cls, count: int
    ) -> service_resource_scope.VpcRequestedVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.VpcRequestedVpcPeeringConnectionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.VpcPeeringConnection]:
        pass


class VpcRouteTablesCollection(ResourceCollection):
    """
    [Vpc.route_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.route_tables)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.VpcRouteTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.VpcRouteTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.VpcRouteTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.VpcRouteTablesCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.RouteTable]:
        pass


class VpcSecurityGroupsCollection(ResourceCollection):
    """
    [Vpc.security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.security_groups)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.VpcSecurityGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.VpcSecurityGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.VpcSecurityGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.VpcSecurityGroupsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.SecurityGroup]:
        pass


class VpcSubnetsCollection(ResourceCollection):
    """
    [Vpc.subnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Vpc.subnets)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.VpcSubnetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.VpcSubnetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.VpcSubnetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.VpcSubnetsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Subnet]:
        pass
