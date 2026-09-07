"""
io_utils.py
-----------
Utilidades de lectura y escritura de archivos para el proyecto CODIP.
"""
import json
import pickle
import pandas as pd
import geopandas as gpd
from pathlib import Path
from loguru import logger


def save_dataframe(df: pd.DataFrame, filepath: str | Path, fmt: str = "csv") -> None:
    """Guarda un DataFrame en el formato especificado."""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    if fmt == "csv":
        df.to_csv(filepath, index=False)
    elif fmt == "parquet":
        df.to_parquet(filepath, index=False)
    logger.info(f"DataFrame guardado en: {filepath}")


def save_model(model, filepath: str | Path) -> None:
    """Serializa y guarda un modelo con pickle."""
    with open(filepath, "wb") as f:
        pickle.dump(model, f)
    logger.info(f"Modelo guardado en: {filepath}")


def save_geojson(gdf: gpd.GeoDataFrame, filepath: str | Path) -> None:
    """Guarda un GeoDataFrame como GeoJSON."""
    gdf.to_file(filepath, driver="GeoJSON")
    logger.info(f"GeoJSON guardado en: {filepath}")
