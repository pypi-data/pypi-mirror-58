"Main interface for snowball service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_snowball.client as client_scope

# pylint: disable=import-self
import mypy_boto3_snowball.paginator as paginator_scope
from mypy_boto3_snowball.type_defs import (
    AddressTypeDef,
    CreateAddressResultTypeDef,
    CreateClusterResultTypeDef,
    CreateJobResultTypeDef,
    DescribeAddressResultTypeDef,
    DescribeAddressesResultTypeDef,
    DescribeClusterResultTypeDef,
    DescribeJobResultTypeDef,
    GetJobManifestResultTypeDef,
    GetJobUnlockCodeResultTypeDef,
    GetSnowballUsageResultTypeDef,
    GetSoftwareUpdatesResultTypeDef,
    JobResourceTypeDef,
    ListClusterJobsResultTypeDef,
    ListClustersResultTypeDef,
    ListCompatibleImagesResultTypeDef,
    ListJobsResultTypeDef,
    NotificationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SnowballClient",)


class SnowballClient(BaseClient):
    """
    [Snowball.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_cluster(self, ClusterId: str) -> Dict[str, Any]:
        """
        [Client.cancel_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.cancel_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_job(self, JobId: str) -> Dict[str, Any]:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.cancel_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_address(self, Address: AddressTypeDef) -> CreateAddressResultTypeDef:
        """
        [Client.create_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.create_address)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cluster(
        self,
        JobType: Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        Resources: JobResourceTypeDef,
        AddressId: str,
        RoleARN: str,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"],
        Description: str = None,
        KmsKeyARN: str = None,
        SnowballType: Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"] = None,
        Notification: NotificationTypeDef = None,
        ForwardingAddressId: str = None,
    ) -> CreateClusterResultTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.create_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_job(
        self,
        JobType: Literal["IMPORT", "EXPORT", "LOCAL_USE"] = None,
        Resources: JobResourceTypeDef = None,
        Description: str = None,
        AddressId: str = None,
        KmsKeyARN: str = None,
        RoleARN: str = None,
        SnowballCapacityPreference: Literal["T50", "T80", "T100", "T42", "NoPreference"] = None,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"] = None,
        Notification: NotificationTypeDef = None,
        ClusterId: str = None,
        SnowballType: Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"] = None,
        ForwardingAddressId: str = None,
    ) -> CreateJobResultTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.create_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_address(self, AddressId: str) -> DescribeAddressResultTypeDef:
        """
        [Client.describe_address documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.describe_address)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_addresses(
        self, MaxResults: int = None, NextToken: str = None
    ) -> DescribeAddressesResultTypeDef:
        """
        [Client.describe_addresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.describe_addresses)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cluster(self, ClusterId: str) -> DescribeClusterResultTypeDef:
        """
        [Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.describe_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_job(self, JobId: str) -> DescribeJobResultTypeDef:
        """
        [Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.describe_job)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_manifest(self, JobId: str) -> GetJobManifestResultTypeDef:
        """
        [Client.get_job_manifest documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.get_job_manifest)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_job_unlock_code(self, JobId: str) -> GetJobUnlockCodeResultTypeDef:
        """
        [Client.get_job_unlock_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.get_job_unlock_code)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_snowball_usage(self) -> GetSnowballUsageResultTypeDef:
        """
        [Client.get_snowball_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.get_snowball_usage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_software_updates(self, JobId: str) -> GetSoftwareUpdatesResultTypeDef:
        """
        [Client.get_software_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.get_software_updates)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_cluster_jobs(
        self, ClusterId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListClusterJobsResultTypeDef:
        """
        [Client.list_cluster_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.list_cluster_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_clusters(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListClustersResultTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.list_clusters)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_compatible_images(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListCompatibleImagesResultTypeDef:
        """
        [Client.list_compatible_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.list_compatible_images)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(self, MaxResults: int = None, NextToken: str = None) -> ListJobsResultTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.list_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_cluster(
        self,
        ClusterId: str,
        RoleARN: str = None,
        Description: str = None,
        Resources: JobResourceTypeDef = None,
        AddressId: str = None,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"] = None,
        Notification: NotificationTypeDef = None,
        ForwardingAddressId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.update_cluster)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_job(
        self,
        JobId: str,
        RoleARN: str = None,
        Notification: NotificationTypeDef = None,
        Resources: JobResourceTypeDef = None,
        AddressId: str = None,
        ShippingOption: Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"] = None,
        Description: str = None,
        SnowballCapacityPreference: Literal["T50", "T80", "T100", "T42", "NoPreference"] = None,
        ForwardingAddressId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Client.update_job)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_addresses"]
    ) -> paginator_scope.DescribeAddressesPaginator:
        """
        [Paginator.DescribeAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_cluster_jobs"]
    ) -> paginator_scope.ListClusterJobsPaginator:
        """
        [Paginator.ListClusterJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_clusters"]
    ) -> paginator_scope.ListClustersPaginator:
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Paginator.ListClusters)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_compatible_images"]
    ) -> paginator_scope.ListCompatibleImagesPaginator:
        """
        [Paginator.ListCompatibleImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_jobs"]
    ) -> paginator_scope.ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/snowball.html#Snowball.Paginator.ListJobs)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ClusterLimitExceededException: Boto3ClientError
    Ec2RequestFailedException: Boto3ClientError
    InvalidAddressException: Boto3ClientError
    InvalidInputCombinationException: Boto3ClientError
    InvalidJobStateException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidResourceException: Boto3ClientError
    KMSRequestFailedException: Boto3ClientError
    UnsupportedAddressException: Boto3ClientError
