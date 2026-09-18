# Baseline de Evidencia del Repositorio

> Fecha de inspección: 2026-09-18
> Commit SHA inspeccionado (snapshot canónico): `0612fb09cf9035af947d9c8ddba5188c27819b95`
> Propósito: Establecer un inventario factual, no interpretativo y reproducible de los artefactos de datos, outputs y notebooks del repositorio.
> Metodología de identidad: Todas las métricas de tamaño y hashes se calculan canónicamente a partir de los Git blobs almacenados en el commit de referencia para eliminar discrepancias locales derivadas de normalización de saltos de línea (LF ↔ CRLF).

---

## 1. Inventario Canónico de Artefactos (Git Blob Identity)

| Ruta de Artefacto | Git Blob SHA | Git Blob Size (bytes) | SHA-256 del Blob | Tipo / Rol |
|---|---|---|---|---|
| `data/raw/proyectos_la_victoria_sep25.csv` | `e3fae1aec1039191261444b0f68ecdbdeb311cee` | 3,754 | `cbfb07831d275adb5c7abb6438407732001a3d80a1ee3e3da8cf76d9eeaf5ac8` | Datos Raw (CSV) |
| `data/raw/proyectos_la_victoria_sep25.xlsx` | `63dadaefe6336a2358cead9cc56e3a806e6ff228` | 14,033 | `56607c5153f32db8e0fa881f861120b2229fda49ca41cd61b407b514549544af` | Datos Raw (XLSX) |
| `data/processed/informacion_oferta_proyectos_activos_la_victoria_5_clusters.xlsx` | `f673bccc1038871f8e1d7237f200a781fa8c92fe` | 54,893 | `6edc97a77a5b4ba656ea3abf99ce4d1ad549b310dd97f27ea4a36d58abd6cea0` | Datos Processed (Histórico) |
| `data/processed/informacion_oferta_proyectos_la_victoria_segmentacion.xlsx` | `15c6de07318a35a48d262f8743cdc03c7aae2ecb` | 23,480 | `646c5190f2eeaf9f3281b56fb1663fdfb66d1d591a24cbf3bc05e1b6a18324ad` | Datos Processed (Histórico) |
| `reports/Estudio de Mercado y Analisis Competitivo para Proyectos Inmobiliarios en La Victoria.pdf` | `152078a8521edf64c8324981fa4c328bd7b5ca58` | 2,571,206 | `f40635d945303dc9f150c6151e4f2d6847ce37c45a5643833ec4f433721740d3` | Informe Maquetado (PDF) |
| `reports/figures/estudio_lar/Layout 1.png` | `561fc41d856aca2e0ab1228ef4e242baccb9cbeb` | 7,945,326 | `c2c224588b726fc8bb68544c62fe16323a1f05f40954bc101f538f756b960f53` | Mapa Cartográfico (Layout 1) |
| `reports/figures/estudio_lar/Layout 2.png` | `7ede7a4173726eaa06593ca575aab190a9efe278` | 7,791,441 | `1cd204ca97d87f52e058265117465d4cca8381d8316b396deea2e6694c5916c4` | Mapa Cartográfico (Layout 2) |
| `reports/figures/estudio_lar/Layout 3.png` | `c6c0229e53eab76735b8127c2e13487acd460273` | 6,800,862 | `ff440183c7ab069bdbfd82e230fdc49011123c6e6ade0dedfabecf689eecac25` | Mapa Cartográfico (Layout 3) |
| `reports/figures/estudio_lar/Layout 4.png` | `f7e79cc450ad461bd360e7a4262effc876bd1154` | 4,434,688 | `1eca26e92ba9229fddc85544e9786ccae15a6258200ff422f06b6af7f71c8ce7` | Mapa Cartográfico (Layout 4) |
| `reports/figures/estudio_lar/Layout 5.png` | `5446079edcdc0921245747ef3b0557812a3f06e3` | 6,599,646 | `57e72a79a347a4d6c2570d30b5f9581b28403dc6b770002b38b1311e70892608` | Mapa Cartográfico (Layout 5) |
| `notebooks/04_modeling/01_cluster_proyectos_la_victoria.ipynb` | `0ab0e4ba5725121db1e00312c4bf440a9156092d` | 570,221 | `6c9c826422788144044a479c2f780e70c8b0d759fadccc0eb02aecb57ff58408` | Notebook Exploratorio |

