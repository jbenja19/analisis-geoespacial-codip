"""
cleaning.py
-----------
Funciones de limpieza y validacion de datos inmobiliarios.
"""
import pandas as pd
from loguru import logger


def remove_duplicates(df: pd.DataFrame, subset: list = None) -> pd.DataFrame:
    """Elimina filas duplicadas."""
    before = len(df)
    df = df.drop_duplicates(subset=subset)
    logger.info(f"Duplicados eliminados: {before - len(df)}")
    return df


def handle_missing(df: pd.DataFrame, strategy: str = "drop") -> pd.DataFrame:
    """Maneja valores nulos segun estrategia: drop, mean, median, mode."""
    if strategy == "drop":
        return df.dropna()
    elif strategy == "mean":
        return df.fillna(df.mean(numeric_only=True))
    elif strategy == "median":
        return df.fillna(df.median(numeric_only=True))
    else:
        raise ValueError(f"Estrategia no reconocida: {strategy}")
