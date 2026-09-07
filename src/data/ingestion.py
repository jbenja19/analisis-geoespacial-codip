"""
ingestion.py
------------
Modulo para la carga e ingesta de datos de proyectos inmobiliarios
desde distintas fuentes (CSV, Excel, APIs, bases de datos, etc.).
"""

from pathlib import Path

import pandas as pd
from loguru import logger


def load_csv(filepath: str | Path, **kwargs) -> pd.DataFrame:
    """Carga un archivo CSV y retorna un DataFrame."""
    logger.info(f"Cargando archivo: {filepath}")
    return pd.read_csv(filepath, **kwargs)


def load_excel(filepath: str | Path, sheet_name: str = 0, **kwargs) -> pd.DataFrame:
    """Carga un archivo Excel y retorna un DataFrame."""
    logger.info(f"Cargando Excel: {filepath} | Hoja: {sheet_name}")
    return pd.read_excel(filepath, sheet_name=sheet_name, **kwargs)
