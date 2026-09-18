# Changelog

Todos los cambios significativos del proyecto se documentan en este archivo.

## [Unreleased]

## [0.2.0] - 2026-09-18

### Incorporación y Gobernanza

- Se incorpora formalmente el estudio de oferta inmobiliaria en La Victoria (Septiembre 2025).
- Se formaliza el contrato de datos para la fuente raw en `schemas/source/proyectos_la_victoria_sep25.yaml`.
- Se incorpora el notebook exploratorio de modelado y clustering en `notebooks/04_modeling/`.
- Se registran los datasets procesados y entregables cartográficos/informes como excepciones gobernadas en `docs/DATA_POLICY.md`.
- Se crea la autoridad sobre procedencia y trazabilidad en `docs/LINEAGE.md`, distinguiendo explícitamente artefactos verificados de relaciones no demostradas (`UNKNOWN`).
- Se genera el reporte factual de baseline en `docs/reports/2026-09-18_repository_baseline.md`.
- Se endurecen las pruebas automatizadas del contrato de datos de entrada (`tests/test_source_contract.py`) y de control de datos versionados (`tests/test_data_policy.py`).
- Se elimina scaffolding especulativo (variables de entorno no utilizadas, dependencias huérfanas de logging y dotenv).

## [0.1.2] - 2026-09-07

### Estructura

- Se redefine el repositorio como scaffold previo a cualquier análisis.
- Se crean capas versionadas para `data/raw`, `external`, `interim` y `processed` mediante placeholders.
- Se agregan `notebooks/`, `schemas/`, `reports/` y registro de decisiones.
- Se elimina la preselección de clustering, métricas, feature engineering y visualizaciones.
- Se reemplaza el diccionario provisional por una plantilla vacía basada en evidencia futura.
- CI queda orientado a lint, formato y validación estructural.
- Se eliminan dependencias específicas de ML hasta que la data y la pregunta justifiquen su incorporación.

## [0.1.0] - 2026-09-07

### Inicialización

- Creación de la estructura inicial del repositorio.
