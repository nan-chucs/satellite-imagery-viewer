from satellite_imagery_viewer.models.imagery import (
    ImagerySearchRequest,
)
from satellite_imagery_viewer.services.discovery import (
    discover_imagery,
)


def test_discover_imagery_normalizes_all_search_results(
    make_stac_item,
    monkeypatch,
):
    items = [
        make_stac_item(
            item_id="item-1",
            platform="Sentinel-2A",
        ),
        make_stac_item(
            item_id="item-2",
            platform="Sentinel-2B",
        ),
    ]

    def fake_search_imagery(search_params):
        return items

    monkeypatch.setattr(
        "satellite_imagery_viewer.services.discovery.search_imagery",
        fake_search_imagery,
    )

    search_params = ImagerySearchRequest(
        collection="sentinel-2-l2a",
        area_of_interest={
            "type": "Polygon",
            "coordinates": [
                [
                    [-122.5, 37.7],
                    [-122.3, 37.7],
                    [-122.3, 37.8],
                    [-122.5, 37.8],
                    [-122.5, 37.7],
                ]
            ],
        },
        time_range="2023-01-01/2023-12-31",
    )

    results = discover_imagery(search_params)

    assert len(results) == 2
    assert results[0].id == "item-1"
    assert results[1].id == "item-2"