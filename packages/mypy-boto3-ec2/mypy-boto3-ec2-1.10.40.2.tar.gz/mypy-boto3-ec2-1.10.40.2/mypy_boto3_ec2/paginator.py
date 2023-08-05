"Main interface for ec2 service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ec2.type_defs import (
    DescribeByoipCidrsResultTypeDef,
    DescribeCapacityReservationsResultTypeDef,
    DescribeClassicLinkInstancesResultTypeDef,
    DescribeClientVpnAuthorizationRulesResultTypeDef,
    DescribeClientVpnConnectionsResultTypeDef,
    DescribeClientVpnEndpointsResultTypeDef,
    DescribeClientVpnRoutesResultTypeDef,
    DescribeClientVpnTargetNetworksResultTypeDef,
    DescribeDhcpOptionsResultTypeDef,
    DescribeEgressOnlyInternetGatewaysResultTypeDef,
    DescribeExportImageTasksResultTypeDef,
    DescribeFastSnapshotRestoresResultTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeFlowLogsResultTypeDef,
    DescribeFpgaImagesResultTypeDef,
    DescribeHostReservationOfferingsResultTypeDef,
    DescribeHostReservationsResultTypeDef,
    DescribeHostsResultTypeDef,
    DescribeIamInstanceProfileAssociationsResultTypeDef,
    DescribeImportImageTasksResultTypeDef,
    DescribeImportSnapshotTasksResultTypeDef,
    DescribeInstanceCreditSpecificationsResultTypeDef,
    DescribeInstanceStatusResultTypeDef,
    DescribeInstancesResultTypeDef,
    DescribeInternetGatewaysResultTypeDef,
    DescribeLaunchTemplateVersionsResultTypeDef,
    DescribeLaunchTemplatesResultTypeDef,
    DescribeMovingAddressesResultTypeDef,
    DescribeNatGatewaysResultTypeDef,
    DescribeNetworkAclsResultTypeDef,
    DescribeNetworkInterfacePermissionsResultTypeDef,
    DescribeNetworkInterfacesResultTypeDef,
    DescribePrefixListsResultTypeDef,
    DescribePrincipalIdFormatResultTypeDef,
    DescribePublicIpv4PoolsResultTypeDef,
    DescribeReservedInstancesModificationsResultTypeDef,
    DescribeReservedInstancesOfferingsResultTypeDef,
    DescribeRouteTablesResultTypeDef,
    DescribeScheduledInstanceAvailabilityResultTypeDef,
    DescribeScheduledInstancesResultTypeDef,
    DescribeSecurityGroupsResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeSpotFleetInstancesResponseTypeDef,
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
    DescribeTransitGatewayRouteTablesResultTypeDef,
    DescribeTransitGatewayVpcAttachmentsResultTypeDef,
    DescribeTransitGatewaysResultTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVolumesModificationsResultTypeDef,
    DescribeVolumesResultTypeDef,
    DescribeVpcClassicLinkDnsSupportResultTypeDef,
    DescribeVpcEndpointConnectionNotificationsResultTypeDef,
    DescribeVpcEndpointConnectionsResultTypeDef,
    DescribeVpcEndpointServiceConfigurationsResultTypeDef,
    DescribeVpcEndpointServicePermissionsResultTypeDef,
    DescribeVpcEndpointServicesResultTypeDef,
    DescribeVpcEndpointsResultTypeDef,
    DescribeVpcPeeringConnectionsResultTypeDef,
    DescribeVpcsResultTypeDef,
    FilterTypeDef,
    GetTransitGatewayAttachmentPropagationsResultTypeDef,
    GetTransitGatewayRouteTableAssociationsResultTypeDef,
    GetTransitGatewayRouteTablePropagationsResultTypeDef,
    PaginatorConfigTypeDef,
    ScheduledInstanceRecurrenceRequestTypeDef,
    SlotDateTimeRangeRequestTypeDef,
    SlotStartTimeRangeRequestTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeByoipCidrsPaginator",
    "DescribeCapacityReservationsPaginator",
    "DescribeClassicLinkInstancesPaginator",
    "DescribeClientVpnAuthorizationRulesPaginator",
    "DescribeClientVpnConnectionsPaginator",
    "DescribeClientVpnEndpointsPaginator",
    "DescribeClientVpnRoutesPaginator",
    "DescribeClientVpnTargetNetworksPaginator",
    "DescribeDhcpOptionsPaginator",
    "DescribeEgressOnlyInternetGatewaysPaginator",
    "DescribeExportImageTasksPaginator",
    "DescribeFastSnapshotRestoresPaginator",
    "DescribeFleetsPaginator",
    "DescribeFlowLogsPaginator",
    "DescribeFpgaImagesPaginator",
    "DescribeHostReservationOfferingsPaginator",
    "DescribeHostReservationsPaginator",
    "DescribeHostsPaginator",
    "DescribeIamInstanceProfileAssociationsPaginator",
    "DescribeImportImageTasksPaginator",
    "DescribeImportSnapshotTasksPaginator",
    "DescribeInstanceCreditSpecificationsPaginator",
    "DescribeInstanceStatusPaginator",
    "DescribeInstancesPaginator",
    "DescribeInternetGatewaysPaginator",
    "DescribeLaunchTemplateVersionsPaginator",
    "DescribeLaunchTemplatesPaginator",
    "DescribeMovingAddressesPaginator",
    "DescribeNatGatewaysPaginator",
    "DescribeNetworkAclsPaginator",
    "DescribeNetworkInterfacePermissionsPaginator",
    "DescribeNetworkInterfacesPaginator",
    "DescribePrefixListsPaginator",
    "DescribePrincipalIdFormatPaginator",
    "DescribePublicIpv4PoolsPaginator",
    "DescribeReservedInstancesModificationsPaginator",
    "DescribeReservedInstancesOfferingsPaginator",
    "DescribeRouteTablesPaginator",
    "DescribeScheduledInstanceAvailabilityPaginator",
    "DescribeScheduledInstancesPaginator",
    "DescribeSecurityGroupsPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeSpotFleetInstancesPaginator",
    "DescribeSpotFleetRequestsPaginator",
    "DescribeSpotInstanceRequestsPaginator",
    "DescribeSpotPriceHistoryPaginator",
    "DescribeStaleSecurityGroupsPaginator",
    "DescribeSubnetsPaginator",
    "DescribeTagsPaginator",
    "DescribeTrafficMirrorFiltersPaginator",
    "DescribeTrafficMirrorSessionsPaginator",
    "DescribeTrafficMirrorTargetsPaginator",
    "DescribeTransitGatewayAttachmentsPaginator",
    "DescribeTransitGatewayRouteTablesPaginator",
    "DescribeTransitGatewayVpcAttachmentsPaginator",
    "DescribeTransitGatewaysPaginator",
    "DescribeVolumeStatusPaginator",
    "DescribeVolumesPaginator",
    "DescribeVolumesModificationsPaginator",
    "DescribeVpcClassicLinkDnsSupportPaginator",
    "DescribeVpcEndpointConnectionNotificationsPaginator",
    "DescribeVpcEndpointConnectionsPaginator",
    "DescribeVpcEndpointServiceConfigurationsPaginator",
    "DescribeVpcEndpointServicePermissionsPaginator",
    "DescribeVpcEndpointServicesPaginator",
    "DescribeVpcEndpointsPaginator",
    "DescribeVpcPeeringConnectionsPaginator",
    "DescribeVpcsPaginator",
    "GetTransitGatewayAttachmentPropagationsPaginator",
    "GetTransitGatewayRouteTableAssociationsPaginator",
    "GetTransitGatewayRouteTablePropagationsPaginator",
)


class DescribeByoipCidrsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeByoipCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DryRun: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeByoipCidrsResultTypeDef, None, None]:
        """
        [DescribeByoipCidrs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs.paginate)
        """


class DescribeCapacityReservationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCapacityReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CapacityReservationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeCapacityReservationsResultTypeDef, None, None]:
        """
        [DescribeCapacityReservations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations.paginate)
        """


class DescribeClassicLinkInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClassicLinkInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InstanceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeClassicLinkInstancesResultTypeDef, None, None]:
        """
        [DescribeClassicLinkInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances.paginate)
        """


class DescribeClientVpnAuthorizationRulesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClientVpnAuthorizationRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClientVpnEndpointId: str,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeClientVpnAuthorizationRulesResultTypeDef, None, None]:
        """
        [DescribeClientVpnAuthorizationRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules.paginate)
        """


class DescribeClientVpnConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClientVpnConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeClientVpnConnectionsResultTypeDef, None, None]:
        """
        [DescribeClientVpnConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections.paginate)
        """


class DescribeClientVpnEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClientVpnEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClientVpnEndpointIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeClientVpnEndpointsResultTypeDef, None, None]:
        """
        [DescribeClientVpnEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints.paginate)
        """


class DescribeClientVpnRoutesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClientVpnRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeClientVpnRoutesResultTypeDef, None, None]:
        """
        [DescribeClientVpnRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes.paginate)
        """


class DescribeClientVpnTargetNetworksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClientVpnTargetNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClientVpnEndpointId: str,
        AssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeClientVpnTargetNetworksResultTypeDef, None, None]:
        """
        [DescribeClientVpnTargetNetworks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks.paginate)
        """


class DescribeDhcpOptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDhcpOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DhcpOptionsIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeDhcpOptionsResultTypeDef, None, None]:
        """
        [DescribeDhcpOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions.paginate)
        """


class DescribeEgressOnlyInternetGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEgressOnlyInternetGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        EgressOnlyInternetGatewayIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeEgressOnlyInternetGatewaysResultTypeDef, None, None]:
        """
        [DescribeEgressOnlyInternetGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways.paginate)
        """


class DescribeExportImageTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeExportImageTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ExportImageTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeExportImageTasksResultTypeDef, None, None]:
        """
        [DescribeExportImageTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks.paginate)
        """


class DescribeFastSnapshotRestoresPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFastSnapshotRestores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeFastSnapshotRestoresResultTypeDef, None, None]:
        """
        [DescribeFastSnapshotRestores.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores.paginate)
        """


class DescribeFleetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFleets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        FleetIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeFleetsResultTypeDef, None, None]:
        """
        [DescribeFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFleets.paginate)
        """


class DescribeFlowLogsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFlowLogs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        FlowLogIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeFlowLogsResultTypeDef, None, None]:
        """
        [DescribeFlowLogs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs.paginate)
        """


class DescribeFpgaImagesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFpgaImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        FpgaImageIds: List[str] = None,
        Owners: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeFpgaImagesResultTypeDef, None, None]:
        """
        [DescribeFpgaImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages.paginate)
        """


class DescribeHostReservationOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeHostReservationOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxDuration: int = None,
        MinDuration: int = None,
        OfferingId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeHostReservationOfferingsResultTypeDef, None, None]:
        """
        [DescribeHostReservationOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings.paginate)
        """


class DescribeHostReservationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeHostReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        HostReservationIdSet: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeHostReservationsResultTypeDef, None, None]:
        """
        [DescribeHostReservations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations.paginate)
        """


class DescribeHostsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeHosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeHosts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        HostIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeHostsResultTypeDef, None, None]:
        """
        [DescribeHosts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeHosts.paginate)
        """


class DescribeIamInstanceProfileAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeIamInstanceProfileAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeIamInstanceProfileAssociationsResultTypeDef, None, None]:
        """
        [DescribeIamInstanceProfileAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations.paginate)
        """


class DescribeImportImageTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImportImageTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ImportTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeImportImageTasksResultTypeDef, None, None]:
        """
        [DescribeImportImageTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks.paginate)
        """


class DescribeImportSnapshotTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImportSnapshotTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ImportTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeImportSnapshotTasksResultTypeDef, None, None]:
        """
        [DescribeImportSnapshotTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks.paginate)
        """


class DescribeInstanceCreditSpecificationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstanceCreditSpecifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeInstanceCreditSpecificationsResultTypeDef, None, None]:
        """
        [DescribeInstanceCreditSpecifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications.paginate)
        """


class DescribeInstanceStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstanceStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeInstanceStatusResultTypeDef, None, None]:
        """
        [DescribeInstanceStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus.paginate)
        """


class DescribeInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeInstancesResultTypeDef, None, None]:
        """
        [DescribeInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInstances.paginate)
        """


class DescribeInternetGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInternetGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeInternetGatewaysResultTypeDef, None, None]:
        """
        [DescribeInternetGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways.paginate)
        """


class DescribeLaunchTemplateVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLaunchTemplateVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        Versions: List[str] = None,
        MinVersion: str = None,
        MaxVersion: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeLaunchTemplateVersionsResultTypeDef, None, None]:
        """
        [DescribeLaunchTemplateVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions.paginate)
        """


class DescribeLaunchTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLaunchTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        LaunchTemplateIds: List[str] = None,
        LaunchTemplateNames: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeLaunchTemplatesResultTypeDef, None, None]:
        """
        [DescribeLaunchTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates.paginate)
        """


class DescribeMovingAddressesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMovingAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PublicIps: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeMovingAddressesResultTypeDef, None, None]:
        """
        [DescribeMovingAddresses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses.paginate)
        """


class DescribeNatGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNatGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        NatGatewayIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeNatGatewaysResultTypeDef, None, None]:
        """
        [DescribeNatGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways.paginate)
        """


class DescribeNetworkAclsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNetworkAcls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeNetworkAclsResultTypeDef, None, None]:
        """
        [DescribeNetworkAcls.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls.paginate)
        """


class DescribeNetworkInterfacePermissionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNetworkInterfacePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        NetworkInterfacePermissionIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeNetworkInterfacePermissionsResultTypeDef, None, None]:
        """
        [DescribeNetworkInterfacePermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions.paginate)
        """


class DescribeNetworkInterfacesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNetworkInterfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeNetworkInterfacesResultTypeDef, None, None]:
        """
        [DescribeNetworkInterfaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces.paginate)
        """


class DescribePrefixListsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePrefixLists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PrefixListIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribePrefixListsResultTypeDef, None, None]:
        """
        [DescribePrefixLists.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists.paginate)
        """


class DescribePrincipalIdFormatPaginator(Boto3Paginator):
    """
    [Paginator.DescribePrincipalIdFormat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Resources: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribePrincipalIdFormatResultTypeDef, None, None]:
        """
        [DescribePrincipalIdFormat.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat.paginate)
        """


class DescribePublicIpv4PoolsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePublicIpv4Pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PoolIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribePublicIpv4PoolsResultTypeDef, None, None]:
        """
        [DescribePublicIpv4Pools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools.paginate)
        """


class DescribeReservedInstancesModificationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedInstancesModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        ReservedInstancesModificationIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeReservedInstancesModificationsResultTypeDef, None, None]:
        """
        [DescribeReservedInstancesModifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications.paginate)
        """


class DescribeReservedInstancesOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedInstancesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
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
        OfferingType: Literal[
            "Heavy Utilization",
            "Medium Utilization",
            "Light Utilization",
            "No Upfront",
            "Partial Upfront",
            "All Upfront",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeReservedInstancesOfferingsResultTypeDef, None, None]:
        """
        [DescribeReservedInstancesOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings.paginate)
        """


class DescribeRouteTablesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeRouteTablesResultTypeDef, None, None]:
        """
        [DescribeRouteTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables.paginate)
        """


class DescribeScheduledInstanceAvailabilityPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScheduledInstanceAvailability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FirstSlotStartTimeRange: SlotDateTimeRangeRequestTypeDef,
        Recurrence: ScheduledInstanceRecurrenceRequestTypeDef,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxSlotDurationInHours: int = None,
        MinSlotDurationInHours: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeScheduledInstanceAvailabilityResultTypeDef, None, None]:
        """
        [DescribeScheduledInstanceAvailability.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability.paginate)
        """


class DescribeScheduledInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScheduledInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ScheduledInstanceIds: List[str] = None,
        SlotStartTimeRange: SlotStartTimeRangeRequestTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeScheduledInstancesResultTypeDef, None, None]:
        """
        [DescribeScheduledInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances.paginate)
        """


class DescribeSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSecurityGroupsResultTypeDef, None, None]:
        """
        [DescribeSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups.paginate)
        """


class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSnapshotsResultTypeDef, None, None]:
        """
        [DescribeSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots.paginate)
        """


class DescribeSpotFleetInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSpotFleetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SpotFleetRequestId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSpotFleetInstancesResponseTypeDef, None, None]:
        """
        [DescribeSpotFleetInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances.paginate)
        """


class DescribeSpotFleetRequestsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSpotFleetRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        SpotFleetRequestIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSpotFleetRequestsResponseTypeDef, None, None]:
        """
        [DescribeSpotFleetRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests.paginate)
        """


class DescribeSpotInstanceRequestsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSpotInstanceRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSpotInstanceRequestsResultTypeDef, None, None]:
        """
        [DescribeSpotInstanceRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests.paginate)
        """


class DescribeSpotPriceHistoryPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSpotPriceHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
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
        ProductDescriptions: List[str] = None,
        StartTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSpotPriceHistoryResultTypeDef, None, None]:
        """
        [DescribeSpotPriceHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory.paginate)
        """


class DescribeStaleSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeStaleSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, VpcId: str, DryRun: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeStaleSecurityGroupsResultTypeDef, None, None]:
        """
        [DescribeStaleSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups.paginate)
        """


class DescribeSubnetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSubnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSubnets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeSubnetsResultTypeDef, None, None]:
        """
        [DescribeSubnets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeSubnets.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTags)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTagsResultTypeDef, None, None]:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTags.paginate)
        """


class DescribeTrafficMirrorFiltersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTrafficMirrorFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TrafficMirrorFilterIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTrafficMirrorFiltersResultTypeDef, None, None]:
        """
        [DescribeTrafficMirrorFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters.paginate)
        """


class DescribeTrafficMirrorSessionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTrafficMirrorSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TrafficMirrorSessionIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTrafficMirrorSessionsResultTypeDef, None, None]:
        """
        [DescribeTrafficMirrorSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions.paginate)
        """


class DescribeTrafficMirrorTargetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTrafficMirrorTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TrafficMirrorTargetIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTrafficMirrorTargetsResultTypeDef, None, None]:
        """
        [DescribeTrafficMirrorTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets.paginate)
        """


class DescribeTransitGatewayAttachmentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTransitGatewayAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTransitGatewayAttachmentsResultTypeDef, None, None]:
        """
        [DescribeTransitGatewayAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments.paginate)
        """


class DescribeTransitGatewayRouteTablesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTransitGatewayRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayRouteTableIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTransitGatewayRouteTablesResultTypeDef, None, None]:
        """
        [DescribeTransitGatewayRouteTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables.paginate)
        """


class DescribeTransitGatewayVpcAttachmentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTransitGatewayVpcAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTransitGatewayVpcAttachmentsResultTypeDef, None, None]:
        """
        [DescribeTransitGatewayVpcAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments.paginate)
        """


class DescribeTransitGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTransitGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeTransitGatewaysResultTypeDef, None, None]:
        """
        [DescribeTransitGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways.paginate)
        """


class DescribeVolumeStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVolumeStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVolumeStatusResultTypeDef, None, None]:
        """
        [DescribeVolumeStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus.paginate)
        """


class DescribeVolumesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVolumes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVolumesResultTypeDef, None, None]:
        """
        [DescribeVolumes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVolumes.paginate)
        """


class DescribeVolumesModificationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVolumesModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        VolumeIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVolumesModificationsResultTypeDef, None, None]:
        """
        [DescribeVolumesModifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications.paginate)
        """


class DescribeVpcClassicLinkDnsSupportPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcClassicLinkDnsSupport documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, VpcIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[DescribeVpcClassicLinkDnsSupportResultTypeDef, None, None]:
        """
        [DescribeVpcClassicLinkDnsSupport.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport.paginate)
        """


class DescribeVpcEndpointConnectionNotificationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpointConnectionNotifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        ConnectionNotificationId: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVpcEndpointConnectionNotificationsResultTypeDef, None, None]:
        """
        [DescribeVpcEndpointConnectionNotifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications.paginate)
        """


class DescribeVpcEndpointConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpointConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVpcEndpointConnectionsResultTypeDef, None, None]:
        """
        [DescribeVpcEndpointConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections.paginate)
        """


class DescribeVpcEndpointServiceConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpointServiceConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        ServiceIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVpcEndpointServiceConfigurationsResultTypeDef, None, None]:
        """
        [DescribeVpcEndpointServiceConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations.paginate)
        """


class DescribeVpcEndpointServicePermissionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpointServicePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceId: str,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVpcEndpointServicePermissionsResultTypeDef, None, None]:
        """
        [DescribeVpcEndpointServicePermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions.paginate)
        """


class DescribeVpcEndpointServicesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpointServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        ServiceNames: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVpcEndpointServicesResultTypeDef, None, None]:
        """
        [DescribeVpcEndpointServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices.paginate)
        """


class DescribeVpcEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DryRun: bool = None,
        VpcEndpointIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVpcEndpointsResultTypeDef, None, None]:
        """
        [DescribeVpcEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints.paginate)
        """


class DescribeVpcPeeringConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcPeeringConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVpcPeeringConnectionsResultTypeDef, None, None]:
        """
        [DescribeVpcPeeringConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections.paginate)
        """


class DescribeVpcsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[DescribeVpcsResultTypeDef, None, None]:
        """
        [DescribeVpcs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.DescribeVpcs.paginate)
        """


class GetTransitGatewayAttachmentPropagationsPaginator(Boto3Paginator):
    """
    [Paginator.GetTransitGatewayAttachmentPropagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayAttachmentId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetTransitGatewayAttachmentPropagationsResultTypeDef, None, None]:
        """
        [GetTransitGatewayAttachmentPropagations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations.paginate)
        """


class GetTransitGatewayRouteTableAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetTransitGatewayRouteTableAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetTransitGatewayRouteTableAssociationsResultTypeDef, None, None]:
        """
        [GetTransitGatewayRouteTableAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations.paginate)
        """


class GetTransitGatewayRouteTablePropagationsPaginator(Boto3Paginator):
    """
    [Paginator.GetTransitGatewayRouteTablePropagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetTransitGatewayRouteTablePropagationsResultTypeDef, None, None]:
        """
        [GetTransitGatewayRouteTablePropagations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations.paginate)
        """