---

## 2. Inspección Detallada de Fuentes Raw

### 2.1 CSV Raw: `data/raw/proyectos_la_victoria_sep25.csv`

- **Encoding**: `latin1` (ISO-8859-1). Es el encoding declarado en el schema y utilizado para la lectura. Contiene caracteres con diacríticos no UTF-8 (ej. `VÖN`).
- **Número de registros**: 43 registros de datos (+ 1 línea de encabezado).
- **Columnas (11)**:
  1. `Inmobiliaria` (string)
  2. `Proyecto` (string)
  3. `Longitud` (float en WGS84, ej. `-77.0168333`)
  4. `Latitud` (float en WGS84, ej. `-12.0890073`)
  5. `cant und totales` (integer, ej. `663`)
  6. `cnat de pisos` (integer, ej. `34`)
  7. `prom_p dorm` (float formateado a 1 decimal, ej. `'1.8'`)
  8. `prom_p area` (float redondeado a entero, ej. `'52'`)
  9. `prom_p ticket` (string con comas de miles, ej. `'311,462'`)
  10. `prom_p pxm2` (string con comas de miles, ej. `'6,063'`)
  11. `activo` (integer binario, `0` o `1`)
- **Nulos observados**: 0 celdas vacías o nulas en todo el archivo.
- **Clave primaria candidata `(Inmobiliaria, Proyecto)`**:
  - Total pares observados: 43.
  - Pares únicos: 43.
  - Duplicados: 0.
- **Distribución de la variable `activo`**:
  - `activo = 1`: 30 proyectos (69.8%).
  - `activo = 0`: 13 proyectos (30.2%).

### 2.2 XLSX Raw: `data/raw/proyectos_la_victoria_sep25.xlsx`

- **Worksheets (1)**:
  - `Hoja1`: estado `visible`, `dimension ref`: `A1:K44`, `max_row`: 44, `max_column`: 11.
  - Filas de datos no vacías excluyendo encabezado: 43.
  - Proyectos únicos observados: 43.
- **Columnas (11)**: Exactamente los mismos 11 nombres y en el mismo orden que el CSV.

### 2.3 Comparación Factual entre CSV Raw y XLSX Raw

1. **Población y entidades**:
   - Ambos archivos representan exactamente la misma población de 43 proyectos inmobiliarios en La Victoria.
   - El conjunto de claves `(Inmobiliaria, Proyecto)` es idéntico entre ambos (`diff = 0`).
2. **Diferencias observadas en los valores**:
   - En el CSV, las columnas `prom_p dorm`, `prom_p area`, `prom_p ticket` y `prom_p pxm2` se encuentran redondeadas o con formato de texto con separador de miles (ej. `prom_p dorm` = `'1.8'`, `prom_p area` = `'52'`, `prom_p ticket` = `'311,462'`, `prom_p pxm2` = `'6,063'`).
   - En el XLSX, los mismos registros contienen valores numéricos continuos de punto flotante sin redondeo agresivo ni formateo de texto (ej. `prom_p dorm` = `1.8461538461538463`, `prom_p area` = `51.681749622926091`, `prom_p ticket` = `311461.53695324284`, `prom_p pxm2` = `6063.1930618401211`).
3. **Determinación de Canonicidad**:
   - **No se declara uno como canónico frente al otro.** La evidencia disponible en el repositorio no contiene el documento de proveniencia upstream que indique si el CSV fue una exportación formateada del Excel o si el Excel fue generado a partir de una fuente primaria distinta.
   - En el estado actual, el contrato `schemas/source/proyectos_la_victoria_sep25.yaml` y el notebook exploratorio apuntan formalmente al archivo CSV.

---

## 3. Inspección Detallada de Datasets en `data/processed/`

### 3.1 `informacion_oferta_proyectos_activos_la_victoria_5_clusters.xlsx`

