# Baseline de Evidencia del Repositorio

> Fecha de inspección: 2026-09-18  
> Commit SHA inspeccionado: `0612fb09cf9035af947d9c8ddba5188c27819b95`  
> Propósito: Establecer un inventario factual, no interpretativo y reproducible del estado de artefactos de datos, outputs y notebooks del repositorio.

---

## 1. Inventario General de Artefactos

| Ruta de Artefacto | Tamaño (bytes) | SHA-256 | Tipo / Rol |
|---|---|---|---|
| `data/raw/proyectos_la_victoria_sep25.csv` | 3,798 | `2430fbe14504c03312e127fa253b0015f4c8f18c2e3c0ff781dbc1ab40c74cee` | Datos Raw (CSV) |
| `data/raw/proyectos_la_victoria_sep25.xlsx` | 13,540 | `a951c89f074d28d052601ba472beff769d6588a44ca70f5e13028c2c8f615366` | Datos Raw (XLSX) |
| `data/processed/informacion_oferta_proyectos_activos_la_victoria_5_clusters.xlsx` | 37,951 | `ae34005081f96ba04a58eb881aa520977ba2f8c6344aa163fb1db6e695d3fa7e` | Datos Processed (Histórico) |
| `data/processed/informacion_oferta_proyectos_la_victoria_segmentacion.xlsx` | 23,480 | `646c5190f2eeaf9f3281b56fb1663fdfb66d1d591a24cbf3bc05e1b6a18324ad` | Datos Processed (Histórico) |
| `reports/Estudio de Mercado y Analisis Competitivo para Proyectos Inmobiliarios en La Victoria.pdf` | 2,571,206 | `f40635d945303dc9f150c6151e4f2d6847ce37c45a5643833ec4f433721740d3` | Informe Maquetado (PDF) |
| `reports/figures/estudio_lar/Layout 1.png` | 7,945,326 | `c2c224588b726fc8bb68544c62fe16323a1f05f40954bc101f538f756b960f53` | Mapa Cartográfico (Layout 1) |
| `reports/figures/estudio_lar/Layout 2.png` | 7,791,441 | `1cd204ca97d87f52e058265117465d4cca8381d8316b396deea2e6694c5916c4` | Mapa Cartográfico (Layout 2) |
| `reports/figures/estudio_lar/Layout 3.png` | 6,800,862 | `ff440183c7ab069bdbfd82e230fdc49011123c6e6ade0dedfabecf689eecac25` | Mapa Cartográfico (Layout 3) |
| `reports/figures/estudio_lar/Layout 4.png` | 4,434,688 | `1eca26e92ba9229fddc85544e9786ccae15a6258200ff422f06b6af7f71c8ce7` | Mapa Cartográfico (Layout 4) |
| `reports/figures/estudio_lar/Layout 5.png` | 6,599,646 | `57e72a79a347a4d6c2570d30b5f9581b28403dc6b770002b38b1311e70892608` | Mapa Cartográfico (Layout 5) |
| `notebooks/04_modeling/01_cluster_proyectos_la_victoria.ipynb` | 578,386 | `05242722f4f4abe64690a43bbbaf73f6e86e1db6a85ef4e41f687925efdfde2d` | Notebook Exploratorio |

---

## 2. Inspección Detallada de Fuentes Raw

### 2.1 CSV Raw: `data/raw/proyectos_la_victoria_sep25.csv`

- **Encoding**: `latin1` (ISO-8859-1 / Windows-1252 compatible). Contiene caracteres con tildes no UTF-8 (ej. `VÍN`).
- **Número de registros**: 43 registros de datos (+ 1 línea de encabezado).
- **Columnas (11)**:
  1. `Inmobiliaria` (string)
  2. `Proyecto` (string)
  3. `Longitud` (float en WGS84, ej. `-77.0168333`)
  4. `Latitud` (float en WGS84, ej. `-12.0890073`)
  5. `cant und totales` (integer, ej. `663`)
  6. `cnat de pisos` (integer, ej. `34`)
  7. `prom_p dorm` (float formateado, ej. `'1.8'`)
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

- **Hojas**: 1 sola hoja (`Hoja1`).
- **Dimensión declarada**: `A1:K44` (44 filas totales = 1 encabezado + 43 filas de datos).
- **Columnas (11)**: Exactamente los mismos 11 nombres y en el mismo orden que el CSV.
- **Clave candidata `(Inmobiliaria, Proyecto)`**: 43 proyectos únicos idénticos a los del CSV.

### 2.3 Comparación Factual entre CSV Raw y XLSX Raw

1. **Población y entidades**:
   - Ambos archivos representan exactamente la misma población de 43 proyectos inmobiliarios en La Victoria.
   - El conjunto de claves `(Inmobiliaria, Proyecto)` es idéntico entre ambos (`diff = 0`).
2. **Diferencias observadas en los valores**:
   - En el CSV, las columnas `prom_p dorm`, `prom_p area`, `prom_p ticket` y `prom_p pxm2` se encuentran redondeadas o con formato de texto con separador de miles (ej. `prom_p dorm` = `1.8`, `prom_p area` = `52`, `prom_p ticket` = `311,462`, `prom_p pxm2` = `6,063`).
   - En el XLSX, los mismos registros contienen valores numéricos continuos de punto flotante sin redondeo agresivo ni formateo de texto (ej. `prom_p dorm` = `1.8461538461538463`, `prom_p area` = `51.681749622926091`, `prom_p ticket` = `311461.53695324284`, `prom_p pxm2` = `6063.1930618401211`).
