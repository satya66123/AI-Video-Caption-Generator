from config.caption_config import SUPPORTED_CAPTION_LANGUAGES


def test_caption_ui_languages_are_configured() -> None:
    """Verify the UI has supported caption languages."""
    assert "en" in SUPPORTED_CAPTION_LANGUAGES
    assert "te" in SUPPORTED_CAPTION_LANGUAGES
    assert "hi" in SUPPORTED_CAPTION_LANGUAGES


def test_caption_ui_language_names_are_not_empty() -> None:
    """Verify every configured language has a display name."""
    for code, name in SUPPORTED_CAPTION_LANGUAGES.items():
        assert code
        assert name