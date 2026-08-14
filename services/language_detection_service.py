"""Video spoken-language detection service."""

from pathlib import Path

import whisper

from typing import Mapping


class LanguageDetectionService:
    """Detect the spoken language in a video."""

    def __init__(self, model_name: str = "base") -> None:
        """Initialize the Whisper model."""
        self.model = whisper.load_model(model_name)

    def detect(self, video_path: str | Path) -> dict[str, object]:
        """Detect the spoken language in a video."""
        path = Path(video_path)

        if not path.is_file():
            raise FileNotFoundError(f"Video not found: {path}")

        audio = whisper.load_audio(str(path))
        audio = whisper.pad_or_trim(audio)

        mel = whisper.log_mel_spectrogram(
            audio,
            n_mels=self.model.dims.n_mels,
        ).to(self.model.device)

        _, raw_probabilities = self.model.detect_language(mel)

        probabilities: Mapping[str, float] = raw_probabilities

        detected_language = max(
            probabilities,
            key=probabilities.get,
        )

        confidence = float(probabilities[detected_language])

        return {
            "language": detected_language,
            "confidence": confidence,
        }