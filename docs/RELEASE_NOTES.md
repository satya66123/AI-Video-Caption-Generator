# 🚀 AI Video Caption Generator — Release Notes

[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Tests](https://img.shields.io/badge/Tests-177%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![OpenAI](https://img.shields.io/badge/AI-OpenAI-412991.svg)](https://openai.com/)
[![Anthropic](https://img.shields.io/badge/AI-Anthropic-orange.svg)](https://www.anthropic.com/)
[![Gemini](https://img.shields.io/badge/AI-Gemini-4285F4.svg)](https://ai.google.dev/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# 📌 Stable Releases

| Version | Status | Description |
|---|---|---|
| **v1.0.0** | ✅ Stable | Core video caption generation release |
| **v1.1.0** | ✅ Stable / Current | Multi-provider AI translation release |

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

[![Tests](https://img.shields.io/badge/Tests-177%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)

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

| Capability | v1.0.0 | v1.1.0 |
|---|---:|---:|
| Video upload | ✅ | ✅ |
| Original video preservation | ✅ | ✅ |
| Whisper transcription | ✅ | ✅ |
| Language detection | ✅ | ✅ |
| SRT generation | ✅ | ✅ |
| VTT generation | ✅ | ✅ |
| FFmpeg caption burning | ✅ | ✅ |
| Captioned video output | ✅ | ✅ |
| Dashboard | ✅ | ✅ |
| Settings | ✅ | ✅ |
| Help | ✅ | ✅ |
| About | ✅ | ✅ |
| Ollama translation | ✅ | ✅ |
| OpenAI translation | ❌ | ✅ |
| Anthropic translation | ❌ | ✅ |
| Gemini translation | ❌ | ✅ |
| Sidebar provider selection | ❌ | ✅ |
| Translation Provider Factory | ❌ | ✅ |
| Environment API-key handling | ❌ | ✅ |
| Automated tests | 153 | 177 |
| GitHub Actions | ✅ | ✅ |
| Manual E2E verification | ✅ | ✅ |

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
[![Tests](https://img.shields.io/badge/Tests-177%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)

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

## 🔗 Project Links

- Repository: https://github.com/satya66123/AI-Video-Caption-Generator
- v1.0.0 Release: https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.0.0
- v1.1.0 Release: https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.1.0
- GitHub Actions: https://github.com/satya66123/AI-Video-Caption-Generator/actions

---

© 2026 Nekkanti Satya Srinath
