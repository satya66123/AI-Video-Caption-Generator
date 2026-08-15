[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Interview Answers

## Tell me about the project.

I built a local-first AI Video Caption Generator using Python and Streamlit. It accepts a video, performs timestamped Whisper transcription, detects the spoken language, translates caption segments using local Ollama/TranslateGemma, exports SRT/VTT and uses FFmpeg to create a separate permanently captioned video.

## Why local AI?

The design reduces dependence on hosted APIs and keeps the core translation workflow local.

## How did you design translation?

I introduced a TranslationProvider abstraction. The caption-generation service depends on the interface, while Ollama is one concrete implementation.

## How did you preserve source media?

The original video is stored separately under `uploads/`; generated captioned videos are written under `outputs/`.

## How did you test it?

I used PyTest across agents, services, providers, utilities and Streamlit pages. The final suite has 145 passing tests, and GitHub Actions runs the suite automatically.

## What was a challenging issue?

Streamlit page tests initially required careful mocking because `st.columns()` is used as a context manager. The tests were aligned with actual Streamlit behavior.

## What would you build next?

A caption editor, batch processing, styling controls and additional translation providers are logical future enhancements.
