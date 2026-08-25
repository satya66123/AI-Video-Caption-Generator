from pathlib import Path
from unittest.mock import MagicMock

from app import save_uploaded_video


def test_save_uploaded_video(tmp_path, monkeypatch) -> None:
    uploaded_file = MagicMock()
    uploaded_file.name = "sample.mp4"
    uploaded_file.getbuffer.return_value = b"video data"

    monkeypatch.setattr(
        "app.UPLOAD_DIR",
        tmp_path,
    )

    result = save_uploaded_video(uploaded_file)

    assert result == tmp_path / "sample.mp4"
    assert result.is_file()
    assert result.read_bytes() == b"video data"


def test_save_uploaded_video_removes_path_components(
    tmp_path,
    monkeypatch,
) -> None:
    uploaded_file = MagicMock()
    uploaded_file.name = "folder/sample.mp4"
    uploaded_file.getbuffer.return_value = b"video"

    monkeypatch.setattr(
        "app.UPLOAD_DIR",
        tmp_path,
    )

    result = save_uploaded_video(uploaded_file)

    assert result.name == "sample.mp4"
    assert result.is_file()
