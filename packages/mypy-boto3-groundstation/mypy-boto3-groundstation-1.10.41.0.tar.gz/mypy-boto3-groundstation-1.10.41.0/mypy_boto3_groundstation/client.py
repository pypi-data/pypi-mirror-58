"Main interface for groundstation service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_groundstation.client as client_scope

# pylint: disable=import-self
import mypy_boto3_groundstation.paginator as paginator_scope
from mypy_boto3_groundstation.type_defs import (
    ConfigIdResponseTypeDef,
    ConfigTypeDataTypeDef,
    ContactIdResponseTypeDef,
    DataflowEndpointGroupIdResponseTypeDef,
    DescribeContactResponseTypeDef,
    EndpointDetailsTypeDef,
    GetConfigResponseTypeDef,
    GetDataflowEndpointGroupResponseTypeDef,
    GetMinuteUsageResponseTypeDef,
    GetMissionProfileResponseTypeDef,
    GetSatelliteResponseTypeDef,
    ListConfigsResponseTypeDef,
    ListContactsResponseTypeDef,
    ListDataflowEndpointGroupsResponseTypeDef,
    ListGroundStationsResponseTypeDef,
    ListMissionProfilesResponseTypeDef,
    ListSatellitesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MissionProfileIdResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GroundStationClient",)


class GroundStationClient(BaseClient):
    """
    [GroundStation.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_contact(self, contactId: str) -> ContactIdResponseTypeDef:
        """
        [Client.cancel_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.cancel_contact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_config(
        self, configData: ConfigTypeDataTypeDef, name: str, tags: Dict[str, str] = None
    ) -> ConfigIdResponseTypeDef:
        """
        [Client.create_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.create_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_dataflow_endpoint_group(
        self, endpointDetails: List[EndpointDetailsTypeDef], tags: Dict[str, str] = None
    ) -> DataflowEndpointGroupIdResponseTypeDef:
        """
        [Client.create_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.create_dataflow_endpoint_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_mission_profile(
        self,
        dataflowEdges: List[List[str]],
        minimumViableContactDurationSeconds: int,
        name: str,
        trackingConfigArn: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        tags: Dict[str, str] = None,
    ) -> MissionProfileIdResponseTypeDef:
        """
        [Client.create_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.create_mission_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_config(
        self,
        configId: str,
        configType: Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    ) -> ConfigIdResponseTypeDef:
        """
        [Client.delete_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.delete_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_dataflow_endpoint_group(
        self, dataflowEndpointGroupId: str
    ) -> DataflowEndpointGroupIdResponseTypeDef:
        """
        [Client.delete_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.delete_dataflow_endpoint_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_mission_profile(self, missionProfileId: str) -> MissionProfileIdResponseTypeDef:
        """
        [Client.delete_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.delete_mission_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_contact(self, contactId: str) -> DescribeContactResponseTypeDef:
        """
        [Client.describe_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.describe_contact)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_config(
        self,
        configId: str,
        configType: Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
    ) -> GetConfigResponseTypeDef:
        """
        [Client.get_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.get_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_dataflow_endpoint_group(
        self, dataflowEndpointGroupId: str
    ) -> GetDataflowEndpointGroupResponseTypeDef:
        """
        [Client.get_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.get_dataflow_endpoint_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_minute_usage(self, month: int, year: int) -> GetMinuteUsageResponseTypeDef:
        """
        [Client.get_minute_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.get_minute_usage)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_mission_profile(self, missionProfileId: str) -> GetMissionProfileResponseTypeDef:
        """
        [Client.get_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.get_mission_profile)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_satellite(self, satelliteId: str) -> GetSatelliteResponseTypeDef:
        """
        [Client.get_satellite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.get_satellite)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_configs(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListConfigsResponseTypeDef:
        """
        [Client.list_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.list_configs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_contacts(
        self,
        endTime: datetime,
        startTime: datetime,
        statusList: List[
            Literal[
                "AVAILABLE",
                "AWS_CANCELLED",
                "CANCELLED",
                "COMPLETED",
                "FAILED",
                "FAILED_TO_SCHEDULE",
                "PASS",
                "POSTPASS",
                "PREPASS",
                "SCHEDULED",
                "SCHEDULING",
            ]
        ],
        groundStation: str = None,
        maxResults: int = None,
        missionProfileArn: str = None,
        nextToken: str = None,
        satelliteArn: str = None,
    ) -> ListContactsResponseTypeDef:
        """
        [Client.list_contacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.list_contacts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dataflow_endpoint_groups(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListDataflowEndpointGroupsResponseTypeDef:
        """
        [Client.list_dataflow_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.list_dataflow_endpoint_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_ground_stations(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListGroundStationsResponseTypeDef:
        """
        [Client.list_ground_stations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.list_ground_stations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_mission_profiles(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListMissionProfilesResponseTypeDef:
        """
        [Client.list_mission_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.list_mission_profiles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_satellites(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListSatellitesResponseTypeDef:
        """
        [Client.list_satellites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.list_satellites)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reserve_contact(
        self,
        endTime: datetime,
        groundStation: str,
        missionProfileArn: str,
        satelliteArn: str,
        startTime: datetime,
        tags: Dict[str, str] = None,
    ) -> ContactIdResponseTypeDef:
        """
        [Client.reserve_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.reserve_contact)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str] = None) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_config(
        self,
        configData: ConfigTypeDataTypeDef,
        configId: str,
        configType: Literal[
            "antenna-downlink",
            "antenna-downlink-demod-decode",
            "antenna-uplink",
            "dataflow-endpoint",
            "tracking",
            "uplink-echo",
        ],
        name: str,
    ) -> ConfigIdResponseTypeDef:
        """
        [Client.update_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.update_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_mission_profile(
        self,
        missionProfileId: str,
        contactPostPassDurationSeconds: int = None,
        contactPrePassDurationSeconds: int = None,
        dataflowEdges: List[List[str]] = None,
        minimumViableContactDurationSeconds: int = None,
        name: str = None,
        trackingConfigArn: str = None,
    ) -> MissionProfileIdResponseTypeDef:
        """
        [Client.update_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Client.update_mission_profile)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_configs"]
    ) -> paginator_scope.ListConfigsPaginator:
        """
        [Paginator.ListConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_contacts"]
    ) -> paginator_scope.ListContactsPaginator:
        """
        [Paginator.ListContacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Paginator.ListContacts)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_dataflow_endpoint_groups"]
    ) -> paginator_scope.ListDataflowEndpointGroupsPaginator:
        """
        [Paginator.ListDataflowEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_ground_stations"]
    ) -> paginator_scope.ListGroundStationsPaginator:
        """
        [Paginator.ListGroundStations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_mission_profiles"]
    ) -> paginator_scope.ListMissionProfilesPaginator:
        """
        [Paginator.ListMissionProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_satellites"]
    ) -> paginator_scope.ListSatellitesPaginator:
        """
        [Paginator.ListSatellites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.41/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites)
        """


class Exceptions:
    ClientError: Boto3ClientError
    DependencyException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
