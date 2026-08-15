[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# User Guide

## 1. Start the Application

```powershell
streamlit run app.py
```

## 2. Open the Caption Generator

Use the sidebar to open the main caption workflow.

## 3. Upload a Video

Choose a supported video:

- MP4
- MOV
- AVI
- MKV
- WebM

## 4. Save the Original

The source video is preserved locally.

## 5. Detect Language

The application detects the spoken language.

## 6. Select Caption Language

Choose a supported target language.

## 7. Generate Captions

The application prepares timestamped caption segments and translates them when required.

## 8. Export Captions

Generate:

- SRT
- VTT

## 9. Burn Captions

Use FFmpeg to permanently burn the selected captions into a separate video.

## 10. Review Outputs

Expected files:

```text
uploads/   → original video
captions/  → SRT / VTT
outputs/   → captioned video
```

## 11. Dashboard

Review counts and recent files.

## 12. Settings

Configure Whisper model, Ollama model and default caption language.

## 13. Help

Use the Help page for troubleshooting Ollama, TranslateGemma and FFmpeg.
