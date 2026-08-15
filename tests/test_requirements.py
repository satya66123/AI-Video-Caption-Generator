"""Tests for project requirements.txt."""

from pathlib import Path


REQUIREMENTS_FILE = (
    Path(__file__).resolve().parent.parent / "requirements.txt"
)


def test_requirements_file_exists() -> None:
    """Verify requirements.txt exists."""
    assert REQUIREMENTS_FILE.exists()


def test_requirements_file_is_not_empty() -> None:
    """Verify requirements.txt contains content."""
    content = REQUIREMENTS_FILE.read_text(
        encoding="utf-8"
    ).strip()

    assert content


def test_requirements_contains_streamlit() -> None:
    """Verify Streamlit is included."""
    content = REQUIREMENTS_FILE.read_text(
        encoding="utf-8"
    )

    assert "streamlit" in content.lower()


def test_requirements_contains_whisper() -> None:
    """Verify Whisper is included."""
    content = REQUIREMENTS_FILE.read_text(
        encoding="utf-8"
    )

    assert "openai-whisper" in content.lower()


def test_requirements_contains_torch() -> None:
    """Verify PyTorch is included."""
    content = REQUIREMENTS_FILE.read_text(
        encoding="utf-8"
    )

    assert "torch" in content.lower()


def test_requirements_contains_langdetect() -> None:
    """Verify language detection dependency is included."""
    content = REQUIREMENTS_FILE.read_text(
        encoding="utf-8"
    )

    assert "langdetect" in content.lower()


def test_requirements_contains_pytest() -> None:
    """Verify PyTest is included."""
    content = REQUIREMENTS_FILE.read_text(
        encoding="utf-8"
    )

    assert "pytest" in content.lower()


def test_requirements_contains_pinned_versions() -> None:
    """Verify the main dependencies use pinned versions."""
    content = REQUIREMENTS_FILE.read_text(
        encoding="utf-8"
    )

    required_packages = (
        "streamlit==",
        "openai-whisper==",
        "torch==",
        "langdetect==",
        "pytest==",
    )

    for package in required_packages:
        assert package in content