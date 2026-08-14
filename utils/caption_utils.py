"""Caption utility functions."""

from pathlib import Path
from config.caption_config import SUPPORTED_CAPTION_LANGUAGES


def _get_video_stem(video_path: str | Path) -> str:
    """Return a valid video filename stem."""
    path = Path(video_path)
    filename = path.name
    stem = path.stem

    if not filename or not stem or stem.startswith("."):
        raise ValueError("Video filename cannot be empty.")

    return stem


def build_caption_filename(
    video_path: str | Path,
    language_code: str,
    extension: str,
) -> str:
    """Build a caption filename from the original video filename."""
    video_name = _get_video_stem(video_path)
    clean_language = language_code.strip().lower()
    clean_extension = extension.strip().lower().lstrip(".")

    if not clean_language:
        raise ValueError("Language code cannot be empty.")

    if clean_extension not in {"srt", "vtt"}:
        raise ValueError("Caption extension must be 'srt' or 'vtt'.")

    return f"{video_name}_{clean_language}.{clean_extension}"


def build_captioned_video_filename(
    video_path: str | Path,
    language_code: str,
) -> str:
    """Build the filename for a burned-caption video."""
    video_name = _get_video_stem(video_path)
    clean_language = language_code.strip().lower()

    if not clean_language:
        raise ValueError("Language code cannot be empty.")

    return f"{video_name}_{clean_language}_captioned.mp4"


def validate_caption_input() -> bool:
    """Validate caption input.

    Full validation will be implemented in a later phase.
    """
    return True


def get_supported_caption_languages() -> dict[str, str]:
    """Return supported caption languages."""
    return SUPPORTED_CAPTION_LANGUAGES.copy()


def validate_caption_language(language_code: str) -> bool:
    """Validate a caption language code."""
    return language_code.strip().lower() in SUPPORTED_CAPTION_LANGUAGES