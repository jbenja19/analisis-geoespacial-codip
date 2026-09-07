"""Operaciones espaciales seguras para datos inmobiliarios."""

from pathlib import Path

import geopandas as gpd
from loguru import logger
from pyproj import CRS


def _require_crs(gdf: gpd.GeoDataFrame, name: str) -> None:
    if gdf.crs is None:
        raise ValueError(
            f"{name} no tiene CRS definido; no se puede reproyectar con seguridad."
        )


def load_geodataframe(
    filepath: str | Path, target_crs: str | None = "EPSG:4326"
) -> gpd.GeoDataFrame:
    """Carga datos geoespaciales y reproyecta solo si el CRS fuente es conocido."""
    gdf = gpd.read_file(filepath)
    _require_crs(gdf, "El archivo geoespacial")
    if (
        target_crs is not None
        and CRS.from_user_input(gdf.crs) != CRS.from_user_input(target_crs)
    ):
        gdf = gdf.to_crs(target_crs)
    logger.info(f"GeoDataFrame cargado: {len(gdf)} registros | CRS: {gdf.crs}")
    return gdf


def spatial_join(
    gdf_left: gpd.GeoDataFrame,
    gdf_right: gpd.GeoDataFrame,
    how: str = "left",
    predicate: str = "intersects",
) -> gpd.GeoDataFrame:
    """Realiza un spatial join alineando el CRS derecho con el izquierdo."""
    _require_crs(gdf_left, "gdf_left")
    _require_crs(gdf_right, "gdf_right")

    right = gdf_right
    if CRS.from_user_input(gdf_left.crs) != CRS.from_user_input(gdf_right.crs):
        right = gdf_right.to_crs(gdf_left.crs)
    return gpd.sjoin(gdf_left, right, how=how, predicate=predicate)


def create_buffer(
    gdf: gpd.GeoDataFrame,
    distance: float,
    crs_proj: str | None = None,
) -> gpd.GeoDataFrame:
    """Crea buffers en metros usando un CRS proyectado apropiado.

    Si ``crs_proj`` no se proporciona, GeoPandas estima la zona UTM a partir de
    la extensión del dataset. Para Lima, WGS 84 / UTM 18S corresponde a
    EPSG:32718. El resultado vuelve al CRS original.
    """
    if distance < 0:
        raise ValueError("distance debe ser mayor o igual a 0 metros.")
    _require_crs(gdf, "gdf")

    original_crs = gdf.crs
    projected_crs = (
        CRS.from_user_input(crs_proj)
        if crs_proj is not None
        else gdf.estimate_utm_crs()
    )
    if projected_crs is None:
        raise ValueError("No se pudo estimar un CRS UTM para el dataset.")
    if not projected_crs.is_projected:
        raise ValueError("crs_proj debe ser un CRS proyectado, no geográfico.")

    axis_info = projected_crs.axis_info
    if axis_info and axis_info[0].unit_name.lower() not in {"metre", "meter"}:
        raise ValueError("crs_proj debe usar metros para que distance esté en metros.")

    buffered = gdf.to_crs(projected_crs).copy()
    buffered["geometry"] = buffered.geometry.buffer(distance)
    return buffered.to_crs(original_crs)
