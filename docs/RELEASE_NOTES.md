# 🚀 AI Video Caption Generator — Release Notes

[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Tests](https://img.shields.io/badge/Tests-217%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
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
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# 📌 Stable Releases

| Version | Status | Description |
|---|---|---|
| **v1.0.0** | ✅ Stable | Core video caption generation release |
| **v1.1.0** | ✅ Stable | Multi-provider AI translation release |
| **v1.2.0** | ✅ Stable | Multi-provider AI translation release, transcript save |
| **v1.3.0** | ✅ Stable / Current | Expanded 8-provider AI translation release |

---

# 🎬 Version 1.0.0 — Core Release

**Release Status:** ✅ Stable  
**Release Date:** August 2026  
**Author:** Nekkanti Satya Srinath  
**License:** MIT

## 🎉 Release Overview

AI Video Caption Generator v1.0.0 is the first complete stable release of the application.

This release provides an end-to-end AI-powered video caption workflow that takes an uploaded video, processes its speech, detects the spoken language, generates multilingual captions, exports SRT and VTT files, and permanently burns captions into the final video.

The release is designed around a local-first architecture using Whisper, Ollama, TranslateGemma, and FFmpeg.

## ✨ Major Features

### 🎬 Video Processing

- Upload video files through the Streamlit interface.
- Save the original uploaded video locally.
- Support MP4, MOV, AVI, MKV, and WebM.

### 📝 Transcription

- Timestamped transcription using OpenAI Whisper.
- Timestamp information is preserved for caption generation.
- Transcript data is used as an internal processing artifact.

### 🌐 Language Detection

- Detect the spoken language of the uploaded video.
- Use detected language information during caption processing.

### 💬 Caption Generation

Supported caption languages:

| Code | Language |
|---|---|
| `en` | English |
| `te` | Telugu |
| `hi` | Hindi |
| `ta` | Tamil |
| `kn` | Kannada |
| `ml` | Malayalam |
| `bn` | Bengali |
| `mr` | Marathi |
| `gu` | Gujarati |
| `pa` | Punjabi |

### 🤖 Local AI Translation

- Local Ollama translation provider.
- TranslateGemma support.
- Local-first translation workflow.
- Default v1.0.0 translation model:

```text
translategemma:12b
```

### 📄 Caption Export

The application generates:

- SRT
- VTT

Both formats preserve timestamped caption segments.

### 🔥 Caption Burning

- FFmpeg integration.
- Permanently burn captions into the video.
- Generate a separate captioned output.
- Preserve the original uploaded video.

### 📊 Dashboard

- Total uploaded videos
- Total caption files
- Total captioned videos
- Recent files
- `.gitkeep` files excluded from Recent Files

### 🧭 Application Pages

- 🏠 Dashboard
- 🎬 Caption Generator
- 📄 Captions
- ⚙️ Settings
- ❓ Help
- ℹ️ About

### ⚙️ Settings

Configure:

- Whisper model
- Ollama translation model
- Default caption language

### ❓ Help

Includes:

- Usage instructions
- Supported video formats
- Caption formats
- AI processing information
- Ollama troubleshooting
- TranslateGemma troubleshooting
- FFmpeg troubleshooting

### ℹ️ About

Includes:

- Project overview
- Core workflow
- Technology stack
- Project scope

## 🧪 v1.0.0 Testing

The original v1.0.0 test suite was executed successfully.

```text
153 passed
0 failed
100% pass rate
```

Coverage included:

- Agents
- Services
- Providers
- Caption generation
- Translation
- Language detection
- Caption files
- SRT
- VTT
- FFmpeg video burning
- Dashboard
- Settings
- Help
- About
- Utility functions
- Error handling
- Edge cases

### v1.0.0 Test Badge

[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)

## 🔄 v1.0.0 GitHub Actions

CI workflow:

```text
.github/workflows/python-app.yml
```

Pipeline:

```text
Checkout Repository
        ↓
Python 3.11
        ↓
Install Dependencies
        ↓
Run PyTest
        ↓
153 Tests
        ↓
PASS ✅
```

**GitHub Actions: Passing ✅**

## 🎯 v1.0.0 End-to-End Workflow

```text
🎬 Upload Video
      ↓
💾 Save Original Video
      ↓
📝 Whisper Transcription
      ↓
🌐 Language Detection
      ↓
💬 Caption Language Selection
      ↓
🤖 Local AI Translation
      ↓
📄 Generate SRT
      ↓
📄 Generate VTT
      ↓
🔥 FFmpeg Caption Burn
      ↓
🎥 Captioned Video
      ↓
⬇️ Preview / Download
```

### Verified Outputs

```text
✅ Original video saved
✅ SRT generated
✅ VTT generated
✅ Captioned video generated
```

## 🏗️ v1.0.0 Technology Stack

| Technology | Role |
|---|---|
| Python 3.11 | Application language |
| Streamlit | User interface |
| OpenAI Whisper | Speech transcription |
| Ollama | Local AI runtime |
| TranslateGemma | Caption translation |
| FFmpeg | Video processing |
| PyTest | Automated testing |
| GitHub Actions | Continuous integration |
| Local file storage | Application storage |

## 🔐 v1.0.0 Local-First Architecture

```text
Video
  ↓
Whisper
  ↓
Language Detection
  ↓
Ollama
  ↓
TranslateGemma
  ↓
SRT / VTT
  ↓
FFmpeg
  ↓
Captioned Video
```

No mandatory hosted translation API was required for the v1.0.0 core translation workflow.

## 💾 v1.0.0 Storage

```text
uploads/
    Original videos

captions/
    SRT files
    VTT files

outputs/
    Captioned videos
```

The original video is preserved separately from the captioned output.

---
Absolutely. I verified the published **v1.2.0** release and its current content. The release is correctly positioned as **Multi-Provider + Timestamped Transcript Saving + Single Model per Provider**. ([GitHub][1])

Here is a cleaner, more professional **feature-focused v1.2.0 Release Notes** you can use:

# 🚀 AI Video Caption Generator v1.2.0

[![Version](https://img.shields.io/badge/Version-v1.2.0-blue?style=for-the-badge\&logo=github)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.2.0)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Multi-Provider](https://img.shields.io/badge/AI-Multi--Provider-purple?style=for-the-badge)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Transcript](https://img.shields.io/badge/Transcript-Timestamped%20Save-orange?style=for-the-badge)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet?style=for-the-badge)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green?style=for-the-badge)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://github.com/satya66123/AI-Video-Caption-Generator/blob/main/LICENSE)

## 🎉 Release Overview

**v1.2.0** is an important evolution of the AI Video Caption Generator.

This release combines the existing **multi-provider AI translation architecture** with a new **timestamped transcript-saving system**.

The provider architecture remains intentionally simple:

> **One configured/default model per provider.**

Dynamic multiple-model selection is introduced in **v1.3.0**. ([GitHub][1])

---

# ⭐ What's New

### 🤖 Multi-Provider AI Translation

Continue using multiple AI providers for caption translation:

* 🦙 Ollama
* 🤖 OpenAI
* 🧠 Anthropic
* ✨ Gemini
* 🔥 Mistral
* ⚡ Groq
* 🟣 Cohere
* 🔷 DeepSeek

Each provider uses **one configured/default model** in v1.2.0. ([GitHub][1])

### 📝 Timestamped Transcript Saving

The major new feature in v1.2.0 is **persistent transcript storage**.

Generated Whisper transcripts are automatically saved to:

```text
transcripts/
```

Example:

```text
transcripts/
├── lecture_20260821_162530.txt
├── tutorial_20260821_163102.txt
└── presentation_20260821_170845.txt
```

The timestamped filename prevents previously generated transcripts from being overwritten. ([GitHub][1])

### ⏱️ Whisper Timestamp Preservation

Saved transcripts retain the timestamps generated by Whisper:

```text
0001 | [0000.00 --> 0004.52] Hello everyone...
0002 | [0004.52 --> 0008.91] Today we are going to learn...
0003 | [0008.91 --> 0013.47] Let's get started...
```

This makes transcripts easy to review and reuse. ([GitHub][1])

### ⬇️ Transcript Download

A **Download Transcript** option is available after transcript generation, allowing users to download the generated `.txt` file directly from the application. ([GitHub][1])

---

# 🔄 Complete v1.2.0 Workflow

```text
Upload Video
     ↓
Save Original Video
     ↓
Whisper Transcription
     ↓
Generate Timestamped Transcript
     ↓
Save Transcript
     ↓
Detect Language
     ↓
Select Caption Language
     ↓
Select AI Provider
     ↓
Provider's Default Model
     ↓
Translation Provider Factory
     ↓
Generate SRT + VTT
     ↓
FFmpeg Caption Burn
     ↓
Final Captioned Video
```

---

# 🎯 v1.2.0 Model Architecture

```text
                AI Provider
                     ↓
        Translation Provider Factory
                     ↓
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
    Ollama        OpenAI       Anthropic
       ↓             ↓             ↓
 One Default     One Default   One Default
    Model           Model         Model
```

### Important

v1.2.0 **does not include dynamic model selection**.

The architecture remains:

```text
Provider
   ↓
One Default Model
   ↓
Translation
```

Dynamic:

```text
Provider
   ↓
Multiple Models
   ↓
Select Model
```

is the major feature introduced in **v1.3.0**. ([GitHub][1])

---

# 🎬 Caption Generation Features

v1.2.0 continues to provide:

* 🎙️ Whisper transcription
* 🌐 Automatic language detection
* 🌍 Multilingual translation
* 📄 SRT generation
* 📄 VTT generation
* 🔥 FFmpeg caption burning
* 🎥 Final captioned-video output
* 🛡️ Original video preservation ([GitHub][1])

---

# 🌍 Supported Caption Languages

* 🇬🇧 English
* 🇮🇳 Telugu
* 🇮🇳 Hindi
* 🇮🇳 Tamil
* 🇮🇳 Kannada
* 🇮🇳 Malayalam
* 🇮🇳 Bengali
* 🇮🇳 Marathi
* 🇮🇳 Gujarati
* 🇮🇳 Punjabi ([GitHub][1])

---

# 📁 Generated Files

v1.2.0 adds a dedicated transcript directory:

```text
AI-Video-Caption-Generator/
│
├── uploads/
│   └── original videos
│
├── transcripts/
│   └── timestamped .txt transcripts
│
├── captions/
│   ├── *.srt
│   └── *.vtt
│
└── outputs/
    └── captioned videos
```

The original video remains separate from the captioned output. ([GitHub][1])

---

# 🔐 Provider Configuration

Cloud provider credentials continue to use environment variables:

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
MISTRAL_API_KEY=
GROQ_API_KEY=
COHERE_API_KEY=
DEEPSEEK_API_KEY=
```

API keys remain outside the application UI and are loaded through environment configuration. ([GitHub][1])

---

# 📄 Caption Formats

v1.2.0 supports:

* `.srt` — SubRip Subtitle
* `.vtt` — WebVTT

Both contain timestamped caption segments. ([GitHub][1])

---

# 🔥 FFmpeg Caption Burning

Generated captions can be permanently embedded into the final video:

```text
Original Video
      ↓
Translated Captions
      ↓
    FFmpeg
      ↓
Captioned Video
```

The original uploaded video is preserved separately. ([GitHub][1])

---

# 🆚 v1.1.0 → v1.2.0

| Feature                       | v1.1.0 | v1.2.0 |
| ----------------------------- | :----: | :----: |
| Ollama                        |    ✅   |    ✅   |
| Multi-Provider                |    ✅   |    ✅   |
| One Model per Provider        |    ✅   |    ✅   |
| Provider Selection            |    ✅   |    ✅   |
| Whisper Transcription         |    ✅   |    ✅   |
| Timestamped Transcript Saving |    ❌   |    ✅   |
| `transcripts/` Directory      |    ❌   |    ✅   |
| Transcript Download           |    ❌   |    ✅   |
| SRT Generation                |    ✅   |    ✅   |
| VTT Generation                |    ✅   |    ✅   |
| FFmpeg Burning                |    ✅   |    ✅   |
| Original Video Preservation   |    ✅   |    ✅   |
| Dynamic Multiple Models       |    ❌   |    ❌   |

This accurately reflects the feature progression documented in your published release. ([GitHub][1])

---

# 📈 Release Evolution

```text
v1.0.0
🦙 Ollama
   ↓
One Local Translation Model
   ↓
Core Caption Generator

        ↓

v1.1.0
🤖 Multi-Provider
   ↓
One Default Model per Provider
   ↓
Multi-Provider Translation

        ↓

v1.2.0
🤖 Multi-Provider
   ↓
One Default Model per Provider
   ↓
📝 Timestamped Transcript Saving
   ↓
⬇️ Transcript Download

        ↓

v1.3.0
🤖 Multi-Provider
   ↓
🧠 Multiple Models per Provider
   ↓
🎯 Dynamic Provider + Model Selection
```

---

# 🚀 What's Next — v1.3.0

The next major step after v1.2.0 is **dynamic multi-model support**.

v1.3.0 extends the architecture with:

* 🧠 Multiple models per provider
* 🎯 Dynamic model selection
* 🔄 Provider → Model mapping
* 🤖 Expanded model choices

This progression is also reflected in the project's current release documentation. ([GitHub][1])

---

# 🏆 v1.2.0 Summary

> **🚀 Multi-Provider AI Translation + 📝 Timestamped Transcript Saving + 🎯 Single Model per Provider**

**Version:** `v1.2.0`
**Status:** ✅ Stable
**Major Addition:** 📝 Timestamped Transcript Storage
**Next Evolution:** 🧠 Dynamic Multi-Model Support in v1.3.0

[View the v1.2.0 GitHub Release](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.2.0?utm_source=chatgpt.com)

[1]: https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.2.0 "Release 🚀 AI Video Caption Generator — v1.2.0 · satya66123/AI-Video-Caption-Generator · GitHub"


---

# 🚀 Version 1.3.0 — Expanded Multi-Provider AI Translation

**Release Status:** ✅ Stable  
**Release Date:** August 2026  
**Author:** Nekkanti Satya Srinath  
**License:** MIT

## 🎉 Release Overview

AI Video Caption Generator v1.3.0 expands the v1.1.0 multi-provider architecture from four providers to **eight supported AI translation providers**.

The complete v1.0.0 caption workflow and v1.1.0 provider architecture remain preserved.

```text
v1.0.0 → Core Caption Generation
v1.1.0 → 4 AI Translation Providers
v1.2.0 → Transcript save , 4 AI Translator Providers
v1.3.0 → 8 AI Translation Providers
```

## ✨ v1.3.0 Major Features

### 🤖 Expanded Multi-Provider Translation

| Provider | Default Model | Type |
|---|---|---|
| 🦙 Ollama | `qwen2.5:1.5b` | Local |
| 🟢 OpenAI | `gpt-5-mini` | API |
| 🟣 Anthropic | `claude-sonnet-4-5` | API |
| 🔵 Gemini | `gemini-3.6-flash` | API |
| 🟠 Mistral | `mistral-medium-latest` | API |
| ⚡ Groq | `llama-3.1-8b-instant` | API |
| 🟪 Cohere | `command-a-03-2025` | API |
| 🔷 DeepSeek | `deepseek-v4-flash` | API |

### 🆕 New v1.3.0 Providers

- 🟠 Mistral translation provider
- ⚡ Groq translation provider
- 🟪 Cohere translation provider
- 🔷 DeepSeek translation provider

### 🔌 Translation Provider Factory

The provider factory now supports all eight providers:

```text
Translation Provider Factory
        ↓
┌─────────┬─────────┬───────────┬────────┐
│ Ollama  │ OpenAI  │ Anthropic │ Gemini │
├─────────┼─────────┼───────────┼────────┤
│ Mistral │  Groq  │  Cohere   │DeepSeek│
└─────────┴─────────┴───────────┴────────┘
```

### 🧭 Sidebar Provider Selection

The sidebar supports selecting all eight providers and stores the selected provider and model in Streamlit session state.

```text
AI Provider
     ↓
Provider Selection
     ↓
Default Model
     ↓
Streamlit Session State
     ↓
Translation Provider Factory
     ↓
Translation
```

### ⚙️ Settings Updates

The Settings page now displays all eight providers, their default models, and API-key configuration status.

### 🔐 Environment API Keys

New v1.3.0 cloud-provider environment variables:

```env
MISTRAL_API_KEY=
MISTRAL_TRANSLATION_MODEL=mistral-medium-latest

GROQ_API_KEY=
GROQ_TRANSLATION_MODEL=llama-3.1-8b-instant

COHERE_API_KEY=
COHERE_TRANSLATION_MODEL=command-a-03-2025

DEEPSEEK_API_KEY=
DEEPSEEK_TRANSLATION_MODEL=deepseek-v4-flash
```

API keys are read from the environment and are never displayed in the UI.

### 🧪 v1.3.0 Testing

The complete project test suite passed successfully:

```text
217 passed
0 failed
100% pass rate
```

New provider coverage includes:

```text
Mistral       → 7 tests passed
Groq          → 7 tests passed
Cohere        → 7 tests passed
DeepSeek      → 7 tests passed
Provider Factory → 15 tests passed
Settings Agent  → 34 tests passed
Full Suite      → 217 tests passed
```

### 🔄 v1.3.0 GitHub Actions

The complete test suite is verified through the project's GitHub Actions workflow.

```text
Checkout Repository
        ↓
Python 3.11
        ↓
Install Dependencies
        ↓
Run PyTest
        ↓
217 Tests
        ↓
PASS ✅
```

### 🎯 v1.3.0 End-to-End Workflow

```text
🎬 Upload Video
      ↓
💾 Save Original Video
      ↓
📝 Whisper Transcription
      ↓
🌐 Language Detection
      ↓
💬 Caption Language Selection
      ↓
🤖 Select AI Provider + Model
      ↓
🔀 Translation Provider Factory
      ↓
┌─────────────────────────────────────┐
│ Ollama / OpenAI / Anthropic / Gemini│
│ Mistral / Groq / Cohere / DeepSeek  │
└─────────────────────────────────────┘
      ↓
📄 Generate SRT
      ↓
📄 Generate VTT
      ↓
🔥 FFmpeg Caption Burn
      ↓
🎥 Captioned Video
      ↓
⬇️ Preview / Download
```

## 📦 v1.3.0 Release Contents

```text
providers/
├── translation_provider.py
├── ollama_translation_provider.py
├── openai_translation_provider.py
├── anthropic_translation_provider.py
├── gemini_translation_provider.py
├── mistral_translation_provider.py
├── groq_translation_provider.py
├── cohere_translation_provider.py
├── deepseek_translation_provider.py
└── translation_provider_factory.py
```

Updated:

```text
pages/settings_agent.py
tests/test_settings_agent.py
tests/test_translation_provider_factory.py
app.py
```

---

# 🚀 Version 1.1.0 — Multi-Provider AI Translation

**Release Status:** ✅ Stable / Current  
**Release Date:** August 2026  
**Author:** Nekkanti Satya Srinath  
**License:** MIT

## 🎉 Release Overview

AI Video Caption Generator v1.1.0 extends the stable v1.0.0 core workflow with **multi-provider AI translation support**.

Users can select the translation provider from the application sidebar and the selected provider/model is stored in Streamlit session state and used by the translation provider factory.

The v1.0.0 caption workflow remains intact:

```text
Video → Whisper → Language Detection → Translation → SRT/VTT → FFmpeg → Captioned Video
```

The major v1.1.0 addition is the provider layer:

```text
Ollama
OpenAI
Anthropic
Gemini
```

## ✨ v1.1.0 Major Features

### 🤖 Multi-Provider Translation

| Provider | Default Model | Type |
|---|---|---|
| 🦙 Ollama | `qwen2.5:1.5b` | Local |
| 🟢 OpenAI | `gpt-5-mini` | API |
| 🟣 Anthropic | `claude-sonnet-4-5` | API |
| 🔵 Gemini | `gemini-3.6-flash` | API |

### 🧭 Sidebar Provider Selection

The sidebar now allows the user to select the AI translation provider.

```text
AI Provider
    ↓
Ollama / OpenAI / Anthropic / Gemini
    ↓
Default Model
    ↓
Translation
```

### 🧠 Session State

The selected provider and model are stored in Streamlit session state:

```text
translation_provider
translation_model
```

This allows the application workflow to use the provider selected by the user.

### 🔌 Translation Provider Factory

v1.1.0 introduces a provider factory architecture for selecting the appropriate translation implementation.

```text
Translation Provider Factory
          ↓
 ┌────────┼─────────┬─────────┐
 ↓        ↓         ↓         ↓
Ollama  OpenAI   Anthropic  Gemini
```

### 🔐 API Key Configuration

Cloud provider credentials are read from environment variables.

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
```

Ollama remains local and does not require a cloud API key.

API keys are not displayed in the UI.

### ⚙️ Settings Updates

The Settings page now provides:

- Whisper model selection
- AI provider selection
- Default provider model
- Provider configuration status
- Local Ollama status
- Cloud API-key status
- Default caption language
- Output directory information

## 🧪 v1.1.0 Testing

The complete updated test suite was executed successfully.

```text
177 passed
0 failed
100% pass rate
```

### v1.1.0 Test Badge

[![Tests](https://img.shields.io/badge/Tests-217%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)

### Test Coverage Areas

The updated suite verifies:

- Application pages
- Agents
- Caption agent
- Caption generation service
- Caption storage
- Caption structure
- Caption workflow
- Caption UI
- SRT utilities
- VTT utilities
- Transcript service
- Language detection
- Translation providers
- Translation provider factory
- Video caption burning
- Settings provider selection
- Requirements
- Error handling
- Edge cases

## 🔄 v1.1.0 GitHub Actions

The latest multi-provider commit is:

```text
6499068
feat: add multi-provider translation settings
```

GitHub Actions successfully executed the Python test workflow.

```text
Workflow: Python Tests
Branch: main
Commit: 6499068
Status: PASS ✅
```

CI pipeline:

```text
Checkout Repository
        ↓
Python 3.11
        ↓
Install Dependencies
        ↓
Run PyTest
        ↓
177 Tests
        ↓
PASS ✅
```

**GitHub Actions: Passing ✅**

## 🎯 v1.1.0 End-to-End Workflow

```text
🎬 Upload Video
      ↓
💾 Save Original Video
      ↓
📝 Whisper Transcription
      ↓
🌐 Language Detection
      ↓
💬 Caption Language Selection
      ↓
🤖 Select AI Provider
      ↓
🔀 Translation Provider Factory
      ↓
┌────────────┬────────────┬────────────┐
↓            ↓            ↓            ↓
Ollama      OpenAI     Anthropic     Gemini
↓            ↓            ↓            ↓
└────────────┴────────────┴────────────┘
                    ↓
              📄 Generate SRT
                    ↓
              📄 Generate VTT
                    ↓
            🔥 FFmpeg Caption Burn
                    ↓
             🎥 Captioned Video
                    ↓
              ⬇️ Preview / Download
```

## ✅ v1.1.0 Manual Provider Verification

All four providers were manually tested through the actual application UI.

```text
🦙 Ollama
   qwen2.5:1.5b
   ✅ Translation
   ✅ SRT
   ✅ VTT
   ✅ Captioned video
   ✅ Original video preserved

🟢 OpenAI
   gpt-5-mini
   ✅ Translation
   ✅ SRT
   ✅ VTT
   ✅ Captioned video
   ✅ Original video preserved

🟣 Anthropic
   claude-sonnet-4-5
   ✅ Translation
   ✅ SRT
   ✅ VTT
   ✅ Captioned video
   ✅ Original video preserved

🔵 Gemini
   gemini-3.6-flash
   ✅ Translation
   ✅ SRT
   ✅ VTT
   ✅ Captioned video
   ✅ Original video preserved
```

### Final v1.1.0 Verification

```text
177 passed
0 failed
100% automated test pass rate

4 / 4 providers manually verified
GitHub Actions: PASS
End-to-end workflow: PASS
```

## 🏗️ v1.1.0 Technology Stack

| Technology | Role |
|---|---|
| Python 3.11 | Application language |
| Streamlit | User interface |
| OpenAI Whisper | Speech transcription |
| Ollama | Local AI translation |
| OpenAI | Cloud AI translation |
| Anthropic | Cloud AI translation |
| Gemini | Cloud AI translation |
| FFmpeg | Video processing |
| PyTest | Automated testing |
| GitHub Actions | Continuous integration |
| Local file storage | Application storage |

## 🔌 v1.1.0 Provider Architecture

```text
                    Streamlit Sidebar
                           ↓
                 Selected Provider/Model
                           ↓
                 Streamlit Session State
                           ↓
              Translation Provider Factory
                           ↓
        ┌──────────┬──────────┬──────────┬──────────┐
        ↓          ↓          ↓          ↓
     Ollama      OpenAI    Anthropic   Gemini
        ↓          ↓          ↓          ↓
        └──────────┴──────────┴──────────┘
                           ↓
                 Caption Generation
                           ↓
                      SRT / VTT
                           ↓
                       FFmpeg
                           ↓
                   Captioned Video
```

## 🔐 v1.1.0 Environment Configuration

Use a local `.env` file.

Example:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_TRANSLATION_MODEL=qwen2.5:1.5b

OPENAI_API_KEY=
OPENAI_TRANSLATION_MODEL=gpt-5-mini

ANTHROPIC_API_KEY=
ANTHROPIC_TRANSLATION_MODEL=claude-sonnet-4-5

GEMINI_API_KEY=
GEMINI_TRANSLATION_MODEL=gemini-3.6-flash

DEFAULT_TRANSLATION_PROVIDER=ollama
DEFAULT_CAPTION_LANGUAGE=en
```

**Never commit real API keys to GitHub.**

## 📦 v1.1.0 Release Contents

```text
app.py
agents/
config/
core/
pages/
providers/
services/
utils/
tests/
.github/workflows/
requirements.txt
README.md
LICENSE
RELEASE_NOTES.md
```

### New / Updated v1.1.0 Provider Files

```text
providers/
├── translation_provider.py
├── ollama_translation_provider.py
├── openai_translation_provider.py
├── anthropic_translation_provider.py
├── gemini_translation_provider.py
└── translation_provider_factory.py
```

Updated settings/testing files include:

```text
pages/settings_agent.py
tests/test_settings_agent.py
tests/test_translation_provider_factory.py
```

---

# 📊 Release Comparison

| Capability | v1.0.0 | v1.1.0 | v1.3.0 |
|---|---:|---:|---:|
| Video upload | ✅ | ✅ | ✅ |
| Original video preservation | ✅ | ✅ | ✅ |
| Whisper transcription | ✅ | ✅ | ✅ |
| Language detection | ✅ | ✅ | ✅ |
| SRT generation | ✅ | ✅ | ✅ |
| VTT generation | ✅ | ✅ | ✅ |
| FFmpeg caption burning | ✅ | ✅ | ✅ |
| Captioned video output | ✅ | ✅ | ✅ |
| Dashboard | ✅ | ✅ | ✅ |
| Settings | ✅ | ✅ | ✅ |
| Help | ✅ | ✅ | ✅ |
| About | ✅ | ✅ | ✅ |
| Ollama translation | ✅ | ✅ | ✅ |
| OpenAI translation | ❌ | ✅ | ✅ |
| Anthropic translation | ❌ | ✅ | ✅ |
| Gemini translation | ❌ | ✅ | ✅ |
| Mistral translation | ❌ | ❌ | ✅ |
| Groq translation | ❌ | ❌ | ✅ |
| Cohere translation | ❌ | ❌ | ✅ |
| DeepSeek translation | ❌ | ❌ | ✅ |
| Sidebar provider selection | ❌ | ✅ | ✅ |
| Translation Provider Factory | ❌ | ✅ | ✅ |
| Environment API-key handling | ❌ | ✅ | ✅ |
| Automated tests | 153 | 177 | **217** |
| GitHub Actions | ✅ | ✅ | ✅ |
| Manual provider verification | Core workflow | 4 / 4 | New providers tested |

---

# 🐛 Reliability and Error Handling

The stable releases validate and handle:

- Empty caption text
- Empty target language
- Unsupported caption language
- Missing transcript service
- Missing caption generation service
- Ollama connection failures
- Empty Ollama responses
- Missing caption segments
- Invalid caption processing states
- Missing cloud provider API keys
- Unknown translation provider
- Provider selection/session-state handling

---

# 📌 Project Status

## v1.0.0

[![Version](https://img.shields.io/badge/Version-v1.0.0-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.0.0)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)

**Core Release: Stable ✅**

- ✅ Core application complete
- ✅ End-to-end workflow verified
- ✅ Original video saving verified
- ✅ SRT generation verified
- ✅ VTT generation verified
- ✅ Captioned video generation verified
- ✅ All pages complete
- ✅ 153 automated tests passing
- ✅ GitHub Actions passing
- ✅ Manual end-to-end testing complete

## v1.1.0

[![Version](https://img.shields.io/badge/Version-v1.1.0-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.1.0)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Tests](https://img.shields.io/badge/Tests-217%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)

**Multi-Provider Release: Stable ✅**

- ✅ Core v1.0.0 workflow preserved
- ✅ Ollama verified
- ✅ OpenAI verified
- ✅ Anthropic verified
- ✅ Gemini verified
- ✅ Sidebar provider selection complete
- ✅ Provider/model session state complete
- ✅ Translation Provider Factory complete
- ✅ API-key configuration complete
- ✅ API-key values protected from UI display
- ✅ Settings provider status complete
- ✅ 177 automated tests passing
- ✅ GitHub Actions passing
- ✅ Manual end-to-end provider testing complete

---

## v1.3.0

[![Version](https://img.shields.io/badge/Version-v1.3.0-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.3.0)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Tests](https://img.shields.io/badge/Tests-217%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)

**Expanded Multi-Provider Release: Stable ✅**

- ✅ Core v1.0.0 workflow preserved
- ✅ v1.1.0 provider architecture preserved
- ✅ Ollama verified
- ✅ OpenAI provider preserved
- ✅ Anthropic provider preserved
- ✅ Gemini provider preserved
- ✅ Mistral provider added
- ✅ Groq provider added
- ✅ Cohere provider added
- ✅ DeepSeek provider added
- ✅ Sidebar provider/model selection updated
- ✅ Translation Provider Factory updated
- ✅ Settings page updated for 8 providers
- ✅ Environment API-key handling updated
- ✅ **217 automated tests passing**
- ✅ GitHub Actions passing

---

# 👤 Author

**Nekkanti Satya Srinath**

AI / Full-Stack Developer

- GitHub: https://github.com/satya66123
- LinkedIn: https://www.linkedin.com/in/satya-srinath-nekkanti-08b012a3/

---

# 📜 License

MIT License.

Copyright (c) 2026 Nekkanti Satya Srinath.

See the [`LICENSE`](LICENSE) file for the complete license text.

---

# 🏆 Release Summary

## v1.0.0

[![Release](https://img.shields.io/badge/Release-v1.0.0-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.0.0)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Tests](https://img.shields.io/badge/153%20Tests-Passing-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)

**Core Release: Stable ✅**

```text
Video → Transcript → Language Detection → Translation
→ SRT/VTT → FFmpeg → Captioned Video
```

**153 tests passed. GitHub Actions passing. End-to-end workflow verified.**

---

## v1.1.0

[![Release](https://img.shields.io/badge/Release-v1.1.0-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.1.0)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Tests](https://img.shields.io/badge/177%20Tests-Passing-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![CI](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)

**Multi-Provider Release: Stable ✅**

```text
Video
  ↓
Transcript
  ↓
Language Detection
  ↓
Provider Selection
  ↓
Ollama / OpenAI / Anthropic / Gemini
  ↓
SRT / VTT
  ↓
FFmpeg
  ↓
Captioned Video
```

**177 tests passed. 4/4 providers manually verified. GitHub Actions passing.**

---

### v1.3.0

[![Release](https://img.shields.io/badge/Release-v1.3.0-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.3.0)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Tests](https://img.shields.io/badge/217%20Tests-Passing-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![CI](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)

**Expanded 8-Provider Release: Stable ✅**

```text
Video
  ↓
Transcript
  ↓
Language Detection
  ↓
Provider Selection
  ↓
Ollama / OpenAI / Anthropic / Gemini
Mistral / Groq / Cohere / DeepSeek
  ↓
SRT / VTT
  ↓
FFmpeg
  ↓
Captioned Video
```

**217 tests passed. 8-provider architecture implemented. GitHub Actions passing.**

---

# 🔗 Project Links

- Repository: https://github.com/satya66123/AI-Video-Caption-Generator
- v1.0.0 Release: https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.0.0
- v1.1.0 Release: https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.1.0
- v1.3.0 Release: https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.3.0
- GitHub Actions: https://github.com/satya66123/AI-Video-Caption-Generator/actions

---

© 2026 Nekkanti Satya Srinath
