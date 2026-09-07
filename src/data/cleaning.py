"""Funciones de limpieza y validación de datos inmobiliarios."""

import pandas as pd
from loguru import logger


def remove_duplicates(
    df: pd.DataFrame, subset: list[str] | None = None
) -> pd.DataFrame:
    """Elimina filas duplicadas sin mutar el DataFrame de entrada."""
    before = len(df)
    result = df.drop_duplicates(subset=subset).copy()
    logger.info(f"Duplicados eliminados: {before - len(result)}")
    return result


def handle_missing(df: pd.DataFrame, strategy: str = "drop") -> pd.DataFrame:
    """Maneja nulos con ``drop``, ``mean``, ``median`` o ``mode``.

    ``mean`` y ``median`` se aplican únicamente a columnas numéricas. ``mode``
    rellena cada columna con su moda cuando existe al menos un valor observado.
    """
    strategy = strategy.lower().strip()
    result = df.copy()

    if strategy == "drop":
        return result.dropna()

    if strategy in {"mean", "median"}:
        numeric_cols = result.select_dtypes(include="number").columns
        if strategy == "mean":
            fill_values = result[numeric_cols].mean()
        else:
            fill_values = result[numeric_cols].median()
        result[numeric_cols] = result[numeric_cols].fillna(fill_values)
        return result

    if strategy == "mode":
        for column in result.columns:
            mode = result[column].mode(dropna=True)
            if not mode.empty:
                result[column] = result[column].fillna(mode.iloc[0])
        return result

    raise ValueError(
        f"Estrategia no reconocida: {strategy}. Usa drop, mean, median o mode."
    )
