[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Configuration

## Caption Configuration

The application defines:

```text
SUPPORTED_CAPTION_FORMATS = srt, vtt
DEFAULT_CAPTION_FORMAT = srt
DEFAULT_CAPTION_LANGUAGE = en
```

## Supported Languages

```text
en  English
te  Telugu
hi  Hindi
ta  Tamil
kn  Kannada
ml  Malayalam
bn  Bengali
mr  Marathi
gu  Gujarati
pa  Punjabi
```

## Whisper

Available model choices in Settings:

```text
tiny
base
small
medium
large
```

The current Settings page defaults to `base`.

## Ollama

Default translation model:

```text
translategemma:12b
```

Default local endpoint:

```text
http://localhost:11434
```

## Directories

```text
uploads/
captions/
outputs/
```

## Session Settings

Streamlit session state stores:

```text
whisper_model
ollama_model
default_caption_language
```

## Environment

Install Python dependencies using:

```powershell
pip install -r requirements.txt
```
