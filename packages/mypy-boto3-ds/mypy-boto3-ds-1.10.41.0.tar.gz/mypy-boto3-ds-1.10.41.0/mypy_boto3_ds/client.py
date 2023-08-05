"Main interface for ds service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_ds.client as client_scope

# pylint: disable=import-self
import mypy_boto3_ds.paginator as paginator_scope
from mypy_boto3_ds.type_defs import (
    AcceptSharedDirectoryResultTypeDef,
    AttributeTypeDef,
    ConnectDirectoryResultTypeDef,
    CreateAliasResultTypeDef,
    CreateComputerResultTypeDef,
    CreateDirectoryResultTypeDef,
    CreateMicrosoftADResultTypeDef,
    CreateSnapshotResultTypeDef,
    CreateTrustResultTypeDef,
    DeleteDirectoryResultTypeDef,
    DeleteSnapshotResultTypeDef,
    DeleteTrustResultTypeDef,
    DescribeCertificateResultTypeDef,
    DescribeConditionalForwardersResultTypeDef,
    DescribeDirectoriesResultTypeDef,
    DescribeDomainControllersResultTypeDef,
    DescribeEventTopicsResultTypeDef,
    DescribeLDAPSSettingsResultTypeDef,
    DescribeSharedDirectoriesResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeTrustsResultTypeDef,
    DirectoryConnectSettingsTypeDef,
    DirectoryVpcSettingsTypeDef,
    GetDirectoryLimitsResultTypeDef,
    GetSnapshotLimitsResultTypeDef,
    IpRouteTypeDef,
    ListCertificatesResultTypeDef,
    ListIpRoutesResultTypeDef,
    ListLogSubscriptionsResultTypeDef,
    ListSchemaExtensionsResultTypeDef,
    ListTagsForResourceResultTypeDef,
    RadiusSettingsTypeDef,
    RegisterCertificateResultTypeDef,
    RejectSharedDirectoryResultTypeDef,
    ShareDirectoryResultTypeDef,
    ShareTargetTypeDef,
    StartSchemaExtensionResultTypeDef,
    TagTypeDef,
    UnshareDirectoryResultTypeDef,
    UnshareTargetTypeDef,
    UpdateTrustResultTypeDef,
    VerifyTrustResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DirectoryServiceClient",)


class DirectoryServiceClient(BaseClient):
    """
    [DirectoryService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_shared_directory(self, SharedDirectoryId: str) -> AcceptSharedDirectoryResultTypeDef:
        """
        [Client.accept_shared_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.accept_shared_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_ip_routes(
        self,
        DirectoryId: str,
        IpRoutes: List[IpRouteTypeDef],
        UpdateSecurityGroupForDirectoryControllers: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.add_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.add_ip_routes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_resource(self, ResourceId: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.add_tags_to_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_schema_extension(self, DirectoryId: str, SchemaExtensionId: str) -> Dict[str, Any]:
        """
        [Client.cancel_schema_extension documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.cancel_schema_extension)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def connect_directory(
        self,
        Name: str,
        Password: str,
        Size: Literal["Small", "Large"],
        ConnectSettings: DirectoryConnectSettingsTypeDef,
        ShortName: str = None,
        Description: str = None,
        Tags: List[TagTypeDef] = None,
    ) -> ConnectDirectoryResultTypeDef:
        """
        [Client.connect_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.connect_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_alias(self, DirectoryId: str, Alias: str) -> CreateAliasResultTypeDef:
        """
        [Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.create_alias)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_computer(
        self,
        DirectoryId: str,
        ComputerName: str,
        Password: str,
        OrganizationalUnitDistinguishedName: str = None,
        ComputerAttributes: List[AttributeTypeDef] = None,
    ) -> CreateComputerResultTypeDef:
        """
        [Client.create_computer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.create_computer)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.create_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.create_conditional_forwarder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_directory(
        self,
        Name: str,
        Password: str,
        Size: Literal["Small", "Large"],
        ShortName: str = None,
        Description: str = None,
        VpcSettings: DirectoryVpcSettingsTypeDef = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDirectoryResultTypeDef:
        """
        [Client.create_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.create_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_log_subscription(self, DirectoryId: str, LogGroupName: str) -> Dict[str, Any]:
        """
        [Client.create_log_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.create_log_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_microsoft_ad(
        self,
        Name: str,
        Password: str,
        VpcSettings: DirectoryVpcSettingsTypeDef,
        ShortName: str = None,
        Description: str = None,
        Edition: Literal["Enterprise", "Standard"] = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateMicrosoftADResultTypeDef:
        """
        [Client.create_microsoft_ad documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.create_microsoft_ad)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot(self, DirectoryId: str, Name: str = None) -> CreateSnapshotResultTypeDef:
        """
        [Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.create_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_trust(
        self,
        DirectoryId: str,
        RemoteDomainName: str,
        TrustPassword: str,
        TrustDirection: Literal["One-Way: Outgoing", "One-Way: Incoming", "Two-Way"],
        TrustType: Literal["Forest", "External"] = None,
        ConditionalForwarderIpAddrs: List[str] = None,
        SelectiveAuth: Literal["Enabled", "Disabled"] = None,
    ) -> CreateTrustResultTypeDef:
        """
        [Client.create_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.create_trust)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.delete_conditional_forwarder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_directory(self, DirectoryId: str) -> DeleteDirectoryResultTypeDef:
        """
        [Client.delete_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.delete_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_log_subscription(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Client.delete_log_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.delete_log_subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_snapshot(self, SnapshotId: str) -> DeleteSnapshotResultTypeDef:
        """
        [Client.delete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.delete_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_trust(
        self, TrustId: str, DeleteAssociatedConditionalForwarder: bool = None
    ) -> DeleteTrustResultTypeDef:
        """
        [Client.delete_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.delete_trust)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_certificate(self, DirectoryId: str, CertificateId: str) -> Dict[str, Any]:
        """
        [Client.deregister_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.deregister_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_event_topic(self, DirectoryId: str, TopicName: str) -> Dict[str, Any]:
        """
        [Client.deregister_event_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.deregister_event_topic)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_certificate(
        self, DirectoryId: str, CertificateId: str
    ) -> DescribeCertificateResultTypeDef:
        """
        [Client.describe_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.describe_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_conditional_forwarders(
        self, DirectoryId: str, RemoteDomainNames: List[str] = None
    ) -> DescribeConditionalForwardersResultTypeDef:
        """
        [Client.describe_conditional_forwarders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.describe_conditional_forwarders)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_directories(
        self, DirectoryIds: List[str] = None, NextToken: str = None, Limit: int = None
    ) -> DescribeDirectoriesResultTypeDef:
        """
        [Client.describe_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.describe_directories)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_domain_controllers(
        self,
        DirectoryId: str,
        DomainControllerIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeDomainControllersResultTypeDef:
        """
        [Client.describe_domain_controllers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.describe_domain_controllers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_topics(
        self, DirectoryId: str = None, TopicNames: List[str] = None
    ) -> DescribeEventTopicsResultTypeDef:
        """
        [Client.describe_event_topics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.describe_event_topics)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_ldaps_settings(
        self,
        DirectoryId: str,
        Type: Literal["Client"] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeLDAPSSettingsResultTypeDef:
        """
        [Client.describe_ldaps_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.describe_ldaps_settings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_shared_directories(
        self,
        OwnerDirectoryId: str,
        SharedDirectoryIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeSharedDirectoriesResultTypeDef:
        """
        [Client.describe_shared_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.describe_shared_directories)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_snapshots(
        self,
        DirectoryId: str = None,
        SnapshotIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeSnapshotsResultTypeDef:
        """
        [Client.describe_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.describe_snapshots)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_trusts(
        self,
        DirectoryId: str = None,
        TrustIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeTrustsResultTypeDef:
        """
        [Client.describe_trusts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.describe_trusts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_ldaps(self, DirectoryId: str, Type: Literal["Client"] = None) -> Dict[str, Any]:
        """
        [Client.disable_ldaps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.disable_ldaps)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_radius(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Client.disable_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.disable_radius)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_sso(
        self, DirectoryId: str, UserName: str = None, Password: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disable_sso documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.disable_sso)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_ldaps(self, DirectoryId: str, Type: Literal["Client"] = None) -> Dict[str, Any]:
        """
        [Client.enable_ldaps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.enable_ldaps)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_radius(
        self, DirectoryId: str, RadiusSettings: RadiusSettingsTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.enable_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.enable_radius)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_sso(
        self, DirectoryId: str, UserName: str = None, Password: str = None
    ) -> Dict[str, Any]:
        """
        [Client.enable_sso documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.enable_sso)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_directory_limits(self) -> GetDirectoryLimitsResultTypeDef:
        """
        [Client.get_directory_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.get_directory_limits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_snapshot_limits(self, DirectoryId: str) -> GetSnapshotLimitsResultTypeDef:
        """
        [Client.get_snapshot_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.get_snapshot_limits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_certificates(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListCertificatesResultTypeDef:
        """
        [Client.list_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.list_certificates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_ip_routes(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListIpRoutesResultTypeDef:
        """
        [Client.list_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.list_ip_routes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_log_subscriptions(
        self, DirectoryId: str = None, NextToken: str = None, Limit: int = None
    ) -> ListLogSubscriptionsResultTypeDef:
        """
        [Client.list_log_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.list_log_subscriptions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_schema_extensions(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListSchemaExtensionsResultTypeDef:
        """
        [Client.list_schema_extensions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.list_schema_extensions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceId: str, NextToken: str = None, Limit: int = None
    ) -> ListTagsForResourceResultTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_certificate(
        self, DirectoryId: str, CertificateData: str
    ) -> RegisterCertificateResultTypeDef:
        """
        [Client.register_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.register_certificate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_event_topic(self, DirectoryId: str, TopicName: str) -> Dict[str, Any]:
        """
        [Client.register_event_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.register_event_topic)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_shared_directory(self, SharedDirectoryId: str) -> RejectSharedDirectoryResultTypeDef:
        """
        [Client.reject_shared_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.reject_shared_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_ip_routes(self, DirectoryId: str, CidrIps: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.remove_ip_routes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_resource(self, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.remove_tags_from_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_user_password(
        self, DirectoryId: str, UserName: str, NewPassword: str
    ) -> Dict[str, Any]:
        """
        [Client.reset_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.reset_user_password)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_from_snapshot(self, SnapshotId: str) -> Dict[str, Any]:
        """
        [Client.restore_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.restore_from_snapshot)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def share_directory(
        self,
        DirectoryId: str,
        ShareTarget: ShareTargetTypeDef,
        ShareMethod: Literal["ORGANIZATIONS", "HANDSHAKE"],
        ShareNotes: str = None,
    ) -> ShareDirectoryResultTypeDef:
        """
        [Client.share_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.share_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_schema_extension(
        self,
        DirectoryId: str,
        CreateSnapshotBeforeSchemaExtension: bool,
        LdifContent: str,
        Description: str,
    ) -> StartSchemaExtensionResultTypeDef:
        """
        [Client.start_schema_extension documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.start_schema_extension)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unshare_directory(
        self, DirectoryId: str, UnshareTarget: UnshareTargetTypeDef
    ) -> UnshareDirectoryResultTypeDef:
        """
        [Client.unshare_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.unshare_directory)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.update_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.update_conditional_forwarder)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_number_of_domain_controllers(
        self, DirectoryId: str, DesiredNumber: int
    ) -> Dict[str, Any]:
        """
        [Client.update_number_of_domain_controllers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.update_number_of_domain_controllers)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_radius(
        self, DirectoryId: str, RadiusSettings: RadiusSettingsTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.update_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.update_radius)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_trust(
        self, TrustId: str, SelectiveAuth: Literal["Enabled", "Disabled"] = None
    ) -> UpdateTrustResultTypeDef:
        """
        [Client.update_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.update_trust)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def verify_trust(self, TrustId: str) -> VerifyTrustResultTypeDef:
        """
        [Client.verify_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Client.verify_trust)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_directories"]
    ) -> paginator_scope.DescribeDirectoriesPaginator:
        """
        [Paginator.DescribeDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_domain_controllers"]
    ) -> paginator_scope.DescribeDomainControllersPaginator:
        """
        [Paginator.DescribeDomainControllers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_shared_directories"]
    ) -> paginator_scope.DescribeSharedDirectoriesPaginator:
        """
        [Paginator.DescribeSharedDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> paginator_scope.DescribeSnapshotsPaginator:
        """
        [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_trusts"]
    ) -> paginator_scope.DescribeTrustsPaginator:
        """
        [Paginator.DescribeTrusts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_ip_routes"]
    ) -> paginator_scope.ListIpRoutesPaginator:
        """
        [Paginator.ListIpRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_log_subscriptions"]
    ) -> paginator_scope.ListLogSubscriptionsPaginator:
        """
        [Paginator.ListLogSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_schema_extensions"]
    ) -> paginator_scope.ListSchemaExtensionsPaginator:
        """
        [Paginator.ListSchemaExtensions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource)
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    AuthenticationFailedException: Boto3ClientError
    CertificateAlreadyExistsException: Boto3ClientError
    CertificateDoesNotExistException: Boto3ClientError
    CertificateInUseException: Boto3ClientError
    CertificateLimitExceededException: Boto3ClientError
    ClientError: Boto3ClientError
    ClientException: Boto3ClientError
    DirectoryAlreadySharedException: Boto3ClientError
    DirectoryDoesNotExistException: Boto3ClientError
    DirectoryLimitExceededException: Boto3ClientError
    DirectoryNotSharedException: Boto3ClientError
    DirectoryUnavailableException: Boto3ClientError
    DomainControllerLimitExceededException: Boto3ClientError
    EntityAlreadyExistsException: Boto3ClientError
    EntityDoesNotExistException: Boto3ClientError
    InsufficientPermissionsException: Boto3ClientError
    InvalidCertificateException: Boto3ClientError
    InvalidLDAPSStatusException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidPasswordException: Boto3ClientError
    InvalidTargetException: Boto3ClientError
    IpRouteLimitExceededException: Boto3ClientError
    NoAvailableCertificateException: Boto3ClientError
    OrganizationsException: Boto3ClientError
    ServiceException: Boto3ClientError
    ShareLimitExceededException: Boto3ClientError
    SnapshotLimitExceededException: Boto3ClientError
    TagLimitExceededException: Boto3ClientError
    UnsupportedOperationException: Boto3ClientError
    UserDoesNotExistException: Boto3ClientError
