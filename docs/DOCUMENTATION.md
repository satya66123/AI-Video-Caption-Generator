[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Complete Documentation

## Project

AI Video Caption Generator

## Purpose

Generate multilingual captions from videos and create a separate permanently captioned video.

## Workflow

```text
Upload → Transcribe → Detect Language → Select Language
→ Translate → SRT/VTT → Burn Captions → Final Video
```

## Outputs

Every successful caption workflow can produce:

- original video
- SRT file
- VTT file
- captioned video

## Technology

- Python 3.11
- Streamlit
- OpenAI Whisper
- Ollama
- TranslateGemma
- FFmpeg
- PyTest
- GitHub Actions

## UI

- Dashboard
- Caption Generator
- Captions
- Settings
- Help
- About

## Testing

Final verified automated test baseline:

```text
145 passed
0 failed
```

Manual end-to-end testing also confirmed the expected media outputs.
