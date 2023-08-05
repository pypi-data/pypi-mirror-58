"Main interface for lightsail service Paginators"
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_lightsail.type_defs import (
    GetActiveNamesResultTypeDef,
    GetBlueprintsResultTypeDef,
    GetBundlesResultTypeDef,
    GetCloudFormationStackRecordsResultTypeDef,
    GetDiskSnapshotsResultTypeDef,
    GetDisksResultTypeDef,
    GetDomainsResultTypeDef,
    GetExportSnapshotRecordsResultTypeDef,
    GetInstanceSnapshotsResultTypeDef,
    GetInstancesResultTypeDef,
    GetKeyPairsResultTypeDef,
    GetLoadBalancersResultTypeDef,
    GetOperationsResultTypeDef,
    GetRelationalDatabaseBlueprintsResultTypeDef,
    GetRelationalDatabaseBundlesResultTypeDef,
    GetRelationalDatabaseEventsResultTypeDef,
    GetRelationalDatabaseParametersResultTypeDef,
    GetRelationalDatabaseSnapshotsResultTypeDef,
    GetRelationalDatabasesResultTypeDef,
    GetStaticIpsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "GetActiveNamesPaginator",
    "GetBlueprintsPaginator",
    "GetBundlesPaginator",
    "GetCloudFormationStackRecordsPaginator",
    "GetDiskSnapshotsPaginator",
    "GetDisksPaginator",
    "GetDomainsPaginator",
    "GetExportSnapshotRecordsPaginator",
    "GetInstanceSnapshotsPaginator",
    "GetInstancesPaginator",
    "GetKeyPairsPaginator",
    "GetLoadBalancersPaginator",
    "GetOperationsPaginator",
    "GetRelationalDatabaseBlueprintsPaginator",
    "GetRelationalDatabaseBundlesPaginator",
    "GetRelationalDatabaseEventsPaginator",
    "GetRelationalDatabaseParametersPaginator",
    "GetRelationalDatabaseSnapshotsPaginator",
    "GetRelationalDatabasesPaginator",
    "GetStaticIpsPaginator",
)


class GetActiveNamesPaginator(Boto3Paginator):
    """
    [Paginator.GetActiveNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetActiveNamesResultTypeDef, None, None]:
        """
        [GetActiveNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames.paginate)
        """


class GetBlueprintsPaginator(Boto3Paginator):
    """
    [Paginator.GetBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, includeInactive: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetBlueprintsResultTypeDef, None, None]:
        """
        [GetBlueprints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints.paginate)
        """


class GetBundlesPaginator(Boto3Paginator):
    """
    [Paginator.GetBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetBundles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, includeInactive: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetBundlesResultTypeDef, None, None]:
        """
        [GetBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetBundles.paginate)
        """


class GetCloudFormationStackRecordsPaginator(Boto3Paginator):
    """
    [Paginator.GetCloudFormationStackRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetCloudFormationStackRecordsResultTypeDef, None, None]:
        """
        [GetCloudFormationStackRecords.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords.paginate)
        """


class GetDiskSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.GetDiskSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetDiskSnapshotsResultTypeDef, None, None]:
        """
        [GetDiskSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots.paginate)
        """


class GetDisksPaginator(Boto3Paginator):
    """
    [Paginator.GetDisks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetDisks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetDisksResultTypeDef, None, None]:
        """
        [GetDisks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetDisks.paginate)
        """


class GetDomainsPaginator(Boto3Paginator):
    """
    [Paginator.GetDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetDomains)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetDomainsResultTypeDef, None, None]:
        """
        [GetDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetDomains.paginate)
        """


class GetExportSnapshotRecordsPaginator(Boto3Paginator):
    """
    [Paginator.GetExportSnapshotRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetExportSnapshotRecordsResultTypeDef, None, None]:
        """
        [GetExportSnapshotRecords.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords.paginate)
        """


class GetInstanceSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.GetInstanceSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetInstanceSnapshotsResultTypeDef, None, None]:
        """
        [GetInstanceSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots.paginate)
        """


class GetInstancesPaginator(Boto3Paginator):
    """
    [Paginator.GetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetInstancesResultTypeDef, None, None]:
        """
        [GetInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetInstances.paginate)
        """


class GetKeyPairsPaginator(Boto3Paginator):
    """
    [Paginator.GetKeyPairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetKeyPairsResultTypeDef, None, None]:
        """
        [GetKeyPairs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs.paginate)
        """


class GetLoadBalancersPaginator(Boto3Paginator):
    """
    [Paginator.GetLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetLoadBalancersResultTypeDef, None, None]:
        """
        [GetLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers.paginate)
        """


class GetOperationsPaginator(Boto3Paginator):
    """
    [Paginator.GetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetOperations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetOperationsResultTypeDef, None, None]:
        """
        [GetOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetOperations.paginate)
        """


class GetRelationalDatabaseBlueprintsPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetRelationalDatabaseBlueprintsResultTypeDef, None, None]:
        """
        [GetRelationalDatabaseBlueprints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints.paginate)
        """


class GetRelationalDatabaseBundlesPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetRelationalDatabaseBundlesResultTypeDef, None, None]:
        """
        [GetRelationalDatabaseBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles.paginate)
        """


class GetRelationalDatabaseEventsPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        relationalDatabaseName: str,
        durationInMinutes: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[GetRelationalDatabaseEventsResultTypeDef, None, None]:
        """
        [GetRelationalDatabaseEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents.paginate)
        """


class GetRelationalDatabaseParametersPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, relationalDatabaseName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetRelationalDatabaseParametersResultTypeDef, None, None]:
        """
        [GetRelationalDatabaseParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters.paginate)
        """


class GetRelationalDatabaseSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetRelationalDatabaseSnapshotsResultTypeDef, None, None]:
        """
        [GetRelationalDatabaseSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots.paginate)
        """


class GetRelationalDatabasesPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetRelationalDatabasesResultTypeDef, None, None]:
        """
        [GetRelationalDatabases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases.paginate)
        """


class GetStaticIpsPaginator(Boto3Paginator):
    """
    [Paginator.GetStaticIps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[GetStaticIpsResultTypeDef, None, None]:
        """
        [GetStaticIps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps.paginate)
        """
