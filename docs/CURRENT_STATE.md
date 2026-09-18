# Estado actual

> Status: CURRENT
> Last verified structurally: 2026-09-18
> Canonical repository: jbenja19/analisis-geoespacial-codip
> Canonical branch: main

Este archivo describe solo el estado vigente conocido del repositorio. No convierte resultados exploratorios en conclusiones certificadas.

## 1. Alcance

El repositorio contiene el estudio geoespacial/inmobiliario de La Victoria (Lima) y su material de análisis asociado.

Configuración vigente:

```text
project stage       = exploratory_analysis
unit of analysis    = proyectos_inmobiliarios_la_victoria
temporal scope      = septiembre_2025
source CRS          = EPSG:4326
analysis CRS        = EPSG:32718
```

Autoridad ejecutable: `config/config.yaml`.

## 2. Datos

Fuente tabular declarada:

```text
data/raw/proyectos_la_victoria_sep25.csv
records declared = 43
grain candidate  = Inmobiliaria + Proyecto
source CRS       = EPSG:4326
```

Contrato: `schemas/source/proyectos_la_victoria_sep25.yaml`.

El repositorio también contiene una versión XLSX de la fuente y datasets procesados del estudio. Su presencia en Git es una excepción explícita; no autoriza añadir nuevos datos reales. Ver `DATA_POLICY.md`.

## 3. Flujo de datos y lineage

```text
source
→ raw
→ interim
→ processed
→ analysis / geospatial / modeling
→ reports
```

`raw` es inmutable. `interim` debe ser regenerable. `processed` debe declarar grano y lineage cuando se formalice una transformación reusable.

La autoridad vigente sobre trazabilidad, relaciones verificadas y gaps es [`docs/LINEAGE.md`](LINEAGE.md).

## 4. Análisis presente

Existe el notebook:

```text
notebooks/04_modeling/01_cluster_proyectos_la_victoria.ipynb
```

La configuración registra la metodología actual como:

```text
clustering_kmeans_pca_and_embeddings_hdbscan
```

Esto describe la implementación/exploración presente; no afirma por sí solo que una metodología sea óptima, estable o certificada para reutilización futura.

## 5. Outputs presentes

El repositorio contiene:

- datasets procesados de segmentación/clustering en `data/processed/`;
- informe PDF del estudio en `reports/`;
- figuras/cartografía en `reports/figures/estudio_lar/`.

Los outputs son evidencia/entregables del estudio. Las reglas necesarias para regenerarlos deberían migrar progresivamente desde notebooks a `src/` cuando se conviertan en proceso reusable.

## 6. Calidad y reproducibilidad

El gate base del repositorio cubre:

- Ruff sobre `src/` y `tests/`;
- Black check sobre `src/` y `tests/`;
- pytest sobre tests estructurales, contrato de fuente, política de datos y gobernanza del repo.

Estado de reproducibilidad actual por componente:

| Componente | Estado de Reproducibilidad | Evidencia / Autoridad |
|---|---|---|
| Fuente y contrato raw | **REPRODUCIBLE** | `schemas/source/` + `tests/test_source_contract.py` |
| Notebook exploratorio | **HISTÓRICO / NO AUTOMATIZADO** | `notebooks/04_modeling/` (salidas cacheadas, sin runner CI) |
| Processed históricos (`.xlsx`) | **HISTÓRICO / UNKNOWN** | `data/processed/` (sin script generador en repo, ver `LINEAGE.md`) |
| Reporte PDF y cartografía | **ENTREGABLE EXTERNO** | `reports/` (generados vía software GIS/diseño externo) |
| Lógica reusable en `src/` | **SCAFFOLD / TARGET** | `src/` (módulos base preparados para migración progresiva) |

No se declara aquí ejecución exitosa de un notebook completo ni reproducción end-to-end de todos los outputs a menos que exista evidencia específica de esa ejecución.

## 7. Git

`main` es la única rama canónica definida por política del repositorio.

Ramas temporales pueden existir solo durante trabajo aislado y deben eliminarse después de integración. La configuración remota de default branch/protección es una responsabilidad de GitHub y debe mantenerse alineada con esta autoridad.

## 8. CURRENT / HISTORY / TARGET

```text
CURRENT
→ este archivo, config, schemas y código vigente

HISTORY
→ docs/reports/, docs/archive/ y Git history

TARGET
→ cambios propuestos aún no implementados
```

No uses documentación histórica para afirmar el estado actual.
