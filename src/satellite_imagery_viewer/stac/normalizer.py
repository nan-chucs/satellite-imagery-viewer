import pystac

from satellite_imagery_viewer.models.imagery import ImagerySearchResponse


def normalize_stac_item_to_imagery_search_response(
    stac_item: pystac.Item,
) -> ImagerySearchResponse:
    """
    Normalize a STAC item to an ImagerySearchResponse object.

    Args:
        stac_item: The STAC item to normalize.

    Returns:
        An ImagerySearchResponse object.
    """
    return ImagerySearchResponse(
        id=stac_item.id,
        datetime=stac_item.properties["datetime"],
        platform=stac_item.properties["platform"],
        collection=stac_item.collection_id,
        geometry=stac_item.geometry,
        proj_code=stac_item.properties.get("proj:code"),
        cloud_cover=stac_item.properties.get("eo:cloud_cover"),
    )