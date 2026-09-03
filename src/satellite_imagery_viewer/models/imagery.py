from pydantic import BaseModel


Position = tuple[float, float]
LinearRing = list[Position]
PolygonCoordinates = list[LinearRing]


class PolygonGeometry(BaseModel):
    type: str
    coordinates: PolygonCoordinates


class ImagerySearchRequest(BaseModel):
    collection: str
    area_of_interest: PolygonGeometry
    time_range: str
    cloud_cover: float | None = None


class ImagerySearchResponse(BaseModel):
    id: str
    datetime: str
    platform: str
    collection: str
    geometry: PolygonGeometry
    proj_code: str | None = None
    cloud_cover: float | None = None