"""Tests de validación para el contrato de la fuente raw proyectos_la_victoria_sep25.

Implementado utilizando exclusivamente la biblioteca estándar de Python y PyYAML
para asegurar que la validación en CI no dependa de bibliotecas analíticas pesadas.
"""

import csv
from pathlib import Path
from typing import Any

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/source/proyectos_la_victoria_sep25.yaml"
CSV_PATH = ROOT / "data/raw/proyectos_la_victoria_sep25.csv"


@pytest.fixture(scope="module")
def source_schema() -> dict[str, Any]:
    """Carga el contrato declarativo de la fuente raw."""
    assert SCHEMA_PATH.is_file(), f"No existe el schema en {SCHEMA_PATH}"
    with SCHEMA_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def parsed_csv_data(
    source_schema: dict[str, Any],
) -> tuple[list[str], list[list[str]]]:
    """Lee y analiza el CSV de datos raw usando el encoding declarado."""
    encoding = source_schema.get("encoding", "utf-8")
    assert CSV_PATH.is_file(), f"No existe el archivo de datos en {CSV_PATH}"

    with CSV_PATH.open("r", encoding=encoding) as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    return header, rows


def test_csv_opens_with_declared_encoding(source_schema: dict[str, Any]) -> None:
    """Valida decodificación del CSV con el encoding especificado."""
    encoding = source_schema.get("encoding")
    assert encoding, "El schema no especifica encoding."
    with CSV_PATH.open("r", encoding=encoding) as f:
        content = f.read()
    assert len(content) > 0, "El contenido del CSV está vacío."


def test_csv_header_matches_schema_columns(
    source_schema: dict[str, Any],
    parsed_csv_data: tuple[list[str], list[list[str]]],
) -> None:
    """Valida que nombres y orden de columnas coincidan con el schema."""
    header, _ = parsed_csv_data
    declared_columns = [col["name"] for col in source_schema["columns"]]
    assert header == declared_columns, (
        f"El header no coincide con schema. Observado: {header}, "
        f"Esperado: {declared_columns}"
    )


def test_record_count_matches_declared(
    source_schema: dict[str, Any],
    parsed_csv_data: tuple[list[str], list[list[str]]],
) -> None:
    """Valida que la cantidad de filas de datos coincida con record_count."""
    _, rows = parsed_csv_data
    expected_count = source_schema.get("record_count")
    assert len(rows) == expected_count, (
        f"Cantidad de registros ({len(rows)}) no coincide con la esperada "
        f"({expected_count})"
    )


def test_primary_key_exists_and_is_unique(
    source_schema: dict[str, Any],
    parsed_csv_data: tuple[list[str], list[list[str]]],
) -> None:
    """Valida que las columnas de primary key existan y sus valores sean únicos."""
    header, rows = parsed_csv_data
    pk_columns = source_schema.get("primary_key", [])
    assert pk_columns, "El schema no define primary_key."

    for col in pk_columns:
        assert col in header, f"Columna de primary key '{col}' no existe en el header."

    col_indices = [header.index(col) for col in pk_columns]
    observed_keys = []
    for r in rows:
        key_val = tuple(r[idx].strip() for idx in col_indices)
        observed_keys.append(key_val)

    unique_keys = set(observed_keys)
    duplicates_count = len(observed_keys) - len(unique_keys)
    assert len(unique_keys) == len(
        observed_keys
    ), f"Se encontraron {duplicates_count} duplicados en la primary key {pk_columns}"


def test_non_nullable_columns_have_no_empty_values(
    source_schema: dict[str, Any],
    parsed_csv_data: tuple[list[str], list[list[str]]],
) -> None:
    """Valida que columnas nullable=false no contengan valores vacíos."""
    header, rows = parsed_csv_data
    non_nullable_cols = [
        col["name"] for col in source_schema["columns"] if not col.get("nullable", True)
    ]

    for col_name in non_nullable_cols:
        col_idx = header.index(col_name)
        for row_idx, r in enumerate(rows, start=1):
            val = r[col_idx].strip()
            assert (
                val != ""
            ), f"Valor vacío en columna no anulable '{col_name}', fila {row_idx}"


def test_integer_columns_are_valid_integers(
    source_schema: dict[str, Any],
    parsed_csv_data: tuple[list[str], list[list[str]]],
) -> None:
    """Valida que columnas declaradas integer sean parseables como enteros."""
    header, rows = parsed_csv_data
    int_cols = [
        col["name"] for col in source_schema["columns"] if col.get("type") == "integer"
    ]

    for col_name in int_cols:
        col_idx = header.index(col_name)
        for row_idx, r in enumerate(rows, start=1):
            val = r[col_idx].strip()
            try:
                int(val)
            except ValueError:
                pytest.fail(
                    f"Columna '{col_name}' fila {row_idx} contiene valor no entero: "
                    f"'{val}'"
                )


def test_float_columns_are_valid_floats(
    source_schema: dict[str, Any],
    parsed_csv_data: tuple[list[str], list[list[str]]],
) -> None:
    """Valida que columnas declaradas float sean parseables como punto flotante."""
    header, rows = parsed_csv_data
    float_cols = [
        col["name"] for col in source_schema["columns"] if col.get("type") == "float"
    ]

    for col_name in float_cols:
        col_idx = header.index(col_name)
        for row_idx, r in enumerate(rows, start=1):
            val = r[col_idx].strip()
            try:
                float(val)
            except ValueError:
                pytest.fail(
                    f"Columna '{col_name}' fila {row_idx} contiene valor no flotante: "
                    f"'{val}'"
                )


def test_activo_column_domain_is_binary(
    parsed_csv_data: tuple[list[str], list[list[str]]],
) -> None:
    """Valida que el indicador 'activo' contenga únicamente valores en {0, 1}."""
    header, rows = parsed_csv_data
    assert "activo" in header, "La columna 'activo' no existe en el header."
    activo_idx = header.index("activo")

    allowed = {"0", "1"}
    for row_idx, r in enumerate(rows, start=1):
        val = r[activo_idx].strip()
        assert (
            val in allowed
        ), f"Fila {row_idx} tiene valor '{val}' en 'activo', fuera de {allowed}"


def test_geospatial_coordinates_within_wgs84_bounds(
    source_schema: dict[str, Any],
    parsed_csv_data: tuple[list[str], list[list[str]]],
) -> None:
    """Valida que longitud y latitud se ubiquen dentro de límites EPSG:4326."""
    header, rows = parsed_csv_data
    geo_config = source_schema.get("geospatial", {})
    lon_col = geo_config.get("longitude_column", "Longitud")
    lat_col = geo_config.get("latitude_column", "Latitud")

    assert lon_col in header, f"Columna de longitud '{lon_col}' no encontrada."
    assert lat_col in header, f"Columna de latitud '{lat_col}' no encontrada."

    lon_idx = header.index(lon_col)
    lat_idx = header.index(lat_col)

    for row_idx, r in enumerate(rows, start=1):
        lon = float(r[lon_idx].strip())
        lat = float(r[lat_idx].strip())

        assert (
            -180.0 <= lon <= 180.0
        ), f"Longitud fuera de rango WGS84 [-180, 180] en fila {row_idx}: {lon}"
        assert (
            -90.0 <= lat <= 90.0
        ), f"Latitud fuera de rango WGS84 [-90, 90] en fila {row_idx}: {lat}"
