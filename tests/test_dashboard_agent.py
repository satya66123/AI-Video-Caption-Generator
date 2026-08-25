"""Tests for the dashboard agent."""

from pathlib import Path

from agents.dashboard_agent import DashboardAgent


def test_dashboard_statistics(tmp_path: Path) -> None:
    """Return correct dashboard statistics."""
    uploads = tmp_path / "uploads"
    captions = tmp_path / "captions"
    outputs = tmp_path / "outputs"

    uploads.mkdir()
    captions.mkdir()
    outputs.mkdir()

    (uploads / "video.mp4").write_bytes(b"video")
    (uploads / "ignored.txt").write_text(
        "test",
        encoding="utf-8",
    )

    (captions / "video_en.srt").write_text(
        "srt",
        encoding="utf-8",
    )
    (captions / "video_en.vtt").write_text(
        "vtt",
        encoding="utf-8",
    )

    (outputs / "video_en_captioned.mp4").write_bytes(b"video")

    agent = DashboardAgent(
        upload_dir=uploads,
        caption_dir=captions,
        output_dir=outputs,
    )

    result = agent.get_statistics()

    assert result["videos"] == 1
    assert result["caption_files"] == 2
    assert result["captioned_videos"] == 1


def test_dashboard_empty_directories(
    tmp_path: Path,
) -> None:
    """Return zero statistics for missing directories."""
    agent = DashboardAgent(
        upload_dir=tmp_path / "uploads",
        caption_dir=tmp_path / "captions",
        output_dir=tmp_path / "outputs",
    )

    result = agent.get_statistics()

    assert result == {
        "videos": 0,
        "caption_files": 0,
        "captioned_videos": 0,
    }


def test_recent_files(
    tmp_path: Path,
) -> None:
    """Return recent files from all dashboard directories."""
    uploads = tmp_path / "uploads"
    captions = tmp_path / "captions"
    outputs = tmp_path / "outputs"

    uploads.mkdir()
    captions.mkdir()
    outputs.mkdir()

    (uploads / "video.mp4").write_bytes(b"video")

    (captions / "video_en.srt").write_text(
        "srt",
        encoding="utf-8",
    )

    (outputs / "video_en_captioned.mp4").write_bytes(b"video")

    agent = DashboardAgent(
        upload_dir=uploads,
        caption_dir=captions,
        output_dir=outputs,
    )

    result = agent.get_recent_files(limit=5)

    assert len(result) == 3

    names = [item["name"] for item in result]

    assert "video.mp4" in names
    assert "video_en.srt" in names
    assert "video_en_captioned.mp4" in names


def test_recent_files_limit(
    tmp_path: Path,
) -> None:
    """Respect the requested recent-file limit."""
    uploads = tmp_path / "uploads"
    uploads.mkdir()

    for index in range(5):
        (uploads / f"video_{index}.mp4").write_bytes(b"video")

    agent = DashboardAgent(
        upload_dir=uploads,
        caption_dir=tmp_path / "captions",
        output_dir=tmp_path / "outputs",
    )

    result = agent.get_recent_files(limit=2)

    assert len(result) == 2


def test_recent_files_zero_limit(
    tmp_path: Path,
) -> None:
    """Return an empty list for a zero limit."""
    agent = DashboardAgent(
        upload_dir=tmp_path / "uploads",
        caption_dir=tmp_path / "captions",
        output_dir=tmp_path / "outputs",
    )

    result = agent.get_recent_files(limit=0)

    assert result == []


def test_recent_files_negative_limit(
    tmp_path: Path,
) -> None:
    """Return an empty list for a negative limit."""
    agent = DashboardAgent(
        upload_dir=tmp_path / "uploads",
        caption_dir=tmp_path / "captions",
        output_dir=tmp_path / "outputs",
    )

    result = agent.get_recent_files(limit=-1)

    assert result == []


def test_recent_files_excludes_gitkeep(
    tmp_path: Path,
) -> None:
    """Do not include .gitkeep files in recent files."""
    uploads = tmp_path / "uploads"
    captions = tmp_path / "captions"
    outputs = tmp_path / "outputs"

    uploads.mkdir()
    captions.mkdir()
    outputs.mkdir()

    (uploads / ".gitkeep").write_text(
        "",
        encoding="utf-8",
    )

    (captions / ".gitkeep").write_text(
        "",
        encoding="utf-8",
    )

    (outputs / ".gitkeep").write_text(
        "",
        encoding="utf-8",
    )

    (uploads / "video.mp4").write_bytes(b"video")

    (captions / "video_en.srt").write_text(
        "srt",
        encoding="utf-8",
    )

    agent = DashboardAgent(
        upload_dir=uploads,
        caption_dir=captions,
        output_dir=outputs,
    )

    result = agent.get_recent_files(limit=10)

    names = [item["name"] for item in result]

    assert ".gitkeep" not in names
    assert "video.mp4" in names
    assert "video_en.srt" in names


def test_recent_files_result_structure(
    tmp_path: Path,
) -> None:
    """Return the expected structure for recent files."""
    uploads = tmp_path / "uploads"
    uploads.mkdir()

    video = uploads / "video.mp4"
    video.write_bytes(b"video")

    agent = DashboardAgent(
        upload_dir=uploads,
        caption_dir=tmp_path / "captions",
        output_dir=tmp_path / "outputs",
    )

    result = agent.get_recent_files()

    assert len(result) == 1

    item = result[0]

    assert item["name"] == "video.mp4"
    assert item["path"] == str(video)
    assert item["type"] == ".mp4"


def test_count_files_without_extension_filter(
    tmp_path: Path,
) -> None:
    """Count all files when no extension filter is supplied."""
    directory = tmp_path / "files"
    directory.mkdir()

    (directory / "one.txt").write_text(
        "one",
        encoding="utf-8",
    )

    (directory / "two.json").write_text(
        "{}",
        encoding="utf-8",
    )

    (directory / ".gitkeep").write_text(
        "",
        encoding="utf-8",
    )

    result = DashboardAgent._count_files(directory)

    assert result == 3


def test_count_files_with_extension_filter(
    tmp_path: Path,
) -> None:
    """Count only files matching the requested extensions."""
    directory = tmp_path / "files"
    directory.mkdir()

    (directory / "one.mp4").write_bytes(b"video")

    (directory / "two.mp4").write_bytes(b"video")

    (directory / "three.txt").write_text(
        "text",
        encoding="utf-8",
    )

    result = DashboardAgent._count_files(
        directory,
        (".mp4",),
    )

    assert result == 2


def test_count_files_is_case_insensitive(
    tmp_path: Path,
) -> None:
    """Extension filtering should be case-insensitive."""
    directory = tmp_path / "files"
    directory.mkdir()

    (directory / "video.MP4").write_bytes(b"video")

    (directory / "caption.SRT").write_text(
        "caption",
        encoding="utf-8",
    )

    result = DashboardAgent._count_files(
        directory,
        (
            ".mp4",
            ".srt",
        ),
    )

    assert result == 2


def test_count_files_missing_directory(
    tmp_path: Path,
) -> None:
    """Return zero when the directory does not exist."""
    directory = tmp_path / "missing"

    result = DashboardAgent._count_files(directory)

    assert result == 0
