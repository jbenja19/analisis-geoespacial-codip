# Registro de decisiones

Este directorio contiene decisiones técnicas o metodológicas materiales y durables.

No abras un ADR para ajustes locales, documentación, renombres o cambios reversibles que no alteren una frontera analítica.

## Cuándo crear uno

Un ADR es apropiado si cambia de forma material:

- grain o keys;
- estrategia de joins;
- reglas semánticas;
- CRS de análisis;
- metodología principal;
- tratamiento de una fuente;
- arquitectura de transformación;
- política de publicación de datos.

## Formato

```text
# ADR-XXX: título
Fecha:
Estado: propuesta | aceptada | reemplazada
Contexto:
Evidencia:
Decisión:
Alternativas consideradas:
Consecuencias:
Validación:
Supersede / superseded by:
```

## Lifecycle

- **propuesta**: todavía no es autoridad CURRENT;
- **aceptada**: decisión vigente;
- **reemplazada**: permanece como historia, pero no gobierna el presente.

`docs/CURRENT_STATE.md` responde qué está vigente hoy. Un ADR explica por qué se tomó una decisión.
