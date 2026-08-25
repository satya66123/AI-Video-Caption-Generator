"""Caption generation service."""

from core.caption_models import CaptionSegment
from providers.translation_provider import TranslationProvider


class CaptionGenerationService:
    """Generate translated captions from timestamped segments."""

    def __init__(
        self,
        translation_provider: TranslationProvider,
    ) -> None:
        """Initialize the caption generation service."""
        self.translation_provider = translation_provider

    def generate(
        self,
        segments: list[CaptionSegment],
        target_language: str,
    ) -> list[CaptionSegment]:
        """Generate translated captions."""
        if not target_language.strip():
            raise ValueError("Target language cannot be empty.")

        if not segments:
            raise ValueError("Caption segments cannot be empty.")

        translated_segments: list[CaptionSegment] = []

        for segment in segments:
            translated_text = self.translation_provider.translate(
                segment.text,
                target_language,
            )

            translated_segments.append(
                CaptionSegment(
                    start=segment.start,
                    end=segment.end,
                    text=translated_text,
                )
            )

        return translated_segments
