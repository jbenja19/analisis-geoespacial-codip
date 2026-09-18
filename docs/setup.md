# Guía de instalación

## Requisitos

- Python 3.10 o superior
- Git

## Crear el entorno

```bash
git clone https://github.com/jbenja19/analisis-geoespacial-codip.git
cd analisis-geoespacial-codip
git switch main
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
if (-not (Test-Path .env)) { Copy-Item .env.example .env }
```

### Linux/macOS

```bash
source .venv/bin/activate
test -f .env || cp .env.example .env
```

## Pre-commit

```bash
python -m pre_commit install
```

## Gate local base

```bash
python -m ruff check src/ tests/
python -m black --check src/ tests/
python -m pytest tests/ -v
```

O con Make:

```bash
make validate
```

Este gate valida estructura, contratos y gobernanza. No equivale a reproducir todos los análisis. Para cambios analíticos usa `VALIDATION.md`.

## JupyterLab

```bash
python -m jupyter lab
```

Los notebooks existentes son superficies de exploración/modelado. La lógica reusable y estable debe migrar a `src/`.

## Sincronización Git

La rama canónica es `main`.

```bash
git fetch --prune origin
git switch main
git pull --ff-only origin main
```

No crees ramas permanentes adicionales. Ver `../CONTRIBUTING.md`.
