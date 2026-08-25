import cohere

from providers.translation_provider import TranslationProvider


class CohereTranslationProvider(TranslationProvider):
    """Translate captions using Cohere."""

    def __init__(
        self,
        model: str = "command-a-03-2025",
        api_key: str | None = None,
    ) -> None:
        self.client = cohere.ClientV2(api_key=api_key)
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

        response = self.client.chat(
            model=self.model,
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

        result = response.message.content[0].text.strip()

        if not result:
            raise RuntimeError("Cohere returned an empty translation.")

        return result
