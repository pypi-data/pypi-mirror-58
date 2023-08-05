"Main interface for license-manager service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_license_manager.client as client_scope

# pylint: disable=import-self
import mypy_boto3_license_manager.paginator as paginator_scope
from mypy_boto3_license_manager.type_defs import (
    CreateLicenseConfigurationResponseTypeDef,
    FilterTypeDef,
    GetLicenseConfigurationResponseTypeDef,
    GetServiceSettingsResponseTypeDef,
    InventoryFilterTypeDef,
    LicenseSpecificationTypeDef,
    ListAssociationsForLicenseConfigurationResponseTypeDef,
    ListFailuresForLicenseConfigurationOperationsResponseTypeDef,
    ListLicenseConfigurationsResponseTypeDef,
    ListLicenseSpecificationsForResourceResponseTypeDef,
    ListResourceInventoryResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsageForLicenseConfigurationResponseTypeDef,
    OrganizationConfigurationTypeDef,
    ProductInformationTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LicenseManagerClient",)


class LicenseManagerClient(BaseClient):
    """
    [LicenseManager.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_license_configuration(
        self,
        Name: str,
        LicenseCountingType: Literal["vCPU", "Instance", "Core", "Socket"],
        Description: str = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        LicenseRules: List[str] = None,
        Tags: List[TagTypeDef] = None,
        ProductInformationList: List[ProductInformationTypeDef] = None,
    ) -> CreateLicenseConfigurationResponseTypeDef:
        """
        [Client.create_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.create_license_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_license_configuration(self, LicenseConfigurationArn: str) -> Dict[str, Any]:
        """
        [Client.delete_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.delete_license_configuration)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_license_configuration(
        self, LicenseConfigurationArn: str
    ) -> GetLicenseConfigurationResponseTypeDef:
        """
        [Client.get_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.get_license_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service_settings(self) -> GetServiceSettingsResponseTypeDef:
        """
        [Client.get_service_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.get_service_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_associations_for_license_configuration(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAssociationsForLicenseConfigurationResponseTypeDef:
        """
        [Client.list_associations_for_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.list_associations_for_license_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_failures_for_license_configuration_operations(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListFailuresForLicenseConfigurationOperationsResponseTypeDef:
        """
        [Client.list_failures_for_license_configuration_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.list_failures_for_license_configuration_operations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_license_configurations(
        self,
        LicenseConfigurationArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> ListLicenseConfigurationsResponseTypeDef:
        """
        [Client.list_license_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.list_license_configurations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_license_specifications_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListLicenseSpecificationsForResourceResponseTypeDef:
        """
        [Client.list_license_specifications_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.list_license_specifications_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_inventory(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[InventoryFilterTypeDef] = None,
    ) -> ListResourceInventoryResponseTypeDef:
        """
        [Client.list_resource_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.list_resource_inventory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_usage_for_license_configuration(
        self,
        LicenseConfigurationArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> ListUsageForLicenseConfigurationResponseTypeDef:
        """
        [Client.list_usage_for_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.list_usage_for_license_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_license_configuration(
        self,
        LicenseConfigurationArn: str,
        LicenseConfigurationStatus: Literal["AVAILABLE", "DISABLED"] = None,
        LicenseRules: List[str] = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        Name: str = None,
        Description: str = None,
        ProductInformationList: List[ProductInformationTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.update_license_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_license_specifications_for_resource(
        self,
        ResourceArn: str,
        AddLicenseSpecifications: List[LicenseSpecificationTypeDef] = None,
        RemoveLicenseSpecifications: List[LicenseSpecificationTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_license_specifications_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.update_license_specifications_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_service_settings(
        self,
        S3BucketArn: str = None,
        SnsTopicArn: str = None,
        OrganizationConfiguration: OrganizationConfigurationTypeDef = None,
        EnableCrossAccountsDiscovery: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_service_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Client.update_service_settings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_associations_for_license_configuration"]
    ) -> paginator_scope.ListAssociationsForLicenseConfigurationPaginator:
        """
        [Paginator.ListAssociationsForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_license_configurations"]
    ) -> paginator_scope.ListLicenseConfigurationsPaginator:
        """
        [Paginator.ListLicenseConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_license_specifications_for_resource"]
    ) -> paginator_scope.ListLicenseSpecificationsForResourcePaginator:
        """
        [Paginator.ListLicenseSpecificationsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_inventory"]
    ) -> paginator_scope.ListResourceInventoryPaginator:
        """
        [Paginator.ListResourceInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_usage_for_license_configuration"]
    ) -> paginator_scope.ListUsageForLicenseConfigurationPaginator:
        """
        [Paginator.ListUsageForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.42/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AuthorizationException: Boto3ClientError
    ClientError: Boto3ClientError
    FailedDependencyException: Boto3ClientError
    FilterLimitExceededException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidResourceStateException: Boto3ClientError
    LicenseUsageException: Boto3ClientError
    RateLimitExceededException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ServerInternalException: Boto3ClientError