3. **Determinación de Canonicidad**:
   - **No se declara uno como canónico frente al otro.** La evidencia disponible en el repositorio no contiene el documento de proveniencia upstream que indique si el CSV fue una exportación formateada del Excel o si el Excel fue generado a partir de una fuente primaria distinta.
   - En el estado actual, el contrato `schemas/source/proyectos_la_victoria_sep25.yaml` y el notebook exploratorio apuntan formalmente al archivo CSV.

---

## 3. Inspección de Datasets en `data/processed/`

### 3.1 `informacion_oferta_proyectos_activos_la_victoria_5_clusters.xlsx`

- **Hojas (6)**:
  - `Resumen clusters`: Tabla resumen agregada con estadísticas de los 5 clusters.
  - `Proyectos  cluster 0`: 83 registros de datos.
  - `Proyectos  cluster 1`: 83 registros de datos.
  - `Proyectos cluster 2`: 83 registros de datos.
  - `Proyectos cluster 3`: 83 registros de datos.
  - `Proyectos cluster 4`: 83 registros de datos.
- **Columnas (11)**:
  `Inmobiliaria`, `Nombre de Proyecto`, `Longitud`, `Latitud`, `Und Totales`, `Cant de Pisos`, `Cant de Dorm`, `Cant de Und`, `Prom. Área Total`, `Prom. Ticket Oferta`, `Prom. Precio por m2 Oferta`.
- **Grano observado**: Desglose tipológico por proyecto y dormitorio (`Cant de Dorm`, `Cant de Und`), asignado a clusters.
- **Relación con el notebook / código**: `UNKNOWN`. El notebook contiene celdas que calculan KMeans con 5 clusters sobre 30 proyectos activos, pero su celda de exportación (celda 13) intenta guardar un CSV llamado `df_activos_cluster_5_la_victoria.csv` a nivel de proyecto (30 filas), no un libro XLSX multificha de 83 filas a nivel tipológico. No existe en el repositorio código que produzca este archivo.

### 3.2 `informacion_oferta_proyectos_la_victoria_segmentacion.xlsx`

- **Hojas (1)**: `Hoja1`.
- **Dimensión**: `A1:O122` (1 encabezado + 121 registros de datos).
- **Columnas (15)**:
  `Inmobiliaria`, `Nombre de Proyecto`, `Longitud`, `Latitud`, `Cantidad de Unidades Totales`, `Cantidad de Pisos`, `Cantidad de Dormitorios`, `Cantidad de dormitorios por piso`, `Prom. Área Total`, `Prom. Precio de Lista Solarizado Neto`, `Prom. Precio por m2`, `prom_p dorm`, `prom_p area`, `prom_p ticket`, `prom_p pxm2`.
- **Grano observado**: Desglose a nivel de tipología/dormitorios por proyecto de la oferta global (121 filas).
- **Relación con el notebook / código**: `UNKNOWN`. Ninguna celda del notebook ni script en `src/` genera este dataset ni consume sus 121 filas tipológicas.

---

## 4. Inspección de Reportes y Figuras

### 4.1 Informe PDF

- **Archivo**: `reports/Estudio de Mercado y Analisis Competitivo para Proyectos Inmobiliarios en La Victoria.pdf` (2.57 MB).
- **Contenido**: Documento final de presentación/informe ejecutivo de mercado y análisis competitivo de la oferta en La Victoria.
- **Productor / Lineage**: `UNKNOWN`. Maquetado fuera del repositorio (herramientas de diseño/presentación); no deriva directamente de una ejecución automatizada en este código.

### 4.2 Figuras Cartográficas (`reports/figures/estudio_lar/`)

- **Archivos**: `Layout 1.png` a `Layout 5.png` (resoluciones altas, entre 4.4 MB y 7.9 MB cada una).
- **Contenido**: Salidas cartográficas impresas con mapas de calor, ubicación de proyectos y límites distritales.
- **Productor / Lineage**: `UNKNOWN`. El patrón de nombres "Layout X" corresponde a composiciones de impresión exportadas típicamente desde software GIS (QGIS / ArcGIS), no desde las funciones de Matplotlib/Seaborn/Folium presentes en el notebook.

---

## 5. Inspección del Notebook

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
- **Metodologías presentes en el código**:
  1. Estandarización de 8 variables numéricas/espaciales (`StandardScaler`).
  2. Detección de k óptimo mediante método del codo (Inertia) y `KElbowVisualizer`.
  3. Reducción de dimensionalidad con PCA a 5 componentes.
  4. Clustering KMeans con $k=4$ y $k=5$ sobre componentes PCA.
  5. Asignación de columna `cluster` ($k=5$).
  6. Mapeo interactivo en Folium.
  7. Embedding / NLP exploratorio con `SentenceTransformer` ('all-MiniLM-L6-v2') sobre nombres de proyectos.
  8. Reducción dimensional con UMAP a 2 componentes.
  9. Clustering no supervisado basado en densidad con HDBSCAN sobre embeddings.
- **Outputs que intenta escribir**:
  - Celda 13: `df_activos.to_csv(save_csv_path, index=False)` hacia `../../data/processed/df_activos_cluster_5_la_victoria.csv`.
  - Este archivo CSV **no existe** en el repositorio.
- **Evaluación de reproducibilidad**:
  - Las celdas contienen salidas cacheadas de ejecuciones previas (algunas en Google Colab).
  - La presencia de estas salidas dentro del JSON del notebook no constituye prueba de reproducibilidad actual local ni certifica la validez metodológica definitiva del análisis.
