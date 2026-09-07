"""
feature_engineering.py
----------------------
Construccion y transformacion de variables para el modelado
de proyectos inmobiliarios.
"""
import pandas as pd
import numpy as np
from loguru import logger


def compute_density(df: pd.DataFrame, units_col: str, area_col: str) -> pd.Series:
    """Calcula densidad de unidades por area."""
    return df[units_col] / df[area_col]


def encode_categorical(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Codifica variables categoricas con one-hot encoding."""
    logger.info(f"Codificando columnas: {columns}")
    return pd.get_dummies(df, columns=columns, drop_first=True)
