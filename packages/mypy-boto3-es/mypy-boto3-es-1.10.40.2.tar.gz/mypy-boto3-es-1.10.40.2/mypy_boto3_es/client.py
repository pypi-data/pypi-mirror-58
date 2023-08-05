"Main interface for es service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_es.client as client_scope

# pylint: disable=import-self
import mypy_boto3_es.paginator as paginator_scope
from mypy_boto3_es.type_defs import (
    CancelElasticsearchServiceSoftwareUpdateResponseTypeDef,
    CognitoOptionsTypeDef,
    CreateElasticsearchDomainResponseTypeDef,
    DeleteElasticsearchDomainResponseTypeDef,
    DescribeElasticsearchDomainConfigResponseTypeDef,
    DescribeElasticsearchDomainResponseTypeDef,
    DescribeElasticsearchDomainsResponseTypeDef,
    DescribeElasticsearchInstanceTypeLimitsResponseTypeDef,
    DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef,
    DescribeReservedElasticsearchInstancesResponseTypeDef,
    DomainEndpointOptionsTypeDef,
    EBSOptionsTypeDef,
    ElasticsearchClusterConfigTypeDef,
    EncryptionAtRestOptionsTypeDef,
    GetCompatibleElasticsearchVersionsResponseTypeDef,
    GetUpgradeHistoryResponseTypeDef,
    GetUpgradeStatusResponseTypeDef,
    ListDomainNamesResponseTypeDef,
    ListElasticsearchInstanceTypesResponseTypeDef,
    ListElasticsearchVersionsResponseTypeDef,
    ListTagsResponseTypeDef,
    LogPublishingOptionTypeDef,
    NodeToNodeEncryptionOptionsTypeDef,
    PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef,
    SnapshotOptionsTypeDef,
    StartElasticsearchServiceSoftwareUpdateResponseTypeDef,
    TagTypeDef,
    UpdateElasticsearchDomainConfigResponseTypeDef,
    UpgradeElasticsearchDomainResponseTypeDef,
    VPCOptionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticsearchServiceClient",)


class ElasticsearchServiceClient(BaseClient):
    """
    [ElasticsearchService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags(self, ARN: str, TagList: List[TagTypeDef]) -> None:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.add_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_elasticsearch_service_software_update(
        self, DomainName: str
    ) -> CancelElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        [Client.cancel_elasticsearch_service_software_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.cancel_elasticsearch_service_software_update)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_elasticsearch_domain(
        self,
        DomainName: str,
        ElasticsearchVersion: str = None,
        ElasticsearchClusterConfig: ElasticsearchClusterConfigTypeDef = None,
        EBSOptions: EBSOptionsTypeDef = None,
        AccessPolicies: str = None,
        SnapshotOptions: SnapshotOptionsTypeDef = None,
        VPCOptions: VPCOptionsTypeDef = None,
        CognitoOptions: CognitoOptionsTypeDef = None,
        EncryptionAtRestOptions: EncryptionAtRestOptionsTypeDef = None,
        NodeToNodeEncryptionOptions: NodeToNodeEncryptionOptionsTypeDef = None,
        AdvancedOptions: Dict[str, str] = None,
        LogPublishingOptions: Dict[
            Literal["INDEX_SLOW_LOGS", "SEARCH_SLOW_LOGS", "ES_APPLICATION_LOGS"],
            LogPublishingOptionTypeDef,
        ] = None,
        DomainEndpointOptions: DomainEndpointOptionsTypeDef = None,
    ) -> CreateElasticsearchDomainResponseTypeDef:
        """
        [Client.create_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.create_elasticsearch_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_elasticsearch_domain(
        self, DomainName: str
    ) -> DeleteElasticsearchDomainResponseTypeDef:
        """
        [Client.delete_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_elasticsearch_service_role(self) -> None:
        """
        [Client.delete_elasticsearch_service_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_service_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_elasticsearch_domain(
        self, DomainName: str
    ) -> DescribeElasticsearchDomainResponseTypeDef:
        """
        [Client.describe_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_elasticsearch_domain_config(
        self, DomainName: str
    ) -> DescribeElasticsearchDomainConfigResponseTypeDef:
        """
        [Client.describe_elasticsearch_domain_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_elasticsearch_domains(
        self, DomainNames: List[str]
    ) -> DescribeElasticsearchDomainsResponseTypeDef:
        """
        [Client.describe_elasticsearch_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domains)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_elasticsearch_instance_type_limits(
        self,
        InstanceType: Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        ElasticsearchVersion: str,
        DomainName: str = None,
    ) -> DescribeElasticsearchInstanceTypeLimitsResponseTypeDef:
        """
        [Client.describe_elasticsearch_instance_type_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_instance_type_limits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_elasticsearch_instance_offerings(
        self,
        ReservedElasticsearchInstanceOfferingId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef:
        """
        [Client.describe_reserved_elasticsearch_instance_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instance_offerings)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_reserved_elasticsearch_instances(
        self,
        ReservedElasticsearchInstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeReservedElasticsearchInstancesResponseTypeDef:
        """
        [Client.describe_reserved_elasticsearch_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instances)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_compatible_elasticsearch_versions(
        self, DomainName: str = None
    ) -> GetCompatibleElasticsearchVersionsResponseTypeDef:
        """
        [Client.get_compatible_elasticsearch_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.get_compatible_elasticsearch_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_upgrade_history(
        self, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> GetUpgradeHistoryResponseTypeDef:
        """
        [Client.get_upgrade_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.get_upgrade_history)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_upgrade_status(self, DomainName: str) -> GetUpgradeStatusResponseTypeDef:
        """
        [Client.get_upgrade_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.get_upgrade_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_domain_names(self) -> ListDomainNamesResponseTypeDef:
        """
        [Client.list_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.list_domain_names)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_elasticsearch_instance_types(
        self,
        ElasticsearchVersion: str,
        DomainName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListElasticsearchInstanceTypesResponseTypeDef:
        """
        [Client.list_elasticsearch_instance_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_instance_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_elasticsearch_versions(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListElasticsearchVersionsResponseTypeDef:
        """
        [Client.list_elasticsearch_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags(self, ARN: str) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.list_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def purchase_reserved_elasticsearch_instance_offering(
        self,
        ReservedElasticsearchInstanceOfferingId: str,
        ReservationName: str,
        InstanceCount: int = None,
    ) -> PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef:
        """
        [Client.purchase_reserved_elasticsearch_instance_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.purchase_reserved_elasticsearch_instance_offering)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags(self, ARN: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.remove_tags)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_elasticsearch_service_software_update(
        self, DomainName: str
    ) -> StartElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        [Client.start_elasticsearch_service_software_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.start_elasticsearch_service_software_update)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_elasticsearch_domain_config(
        self,
        DomainName: str,
        ElasticsearchClusterConfig: ElasticsearchClusterConfigTypeDef = None,
        EBSOptions: EBSOptionsTypeDef = None,
        SnapshotOptions: SnapshotOptionsTypeDef = None,
        VPCOptions: VPCOptionsTypeDef = None,
        CognitoOptions: CognitoOptionsTypeDef = None,
        AdvancedOptions: Dict[str, str] = None,
        AccessPolicies: str = None,
        LogPublishingOptions: Dict[
            Literal["INDEX_SLOW_LOGS", "SEARCH_SLOW_LOGS", "ES_APPLICATION_LOGS"],
            LogPublishingOptionTypeDef,
        ] = None,
        DomainEndpointOptions: DomainEndpointOptionsTypeDef = None,
    ) -> UpdateElasticsearchDomainConfigResponseTypeDef:
        """
        [Client.update_elasticsearch_domain_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.update_elasticsearch_domain_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upgrade_elasticsearch_domain(
        self, DomainName: str, TargetVersion: str, PerformCheckOnly: bool = None
    ) -> UpgradeElasticsearchDomainResponseTypeDef:
        """
        [Client.upgrade_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Client.upgrade_elasticsearch_domain)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_reserved_elasticsearch_instance_offerings"]
    ) -> paginator_scope.DescribeReservedElasticsearchInstanceOfferingsPaginator:
        """
        [Paginator.DescribeReservedElasticsearchInstanceOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_reserved_elasticsearch_instances"]
    ) -> paginator_scope.DescribeReservedElasticsearchInstancesPaginator:
        """
        [Paginator.DescribeReservedElasticsearchInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_upgrade_history"]
    ) -> paginator_scope.GetUpgradeHistoryPaginator:
        """
        [Paginator.GetUpgradeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_elasticsearch_instance_types"]
    ) -> paginator_scope.ListElasticsearchInstanceTypesPaginator:
        """
        [Paginator.ListElasticsearchInstanceTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_elasticsearch_versions"]
    ) -> paginator_scope.ListElasticsearchVersionsPaginator:
        """
        [Paginator.ListElasticsearchVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.40/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions)
        """


class Exceptions:
    BaseException: Boto3ClientError
    ClientError: Boto3ClientError
    DisabledOperationException: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidTypeException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError
