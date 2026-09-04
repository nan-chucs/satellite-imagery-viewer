import pystac
import pystac_client
import planetary_computer

from satellite_imagery_viewer.models.imagery import ImagerySearchRequest


def search_imagery(
search_params: ImagerySearchRequest
) -> list[pystac.Item]:
    search_kwargs = {
        "collections": [search_params.collection],
        "intersects": search_params.area_of_interest.model_dump(mode="json"),
        "datetime": search_params.time_range,
    }

    if search_params.cloud_cover is not None:
        search_kwargs["query"] = {
            "eo:cloud_cover": {
                "lte": search_params.cloud_cover
            }
        }
    print(type(search_kwargs["intersects"]))
    print(search_kwargs["intersects"])

    catalog = pystac_client.Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
        modifier=planetary_computer.sign_inplace,
    )

    search = catalog.search(**search_kwargs)
    items = list(search.item_collection())

    return items