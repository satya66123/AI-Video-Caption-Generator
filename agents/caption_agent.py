"""Caption agent."""

from pathlib import Path

from services.language_detection_service import LanguageDetectionService

from config.caption_config import DEFAULT_CAPTION_LANGUAGE
from utils.caption_utils import validate_caption_language


class CaptionAgent:
    """Main agent responsible for the caption-generation workflow."""

    def select_caption_language(
            self,
            language_code: str = DEFAULT_CAPTION_LANGUAGE,
    ) -> str:
        """Validate and return the selected caption language."""
        normalized_language = language_code.strip().lower()

        if not validate_caption_language(normalized_language):
            raise ValueError(
                f"Unsupported caption language: {language_code}"
            )

        return normalized_language

    def __init__(
        self,
        language_detection_service: LanguageDetectionService | None = None,
    ) -> None:
        """Initialize the caption agent."""
        self.language_detection_service = (
            language_detection_service
            or LanguageDetectionService()
        )

    def detect_language(
        self,
        video_path: str | Path,
    ) -> dict[str, object]:
        """Detect the spoken language of a video."""
        return self.language_detection_service.detect(video_path)

