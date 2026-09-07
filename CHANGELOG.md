# Changelog

Todos los cambios significativos del proyecto se documentan en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

---

## [Unreleased]

---

## [0.1.1] - 2026-09-07

### Corregido
- CRS proyectado para Lima: referencia `EPSG:32718` y estrategia UTM automática para operaciones métricas.
- Validación y alineamiento de CRS antes de buffers y spatial joins.
- Validación de coordenadas geográficas y renderizado cartográfico determinista.
- Manejo de valores faltantes, densidades con áreas no positivas y validaciones de clustering.
- Tipos de retorno y casos límite en evaluación y visualización.
- Referencias de plantilla de Colombia sustituidas por un contrato canónico provisional para Perú.
- Dependencias faltantes para Excel, Parquet y pruebas.
- Configuración de Ruff, Black, pytest y pre-commit alineada con CI.

### Agregado
- Tests geoespaciales para coordenadas, buffers, CRS y mapas.
- GitHub Actions con gates de Ruff, Black y pytest.
- Reglas metodológicas de trazabilidad, estabilidad, sensibilidad y prevención de leakage.
- Advertencias de gobernanza para repositorio público y licencia MIT.

---

## [0.1.0] - 2026-09-07

### Inicializacion
- Creacion del repositorio local.
- Inicializacion de Git.
- Estructura base del proyecto CODIP.
- Directorios: data/, notebooks/, src/, paper/, reports/, tests/, docs/ y config/.
- README, .gitignore, requirements.txt, pyproject.toml y documentacion inicial.
