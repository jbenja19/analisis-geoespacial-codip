.PHONY: install install-dev env clean lint test validate notebooks

## Instalar dependencias de trabajo
install:
	python -m pip install -r requirements.txt

## Instalar herramientas de calidad/desarrollo
install-dev:
	python -m pip install -r requirements-dev.txt

## Crear entorno virtual
env:
	python -m venv .venv

## Limpiar caches de Python/Jupyter
clean:
	python -c "from pathlib import Path; import shutil; [p.unlink() for p in Path('.').rglob('*.pyc') if p.is_file()]; [shutil.rmtree(p, ignore_errors=True) for p in list(Path('.').rglob('__pycache__')) + list(Path('.').rglob('.ipynb_checkpoints'))]"

## Validar estilo
lint:
	python -m ruff check src/ tests/
	python -m black --check src/ tests/

## Ejecutar tests de estructura, contratos y gobernanza
test:
	python -m pytest tests/ -v

## Gate local base equivalente al CI actual
validate: lint test

## Abrir JupyterLab
notebooks:
	python -m jupyter lab
