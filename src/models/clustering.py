"""Algoritmos de clustering para segmentación de proyectos inmobiliarios."""

import numpy as np
from loguru import logger
from sklearn.cluster import DBSCAN, KMeans

try:
    import hdbscan

    HDBSCAN_AVAILABLE = True
except ImportError:
    hdbscan = None
    HDBSCAN_AVAILABLE = False


def _validate_matrix(X: np.ndarray) -> np.ndarray:
    matrix = np.asarray(X, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise ValueError("X debe ser una matriz 2D no vacía.")
    if not np.isfinite(matrix).all():
        raise ValueError(
            "X contiene NaN o infinitos; limpia los datos antes de modelar."
        )
    return matrix


def run_kmeans(
    X: np.ndarray, n_clusters: int = 5, random_state: int = 42
) -> tuple[np.ndarray, KMeans]:
    """Aplica KMeans y retorna ``(labels, model)``."""
    matrix = _validate_matrix(X)
    if not 1 <= n_clusters <= len(matrix):
        raise ValueError("n_clusters debe estar entre 1 y el número de observaciones.")
    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init="auto")
    labels = model.fit_predict(matrix)
    logger.info(f"KMeans: {n_clusters} clusters | Inercia: {model.inertia_:.2f}")
    return labels, model


def run_dbscan(
    X: np.ndarray, eps: float = 0.5, min_samples: int = 5
) -> tuple[np.ndarray, DBSCAN]:
    """Aplica DBSCAN y retorna ``(labels, model)``; -1 representa ruido."""
    matrix = _validate_matrix(X)
    model = DBSCAN(eps=eps, min_samples=min_samples)
    labels = model.fit_predict(matrix)
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    logger.info(
        f"DBSCAN: {n_clusters} clusters | Puntos de ruido: {(labels == -1).sum()}"
    )
    return labels, model


def run_hdbscan(
    X: np.ndarray, min_cluster_size: int = 10
) -> tuple[np.ndarray, object]:
    """Aplica HDBSCAN y retorna ``(labels, model)``."""
    if not HDBSCAN_AVAILABLE:
        raise ImportError("Instala hdbscan: pip install hdbscan")
    matrix = _validate_matrix(X)
    model = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size)
    labels = model.fit_predict(matrix)
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    logger.info(f"HDBSCAN: {n_clusters} clusters")
    return labels, model
