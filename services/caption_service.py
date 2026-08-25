"""Caption storage service."""

import json
from pathlib import Path

from core.caption_models import CaptionRecord


class CaptionService:
    """Manage caption-only JSON history."""

    def __init__(self, storage_dir: str | Path = "data/captions") -> None:
        """Initialize caption storage."""
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

    def get_storage_path(self, video_id: str) -> Path:
        """Return the JSON path for a video caption record."""
        if not video_id.strip():
            raise ValueError("Video ID cannot be empty.")

        return self.storage_dir / f"{video_id}.json"

    def save_record(self, record: CaptionRecord) -> Path:
        """Save a caption-only record as JSON."""
        storage_path = self.get_storage_path(record.video_id)

        with storage_path.open("w", encoding="utf-8") as file:
            json.dump(
                record.to_dict(),
                file,
                indent=2,
                ensure_ascii=False,
            )

        return storage_path

    def load_record(self, video_id: str) -> CaptionRecord:
        """Load a caption-only record from JSON."""
        storage_path = self.get_storage_path(video_id)

        if not storage_path.is_file():
            raise FileNotFoundError(f"Caption record not found: {storage_path}")

        with storage_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return CaptionRecord(**data)
