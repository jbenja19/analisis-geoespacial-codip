import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_governance_authorities_exist() -> None:
    required = [
        "AGENTS.md",
        "CONTRIBUTING.md",
        "docs/README.md",
        "docs/CURRENT_STATE.md",
        "docs/LINEAGE.md",
        "docs/DATA_POLICY.md",
        "docs/VALIDATION.md",
        "docs/archive/README.md",
        "docs/reports/README.md",
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    assert not missing, f"Faltan autoridades de gobernanza: {missing}"


def test_main_is_the_only_canonical_branch_in_repository_policy() -> None:
    current_state = (ROOT / "docs/CURRENT_STATE.md").read_text(encoding="utf-8")
    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert "Canonical branch: main" in current_state
    assert "`main` es la única rama canónica" in contributing
    assert "branches: [main]" in ci
    assert "branches: [master]" not in ci


def test_project_version_is_consistent() -> None:
    config = yaml.safe_load((ROOT / "config/config.yaml").read_text(encoding="utf-8"))
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")

    match = re.search(r'^version = "([^"]+)"$', pyproject, flags=re.MULTILINE)
    assert match, "No se encontró version en pyproject.toml"
    assert match.group(1) == config["project"]["version"]


def test_readme_does_not_claim_notebooks_are_empty() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    setup = (ROOT / "docs/setup.md").read_text(encoding="utf-8").lower()

    stale_phrases = [
        "notebooks/               # exploración; inicialmente vacío",
        "deliberadamente vacío de análisis",
    ]
    for phrase in stale_phrases:
        assert phrase not in readme
        assert phrase not in setup
