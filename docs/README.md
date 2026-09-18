# Mapa de documentación

Este directorio separa estado vigente, proceso, decisiones e historia para evitar que un notebook o reporte antiguo se convierta accidentalmente en autoridad.

| Necesito entender... | Fuente |
|---|---|
| Qué existe y es vigente hoy | [CURRENT_STATE.md](CURRENT_STATE.md) |
| Cómo se ejecuta el trabajo analítico | [project_workflow.md](project_workflow.md) |
| Cómo instalar y validar localmente | [setup.md](setup.md) |
| Qué datos pueden versionarse | [DATA_POLICY.md](DATA_POLICY.md) |
| Qué validación corresponde a un cambio | [VALIDATION.md](VALIDATION.md) |
| Decisiones materiales | [decisions/](decisions/) |
| Evidencia histórica de ejecuciones/cierres | [reports/](reports/) |
| Documentación superseded | [archive/](archive/) |
| Outputs analíticos consumibles | [../reports/](../reports/) |

## Regla de autoridad

```text
CURRENT
→ docs/CURRENT_STATE.md + contratos/config/código vigentes

HISTORY
→ docs/reports/ + docs/archive/ + Git history

TARGET
→ decisiones propuestas o trabajo explícitamente marcado como pendiente
```

La fecha de un archivo no le concede autoridad. Para una afirmación sobre el presente, resuelve primero `CURRENT_STATE.md` y después verifica contrato/config/código cuando corresponda.

Los outputs de `reports/` son productos analíticos. Los archivos de `docs/reports/` son evidencia de proceso/validación; no deben duplicar el informe analítico.
