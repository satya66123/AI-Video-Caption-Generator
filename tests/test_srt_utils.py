import pytest

from core.caption_models import CaptionSegment
from utils.srt_utils import (
    format_srt_timestamp,
    generate_srt,
)


def test_format_srt_timestamp() -> None:
    assert format_srt_timestamp(0) == "00:00:00,000"
    assert format_srt_timestamp(2.5) == "00:00:02,500"
    assert format_srt_timestamp(65.25) == "00:01:05,250"


def test_negative_timestamp_is_rejected() -> None:
    with pytest.raises(ValueError):
        format_srt_timestamp(-1)


def test_generate_srt() -> None:
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

    result = generate_srt(segments)

    expected = (
        "1\n"
        "00:00:00,000 --> 00:00:02,500\n"
        "Hello everyone\n\n"
        "2\n"
        "00:00:02,500 --> 00:00:05,000\n"
        "Welcome to the video\n"
    )

    assert result == expected


def test_empty_segments_are_rejected() -> None:
    with pytest.raises(ValueError):
        generate_srt([])


def test_invalid_segment_time_is_rejected() -> None:
    segments = [
        CaptionSegment(
            start=5.0,
            end=2.0,
            text="Invalid",
        )
    ]

    with pytest.raises(ValueError):
        generate_srt(segments)


def test_empty_caption_text_is_rejected() -> None:
    segments = [
        CaptionSegment(
            start=0.0,
            end=2.0,
            text="",
        )
    ]

    with pytest.raises(ValueError):
        generate_srt(segments)
