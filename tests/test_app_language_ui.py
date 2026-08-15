from pathlib import Path
from unittest.mock import MagicMock

import app


def test_detected_language_is_stored() -> None:
    detection = {
        "language": "te",
        "language_name": "Telugu",
    }

    assert detection["language"] == "te"
    assert detection["language_name"] == "Telugu"


def test_caption_language_mapping() -> None:
    caption_languages = {
        "English": "en",
        "Telugu": "te",
        "Hindi": "hi",
        "Tamil": "ta",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Bengali": "bn",
        "Marathi": "mr",
    }

    assert caption_languages["English"] == "en"
    assert caption_languages["Telugu"] == "te"
    assert caption_languages["Hindi"] == "hi"


def test_uploaded_video_path_is_a_path() -> None:
    video_path = Path("uploads/gm.mp4")

    assert isinstance(video_path, Path)
    assert video_path.name == "gm.mp4"