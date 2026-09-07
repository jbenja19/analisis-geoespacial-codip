# Metodología: Segmentación Geoespacial de Proyectos Inmobiliarios

> **Estado:** protocolo inicial de investigación. Los clusters obtenidos deben
> interpretarse como una segmentación empírica condicionada por datos, features,
> escalamiento, métrica y algoritmo; no como categorías naturales ni resultados
> causales.

## 1. Definición del problema y unidad de análisis

- Fijar la pregunta analítica antes de seleccionar algoritmos.
- Documentar el grano del dataset: proyecto, proyecto-fecha, unidad u otro.
- Definir población, cobertura geográfica y período de observación.
- Evitar mezclar cortes temporales incompatibles en una misma fotografía de mercado.

## 2. Perfilado y contrato de datos

Antes de limpiar o modelar:

- Inventariar fuentes, propietario, fecha de corte y reglas de acceso.
- Medir completitud, duplicados, cardinalidad, rangos y unidades.
- Documentar llaves y relaciones entre fuentes.
- Construir el mapeo fuente -> variable canónica en `docs/data_dictionary.md`.
- No asumir que campos con nombres parecidos tienen la misma semántica.

## 3. Control geoespacial

- Coordenadas de intercambio/visualización: WGS84 (`EPSG:4326`).
- Validar rangos de latitud/longitud y detectar coordenadas repetidas o imposibles.
- Para distancias, áreas y buffers usar un CRS proyectado en metros.
- Para Lima Metropolitana, UTM 18S es `EPSG:32718`; para otros ámbitos, estimar
  o seleccionar el CRS adecuado en vez de aplicar una zona UTM fija.
- Verificar CRS antes de cualquier spatial join y reproyectar de forma explícita.

## 4. Feature engineering

Bloques candidatos, sujetos a disponibilidad real:

- Características físicas del proyecto.
- Escala/densidad del proyecto.
- Precio y posicionamiento comercial con moneda/fecha comparables.
- Accesibilidad y distancias a infraestructura.
- Entorno urbano y densidad de POI por radios predefinidos.
- Variables territoriales obtenidas mediante spatial joins documentados.

Cada feature debe registrar definición, unidad, fuente, fecha y transformación.

## 5. Preprocesamiento para clustering

- Tratar faltantes con una regla justificada; no imputar automáticamente por conveniencia.
- Revisar outliers y errores de captura antes de winsorizar o eliminar observaciones.
- Escalar variables cuando la métrica del algoritmo lo requiera.
- Evitar que grupos con muchas variables correlacionadas dominen la distancia.
- Usar PCA como herramienta de diagnóstico/reducción cuando sea útil, no como paso obligatorio.

## 6. Modelos candidatos

- **KMeans:** baseline para clusters aproximadamente compactos bajo distancia euclídea.
- **DBSCAN:** útil para densidad/ruido, sensible a `eps`, `min_samples` y escala.
- **HDBSCAN:** alternativa para densidades heterogéneas y observaciones de ruido.

Si las coordenadas entran directamente al modelo, su representación y métrica
 deben justificarse. No usar grados de latitud/longitud como si fueran metros.

## 7. Validación

No seleccionar el modelo solo por una métrica interna.

### 7.1 Métricas internas

- Silhouette Score.
- Davies-Bouldin Index.
- Calinski-Harabasz Index.
- Proporción de ruido para DBSCAN/HDBSCAN.

### 7.2 Robustez y estabilidad

- Sensibilidad a escalamiento, selección de features y ponderaciones.
- Sensibilidad a hiperparámetros y número de clusters.
- Estabilidad ante remuestreo o pequeñas perturbaciones del dataset.
- Comparación entre fechas de corte cuando exista dimensión temporal.

### 7.3 Coherencia espacial y sustantiva

- Mapear clusters y revisar patrones territoriales plausibles.
- Medir autocorrelación espacial cuando corresponda.
- Caracterizar distribuciones de features por cluster, no solo centroides.
- Validar interpretabilidad con conocimiento del dominio sin forzar el resultado.

## 8. Sensibilidad y prevención de leakage

- No incorporar al vector de features una etiqueta que se quiera redescubrir.
- Separar variables derivadas de una misma fuente para evitar doble ponderación accidental.
- Ejecutar especificaciones alternativas y reportar cuándo cambia la segmentación.

## 9. Reproducibilidad

- Versionar código, configuración, diccionario y decisiones metodológicas.
- Mantener datos crudos fuera de Git y registrar su huella/versión por un mecanismo seguro.
- Fijar `random_state` cuando aplique.
- Generar tablas y figuras del paper desde scripts/notebooks reproducibles.

## 10. Reporte

El paper debe distinguir claramente:

1. hechos observados en las fuentes,
2. variables construidas,
3. decisiones metodológicas,
4. resultados de clustering,
5. interpretación del dominio,
6. limitaciones y análisis de sensibilidad.
