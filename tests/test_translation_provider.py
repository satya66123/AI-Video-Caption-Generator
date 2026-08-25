from unittest.mock import patch

import pytest

from providers.ollama_translation_provider import (
    OllamaTranslationProvider,
)


def test_empty_text_is_rejected() -> None:
    provider = OllamaTranslationProvider()

    with pytest.raises(ValueError):
        provider.translate("", "English")


def test_empty_language_is_rejected() -> None:
    provider = OllamaTranslationProvider()

    with pytest.raises(ValueError):
        provider.translate("Hello", "")


@patch("providers.ollama_translation_provider.urllib.request.urlopen")
def test_ollama_translation(mock_urlopen) -> None:
    mock_response = mock_urlopen.return_value.__enter__.return_value

    mock_response.read.return_value = b'{"response": "Hello everyone"}'

    provider = OllamaTranslationProvider()

    result = provider.translate(
        "Namaskaram andariki",
        "English",
    )

    assert result == "Hello everyone"


def test_default_translation_model() -> None:
    provider = OllamaTranslationProvider()

    assert provider.model == "qwen2.5:1.5b"


@patch("providers.ollama_translation_provider.urllib.request.urlopen")
def test_empty_ollama_response_is_rejected(mock_urlopen) -> None:
    mock_response = mock_urlopen.return_value.__enter__.return_value

    mock_response.read.return_value = b'{"response": ""}'

    provider = OllamaTranslationProvider()

    with pytest.raises(RuntimeError):
        provider.translate(
            "Hello",
            "Telugu",
        )
