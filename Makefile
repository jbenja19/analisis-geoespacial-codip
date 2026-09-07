.PHONY: install env clean lint test notebooks

## Instalar dependencias
install:
	python -m pip install -r requirements.txt

## Crear entorno virtual
env:
	python -m venv .venv

## Limpiar caches de Python/Jupyter de forma portable
clean:
	python -c "from pathlib import Path; import shutil; [p.unlink() for p in Path('.').rglob('*.pyc') if p.is_file()]; [shutil.rmtree(p, ignore_errors=True) for p in list(Path('.').rglob('__pycache__')) + list(Path('.').rglob('.ipynb_checkpoints'))]"

## Ejecutar linters
lint:
	python -m ruff check src/ tests/
	python -m black --check src/ tests/

## Ejecutar tests
test:
	python -m pytest tests/ -v

## Iniciar JupyterLab
notebooks:
	python -m jupyter lab
