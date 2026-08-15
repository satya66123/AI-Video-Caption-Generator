from pathlib import Path

import pytest

from services.caption_file_service import CaptionFileService


def test_save_srt(tmp_path: Path) -> None:
    service = CaptionFileService(tmp_path)

    result = service.save_srt(
        "gm.mp4",
        "en",
        "1\n00:00:00,000 --> 00:00:02,000\nHello\n",
    )

    assert result == tmp_path / "gm_en.srt"
    assert result.is_file()

    assert result.read_text(encoding="utf-8") == (
        "1\n00:00:00,000 --> 00:00:02,000\nHello\n"
    )


def test_save_vtt(tmp_path: Path) -> None:
    service = CaptionFileService(tmp_path)

    result = service.save_vtt(
        "gm.mp4",
        "en",
        "WEBVTT\n\n"
        "1\n"
        "00:00:00.000 --> 00:00:02.000\n"
        "Hello\n",
    )

    assert result == tmp_path / "gm_en.vtt"
    assert result.is_file()


def test_original_video_extension_is_not_used(
    tmp_path: Path,
) -> None:
    service = CaptionFileService(tmp_path)

    result = service.save_srt(
        "my_video.mkv",
        "te",
        "caption",
    )

    assert result.name == "my_video_te.srt"


def test_empty_content_is_rejected(tmp_path: Path) -> None:
    service = CaptionFileService(tmp_path)

    with pytest.raises(ValueError):
        service.save_srt(
            "gm.mp4",
            "en",
            "",
        )


def test_nested_output_directory_is_created(
    tmp_path: Path,
) -> None:
    output_dir = tmp_path / "generated" / "captions"

    service = CaptionFileService(output_dir)

    result = service.save_srt(
        "gm.mp4",
        "en",
        "caption",
    )

    assert output_dir.is_dir()
    assert result.is_file()