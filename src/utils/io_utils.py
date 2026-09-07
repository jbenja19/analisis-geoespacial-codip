"""Utilidades de escritura de artefactos del proyecto."""

import pickle
from pathlib import Path

import geopandas as gpd
import pandas as pd
from loguru import logger


def save_dataframe(df: pd.DataFrame, filepath: str | Path, fmt: str = "csv") -> None:
    """Guarda un DataFrame como CSV o Parquet."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    fmt = fmt.lower().strip()
    if fmt == "csv":
        df.to_csv(path, index=False)
    elif fmt == "parquet":
        df.to_parquet(path, index=False)
    else:
        raise ValueError(f"Formato no soportado: {fmt}. Usa csv o parquet.")
    logger.info(f"DataFrame guardado en: {path}")


def save_model(model: object, filepath: str | Path) -> None:
    """Serializa un modelo local con pickle."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as file:
        pickle.dump(model, file)
    logger.info(f"Modelo guardado en: {path}")


def save_geojson(gdf: gpd.GeoDataFrame, filepath: str | Path) -> None:
    """Guarda un GeoDataFrame como GeoJSON."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    gdf.to_file(path, driver="GeoJSON")
    logger.info(f"GeoJSON guardado en: {path}")
