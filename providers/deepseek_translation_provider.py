from openai import OpenAI

from providers.translation_provider import TranslationProvider


class DeepSeekTranslationProvider(TranslationProvider):
    """Translate captions using DeepSeek."""

    BASE_URL = "https://api.deepseek.com"

    def __init__(
        self,
        model: str = "deepseek-v4-flash",
        api_key: str | None = None,
    ) -> None:
        self.client = OpenAI(
            api_key=api_key,
            base_url=self.BASE_URL,
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
            raise ValueError("Target language cannot be empty.")

        response = self.client.chat.completions.create(
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

        result = response.choices[0].message.content.strip()

        if not result:
            raise RuntimeError("DeepSeek returned an empty translation.")

        return result
