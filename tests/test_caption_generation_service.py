from unittest.mock import MagicMock

import pytest

from core.caption_models import CaptionSegment
from services.caption_generation_service import (
    CaptionGenerationService,
)


def test_generate_translates_and_preserves_timestamps() -> None:
    provider = MagicMock()

    provider.translate.side_effect = [
        "Hello everyone",
        "Welcome to the video",
    ]

    service = CaptionGenerationService(provider)

    segments = [
        CaptionSegment(
            start=0.0,
            end=2.5,
            text="నమస్కారం అందరికీ",
        ),
        CaptionSegment(
            start=2.5,
            end=5.0,
            text="వీడియోకు స్వాగతం",
        ),
    ]

    result = service.generate(
        segments,
        "English",
    )

    assert len(result) == 2

    assert result[0].start == 0.0
    assert result[0].end == 2.5
    assert result[0].text == "Hello everyone"

    assert result[1].start == 2.5
    assert result[1].end == 5.0
    assert result[1].text == "Welcome to the video"

    assert provider.translate.call_count == 2
