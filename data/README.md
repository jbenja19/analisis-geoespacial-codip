# Directorio de datos

Por regla general, los datos reales no se versionan en Git.

El repositorio alberga excepciones explícitas y acotadas correspondientes al estudio histórico de La Victoria (fuentes raw y outputs procesados iniciales), gobernadas estrictamente por [`docs/DATA_POLICY.md`](../docs/DATA_POLICY.md). Ningún archivo de datos adicional debe versionarse sin autorización explícita.

- `raw/`: copia inmutable de lo recibido (auditable contra `schemas/source/`).
- `external/`: fuentes externas sin mezclar con la fuente principal.
- `interim/`: resultados intermedios regenerables.
- `processed/`: datasets analíticos derivados (trazables según [`docs/LINEAGE.md`](../docs/LINEAGE.md)).

Nunca sobrescribir `raw/` desde scripts o notebooks.
