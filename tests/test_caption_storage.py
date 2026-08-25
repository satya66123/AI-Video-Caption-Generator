import json

from core.caption_models import CaptionRecord
from services.caption_service import CaptionService


def test_caption_record_to_dict() -> None:
    record = CaptionRecord(
        video_id="my_video",
        source_language="te",
        source_language_confidence=0.96,
        caption_language="en",
        format="srt",
        caption_file="my_video_en.srt",
        captioned_video="my_video_en_captioned.mp4",
        status="completed",
        created_at="2026-08-14T13:00:00",
        updated_at="2026-08-14T13:05:00",
    )

    data = record.to_dict()

    assert data["video_id"] == "my_video"
    assert data["source_language"] == "te"
    assert data["caption_language"] == "en"
    assert data["format"] == "srt"
    assert data["status"] == "completed"


def test_caption_record_save_and_load(tmp_path) -> None:
    service = CaptionService(tmp_path)

    record = CaptionRecord(
        video_id="test_video",
        source_language="te",
        source_language_confidence=0.95,
        caption_language="en",
        format="srt",
        caption_file="test_video_en.srt",
        captioned_video="test_video_en_captioned.mp4",
        status="completed",
    )

    path = service.save_record(record)

    assert path.is_file()

    loaded = service.load_record("test_video")

    assert loaded.video_id == "test_video"
    assert loaded.source_language == "te"
    assert loaded.caption_language == "en"
    assert loaded.status == "completed"


def test_caption_json_contains_only_caption_fields(tmp_path) -> None:
    service = CaptionService(tmp_path)

    record = CaptionRecord(
        video_id="video_001",
        source_language="te",
        source_language_confidence=0.96,
        caption_language="en",
        format="srt",
    )

    path = service.save_record(record)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    allowed_fields = {
        "video_id",
        "source_language",
        "source_language_confidence",
        "caption_language",
        "format",
        "caption_file",
        "captioned_video",
        "status",
        "created_at",
        "updated_at",
    }

    assert set(data.keys()) == allowed_fields


def test_empty_video_id_is_rejected(tmp_path) -> None:
    service = CaptionService(tmp_path)

    record = CaptionRecord(video_id="")

    try:
        service.save_record(record)
        assert False, "Expected ValueError"
    except ValueError:
        pass
