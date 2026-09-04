from satellite_imagery_viewer.stac.search import search_imagery
from satellite_imagery_viewer.stac.normalizer import (
    normalize_stac_item_to_imagery_search_response,
)
from satellite_imagery_viewer.models.imagery import (
    ImagerySearchRequest, 
    ImagerySearchResponse,
)


def discover_imagery(
search_params: ImagerySearchRequest
) -> list[ImagerySearchResponse]:
    items = search_imagery(search_params)
    return [normalize_stac_item_to_imagery_search_response(item) for item in items]