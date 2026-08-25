from pathlib import Path
from unittest.mock import MagicMock

import pytest

from services.transcript_service import TranscriptService


def test_missing_video_is_rejected() -> None:
    service = TranscriptService()

    with pytest.raises(FileNotFoundError):
        service.transcribe("missing_video.mp4")


def test_transcribe_returns_timestamped_segments(
    tmp_path: Path,
) -> None:
    video_path = tmp_path / "video.mp4"
    video_path.write_bytes(b"fake video")

    service = TranscriptService()

    mock_model = MagicMock()

    mock_model.transcribe.return_value = {
        "text": "Hello everyone",
        "segments": [
            {
                "start": 0.0,
                "end": 2.5,
                "text": " Hello everyone ",
            },
            {
                "start": 2.5,
                "end": 5.0,
                "text": " Welcome ",
            },
        ],
    }

    service._model = mock_model

    result = service.transcribe(video_path)

    assert result["text"] == "Hello everyone"
    assert len(result["segments"]) == 2

    assert result["segments"][0] == {
        "start": 0.0,
        "end": 2.5,
        "text": "Hello everyone",
    }

    assert result["segments"][1] == {
        "start": 2.5,
        "end": 5.0,
        "text": "Welcome",
    }

    mock_model.transcribe.assert_called_once_with(
        str(video_path),
        task="transcribe",
    )


def test_empty_transcript_is_supported(
    tmp_path: Path,
) -> None:
    video_path = tmp_path / "silent.mp4"
    video_path.write_bytes(b"fake video")

    service = TranscriptService()

    mock_model = MagicMock()

    mock_model.transcribe.return_value = {
        "text": "",
        "segments": [],
    }

    service._model = mock_model

    result = service.transcribe(video_path)

    assert result["text"] == ""
    assert result["segments"] == []
