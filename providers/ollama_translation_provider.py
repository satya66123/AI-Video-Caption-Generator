"""Ollama translation provider."""

import json
import urllib.error
import urllib.request

from providers.translation_provider import TranslationProvider


class OllamaTranslationProvider(TranslationProvider):
    """Translate captions using a local Ollama model."""

    def __init__(
        self,
        model: str = "qwen2.5:1.5b",
        base_url: str = "http://localhost:11434",
    ) -> None:
        """Initialize the Ollama provider."""
        self.model = model
        self.base_url = base_url.rstrip("/")

    def translate(
        self,
        text: str,
        target_language: str,
    ) -> str:
        """Translate text using Ollama."""
        if not text.strip():
            raise ValueError("Text cannot be empty.")

        if not target_language.strip():
            raise ValueError("Target language cannot be empty.")

        prompt = (
            f"Translate the following text into {target_language}. "
            "Return only the translation. "
            "Do not add explanations, notes, quotes, or commentary.\n\n"
            f"Text:\n{text}"
        )

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        request = urllib.request.Request(
            f"{self.base_url}/api/generate",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(request) as response:
                result = json.loads(
                    response.read().decode("utf-8")
                )
        except urllib.error.URLError as exc:
            raise RuntimeError(
                "Unable to connect to Ollama."
            ) from exc

        translated_text = result.get("response", "").strip()

        if not translated_text:
            raise RuntimeError(
                "Ollama returned an empty translation."
            )

        return translated_text