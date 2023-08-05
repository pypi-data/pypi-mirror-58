"Main interface for groundstation service"
from mypy_boto3_groundstation.client import GroundStationClient as Client, GroundStationClient
from mypy_boto3_groundstation.paginator import (
    ListConfigsPaginator,
    ListContactsPaginator,
    ListDataflowEndpointGroupsPaginator,
    ListGroundStationsPaginator,
    ListMissionProfilesPaginator,
    ListSatellitesPaginator,
)


__all__ = (
    "Client",
    "GroundStationClient",
    "ListConfigsPaginator",
    "ListContactsPaginator",
    "ListDataflowEndpointGroupsPaginator",
    "ListGroundStationsPaginator",
    "ListMissionProfilesPaginator",
    "ListSatellitesPaginator",
)
