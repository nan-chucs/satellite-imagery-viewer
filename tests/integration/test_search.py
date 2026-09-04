import pystac
import pytest

from satellite_imagery_viewer.models.imagery import (
    ImagerySearchRequest,
)
from satellite_imagery_viewer.stac.search import search_imagery


AREA_OF_INTEREST = {
    "type": "Polygon",
    "coordinates": [
        [
            [-122.522, 37.7045],
            [-122.356, 37.7045],
            [-122.356, 37.815],
            [-122.522, 37.815],
            [-122.522, 37.7045],
        ]
    ],
}

TIME_RANGE = "2023-01-01/2023-12-31"


@pytest.mark.integration
@pytest.mark.parametrize(
    "collection",
    [
        "sentinel-2-l2a",
        "landsat-c2-l2",
        "sentinel-1-grd",
    ],
)
def test_search_imagery_returns_items(collection):
    search_params = ImagerySearchRequest(
        collection=collection,
        area_of_interest=AREA_OF_INTEREST,
        time_range=TIME_RANGE,
    )

    results = search_imagery(search_params)

    assert len(results) > 0
    assert all(
        isinstance(item, pystac.Item)
        for item in results
    )