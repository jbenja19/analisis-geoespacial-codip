# Lineage de Datos y Artefactos

> Status: CURRENT  
> Fecha de actualización: 2026-09-18  
> Autoridad: Este documento es la autoridad sobre la procedencia, transformaciones conocidas y gaps de trazabilidad de los datos y outputs en el repositorio.

---

## 1. Convención de Estados de Lineage

Para evitar atribuir orígenes no demostrados a los artefactos, cada relación de procedencia se califica bajo una de cuatro categorías estrictas:

- **`VERIFIED`**: Relación demostrada inequívocamente mediante código ejecutable, rutas de archivo o evidencia documental directa en el repositorio.
- **`INFERRED`**: Relación razonablemente inferida a partir de similitud de esquemas o valores, pero que carece de código o traza ejecutable explícita.
- **`UNKNOWN`**: Procedencia o relación no demostrable con la evidencia actualmente disponible en el repositorio.
- **`TARGET`**: Flujo futuro previsto y deseado, pendiente de implementación como proceso reproducible.

---

## 2. Mapa de Lineage Vigente

```text
[ Fuentes Raw ]
data/raw/proyectos_la_victoria_sep25.csv ───(VERIFIED)───► notebooks/04_modeling/01_cluster_...ipynb
data/raw/proyectos_la_victoria_sep25.xlsx ───(UNKNOWN)────► [Sin consumidor en código actual]

[ Artefactos Procesados ]
[Proceso o script generador no documentado] ───(UNKNOWN)────► data/processed/..._5_clusters.xlsx
[Proceso o script generador no documentado] ───(UNKNOWN)────► data/processed/..._segmentacion.xlsx

[ Entregables y Reportes ]
[Herramienta externa de diseño / GIS] ───(UNKNOWN)────► reports/Estudio de Mercado...pdf
[Composición de impresión externa / QGIS] ───(UNKNOWN)────► reports/figures/estudio_lar/Layout *.png
```

---

## 3. Detalle por Componente

### 3.1 Fuentes Raw

1. **`data/raw/proyectos_la_victoria_sep25.csv`**:
   - **Estado**: `VERIFIED`.
   - **Consumidor verificado**: Leído directamente en la celda 3 de `notebooks/04_modeling/01_cluster_proyectos_la_victoria.ipynb`.
   - **Contrato de gobierno**: Formalizado y testeado en `schemas/source/proyectos_la_victoria_sep25.yaml`.
2. **`data/raw/proyectos_la_victoria_sep25.xlsx`**:
   - **Estado**: `INFERRED` respecto a la misma población que el CSV; `UNKNOWN` respecto a su relación de precedencia exacta con el CSV.
   - **Consumidor**: Ningún script ni notebook del repositorio lee actualmente este archivo.

### 3.2 Transformaciones Conocidas

- **Limpieza y selección exploratoria**:
  - Filtro de proyectos activos (`activo == 1`, reduciendo de 43 a 30 registros) en el notebook (`VERIFIED`).
  - Estandarización de variables con `StandardScaler` en el notebook (`VERIFIED`).
  - Reducción dimensional PCA (5 componentes) en el notebook (`VERIFIED`).

### 3.3 Datasets en `data/processed/`

1. **`data/processed/informacion_oferta_proyectos_activos_la_victoria_5_clusters.xlsx`**:
   - **Estado**: `UNKNOWN`.
   - **Detalle**: Libro con 6 hojas a nivel tipológico (83 filas por cluster). No es producido por el código actual del notebook (que sólo intentaba escribir un CSV a nivel proyecto).
2. **`data/processed/informacion_oferta_proyectos_la_victoria_segmentacion.xlsx`**:
   - **Estado**: `UNKNOWN`.
   - **Detalle**: Dataset de 121 registros a nivel tipológico. No existe en el repositorio código que lo genere ni que lo consuma.
   - **Decisión de contrato**: No se creará `schemas/processed/` para estos archivos mientras su semántica, granularidad y proceso generador no estén demostrados documental o analíticamente.

### 3.4 Notebook y Modelado

- **`notebooks/04_modeling/01_cluster_proyectos_la_victoria.ipynb`**:
  - **Entrada**: `data/raw/proyectos_la_victoria_sep25.csv` (`VERIFIED`).
  - **Salida intentada**: `../../data/processed/df_activos_cluster_5_la_victoria.csv` (No versionado en el repositorio).
  - **Salida persistida en disco**: Ninguna.

### 3.5 Reportes y Figuras

- **Informe PDF (`reports/Estudio de Mercado y Analisis Competitivo para Proyectos Inmobiliarios en La Victoria.pdf`)**:
  - **Estado**: `UNKNOWN`. Maquetado externo.
- **Mapas (`reports/figures/estudio_lar/Layout 1.png` a `Layout 5.png`)**:
  - **Estado**: `UNKNOWN`. Generados externamente mediante layouts cartográficos (GIS).

---

## 4. Gaps de Lineage Identificados

1. **Gap Raw CSV vs Raw XLSX**: No se cuenta con el registro de exportación que indique si el CSV fue generado a partir del XLSX o viceversa.
2. **Gap Raw → Processed XLSX**: No existe script ejecutable que transforme la fuente raw (43 proyectos) o fuentes de tipologías primarias en los archivos `_5_clusters.xlsx` (83 filas tipológicas por cluster) ni `_segmentacion.xlsx` (121 filas tipológicas).
3. **Gap Modelado → Processed**: El archivo CSV resultante del clustering en el notebook (`df_activos_cluster_5_la_victoria.csv`) no fue persistido ni integrado como insumo downstream.
4. **Gap Analysis → Reports**: No existe un pipeline automatizado para compilar las figuras ni el informe PDF a partir del código del repositorio.

---

## 5. Target Futuro

El flujo objetivo del repositorio para cuando se formalice la analítica es:

```text
source (recepción externa documentada)
  │
  ▼ (copia inmutable auditada)
data/raw/
  │
  ▼ (validación con schema en CI y perfilado en src/data/)
data/interim/ (tipologías normalizadas, joins con cartografía oficial)
  │
  ▼ (transformación tipológica / proyecto reproducible en src/data/)
data/processed/ (datasets analíticos con grain, CRS y contrato formal)
  │
  ▼ (modelado y segmentación en src/analysis/ y src/geospatial/)
reports/ (figuras generadas programáticamente e informes reproducibles)
```

> **Nota**: Este flujo está catalogado como `TARGET`. No se asumirá implementado hasta que existan módulos ejecutables en `src/` que garanticen su reproducción determinista.
