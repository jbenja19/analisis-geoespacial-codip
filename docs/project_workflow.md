# Workflow del proyecto

Este documento define el orden de trabajo analítico. No prescribe una metodología única.

## Fase 0 — Recepción

- colocar copia exacta de cada fuente en `data/raw/` solo si su política de publicación lo permite;
- no editar ni sobrescribir raw;
- registrar origen, fecha, responsable, periodo y restricciones;
- aplicar `DATA_POLICY.md`.

## Fase 1 — Inventario

Antes de transformar:

- identificar archivos/tablas/endpoints;
- formato, tamaño y cobertura;
- grain aparente;
- campos geográficos;
- identificadores candidatos;
- documentación y restricciones disponibles.

## Fase 2 — Perfilado técnico

Para cada fuente:

- tipos observados;
- nulos;
- cardinalidad;
- duplicados;
- rangos/outliers;
- encoding;
- consistencia temporal;
- calidad geográfica;
- llaves candidatas.

El perfilado genera evidencia; no corrige silenciosamente.

## Fase 3 — Contratos y significado

Crear/actualizar `schemas/source/` y documentar:

- grain;
- keys;
- unidades;
- significado de campos;
- cobertura temporal;
- CRS;
- relaciones observadas.

Crear un esquema canónico solo si varias fuentes necesitan armonización real.

## Fase 4 — Transformaciones

Definir explícitamente:

- limpieza;
- joins y cardinalidades;
- deduplicación/nulos;
- unidades/monedas;
- reglas temporales;
- reglas geoespaciales/CRS.

La lógica reusable vive en `src/`. Una decisión durable que cambie significado debe registrarse en `docs/decisions/`.

## Fase 5 — Dataset analítico

```text
raw → interim → processed
```

- raw: inmutable;
- interim: regenerable;
- processed: grain y lineage explícitos.

## Fase 6 — Exploración

Los notebooks sirven para EDA y experimentación. Si una transformación es necesaria para reproducir un resultado, debe migrar a código reusable antes de tratarla como proceso estable.

## Fase 7 — Decisión metodológica

Seleccionar métodos según:

- pregunta;
- unidad de análisis;
- estructura de variables;
- dimensión temporal;
- cobertura espacial;
- tamaño muestral;
- sesgos/limitaciones.

La metodología vigente de un estudio no debe generalizarse automáticamente a otro.

## Fase 8 — Análisis, validación y outputs

Ejecutar análisis/modelos y generar outputs en `reports/`.

La validación se selecciona según `VALIDATION.md`. Cambiar un output publicado o metodología material exige validación L3 o evidencia equivalente.

## Fase 9 — Estado y cierre

Cuando el estado vigente cambie:

- actualizar `CURRENT_STATE.md`;
- registrar ADR solo si hubo una decisión material;
- conservar evidencia histórica relevante en `docs/reports/`;
- mover documentación superseded a `docs/archive/` cuando corresponda;
- no duplicar la misma autoridad en múltiples documentos.
