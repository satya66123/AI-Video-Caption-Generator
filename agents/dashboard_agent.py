"""Dashboard agent."""

from pathlib import Path
from typing import Any


class DashboardAgent:
    """Provide dashboard statistics for the caption application."""

    def __init__(
        self,
        upload_dir: str | Path = "uploads",
        caption_dir: str | Path = "captions",
        output_dir: str | Path = "outputs",
    ) -> None:
        """Initialize the dashboard agent."""
        self.upload_dir = Path(upload_dir)
        self.caption_dir = Path(caption_dir)
        self.output_dir = Path(output_dir)

    @staticmethod
    def _count_files(
        directory: Path,
        extensions: tuple[str, ...] | None = None,
    ) -> int:
        """Count files in a directory."""
        if not directory.exists():
            return 0

        files = [path for path in directory.iterdir() if path.is_file()]

        if extensions is None:
            return len(files)

        normalized_extensions = {extension.lower() for extension in extensions}

        return sum(1 for path in files if path.suffix.lower() in normalized_extensions)

    def get_statistics(self) -> dict[str, int]:
        """Return dashboard file statistics."""
        return {
            "videos": self._count_files(
                self.upload_dir,
                (
                    ".mp4",
                    ".mov",
                    ".avi",
                    ".mkv",
                    ".webm",
                ),
            ),
            "caption_files": self._count_files(
                self.caption_dir,
                (
                    ".srt",
                    ".vtt",
                ),
            ),
            "captioned_videos": self._count_files(
                self.output_dir,
                (
                    ".mp4",
                    ".mov",
                    ".avi",
                    ".mkv",
                    ".webm",
                ),
            ),
        }

    def get_recent_files(
        self,
        limit: int = 5,
    ) -> list[dict[str, Any]]:
        """Return the most recently modified output files."""
        if limit <= 0:
            return []

        directories = (
            self.upload_dir,
            self.caption_dir,
            self.output_dir,
        )

        files: list[Path] = []

        for directory in directories:
            if not directory.exists():
                continue

            files.extend(
                path
                for path in directory.iterdir()
                if path.is_file() and path.name != ".gitkeep"
            )

        files.sort(
            key=lambda path: path.stat().st_mtime,
            reverse=True,
        )

        return [
            {
                "name": path.name,
                "path": str(path),
                "type": path.suffix.lower(),
            }
            for path in files[:limit]
        ]
