from pathlib import Path

import pytest

from utils.caption_utils import (
    build_caption_filename,
    build_captioned_video_filename,
)


def test_build_srt_filename() -> None:
    result = build_caption_filename(
        "my_video.mp4",
        "en",
        "srt",
    )

    assert result == "my_video_en.srt"


def test_build_vtt_filename() -> None:
    result = build_caption_filename(
        "my_video.mp4",
        "en",
        "vtt",
    )

    assert result == "my_video_en.vtt"


def test_build_captioned_video_filename() -> None:
    result = build_captioned_video_filename(
        "my_video.mp4",
        "en",
    )

    assert result == "my_video_en_captioned.mp4"


def test_original_video_extension_is_removed() -> None:
    result = build_caption_filename(
        Path("lecture_video.mkv"),
        "te",
        "srt",
    )

    assert result == "lecture_video_te.srt"


def test_language_code_is_normalized() -> None:
    result = build_caption_filename(
        "video.mp4",
        " EN ",
        "SRT",
    )

    assert result == "video_en.srt"


def test_invalid_caption_extension() -> None:
    with pytest.raises(ValueError):
        build_caption_filename(
            "video.mp4",
            "en",
            "txt",
        )


def test_empty_language_code() -> None:
    with pytest.raises(ValueError):
        build_caption_filename(
            "video.mp4",
            "",
            "srt",
        )


def test_empty_video_filename() -> None:
    with pytest.raises(ValueError):
        build_caption_filename(
            ".mp4",
            "en",
            "srt",
        )