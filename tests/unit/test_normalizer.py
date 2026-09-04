from satellite_imagery_viewer.stac.normalizer import (
    normalize_stac_item_to_imagery_search_response,
)


def test_normalize_stac_item_to_imagery_search_response(
    make_stac_item,
):
    stac_item = make_stac_item()

    result = normalize_stac_item_to_imagery_search_response(
        stac_item
    )

    assert result.id == "test-item"
    assert result.datetime == "2023-01-01T00:00:00Z"
    assert result.platform == "Sentinel-2A"
    assert result.collection == "sentinel-2-l2a"
    assert result.geometry.type == "Polygon"