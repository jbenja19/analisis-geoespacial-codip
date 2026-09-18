# Análisis Geoespacial - CODIP

Proyecto reproducible de análisis geoespacial y segmentación de oferta inmobiliaria para el estudio La Victoria (Lima, Perú).

## Estado actual

La fuente de verdad del estado vigente es [`docs/CURRENT_STATE.md`](docs/CURRENT_STATE.md). La autoridad sobre procedencia de datos y entregables es [`docs/LINEAGE.md`](docs/LINEAGE.md). El mapa de documentación está en [`docs/README.md`](docs/README.md).

Actualmente el repositorio contiene:

- fuente tabular del estudio La Victoria y su contrato en `schemas/source/`;
- configuración geoespacial con WGS84 como CRS de fuente y UTM 18S para análisis;
- notebook de modelado en `notebooks/04_modeling/01_cluster_proyectos_la_victoria.ipynb`;
- resultados procesados y material cartográfico/reportes del estudio;
- trazabilidad y gaps formalizados en `docs/LINEAGE.md`;
- tests estructurales y de contrato del dataset fuente.

La presencia de un notebook o un output no implica por sí sola que el resultado sea una autoridad metodológica certificada. `CURRENT_STATE.md` distingue lo vigente de lo histórico o pendiente.

## Principios

1. **Raw es inmutable.** No se corrige ni sobrescribe silenciosamente.
2. **La fuente manda.** Grain, llaves, joins, unidades y semántica se derivan de evidencia.
3. **Separación de capas.** `raw → interim → processed`; los outputs analíticos viven fuera de las capas de datos.
4. **Notebooks para explorar; `src/` para reproducir.** La lógica durable no debe depender de ejecución manual de celdas.
5. **CRS explícito.** Toda transformación espacial debe declarar CRS de entrada y de análisis.
6. **Decisiones materiales trazables.** Se registran en `docs/decisions/`.
7. **Validación proporcional.** No se ejecuta todo el proyecto por reflejo; se escala según blast radius.
8. **Datos y secretos bajo política explícita.** Ver `docs/DATA_POLICY.md`.

## Estructura

```text
analisis-geoespacial-codip/
├── data/
│   ├── raw/                 # evidencia fuente inmutable
│   ├── external/            # fuentes externas
│   ├── interim/             # transformaciones regenerables
│   └── processed/           # datasets analíticos derivados
├── notebooks/               # exploración y modelado interactivo
├── schemas/
│   ├── source/              # contratos de fuentes
│   └── canonical/           # contratos armonizados solo si hacen falta
├── src/
│   ├── data/
│   ├── geospatial/
│   ├── analysis/
│   ├── visualization/
│   └── utils/
├── tests/
├── config/
├── docs/
│   ├── README.md
│   ├── CURRENT_STATE.md
│   ├── LINEAGE.md
│   ├── project_workflow.md
│   ├── DATA_POLICY.md
│   ├── VALIDATION.md
│   ├── decisions/
│   ├── reports/
│   └── archive/
└── reports/                 # outputs analíticos: figuras, tablas, exports e informe
```

## Flujo de análisis

```text
recepción de fuente
→ inventario y perfilado
→ contrato / grain / llaves
→ reglas de calidad
→ transformación reproducible
→ EDA
→ decisión metodológica
→ análisis/modelado
→ validación
→ outputs
```

Detalle: [`docs/project_workflow.md`](docs/project_workflow.md).

## Instalación

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

Setup completo: [`docs/setup.md`](docs/setup.md).

## Validación local

```bash
python -m ruff check src/ tests/
python -m black --check src/ tests/
python -m pytest tests/ -v
```

La estrategia de escalamiento está en [`docs/VALIDATION.md`](docs/VALIDATION.md).

## Git

`main` es la única rama canónica. Las ramas temporales son excepcionales y deben borrarse después de integrarse. Ver [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Datos y publicación

Este repositorio es público y actualmente contiene excepciones explícitas de archivos de datos versionados. No generalices esas excepciones ni añadas nuevos datos reales sin clasificación de publicación y revisión de confidencialidad/licencia. Ver [`docs/DATA_POLICY.md`](docs/DATA_POLICY.md).
