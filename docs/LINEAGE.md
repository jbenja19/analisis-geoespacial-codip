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
[Productor / herramienta: UNKNOWN] ───────────(UNKNOWN)────► reports/Estudio de Mercado...pdf
[Productor / herramienta: UNKNOWN] ───────────(UNKNOWN)────► reports/figures/estudio_lar/Layout *.png
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

- **Limpieza y selección exploratoria en el notebook**:
  - Filtro de proyectos activos (`activo == 1`, reduciendo de 43 a 30 registros) (`VERIFIED`).
  - Estandarización de 8 variables cuantitativas/espaciales con `StandardScaler` (`VERIFIED`).
  - Reducción dimensional PCA: Configurado con 3 componentes (`pca = PCA(n_components=3)`). El slicing posterior `PCA_components.iloc[:, :5]` selecciona efectivamente los 3 componentes existentes sin alterar la dimensionalidad (`VERIFIED`).
  - Embeddings de texto: Modelo `SentenceTransformer("thenlper/gte-small")` aplicado sobre texto concatenado que incluye latitud, longitud, cantidad de pisos, unidades totales, dormitorios promedio, área promedio y precio por m². Los campos `Proyecto` e `Inmobiliaria` aparecen comentados en el código y no forman parte del texto de entrada (`VERIFIED`).

### 3.3 Datasets en `data/processed/`

1. **`data/processed/informacion_oferta_proyectos_activos_la_victoria_5_clusters.xlsx`**:
   - **Estado**: `UNKNOWN`.
   - **Detalle**: Libro con 7 hojas (`Proyectos activos La Victoria`, `Clusters`, `Proyectos cluster 0`, `Proyectos  cluster 1`, `Proyectos cluster 2`, `Proyectos cluster 3`, `Proyectos cluster 4`). Contiene desgloses tipológicos donde las hojas por cluster aplican filas ocultas (`hidden="1"`). No es producido por el código actual del notebook.
2. **`data/processed/informacion_oferta_proyectos_la_victoria_segmentacion.xlsx`**:
   - **Estado**: `UNKNOWN`.
   - **Detalle**: Dataset de 121 registros a nivel tipológico. No existe en el repositorio código que lo genere ni que lo consuma.
   - **Decisión de contrato**: No se creará `schemas/processed/` para estos archivos mientras su semántica, granularidad y proceso generador no estén demostrados documental o analíticamente.

### 3.4 Notebook y Modelado

- **`notebooks/04_modeling/01_cluster_proyectos_la_victoria.ipynb`**:
  - **Entrada**: `data/raw/proyectos_la_victoria_sep25.csv` (`VERIFIED`).
  - **Salida intentada**: `../../data/processed/df_activos_cluster_5_la_victoria.csv` (No versionado en el repositorio).
  - **Salida versionada en el repositorio**: Ninguna correspondiente a ese nombre.

### 3.5 Reportes y Figuras

- **Informe PDF (`reports/Estudio de Mercado y Analisis Competitivo para Proyectos Inmobiliarios en La Victoria.pdf`)**:
  - **Estado**: `UNKNOWN`.
  - **Productor / herramienta**: `UNKNOWN`. El repositorio contiene el artefacto final, pero no contiene proyecto fuente, script ni metadata suficiente para demostrar qué herramienta lo generó.
- **Mapas (`reports/figures/estudio_lar/Layout 1.png` a `Layout 5.png`)**:
  - **Estado**: `UNKNOWN`.
  - **Productor / herramienta**: `UNKNOWN`. El nombre `Layout X.png` describe el nombre observado en el archivo, pero no permite inferir demostradamente la herramienta productora. El repositorio no contiene proyectos de cartografía ni scripts generadores.

---

## 4. Gaps de Lineage Identificados

1. **Gap Raw CSV vs Raw XLSX**: No se cuenta con el registro de exportación que indique si el CSV fue generado a partir del XLSX o viceversa.
2. **Gap Raw → Processed XLSX**: No existe script ejecutable que transforme la fuente raw (43 proyectos) o fuentes de tipologías primarias en los archivos `_5_clusters.xlsx` ni `_segmentacion.xlsx`.
3. **Gap Modelado → Processed**: El archivo CSV resultante del clustering en el notebook (`df_activos_cluster_5_la_victoria.csv`) no fue persistido ni integrado como insumo downstream.
4. **Gap Analysis → Reports**: No existe un pipeline automatizado para compilar las figuras ni el informe PDF a partir del código del repositorio.

---

## 5. Target Futuro

El flujo objetivo del repositorio para cuando se formalice la analítica es:

```text
source
→ raw
→ validation / profiling
→ interim (solo cuando una transformación intermedia sea necesaria)
→ processed
→ analysis / geospatial
→ reports
```

- La capa `interim` es optativa: no obliga a materializar un dataset físico intermedio si una transformación directa puede producir un `processed` reproducible sin perder auditabilidad ni claridad.
- Cada etapa `processed` deberá contar con grano, CRS y contrato formal documentado.
- Este flujo está catalogado como `TARGET`. No se asumirá implementado hasta que existan módulos ejecutables en `src/` que garanticen su reproducción determinista.
