from pathlib import Path


def test_project_structure() -> None:
    """Verify the Phase 0 project structure exists."""
    project_root = Path(__file__).resolve().parents[1]

    expected_directories = [
        "agents",
        "services",
        "utils",
        "pages",
        "config",
        "core",
        "tests",
        "data/captions",
        "captions",
        "outputs",
        "uploads",
    ]

    for directory in expected_directories:
        assert (project_root / directory).is_dir()


def test_app_exists() -> None:
    """Verify the Streamlit entry point exists."""
    project_root = Path(__file__).resolve().parents[1]

    assert (project_root / "app.py").is_file()


def test_requirements_exists() -> None:
    """Verify the requirements file exists."""
    project_root = Path(__file__).resolve().parents[1]

    assert (project_root / "requirements.txt").is_file()
