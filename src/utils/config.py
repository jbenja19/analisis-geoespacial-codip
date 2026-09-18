"""Gestión de configuración del proyecto mediante YAML."""

from pathlib import Path
from typing import Any

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_config(config_path: str | Path | None = None) -> dict[str, Any]:
    """Carga la configuración del proyecto desde un archivo YAML."""
    if config_path is None:
        config_path = PROJECT_ROOT / "config" / "config.yaml"
    with open(config_path, encoding="utf-8") as f:
        return yaml.safe_load(f)
