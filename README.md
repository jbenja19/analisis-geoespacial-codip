# Análisis Geoespacial - CODIP

> Segmentación de proyectos inmobiliarios mediante análisis geoespacial y ciencia de datos.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Base%20t%C3%A9cnica%20inicial-orange)]()

## Propósito

Este repositorio contiene la base técnica y metodológica de un proyecto de
análisis geoespacial aplicado al mercado inmobiliario para **CODIP,
Confederación de Desarrolladores Inmobiliarios del Perú**.

El objetivo es construir y validar una metodología reproducible para segmentar
proyectos inmobiliarios a partir de características físicas, comerciales,
socioeconómicas y territoriales, dejando trazabilidad suficiente para un paper
técnico/académico.

**Estado actual:** scaffold funcional. Ya existen módulos iniciales y tests, pero
la metodología todavía debe validarse con las fuentes reales antes de interpretar
clusters como resultados de negocio o como una taxonomía definitiva.

## Principios del proyecto

- **Source truth primero:** no se inventan columnas ni semánticas faltantes.
- **CRS explícito:** WGS84 (`EPSG:4326`) para intercambio/visualización; operaciones
  métricas en un CRS proyectado apropiado.
- **Sin distancias en grados:** buffers, áreas y distancias no se calculan directamente
  sobre latitud/longitud.
- **Reproducibilidad:** configuración, transformaciones, tests y decisiones deben quedar versionadas.
- **Validación múltiple:** no se selecciona un clustering únicamente por silhouette u otra métrica interna.
- **No causalidad:** los clusters describen estructura empírica; no prueban relaciones causales.

## Convención geoespacial

Para Lima Metropolitana, WGS 84 / UTM zone 18S corresponde a `EPSG:32718` y usa
metros. Sin embargo, el código de buffers usa **estimación UTM automática por
defecto**, para no aplicar una zona fija a observaciones ubicadas en otra parte
del Perú.

## Estructura

```text
analisis-geoespacial-codip/
├── data/                  # Ignorado por Git: raw/interim/processed/external
├── notebooks/             # Exploración y análisis reproducible
├── src/
│   ├── data/              # Ingesta, limpieza y feature engineering
│   ├── geospatial/        # CRS, joins, buffers, geocodificación y mapas
│   ├── models/            # Preprocesamiento, clustering y evaluación
│   ├── visualization/     # Gráficos estadísticos/geoespaciales
│   └── utils/             # Configuración e I/O
├── tests/                 # Tests unitarios y geoespaciales
├── docs/                  # Metodología, diccionario y setup
├── paper/                 # Outline, referencias, figuras y versiones del paper
├── config/                # Configuración reproducible
└── .github/workflows/     # CI
```

La estructura puede evolucionar con el proyecto, pero los cambios relevantes deben
documentarse.

## Instalación

### Requisitos

- Python 3.10+
- Git

### Windows PowerShell

```powershell
git clone https://github.com/jbenja19/analisis-geoespacial-codip.git
cd analisis-geoespacial-codip
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

### Linux/macOS

```bash
git clone https://github.com/jbenja19/analisis-geoespacial-codip.git
cd analisis-geoespacial-codip
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
```

## Validaciones

```bash
python -m pytest tests/ -v
python -m ruff check src/ tests/
python -m black --check src/ tests/
```

Los mismos gates se ejecutan en GitHub Actions para cambios hacia `master`.

## Stack actual

| Área | Herramientas |
|---|---|
| Datos | Pandas, NumPy, SciPy, PyArrow |
| Geoespacial | GeoPandas, Shapely, PyProj, Folium, Contextily |
| Machine Learning | Scikit-learn, HDBSCAN |
| Visualización | Matplotlib, Seaborn, Plotly |
| Notebooks | JupyterLab |
| Calidad | pytest, Ruff, Black, pre-commit |
| Documentación | Markdown / LaTeX |

## Flujo metodológico

```text
Perfilado y contrato de datos
    -> control de coordenadas y CRS
        -> limpieza y feature engineering
            -> EDA espacial
                -> clustering candidato
                    -> validación interna + estabilidad + coherencia espacial
                        -> análisis de sensibilidad
                            -> reporte/paper
```

La metodología detallada está en [`docs/methodology.md`](docs/methodology.md) y el
esquema canónico provisional en
[`docs/data_dictionary.md`](docs/data_dictionary.md).

## Gobernanza de datos

- No subir datos crudos, credenciales, tokens ni exportaciones de sistemas internos.
- `.env` está ignorado; `.env.example` solo contiene placeholders.
- Antes de incorporar una fuente real, documentar propietario, grano, fecha de corte,
  permisos de uso y correspondencia con el esquema canónico.

> **Importante:** este repositorio es actualmente público. No debe contener datos,
> credenciales, documentación confidencial ni propiedad intelectual interna que no
> esté autorizada para publicación.

## Licencia

El repositorio incluye una licencia MIT. Si el trabajo, código o metodología debe
quedar bajo titularidad o restricciones internas de CODIP, la licencia y la
visibilidad del repositorio deben revisarse antes de publicar contenido sustantivo.
