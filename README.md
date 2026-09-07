# Analisis Geoespacial - CODIP

> Segmentacion de Proyectos Inmobiliarios mediante Analisis Geoespacial y Ciencia de Datos

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-En%20Desarrollo-orange)]()
[![DVC](https://img.shields.io/badge/Data%20Version%20Control-DVC-945DD6?logo=dvc)](https://dvc.org/)

---

## Descripcion del Proyecto

Este repositorio contiene el trabajo de investigacion y desarrollo del proyecto **CODIP** (Clasificacion y Organizacion de Datos de Proyectos Inmobiliarios), cuyo objetivo es disenar y estandarizar una metodologia de **analisis geoespacial para la segmentacion de proyectos inmobiliarios** en funcion de sus caracteristicas fisicas, socioeconomicas y territoriales.

El producto final es un **paper academico/tecnico** que documente y valide esta metodologia como estandar reproducible para el sector inmobiliario.

### Objetivos

- Recopilar y procesar datos de proyectos inmobiliarios con atributos geoespaciales.
- Identificar variables relevantes (localizacion, tipologia, area, densidad, entorno, etc.).
- Aplicar tecnicas de clustering y segmentacion no supervisada para clasificar tipologias.
- Validar los resultados con metricas estadisticas y analisis geoespacial.
- Producir un paper que estandarice esta metodologia como marco de referencia reproducible.

---

## Nota sobre la Estructura del Repositorio

> **Esta estructura es dinamica, no estatica.**

El arbol de directorios presentado aqui representa el **punto de partida** del proyecto, basado en buenas practicas de ciencia de datos y analisis geoespacial. Sin embargo, **esta sujeto a evolucionar** conforme avance el desarrollo:

- Se pueden agregar nuevos modulos, carpetas o sub-proyectos segun las necesidades que emerjan.
- Algunas carpetas pueden renombrarse, reorganizarse o eliminarse si el flujo de trabajo lo requiere.
- Cualquier cambio estructural significativo se registrara en [`CHANGELOG.md`](CHANGELOG.md).

**Esta flexibilidad es intencional**: los proyectos de ciencia de datos tienen naturaleza exploratoria y sus necesidades evolucionan con los datos y los hallazgos.

---

## Estructura del Repositorio

```
analisis-geoespacial-codip/
|
+-- data/                        # Datos del proyecto (NO se versiona en Git)
|   +-- raw/                     # Datos originales sin modificar (inmutables)
|   +-- interim/                 # Datos en transformacion intermedia
|   +-- processed/               # Datos listos para modelado
|   +-- external/                # Datos externos (shapefiles, APIs, etc.)
|
+-- notebooks/                   # Jupyter Notebooks de exploracion y analisis
|   +-- 01_exploratory/          # EDA: exploracion y descripcion inicial
|   +-- 02_preprocessing/        # Limpieza, transformacion y feature engineering
|   +-- 03_geospatial/           # Analisis geoespacial y visualizaciones de mapas
|   +-- 04_modeling/             # Clustering, segmentacion y evaluacion de modelos
|   +-- 05_reporting/            # Resultados finales y graficos para el paper
|
+-- src/                         # Codigo fuente modular y reutilizable
|   +-- data/
|   |   +-- ingestion.py         # Carga de datos desde fuentes
|   |   +-- cleaning.py          # Limpieza y validacion de datos
|   |   +-- feature_engineering.py
|   +-- geospatial/
|   |   +-- spatial_ops.py       # Operaciones espaciales (joins, buffers, etc.)
|   |   +-- geocoding.py         # Geocodificacion y manejo de coordenadas
|   |   +-- maps.py              # Generacion de visualizaciones cartograficas
|   +-- models/
|   |   +-- clustering.py        # Algoritmos: KMeans, DBSCAN, HDBSCAN
|   |   +-- evaluation.py        # Metricas: silhouette, Davies-Bouldin
|   |   +-- preprocessing.py     # Escalado, PCA, reduccion de dimensionalidad
|   +-- visualization/
|   |   +-- plots.py             # Graficos estadisticos
|   |   +-- geo_plots.py         # Mapas y visualizaciones geoespaciales
|   +-- utils/
|       +-- config.py            # Gestion de configuracion
|       +-- io_utils.py          # Funciones de lectura/escritura
|
+-- paper/                       # Documento final: paper academico/tecnico
|   +-- draft/                   # Borradores del paper
|   +-- figures/                 # Figuras y mapas exportados para el paper
|   +-- references/              # Referencias bibliograficas (.bib)
|   +-- final/                   # Version final del paper (PDF, docx)
|
+-- reports/                     # Reportes intermedios de analisis
|   +-- figures/
|   +-- summaries/
|
+-- tests/                       # Pruebas unitarias del codigo fuente
+-- docs/                        # Documentacion tecnica
|   +-- methodology.md           # Descripcion de la metodologia
|   +-- data_dictionary.md       # Diccionario de variables y datasets
|   +-- setup.md                 # Guia de instalacion detallada
|   +-- decisions/               # Registro de decisiones tecnicas (ADR)
|
+-- config/                      # Archivos de configuracion
|   +-- config.yaml
|   +-- logging.yaml
|
+-- .env.example
+-- .gitignore
+-- .pre-commit-config.yaml
+-- CHANGELOG.md
+-- LICENSE
+-- Makefile
+-- pyproject.toml
+-- requirements.txt
+-- README.md
```

---

## Inicio Rapido

### Pre-requisitos

- Python 3.10+
- Git

### Instalacion

```bash
# 1. Clonar el repositorio
git clone https://github.com/<tu-usuario>/analisis-geoespacial-codip.git
cd analisis-geoespacial-codip

# 2. Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env

# 5. (Opcional) Instalar hooks de pre-commit
pre-commit install
```

---

## Stack Tecnologico

| Categoria              | Herramientas                                      |
|------------------------|---------------------------------------------------|
| Lenguaje               | Python 3.10+                                      |
| Geoespacial            | GeoPandas, Shapely, Folium, PyProj, GDAL          |
| Analisis de datos      | Pandas, NumPy, SciPy                              |
| Machine Learning       | Scikit-learn, HDBSCAN                             |
| Visualizacion          | Matplotlib, Seaborn, Plotly, Kepler.gl            |
| Notebooks              | JupyterLab                                        |
| Versionado de datos    | DVC                                               |
| Calidad de codigo      | Ruff, Black, pre-commit                           |
| Documentacion          | Markdown / LaTeX (paper)                          |

---

## Metodologia (Resumen)

```
Recoleccion de Datos
    --> Preprocesamiento y Limpieza
        --> Feature Engineering Geoespacial
            --> Analisis Exploratorio (EDA)
                --> Clustering / Segmentacion
                    --> Validacion y Evaluacion
                        --> Visualizacion Cartografica
                            --> Redaccion del Paper
```

---

## Equipo

| Nombre         | Rol                          |
|----------------|------------------------------|
| CODIP Team     | Investigacion y Desarrollo   |

---

## Licencia

Este proyecto esta bajo la licencia [MIT](LICENSE).

---

## Contacto

Para consultas, abrir un [Issue](https://github.com/<tu-usuario>/analisis-geoespacial-codip/issues) en este repositorio.
