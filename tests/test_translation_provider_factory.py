"""Tests for translation provider factory."""

from unittest.mock import patch

import pytest

from providers.translation_provider_factory import (
    TranslationProviderFactory,
)

from providers.mistral_translation_provider import (
    MistralTranslationProvider,
)
from providers.groq_translation_provider import (
    GroqTranslationProvider,
)
from providers.cohere_translation_provider import (
    CohereTranslationProvider,
)
from providers.deepseek_translation_provider import (
    DeepSeekTranslationProvider,
)


def test_supported_providers() -> None:
    """Verify all supported providers are registered."""
    assert (
        TranslationProviderFactory.SUPPORTED_PROVIDERS
        == (
            "ollama",
            "openai",
            "anthropic",
            "gemini",
        )
    )

def test_supported_providers() -> None:
    """Verify all supported translation providers."""
    assert TranslationProviderFactory.SUPPORTED_PROVIDERS == (
        "ollama",
        "openai",
        "anthropic",
        "gemini",
        "mistral",
        "groq",
        "cohere",
        "deepseek",
    )

def test_create_mistral_provider() -> None:
    """Create a Mistral provider."""
    provider = TranslationProviderFactory.create(
        "mistral",
        api_key="test-key",
    )

    assert isinstance(
        provider,
        MistralTranslationProvider,
    )


def test_create_groq_provider() -> None:
    """Create a Groq provider."""
    provider = TranslationProviderFactory.create(
        "groq",
        api_key="test-key",
    )

    assert isinstance(
        provider,
        GroqTranslationProvider,
    )


def test_create_cohere_provider() -> None:
    """Create a Cohere provider."""
    provider = TranslationProviderFactory.create(
        "cohere",
        api_key="test-key",
    )

    assert isinstance(
        provider,
        CohereTranslationProvider,
    )


def test_create_deepseek_provider() -> None:
    """Create a DeepSeek provider."""
    provider = TranslationProviderFactory.create(
        "deepseek",
        api_key="test-key",
    )

    assert isinstance(
        provider,
        DeepSeekTranslationProvider,
    )

@patch(
    "providers.translation_provider_factory."
    "OllamaTranslationProvider"
)
def test_create_ollama_provider(
    mock_provider,
) -> None:
    """Create Ollama provider."""
    TranslationProviderFactory.create(
        "ollama",
    )

    mock_provider.assert_called_once_with()


@patch(
    "providers.translation_provider_factory."
    "OpenAITranslationProvider"
)
def test_create_openai_provider(
    mock_provider,
) -> None:
    """Create OpenAI provider."""
    TranslationProviderFactory.create(
        "openai",
    )

    mock_provider.assert_called_once_with()


@patch(
    "providers.translation_provider_factory."
    "AnthropicTranslationProvider"
)
def test_create_anthropic_provider(
    mock_provider,
) -> None:
    """Create Anthropic provider."""
    TranslationProviderFactory.create(
        "anthropic",
    )

    mock_provider.assert_called_once_with()


@patch(
    "providers.translation_provider_factory."
    "GeminiTranslationProvider"
)
def test_create_gemini_provider(
    mock_provider,
) -> None:
    """Create Gemini provider."""
    TranslationProviderFactory.create(
        "gemini",
    )

    mock_provider.assert_called_once_with()


@pytest.mark.parametrize(
    "provider",
    [
        "OLLAMA",
        "OpenAI",
        "ANTHROPIC",
        "Gemini",
    ],
)
def test_create_is_case_insensitive(
    provider: str,
) -> None:
    """Provider names are case insensitive."""
    with patch(
        "providers.translation_provider_factory."
        "OllamaTranslationProvider"
    ) as ollama:
        with patch(
            "providers.translation_provider_factory."
            "OpenAITranslationProvider"
        ) as openai:
            with patch(
                "providers.translation_provider_factory."
                "AnthropicTranslationProvider"
            ) as anthropic:
                with patch(
                    "providers.translation_provider_factory."
                    "GeminiTranslationProvider"
                ) as gemini:

                    TranslationProviderFactory.create(
                        provider,
                    )

                    assert (
                        ollama.called
                        or openai.called
                        or anthropic.called
                        or gemini.called
                    )


def test_create_rejects_empty_provider() -> None:
    """Reject an empty provider name."""
    with pytest.raises(
        ValueError,
        match="Translation provider cannot be empty.",
    ):
        TranslationProviderFactory.create("   ")


def test_create_rejects_unsupported_provider() -> None:
    """Reject an unsupported provider."""
    with pytest.raises(
        ValueError,
        match="Unsupported translation provider",
    ):
        TranslationProviderFactory.create(
            "unsupported",
        )