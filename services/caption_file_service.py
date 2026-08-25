"""Caption file writing service."""

from pathlib import Path

from utils.caption_utils import (
    build_caption_filename,
)


class CaptionFileService:
    """Save generated caption files."""

    def __init__(self, output_dir: str | Path = "captions") -> None:
        """Initialize the caption file service."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_srt(
        self,
        video_path: str | Path,
        language_code: str,
        content: str,
    ) -> Path:
        """Save SRT caption content."""
        return self._save(
            video_path,
            language_code,
            "srt",
            content,
        )

    def save_vtt(
        self,
        video_path: str | Path,
        language_code: str,
        content: str,
    ) -> Path:
        """Save VTT caption content."""
        return self._save(
            video_path,
            language_code,
            "vtt",
            content,
        )

    def _save(
        self,
        video_path: str | Path,
        language_code: str,
        extension: str,
        content: str,
    ) -> Path:
        """Save caption content to disk."""
        if not content.strip():
            raise ValueError("Caption content cannot be empty.")

        filename = build_caption_filename(
            video_path,
            language_code,
            extension,
        )

        output_path = self.output_dir / filename

        output_path.write_text(
            content,
            encoding="utf-8",
        )

        return output_path
