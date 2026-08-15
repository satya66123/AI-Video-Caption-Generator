# 🎬 AI Video Caption Generator

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![PyTest](https://img.shields.io/badge/tests-153%20passed-brightgreen.svg)](https://pytest.org/)
[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Nekkanti%20Satya%20Srinath-black.svg)](https://github.com/satya66123)

An AI-powered video caption generation application built with Python and Streamlit. It automatically processes uploaded videos, detects spoken language, generates timestamped captions, translates captions into supported languages using a local Ollama model, exports SRT/VTT files, and permanently burns captions into the final video with FFmpeg.

## ✨ Features

- 🎬 Video upload and local storage
- 📝 Internal timestamped transcription using OpenAI Whisper
- 🌐 Spoken-language detection
- 💬 Multilingual caption generation
- 🤖 Local Ollama translation support
- 📄 SRT caption generation
- 📄 VTT caption generation
- 🔥 Permanent caption burning with FFmpeg
- 🎥 Final captioned-video preview and download
- 📊 Dashboard with video and caption statistics
- 🕐 Recent-file listing
- 🧹 `.gitkeep` files excluded from Recent Files
- ⚙️ Application Settings
- ❓ Help and troubleshooting page
- ℹ️ About page
- 🧭 Clean sidebar navigation
- 🧪 Comprehensive automated test suite
- 🔄 GitHub Actions CI
- 💾 Lightweight file-based storage
- 🔒 Local-first AI processing architecture

## 🧩 Core Workflow

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
┌──────────────────────┐
│ Local Ollama         │
│ Translation          │
└──────────┬───────────┘
           ↓
     ┌─────┴─────┐
     ↓           ↓
┌─────────┐ ┌─────────┐
│   SRT   │ │   VTT   │
└────┬────┘ └────┬────┘
     └─────┬─────┘
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

## 🌐 Supported Caption Languages

The application currently supports:

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

## 📄 Caption Formats

The application generates:

- **SRT** — SubRip Subtitle format
- **VTT** — WebVTT format

Both files contain timestamped caption segments.

## 🎥 Supported Video Formats

- MP4
- MOV
- AVI
- MKV
- WebM

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Application development |
| Streamlit | Web UI |
| OpenAI Whisper | Speech transcription |
| Ollama | Local AI translation |
| TranslateGemma | Local translation model support |
| FFmpeg | Video processing and caption burning |
| PyTest | Automated testing |
| JSON / local files | Lightweight application storage |
| GitHub Actions | Continuous integration |

## 🤖 Local AI

The project is designed around local AI processing.

The translation provider communicates with a locally running Ollama instance.

Example model:

```text
translategemma:12b
```

The application can be configured through the Settings page.

> Make sure the required Ollama model is installed locally before generating translated captions.

Example:

```powershell
ollama pull translategemma:12b
```

Start Ollama if required:

```powershell
ollama serve
```

Check installed models:

```powershell
ollama list
```

## 🔥 FFmpeg

FFmpeg is used to permanently burn captions into the generated video.

Verify FFmpeg:

```powershell
ffmpeg -version
```

FFmpeg must be installed and available on the system `PATH`.

## 📁 Project Structure

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
│   └── ollama_translation_provider.py
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

> The exact repository may contain additional modules and tests as development continues.

## 🚀 Installation

### 1. Clone the repository

```powershell
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-Video-Caption-Generator
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### 3. Install Python dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install system dependencies

Install:

- FFmpeg
- Ollama

Verify:

```powershell
python --version
ffmpeg -version
ollama --version
```

### 5. Install the translation model

```powershell
ollama pull translategemma:12b
```

### 6. Run the application

```powershell
streamlit run app.py

```

The application will open in your browser.

## 🖥️ Application Navigation

The application provides a single sidebar navigation:

```text
🏠 Dashboard
🎬 Caption Generator
📄 Captions
⚙️ Settings
❓ Help
ℹ️ About
```

### 🏠 Dashboard

Displays:

- Total videos
- Caption files
- Captioned videos
- Recent generated files

Git placeholder files such as `.gitkeep` are intentionally excluded.

### 🎬 Caption Generator

Main processing workflow:

1. Upload a video
2. Save the original video
3. Detect spoken language
4. Select caption language
5. Generate captions
6. Download SRT/VTT
7. Burn captions into the video
8. Preview/download the final captioned video

### 📄 Captions

Browse generated SRT and VTT files.

### ⚙️ Settings

Configure:

- Whisper model
- Ollama translation model
- Default caption language

### ❓ Help

Provides:

- Usage instructions
- Supported formats
- AI processing information
- Ollama troubleshooting
- TranslateGemma troubleshooting
- FFmpeg troubleshooting

### ℹ️ About

Provides:

- Project overview
- Core workflow
- Technology stack
- Project scope

## 🧪 Testing

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

### Current Test Status

```text
145 passed
0 failed
```

The complete workflow has also been manually tested, including:

- Original video saving
- SRT generation
- VTT generation
- Captioned-video generation
- Final video output

## 🔄 GitHub Actions

The project includes a GitHub Actions workflow:

```text
.github/workflows/python-app.yml
```

The workflow:

1. Checks out the repository
2. Sets up Python 3.11
3. Installs dependencies
4. Runs the PyTest suite

Every push and pull request targeting the configured main branch is automatically tested.

---

# 📸 Application Screenshots

Explore the AI Video Caption Generator through the screenshots below.

---

## 🏠 Dashboard

[![Dashboard](https://img.shields.io/badge/UI-Dashboard-blue.svg)](docs/screenshots/dashboard.png)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](docs/screenshots/dashboard.png)

Main dashboard showing video statistics and recent generated files.

<p align="center">
  <img src="docs/screenshots/dashboard.png" alt="AI Video Caption Generator Dashboard" width="900">
</p>

---

## 🎬 Caption Generator

[![Caption Generator](https://img.shields.io/badge/UI-Caption%20Generator-blueviolet.svg)](docs/screenshots/initalcaptiongenratorpage.png)
[![Status](https://img.shields.io/badge/Status-Ready-brightgreen.svg)](docs/screenshots/initalcaptiongenratorpage.png)

Main caption-generation interface.

<p align="center">
  <img src="docs/screenshots/initalcaptiongenratorpage.png" alt="Caption Generator Page" width="900">
</p>

---

## 📤 Video Upload

[![Upload](https://img.shields.io/badge/Feature-Video%20Upload-orange.svg)](docs/screenshots/aftervideoupload.png)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](docs/screenshots/aftervideoupload.png)

Video uploaded successfully and ready for processing.

<p align="center">
  <img src="docs/screenshots/aftervideoupload.png" alt="Video Upload" width="900">
</p>

---

## 💾 Original Video Saved

[![Storage](https://img.shields.io/badge/Feature-Original%20Video%20Saved-blue.svg)](docs/screenshots/aftervideosaved.png)
[![Status](https://img.shields.io/badge/Status-Success-brightgreen.svg)](docs/screenshots/aftervideosaved.png)

The original uploaded video is successfully preserved.

<p align="center">
  <img src="docs/screenshots/aftervideosaved.png" alt="Original Video Saved" width="900">
</p>

---

## 🌐 Language Detection

[![AI](https://img.shields.io/badge/AI-Language%20Detection-purple.svg)](docs/screenshots/detectlanguage.png)
[![Status](https://img.shields.io/badge/Status-Success-brightgreen.svg)](docs/screenshots/detectlanguage.png)

Detected spoken language used for caption processing.

<p align="center">
  <img src="docs/screenshots/detectlanguage.png" alt="Language Detection" width="900">
</p>

---

## 📝 Caption Generation

[![AI](https://img.shields.io/badge/AI-Caption%20Generation-blueviolet.svg)](docs/screenshots/generatingcaptions.png)
[![Status](https://img.shields.io/badge/Status-Processing-yellow.svg)](docs/screenshots/generatingcaptions.png)

Caption generation in progress.

<p align="center">
  <img src="docs/screenshots/generatingcaptions.png" alt="Generating Captions" width="900">
</p>

---

## ✅ Captions Generated Successfully

[![Captions](https://img.shields.io/badge/Feature-Captions%20Generated-success.svg)](docs/screenshots/captionsgeneratedsuccessfully.png)
[![SRT](https://img.shields.io/badge/Format-SRT-blue.svg)](docs/screenshots/captionsgeneratedsuccessfully.png)
[![VTT](https://img.shields.io/badge/Format-VTT-purple.svg)](docs/screenshots/captionsgeneratedsuccessfully.png)

Caption generation completed successfully.

<p align="center">
  <img src="docs/screenshots/captionsgenratedsucessfully.png" alt="Captions Generated Successfully" width="900">
</p>

---

## 📄 Captions

[![SRT](https://img.shields.io/badge/Caption-SRT-blue.svg)](docs/screenshots/captions.png)
[![VTT](https://img.shields.io/badge/Caption-VTT-purple.svg)](docs/screenshots/captions.png)
[![Status](https://img.shields.io/badge/Status-Ready-brightgreen.svg)](docs/screenshots/captions.png)

Generated subtitle files and caption information.

<p align="center">
  <img src="docs/screenshots/captions.png" alt="Generated Captions" width="900">
</p>

---

## 🔥 Caption Burning

[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](docs/screenshots/burningvideo.png)
[![Feature](https://img.shields.io/badge/Feature-Caption%20Burning-orange.svg)](docs/screenshots/burningvideo.png)
[![Status](https://img.shields.io/badge/Status-Processing-yellow.svg)](docs/screenshots/burningvideo.png)

FFmpeg permanently burns the selected captions into the video.

<p align="center">
  <img src="docs/screenshots/burningvideo.png" alt="Caption Burning with FFmpeg" width="900">
</p>

---

## 🎥 Captioned Video

[![Output](https://img.shields.io/badge/Output-Captioned%20Video-success.svg)](docs/screenshots/captionedvideo.png)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](docs/screenshots/captionedvideo.png)

Final video with captions permanently embedded.

<p align="center">
  <img src="docs/screenshots/captionedvideo.png" alt="Captioned Video" width="900">
</p>

---

## ⚙️ Settings

[![Settings](https://img.shields.io/badge/UI-Settings-blue.svg)](docs/screenshots/settings.png)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](docs/screenshots/settings.png)

Configure Whisper, Ollama and the default caption language.

<p align="center">
  <img src="docs/screenshots/settings.png" alt="Application Settings" width="900">
</p>

---

## ❓ Help

[![Help](https://img.shields.io/badge/UI-Help-orange.svg)](docs/screenshots/help.png)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](docs/screenshots/help.png)

Application usage instructions and troubleshooting information.

<p align="center">
  <img src="docs/screenshots/help.png" alt="Help Page" width="900">
</p>

---

## ℹ️ About

[![About](https://img.shields.io/badge/UI-About-lightgrey.svg)](docs/screenshots/about.png)
[![Project](https://img.shields.io/badge/Project-AI%20Video%20Caption%20Generator-blue.svg)](docs/screenshots/about.png)

Project overview, workflow and technology information.

<p align="center">
  <img src="docs/screenshots/about.png" alt="About Page" width="900">
</p>

---

## 💾 Generated Files

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

## 🔐 Privacy and Local Processing

The project is designed for local-first processing.

Video and generated caption files are stored locally by the application. Translation requests are sent to the locally running Ollama service rather than requiring a hosted translation API.

Users should still review the configuration and dependencies of any local or third-party software used with the project.

## ⚠️ Requirements

Before running the complete workflow, ensure:

- Python 3.11 is installed
- Required Python dependencies are installed
- FFmpeg is installed and available on `PATH`
- Ollama is installed
- The required Ollama model is available
- Sufficient disk space is available for videos and generated outputs

## 🛠️ Troubleshooting

### Ollama connection error

Verify:

```powershell
ollama --version
ollama list
ollama serve
```

### Translation model missing

Install the model:

```powershell
ollama pull translategemma:12b
```

### FFmpeg not found

Verify:

```powershell
ffmpeg -version
```

### Tests fail locally

Make sure the virtual environment is activated:

```powershell
.venv\Scripts\activate
```

Then reinstall dependencies:

```powershell
pip install -r requirements.txt
```

Run:

```powershell
pytest -v
```

## 📌 Development Status

### Core Application

**Complete ✅**

The implemented and manually verified workflow produces:

- Original saved video
- SRT captions
- VTT captions
- Final captioned video

### Automated Testing

**Complete ✅**

```text
145 passed
```

### GitHub CI

**Passing ✅**

The GitHub Actions test workflow is passing.

## 🗺️ Future Improvements

Possible future enhancements include:

- Caption editing before export
- More translation providers
- Additional caption formats
- Batch video processing
- Caption style customization
- Subtitle positioning controls
- Advanced video/audio metadata
- Job progress tracking
- Improved output management
- Additional language support

These are future possibilities and are not required for the current completed workflow.

## 🤝 Contributing

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

Before submitting changes, make sure:

```powershell
pytest
```

passes successfully.

## 📜 License

This project is licensed under the MIT License.

Copyright (c) 2026 Nekkanti Satya Srinath

See the `LICENSE` file for the complete license text.

## 👤 Author

**Nekkanti Satya Srinath**

AI / Full-Stack Developer

- GitHub: https://github.com/satya66123
- LinkedIn: https://www.linkedin.com/in/satya-srinath-nekkanti-08b012a3/
- Phone: +91 7396531602

## 📫 Contact

**Nekkanti Satya Srinath**

- GitHub: https://github.com/satya66123
- LinkedIn: https://www.linkedin.com/in/satya-srinath-nekkanti-08b012a3/
- Phone: +91 7396531602

For project questions, issues, feature requests, or collaboration, please use the GitHub repository's Issues or Discussions where available.

## ⭐ Acknowledgements

This project uses and builds upon open-source technologies including:

- Python
- Streamlit
- OpenAI Whisper
- Ollama
- TranslateGemma
- FFmpeg
- PyTest
- GitHub Actions

Please review the individual licenses and terms of the third-party technologies and models used by your installation.

---

## 📋 Project Summary

**AI Video Caption Generator** is a local-first AI application that transforms videos into multilingual captioned videos.

```text
Upload
  ↓
Transcribe
  ↓
Detect Language
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

## 🎬 v1.0.0 Release

![AI Video Caption Generator v1.0.0](docs/screenshots/AI-Video-Caption-Generator-pic.png)
[![Tests](https://img.shields.io/badge/153%20Tests-Passing-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Tested%20Successfully-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Version](https://img.shields.io/badge/Version-v1.0.0-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.0.0)

---

## **153 Tests Passed • 0 Failed • 100% Pass Rate • v1.0.0**

## 🚀 [GitHub Repository](https://github.com/satya66123/AI-Video-Caption-Generator)  
## 📦 [Release Notes — v1.0.0](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.0.0)

**Status: Core release complete ✅**

**Tests: 153 passed ✅**

**GitHub Actions: Passing ✅**
---

## 📊 Project Status

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)

**Status: Core Release Complete ✅**

- ✅ End-to-end video caption workflow verified
- ✅ Original video saved
- ✅ SRT generated
- ✅ VTT generated
- ✅ Captioned video generated
- ✅ Dashboard complete
- ✅ Sidebar navigation complete
- ✅ Settings / Help / About complete
- ✅ 153 automated tests passing
- ✅ GitHub Actions CI passing
- ✅ Manual end-to-end testing completed
