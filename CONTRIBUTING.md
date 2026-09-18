# Contribuir

Este repositorio prioriza un flujo simple, reproducible y con una sola autoridad Git.

## Rama canónica

`main` es la única rama canónica del proyecto.

Política:

- no mantener ramas permanentes `master`, `dev`, `develop` o similares;
- no crear una rama por defecto para cada cambio;
- usar una rama temporal solo si el cambio necesita aislamiento, revisión o rollback independiente;
- nombres temporales permitidos: `feat/*`, `fix/*`, `chore/*`, `analysis/*`;
- una rama temporal representa una sola iniciativa;
- eliminar la rama remota y local inmediatamente después de integrarla;
- no force-push a `main`.

Para cambios pequeños de documentación, configuración o mantenimiento en un flujo de un solo mantenedor, un fast-forward directo a `main` es aceptable cuando las reglas remotas lo permitan y la validación proporcional haya pasado.

## Antes de modificar

Comprueba:

```bash
git status --short
git branch --show-current
git rev-parse HEAD
git fetch --prune origin
```

No mezcles cambios no relacionados ni sobrescribas trabajo local ajeno.

## Validación

Usa `docs/VALIDATION.md`.

Un PASS focalizado no significa regresión completa. Reporta los comandos realmente ejecutados.

## Datos

Antes de añadir datos reales, revisa `docs/DATA_POLICY.md`. El hecho de que un formato o archivo pueda versionarse técnicamente no implica autorización para publicarlo.

## Decisiones

Usa `docs/decisions/` solo para decisiones materiales y durables: cambios de grano, semántica, CRS, metodología, reglas de transformación, arquitectura o publicación de datos.

## Integración

Antes de actualizar `main`:

1. sincroniza con `origin/main`;
2. ejecuta la validación proporcional;
3. revisa el diff y los archivos staged;
4. publica sin reescribir historia;
5. verifica que el remoto apunta al commit esperado;
6. si se usó una rama temporal, elimínala tras integrar.
