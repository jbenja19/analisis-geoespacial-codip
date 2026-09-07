"""Métricas internas para resultados de clustering."""

import numpy as np
from loguru import logger
from sklearn.metrics import (
    calinski_harabasz_score,
    davies_bouldin_score,
    silhouette_score,
)


def evaluate_clustering(X: np.ndarray, labels: np.ndarray) -> dict[str, float | int]:
    """Evalúa clusters no-ruido cuando las métricas están matemáticamente definidas."""
    matrix = np.asarray(X)
    labels = np.asarray(labels)
    if matrix.ndim != 2:
        raise ValueError("X debe ser una matriz 2D.")
    if len(matrix) != len(labels):
        raise ValueError("X y labels deben tener el mismo número de observaciones.")

    mask = labels != -1
    X_valid = matrix[mask]
    labels_valid = labels[mask]
    valid_labels = np.unique(labels_valid)

    if len(valid_labels) < 2 or len(X_valid) <= len(valid_labels):
        logger.warning("No hay suficientes clusters/muestras válidas para evaluar.")
        return {}

    metrics: dict[str, float | int] = {
        "silhouette": float(silhouette_score(X_valid, labels_valid)),
        "davies_bouldin": float(davies_bouldin_score(X_valid, labels_valid)),
        "calinski_harabasz": float(calinski_harabasz_score(X_valid, labels_valid)),
        "n_clusters": int(len(valid_labels)),
        "n_noise": int((labels == -1).sum()),
        "noise_ratio": float((labels == -1).mean()),
    }
    for key, value in metrics.items():
        logger.info(f"  {key}: {value}")
    return metrics
