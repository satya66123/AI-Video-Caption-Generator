from openai import OpenAI

from providers.translation_provider import TranslationProvider


class OpenAITranslationProvider(TranslationProvider):
    """Translate captions using OpenAI."""

    def __init__(
        self,
        model: str = "gpt-5-mini",
        api_key: str | None = None,
    ) -> None:
        self.client = OpenAI(api_key=api_key)
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

        response = self.client.responses.create(
            model=self.model,
            input=(
                f"Translate the following text into "
                f"{target_language}. "
                "Return only the translation.\n\n"
                f"{text}"
            ),
        )

        result = response.output_text.strip()

        if not result:
            raise RuntimeError("OpenAI returned an empty translation.")

        return result
