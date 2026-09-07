"""
clustering.py
-------------
Algoritmos de clustering y segmentacion para clasificar
tipologias de proyectos inmobiliarios.
"""
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from loguru import logger

try:
    import hdbscan
    HDBSCAN_AVAILABLE = True
except ImportError:
    HDBSCAN_AVAILABLE = False


def run_kmeans(X: np.ndarray, n_clusters: int = 5, random_state: int = 42) -> np.ndarray:
    """Aplica KMeans y retorna etiquetas de cluster."""
    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init="auto")
    labels = model.fit_predict(X)
    logger.info(f"KMeans: {n_clusters} clusters | Inercia: {model.inertia_:.2f}")
    return labels, model


def run_dbscan(X: np.ndarray, eps: float = 0.5, min_samples: int = 5) -> np.ndarray:
    """Aplica DBSCAN y retorna etiquetas de cluster (-1 = ruido)."""
    model = DBSCAN(eps=eps, min_samples=min_samples)
    labels = model.fit_predict(X)
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    logger.info(f"DBSCAN: {n_clusters} clusters | Puntos de ruido: {(labels == -1).sum()}")
    return labels, model


def run_hdbscan(X: np.ndarray, min_cluster_size: int = 10) -> np.ndarray:
    """Aplica HDBSCAN (robusto a ruido) y retorna etiquetas."""
    if not HDBSCAN_AVAILABLE:
        raise ImportError("Instala hdbscan: pip install hdbscan")
    model = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size)
    labels = model.fit_predict(X)
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    logger.info(f"HDBSCAN: {n_clusters} clusters")
    return labels, model
