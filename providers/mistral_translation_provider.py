from mistralai.client import Mistral

from providers.translation_provider import TranslationProvider


class MistralTranslationProvider(TranslationProvider):
    """Translate captions using Mistral."""

    def __init__(
        self,
        model: str = "mistral-medium-latest",
        api_key: str | None = None,
    ) -> None:
        self.client = Mistral(api_key=api_key)
        self.model = model

    def translate(
        self,
        text: str,
        target_language: str,
    ) -> str:
        if not text.strip():
            raise ValueError("Text cannot be empty.")

        if not target_language.strip():
            raise ValueError(
                "Target language cannot be empty."
            )

        response = self.client.chat.complete(
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

        result = (
            response.choices[0]
            .message.content
            .strip()
        )

        if not result:
            raise RuntimeError(
                "Mistral returned an empty translation."
            )

        return result