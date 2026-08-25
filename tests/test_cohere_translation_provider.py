"""Tests for the Cohere translation provider."""

from unittest.mock import MagicMock, patch

import pytest

from providers.cohere_translation_provider import (
    CohereTranslationProvider,
)


def test_cohere_provider_initialization() -> None:
    """Initialize the Cohere provider."""
    with patch("providers.cohere_translation_provider.cohere.ClientV2") as mock_client:
        provider = CohereTranslationProvider(
            model="command-a-03-2025",
            api_key="test-key",
        )

        mock_client.assert_called_once_with(api_key="test-key")

        assert provider.model == "command-a-03-2025"


def test_cohere_translation() -> None:
    """Translate text using Cohere."""
    mock_response = MagicMock()

    mock_response.message.content = [MagicMock(text="Hola mundo")]

    with patch("providers.cohere_translation_provider.cohere.ClientV2") as mock_client:
        mock_instance = mock_client.return_value

        mock_instance.chat.return_value = mock_response

        provider = CohereTranslationProvider(
            model="command-a-03-2025",
            api_key="test-key",
        )

        result = provider.translate(
            "Hello world",
            "Spanish",
        )

        assert result == "Hola mundo"

        mock_instance.chat.assert_called_once()


def test_cohere_empty_text() -> None:
    """Reject empty source text."""
    with patch("providers.cohere_translation_provider.cohere.ClientV2"):
        provider = CohereTranslationProvider(api_key="test-key")

        with pytest.raises(
            ValueError,
            match="Text cannot be empty.",
        ):
            provider.translate("", "Spanish")


def test_cohere_whitespace_text() -> None:
    """Reject whitespace-only source text."""
    with patch("providers.cohere_translation_provider.cohere.ClientV2"):
        provider = CohereTranslationProvider(api_key="test-key")

        with pytest.raises(
            ValueError,
            match="Text cannot be empty.",
        ):
            provider.translate("   ", "Spanish")


def test_cohere_empty_target_language() -> None:
    """Reject empty target language."""
    with patch("providers.cohere_translation_provider.cohere.ClientV2"):
        provider = CohereTranslationProvider(api_key="test-key")

        with pytest.raises(
            ValueError,
            match="Target language cannot be empty.",
        ):
            provider.translate("Hello world", "")


def test_cohere_whitespace_target_language() -> None:
    """Reject whitespace-only target language."""
    with patch("providers.cohere_translation_provider.cohere.ClientV2"):
        provider = CohereTranslationProvider(api_key="test-key")

        with pytest.raises(
            ValueError,
            match="Target language cannot be empty.",
        ):
            provider.translate("Hello world", "   ")


def test_cohere_empty_response() -> None:
    """Reject an empty Cohere response."""
    mock_response = MagicMock()

    mock_response.message.content = [MagicMock(text="")]

    with patch("providers.cohere_translation_provider.cohere.ClientV2") as mock_client:
        mock_instance = mock_client.return_value

        mock_instance.chat.return_value = mock_response

        provider = CohereTranslationProvider(api_key="test-key")

        with pytest.raises(
            RuntimeError,
            match="Cohere returned an empty translation.",
        ):
            provider.translate(
                "Hello world",
                "Spanish",
            )
