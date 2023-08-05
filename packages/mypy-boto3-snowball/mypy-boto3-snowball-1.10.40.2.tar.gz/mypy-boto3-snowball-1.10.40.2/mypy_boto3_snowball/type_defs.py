"Main interface for snowball service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)

CreateAddressResultTypeDef = TypedDict(
    "CreateAddressResultTypeDef", {"AddressId": str}, total=False
)

CreateClusterResultTypeDef = TypedDict(
    "CreateClusterResultTypeDef", {"ClusterId": str}, total=False
)

CreateJobResultTypeDef = TypedDict("CreateJobResultTypeDef", {"JobId": str}, total=False)

DescribeAddressResultTypeDef = TypedDict(
    "DescribeAddressResultTypeDef", {"Address": AddressTypeDef}, total=False
)

DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef",
    {"Addresses": List[AddressTypeDef], "NextToken": str},
    total=False,
)

_RequiredEc2AmiResourceTypeDef = TypedDict("_RequiredEc2AmiResourceTypeDef", {"AmiId": str})
_OptionalEc2AmiResourceTypeDef = TypedDict(
    "_OptionalEc2AmiResourceTypeDef", {"SnowballAmiId": str}, total=False
)


class Ec2AmiResourceTypeDef(_RequiredEc2AmiResourceTypeDef, _OptionalEc2AmiResourceTypeDef):
    pass


EventTriggerDefinitionTypeDef = TypedDict(
    "EventTriggerDefinitionTypeDef", {"EventResourceARN": str}, total=False
)

LambdaResourceTypeDef = TypedDict(
    "LambdaResourceTypeDef",
    {"LambdaArn": str, "EventTriggers": List[EventTriggerDefinitionTypeDef]},
    total=False,
)

KeyRangeTypeDef = TypedDict("KeyRangeTypeDef", {"BeginMarker": str, "EndMarker": str}, total=False)

S3ResourceTypeDef = TypedDict(
    "S3ResourceTypeDef", {"BucketArn": str, "KeyRange": KeyRangeTypeDef}, total=False
)

JobResourceTypeDef = TypedDict(
    "JobResourceTypeDef",
    {
        "S3Resources": List[S3ResourceTypeDef],
        "LambdaResources": List[LambdaResourceTypeDef],
        "Ec2AmiResources": List[Ec2AmiResourceTypeDef],
    },
    total=False,
)

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)

ClusterMetadataTypeDef = TypedDict(
    "ClusterMetadataTypeDef",
    {
        "ClusterId": str,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "ClusterState": Literal["AwaitingQuorum", "Pending", "InUse", "Complete", "Cancelled"],
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Resources": JobResourceTypeDef,
        "AddressId": str,
        "ShippingOption": Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"],
        "Notification": NotificationTypeDef,
        "ForwardingAddressId": str,
    },
    total=False,
)

DescribeClusterResultTypeDef = TypedDict(
    "DescribeClusterResultTypeDef", {"ClusterMetadata": ClusterMetadataTypeDef}, total=False
)

DataTransferTypeDef = TypedDict(
    "DataTransferTypeDef",
    {"BytesTransferred": int, "ObjectsTransferred": int, "TotalBytes": int, "TotalObjects": int},
    total=False,
)

JobLogsTypeDef = TypedDict(
    "JobLogsTypeDef",
    {"JobCompletionReportURI": str, "JobSuccessLogURI": str, "JobFailureLogURI": str},
    total=False,
)

ShipmentTypeDef = TypedDict("ShipmentTypeDef", {"Status": str, "TrackingNumber": str}, total=False)

ShippingDetailsTypeDef = TypedDict(
    "ShippingDetailsTypeDef",
    {
        "ShippingOption": Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"],
        "InboundShipment": ShipmentTypeDef,
        "OutboundShipment": ShipmentTypeDef,
    },
    total=False,
)

JobMetadataTypeDef = TypedDict(
    "JobMetadataTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Resources": JobResourceTypeDef,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "AddressId": str,
        "ShippingDetails": ShippingDetailsTypeDef,
        "SnowballCapacityPreference": Literal["T50", "T80", "T100", "T42", "NoPreference"],
        "Notification": NotificationTypeDef,
        "DataTransferProgress": DataTransferTypeDef,
        "JobLogInfo": JobLogsTypeDef,
        "ClusterId": str,
        "ForwardingAddressId": str,
    },
    total=False,
)

DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef",
    {"JobMetadata": JobMetadataTypeDef, "SubJobMetadata": List[JobMetadataTypeDef]},
    total=False,
)

GetJobManifestResultTypeDef = TypedDict(
    "GetJobManifestResultTypeDef", {"ManifestURI": str}, total=False
)

GetJobUnlockCodeResultTypeDef = TypedDict(
    "GetJobUnlockCodeResultTypeDef", {"UnlockCode": str}, total=False
)

GetSnowballUsageResultTypeDef = TypedDict(
    "GetSnowballUsageResultTypeDef", {"SnowballLimit": int, "SnowballsInUse": int}, total=False
)

GetSoftwareUpdatesResultTypeDef = TypedDict(
    "GetSoftwareUpdatesResultTypeDef", {"UpdatesURI": str}, total=False
)

JobListEntryTypeDef = TypedDict(
    "JobListEntryTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "IsMaster": bool,
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

ListClusterJobsResultTypeDef = TypedDict(
    "ListClusterJobsResultTypeDef",
    {"JobListEntries": List[JobListEntryTypeDef], "NextToken": str},
    total=False,
)

ClusterListEntryTypeDef = TypedDict(
    "ClusterListEntryTypeDef",
    {
        "ClusterId": str,
        "ClusterState": Literal["AwaitingQuorum", "Pending", "InUse", "Complete", "Cancelled"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

ListClustersResultTypeDef = TypedDict(
    "ListClustersResultTypeDef",
    {"ClusterListEntries": List[ClusterListEntryTypeDef], "NextToken": str},
    total=False,
)

CompatibleImageTypeDef = TypedDict(
    "CompatibleImageTypeDef", {"AmiId": str, "Name": str}, total=False
)

ListCompatibleImagesResultTypeDef = TypedDict(
    "ListCompatibleImagesResultTypeDef",
    {"CompatibleImages": List[CompatibleImageTypeDef], "NextToken": str},
    total=False,
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {"JobListEntries": List[JobListEntryTypeDef], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
