"""Tests for the video caption burn service."""

from pathlib import Path
from unittest.mock import patch

import pytest

from services.video_caption_burn_service import (
    VideoCaptionBurnService,
)


def test_build_output_path(tmp_path: Path) -> None:
    """Build the expected captioned-video output path."""
    service = VideoCaptionBurnService(tmp_path / "exports")

    video_path = tmp_path / "gm.mp4"

    result = service.build_output_path(
        video_path,
        "en",
    )

    assert result == (tmp_path / "exports" / "gm_en_captioned.mp4")


def test_missing_video_is_rejected(
    tmp_path: Path,
) -> None:
    """Reject a missing video."""
    service = VideoCaptionBurnService(tmp_path / "exports")

    video_path = tmp_path / "missing.mp4"
    caption_path = tmp_path / "gm_en.srt"

    caption_path.write_text(
        "caption",
        encoding="utf-8",
    )

    with pytest.raises(FileNotFoundError):
        service.burn(
            video_path,
            caption_path,
            "en",
        )


def test_missing_caption_is_rejected(
    tmp_path: Path,
) -> None:
    """Reject a missing caption file."""
    service = VideoCaptionBurnService(tmp_path / "exports")

    video_path = tmp_path / "gm.mp4"
    caption_path = tmp_path / "missing.srt"

    video_path.write_bytes(b"video")

    with pytest.raises(FileNotFoundError):
        service.burn(
            video_path,
            caption_path,
            "en",
        )


@patch("services.video_caption_burn_service.subprocess.run")
def test_burn_calls_ffmpeg(
    mock_run,
    tmp_path: Path,
) -> None:
    """Verify the FFmpeg command used for caption burning."""
    service = VideoCaptionBurnService(tmp_path / "exports")

    video_path = tmp_path / "gm.mp4"
    caption_path = tmp_path / "gm_en.srt"
    output_path = tmp_path / "exports" / "gm_en_captioned.mp4"

    video_path.write_bytes(b"video")

    caption_path.write_text(
        "caption",
        encoding="utf-8",
    )

    def create_output(*args, **kwargs):
        """Create a fake FFmpeg output."""
        output_path.write_bytes(b"captioned video")

    mock_run.side_effect = create_output

    result = service.burn(
        video_path,
        caption_path,
        "en",
    )

    assert result == output_path
    assert output_path.is_file()

    command = mock_run.call_args.args[0]

    assert command[0] == "ffmpeg"
    assert "-y" in command
    assert "-i" in command
    assert str(video_path) in command
    assert "-vf" in command

    # Find the FFmpeg video-filter argument.
    filter_index = command.index("-vf")
    subtitle_filter = command[filter_index + 1]

    # The service uses an absolute POSIX-style path
    # and escapes the Windows drive-letter colon.
    expected_path = caption_path.resolve().as_posix().replace(":", r"\:")

    expected_filter = f"subtitles=filename='{expected_path}'"

    assert subtitle_filter == expected_filter

    assert "-c:a" in command
    assert "copy" in command
    assert str(output_path) in command


@patch("services.video_caption_burn_service.subprocess.run")
def test_ffmpeg_failure_is_converted_to_runtime_error(
    mock_run,
    tmp_path: Path,
) -> None:
    """Convert an FFmpeg failure into RuntimeError."""
    service = VideoCaptionBurnService(tmp_path / "exports")

    video_path = tmp_path / "gm.mp4"
    caption_path = tmp_path / "gm_en.srt"

    video_path.write_bytes(b"video")

    caption_path.write_text(
        "caption",
        encoding="utf-8",
    )

    mock_run.side_effect = __import__("subprocess").CalledProcessError(
        returncode=1,
        cmd=["ffmpeg"],
        stderr="FFmpeg test error",
    )

    with pytest.raises(
        RuntimeError,
        match="FFmpeg test error",
    ):
        service.burn(
            video_path,
            caption_path,
            "en",
        )
