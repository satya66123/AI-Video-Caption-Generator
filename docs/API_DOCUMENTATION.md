[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# API Documentation

## Overview

The application is primarily a Streamlit application with internal Python agents, services, providers, models and utilities.

## Core Interfaces

### TranslationProvider

Defines the translation contract:

```python
translate(text: str, target_language: str) -> str
```

Implementations can provide different translation backends without changing the caption-generation service.

### CaptionSegment

Represents one timestamped caption:

```text
start
end
text
```

## CaptionAgent

Main caption workflow coordination responsibilities include:

- selecting and validating caption language
- obtaining internal transcript data
- detecting spoken language
- converting transcript segments into CaptionSegment objects
- preparing caption workflow data

## CaptionGenerationService

Generates translated caption segments from timestamped segments.

Inputs:

- list of CaptionSegment
- target language

Output:

- translated list of CaptionSegment

Validation includes empty target language and empty segment collections.

## OllamaTranslationProvider

Communicates with a local Ollama `/api/generate` endpoint.

Default model:

```text
translategemma:12b
```

## DashboardAgent

Provides:

- video count
- caption-file count
- captioned-video count
- recent-file information

`.gitkeep` files are excluded from recent files.

## Configuration API

Caption configuration defines supported formats, default format, supported languages and default language.

## Error Contracts

The application raises explicit errors for invalid languages, empty translation input, unavailable services, Ollama connection failures and empty translation responses.
