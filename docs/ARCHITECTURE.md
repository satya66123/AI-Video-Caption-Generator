[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Architecture

## Layered Architecture

```text
Streamlit UI
    ↓
Pages / Agents
    ↓
Services
    ↓
Providers
    ↓
Local AI / Media Tools
```

## Main Components

### UI
Streamlit provides the application interface and sidebar navigation.

### Agents
Agents coordinate workflows and page-level application behavior.

### Services
Services contain reusable processing logic.

### Providers
Providers abstract external or replaceable integrations such as translation.

### Core
Core models represent domain objects such as timestamped caption segments.

### Config
Configuration defines supported caption languages and formats.

### Utils
Utilities provide reusable validation and formatting operations.

## Processing Flow

```text
Video
 ↓
Whisper
 ↓
Language Detection
 ↓
Caption Language
 ↓
Translation Provider
 ↓
SRT / VTT
 ↓
FFmpeg
 ↓
Captioned Video
```

## Storage

```text
uploads/
captions/
outputs/
```

The original video is preserved separately from generated output.
