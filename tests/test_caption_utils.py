from pathlib import Path

import pytest

from utils.caption_utils import (
    build_caption_filename,
    build_captioned_video_filename,
)
from config.caption_config import SUPPORTED_CAPTION_LANGUAGES
from utils.caption_utils import (
    get_supported_caption_languages,
    validate_caption_language,
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


def test_supported_caption_languages() -> None:
    languages = get_supported_caption_languages()

    assert languages["en"] == "English"
    assert languages["te"] == "Telugu"
    assert languages["hi"] == "Hindi"


def test_supported_caption_languages_returns_copy() -> None:
    languages = get_supported_caption_languages()

    languages["xx"] = "Test"

    assert "xx" not in SUPPORTED_CAPTION_LANGUAGES


def test_valid_caption_language() -> None:
    assert validate_caption_language("en") is True
    assert validate_caption_language("te") is True


def test_caption_language_is_case_insensitive() -> None:
    assert validate_caption_language("EN") is True
    assert validate_caption_language("Te") is True


def test_invalid_caption_language() -> None:
    assert validate_caption_language("xyz") is False