- **Worksheets (7)** (todas con estado `visible`):
  1. `Proyectos activos La Victoria`:
     - `dimension ref`: `B2:L88`, `max_row`: 88, `max_column`: 12.
     - Filas no vacías de datos (excluyendo encabezado en fila 2): 84.
     - Columnas (11): `Inmobiliaria`, `Nombre de Proyecto`, `Longitud`, `Latitud`, `Und Totales`, `Cant de Pisos`, `Cant de Dorm`, `Cant de Und`, `Prom. Área Total`, `Prom. Ticket Oferta`, `Prom. Precio por m2 Oferta`.
     - Proyectos únicos observados: 31.
  2. `Clusters`:
     - `dimension ref`: `B2:H7`, `max_row`: 7, `max_column`: 8.
     - Filas no vacías de datos: 5 (resumen agregado de los 5 clusters).
     - Columnas (7): `Cluster`, `Und totales prom`, `Cant pisos prom`, `Cant dorm prom`, `Área prom (m2)`, `Ticket prom (S/)`, `Precio x m2 prom`.
  3. `Proyectos cluster 0`:
     - `dimension ref`: `B2:L86`, `max_row`: 86, `max_column`: 12.
     - Filas totales en XML: 83 filas de datos (mismas 11 columnas que la hoja principal).
     - Filas visibles / ocultas: 50 filas marcadas como ocultas (`hidden="1"`), 33 filas visibles.
     - Proyectos únicos observados en las 83 filas: 30.
  4. `Proyectos  cluster 1` (nombre con doble espacio):
     - `dimension ref`: `B2:L87`, `max_row`: 87, `max_column`: 12.
     - Filas totales en XML: 83 filas de datos.
     - Filas visibles / ocultas: 78 filas ocultas (`hidden="1"`), 5 filas visibles.
     - Proyectos únicos observados: 30.
  5. `Proyectos cluster 2`:
     - `dimension ref`: `B2:L87`, `max_row`: 87, `max_column`: 12.
     - Filas totales en XML: 83 filas de datos.
     - Filas visibles / ocultas: 78 filas ocultas (`hidden="1"`), 5 filas visibles.
     - Proyectos únicos observados: 30.
  6. `Proyectos cluster 3`:
     - `dimension ref`: `B2:L87`, `max_row`: 87, `max_column`: 12.
     - Filas totales en XML: 83 filas de datos.
     - Filas visibles / ocultas: 70 filas ocultas (`hidden="1"`), 13 filas visibles.
     - Proyectos únicos observados: 30.
  7. `Proyectos cluster 4`:
     - `dimension ref`: `B2:L86`, `max_row`: 86, `max_column`: 12.
     - Filas totales en XML: 83 filas de datos.
     - Filas visibles / ocultas: 49 filas ocultas (`hidden="1"`), 34 filas visibles.
     - Proyectos únicos observados: 30.
- **Relación con el notebook / código**: `UNKNOWN`. El notebook contiene celdas que calculan KMeans con 5 clusters sobre 30 proyectos activos, pero su celda de exportación intenta guardar un CSV llamado `df_activos_cluster_5_la_victoria.csv` a nivel de proyecto (30 filas), no un libro XLSX multificha con desgloses tipológicos y filas ocultas por cluster. No existe en el repositorio código que produzca este archivo.

### 3.2 `informacion_oferta_proyectos_la_victoria_segmentacion.xlsx`

- **Worksheets (1)**:
  - `Hoja1`: estado `visible`, `dimension ref`: `A1:O122`, `max_row`: 122, `max_column`: 15.
  - Filas no vacías de datos (excluyendo encabezado): 121.
  - Proyectos únicos observados: 43.
  - Columnas (15): `Inmobiliaria`, `Nombre de Proyecto`, `Longitud`, `Latitud`, `Cantidad de Unidades Totales`, `Cantidad de Pisos`, `Cantidad de Dormitorios`, `Cantidad de dormitorios por piso`, `Prom. Área Total`, `Prom. Precio de Lista Solarizado Neto`, `Prom. Precio por m2`, `prom_p dorm`, `prom_p area`, `prom_p ticket`, `prom_p pxm2`.
- **Relación con el notebook / código**: `UNKNOWN`. Ninguna celda del notebook ni script en `src/` genera este dataset tipológico ni consume sus 121 registros.

