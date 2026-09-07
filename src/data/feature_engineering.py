"""Construcción y transformación de variables para modelado."""

import numpy as np
import pandas as pd
from loguru import logger


def compute_density(df: pd.DataFrame, units_col: str, area_col: str) -> pd.Series:
    """Calcula unidades por m² evitando divisiones por cero o áreas negativas."""
    missing = {units_col, area_col} - set(df.columns)
    if missing:
        raise KeyError(f"Columnas faltantes para densidad: {sorted(missing)}")

    area = pd.to_numeric(df[area_col], errors="coerce")
    units = pd.to_numeric(df[units_col], errors="coerce")
    invalid_area = area <= 0
    if invalid_area.any():
        logger.warning(
            f"Áreas no positivas detectadas: {int(invalid_area.sum())}; densidad=NaN."
        )
    safe_area = area.mask(invalid_area, np.nan)
    return units / safe_area


def encode_categorical(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Codifica variables categóricas con one-hot encoding."""
    missing = set(columns) - set(df.columns)
    if missing:
        raise KeyError(f"Columnas categóricas faltantes: {sorted(missing)}")
    logger.info(f"Codificando columnas: {columns}")
    return pd.get_dummies(df, columns=columns, drop_first=True)
