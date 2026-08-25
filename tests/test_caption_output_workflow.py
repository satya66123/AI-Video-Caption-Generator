from pathlib import Path
from unittest.mock import MagicMock

from agents.caption_agent import CaptionAgent
from core.caption_models import CaptionSegment


def test_generate_caption_files() -> None:
    generation_service = MagicMock()

    generation_service.generate.return_value = [
        CaptionSegment(
            start=0.0,
            end=2.5,
            text="Hello everyone",
        )
    ]

    file_service = MagicMock()

    file_service.save_srt.return_value = Path("captions/gm_en.srt")

    file_service.save_vtt.return_value = Path("captions/gm_en.vtt")

    agent = CaptionAgent(
        language_detection_service=MagicMock(),
        transcript_service=MagicMock(),
        caption_generation_service=generation_service,
        caption_file_service=file_service,
    )

    result = agent.generate_caption_files(
        "gm.mp4",
        "en",
    )

    assert result["caption_language"] == "en"
    assert result["srt_path"] == Path("captions/gm_en.srt")
    assert result["vtt_path"] == Path("captions/gm_en.vtt")

    file_service.save_srt.assert_called_once()
    file_service.save_vtt.assert_called_once()


def test_generate_captioned_video() -> None:
    generation_service = MagicMock()

    generation_service.generate.return_value = [
        CaptionSegment(
            start=0.0,
            end=2.5,
            text="Hello everyone",
        )
    ]

    file_service = MagicMock()

    file_service.save_srt.return_value = Path("captions/gm_en.srt")

    file_service.save_vtt.return_value = Path("captions/gm_en.vtt")

    burn_service = MagicMock()

    burn_service.burn.return_value = Path("outputs/gm_en_captioned.mp4")

    agent = CaptionAgent(
        language_detection_service=MagicMock(),
        transcript_service=MagicMock(),
        caption_generation_service=generation_service,
        caption_file_service=file_service,
        video_caption_burn_service=burn_service,
    )

    result = agent.generate_captioned_video(
        "gm.mp4",
        "en",
    )

    assert result["output_video"] == Path("outputs/gm_en_captioned.mp4")

    burn_service.burn.assert_called_once()