---

## 4. Inspección de Reportes y Figuras

### 4.1 Informe PDF

- **Archivo**: `reports/Estudio de Mercado y Analisis Competitivo para Proyectos Inmobiliarios en La Victoria.pdf`
- **Contenido**: Documento final de presentación/informe de mercado y análisis competitivo de la oferta en La Victoria.
- **Productor / herramienta**: `UNKNOWN`. El repositorio contiene el artefacto final, pero no contiene proyecto fuente, script ni metadata suficiente para demostrar qué herramienta lo generó.

### 4.2 Figuras Cartográficas (`reports/figures/estudio_lar/`)

- **Archivos**: `Layout 1.png` a `Layout 5.png`.
- **Contenido**: Salidas cartográficas impresas con mapas de calor, ubicación de proyectos y límites distritales.
- **Productor / herramienta**: `UNKNOWN`. El nombre `Layout X.png` describe el nombre observado en el archivo, pero no permite inferir demostradamente la herramienta productora. El repositorio no contiene proyectos de cartografía ni scripts generadores.

---

## 5. Inspección Factual del Notebook

- **Archivo**: `notebooks/04_modeling/01_cluster_proyectos_la_victoria.ipynb`
- **Estructura**: 49 celdas en total (1 celda Markdown de título, 48 celdas de código).
- **Dependencias importadas**:
  - Análisis y datos: `pandas`, `numpy`, `bs4` (BeautifulSoup), `requests`.
  - Visualización: `matplotlib.pyplot`, `seaborn`, `mpl_toolkits.mplot3d`, `folium`.
  - Modelado y ML: `sklearn.cluster.KMeans`, `sklearn.preprocessing.StandardScaler`, `sklearn.decomposition.PCA`, `sklearn.metrics.silhouette_score`, `yellowbrick.cluster.KElbowVisualizer`, `kneed.KneeLocator`, `umap.UMAP`, `hdbscan.HDBSCAN`, `sentence_transformers.SentenceTransformer`.
  - Entorno: `google.colab.drive`.
- **Fuentes que lee**:
  - `df = pd.read_csv(file_path, encoding='latin1')`, evaluando varias rutas relativas y locales, con fallback a Google Drive.
- **Filtros aplicados**:
  - `df_activos = df[df['activo'] == 1]` (restringe la muestra a los 30 proyectos activos).
- **Metodologías observadas en el código**:
  1. Estandarización de 8 variables numéricas/espaciales (`StandardScaler`).
  2. Detección de k óptimo mediante método del codo (Inertia) y `KElbowVisualizer`.
  3. Reducción dimensional con PCA: configurado explícitamente con 3 componentes (`pca = PCA(n_components=3)`). El ajuste posterior del modelo KMeans utiliza `PCA_components.iloc[:, :5]`, lo cual selecciona efectivamente los 3 componentes existentes sin aumentar la dimensionalidad.
  4. Clustering KMeans con $k=4$ y $k=5$ sobre los componentes PCA.
  5. Mapeo interactivo con Folium.
  6. Generación de embeddings mediante `SentenceTransformer("thenlper/gte-small")`. El texto de entrada se construye concatenando `Latitud`, `Longitud`, `cnat de pisos`, `cant und totales`, `prom_p dorm`, `prom_p area` y `prom_p pxm2`. Los campos `Proyecto` e `Inmobiliaria` aparecen comentados en el código y no forman parte del texto.
  7. Reducción dimensional con UMAP a 2 componentes.
  8. Clustering no supervisado basado en densidad con HDBSCAN sobre los embeddings reducidos.
- **Outputs que intenta escribir**:
  - Celda 13: `df_activos.to_csv(save_csv_path, index=False)` hacia `../../data/processed/df_activos_cluster_5_la_victoria.csv`.
  - Salida versionada en el repositorio: ninguna correspondiente a ese nombre.
- **Evaluación de reproducibilidad**:
  - Las celdas contienen salidas cacheadas de ejecuciones previas (incluyendo artefactos de Google Colab).
  - La presencia de estas salidas dentro del archivo no constituye prueba de reproducibilidad actual local ni certifica la validez metodológica definitiva del análisis.
