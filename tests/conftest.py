import pystac
import pytest


try:
    import truststore

    truststore.inject_into_ssl()
except ImportError:
    pass


@pytest.fixture
def make_stac_item():
    def _make_stac_item(
        item_id="test-item",
        platform="Sentinel-2A",
        collection="sentinel-2-l2a",
    ):
        return pystac.Item.from_dict(
            {
                "type": "Feature",
                "stac_version": "1.0.0",
                "id": item_id,
                "collection": collection,
                "geometry": {
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
                "bbox": [-122.5, 37.7, -122.3, 37.8],
                "properties": {
                    "datetime": "2023-01-01T00:00:00Z",
                    "platform": platform,
                },
                "links": [],
                "assets": {},
            }
        )

    return _make_stac_item