"""
spatial_ops.py
--------------
Operaciones espaciales sobre datos inmobiliarios:
spatial joins, buffers, intersection, etc.
"""
import geopandas as gpd
from loguru import logger


def load_geodataframe(filepath: str, crs: str = "EPSG:4326") -> gpd.GeoDataFrame:
    """Carga un archivo geoespacial (shapefile, GeoJSON, GeoPackage)."""
    gdf = gpd.read_file(filepath)
    gdf = gdf.to_crs(crs)
    logger.info(f"GeoDataFrame cargado: {len(gdf)} registros | CRS: {gdf.crs}")
    return gdf


def spatial_join(gdf_left: gpd.GeoDataFrame, gdf_right: gpd.GeoDataFrame,
                 how: str = "left", predicate: str = "intersects") -> gpd.GeoDataFrame:
    """Realiza un spatial join entre dos GeoDataFrames."""
    return gpd.sjoin(gdf_left, gdf_right, how=how, predicate=predicate)


def create_buffer(gdf: gpd.GeoDataFrame, distance: float, crs_proj: str = "EPSG:32617") -> gpd.GeoDataFrame:
    """Crea un buffer alrededor de las geometrias (en metros)."""
    gdf_proj = gdf.to_crs(crs_proj)
    gdf_proj["geometry"] = gdf_proj.buffer(distance)
    return gdf_proj.to_crs(gdf.crs)
