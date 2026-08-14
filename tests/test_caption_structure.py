from pathlib import Path


def test_caption_architecture() -> None:
    """Verify the Caption Generator architecture exists."""
    project_root = Path(__file__).resolve().parents[1]

    expected_files = [
        "agents/caption_agent.py",
        "services/caption_service.py",
        "utils/caption_utils.py",
        "pages/caption_generator_agent.py",
        "config/caption_config.py",
        "core/caption_models.py",
    ]

    for file_path in expected_files:
        assert (project_root / file_path).is_file()


def test_caption_agent_import() -> None:
    """Verify the CaptionAgent can be imported."""
    from agents.caption_agent import CaptionAgent

    assert CaptionAgent is not None


def test_caption_service_import() -> None:
    """Verify the CaptionService can be imported."""
    from services.caption_service import CaptionService

    assert CaptionService is not None