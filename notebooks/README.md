# Notebooks

Este directorio alberga notebooks utilizados como superficies de exploración, prototipado y modelado interactivo.

Actualmente contiene:
- `04_modeling/01_cluster_proyectos_la_victoria.ipynb`: Prototipo exploratorio de clustering y reducción dimensional para los proyectos inmobiliarios de La Victoria.

Pautas de trabajo:
1. Los notebooks son válidos para experimentación, análisis preliminar y visualización rápida.
2. La lógica necesaria para reproducir resultados analíticos estables debe migrar de manera estructurada a `src/`.
3. La presencia de salidas cacheadas dentro de un notebook no equivale a una ejecución certificada ni a un pipeline reproducible (ver [`docs/CURRENT_STATE.md`](../docs/CURRENT_STATE.md) y [`docs/LINEAGE.md`](../docs/LINEAGE.md)).
4. No sobrescribir `data/raw/` desde ningún notebook.
