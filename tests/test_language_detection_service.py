from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from services.language_detection_service import (
    LanguageDetectionService,
)


def test_video_not_found() -> None:
    with patch("services.language_detection_service.whisper.load_model"):
        service = LanguageDetectionService()

        with pytest.raises(FileNotFoundError):
            service.detect("missing_video.mp4")


def test_detect_language(tmp_path: Path) -> None:
    video_path = tmp_path / "test_video.mp4"
    video_path.write_bytes(b"fake video")

    mock_model = MagicMock()
    mock_model.device = "cpu"
    mock_model.dims.n_mels = 80

    mock_probabilities = {
        "en": 0.92,
        "te": 0.06,
        "hi": 0.02,
    }

    with patch(
        "services.language_detection_service.whisper.load_model",
        return_value=mock_model,
    ), patch(
        "services.language_detection_service.whisper.load_audio",
        return_value=MagicMock(),
    ), patch(
        "services.language_detection_service.whisper.pad_or_trim",
        return_value=MagicMock(),
    ), patch(
        "services.language_detection_service.whisper.log_mel_spectrogram",
        return_value=MagicMock(),
    ):
        mock_model.detect_language.return_value = (
            MagicMock(),
            mock_probabilities,
        )

        service = LanguageDetectionService()
        result = service.detect(video_path)

    assert result["language"] == "en"
    assert result["confidence"] == pytest.approx(0.92)
