"""
preprocessing.py
----------------
Preprocesamiento de features para modelado:
escalado, PCA y reduccion de dimensionalidad.
"""

import numpy as np
import pandas as pd
from loguru import logger
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def scale_features(df: pd.DataFrame, method: str = "standard") -> tuple:
    """Escala features numericas. Retorna (array_escalado, scaler)."""
    if method == "standard":
        scaler = StandardScaler()
    elif method == "minmax":
        scaler = MinMaxScaler()
    else:
        raise ValueError(f"Metodo no reconocido: {method}")
    X_scaled = scaler.fit_transform(df.select_dtypes(include="number"))
    logger.info(f"Features escaladas con {method}. Shape: {X_scaled.shape}")
    return X_scaled, scaler


def apply_pca(X: np.ndarray, n_components: float = 0.95) -> tuple:
    """Aplica PCA. n_components puede ser int o float (varianza explicada)."""
    pca = PCA(n_components=n_components, random_state=42)
    X_pca = pca.fit_transform(X)
    explained = pca.explained_variance_ratio_.sum()
    logger.info(
        f"PCA: {X_pca.shape[1]} componentes | Varianza explicada: {explained:.3f}"
    )
    return X_pca, pca
