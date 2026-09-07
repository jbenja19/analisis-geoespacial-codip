"""
geo_plots.py
------------
Visualizaciones geoespaciales de los clusters
de proyectos inmobiliarios.
"""
import geopandas as gpd
import matplotlib.cm as cm
import matplotlib.pyplot as plt


def plot_clusters_static(
    gdf: gpd.GeoDataFrame,
    cluster_col: str = "cluster",
    title: str = "Segmentacion Geoespacial de Proyectos",
) -> plt.Figure:
    """Genera un mapa estatico con los proyectos coloreados por cluster."""
    fig, ax = plt.subplots(figsize=(12, 8))
    n_clusters = gdf[cluster_col].nunique()
    cmap = cm.get_cmap("tab10", n_clusters)
    gdf.plot(
        column=cluster_col,
        ax=ax,
        cmap=cmap,
        legend=True,
        legend_kwds={"title": "Cluster", "loc": "lower right"},
    )
    ax.set_title(title, fontsize=14)
    ax.axis("off")
    plt.tight_layout()
    return fig
