[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Workflow

## Complete Workflow

```text
                 ┌───────────────┐
                 │ Upload Video  │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Save Original │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │    Whisper    │
                 │ Transcription │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │Language Detect│
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │Select Caption │
                 │    Language   │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │Ollama /       │
                 │TranslateGemma │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │   SRT + VTT   │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │    FFmpeg     │
                 │ Caption Burn  │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │ Captioned     │
                 │    Video      │
                 └───────────────┘
```

## Processing Rules

1. Never overwrite the original video.
2. Preserve timestamp information.
3. Validate target language.
4. Use the configured translation provider.
5. Generate standard subtitle formats.
6. Burn captions into a separate output.
7. Keep generated files separated by directory.

## Verified Result

The workflow has been manually executed successfully and produces the expected original, SRT, VTT and captioned-video outputs.
