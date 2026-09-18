# Agent Instructions — analisis-geoespacial-codip

> Scope: reglas de trabajo para humanos y agentes dentro de este repositorio.

## 1. Autoridad y contexto

- La rama canónica es `main`.
- `docs/CURRENT_STATE.md` describe únicamente el estado vigente.
- `docs/README.md` es el mapa de documentación.
- `docs/project_workflow.md` define el flujo de análisis.
- `docs/DATA_POLICY.md` gobierna qué datos pueden versionarse.
- `docs/VALIDATION.md` define validación proporcional.
- `docs/decisions/` registra decisiones materiales; no crear ADRs para ajustes triviales y reversibles.

No uses un reporte histórico, un notebook antiguo o una conversación como autoridad sobre el estado actual.

## 2. Modelo analítico

La responsabilidad del repositorio es análisis reproducible, no runtime de aplicación ni plataforma de IA.

Flujo esperado:

```text
source
→ data/raw
→ data/interim
→ data/processed
→ analysis / geospatial / modeling
→ reports
```

- `raw` es inmutable.
- El grano, llaves, joins, CRS, unidades y cambios semánticos deben ser explícitos.
- Los notebooks son válidos para exploración; la lógica necesaria para reproducir resultados debe migrar a `src/`.
- No introduzcas Medallion, Serving, backend, runtime, agentes, deployment o abstracciones equivalentes sin un problema concreto que lo justifique.

## 3. Cambios

Antes de editar:
1. identifica la pregunta o responsabilidad que cambia;
2. inspecciona la autoridad más cercana;
3. limita el cambio a la superficie mínima suficiente;
4. selecciona la validación proporcional de `docs/VALIDATION.md`.

Para cambios de significado analítico —grano, variable derivada, join, CRS, regla de inclusión, métrica o metodología— documenta evidencia y consecuencias. Si la decisión es material y durable, registra un ADR.

## 4. Git

Sigue `CONTRIBUTING.md`.

- `main` es la única autoridad compartida.
- No crear ramas permanentes `master`, `dev`, `develop` ni ramas de conveniencia.
- Crear una rama temporal solo cuando el aislamiento reduzca riesgo o facilite revisión.
- Toda rama temporal debe eliminarse después de integrarse.
- Nunca force-push ni reescribas historia publicada de `main`.

## 5. Evidencia

No inventes resultados de tests, análisis, benchmarks ni ejecución de notebooks. Reporta exactamente qué se ejecutó.

Prioriza evidencia compacta:

```text
schema / metadata / hashes / counts / diffs focalizados
→ consultas o muestras acotadas
→ outputs resumidos
```

No cargues datasets completos en contexto si un perfilado determinista basta.
