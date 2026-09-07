import geopandas as gpd
import pandas as pd
import pytest
from shapely.geometry import Point, box

from src.geospatial.geocoding import coords_to_geodataframe
from src.geospatial.maps import add_cluster_layer, create_base_map
from src.geospatial.spatial_ops import create_buffer, spatial_join


def test_coords_to_geodataframe_validates_ranges():
    df = pd.DataFrame({"latitud": [-12.0464], "longitud": [-77.0428]})
    gdf = coords_to_geodataframe(df)
    assert str(gdf.crs) == "EPSG:4326"

    invalid = pd.DataFrame({"latitud": [-120.0], "longitud": [-77.0]})
    with pytest.raises(ValueError):
        coords_to_geodataframe(invalid)


def test_buffer_uses_metric_projection_for_lima():
    gdf = gpd.GeoDataFrame(
        {"id": [1]}, geometry=[Point(-77.0428, -12.0464)], crs="EPSG:4326"
    )
    buffered = create_buffer(gdf, distance=100)
    assert buffered.crs == gdf.crs

    area_m2 = buffered.to_crs("EPSG:32718").geometry.area.iloc[0]
    assert 30_000 < area_m2 < 33_000


def test_spatial_join_aligns_crs():
    left = gpd.GeoDataFrame(
        {"id": [1]}, geometry=[Point(-77.0428, -12.0464)], crs="EPSG:4326"
    )
    right = gpd.GeoDataFrame(
        {"zone": ["test"]},
        geometry=[box(-77.1, -12.1, -77.0, -12.0)],
        crs="EPSG:4326",
    ).to_crs("EPSG:32718")
    joined = spatial_join(left, right)
    assert joined.loc[0, "zone"] == "test"


def test_cluster_map_accepts_projected_points():
    gdf = gpd.GeoDataFrame(
        {"cluster": [0, -1]},
        geometry=[Point(-77.04, -12.04), Point(-77.03, -12.05)],
        crs="EPSG:4326",
    ).to_crs("EPSG:32718")
    fmap = add_cluster_layer(create_base_map(), gdf)
    assert len(fmap._children) >= 3
