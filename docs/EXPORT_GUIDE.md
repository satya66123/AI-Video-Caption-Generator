[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Export Guide

## SRT Export

SRT is a widely supported subtitle format.

A typical structure is:

```text
1
00:00:01,000 --> 00:00:03,500
Caption text
```

## VTT Export

VTT is commonly used by web video systems.

Example:

```text
WEBVTT

00:00:01.000 --> 00:00:03.500
Caption text
```

## Captioned Video

The selected captions can be permanently burned into a separate output video using FFmpeg.

## Output Locations

```text
captions/  → SRT and VTT
outputs/   → captioned videos
```

## Original Preservation

The source video remains in `uploads/` and is not overwritten.
