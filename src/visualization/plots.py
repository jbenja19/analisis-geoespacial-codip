"""
plots.py
--------
Graficos estadisticos para el analisis y presentacion
de resultados del clustering de proyectos inmobiliarios.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_cluster_distribution(labels: np.ndarray, title: str = "Distribucion de Clusters") -> None:
    """Grafica la distribucion de tamanio de cada cluster."""
    unique, counts = np.unique(labels, return_counts=True)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar([str(u) for u in unique], counts, color=sns.color_palette("tab10"))
    ax.set_xlabel("Cluster")
    ax.set_ylabel("Cantidad de Proyectos")
    ax.set_title(title)
    plt.tight_layout()
    return fig


def plot_elbow(inertias: list, k_range: range, title: str = "Metodo del Codo") -> None:
    """Grafica el metodo del codo para seleccion de K en KMeans."""
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(list(k_range), inertias, marker="o", linewidth=2)
    ax.set_xlabel("Numero de Clusters (K)")
    ax.set_ylabel("Inercia")
    ax.set_title(title)
    plt.tight_layout()
    return fig


def plot_feature_importance(feature_names: list, importances: np.ndarray) -> None:
    """Grafica la importancia de features en la segmentacion."""
    df = pd.DataFrame({"feature": feature_names, "importance": importances})
    df = df.sort_values("importance", ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=df, y="feature", x="importance", ax=ax, palette="viridis")
    ax.set_title("Importancia de Variables")
    plt.tight_layout()
    return fig
