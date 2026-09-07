# Guía de instalación

## Requisitos

- Python 3.10 o superior
- Git

## Crear el entorno

```bash
git clone https://github.com/jbenja19/analisis-geoespacial-codip.git
cd analisis-geoespacial-codip
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
Copy-Item .env.example .env
```

### Linux/macOS

```bash
source .venv/bin/activate
cp .env.example .env
```

## Pre-commit

```bash
python -m pre_commit install
```

## Verificación del scaffold

```bash
python -m ruff check src/ tests/
python -m black --check src/ tests/
python -m pytest tests/ -v
```

Estos comandos verifican calidad y estructura del repositorio. No ejecutan ningún análisis de datos.

## JupyterLab

```bash
python -m jupyter lab
```

`notebooks/` está deliberadamente vacío de análisis hasta disponer de data real.
