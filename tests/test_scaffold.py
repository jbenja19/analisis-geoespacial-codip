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


def test_raw_directory_contains_expected_sources() -> None:
    raw_files = {path.name for path in (ROOT / "data/raw").iterdir() if path.is_file()}
    expected = {"proyectos_la_victoria_sep25.csv", "proyectos_la_victoria_sep25.xlsx"}
    assert expected.issubset(
        raw_files
    ), f"Faltan fuentes raw esperadas: {expected - raw_files}"
    for filename in expected:
        file_path = ROOT / "data/raw" / filename
        assert file_path.stat().st_size > 0, f"El archivo raw {filename} está vacío."


def test_config_reflects_active_study_state() -> None:
    with (ROOT / "config/config.yaml").open(encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)

    assert config["project"]["stage"] == "exploratory_analysis"
    assert config["analysis"]["methodology"] is not None
    assert (
        config["analysis"]["unit_of_analysis"] == "proyectos_inmobiliarios_la_victoria"
    )
    assert config["geospatial"]["source_crs"] == "EPSG:4326"
    assert config["geospatial"]["analysis_crs"] == "EPSG:32718"
    assert config["raw_data"]["immutable"] is True
    assert config["raw_data"]["overwrite_allowed"] is False


def test_source_schema_matches_csv_header() -> None:
    schema_path = ROOT / "schemas/source/proyectos_la_victoria_sep25.yaml"
    assert (
        schema_path.is_file()
    ), "No se encontró el contrato de datos en schemas/source/"

    with schema_path.open(encoding="utf-8") as schema_file:
        schema = yaml.safe_load(schema_file)

    expected_cols = [col["name"] for col in schema["columns"]]
    csv_path = ROOT / "data/raw/proyectos_la_victoria_sep25.csv"
    with csv_path.open(encoding="latin1") as f:
        header = f.readline().strip().split(",")

    assert (
        header == expected_cols
    ), f"Discrepancia entre header CSV y schema: {header} vs {expected_cols}"
