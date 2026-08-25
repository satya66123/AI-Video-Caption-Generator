"""Caption Generator data models."""

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class CaptionConfig:
    """Configuration for a caption-generation request."""

    language: str
    format: str = "srt"


@dataclass
class CaptionRecord:
    """Caption-only history record for a video."""

    video_id: str
    source_language: str = ""
    source_language_confidence: float | None = None
    caption_language: str = ""
    format: str = "srt"
    caption_file: str = ""
    captioned_video: str = ""
    status: str = "pending"
    created_at: str = ""
    updated_at: str = ""

    def to_dict(self) -> dict[str, Any]:
        """Convert the record to a JSON-compatible dictionary."""
        return asdict(self)


@dataclass
class CaptionSegment:
    """A single timestamped caption segment."""

    start: float
    end: float
    text: str
