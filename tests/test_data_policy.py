"""Test de cumplimiento de la política de datos versionados (docs/DATA_POLICY.md).

Este test audita los archivos reales rastreados por Git bajo el directorio data/
para evitar la inclusión silenciosa o accidental de nuevos datasets sin previa
clasificación y aprobación explícita de publicación.

IMPORTANTE: La lista blanca (allowlist) aquí definida constituye un control técnico
de integridad en Git y NO debe interpretarse como una prueba de autorización de
publicación o renuncia a derechos de propiedad intelectual.
"""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Excepciones históricas acotadas y explícitamente autorizadas bajo data/
ALLOWED_DATA_FILES = {
    "data/raw/proyectos_la_victoria_sep25.csv",
    "data/raw/proyectos_la_victoria_sep25.xlsx",
    "data/processed/informacion_oferta_proyectos_activos_la_victoria_5_clusters.xlsx",
    "data/processed/informacion_oferta_proyectos_la_victoria_segmentacion.xlsx",
}

# Extensiones de formatos de datos que nunca deben agregarse sin actualizar la política
DATA_EXTENSIONS = {
    ".csv",
    ".xlsx",
    ".xls",
    ".parquet",
    ".feather",
    ".geojson",
    ".shp",
    ".shx",
    ".dbf",
    ".prj",
    ".gpkg",
    ".json",
}


def test_no_unauthorized_data_files_are_tracked_in_git() -> None:
    """Verifica que no existan datos versionados bajo data/ fuera de allowlist."""
    try:
        result = subprocess.run(
            ["git", "ls-files", "data"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        tracked_files = [
            line.strip().replace("\\", "/")
            for line in result.stdout.splitlines()
            if line.strip()
        ]
    except Exception:
        # Fallback para entornos donde git CLI no esté disponible
        tracked_files = [
            p.relative_to(ROOT).as_posix()
            for p in (ROOT / "data").rglob("*")
            if p.is_file()
        ]

    # Filtrar metadatos estructurales permitidos (.gitkeep, README.md)
    real_data_files = {
        f
        for f in tracked_files
        if not f.endswith(".gitkeep") and not Path(f).name.lower().startswith("readme")
    }

    # Comprobar que no hay archivos fuera de la allowlist
    unauthorized = real_data_files - ALLOWED_DATA_FILES
    assert not unauthorized, (
        f"Archivos de datos no autorizados por la política: {unauthorized}. "
        "Consulte docs/DATA_POLICY.md antes de versionar nuevos datos."
    )

    # Comprobar que no faltan archivos esenciales de la allowlist
    missing = ALLOWED_DATA_FILES - real_data_files
    assert not missing, f"Faltan archivos esperados de la allowlist de datos: {missing}"
