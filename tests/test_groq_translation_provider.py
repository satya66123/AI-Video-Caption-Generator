"""Tests for the Groq translation provider."""

from unittest.mock import MagicMock, patch

import pytest

from providers.groq_translation_provider import (
    GroqTranslationProvider,
)


def test_groq_provider_initialization() -> None:
    """Initialize the Groq provider."""
    with patch(
        "providers.groq_translation_provider.Groq"
    ) as mock_groq:
        provider = GroqTranslationProvider(
            model="llama-3.1-8b-instant",
            api_key="test-key",
        )

        mock_groq.assert_called_once_with(
            api_key="test-key"
        )

        assert (
            provider.model
            == "llama-3.1-8b-instant"
        )


def test_groq_translation() -> None:
    """Translate text using Groq."""
    mock_response = MagicMock()

    mock_response.choices[0].message.content = (
        "Hola mundo"
    )

    with patch(
        "providers.groq_translation_provider.Groq"
    ) as mock_groq:
        mock_client = mock_groq.return_value

        mock_client.chat.completions.create.return_value = (
            mock_response
        )

        provider = GroqTranslationProvider(
            model="llama-3.1-8b-instant",
            api_key="test-key",
        )

        result = provider.translate(
            "Hello world",
            "Spanish",
        )

        assert result == "Hola mundo"

        mock_client.chat.completions.create.assert_called_once()


def test_groq_empty_text() -> None:
    """Reject empty source text."""
    with patch(
        "providers.groq_translation_provider.Groq"
    ):
        provider = GroqTranslationProvider(
            api_key="test-key"
        )

        with pytest.raises(
            ValueError,
            match="Text cannot be empty.",
        ):
            provider.translate("", "Spanish")


def test_groq_whitespace_text() -> None:
    """Reject whitespace-only source text."""
    with patch(
        "providers.groq_translation_provider.Groq"
    ):
        provider = GroqTranslationProvider(
            api_key="test-key"
        )

        with pytest.raises(
            ValueError,
            match="Text cannot be empty.",
        ):
            provider.translate("   ", "Spanish")


def test_groq_empty_target_language() -> None:
    """Reject empty target language."""
    with patch(
        "providers.groq_translation_provider.Groq"
    ):
        provider = GroqTranslationProvider(
            api_key="test-key"
        )

        with pytest.raises(
            ValueError,
            match="Target language cannot be empty.",
        ):
            provider.translate("Hello world", "")


def test_groq_whitespace_target_language() -> None:
    """Reject whitespace-only target language."""
    with patch(
        "providers.groq_translation_provider.Groq"
    ):
        provider = GroqTranslationProvider(
            api_key="test-key"
        )

        with pytest.raises(
            ValueError,
            match="Target language cannot be empty.",
        ):
            provider.translate("Hello world", "   ")


def test_groq_empty_response() -> None:
    """Reject an empty Groq response."""
    mock_response = MagicMock()

    mock_response.choices[0].message.content = ""

    with patch(
        "providers.groq_translation_provider.Groq"
    ) as mock_groq:
        mock_client = mock_groq.return_value

        mock_client.chat.completions.create.return_value = (
            mock_response
        )

        provider = GroqTranslationProvider(
            api_key="test-key"
        )

        with pytest.raises(
            RuntimeError,
            match="Groq returned an empty translation.",
        ):
            provider.translate(
                "Hello world",
                "Spanish",
            )