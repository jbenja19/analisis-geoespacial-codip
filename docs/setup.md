# Guia de Instalacion - CODIP

## Requisitos del Sistema

- Python 3.10 o superior
- Git
- 8 GB RAM recomendados para datasets grandes
- (Opcional) GDAL para operaciones avanzadas con rasters

## Instalacion Paso a Paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/<tu-usuario>/analisis-geoespacial-codip.git
cd analisis-geoespacial-codip
```

### 2. Crear entorno virtual

```bash
# Con venv (incluido en Python)
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux / Mac
```

### 3. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
copy .env.example .env     # Windows
# cp .env.example .env    # Linux / Mac
```
Edita `.env` con tus claves de API y rutas locales.

### 5. Instalar pre-commit hooks (opcional pero recomendado)

```bash
pre-commit install
```

### 6. Iniciar JupyterLab

```bash
jupyter lab
```

## Verificacion de la Instalacion

```python
import geopandas as gpd
import sklearn
print("Instalacion exitosa!")
```
