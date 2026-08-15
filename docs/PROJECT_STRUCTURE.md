[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Project Structure

```text
AI-Video-Caption-Generator/
│
├── .github/
│   └── workflows/
│       └── python-app.yml
│
├── agents/
├── config/
├── core/
├── pages/
├── providers/
├── services/
├── utils/
├── tests/
│
├── uploads/
├── captions/
├── outputs/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── RELEASE_NOTES.md
└── docs/
```

## Directory Responsibilities

### agents/
Workflow coordination.

### config/
Application constants and supported caption configuration.

### core/
Domain models.

### pages/
Streamlit pages.

### providers/
External/replaceable provider implementations.

### services/
Reusable processing logic.

### utils/
Utility and validation functions.

### tests/
Automated tests.

### uploads/
Original videos.

### captions/
SRT/VTT files.

### outputs/
Captioned videos.
