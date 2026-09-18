# Validación proporcional

La validación debe demostrar el cambio sin ejecutar trabajo irrelevante.

## L0 — Estática / documentación

Usa L0 para documentación y metadata sin cambio de comportamiento analítico.

Evidencia típica:

```bash
git diff --check
python -m pytest tests/test_repository_governance.py -v
```

## L1 — Estructura / contrato / helper focalizado

Usa L1 cuando cambia una fuente declarada, schema, configuración o helper local.

Evidencia típica:

```bash
python -m pytest tests/test_scaffold.py -v
python -m ruff check src/ tests/
python -m black --check src/ tests/
```

Añade tests focalizados para la transformación concreta si existe código reusable en `src/`.

## L2 — Transformación o análisis

Usa L2 cuando cambia:

- limpieza;
- grain;
- joins;
- unidades/moneda;
- CRS o cálculo espacial;
- feature engineering;
- reglas de inclusión;
- variables usadas por modelado;
- lógica reusable extraída a `src/`.

Valida productor y consumidor relevantes, calidad de datos y reconciliaciones del dataset afectado. No basta con que el notebook abra.

## L3 — Reproducción / publicación

Usa L3 cuando el cambio pretende publicar o reemplazar resultados del estudio, modificar metodología materialmente o promover un proceso reusable.

Debe incluir, según aplique:

- L0-L2;
- ejecución reproducible desde fuente autorizada;
- reconciliación de counts/grain/keys;
- validación geoespacial del CRS y geometrías;
- regeneración de outputs afectados;
- revisión de resultados y limitaciones;
- evidencia de qué notebook/script/comando se ejecutó.

## Escalamiento obligatorio

Sube de nivel si cambia significado analítico, grain, join, CRS, fuente, metodología o un output publicado.

Un PASS L0/L1 no significa que los resultados analíticos hayan sido reproducidos.

## Gate base del repositorio

Para cambios de infraestructura/gobernanza sin cambio analítico:

```bash
python -m ruff check src/ tests/
python -m black --check src/ tests/
python -m pytest tests/ -v
```

Ese gate es el que ejecuta CI actualmente.
