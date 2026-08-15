from pathlib import Path
from unittest.mock import MagicMock

from agents.caption_agent import CaptionAgent


def test_prepare_caption_segments() -> None:
    transcript_service = MagicMock()

    transcript_service.transcribe.return_value = {
        "text": "Hello everyone",
        "segments": [
            {
                "start": 0.0,
                "end": 2.5,
                "text": "Hello everyone",
            },
            {
                "start": 2.5,
                "end": 5.0,
                "text": "Welcome",
            },
        ],
    }

    language_service = MagicMock()

    language_service.detect.return_value = {
        "language": "en",
        "language_name": "English",
    }

    agent = CaptionAgent(
        language_detection_service=language_service,
        transcript_service=transcript_service,
    )

    result = agent.prepare_caption_segments(
        Path("video.mp4"),
        "en",
    )

    assert result["video_path"] == "video.mp4"
    assert result["caption_language"] == "en"

    assert result["detected_language"] == {
        "language": "en",
        "language_name": "English",
    }

    assert len(result["segments"]) == 2
    assert result["segments"][0].text == "Hello everyone"
    assert result["segments"][1].text == "Welcome"

    transcript_service.transcribe.assert_called_once_with(
        Path("video.mp4")
    )

    language_service.detect.assert_called_once_with(
        Path("video.mp4")
    )