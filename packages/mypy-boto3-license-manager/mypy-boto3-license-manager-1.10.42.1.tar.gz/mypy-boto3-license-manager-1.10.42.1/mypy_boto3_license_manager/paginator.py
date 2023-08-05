"Main interface for license-manager service Paginators"
from __future__ import annotations

from typing import Generator, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_license_manager.type_defs import (
    FilterTypeDef,
    InventoryFilterTypeDef,
    ListAssociationsForLicenseConfigurationResponseTypeDef,
    ListLicenseConfigurationsResponseTypeDef,
    ListLicenseSpecificationsForResourceResponseTypeDef,
    ListResourceInventoryResponseTypeDef,
    ListUsageForLicenseConfigurationResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListAssociationsForLicenseConfigurationPaginator",
    "ListLicenseConfigurationsPaginator",
    "ListLicenseSpecificationsForResourcePaginator",
    "ListResourceInventoryPaginator",
    "ListUsageForLicenseConfigurationPaginator",
)


class ListAssociationsForLicenseConfigurationPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociationsForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, LicenseConfigurationArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListAssociationsForLicenseConfigurationResponseTypeDef, None, None]:
        """
        [ListAssociationsForLicenseConfiguration.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration.paginate)
        """


class ListLicenseConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListLicenseConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LicenseConfigurationArns: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListLicenseConfigurationsResponseTypeDef, None, None]:
        """
        [ListLicenseConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations.paginate)
        """


class ListLicenseSpecificationsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListLicenseSpecificationsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListLicenseSpecificationsForResourceResponseTypeDef, None, None]:
        """
        [ListLicenseSpecificationsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource.paginate)
        """


class ListResourceInventoryPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[InventoryFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListResourceInventoryResponseTypeDef, None, None]:
        """
        [ListResourceInventory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory.paginate)
        """


class ListUsageForLicenseConfigurationPaginator(Boto3Paginator):
    """
    [Paginator.ListUsageForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LicenseConfigurationArn: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListUsageForLicenseConfigurationResponseTypeDef, None, None]:
        """
        [ListUsageForLicenseConfiguration.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration.paginate)
        """
