"""
maps.py
-------
Generacion de visualizaciones cartograficas interactivas
y estaticas para el analisis geoespacial de proyectos.
"""
import folium
import geopandas as gpd
from loguru import logger


def create_base_map(center: list = None, zoom: int = 12) -> folium.Map:
    """Crea un mapa base de Folium."""
    if center is None:
        center = [0.0, 0.0]
    return folium.Map(location=center, zoom_start=zoom, tiles="CartoDB positron")


def add_cluster_layer(fmap: folium.Map, gdf: gpd.GeoDataFrame,
                      cluster_col: str = "cluster") -> folium.Map:
    """Agrega una capa de puntos coloreados por cluster al mapa."""
    import random
    clusters = gdf[cluster_col].unique()
    colors = {c: f"#{random.randint(0, 0xFFFFFF):06x}" for c in clusters}
    for _, row in gdf.iterrows():
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=6,
            color=colors.get(row[cluster_col], "#gray"),
            fill=True,
            popup=str(row[cluster_col])
        ).add_to(fmap)
    return fmap
