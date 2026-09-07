"""Tests unitarios para modulos de modelado."""
import numpy as np
import pytest
from src.models.clustering import run_kmeans
from src.models.evaluation import evaluate_clustering
from src.models.preprocessing import scale_features
import pandas as pd


def test_kmeans_basic():
    X = np.random.rand(50, 3)
    labels, model = run_kmeans(X, n_clusters=3)
    assert len(labels) == 50
    assert len(set(labels)) == 3


def test_evaluate_clustering():
    X = np.random.rand(30, 2)
    labels = np.array([0]*10 + [1]*10 + [2]*10)
    metrics = evaluate_clustering(X, labels)
    assert "silhouette" in metrics


def test_scale_features():
    df = pd.DataFrame({"a": [1.0, 2.0, 3.0], "b": [10.0, 20.0, 30.0]})
    X_scaled, scaler = scale_features(df, method="standard")
    assert X_scaled.shape == (3, 2)
