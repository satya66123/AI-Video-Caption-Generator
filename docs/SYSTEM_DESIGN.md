[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# System Design

## Goal

Transform a video into multilingual subtitle files and a permanently captioned output while preserving the original.

## Components

```text
Streamlit
  ↓
Caption Agent
  ↓
Transcript / Language Detection Services
  ↓
Caption Generation Service
  ↓
Translation Provider
  ↓
SRT / VTT
  ↓
FFmpeg
```

## Inputs

A supported video file.

## Outputs

- Original video
- SRT
- VTT
- Captioned video

## State

Settings are held in Streamlit session state.

## Failure Boundaries

Explicit errors are returned for invalid input, missing dependencies, unavailable Ollama and invalid processing state.

## Scalability Direction

Future batch processing could introduce a job layer while preserving the current agent/service/provider boundaries.
