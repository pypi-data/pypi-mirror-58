"Main interface for worklink service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_worklink.client as client_scope
from mypy_boto3_worklink.type_defs import (
    AssociateWebsiteAuthorizationProviderResponseTypeDef,
    AssociateWebsiteCertificateAuthorityResponseTypeDef,
    CreateFleetResponseTypeDef,
    DescribeAuditStreamConfigurationResponseTypeDef,
    DescribeCompanyNetworkConfigurationResponseTypeDef,
    DescribeDevicePolicyConfigurationResponseTypeDef,
    DescribeDeviceResponseTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeFleetMetadataResponseTypeDef,
    DescribeIdentityProviderConfigurationResponseTypeDef,
    DescribeWebsiteCertificateAuthorityResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListFleetsResponseTypeDef,
    ListWebsiteAuthorizationProvidersResponseTypeDef,
    ListWebsiteCertificateAuthoritiesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WorkLinkClient",)


class WorkLinkClient(BaseClient):
    """
    [WorkLink.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_domain(
        self, FleetArn: str, DomainName: str, AcmCertificateArn: str, DisplayName: str = None
    ) -> Dict[str, Any]:
        """
        [Client.associate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.associate_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_website_authorization_provider(
        self, FleetArn: str, AuthorizationProviderType: Literal["SAML"], DomainName: str = None
    ) -> AssociateWebsiteAuthorizationProviderResponseTypeDef:
        """
        [Client.associate_website_authorization_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.associate_website_authorization_provider)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_website_certificate_authority(
        self, FleetArn: str, Certificate: str, DisplayName: str = None
    ) -> AssociateWebsiteCertificateAuthorityResponseTypeDef:
        """
        [Client.associate_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.associate_website_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_fleet(
        self, FleetName: str, DisplayName: str = None, OptimizeForEndUserLocation: bool = None
    ) -> CreateFleetResponseTypeDef:
        """
        [Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.create_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_fleet(self, FleetArn: str) -> Dict[str, Any]:
        """
        [Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.delete_fleet)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_audit_stream_configuration(
        self, FleetArn: str
    ) -> DescribeAuditStreamConfigurationResponseTypeDef:
        """
        [Client.describe_audit_stream_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.describe_audit_stream_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_company_network_configuration(
        self, FleetArn: str
    ) -> DescribeCompanyNetworkConfigurationResponseTypeDef:
        """
        [Client.describe_company_network_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.describe_company_network_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_device(self, FleetArn: str, DeviceId: str) -> DescribeDeviceResponseTypeDef:
        """
        [Client.describe_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.describe_device)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_device_policy_configuration(
        self, FleetArn: str
    ) -> DescribeDevicePolicyConfigurationResponseTypeDef:
        """
        [Client.describe_device_policy_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.describe_device_policy_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_domain(self, FleetArn: str, DomainName: str) -> DescribeDomainResponseTypeDef:
        """
        [Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.describe_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_fleet_metadata(self, FleetArn: str) -> DescribeFleetMetadataResponseTypeDef:
        """
        [Client.describe_fleet_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.describe_fleet_metadata)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_identity_provider_configuration(
        self, FleetArn: str
    ) -> DescribeIdentityProviderConfigurationResponseTypeDef:
        """
        [Client.describe_identity_provider_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.describe_identity_provider_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_website_certificate_authority(
        self, FleetArn: str, WebsiteCaId: str
    ) -> DescribeWebsiteCertificateAuthorityResponseTypeDef:
        """
        [Client.describe_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.describe_website_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_domain(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        [Client.disassociate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.disassociate_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_website_authorization_provider(
        self, FleetArn: str, AuthorizationProviderId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_website_authorization_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.disassociate_website_authorization_provider)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_website_certificate_authority(
        self, FleetArn: str, WebsiteCaId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.disassociate_website_certificate_authority)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_devices(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDevicesResponseTypeDef:
        """
        [Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.list_devices)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_domains(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDomainsResponseTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.list_domains)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_fleets(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListFleetsResponseTypeDef:
        """
        [Client.list_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.list_fleets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_website_authorization_providers(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListWebsiteAuthorizationProvidersResponseTypeDef:
        """
        [Client.list_website_authorization_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.list_website_authorization_providers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_website_certificate_authorities(
        self, FleetArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListWebsiteCertificateAuthoritiesResponseTypeDef:
        """
        [Client.list_website_certificate_authorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.list_website_certificate_authorities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_domain_access(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        [Client.restore_domain_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.restore_domain_access)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_domain_access(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        [Client.revoke_domain_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.revoke_domain_access)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def sign_out_user(self, FleetArn: str, Username: str) -> Dict[str, Any]:
        """
        [Client.sign_out_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.sign_out_user)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_audit_stream_configuration(
        self, FleetArn: str, AuditStreamArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_audit_stream_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.update_audit_stream_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_company_network_configuration(
        self, FleetArn: str, VpcId: str, SubnetIds: List[str], SecurityGroupIds: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.update_company_network_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.update_company_network_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_device_policy_configuration(
        self, FleetArn: str, DeviceCaCertificate: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_device_policy_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.update_device_policy_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_domain_metadata(
        self, FleetArn: str, DomainName: str, DisplayName: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_domain_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.update_domain_metadata)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_fleet_metadata(
        self, FleetArn: str, DisplayName: str = None, OptimizeForEndUserLocation: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.update_fleet_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.update_fleet_metadata)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_identity_provider_configuration(
        self,
        FleetArn: str,
        IdentityProviderType: Literal["SAML"],
        IdentityProviderSamlMetadata: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_identity_provider_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/worklink.html#WorkLink.Client.update_identity_provider_configuration)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
