import pystac

from satellite_imagery_viewer.models.imagery import ImagerySearchResponse


def normalize_stac_item_to_imagery_search_response(
    stac_item: pystac.Item,
) -> ImagerySearchResponse:
    return ImagerySearchResponse(
        id=stac_item.id,
        datetime=stac_item.properties["datetime"],
        platform=stac_item.properties["platform"],
        collection=stac_item.collection_id,
        geometry=stac_item.geometry,
    )