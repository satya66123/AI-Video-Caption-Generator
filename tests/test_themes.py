import pytest

from app import THEMES


def test_themes_exist():
    """Verify all application themes are defined."""

    assert len(THEMES) == 15


def test_expected_themes_exist():
    """Verify all expected themes are available."""

    expected_themes = {
        # Dark themes
        "🌙 Dark",
        "🌌 Midnight Blue",
        "💜 Cosmic Purple",
        "🌊 Ocean",
        "🌿 Emerald",

        # Light themes
        "☀️ Light",
        "🌤️ Sky Light",
        "💜 Lavender Light",
        "🌿 Mint Light",
        "🌊 Aqua Light",
        "🌸 Rose Light",
        "🍑 Peach Light",
        "🌼 Amber Light",
        "🩵 Ice Light",
        "🌱 Sage Light",
    }

    assert set(THEMES.keys()) == expected_themes


def test_light_themes_are_available():
    """Verify all light themes are available."""

    light_themes = {
        "☀️ Light",
        "🌤️ Sky Light",
        "💜 Lavender Light",
        "🌿 Mint Light",
        "🌊 Aqua Light",
        "🌸 Rose Light",
        "🍑 Peach Light",
        "🌼 Amber Light",
        "🩵 Ice Light",
        "🌱 Sage Light",
    }

    for theme_name in light_themes:
        assert theme_name in THEMES


def test_light_themes_use_black_text():
    """Verify all light themes use black text."""

    light_themes = {
        "☀️ Light",
        "🌤️ Sky Light",
        "💜 Lavender Light",
        "🌿 Mint Light",
        "🌊 Aqua Light",
        "🌸 Rose Light",
        "🍑 Peach Light",
        "🌼 Amber Light",
        "🩵 Ice Light",
        "🌱 Sage Light",
    }

    for theme_name in light_themes:
        assert THEMES[theme_name]["text"] == "#000000"


@pytest.mark.parametrize(
    "theme_name",
    THEMES.keys(),
)
def test_theme_has_required_properties(theme_name):
    """Verify every theme contains the required properties."""

    theme = THEMES[theme_name]

    assert "background" in theme
    assert "sidebar" in theme
    assert "text" in theme
    assert "accent" in theme


@pytest.mark.parametrize(
    "theme_name",
    THEMES.keys(),
)
def test_theme_values_are_valid_strings(theme_name):
    """Verify theme configuration values are strings."""

    theme = THEMES[theme_name]

    assert isinstance(theme["background"], str)
    assert isinstance(theme["sidebar"], str)
    assert isinstance(theme["text"], str)
    assert isinstance(theme["accent"], str)


@pytest.mark.parametrize(
    "theme_name",
    THEMES.keys(),
)
def test_theme_values_are_not_empty(theme_name):
    """Verify theme configuration values are not empty."""

    theme = THEMES[theme_name]

    assert theme["background"].strip()
    assert theme["sidebar"].strip()
    assert theme["text"].strip()
    assert theme["accent"].strip()


def test_dark_is_default_theme():
    """Verify Dark is the first/default theme."""

    assert next(iter(THEMES)) == "🌙 Dark"