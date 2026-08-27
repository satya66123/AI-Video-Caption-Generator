[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![PyTest](https://img.shields.io/badge/tests-267%20passed-brightgreen.svg)](https://pytest.org/)
[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![OpenAI](https://img.shields.io/badge/AI-OpenAI-412991.svg)](https://openai.com/)
[![Anthropic](https://img.shields.io/badge/AI-Anthropic-orange.svg)](https://www.anthropic.com/)
[![Gemini](https://img.shields.io/badge/AI-Gemini-4285F4.svg)](https://ai.google.dev/)
[![Mistral](https://img.shields.io/badge/AI-Mistral-orange.svg)](https://mistral.ai/)
[![Groq](https://img.shields.io/badge/AI-Groq-black.svg)](https://groq.com/)
[![Cohere](https://img.shields.io/badge/AI-Cohere-purple.svg)](https://cohere.com/)
[![DeepSeek](https://img.shields.io/badge/AI-DeepSeek-blue.svg)](https://www.deepseek.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Nekkanti%20Satya%20Srinath-black.svg)](https://github.com/satya66123)

# Contributing

## Setup

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```powershell
streamlit run app.py
```

## Test

```powershell
pytest -v
```

## Development Rules

- Keep workflow coordination in agents.
- Keep reusable business logic in services.
- Keep replaceable integrations behind providers.
- Validate user input.
- Add tests for new functionality.
- Avoid unrelated refactoring in feature changes.

## Pull Requests

Include:

- summary
- motivation
- implementation details
- tests
- test result
- screenshots for UI changes when useful

## Commit Examples

```text
feat: add caption export
fix: handle Ollama connection error
test: add dashboard coverage
docs: update user guide
ci: update GitHub Actions
```
