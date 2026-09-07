# Metodologia: Segmentacion Geoespacial de Proyectos Inmobiliarios

## 1. Recoleccion de Datos
- Fuentes de datos inmobiliarios: APIs publicas, datos catastrales, registros internos.
- Variables objetivo: ubicacion (lat/lon), tipologia, area construida, numero de unidades, precio, estrato, densidad, etc.

## 2. Preprocesamiento
- Limpieza de valores nulos y duplicados.
- Normalizacion y estandarizacion de variables numericas.
- Geocodificacion de direcciones cuando no se dispone de coordenadas.

## 3. Feature Engineering Geoespacial
- Calculo de variables derivadas: densidad de unidades, distancia a puntos de interes (POI), accesibilidad.
- Operaciones espaciales: spatial joins con capas de zonificacion, infraestructura, uso de suelo.

## 4. Analisis Exploratorio (EDA)
- Estadisticas descriptivas por tipologia de proyecto.
- Mapas de distribucion espacial.
- Correlaciones entre variables.

## 5. Modelado y Segmentacion
- Algoritmos evaluados: KMeans, DBSCAN, HDBSCAN.
- Seleccion del numero optimo de clusters: metodo del codo, silhouette analysis.
- Reduccion de dimensionalidad con PCA para visualizacion.

## 6. Validacion
- Metricas: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index.
- Interpretacion de clusters: caracterizacion por variables centroides.

## 7. Visualizacion y Reporte
- Mapas interactivos de clusters.
- Reportes estadisticos por segmento.
- Figuras exportadas para el paper.
