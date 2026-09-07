import numpy as np
import pytest

from src.models.clustering import run_kmeans
from src.models.evaluation import evaluate_clustering


def test_kmeans_basic_deterministic():
    X = np.vstack(
        [
            np.zeros((10, 2)),
            np.ones((10, 2)) * 10,
            np.ones((10, 2)) * 20,
        ]
    )
    labels, _ = run_kmeans(X, n_clusters=3)
    assert len(labels) == 30
    assert len(set(labels)) == 3


def test_kmeans_rejects_non_finite_input():
    with pytest.raises(ValueError):
        run_kmeans(np.array([[1.0, np.nan], [2.0, 3.0]]), n_clusters=2)


def test_evaluate_clustering():
    X = np.vstack(
        [
            np.zeros((10, 2)),
            np.ones((10, 2)) * 10,
            np.ones((10, 2)) * 20,
        ]
    )
    labels = np.array([0] * 10 + [1] * 10 + [2] * 10)
    metrics = evaluate_clustering(X, labels)
    assert "silhouette" in metrics
    assert metrics["n_clusters"] == 3


def test_evaluate_clustering_rejects_length_mismatch():
    with pytest.raises(ValueError):
        evaluate_clustering(np.zeros((3, 2)), np.array([0, 1]))
