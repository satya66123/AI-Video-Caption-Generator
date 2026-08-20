"""Tests for the Mistral translation provider."""

from unittest.mock import MagicMock, patch

import pytest

from providers.mistral_translation_provider import (
    MistralTranslationProvider,
)


def test_mistral_provider_initialization() -> None:
    """Initialize the Mistral provider."""
    with patch(
        "providers.mistral_translation_provider.Mistral"
    ) as mock_mistral:
        provider = MistralTranslationProvider(
            model="mistral-medium-latest",
            api_key="test-key",
        )

        mock_mistral.assert_called_once_with(
            api_key="test-key"
        )

        assert (
            provider.model
            == "mistral-medium-latest"
        )


def test_mistral_translation() -> None:
    """Translate text using Mistral."""
    mock_response = MagicMock()

    mock_response.choices[0].message.content = (
        "Hola mundo"
    )

    with patch(
        "providers.mistral_translation_provider.Mistral"
    ) as mock_mistral:
        mock_client = mock_mistral.return_value

        mock_client.chat.complete.return_value = (
            mock_response
        )

        provider = MistralTranslationProvider(
            model="mistral-medium-latest",
            api_key="test-key",
        )

        result = provider.translate(
            "Hello world",
            "Spanish",
        )

        assert result == "Hola mundo"

        mock_client.chat.complete.assert_called_once()


def test_mistral_empty_text() -> None:
    """Reject empty source text."""
    with patch(
        "providers.mistral_translation_provider.Mistral"
    ):
        provider = MistralTranslationProvider(
            api_key="test-key"
        )

        with pytest.raises(
            ValueError,
            match="Text cannot be empty.",
        ):
            provider.translate(
                "",
                "Spanish",
            )


def test_mistral_whitespace_text() -> None:
    """Reject whitespace-only source text."""
    with patch(
        "providers.mistral_translation_provider.Mistral"
    ):
        provider = MistralTranslationProvider(
            api_key="test-key"
        )

        with pytest.raises(
            ValueError,
            match="Text cannot be empty.",
        ):
            provider.translate(
                "   ",
                "Spanish",
            )


def test_mistral_empty_target_language() -> None:
    """Reject empty target language."""
    with patch(
        "providers.mistral_translation_provider.Mistral"
    ):
        provider = MistralTranslationProvider(
            api_key="test-key"
        )

        with pytest.raises(
            ValueError,
            match="Target language cannot be empty.",
        ):
            provider.translate(
                "Hello world",
                "",
            )


def test_mistral_whitespace_target_language() -> None:
    """Reject whitespace-only target language."""
    with patch(
        "providers.mistral_translation_provider.Mistral"
    ):
        provider = MistralTranslationProvider(
            api_key="test-key"
        )

        with pytest.raises(
            ValueError,
            match="Target language cannot be empty.",
        ):
            provider.translate(
                "Hello world",
                "   ",
            )


def test_mistral_empty_response() -> None:
    """Reject an empty Mistral response."""
    mock_response = MagicMock()

    mock_response.choices[0].message.content = ""

    with patch(
        "providers.mistral_translation_provider.Mistral"
    ) as mock_mistral:
        mock_client = mock_mistral.return_value

        mock_client.chat.complete.return_value = (
            mock_response
        )

        provider = MistralTranslationProvider(
            api_key="test-key"
        )

        with pytest.raises(
            RuntimeError,
            match="Mistral returned an empty translation.",
        ):
            provider.translate(
                "Hello world",
                "Spanish",
            )