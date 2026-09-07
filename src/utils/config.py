"""
config.py
---------
Gestion de configuracion del proyecto mediante YAML y variables de entorno.
"""
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_config(config_path: str = None) -> dict:
    """Carga la configuracion desde un archivo YAML."""
    if config_path is None:
        config_path = PROJECT_ROOT / "config" / "config.yaml"
    with open(config_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_env(key: str, default=None):
    """Obtiene una variable de entorno con valor por defecto."""
    return os.getenv(key, default)
