"""
evaluation.py
-------------
Metricas de evaluacion para los resultados de clustering:
Silhouette Score, Davies-Bouldin, Calinski-Harabasz.
"""
import numpy as np
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from loguru import logger


def evaluate_clustering(X: np.ndarray, labels: np.ndarray) -> dict:
    """
    Calcula metricas de evaluacion de clustering.
    Solo valido si hay mas de 1 cluster y menos clusters que muestras.
    """
    unique_labels = set(labels)
    valid_labels = unique_labels - {-1}

    if len(valid_labels) < 2:
        logger.warning("Se necesitan al menos 2 clusters para evaluar.")
        return {}

    mask = labels != -1
    X_valid, labels_valid = X[mask], labels[mask]

    metrics = {
        "silhouette": silhouette_score(X_valid, labels_valid),
        "davies_bouldin": davies_bouldin_score(X_valid, labels_valid),
        "calinski_harabasz": calinski_harabasz_score(X_valid, labels_valid),
        "n_clusters": len(valid_labels),
        "n_noise": (labels == -1).sum(),
    }
    for k, v in metrics.items():
        logger.info(f"  {k}: {v}")
    return metrics
