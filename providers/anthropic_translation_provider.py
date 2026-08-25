from anthropic import Anthropic

from providers.translation_provider import TranslationProvider


class AnthropicTranslationProvider(TranslationProvider):
    """Translate captions using Anthropic Claude."""

    def __init__(
        self,
        model: str = "claude-sonnet-4-5",
        api_key: str | None = None,
    ) -> None:
        self.client = Anthropic(api_key=api_key)
        self.model = model

    def translate(
        self,
        text: str,
        target_language: str,
    ) -> str:
        if not text.strip():
            raise ValueError("Text cannot be empty.")

        if not target_language.strip():
            raise ValueError("Target language cannot be empty.")

        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Translate the following text into "
                        f"{target_language}. "
                        "Return only the translation.\n\n"
                        f"{text}"
                    ),
                }
            ],
        )

        result = message.content[0].text.strip()

        if not result:
            raise RuntimeError("Anthropic returned an empty translation.")

        return result
