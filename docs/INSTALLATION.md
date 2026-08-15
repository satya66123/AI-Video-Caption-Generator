[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Installation Guide

## Prerequisites

Install:

- Python 3.11
- FFmpeg
- Ollama

## Clone

```powershell
git clone https://github.com/satya66123/AI-Video-Caption-Generator.git
cd AI-Video-Caption-Generator
```

## Virtual Environment

```powershell
python -m venv .venv
.venv\Scripts\activate
```

## Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Verify Python

```powershell
python --version
```

## Verify FFmpeg

```powershell
ffmpeg -version
```

## Verify Ollama

```powershell
ollama --version
ollama list
```

## Install Translation Model

```powershell
ollama pull translategemma:12b
```

## Start Application

```powershell
streamlit run app.py
```

## Run Tests

```powershell
pytest -v
```
