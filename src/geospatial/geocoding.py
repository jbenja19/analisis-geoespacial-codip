"""
geocoding.py
------------
Geocodificacion de direcciones y manejo de coordenadas
para proyectos inmobiliarios.
"""
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from loguru import logger


def coords_to_geodataframe(df: pd.DataFrame, lat_col: str = "lat",
                            lon_col: str = "lon", crs: str = "EPSG:4326") -> gpd.GeoDataFrame:
    """Convierte un DataFrame con coordenadas a GeoDataFrame."""
    geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
    return gpd.GeoDataFrame(df, geometry=geometry, crs=crs)
