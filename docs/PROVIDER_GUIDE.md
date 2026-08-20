# 🤖 AI Translation Provider Guide

[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-217%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![OpenAI](https://img.shields.io/badge/AI-OpenAI-412991.svg)](https://openai.com/)
[![Anthropic](https://img.shields.io/badge/AI-Anthropic-orange.svg)](https://www.anthropic.com/)
[![Gemini](https://img.shields.io/badge/AI-Gemini-4285F4.svg)](https://ai.google.dev/)
[![Mistral](https://img.shields.io/badge/AI-Mistral-orange.svg)](https://mistral.ai/)
[![Groq](https://img.shields.io/badge/AI-Groq-black.svg)](https://groq.com/)
[![Cohere](https://img.shields.io/badge/AI-Cohere-purple.svg)](https://cohere.com/)
[![DeepSeek](https://img.shields.io/badge/AI-DeepSeek-blue.svg)](https://www.deepseek.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

### 🤖 AI Translation Provider Guide

## 📌 Overview

AI Video Caption Generator uses a provider-based architecture for caption translation.

The application separates caption generation from the underlying AI provider. This allows different AI providers to be selected without changing the core caption-generation workflow.

### Current Stable Version

```text
v1.3.0
````

### Supported Providers

```text
1. Ollama
2. OpenAI
3. Anthropic
4. Gemini
5. Mistral
6. Groq
7. Cohere
8. DeepSeek
```

---

# 🏗️ Provider Architecture

Translation is abstracted through the common `TranslationProvider` interface.

```python
from abc import ABC, abstractmethod


class TranslationProvider(ABC):
    """Base interface for translation providers."""

    @abstractmethod
    def translate(
        self,
        text: str,
        target_language: str,
    ) -> str:
        """Translate text into the target language."""
        ...
```

Every provider implements:

```python
translate(
    text: str,
    target_language: str,
) -> str
```

The provider must return the translated text as a string.

---

# 🔀 Translation Provider Factory

The application uses `TranslationProviderFactory` to create providers.

```python
TranslationProviderFactory.create(
    provider,
    **kwargs,
)
```

Supported provider names:

```text
ollama
openai
anthropic
gemini
mistral
groq
cohere
deepseek
```

### Architecture

```text
                         TranslationProviderFactory
                                    │
          ┌─────────────┬───────────┼─────────────┐
          │             │           │             │
       Ollama         OpenAI     Anthropic      Gemini
          │             │           │             │
          └─────────────┴───────────┼─────────────┘
                                    │
          ┌─────────────┬───────────┼─────────────┐
          │             │           │             │
       Mistral         Groq       Cohere       DeepSeek
          │             │           │             │
          └─────────────┴───────────┼─────────────┘
                                    ↓
                             Translated Text
```

---

# 🌐 Supported Providers

| Provider  | Default Model           | Type      | API Key             |
| --------- | ----------------------- | --------- | ------------------- |
| Ollama    | `qwen2.5:1.5b`          | Local     | Not required        |
| OpenAI    | `gpt-5-mini`            | Cloud API | `OPENAI_API_KEY`    |
| Anthropic | `claude-sonnet-4-5`     | Cloud API | `ANTHROPIC_API_KEY` |
| Gemini    | `gemini-3.6-flash`      | Cloud API | `GEMINI_API_KEY`    |
| Mistral   | `mistral-medium-latest` | Cloud API | `MISTRAL_API_KEY`   |
| Groq      | `llama-3.1-8b-instant`  | Cloud API | `GROQ_API_KEY`      |
| Cohere    | `command-a-03-2025`     | Cloud API | `COHERE_API_KEY`    |
| DeepSeek  | `deepseek-v4-flash`     | Cloud API | `DEEPSEEK_API_KEY`  |

---

# 🦙 1. Ollama Provider

The Ollama provider uses a locally running Ollama server.

## Endpoint

```text
http://localhost:11434
```

## Default Model

```text
qwen2.5:1.5b
```

## Configuration

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_TRANSLATION_MODEL=qwen2.5:1.5b
```

## API Key

No cloud API key is required.

## Architecture

```text
Application
     ↓
OllamaTranslationProvider
     ↓
Local Ollama Server
     ↓
qwen2.5:1.5b
     ↓
Translation
```

## Advantages

* Local processing
* No cloud API key
* Suitable for local-first workflows
* No external translation API required

---

# 🟢 2. OpenAI Provider

The OpenAI provider uses the OpenAI API.

## Default Model

```text
gpt-5-mini
```

## Environment Variable

```env
OPENAI_API_KEY=
```

## Architecture

```text
Application
     ↓
OpenAITranslationProvider
     ↓
OpenAI API
     ↓
gpt-5-mini
     ↓
Translation
```

## Implementation Pattern

The provider uses the OpenAI client and sends a translation instruction requesting only the translated result.

---

# 🟣 3. Anthropic Provider

The Anthropic provider uses the Anthropic API.

## Default Model

```text
claude-sonnet-4-5
```

## Environment Variable

```env
ANTHROPIC_API_KEY=
```

## Architecture

```text
Application
     ↓
AnthropicTranslationProvider
     ↓
Anthropic API
     ↓
claude-sonnet-4-5
     ↓
Translation
```

---

# 🔵 4. Gemini Provider

The Gemini provider uses the Google Gemini API.

## Default Model

```text
gemini-3.6-flash
```

## Environment Variable

```env
GEMINI_API_KEY=
```

## Architecture

```text
Application
     ↓
GeminiTranslationProvider
     ↓
Gemini API
     ↓
gemini-3.6-flash
     ↓
Translation
```

---

# 🟠 5. Mistral Provider

Mistral was added as part of the v1.3.0 provider expansion.

## Default Model

```text
mistral-medium-latest
```

## Environment Variable

```env
MISTRAL_API_KEY=
```

## Architecture

```text
Application
     ↓
MistralTranslationProvider
     ↓
Mistral API
     ↓
mistral-medium-latest
     ↓
Translation
```

## Provider Requirements

The Mistral provider:

* validates source text
* validates target language
* sends translation requests
* extracts the translation
* rejects empty responses

---

# ⚡ 6. Groq Provider

Groq was added as part of the v1.3.0 provider expansion.

## Default Model

```text
llama-3.1-8b-instant
```

## Environment Variable

```env
GROQ_API_KEY=
```

## Architecture

```text
Application
     ↓
GroqTranslationProvider
     ↓
Groq API
     ↓
llama-3.1-8b-instant
     ↓
Translation
```

## Provider Requirements

The Groq provider:

* validates source text
* validates target language
* sends translation requests
* extracts the translation
* rejects empty responses

---

# 🟪 7. Cohere Provider

Cohere was added as part of the v1.3.0 provider expansion.

## Default Model

```text
command-a-03-2025
```

## Environment Variable

```env
COHERE_API_KEY=
```

## Architecture

```text
Application
     ↓
CohereTranslationProvider
     ↓
Cohere API
     ↓
command-a-03-2025
     ↓
Translation
```

## Provider Requirements

The Cohere provider:

* validates source text
* validates target language
* sends translation requests
* extracts the translation
* rejects empty responses

---

# 🔷 8. DeepSeek Provider

DeepSeek was added as part of the v1.3.0 provider expansion.

## Default Model

```text
deepseek-v4-flash
```

## Environment Variable

```env
DEEPSEEK_API_KEY=
```

## Architecture

```text
Application
     ↓
DeepSeekTranslationProvider
     ↓
DeepSeek API
     ↓
deepseek-v4-flash
     ↓
Translation
```

## Provider Requirements

The DeepSeek provider:

* validates source text
* validates target language
* sends translation requests
* extracts the translation
* rejects empty responses

---

# 📝 Translation Request

All providers follow the same conceptual translation contract.

```python
provider.translate(
    text,
    target_language,
)
```

Example:

```python
result = provider.translate(
    "Hello world",
    "Telugu",
)
```

Expected behavior:

```text
Input:
Hello world

Target:
Telugu

Output:
[Translated Telugu text]
```

Providers should return only the translation and avoid unnecessary commentary.

---

# ✅ Input Validation

The provider layer validates translation input.

## Empty Source Text

```python
provider.translate(
    "",
    "Telugu",
)
```

Raises:

```text
ValueError
```

with:

```text
Text cannot be empty.
```

## Whitespace Source Text

```python
provider.translate(
    "   ",
    "Telugu",
)
```

Also raises:

```text
ValueError
```

## Empty Target Language

```python
provider.translate(
    "Hello",
    "",
)
```

Raises:

```text
ValueError
```

with:

```text
Target language cannot be empty.
```

## Whitespace Target Language

```python
provider.translate(
    "Hello",
    "   ",
)
```

Also raises:

```text
ValueError
```

---

# 🚨 Empty Response Handling

Providers must reject empty AI responses.

Example:

```python
result = ""
```

The provider raises a runtime error such as:

```text
<Provider> returned an empty translation.
```

This prevents empty caption output from silently entering the caption-generation pipeline.

---

# 🔐 API Key Configuration

Cloud provider API keys are loaded from environment variables.

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
MISTRAL_API_KEY=
GROQ_API_KEY=
COHERE_API_KEY=
DEEPSEEK_API_KEY=
```

Ollama does not require a cloud API key.

## Security

Never place real API keys directly into source code.

Do not commit:

```env
OPENAI_API_KEY=real-key
ANTHROPIC_API_KEY=real-key
GEMINI_API_KEY=real-key
MISTRAL_API_KEY=real-key
GROQ_API_KEY=real-key
COHERE_API_KEY=real-key
DEEPSEEK_API_KEY=real-key
```

Use `.env` or environment variables instead.

---

# ⚙️ Settings Integration

The Settings page exposes all supported providers.

```text
🤖 Translation Provider

Ollama
OpenAI
Anthropic
Gemini
Mistral
Groq
Cohere
DeepSeek
```

The selected provider is stored in:

```python
st.session_state["translation_provider"]
```

The selected model is stored in:

```python
st.session_state["translation_model"]
```

Example:

```python
st.session_state["translation_provider"] = "mistral"

st.session_state["translation_model"] = (
    "mistral-medium-latest"
)
```

---

# 🧭 Sidebar Integration

The sidebar allows the user to select the active translation provider.

```text
Sidebar
   ↓
AI Provider
   ↓
Model
   ↓
Session State
   ↓
Caption Agent
   ↓
Translation Provider Factory
```

The selected provider is used by the caption-generation workflow.

---

# 🔀 Provider Selection Flow

```text
User selects provider
        ↓
Provider name normalized
        ↓
TranslationProviderFactory
        ↓
Provider instance created
        ↓
CaptionGenerationService
        ↓
translate()
        ↓
Translated caption text
```

---

# 🏭 Translation Provider Factory Example

```python
from providers.translation_provider_factory import (
    TranslationProviderFactory,
)

provider = TranslationProviderFactory.create(
    "mistral",
    api_key="...",
)
```

The factory supports:

```python
TranslationProviderFactory.create("ollama")
TranslationProviderFactory.create("openai")
TranslationProviderFactory.create("anthropic")
TranslationProviderFactory.create("gemini")
TranslationProviderFactory.create("mistral")
TranslationProviderFactory.create("groq")
TranslationProviderFactory.create("cohere")
TranslationProviderFactory.create("deepseek")
```

---

# 🧪 Provider Testing

Each provider has dedicated automated tests.

## v1.3.0 New Provider Tests

```text
Mistral
    7 passed

Groq
    7 passed

Cohere
    7 passed

DeepSeek
    7 passed
```

## Factory Tests

```text
15 passed
```

## Settings Tests

```text
34 passed
```

## Complete Project Suite

```text
217 passed
0 failed
```

### Test Status

```text
╔════════════════════════════════════╗
║        v1.3.0 TEST STATUS          ║
╠════════════════════════════════════╣
║ Tests Passed       : 217           ║
║ Tests Failed       : 0             ║
║ Pass Rate          : 100%          ║
║ Status             : PASS ✅       ║
╚════════════════════════════════════╝
```

---

# 🔄 GitHub Actions

Provider tests are included in the project's automated CI pipeline.

```text
GitHub Push
     ↓
GitHub Actions
     ↓
Python 3.11
     ↓
Install Dependencies
     ↓
Run PyTest
     ↓
217 Tests
     ↓
PASS ✅
```

---

# 🧩 Provider File Structure

The provider architecture is organized as:

```text
providers/
│
├── translation_provider.py
│
├── ollama_translation_provider.py
├── openai_translation_provider.py
├── anthropic_translation_provider.py
├── gemini_translation_provider.py
│
├── mistral_translation_provider.py
├── groq_translation_provider.py
├── cohere_translation_provider.py
├── deepseek_translation_provider.py
│
└── translation_provider_factory.py
```

Tests:

```text
tests/
│
├── test_ollama_translation_provider.py
├── test_openai_translation_provider.py
├── test_anthropic_translation_provider.py
├── test_gemini_translation_provider.py
│
├── test_mistral_translation_provider.py
├── test_groq_translation_provider.py
├── test_cohere_translation_provider.py
├── test_deepseek_translation_provider.py
│
├── test_translation_provider_factory.py
└── test_settings_agent.py
```

---

# 🔌 Adding a New Provider

A future provider should implement the `TranslationProvider` interface.

Example:

```python
from providers.translation_provider import (
    TranslationProvider,
)


class NewTranslationProvider(
    TranslationProvider,
):
    """Translate captions using a new AI provider."""

    def __init__(
        self,
        model: str,
        api_key: str | None = None,
    ) -> None:
        ...

    def translate(
        self,
        text: str,
        target_language: str,
    ) -> str:
        ...
```

The implementation should:

1. Validate source text.
2. Validate target language.
3. Call the provider API.
4. Extract the translated text.
5. Reject empty responses.
6. Return the translated string.

---

# 🛠️ Adding the Provider to the Factory

After creating a provider, add its import:

```python
from providers.new_translation_provider import (
    NewTranslationProvider,
)
```

Add the provider name to:

```python
SUPPORTED_PROVIDERS
```

Then add the provider creation logic.

Example:

```python
if normalized_provider == "newprovider":
    return NewTranslationProvider(
        **kwargs,
    )
```

---

# ⚙️ Adding the Provider to Settings

Add the provider configuration:

```python
"NewProvider": {
    "key": "newprovider",
    "model": "default-model",
    "environment_variable": "NEWPROVIDER_API_KEY",
},
```

The Settings page can then display:

```text
NewProvider
default-model
API key status
```

---

# 🧪 Testing a New Provider

Every new provider should have tests for at least:

```text
Provider initialization
Successful translation
Empty source text
Whitespace source text
Empty target language
Whitespace target language
Empty provider response
```

Expected baseline:

```text
7 tests
7 passed
```

---

# 📊 Provider Evolution

| Version | Supported Providers                                                |
| ------- | ------------------------------------------------------------------ |
| v1.0.0  | Ollama                                                             |
| v1.1.0  | Ollama, OpenAI, Anthropic, Gemini                                  |
| v1.3.0  | Ollama, OpenAI, Anthropic, Gemini, Mistral, Groq, Cohere, DeepSeek |

---

# 🎯 Design Principles

The provider architecture follows these principles:

### 1. Separation of Concerns

Provider-specific API logic stays inside provider classes.

### 2. Common Interface

All providers implement:

```python
translate(
    text,
    target_language,
)
```

### 3. Factory-Based Creation

The factory creates providers without requiring the rest of the application to know provider-specific implementation details.

### 4. Configuration Through Environment

Cloud credentials are loaded from environment variables.

### 5. Local-First Option

Ollama provides a local translation option without requiring a cloud API.

### 6. Testability

Provider implementations can be tested independently using mocked API clients.

### 7. Extensibility

New providers can be added without rewriting the core caption-generation service.

---

# 🏆 v1.3.0 Status

```text
Version
    v1.3.0

Providers
    8 supported

New Providers
    Mistral
    Groq
    Cohere
    DeepSeek

Automated Tests
    217 passed

Failed Tests
    0

Pass Rate
    100%

Status
    STABLE ✅
```

---

# 📜 Version History

## v1.0.0

Core caption-generation release.

```text
Video
 ↓
Whisper
 ↓
Language Detection
 ↓
Ollama
 ↓
SRT / VTT
 ↓
FFmpeg
 ↓
Captioned Video
```

---

## v1.1.0

Multi-provider translation architecture introduced.

```text
Ollama
OpenAI
Anthropic
Gemini
```

---

## v1.3.0

Expanded provider architecture.

```text
Ollama
OpenAI
Anthropic
Gemini
Mistral
Groq
Cohere
DeepSeek
```

```text
217 tests passed
100% pass rate
Stable ✅
```

---

# 📌 Summary

AI Video Caption Generator v1.3.0 provides a flexible, extensible translation-provider architecture supporting:

```text
┌───────────────────────────────────────────┐
│           AI TRANSLATION LAYER            │
├───────────────────────────────────────────┤
│ Ollama                                    │
│ OpenAI                                    │
│ Anthropic                                 │
│ Gemini                                    │
│ Mistral                                   │
│ Groq                                      │
│ Cohere                                    │
│ DeepSeek                                  │
└───────────────────────────────────────────┘
                     ↓
             TranslationProvider
                     ↓
          Caption Generation Service
                     ↓
                SRT / VTT
                     ↓
                  FFmpeg
                     ↓
              Captioned Video
```

**v1.3.0 — 8 AI Translation Providers — 217 Tests Passing — Stable ✅**
