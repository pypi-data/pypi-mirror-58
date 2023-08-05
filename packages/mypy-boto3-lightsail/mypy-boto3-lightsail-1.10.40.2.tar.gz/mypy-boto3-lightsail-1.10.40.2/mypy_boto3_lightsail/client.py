"Main interface for lightsail service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_lightsail.client as client_scope

# pylint: disable=import-self
import mypy_boto3_lightsail.paginator as paginator_scope
from mypy_boto3_lightsail.type_defs import (
    AddOnRequestTypeDef,
    AllocateStaticIpResultTypeDef,
    AttachDiskResultTypeDef,
    AttachInstancesToLoadBalancerResultTypeDef,
    AttachLoadBalancerTlsCertificateResultTypeDef,
    AttachStaticIpResultTypeDef,
    CloseInstancePublicPortsResultTypeDef,
    CopySnapshotResultTypeDef,
    CreateCloudFormationStackResultTypeDef,
    CreateDiskFromSnapshotResultTypeDef,
    CreateDiskResultTypeDef,
    CreateDiskSnapshotResultTypeDef,
    CreateDomainEntryResultTypeDef,
    CreateDomainResultTypeDef,
    CreateInstanceSnapshotResultTypeDef,
    CreateInstancesFromSnapshotResultTypeDef,
    CreateInstancesResultTypeDef,
    CreateKeyPairResultTypeDef,
    CreateLoadBalancerResultTypeDef,
    CreateLoadBalancerTlsCertificateResultTypeDef,
    CreateRelationalDatabaseFromSnapshotResultTypeDef,
    CreateRelationalDatabaseResultTypeDef,
    CreateRelationalDatabaseSnapshotResultTypeDef,
    DeleteAutoSnapshotResultTypeDef,
    DeleteDiskResultTypeDef,
    DeleteDiskSnapshotResultTypeDef,
    DeleteDomainEntryResultTypeDef,
    DeleteDomainResultTypeDef,
    DeleteInstanceResultTypeDef,
    DeleteInstanceSnapshotResultTypeDef,
    DeleteKeyPairResultTypeDef,
    DeleteKnownHostKeysResultTypeDef,
    DeleteLoadBalancerResultTypeDef,
    DeleteLoadBalancerTlsCertificateResultTypeDef,
    DeleteRelationalDatabaseResultTypeDef,
    DeleteRelationalDatabaseSnapshotResultTypeDef,
    DetachDiskResultTypeDef,
    DetachInstancesFromLoadBalancerResultTypeDef,
    DetachStaticIpResultTypeDef,
    DisableAddOnResultTypeDef,
    DiskMapTypeDef,
    DomainEntryTypeDef,
    DownloadDefaultKeyPairResultTypeDef,
    EnableAddOnResultTypeDef,
    ExportSnapshotResultTypeDef,
    GetActiveNamesResultTypeDef,
    GetAutoSnapshotsResultTypeDef,
    GetBlueprintsResultTypeDef,
    GetBundlesResultTypeDef,
    GetCloudFormationStackRecordsResultTypeDef,
    GetDiskResultTypeDef,
    GetDiskSnapshotResultTypeDef,
    GetDiskSnapshotsResultTypeDef,
    GetDisksResultTypeDef,
    GetDomainResultTypeDef,
    GetDomainsResultTypeDef,
    GetExportSnapshotRecordsResultTypeDef,
    GetInstanceAccessDetailsResultTypeDef,
    GetInstanceMetricDataResultTypeDef,
    GetInstancePortStatesResultTypeDef,
    GetInstanceResultTypeDef,
    GetInstanceSnapshotResultTypeDef,
    GetInstanceSnapshotsResultTypeDef,
    GetInstanceStateResultTypeDef,
    GetInstancesResultTypeDef,
    GetKeyPairResultTypeDef,
    GetKeyPairsResultTypeDef,
    GetLoadBalancerMetricDataResultTypeDef,
    GetLoadBalancerResultTypeDef,
    GetLoadBalancerTlsCertificatesResultTypeDef,
    GetLoadBalancersResultTypeDef,
    GetOperationResultTypeDef,
    GetOperationsForResourceResultTypeDef,
    GetOperationsResultTypeDef,
    GetRegionsResultTypeDef,
    GetRelationalDatabaseBlueprintsResultTypeDef,
    GetRelationalDatabaseBundlesResultTypeDef,
    GetRelationalDatabaseEventsResultTypeDef,
    GetRelationalDatabaseLogEventsResultTypeDef,
    GetRelationalDatabaseLogStreamsResultTypeDef,
    GetRelationalDatabaseMasterUserPasswordResultTypeDef,
    GetRelationalDatabaseMetricDataResultTypeDef,
    GetRelationalDatabaseParametersResultTypeDef,
    GetRelationalDatabaseResultTypeDef,
    GetRelationalDatabaseSnapshotResultTypeDef,
    GetRelationalDatabaseSnapshotsResultTypeDef,
    GetRelationalDatabasesResultTypeDef,
    GetStaticIpResultTypeDef,
    GetStaticIpsResultTypeDef,
    ImportKeyPairResultTypeDef,
    InstanceEntryTypeDef,
    IsVpcPeeredResultTypeDef,
    OpenInstancePublicPortsResultTypeDef,
    PeerVpcResultTypeDef,
    PortInfoTypeDef,
    PutInstancePublicPortsResultTypeDef,
    RebootInstanceResultTypeDef,
    RebootRelationalDatabaseResultTypeDef,
    RelationalDatabaseParameterTypeDef,
    ReleaseStaticIpResultTypeDef,
    StartInstanceResultTypeDef,
    StartRelationalDatabaseResultTypeDef,
    StopInstanceResultTypeDef,
    StopRelationalDatabaseResultTypeDef,
    TagResourceResultTypeDef,
    TagTypeDef,
    UnpeerVpcResultTypeDef,
    UntagResourceResultTypeDef,
    UpdateDomainEntryResultTypeDef,
    UpdateLoadBalancerAttributeResultTypeDef,
    UpdateRelationalDatabaseParametersResultTypeDef,
    UpdateRelationalDatabaseResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LightsailClient",)


class LightsailClient(BaseClient):
    """
    [Lightsail.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def allocate_static_ip(self, staticIpName: str) -> AllocateStaticIpResultTypeDef:
        """
        [Client.allocate_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.allocate_static_ip)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_disk(
        self, diskName: str, instanceName: str, diskPath: str
    ) -> AttachDiskResultTypeDef:
        """
        [Client.attach_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.attach_disk)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_instances_to_load_balancer(
        self, loadBalancerName: str, instanceNames: List[str]
    ) -> AttachInstancesToLoadBalancerResultTypeDef:
        """
        [Client.attach_instances_to_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.attach_instances_to_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_load_balancer_tls_certificate(
        self, loadBalancerName: str, certificateName: str
    ) -> AttachLoadBalancerTlsCertificateResultTypeDef:
        """
        [Client.attach_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.attach_load_balancer_tls_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_static_ip(self, staticIpName: str, instanceName: str) -> AttachStaticIpResultTypeDef:
        """
        [Client.attach_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.attach_static_ip)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def close_instance_public_ports(
        self, portInfo: PortInfoTypeDef, instanceName: str
    ) -> CloseInstancePublicPortsResultTypeDef:
        """
        [Client.close_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.close_instance_public_ports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_snapshot(
        self,
        targetSnapshotName: str,
        sourceRegion: Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
        sourceSnapshotName: str = None,
        sourceResourceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> CopySnapshotResultTypeDef:
        """
        [Client.copy_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.copy_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cloud_formation_stack(
        self, instances: List[InstanceEntryTypeDef]
    ) -> CreateCloudFormationStackResultTypeDef:
        """
        [Client.create_cloud_formation_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_cloud_formation_stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_disk(
        self,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        tags: List[TagTypeDef] = None,
        addOns: List[AddOnRequestTypeDef] = None,
    ) -> CreateDiskResultTypeDef:
        """
        [Client.create_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_disk)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_disk_from_snapshot(
        self,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        diskSnapshotName: str = None,
        tags: List[TagTypeDef] = None,
        addOns: List[AddOnRequestTypeDef] = None,
        sourceDiskName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> CreateDiskFromSnapshotResultTypeDef:
        """
        [Client.create_disk_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_disk_from_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_disk_snapshot(
        self,
        diskSnapshotName: str,
        diskName: str = None,
        instanceName: str = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateDiskSnapshotResultTypeDef:
        """
        [Client.create_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_disk_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_domain(
        self, domainName: str, tags: List[TagTypeDef] = None
    ) -> CreateDomainResultTypeDef:
        """
        [Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_domain_entry(
        self, domainName: str, domainEntry: DomainEntryTypeDef
    ) -> CreateDomainEntryResultTypeDef:
        """
        [Client.create_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_domain_entry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instance_snapshot(
        self, instanceSnapshotName: str, instanceName: str, tags: List[TagTypeDef] = None
    ) -> CreateInstanceSnapshotResultTypeDef:
        """
        [Client.create_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_instance_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instances(
        self,
        instanceNames: List[str],
        availabilityZone: str,
        blueprintId: str,
        bundleId: str,
        customImageName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List[TagTypeDef] = None,
        addOns: List[AddOnRequestTypeDef] = None,
    ) -> CreateInstancesResultTypeDef:
        """
        [Client.create_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instances_from_snapshot(
        self,
        instanceNames: List[str],
        availabilityZone: str,
        bundleId: str,
        attachedDiskMapping: Dict[str, List[DiskMapTypeDef]] = None,
        instanceSnapshotName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List[TagTypeDef] = None,
        addOns: List[AddOnRequestTypeDef] = None,
        sourceInstanceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> CreateInstancesFromSnapshotResultTypeDef:
        """
        [Client.create_instances_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_instances_from_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_key_pair(
        self, keyPairName: str, tags: List[TagTypeDef] = None
    ) -> CreateKeyPairResultTypeDef:
        """
        [Client.create_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_load_balancer(
        self,
        loadBalancerName: str,
        instancePort: int,
        healthCheckPath: str = None,
        certificateName: str = None,
        certificateDomainName: str = None,
        certificateAlternativeNames: List[str] = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateLoadBalancerResultTypeDef:
        """
        [Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_load_balancer_tls_certificate(
        self,
        loadBalancerName: str,
        certificateName: str,
        certificateDomainName: str,
        certificateAlternativeNames: List[str] = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateLoadBalancerTlsCertificateResultTypeDef:
        """
        [Client.create_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_load_balancer_tls_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_relational_database(
        self,
        relationalDatabaseName: str,
        relationalDatabaseBlueprintId: str,
        relationalDatabaseBundleId: str,
        masterDatabaseName: str,
        masterUsername: str,
        availabilityZone: str = None,
        masterUserPassword: str = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        publiclyAccessible: bool = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateRelationalDatabaseResultTypeDef:
        """
        [Client.create_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_relational_database)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_relational_database_from_snapshot(
        self,
        relationalDatabaseName: str,
        availabilityZone: str = None,
        publiclyAccessible: bool = None,
        relationalDatabaseSnapshotName: str = None,
        relationalDatabaseBundleId: str = None,
        sourceRelationalDatabaseName: str = None,
        restoreTime: datetime = None,
        useLatestRestorableTime: bool = None,
        tags: List[TagTypeDef] = None,
    ) -> CreateRelationalDatabaseFromSnapshotResultTypeDef:
        """
        [Client.create_relational_database_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_relational_database_from_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_relational_database_snapshot(
        self,
        relationalDatabaseName: str,
        relationalDatabaseSnapshotName: str,
        tags: List[TagTypeDef] = None,
    ) -> CreateRelationalDatabaseSnapshotResultTypeDef:
        """
        [Client.create_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.create_relational_database_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_auto_snapshot(self, resourceName: str, date: str) -> DeleteAutoSnapshotResultTypeDef:
        """
        [Client.delete_auto_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_auto_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_disk(self, diskName: str, forceDeleteAddOns: bool = None) -> DeleteDiskResultTypeDef:
        """
        [Client.delete_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_disk)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_disk_snapshot(self, diskSnapshotName: str) -> DeleteDiskSnapshotResultTypeDef:
        """
        [Client.delete_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_disk_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_domain(self, domainName: str) -> DeleteDomainResultTypeDef:
        """
        [Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_domain_entry(
        self, domainName: str, domainEntry: DomainEntryTypeDef
    ) -> DeleteDomainEntryResultTypeDef:
        """
        [Client.delete_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_domain_entry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_instance(
        self, instanceName: str, forceDeleteAddOns: bool = None
    ) -> DeleteInstanceResultTypeDef:
        """
        [Client.delete_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_instance_snapshot(
        self, instanceSnapshotName: str
    ) -> DeleteInstanceSnapshotResultTypeDef:
        """
        [Client.delete_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_instance_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_key_pair(self, keyPairName: str) -> DeleteKeyPairResultTypeDef:
        """
        [Client.delete_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_known_host_keys(self, instanceName: str) -> DeleteKnownHostKeysResultTypeDef:
        """
        [Client.delete_known_host_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_known_host_keys)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_load_balancer(self, loadBalancerName: str) -> DeleteLoadBalancerResultTypeDef:
        """
        [Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_load_balancer_tls_certificate(
        self, loadBalancerName: str, certificateName: str, force: bool = None
    ) -> DeleteLoadBalancerTlsCertificateResultTypeDef:
        """
        [Client.delete_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer_tls_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_relational_database(
        self,
        relationalDatabaseName: str,
        skipFinalSnapshot: bool = None,
        finalRelationalDatabaseSnapshotName: str = None,
    ) -> DeleteRelationalDatabaseResultTypeDef:
        """
        [Client.delete_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_relational_database)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_relational_database_snapshot(
        self, relationalDatabaseSnapshotName: str
    ) -> DeleteRelationalDatabaseSnapshotResultTypeDef:
        """
        [Client.delete_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.delete_relational_database_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_disk(self, diskName: str) -> DetachDiskResultTypeDef:
        """
        [Client.detach_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.detach_disk)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_instances_from_load_balancer(
        self, loadBalancerName: str, instanceNames: List[str]
    ) -> DetachInstancesFromLoadBalancerResultTypeDef:
        """
        [Client.detach_instances_from_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.detach_instances_from_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_static_ip(self, staticIpName: str) -> DetachStaticIpResultTypeDef:
        """
        [Client.detach_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.detach_static_ip)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_add_on(
        self, addOnType: Literal["AutoSnapshot"], resourceName: str
    ) -> DisableAddOnResultTypeDef:
        """
        [Client.disable_add_on documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.disable_add_on)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def download_default_key_pair(self) -> DownloadDefaultKeyPairResultTypeDef:
        """
        [Client.download_default_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.download_default_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_add_on(
        self, resourceName: str, addOnRequest: AddOnRequestTypeDef
    ) -> EnableAddOnResultTypeDef:
        """
        [Client.enable_add_on documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.enable_add_on)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_snapshot(self, sourceSnapshotName: str) -> ExportSnapshotResultTypeDef:
        """
        [Client.export_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.export_snapshot)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_active_names(self, pageToken: str = None) -> GetActiveNamesResultTypeDef:
        """
        [Client.get_active_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_active_names)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_auto_snapshots(self, resourceName: str) -> GetAutoSnapshotsResultTypeDef:
        """
        [Client.get_auto_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_auto_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_blueprints(
        self, includeInactive: bool = None, pageToken: str = None
    ) -> GetBlueprintsResultTypeDef:
        """
        [Client.get_blueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_blueprints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bundles(
        self, includeInactive: bool = None, pageToken: str = None
    ) -> GetBundlesResultTypeDef:
        """
        [Client.get_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_bundles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cloud_formation_stack_records(
        self, pageToken: str = None
    ) -> GetCloudFormationStackRecordsResultTypeDef:
        """
        [Client.get_cloud_formation_stack_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_cloud_formation_stack_records)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_disk(self, diskName: str) -> GetDiskResultTypeDef:
        """
        [Client.get_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_disk)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_disk_snapshot(self, diskSnapshotName: str) -> GetDiskSnapshotResultTypeDef:
        """
        [Client.get_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_disk_snapshots(self, pageToken: str = None) -> GetDiskSnapshotsResultTypeDef:
        """
        [Client.get_disk_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_disks(self, pageToken: str = None) -> GetDisksResultTypeDef:
        """
        [Client.get_disks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_disks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_domain(self, domainName: str) -> GetDomainResultTypeDef:
        """
        [Client.get_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_domains(self, pageToken: str = None) -> GetDomainsResultTypeDef:
        """
        [Client.get_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_domains)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_export_snapshot_records(
        self, pageToken: str = None
    ) -> GetExportSnapshotRecordsResultTypeDef:
        """
        [Client.get_export_snapshot_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_export_snapshot_records)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instance(self, instanceName: str) -> GetInstanceResultTypeDef:
        """
        [Client.get_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instance_access_details(
        self, instanceName: str, protocol: Literal["ssh", "rdp"] = None
    ) -> GetInstanceAccessDetailsResultTypeDef:
        """
        [Client.get_instance_access_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_instance_access_details)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instance_metric_data(
        self,
        instanceName: str,
        metricName: Literal[
            "CPUUtilization",
            "NetworkIn",
            "NetworkOut",
            "StatusCheckFailed",
            "StatusCheckFailed_Instance",
            "StatusCheckFailed_System",
        ],
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        statistics: List[Literal["Minimum", "Maximum", "Sum", "Average", "SampleCount"]],
    ) -> GetInstanceMetricDataResultTypeDef:
        """
        [Client.get_instance_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_instance_metric_data)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instance_port_states(self, instanceName: str) -> GetInstancePortStatesResultTypeDef:
        """
        [Client.get_instance_port_states documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_instance_port_states)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instance_snapshot(self, instanceSnapshotName: str) -> GetInstanceSnapshotResultTypeDef:
        """
        [Client.get_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instance_snapshots(self, pageToken: str = None) -> GetInstanceSnapshotsResultTypeDef:
        """
        [Client.get_instance_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instance_state(self, instanceName: str) -> GetInstanceStateResultTypeDef:
        """
        [Client.get_instance_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_instance_state)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_instances(self, pageToken: str = None) -> GetInstancesResultTypeDef:
        """
        [Client.get_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_key_pair(self, keyPairName: str) -> GetKeyPairResultTypeDef:
        """
        [Client.get_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_key_pairs(self, pageToken: str = None) -> GetKeyPairsResultTypeDef:
        """
        [Client.get_key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_key_pairs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_load_balancer(self, loadBalancerName: str) -> GetLoadBalancerResultTypeDef:
        """
        [Client.get_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_load_balancer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_load_balancer_metric_data(
        self,
        loadBalancerName: str,
        metricName: Literal[
            "ClientTLSNegotiationErrorCount",
            "HealthyHostCount",
            "UnhealthyHostCount",
            "HTTPCode_LB_4XX_Count",
            "HTTPCode_LB_5XX_Count",
            "HTTPCode_Instance_2XX_Count",
            "HTTPCode_Instance_3XX_Count",
            "HTTPCode_Instance_4XX_Count",
            "HTTPCode_Instance_5XX_Count",
            "InstanceResponseTime",
            "RejectedConnectionCount",
            "RequestCount",
        ],
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        statistics: List[Literal["Minimum", "Maximum", "Sum", "Average", "SampleCount"]],
    ) -> GetLoadBalancerMetricDataResultTypeDef:
        """
        [Client.get_load_balancer_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_metric_data)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_load_balancer_tls_certificates(
        self, loadBalancerName: str
    ) -> GetLoadBalancerTlsCertificatesResultTypeDef:
        """
        [Client.get_load_balancer_tls_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_tls_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_load_balancers(self, pageToken: str = None) -> GetLoadBalancersResultTypeDef:
        """
        [Client.get_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_load_balancers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_operation(self, operationId: str) -> GetOperationResultTypeDef:
        """
        [Client.get_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_operation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_operations(self, pageToken: str = None) -> GetOperationsResultTypeDef:
        """
        [Client.get_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_operations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_operations_for_resource(
        self, resourceName: str, pageToken: str = None
    ) -> GetOperationsForResourceResultTypeDef:
        """
        [Client.get_operations_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_operations_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_regions(
        self,
        includeAvailabilityZones: bool = None,
        includeRelationalDatabaseAvailabilityZones: bool = None,
    ) -> GetRegionsResultTypeDef:
        """
        [Client.get_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_regions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_database(
        self, relationalDatabaseName: str
    ) -> GetRelationalDatabaseResultTypeDef:
        """
        [Client.get_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_database)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_database_blueprints(
        self, pageToken: str = None
    ) -> GetRelationalDatabaseBlueprintsResultTypeDef:
        """
        [Client.get_relational_database_blueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_database_blueprints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_database_bundles(
        self, pageToken: str = None
    ) -> GetRelationalDatabaseBundlesResultTypeDef:
        """
        [Client.get_relational_database_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_database_bundles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_database_events(
        self, relationalDatabaseName: str, durationInMinutes: int = None, pageToken: str = None
    ) -> GetRelationalDatabaseEventsResultTypeDef:
        """
        [Client.get_relational_database_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_database_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_database_log_events(
        self,
        relationalDatabaseName: str,
        logStreamName: str,
        startTime: datetime = None,
        endTime: datetime = None,
        startFromHead: bool = None,
        pageToken: str = None,
    ) -> GetRelationalDatabaseLogEventsResultTypeDef:
        """
        [Client.get_relational_database_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_database_log_streams(
        self, relationalDatabaseName: str
    ) -> GetRelationalDatabaseLogStreamsResultTypeDef:
        """
        [Client.get_relational_database_log_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_streams)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_database_master_user_password(
        self,
        relationalDatabaseName: str,
        passwordVersion: Literal["CURRENT", "PREVIOUS", "PENDING"] = None,
    ) -> GetRelationalDatabaseMasterUserPasswordResultTypeDef:
        """
        [Client.get_relational_database_master_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_database_master_user_password)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_database_metric_data(
        self,
        relationalDatabaseName: str,
        metricName: Literal[
            "CPUUtilization",
            "DatabaseConnections",
            "DiskQueueDepth",
            "FreeStorageSpace",
            "NetworkReceiveThroughput",
            "NetworkTransmitThroughput",
        ],
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        statistics: List[Literal["Minimum", "Maximum", "Sum", "Average", "SampleCount"]],
    ) -> GetRelationalDatabaseMetricDataResultTypeDef:
        """
        [Client.get_relational_database_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_database_metric_data)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_database_parameters(
        self, relationalDatabaseName: str, pageToken: str = None
    ) -> GetRelationalDatabaseParametersResultTypeDef:
        """
        [Client.get_relational_database_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_database_parameters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_database_snapshot(
        self, relationalDatabaseSnapshotName: str
    ) -> GetRelationalDatabaseSnapshotResultTypeDef:
        """
        [Client.get_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_database_snapshots(
        self, pageToken: str = None
    ) -> GetRelationalDatabaseSnapshotsResultTypeDef:
        """
        [Client.get_relational_database_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_relational_databases(
        self, pageToken: str = None
    ) -> GetRelationalDatabasesResultTypeDef:
        """
        [Client.get_relational_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_relational_databases)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_static_ip(self, staticIpName: str) -> GetStaticIpResultTypeDef:
        """
        [Client.get_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_static_ip)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_static_ips(self, pageToken: str = None) -> GetStaticIpsResultTypeDef:
        """
        [Client.get_static_ips documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.get_static_ips)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_key_pair(self, keyPairName: str, publicKeyBase64: str) -> ImportKeyPairResultTypeDef:
        """
        [Client.import_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.import_key_pair)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def is_vpc_peered(self) -> IsVpcPeeredResultTypeDef:
        """
        [Client.is_vpc_peered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.is_vpc_peered)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def open_instance_public_ports(
        self, portInfo: PortInfoTypeDef, instanceName: str
    ) -> OpenInstancePublicPortsResultTypeDef:
        """
        [Client.open_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.open_instance_public_ports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def peer_vpc(self) -> PeerVpcResultTypeDef:
        """
        [Client.peer_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.peer_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_instance_public_ports(
        self, portInfos: List[PortInfoTypeDef], instanceName: str
    ) -> PutInstancePublicPortsResultTypeDef:
        """
        [Client.put_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.put_instance_public_ports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot_instance(self, instanceName: str) -> RebootInstanceResultTypeDef:
        """
        [Client.reboot_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.reboot_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot_relational_database(
        self, relationalDatabaseName: str
    ) -> RebootRelationalDatabaseResultTypeDef:
        """
        [Client.reboot_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.reboot_relational_database)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def release_static_ip(self, staticIpName: str) -> ReleaseStaticIpResultTypeDef:
        """
        [Client.release_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.release_static_ip)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_instance(self, instanceName: str) -> StartInstanceResultTypeDef:
        """
        [Client.start_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.start_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_relational_database(
        self, relationalDatabaseName: str
    ) -> StartRelationalDatabaseResultTypeDef:
        """
        [Client.start_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.start_relational_database)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_instance(self, instanceName: str, force: bool = None) -> StopInstanceResultTypeDef:
        """
        [Client.stop_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.stop_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_relational_database(
        self, relationalDatabaseName: str, relationalDatabaseSnapshotName: str = None
    ) -> StopRelationalDatabaseResultTypeDef:
        """
        [Client.stop_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.stop_relational_database)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, resourceName: str, tags: List[TagTypeDef], resourceArn: str = None
    ) -> TagResourceResultTypeDef:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unpeer_vpc(self) -> UnpeerVpcResultTypeDef:
        """
        [Client.unpeer_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.unpeer_vpc)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(
        self, resourceName: str, tagKeys: List[str], resourceArn: str = None
    ) -> UntagResourceResultTypeDef:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_domain_entry(
        self, domainName: str, domainEntry: DomainEntryTypeDef
    ) -> UpdateDomainEntryResultTypeDef:
        """
        [Client.update_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.update_domain_entry)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_load_balancer_attribute(
        self,
        loadBalancerName: str,
        attributeName: Literal[
            "HealthCheckPath",
            "SessionStickinessEnabled",
            "SessionStickiness_LB_CookieDurationSeconds",
        ],
        attributeValue: str,
    ) -> UpdateLoadBalancerAttributeResultTypeDef:
        """
        [Client.update_load_balancer_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.update_load_balancer_attribute)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_relational_database(
        self,
        relationalDatabaseName: str,
        masterUserPassword: str = None,
        rotateMasterUserPassword: bool = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        enableBackupRetention: bool = None,
        disableBackupRetention: bool = None,
        publiclyAccessible: bool = None,
        applyImmediately: bool = None,
    ) -> UpdateRelationalDatabaseResultTypeDef:
        """
        [Client.update_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.update_relational_database)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_relational_database_parameters(
        self, relationalDatabaseName: str, parameters: List[RelationalDatabaseParameterTypeDef]
    ) -> UpdateRelationalDatabaseParametersResultTypeDef:
        """
        [Client.update_relational_database_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Client.update_relational_database_parameters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_active_names"]
    ) -> paginator_scope.GetActiveNamesPaginator:
        """
        [Paginator.GetActiveNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_blueprints"]
    ) -> paginator_scope.GetBlueprintsPaginator:
        """
        [Paginator.GetBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_bundles"]
    ) -> paginator_scope.GetBundlesPaginator:
        """
        [Paginator.GetBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetBundles)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_cloud_formation_stack_records"]
    ) -> paginator_scope.GetCloudFormationStackRecordsPaginator:
        """
        [Paginator.GetCloudFormationStackRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_disk_snapshots"]
    ) -> paginator_scope.GetDiskSnapshotsPaginator:
        """
        [Paginator.GetDiskSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_disks"]
    ) -> paginator_scope.GetDisksPaginator:
        """
        [Paginator.GetDisks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetDisks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_domains"]
    ) -> paginator_scope.GetDomainsPaginator:
        """
        [Paginator.GetDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetDomains)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_export_snapshot_records"]
    ) -> paginator_scope.GetExportSnapshotRecordsPaginator:
        """
        [Paginator.GetExportSnapshotRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_instance_snapshots"]
    ) -> paginator_scope.GetInstanceSnapshotsPaginator:
        """
        [Paginator.GetInstanceSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_instances"]
    ) -> paginator_scope.GetInstancesPaginator:
        """
        [Paginator.GetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_key_pairs"]
    ) -> paginator_scope.GetKeyPairsPaginator:
        """
        [Paginator.GetKeyPairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_load_balancers"]
    ) -> paginator_scope.GetLoadBalancersPaginator:
        """
        [Paginator.GetLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_operations"]
    ) -> paginator_scope.GetOperationsPaginator:
        """
        [Paginator.GetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetOperations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_relational_database_blueprints"]
    ) -> paginator_scope.GetRelationalDatabaseBlueprintsPaginator:
        """
        [Paginator.GetRelationalDatabaseBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_relational_database_bundles"]
    ) -> paginator_scope.GetRelationalDatabaseBundlesPaginator:
        """
        [Paginator.GetRelationalDatabaseBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_relational_database_events"]
    ) -> paginator_scope.GetRelationalDatabaseEventsPaginator:
        """
        [Paginator.GetRelationalDatabaseEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_relational_database_parameters"]
    ) -> paginator_scope.GetRelationalDatabaseParametersPaginator:
        """
        [Paginator.GetRelationalDatabaseParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_relational_database_snapshots"]
    ) -> paginator_scope.GetRelationalDatabaseSnapshotsPaginator:
        """
        [Paginator.GetRelationalDatabaseSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_relational_databases"]
    ) -> paginator_scope.GetRelationalDatabasesPaginator:
        """
        [Paginator.GetRelationalDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_static_ips"]
    ) -> paginator_scope.GetStaticIpsPaginator:
        """
        [Paginator.GetStaticIps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AccountSetupInProgressException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    NotFoundException: Boto3ClientError
    OperationFailureException: Boto3ClientError
    ServiceException: Boto3ClientError
    UnauthenticatedException: Boto3ClientError
