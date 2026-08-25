from pathlib import Path
from unittest.mock import MagicMock

import pytest

from agents.caption_agent import CaptionAgent


def test_caption_agent_detect_language(tmp_path: Path) -> None:
    video_path = tmp_path / "gm.mp4"
    video_path.write_bytes(b"fake video")

    mock_service = MagicMock()

    mock_service.detect.return_value = {
        "language": "en",
        "confidence": 0.95,
    }

    agent = CaptionAgent(
        language_detection_service=mock_service,
    )

    result = agent.detect_language(video_path)

    assert result["language"] == "en"
    assert result["confidence"] == 0.95
    mock_service.detect.assert_called_once_with(video_path)


def test_select_caption_language() -> None:
    agent = CaptionAgent(
        language_detection_service=MagicMock(),
    )

    assert agent.select_caption_language("en") == "en"
    assert agent.select_caption_language("te") == "te"


def test_select_caption_language_normalizes_code() -> None:
    agent = CaptionAgent(
        language_detection_service=MagicMock(),
    )

    assert agent.select_caption_language(" EN ") == "en"


def test_select_caption_language_rejects_invalid_language() -> None:
    agent = CaptionAgent(
        language_detection_service=MagicMock(),
    )

    with pytest.raises(ValueError):
        agent.select_caption_language("xyz")
