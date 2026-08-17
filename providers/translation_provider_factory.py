"""Translation provider factory."""

from providers.translation_provider import TranslationProvider
from providers.ollama_translation_provider import (
    OllamaTranslationProvider,
)
from providers.openai_translation_provider import (
    OpenAITranslationProvider,
)
from providers.anthropic_translation_provider import (
    AnthropicTranslationProvider,
)
from providers.gemini_translation_provider import (
    GeminiTranslationProvider,
)


class TranslationProviderFactory:
    """Create translation providers based on provider name."""

    SUPPORTED_PROVIDERS = (
        "ollama",
        "openai",
        "anthropic",
        "gemini",
    )

    @classmethod
    def create(
        cls,
        provider: str,
        **kwargs: object,
    ) -> TranslationProvider:
        """Create a translation provider."""
        normalized_provider = provider.strip().lower()

        if not normalized_provider:
            raise ValueError(
                "Translation provider cannot be empty."
            )

        if normalized_provider == "ollama":
            return OllamaTranslationProvider(
                **kwargs,
            )

        if normalized_provider == "openai":
            return OpenAITranslationProvider(
                **kwargs,
            )

        if normalized_provider == "anthropic":
            return AnthropicTranslationProvider(
                **kwargs,
            )

        if normalized_provider == "gemini":
            return GeminiTranslationProvider(
                **kwargs,
            )

        raise ValueError(
            f"Unsupported translation provider: {provider}"
        )