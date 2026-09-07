from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIRS = [
    "data/raw",
    "data/external",
    "data/interim",
    "data/processed",
    "notebooks",
    "schemas/source",
    "schemas/canonical",
    "src/data",
    "src/geospatial",
    "src/analysis",
    "src/visualization",
    "src/utils",
    "docs/decisions",
    "reports/figures",
    "reports/tables",
    "reports/exports",
]


def test_required_scaffold_directories_exist() -> None:
    missing = [path for path in REQUIRED_DIRS if not (ROOT / path).is_dir()]
    assert not missing, f"Faltan directorios del scaffold: {missing}"


def test_raw_directory_contains_only_placeholder() -> None:
    raw_files = [path.name for path in (ROOT / "data/raw").iterdir() if path.is_file()]
    assert raw_files == [".gitkeep"]


def test_config_does_not_preselect_analysis_method() -> None:
    with (ROOT / "config/config.yaml").open(encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)

    assert config["project"]["stage"] == "scaffold"
    assert config["analysis"]["methodology"] is None
    assert config["analysis"]["unit_of_analysis"] is None
    assert config["analysis"]["temporal_scope"] is None
    assert config["geospatial"]["source_crs"] is None
    assert config["geospatial"]["analysis_crs"] is None
    assert config["raw_data"]["immutable"] is True
    assert config["raw_data"]["overwrite_allowed"] is False
