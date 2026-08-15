[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Troubleshooting

## Ollama Connection Error

Run:

```powershell
ollama --version
ollama list
ollama serve
```

Confirm the Ollama service is available at the configured local endpoint.

## Missing Translation Model

```powershell
ollama pull translategemma:12b
```

## FFmpeg Not Found

```powershell
ffmpeg -version
```

Ensure FFmpeg is installed and available on PATH.

## Transcript Service Not Configured

Configure the transcript service before invoking the caption workflow.

## Caption Generation Service Not Configured

Configure the caption-generation dependency before translation.

## Empty Translation

Verify that the selected Ollama model returns a non-empty response.

## Unsupported Caption Language

Select a language from the configured supported-language list.

## No Caption Segments

Verify that transcription produced timestamped segments.

## Tests Failing

Activate the virtual environment and reinstall dependencies:

```powershell
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

## Recent Files Showing Unexpected Entries

The dashboard intentionally excludes `.gitkeep`. Generated files are read from the configured upload, caption and output directories.
