from pathlib import Path


def test_caption_architecture() -> None:
    """Verify the Caption Generator architecture exists."""
    project_root = Path(__file__).resolve().parents[1]

    py_ = [
        "agents/caption_agent.py",
        "services/caption_service.py",
        "utils/caption_utils.py",
        "pages/caption_generator_agent.py",
        "config/caption_config.py",
        "core/caption_models.py",
        "services/caption_generation_service.py",
    ]
    expected_files = py_

    for file_path in expected_files:
        assert (project_root / file_path).is_file()


def test_translation_provider_import() -> None:
    """Verify the translation provider can be imported."""
    from providers.translation_provider import TranslationProvider

    assert TranslationProvider is not None


def test_video_caption_burn_service_import() -> None:
    """Verify the video caption burn service can be imported."""
    from services.video_caption_burn_service import (
        VideoCaptionBurnService,
    )

    assert VideoCaptionBurnService is not None


def test_caption_file_service_import() -> None:
    """Verify the caption file service can be imported."""
    from services.caption_file_service import CaptionFileService

    assert CaptionFileService is not None


def test_ollama_translation_provider_import() -> None:
    """Verify the Ollama provider can be imported."""
    from providers.ollama_translation_provider import (
        OllamaTranslationProvider,
    )

    assert OllamaTranslationProvider is not None


def test_caption_generation_service_import() -> None:
    """Verify the CaptionGenerationService can be imported."""
    from services.caption_generation_service import (
        CaptionGenerationService,
    )

    assert CaptionGenerationService is not None


def test_caption_agent_import() -> None:
    """Verify the CaptionAgent can be imported."""
    from agents.caption_agent import CaptionAgent

    assert CaptionAgent is not None


def test_caption_service_import() -> None:
    """Verify the CaptionService can be imported."""
    from services.caption_service import CaptionService

    assert CaptionService is not None
