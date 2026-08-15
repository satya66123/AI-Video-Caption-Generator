[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Provider Guide

## Provider Pattern

Translation is abstracted through:

```python
class TranslationProvider(ABC):
    @abstractmethod
    def translate(self, text: str, target_language: str) -> str:
        ...
```

## Ollama Provider

The current implementation uses a local Ollama server.

Default endpoint:

```text
http://localhost:11434
```

Default model:

```text
translategemma:12b
```

## Request

The provider sends a prompt requesting translation only, without commentary.

## Validation

The provider rejects:

- empty source text
- empty target language

It also rejects empty model responses.

## Connection Errors

Ollama connection failures are converted into a clear runtime error.

## Extending Providers

A future provider should implement the TranslationProvider interface and return a translated string without changing CaptionGenerationService.
