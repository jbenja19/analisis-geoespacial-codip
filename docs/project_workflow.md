# Workflow del proyecto

Este documento define **el orden de trabajo**, no una metodología analítica.

## Fase 0 — Recepción

- Colocar una copia exacta de cada fuente en `data/raw/`.
- No editar, renombrar internamente ni sobrescribir el contenido de los archivos raw.
- Registrar origen, fecha de recepción, responsable, periodo cubierto y restricciones de uso.

## Fase 1 — Inventario de fuentes

Antes de transformar:

- identificar archivos/tablas/endpoints;
- registrar formatos y tamaños;
- identificar frecuencia y cobertura temporal;
- identificar granularidad aparente;
- registrar documentación disponible;
- registrar campos de ubicación existentes;
- detectar si existe un identificador estable.

No se construye un modelo ni se define una taxonomía en esta fase.

## Fase 2 — Perfilado técnico

Para cada fuente real:

- tipos observados;
- porcentaje de nulos;
- cardinalidad;
- duplicados;
- rangos y valores extremos;
- codificaciones;
- consistencia temporal;
- calidad de campos geográficos;
- candidatos a llave primaria/foránea.

El perfilado debe generar evidencia, no corregir silenciosamente la data.

## Fase 3 — Diccionario y contratos

Completar `docs/data_dictionary_template.md` y crear los contratos necesarios en `schemas/source/`.

Solo después de esta fase se puede decidir si hace falta un esquema canónico en `schemas/canonical/`.

## Fase 4 — Diseño de transformaciones

Con la semántica ya entendida:

- definir reglas de limpieza;
- definir joins;
- definir tratamiento de duplicados y nulos;
- definir unidades y monedas;
- definir reglas temporales;
- definir reglas geoespaciales y CRS;
- documentar cada decisión no trivial en `docs/decisions/`.

La implementación reutilizable debe ir en `src/`.

## Fase 5 — Dataset analítico

Crear capas reproducibles:

```text
raw → interim → processed
```

`raw` nunca se modifica. `interim` puede regenerarse. `processed` debe tener un grano explícito y trazabilidad hacia las fuentes.

## Fase 6 — Exploración

Recién aquí comienza el EDA tabular y geoespacial. Los notebooks pueden utilizarse para exploración, pero cualquier transformación necesaria para reproducir resultados debe migrar a `src/`.

## Fase 7 — Decisión metodológica

Elegir métodos en función de:

- pregunta de investigación o negocio;
- unidad de análisis;
- estructura real de las variables;
- dimensión temporal;
- cobertura espacial;
- tamaño muestral;
- sesgos y limitaciones de las fuentes.

El scaffold no preselecciona clustering, regresión, ML ni ninguna otra técnica.

## Fase 8 — Análisis, validación y outputs

Solo después de las fases anteriores se implementan análisis/modelos, validaciones y productos finales. Figuras, tablas y exportaciones van en `reports/`.
