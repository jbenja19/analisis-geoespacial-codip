"""Visualizaciones cartográficas interactivas para proyectos inmobiliarios."""

import folium
import geopandas as gpd

_CLUSTER_COLORS = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
]


def create_base_map(center: list[float] | None = None, zoom: int = 12) -> folium.Map:
    """Crea un mapa base de Folium; por defecto centra en Lima Metropolitana."""
    if center is None:
        center = [-12.0464, -77.0428]
    return folium.Map(location=center, zoom_start=zoom, tiles="CartoDB positron")


def add_cluster_layer(
    fmap: folium.Map,
    gdf: gpd.GeoDataFrame,
    cluster_col: str = "cluster",
) -> folium.Map:
    """Agrega puntos de clusters de forma determinista y en WGS84."""
    if cluster_col not in gdf.columns:
        raise KeyError(f"No existe la columna de cluster: {cluster_col}")
    if gdf.crs is None:
        raise ValueError("El GeoDataFrame debe tener CRS definido.")

    display = gdf.to_crs("EPSG:4326")
    clusters = sorted(display[cluster_col].dropna().unique(), key=str)
    colors = {
        cluster: _CLUSTER_COLORS[index % len(_CLUSTER_COLORS)]
        for index, cluster in enumerate(clusters)
    }

    for _, row in display.iterrows():
        geometry = row.geometry
        if geometry is None or geometry.is_empty:
            continue
        point = (
            geometry
            if geometry.geom_type == "Point"
            else geometry.representative_point()
        )
        cluster = row[cluster_col]
        color = "#808080" if cluster == -1 else colors.get(cluster, "#808080")
        folium.CircleMarker(
            location=[point.y, point.x],
            radius=6,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8,
            popup=f"Cluster: {cluster}",
        ).add_to(fmap)
    return fmap
