from google import genai

from providers.translation_provider import TranslationProvider


class GeminiTranslationProvider(TranslationProvider):
    """Translate captions using Google Gemini."""

    def __init__(
        self,
        model: str = "gemini-3.6-flash",
        api_key: str | None = None,
    ) -> None:
        self.client = genai.Client(
            api_key=api_key,
        )
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

        response = self.client.models.generate_content(
            model=self.model,
            contents=(
                f"Translate the following text into "
                f"{target_language}. "
                "Return only the translation.\n\n"
                f"{text}"
            ),
        )

        result = response.text.strip()

        if not result:
            raise RuntimeError(
                "Gemini returned an empty translation."
            )

        return result