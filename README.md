# 🎬 AI Video Caption Generator

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![PyTest](https://img.shields.io/badge/tests-217%20passed-brightgreen.svg)](https://pytest.org/)
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

An AI-powered video caption generation application built with Python and Streamlit.

The application processes uploaded videos, detects spoken language, generates timestamped captions, translates captions into supported languages using a selectable AI provider and model, exports SRT/VTT files, and permanently burns captions into the final video using FFmpeg.

---

# 📌 Stable Releases

The project has evolved through three major stable releases.

| Version    | Status   | Main Scope                                  |
| ---------- | -------- | ------------------------------------------- |
| **v1.0.0** | ✅ Stable | Ollama-based core caption generation        |
| **v1.1.0** | ✅ Stable | Multi-provider AI translation               |
| **v1.3.0** | ✅ Stable | Multi-provider + multi-model AI translation |

## Release Evolution

```text
v1.0.0
Ollama-Based AI
      ↓
One Translation Model
      ↓
Core Caption Generator
```

```text
v1.1.0
Multiple AI Providers
      ↓
One Default Model per Provider
      ↓
Multi-Provider Translation
```

```text
v1.3.0
Multiple AI Providers
      ↓
Multiple Models per Provider
      ↓
Provider + Model Selection
      ↓
Multi-Model Translation
```

---

# 🚀 v1.3.0 — Multi-Provider + Multi-Model AI Translation

**Current stable release**

v1.3.0 extends the multi-provider architecture introduced in v1.1.0 by adding **multi-model support**.

Users can now select:

1. An AI provider
2. A model available for that provider

directly from the application sidebar.

## v1.3.0 Evolution

v1.0.0 started with a local Ollama-based translation workflow using a single configured model.

v1.1.0 introduced multiple AI providers, with one configured/default model for each provider.

v1.3.0 introduces multiple models per provider, allowing users to dynamically choose the provider and model used for translation.

```text
Provider
   ↓
Select Provider
   ↓
Available Models for Provider
   ↓
Select Model
   ↓
Translation Provider Factory
   ↓
Generate Captions
```

## v1.3.0 Providers

| Provider     | Mode  | Example Models                                                          |
| ------------ | ----- | ----------------------------------------------------------------------- |
| 🦙 Ollama    | Local | `qwen2.5:1.5b`, `gemma3:4b`, `mistral:latest`                           |
| 🟢 OpenAI    | API   | `gpt-5-mini`, `gpt-4o`, `gpt-4o-mini`                                   |
| 🟣 Anthropic | API   | `claude-sonnet-4-5`, `claude-haiku-4-5`, `claude-opus-4-1`              |
| 🔵 Gemini    | API   | `gemini-2.5-flash`, `gemini-2.5-pro`, `gemini-2.0-flash`                |
| 🟠 Mistral   | API   | `mistral-medium-latest`, `mistral-large-latest`, `mistral-small-latest` |
| ⚡ Groq       | API   | `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `mixtral-8x7b-32768` |
| 🟪 Cohere    | API   | `command-a-03-2025`, `command-r-plus`, `command-r`                      |
| 🔷 DeepSeek  | API   | `deepseek-chat`, `deepseek-reasoner`, `deepseek-v4-flash`               |

> Model availability depends on the provider and the provider API/account configuration.

## v1.3.0 Highlights

* 🤖 Multi-provider AI translation
* 🧠 **Multi-model support**
* 🔀 Provider + model selection
* 🧭 Provider selection from the sidebar
* 🎯 Model selection dynamically based on the selected provider
* 🦙 Multiple Ollama models
* 🟢 Multiple OpenAI models
* 🟣 Multiple Anthropic models
* 🔵 Multiple Gemini models
* 🟠 Multiple Mistral models
* ⚡ Multiple Groq models
* 🟪 Multiple Cohere models
* 🔷 Multiple DeepSeek models
* 🔌 Translation Provider Factory
* ⚙️ Provider and model configuration in Settings
* 🔐 Environment-based API-key configuration
* 🔒 API keys remain hidden from the UI
* 🧪 Expanded provider and model test coverage
* 🔄 GitHub Actions CI preserved
* 🎥 SRT/VTT generation preserved
* 🔥 FFmpeg caption burning preserved
* 💾 Original uploaded video preservation preserved

## v1.3.0 Sidebar Selection

```text
🤖 AI Provider

Provider
┌─────────────────────────────┐
│ OpenAI                   ▼  │
└─────────────────────────────┘

Model
┌─────────────────────────────┐
│ gpt-5-mini               ▼  │
└─────────────────────────────┘
```

When the provider changes, the model list changes automatically.

Example:

```text
Ollama
  ├── qwen2.5:1.5b
  ├── gemma3:4b
  └── mistral:latest
```

```text
OpenAI
  ├── gpt-5-mini
  ├── gpt-4o
  └── gpt-4o-mini
```

```text
Anthropic
  ├── claude-sonnet-4-5
  ├── claude-haiku-4-5
  └── claude-opus-4-1
```

## v1.3.0 Translation Flow

```text
Upload Video
      ↓
Save Original Video
      ↓
Whisper Transcription
      ↓
Language Detection
      ↓
Select Caption Language
      ↓
Select AI Provider
      ↓
Select AI Model
      ↓
Translation Provider Factory
      ↓
┌──────────────────────────────────────────────┐
│ Ollama / OpenAI / Anthropic / Gemini         │
│ Mistral / Groq / Cohere / DeepSeek           │
└──────────────────────────────────────────────┘
      ↓
Generate SRT + VTT
      ↓
FFmpeg Caption Burn
      ↓
Final Captioned Video
```

## v1.3.0 Verification

```text
217 passed
0 failed
100% pass rate
```

Provider and integration coverage includes:

```text
Ollama       → Provider tests ✅
OpenAI       → Provider tests ✅
Anthropic    → Provider tests ✅
Gemini       → Provider tests ✅
Mistral      → Provider tests ✅
Groq         → Provider tests ✅
Cohere       → Provider tests ✅
DeepSeek     → Provider tests ✅
Factory      → Integration tests ✅
Settings     → Provider configuration tests ✅
Full Suite   → 217 tests passed ✅
```

---

# 🚀 v1.1.0 — Multi-Provider AI Translation

**Stable release**

v1.1.0 introduced multi-provider AI translation to the original v1.0.0 Ollama-based architecture.

The application moved from a single AI provider to multiple selectable providers.

However, v1.1.0 used **one configured/default model per provider**.

## v1.1.0 Architecture

```text
Provider Selection
       ↓
┌────────────────────────────┐
│ Ollama                     │
│ OpenAI                     │
│ Anthropic                  │
│ Gemini                     │
└─────────────┬──────────────┘
              ↓
     One Default Model
       per Provider
              ↓
Translation Provider Factory
              ↓
Generate Captions
```

## v1.1.0 Providers

| Provider     | Default Model       | Mode  |
| ------------ | ------------------- | ----- |
| 🦙 Ollama    | `qwen2.5:1.5b`      | Local |
| 🟢 OpenAI    | `gpt-5-mini`        | API   |
| 🟣 Anthropic | `claude-sonnet-4-5` | API   |
| 🔵 Gemini    | `gemini-3.6-flash`  | API   |

## v1.1.0 Highlights

* 🤖 Multi-provider AI translation
* 🦙 Ollama translation
* 🟢 OpenAI translation
* 🟣 Anthropic translation
* 🔵 Gemini translation
* 🎯 One default model per provider
* 🧭 Provider selection from the sidebar
* 🧠 Provider and model stored in Streamlit session state
* 🔌 Translation Provider Factory
* 🔐 Environment-based API-key configuration
* 🔒 API keys never displayed in the UI
* ⚙️ Provider configuration/status in Settings
* 🧪 Expanded test coverage
* 🔄 GitHub Actions CI
* 🎥 SRT/VTT generation preserved
* 🔥 FFmpeg caption burning preserved
* 💾 Original uploaded video preserved

## v1.1.0 Flow

```text
Upload Video
     ↓
Save Original Video
     ↓
Whisper Transcription
     ↓
Language Detection
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

## v1.1.0 Verification

```text
177 automated tests
0 failed
100% pass rate
```

The complete workflow was manually verified for:

```text
Ollama     → SRT + VTT + Captioned Video + Original Video ✅
OpenAI     → SRT + VTT + Captioned Video + Original Video ✅
Anthropic  → SRT + VTT + Captioned Video + Original Video ✅
Gemini     → SRT + VTT + Captioned Video + Original Video ✅
```

---

# 🎬 v1.0.0 — Core Ollama Caption Generator

**Original stable release**

v1.0.0 was the original **Ollama-based local AI release**.

The initial version used one configured Ollama translation model together with Whisper and FFmpeg.

## v1.0.0 Architecture

```text
Video
  ↓
Whisper Transcription
  ↓
Language Detection
  ↓
Ollama
  ↓
One Local Translation Model
  ↓
SRT + VTT
  ↓
FFmpeg
  ↓
Final Captioned Video
```

## v1.0.0 Core Model

```text
qwen2.5:1.5b
```

## v1.0.0 Highlights

* 🎬 Video upload
* 📝 Whisper timestamped transcription
* 🌐 Spoken-language detection
* 💬 Multilingual caption generation
* 🦙 Local Ollama translation
* 🎯 Single configured translation model
* 📄 SRT generation
* 📄 VTT generation
* 🔥 FFmpeg caption burning
* 🎥 Final captioned-video preview
* 💾 Original video preservation
* 📊 Dashboard
* ⚙️ Settings
* ❓ Help
* ℹ️ About
* 🧪 Automated testing
* 🔄 GitHub Actions CI

## v1.0.0 Workflow

```text
Upload
  ↓
Transcribe with Whisper
  ↓
Detect Language
  ↓
Translate with Ollama
  ↓
Generate SRT + VTT
  ↓
Burn Captions with FFmpeg
  ↓
Final Captioned Video
```

---

# ✨ Features

## 🎬 Video Processing

* Video upload
* Original video preservation
* Local video storage
* MP4 support
* MOV support
* AVI support
* MKV support
* WebM support

## 📝 Transcription

* OpenAI Whisper transcription
* Timestamped transcript segments
* Spoken-language detection
* Internal transcript processing

## 🌐 Caption Languages

* English
* Telugu
* Hindi
* Tamil
* Kannada
* Malayalam
* Bengali
* Marathi
* Gujarati
* Punjabi

## 🤖 AI Translation

### Local

* Ollama

### Cloud Providers

* OpenAI
* Anthropic
* Gemini
* Mistral
* Groq
* Cohere
* DeepSeek

## 🧠 Multi-Model Support

Starting with v1.3.0, users can select multiple models depending on the selected provider.

```text
Select Provider
      ↓
Load Provider Models
      ↓
Select Model
      ↓
Run Translation
```

## 📄 Caption Formats

* SRT
* VTT

## 🔥 Video Caption Burning

FFmpeg permanently burns the generated captions into the final video.

## 📊 Dashboard

* Total videos
* Generated caption files
* Captioned videos
* Recent files

## ⚙️ Settings

* Whisper model selection
* AI provider selection
* AI model selection
* Default caption language
* Provider configuration/status

## 🧪 Testing

* PyTest automated tests
* Provider tests
* Factory tests
* Settings tests
* Service tests
* Agent tests
* GitHub Actions CI

---

# 🧩 Core Workflow

```text
┌──────────────────────┐
│     Upload Video     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Save Original Video  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Whisper Transcription│
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Language Detection   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Select Caption Lang. │
└──────────┬───────────┘
           ↓
┌───────────────────────────────┐
│ Select AI Provider            │
│                               │
│ Ollama / OpenAI / Anthropic   │
│ Gemini / Mistral / Groq       │
│ Cohere / DeepSeek             │
└──────────────┬────────────────┘
               ↓
┌───────────────────────────────┐
│ Select AI Model               │
│                               │
│ Model list depends on        │
│ selected provider             │
└──────────────┬────────────────┘
               ↓
┌───────────────────────────────┐
│ Translation Provider Factory  │
└──────────────┬────────────────┘
               ↓
       ┌───────┴───────┐
       ↓               ↓
┌───────────┐     ┌───────────┐
│    SRT    │     │    VTT    │
└─────┬─────┘     └─────┬─────┘
      └─────────┬───────┘
                ↓
┌──────────────────────┐
│ FFmpeg Caption Burn  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Final Captioned      │
│ Video                │
└──────────────────────┘
```

---

# 🌐 Supported Caption Languages

| Code | Language  |
| ---- | --------- |
| `en` | English   |
| `te` | Telugu    |
| `hi` | Hindi     |
| `ta` | Tamil     |
| `kn` | Kannada   |
| `ml` | Malayalam |
| `bn` | Bengali   |
| `mr` | Marathi   |
| `gu` | Gujarati  |
| `pa` | Punjabi   |

---

# 📄 Caption Formats

The application generates:

### SRT

SubRip Subtitle format.

### VTT

WebVTT format.

Both formats contain timestamped caption segments.

---

# 🎥 Supported Video Formats

* MP4
* MOV
* AVI
* MKV
* WebM

---

# 🛠️ Technology Stack

| Technology             | Purpose                              |
| ---------------------- | ------------------------------------ |
| Python 3.11            | Application development              |
| Streamlit              | Web UI                               |
| OpenAI Whisper         | Speech transcription                 |
| Ollama                 | Local AI translation                 |
| OpenAI                 | AI translation provider              |
| Anthropic              | AI translation provider              |
| Gemini                 | AI translation provider              |
| Mistral                | AI translation provider              |
| Groq                   | AI translation provider              |
| Cohere                 | AI translation provider              |
| DeepSeek               | AI translation provider              |
| Qwen / Gemma / Mistral | Local model support                  |
| FFmpeg                 | Video processing and caption burning |
| PyTest                 | Automated testing                    |
| JSON / Local Files     | Lightweight storage                  |
| GitHub Actions         | Continuous integration               |

---

# 🤖 AI Provider Architecture

The application uses a provider abstraction so translation logic is separated from provider-specific implementations.

```text
                    Translation Provider
                            │
                            ▼
                 Translation Provider Factory
                            │
        ┌───────────┬───────┴───────┬───────────┐
        ↓           ↓               ↓           ↓
     Ollama      OpenAI         Anthropic     Gemini
        │
        ├── qwen2.5:1.5b
        ├── gemma3:4b
        └── mistral:latest

        ┌───────────┬───────────┬───────────┐
        ↓           ↓           ↓           ↓
     Mistral      Groq        Cohere      DeepSeek
```

The provider is selected first, and the available models are then loaded for that provider.

---

# 🦙 Local AI with Ollama

The project supports local AI translation through Ollama.

Example models:

```text
qwen2.5:1.5b
gemma3:4b
mistral:latest
```

Install Ollama and verify it:

```powershell
ollama --version
```

Check installed models:

```powershell
ollama list
```

Pull the default model:

```powershell
ollama pull qwen2.5:1.5b
```

Start Ollama if required:

```powershell
ollama serve
```

> Make sure the selected Ollama model is installed locally before generating translated captions.

---

# 🔐 Cloud Provider Configuration

Cloud providers use environment variables for API keys.

Example:

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
MISTRAL_API_KEY=
GROQ_API_KEY=
COHERE_API_KEY=
DEEPSEEK_API_KEY=
```

API keys should never be committed to Git.

Use a local `.env` file and keep it excluded from version control.

---

# 🔥 FFmpeg

FFmpeg is used to permanently burn captions into the generated video.

Verify FFmpeg:

```powershell
ffmpeg -version
```

FFmpeg must be installed and available on the system `PATH`.

---

# 📁 Project Structure

```text
AI-Video-Caption-Generator/
│
├── .github/
│   └── workflows/
│       └── python-app.yml
│
├── agents/
│   ├── __init__.py
│   ├── caption_agent.py
│   └── dashboard_agent.py
│
├── config/
│   └── caption_config.py
│
├── core/
│   └── caption_models.py
│
├── pages/
│   ├── about_agent.py
│   ├── dashboard_agent.py
│   ├── help_agent.py
│   └── settings_agent.py
│
├── providers/
│   ├── translation_provider.py
│   ├── ollama_translation_provider.py
│   ├── openai_translation_provider.py
│   ├── anthropic_translation_provider.py
│   ├── gemini_translation_provider.py
│   ├── mistral_translation_provider.py
│   ├── groq_translation_provider.py
│   ├── cohere_translation_provider.py
│   ├── deepseek_translation_provider.py
│   └── translation_provider_factory.py
│
├── services/
│   ├── caption_generation_service.py
│   ├── caption_file_service.py
│   ├── language_detection_service.py
│   ├── transcript_service.py
│   └── video_caption_burn_service.py
│
├── tests/
│   ├── test_*.py
│   └── ...
│
├── uploads/
│   └── .gitkeep
│
├── captions/
│   └── .gitkeep
│
├── outputs/
│   └── .gitkeep
│
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

# 🚀 Installation

## 1. Clone the Repository

```powershell
git clone https://github.com/satya66123/AI-Video-Caption-Generator.git
cd AI-Video-Caption-Generator
```

## 2. Create a Virtual Environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

## 3. Install Python Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Install System Dependencies

Install:

* FFmpeg
* Ollama

Verify:

```powershell
python --version
ffmpeg -version
ollama --version
```

## 5. Install an Ollama Model

```powershell
ollama pull qwen2.5:1.5b
```

Additional models can be installed when required.

## 6. Configure Cloud Providers

If using cloud providers, configure the required API keys in `.env`.

Example:

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
MISTRAL_API_KEY=
GROQ_API_KEY=
COHERE_API_KEY=
DEEPSEEK_API_KEY=
```

## 7. Run the Application

```powershell
streamlit run app.py
```

The application will open in your browser.

---

# 🖥️ Application Navigation

The application provides a sidebar navigation:

```text
🏠 Dashboard
🎬 Caption Generator
📄 Captions
⚙️ Settings
❓ Help
ℹ️ About
```

---

# 🏠 Dashboard

The Dashboard displays:

* Total videos
* Generated caption files
* Captioned videos
* Recent generated files

Git placeholder files such as `.gitkeep` are excluded from Recent Files.

---

# 🎬 Caption Generator

The main workflow is:

1. Upload a video
2. Save the original video
3. Detect spoken language
4. Select caption language
5. Select AI provider
6. Select AI model
7. Generate captions
8. Download SRT/VTT
9. Burn captions into the video
10. Preview/download the final captioned video

---

# 📄 Captions

The Captions page allows users to browse generated:

* SRT files
* VTT files

Caption contents can be viewed and downloaded.

---

# ⚙️ Settings

The Settings page provides configuration for:

* Whisper model
* AI provider
* AI model
* Default caption language
* Provider configuration
* API-key status

## Provider → Model Selection

In v1.3.0, the model selection is dependent on the selected provider.

```text
Provider
   ↓
Ollama
   ↓
Ollama Models
```

or:

```text
Provider
   ↓
OpenAI
   ↓
OpenAI Models
```

This prevents an invalid combination such as:

```text
Provider: OpenAI
Model: qwen2.5:1.5b
```

Instead:

```text
Provider: OpenAI
Model: gpt-5-mini
```

---

# ❓ Help

The Help page provides:

* Usage instructions
* Supported video formats
* Supported caption formats
* AI processing information
* Ollama troubleshooting
* Translation model troubleshooting
* FFmpeg troubleshooting

---

# ℹ️ About

The About page provides:

* Project overview
* Core workflow
* Technology stack
* Project scope
* Current application version

---

# 🧪 Testing

The project contains a comprehensive PyTest suite.

Run all tests:

```powershell
pytest
```

Run with verbose output:

```powershell
pytest -v
```

Run a specific test file:

```powershell
pytest tests/test_dashboard_agent.py -v
```

## Current Test Status

```text
217 passed
0 failed
100% pass rate
```

The test suite covers the application components, including:

* Agents
* Services
* Translation providers
* Translation Provider Factory
* Settings
* Configuration
* Caption generation
* Caption files
* Video caption burning

---

# 🔄 GitHub Actions

The project includes a GitHub Actions workflow:

```text
.github/workflows/python-app.yml
```

The workflow:

1. Checks out the repository
2. Sets up Python 3.11
3. Installs dependencies
4. Runs the PyTest suite

Every configured push and pull request is automatically tested.

---

# 📊 Release Comparison

| Capability                         | v1.0.0 | v1.1.0 | v1.3.0 |
| ---------------------------------- | :----: | :----: | :----: |
| Video upload                       |    ✅   |    ✅   |    ✅   |
| Original video preservation        |    ✅   |    ✅   |    ✅   |
| Whisper transcription              |    ✅   |    ✅   |    ✅   |
| Language detection                 |    ✅   |    ✅   |    ✅   |
| SRT generation                     |    ✅   |    ✅   |    ✅   |
| VTT generation                     |    ✅   |    ✅   |    ✅   |
| FFmpeg caption burning             |    ✅   |    ✅   |    ✅   |
| Captioned video output             |    ✅   |    ✅   |    ✅   |
| Dashboard                          |    ✅   |    ✅   |    ✅   |
| Settings / Help / About            |    ✅   |    ✅   |    ✅   |
| Ollama translation                 |    ✅   |    ✅   |    ✅   |
| Multiple AI providers              |    ❌   |    ✅   |    ✅   |
| Multiple models per provider       |    ❌   |    ❌   |    ✅   |
| Provider selection                 |    ❌   |    ✅   |    ✅   |
| Model selection                    |    ❌   |    ❌   |    ✅   |
| Dynamic Provider → Model selection |    ❌   |    ❌   |    ✅   |
| Translation Provider Factory       |    ❌   |    ✅   |    ✅   |
| Environment API-key handling       |    ❌   |    ✅   |    ✅   |
| Automated tests                    |   153  |   177  |   217  |
| GitHub Actions                     |    ✅   |    ✅   |    ✅   |
| Manual E2E verification            |    ✅   |    ✅   |    ✅   |

---

# 📸 Application Screenshots

## 🏠 Dashboard

Main dashboard showing video statistics and recent generated files.

<p align="center">
  <img src="docs/screenshots/dashboard.png" alt="AI Video Caption Generator Dashboard" width="900">
</p>

---

## 🎬 Caption Generator

Main caption-generation interface.

<p align="center">
  <img src="docs/screenshots/initalcaptiongenratorpage.png" alt="Caption Generator Page" width="900">
</p>

---

## 📤 Video Upload

Video uploaded successfully and ready for processing.

<p align="center">
  <img src="docs/screenshots/aftervideoupload.png" alt="Video Upload" width="900">
</p>

---

## 💾 Original Video Saved

The original uploaded video is preserved separately.

<p align="center">
  <img src="docs/screenshots/aftervideosaved.png" alt="Original Video Saved" width="900">
</p>

---

## 🌐 Language Detection

Detected spoken language used for caption processing.

<p align="center">
  <img src="docs/screenshots/detectlanguage.png" alt="Language Detection" width="900">
</p>

---

## 📝 Caption Generation

Caption generation in progress.

<p align="center">
  <img src="docs/screenshots/generatingcaptions.png" alt="Generating Captions" width="900">
</p>

---

## ✅ Captions Generated Successfully

Generated SRT and VTT captions.

<p align="center">
  <img src="docs/screenshots/captionsgenratedsucessfully.png" alt="Captions Generated Successfully" width="900">
</p>

---

## 📄 Captions

Generated subtitle files and caption information.

<p align="center">
  <img src="docs/screenshots/captions.png" alt="Generated Captions" width="900">
</p>

---

## 🔥 Caption Burning

FFmpeg permanently burns the selected captions into the video.

<p align="center">
  <img src="docs/screenshots/burningvideo.png" alt="Caption Burning with FFmpeg" width="900">
</p>

---

## 🎥 Captioned Video

Final video with captions permanently embedded.

<p align="center">
  <img src="docs/screenshots/captionedvideo.png" alt="Captioned Video" width="900">
</p>

---

## ⚙️ Settings

Configure Whisper, AI providers, models and the default caption language.

<p align="center">
  <img src="docs/screenshots/settings.png" alt="Application Settings" width="900">
</p>

---

## ❓ Help

Application usage instructions and troubleshooting information.

<p align="center">
  <img src="docs/screenshots/help.png" alt="Help Page" width="900">
</p>

---

## ℹ️ About

Project overview, workflow and technology information.

<p align="center">
  <img src="docs/screenshots/about.png" alt="About Page" width="900">
</p>

---

# 💾 Generated Files

The application uses local directories:

```text
uploads/
    original video files

captions/
    *.srt
    *.vtt

outputs/
    captioned video files
```

The original uploaded video is preserved separately from the captioned output.

---

# 🔐 Privacy and Processing

The application supports local-first processing through Ollama.

When Ollama is selected, translation processing can be performed through the locally running Ollama service.

When a cloud provider is selected, the relevant translation request is sent to that provider's API.

Users should review the configuration, privacy policies and terms of any third-party services they choose to use.

API keys are loaded from environment variables and are not displayed in the application UI.

---

# ⚠️ Requirements

Before running the complete workflow, ensure:

* Python 3.11 is installed
* Required Python dependencies are installed
* FFmpeg is installed and available on `PATH`
* Ollama is installed for local translation
* Required Ollama models are available when using Ollama
* Required cloud API keys are configured when using cloud providers
* Sufficient disk space is available for videos and generated outputs

---

# 🛠️ Troubleshooting

## Ollama Connection Error

Verify:

```powershell
ollama --version
ollama list
ollama serve
```

## Translation Model Missing

Install the selected model:

```powershell
ollama pull qwen2.5:1.5b
```

Check installed models:

```powershell
ollama list
```

## Cloud Provider API Key Missing

Check the corresponding environment variable:

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
MISTRAL_API_KEY=
GROQ_API_KEY=
COHERE_API_KEY=
DEEPSEEK_API_KEY=
```

## FFmpeg Not Found

Verify:

```powershell
ffmpeg -version
```

Make sure FFmpeg is available on the system `PATH`.

## Tests Fail Locally

Activate the virtual environment:

```powershell
.venv\Scripts\activate
```

Reinstall dependencies:

```powershell
pip install -r requirements.txt
```

Run:

```powershell
pytest -v
```

---

# 📌 Development Status

## Core Application

**Complete ✅**

The implemented workflow produces:

* Original saved video
* SRT captions
* VTT captions
* Final captioned video

## Multi-Provider Translation

**Complete ✅**

Supported providers:

* Ollama
* OpenAI
* Anthropic
* Gemini
* Mistral
* Groq
* Cohere
* DeepSeek

## Multi-Model Selection

**Complete in v1.3.0 ✅**

Users can:

* Select an AI provider
* View models available for that provider
* Select an AI model
* Use the selected provider/model for translation

## Automated Testing

**Complete ✅**

```text
217 passed
0 failed
100% pass rate
```

## GitHub CI

**Passing ✅**

The GitHub Actions test workflow is passing.

---

# 🗺️ Future Improvements

Possible future enhancements include:

* Caption editing before export
* More translation providers
* Additional AI models
* Additional caption formats
* Batch video processing
* Caption style customization
* Subtitle positioning controls
* Advanced video/audio metadata
* Job progress tracking
* Improved output management
* Additional language support

These are future possibilities and are not required for the current completed workflow.

---

# 🤝 Contributing

Contributions are welcome.

General workflow:

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add or update tests
5. Run the full test suite
6. Verify the application manually when applicable
7. Commit your changes
8. Open a pull request

Before submitting changes:

```powershell
pytest
```

must pass successfully.

---

# 📜 License

This project is licensed under the MIT License.

Copyright (c) 2026 Nekkanti Satya Srinath

See the `LICENSE` file for the complete license text.

---

# 👤 Author

**Nekkanti Satya Srinath**

AI / Full-Stack Developer

* GitHub: https://github.com/satya66123
* LinkedIn: https://www.linkedin.com/in/satya-srinath-nekkanti-08b012a3/

---

# 📫 Contact

**Nekkanti Satya Srinath**

For project questions, issues, feature requests, or collaboration, please use the GitHub repository's Issues or Discussions where available.

---

# ⭐ Acknowledgements

This project uses and builds upon open-source technologies including:

* Python
* Streamlit
* OpenAI Whisper
* Ollama
* Qwen
* Gemma
* FFmpeg
* PyTest
* GitHub Actions

Please review the individual licenses and terms of the third-party technologies and models used by your installation.

---

# 📋 Project Summary

**AI Video Caption Generator** is an AI-powered application that transforms videos into multilingual captioned videos.

The project evolved through three major stable releases:

```text
v1.0.0
Ollama-Based Core
One Local Model
        ↓
v1.1.0
Multi-Provider AI
One Default Model per Provider
        ↓
v1.3.0
Multi-Provider + Multi-Model AI
Provider + Model Selection
```

## Complete Workflow

```text
Upload
  ↓
Save Original Video
  ↓
Transcribe
  ↓
Detect Language
  ↓
Select Caption Language
  ↓
Select Provider
  ↓
Select Model
  ↓
Translate
  ↓
Generate SRT + VTT
  ↓
Burn Captions
  ↓
Download Final Video
```

---

# 🎬 v1.0.0 Release

![AI Video Caption Generator v1.0.0](docs/screenshots/AI-Video-Caption-Generator-pic.png)

[![Tests](https://img.shields.io/badge/153%20Tests-Passing-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Tested%20Successfully-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Version](https://img.shields.io/badge/Version-v1.0.0-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.0.0)

**Original release:** Ollama-based local AI caption generation.

---

# 🚀 v1.1.0 Release

v1.1.0 introduced multi-provider AI translation.
![AI Video Caption Generator v1.1.0](docs/screenshots/AI-Video-Caption-Generator-pic.png)
[![Tests](https://img.shields.io/badge/177%20Tests-Passing-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Tested%20Successfully-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Version](https://img.shields.io/badge/Version-v1.1.0-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.1.0)




```text
Ollama
OpenAI
Anthropic
Gemini
```

Each provider used one configured/default translation model.

---

# 🚀 v1.3.0 Release

v1.3.0 introduces:

![AI Video Caption Generator v1.3.0](docs/screenshots/AI-Video-Caption-Generator-pic.png)
[![Tests](https://img.shields.io/badge/217%20Tests-Passing-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Tested%20Successfully-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Version](https://img.shields.io/badge/Version-v1.3.0-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.3.0)



```text
8 AI Providers
      +
Multiple Models per Provider
      +
Provider Selection
      +
Model Selection
```

The application now supports dynamic:

```text
Provider → Available Models → Selected Model
```

This is the major evolution from the v1.1.0 architecture.

---

# 🏆 Stable Release Summary

```text
AI Video Caption Generator
────────────────────────────────────────

v1.0.0 → Core Ollama Caption Generator
          One Local Translation Model
          Stable ✅

v1.1.0 → Multi-Provider AI Translation
          One Default Model per Provider
          Stable ✅

v1.3.0 → Multi-Provider + Multi-Model AI
          Multiple Models per Provider
          Provider + Model Selection
          Stable ✅

────────────────────────────────────────

Automated Tests: 217 passed
Failed Tests: 0
Pass Rate: 100%
GitHub Actions: Passing

Current Stable Release: v1.3.0 🚀
```

**v1.0.0** remains documented as the original Ollama-based core release.

**v1.1.0** introduced multi-provider AI translation with one default model per provider.

**v1.3.0** adds multi-model support, allowing users to select both the AI provider and the model used for translation.

## Current Stable Release

# 🚀 v1.3.0

**Multi-Provider + Multi-Model AI Translation**

**Status: Stable ✅**

**Tests: 217 passed ✅**

**GitHub Actions: Passing ✅**

---

⭐ If you find this project useful, consider starring the repository and sharing it with other developers.
