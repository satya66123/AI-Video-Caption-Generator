"""Internal Whisper transcript service."""

from pathlib import Path
from typing import Any


class TranscriptService:
    """Generate an internal timestamped transcript from a video."""

    def __init__(
        self,
        model_name: str = "base",
    ) -> None:
        """Initialize the Whisper transcript service."""
        self.model_name = model_name
        self._model: Any | None = None

    def _load_model(self) -> Any:
        """Load the Whisper model lazily."""
        if self._model is None:
            import whisper

            self._model = whisper.load_model(self.model_name)

        return self._model

    def transcribe(
        self,
        video_path: str | Path,
    ) -> dict[str, Any]:
        """
        Transcribe a video into timestamped segments.

        The returned transcript is intended for internal
        caption processing and is not persisted.
        """
        path = Path(video_path)

        if not path.is_file():
            raise FileNotFoundError(f"Video not found: {path}")

        model = self._load_model()

        result = model.transcribe(
            str(path),
            task="transcribe",
        )

        segments = []

        for segment in result.get("segments", []):
            segments.append(
                {
                    "start": float(segment["start"]),
                    "end": float(segment["end"]),
                    "text": str(segment["text"]).strip(),
                }
            )

        return {
            "text": str(result.get("text", "")).strip(),
            "segments": segments,
        }
