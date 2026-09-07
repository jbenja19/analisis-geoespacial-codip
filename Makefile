.PHONY: install env clean lint test notebooks

## Instalar dependencias
install:
	pip install -r requirements.txt

## Crear entorno virtual
env:
	python -m venv .venv

## Limpiar archivos temporales
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +

## Ejecutar linter
lint:
	ruff check src/ tests/
	black --check src/ tests/

## Ejecutar tests
test:
	pytest tests/ -v

## Iniciar JupyterLab
notebooks:
	jupyter lab
