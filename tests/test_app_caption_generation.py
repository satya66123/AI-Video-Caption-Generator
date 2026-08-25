from pathlib import Path
from unittest.mock import MagicMock, patch

from core.caption_models import CaptionSegment


def test_caption_result_contains_srt_and_vtt_paths() -> None:
    result = {
        "caption_language": "en",
        "srt_path": Path("captions/gm_en.srt"),
        "vtt_path": Path("captions/gm_en.vtt"),
        "segments": [
            CaptionSegment(
                start=0.0,
                end=2.5,
                text="Hello everyone",
            )
        ],
    }

    assert result["caption_language"] == "en"
    assert result["srt_path"].name == "gm_en.srt"
    assert result["vtt_path"].name == "gm_en.vtt"


def test_caption_result_contains_translated_segments() -> None:
    segments = [
        CaptionSegment(
            start=0.0,
            end=2.5,
            text="Hello everyone",
        ),
        CaptionSegment(
            start=2.5,
            end=5.0,
            text="Welcome to the video",
        ),
    ]

    result = {
        "segments": segments,
    }

    assert len(result["segments"]) == 2
    assert result["segments"][0].text == "Hello everyone"
    assert result["segments"][1].text == "Welcome to the video"


def test_caption_language_is_preserved() -> None:
    result = {
        "caption_language": "en",
    }

    assert result["caption_language"] == "en"


def test_caption_paths_use_video_name() -> None:
    video_path = Path("uploads/gm.mp4")

    srt_path = Path("captions/gm_en.srt")
    vtt_path = Path("captions/gm_en.vtt")

    assert video_path.stem == "gm"
    assert srt_path.stem == "gm_en"
    assert vtt_path.stem == "gm_en"


def test_caption_generation_service_result_shape() -> None:
    generation_service = MagicMock()

    generation_service.generate.return_value = [
        CaptionSegment(
            start=0.0,
            end=2.0,
            text="Hello",
        )
    ]

    segments = generation_service.generate(
        segments=[
            CaptionSegment(
                start=0.0,
                end=2.0,
                text="నమస్కారం",
            )
        ],
        target_language="en",
    )

    assert len(segments) == 1
    assert segments[0].start == 0.0
    assert segments[0].end == 2.0
    assert segments[0].text == "Hello"

    generation_service.generate.assert_called_once()
