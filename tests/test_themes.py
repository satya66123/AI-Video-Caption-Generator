import pytest

from app import THEMES


def test_themes_exist():
    """Verify all application themes are defined."""

    assert len(THEMES) == 5


def test_expected_themes_exist():
    """Verify the expected themes are available."""

    expected_themes = {
        "🌙 Dark",
        "🌌 Midnight Blue",
        "💜 Cosmic Purple",
        "🌊 Ocean",
        "🌿 Emerald",
    }

    assert set(THEMES.keys()) == expected_themes


def test_light_theme_is_removed():
    """Verify the Light theme is no longer available."""

    assert "☀️ Light" not in THEMES


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


def test_dark_is_default_theme():
    """Verify Dark is the first/default theme."""

    assert next(iter(THEMES)) == "🌙 Dark"