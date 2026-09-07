"""Conversión y validación básica de coordenadas geográficas."""

import geopandas as gpd
import pandas as pd


def coords_to_geodataframe(
    df: pd.DataFrame,
    lat_col: str = "latitud",
    lon_col: str = "longitud",
    crs: str = "EPSG:4326",
) -> gpd.GeoDataFrame:
    """Convierte lat/lon válidas a ``GeoDataFrame`` sin mutar el original."""
    missing = {lat_col, lon_col} - set(df.columns)
    if missing:
        raise KeyError(f"Columnas de coordenadas faltantes: {sorted(missing)}")

    result = df.copy()
    lat = pd.to_numeric(result[lat_col], errors="coerce")
    lon = pd.to_numeric(result[lon_col], errors="coerce")
    invalid = lat.isna() | lon.isna() | ~lat.between(-90, 90) | ~lon.between(-180, 180)
    if invalid.any():
        raise ValueError(
            f"Se detectaron {int(invalid.sum())} coordenadas inválidas o no numéricas."
        )

    geometry = gpd.points_from_xy(lon, lat)
    return gpd.GeoDataFrame(result, geometry=geometry, crs=crs)
