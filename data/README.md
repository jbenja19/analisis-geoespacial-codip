# Directorio de datos

Los datos reales no se versionan en Git.

- `raw/`: copia inmutable de lo recibido.
- `external/`: fuentes externas sin mezclar con la fuente principal.
- `interim/`: resultados intermedios regenerables.
- `processed/`: datasets analíticos reproducibles con grano documentado.

Nunca sobrescribir `raw/` desde scripts o notebooks.
