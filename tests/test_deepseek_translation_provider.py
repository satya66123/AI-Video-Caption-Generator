"""Tests for the DeepSeek translation provider."""

from unittest.mock import MagicMock, patch

import pytest

from providers.deepseek_translation_provider import (
    DeepSeekTranslationProvider,
)


def test_deepseek_provider_initialization() -> None:
    """Initialize the DeepSeek provider."""
    with patch("providers.deepseek_translation_provider.OpenAI") as mock_openai:
        provider = DeepSeekTranslationProvider(
            model="deepseek-v4-flash",
            api_key="test-key",
        )

        mock_openai.assert_called_once_with(
            api_key="test-key",
            base_url="https://api.deepseek.com",
        )

        assert provider.model == "deepseek-v4-flash"


def test_deepseek_translation() -> None:
    """Translate text using DeepSeek."""
    mock_response = MagicMock()

    mock_response.choices[0].message.content = "Hola mundo"

    with patch("providers.deepseek_translation_provider.OpenAI") as mock_openai:
        mock_client = mock_openai.return_value

        mock_client.chat.completions.create.return_value = mock_response

        provider = DeepSeekTranslationProvider(
            model="deepseek-v4-flash",
            api_key="test-key",
        )

        result = provider.translate(
            "Hello world",
            "Spanish",
        )

        assert result == "Hola mundo"

        mock_client.chat.completions.create.assert_called_once()


def test_deepseek_empty_text() -> None:
    """Reject empty source text."""
    with patch("providers.deepseek_translation_provider.OpenAI"):
        provider = DeepSeekTranslationProvider(api_key="test-key")

        with pytest.raises(
            ValueError,
            match="Text cannot be empty.",
        ):
            provider.translate(
                "",
                "Spanish",
            )


def test_deepseek_whitespace_text() -> None:
    """Reject whitespace-only source text."""
    with patch("providers.deepseek_translation_provider.OpenAI"):
        provider = DeepSeekTranslationProvider(api_key="test-key")

        with pytest.raises(
            ValueError,
            match="Text cannot be empty.",
        ):
            provider.translate(
                "   ",
                "Spanish",
            )


def test_deepseek_empty_target_language() -> None:
    """Reject empty target language."""
    with patch("providers.deepseek_translation_provider.OpenAI"):
        provider = DeepSeekTranslationProvider(api_key="test-key")

        with pytest.raises(
            ValueError,
            match="Target language cannot be empty.",
        ):
            provider.translate(
                "Hello world",
                "",
            )


def test_deepseek_whitespace_target_language() -> None:
    """Reject whitespace-only target language."""
    with patch("providers.deepseek_translation_provider.OpenAI"):
        provider = DeepSeekTranslationProvider(api_key="test-key")

        with pytest.raises(
            ValueError,
            match="Target language cannot be empty.",
        ):
            provider.translate(
                "Hello world",
                "   ",
            )


def test_deepseek_empty_response() -> None:
    """Reject an empty DeepSeek response."""
    mock_response = MagicMock()

    mock_response.choices[0].message.content = ""

    with patch("providers.deepseek_translation_provider.OpenAI") as mock_openai:
        mock_client = mock_openai.return_value

        mock_client.chat.completions.create.return_value = mock_response

        provider = DeepSeekTranslationProvider(api_key="test-key")

        with pytest.raises(
            RuntimeError,
            match="DeepSeek returned an empty translation.",
        ):
            provider.translate(
                "Hello world",
                "Spanish",
            )
