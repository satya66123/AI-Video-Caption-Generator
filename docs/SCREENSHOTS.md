# 📸 AI Video Caption Generator — Screenshots

[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-267%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Version](https://img.shields.io/badge/Version-v1.4.1-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.4.1)
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
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)

A visual walkthrough of the **AI Video Caption Generator**, including the current
**v1.4.1 frontend, themes, multi-provider/model Settings, Help, About, and complete
caption-processing workflow**.

> **Note:** Existing v1.0.0–v1.4.1 screenshots are preserved. v1.4.1 adds the
> current-release screenshot and updated verification information.

---

## 📑 Screenshot Index

| # | Screenshot | Feature |
|---:|---|---|
| 1 | 🚀 [v1.4.1 Release](#-v141-release) | Current release |
| 2 | 🏠 [Dashboard](#-dashboard) | Dashboard |
| 3 | 🎬 [Caption Generator](#-caption-generator) | Main workflow |
| 4 | 📤 [Video Upload](#-video-upload) | Upload |
| 5 | 💾 [Original Video Saved](#-original-video-saved) | Storage |
| 6 | 🌐 [Language Detection](#-language-detection) | Original language |
| 7 | 📝 [Generating Captions](#-generating-captions) | Caption processing |
| 8 | ✅ [Captions Generated](#-captions-generated-successfully) | Successful generation |
| 9 | 📄 [Captions](#-captions) | SRT/VTT |
| 10 | 🔥 [Caption Burning](#-caption-burning) | FFmpeg |
| 11 | 🎥 [Captioned Video](#-captioned-video) | Final output |
| 12 | ⚙️ [Settings](#-settings) | Configuration |
| 13 | ❓ [Help](#-help) | Help |
| 14 | ℹ️ [About](#-about) | Project information |

---

# 🚀 v1.4.1 Release

**Tab-Based Frontend + 15 Themes + Multi-Provider / Multi-Model AI**

<p align="center">
  <img src="screenshots/AI-Video-Caption-Generator-v1.4.1-pic.png"
       alt="AI Video Caption Generator v1.4.1"
       width="900">
</p>

[![Version](https://img.shields.io/badge/Version-v1.4.1-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.4.1)
[![Tests](https://img.shields.io/badge/267%20Tests-Passing-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Pass Rate](https://img.shields.io/badge/Pass%20Rate-100%25-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Tested%20Successfully-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)

## v1.4.1 Key Features

- 🖥️ Added `apptab.py` tab-based frontend
- 🏠 Dashboard remains the default tab
- 🎬 Caption Generator
- 📄 Captions
- ⚙️ Settings
- ❓ Help
- ℹ️ About
- 🎨 **15 application themes**
- 🌙 5 dark themes
- ☀️ 10 light themes
- 🖤 Improved light-theme text visibility
- 🔽 Improved dropdown/selectbox readability
- 📝 Improved caption text visibility
- 🕐 Improved Recent Files readability
- 🤖 **8 AI providers**
- 🧠 Provider-specific multi-model selection
- 🌐 Original spoken-language detection
- 📄 Transcript, SRT and VTT generation
- 🔥 FFmpeg caption burning
- 💾 Original video preservation
- 🛠️ Expanded Help and Troubleshooting
- ℹ️ Expanded About documentation
- 📁 Project-folder documentation

### v1.4.1 AI Providers

```text
Ollama
OpenAI
Anthropic
Gemini
Mistral
Groq
Cohere
DeepSeek
```

### v1.4.1 Themes

```text
🌙 Dark
🌌 Midnight Blue
💜 Cosmic Purple
🌊 Ocean
🌿 Emerald

☀️ Light
🌤️ Sky Light
💜 Lavender Light
🌿 Mint Light
🌊 Aqua Light
🌸 Rose Light
🍑 Peach Light
🌼 Amber Light
🩵 Ice Light
🌱 Sage Light
```

### v1.4.1 Frontend Structure

```text
app.py
   ↓
apptab.py
   ↓
Tab Navigation
   ↓
Existing Agents / Services / Providers
   ↓
Existing Caption Workflow
```

---

# 🏠 Dashboard

[![Dashboard](https://img.shields.io/badge/UI-Dashboard-blue.svg)](screenshots/dashboard.png)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](screenshots/dashboard.png)

The Dashboard provides an overview of videos, caption files, captioned videos
and recent files.

<p align="center">
  <img src="screenshots/dashboard.png" alt="AI Video Caption Generator Dashboard" width="900">
</p>

---

# 🎬 Caption Generator

[![Caption Generator](https://img.shields.io/badge/UI-Caption%20Generator-blueviolet.svg)](screenshots/initalcaptiongenratorpage.png)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](screenshots/initalcaptiongenratorpage.png)

The main Caption Generator page starts the video caption workflow.

<p align="center">
  <img src="screenshots/initalcaptiongenratorpage.png" alt="AI Video Caption Generator Main Page" width="900">
</p>

---

# 📤 Video Upload

[![Upload](https://img.shields.io/badge/Feature-Video%20Upload-orange.svg)](screenshots/aftervideoupload.png)
[![Status](https://img.shields.io/badge/Status-Success-brightgreen.svg)](screenshots/aftervideoupload.png)

Shows the application after a video has been uploaded successfully.

<p align="center">
  <img src="screenshots/aftervideoupload.png" alt="Video Uploaded" width="900">
</p>

---

# 💾 Original Video Saved

[![Storage](https://img.shields.io/badge/Feature-Original%20Video%20Saved-blue.svg)](screenshots/aftervideosaved.png)
[![Status](https://img.shields.io/badge/Status-Success-brightgreen.svg)](screenshots/aftervideosaved.png)

Confirms that the original uploaded video has been saved separately.

<p align="center">
  <img src="screenshots/aftervideosaved.png" alt="Original Video Saved" width="900">
</p>

---

# 🌐 Language Detection

[![AI](https://img.shields.io/badge/AI-Language%20Detection-purple.svg)](screenshots/detectlanguage.png)
[![Status](https://img.shields.io/badge/Status-Success-brightgreen.svg)](screenshots/detectlanguage.png)

Shows detection of the video's original spoken language.

<p align="center">
  <img src="screenshots/detectlanguage.png" alt="Original Language Detection" width="900">
</p>

---

# 📝 Generating Captions

[![AI](https://img.shields.io/badge/AI-Caption%20Generation-blueviolet.svg)](screenshots/generatingcaptions.png)
[![Status](https://img.shields.io/badge/Status-Processing-yellow.svg)](screenshots/generatingcaptions.png)

Shows the caption-generation processing stage.

<p align="center">
  <img src="screenshots/generatingcaptions.png" alt="Generating Captions" width="900">
</p>

---

# ✅ Captions Generated Successfully

[![Captions](https://img.shields.io/badge/Feature-Captions%20Generated-success.svg)](screenshots/captionsgenratedsucessfully.png)
[![SRT](https://img.shields.io/badge/Format-SRT-blue.svg)](screenshots/captionsgenratedsucessfully.png)
[![VTT](https://img.shields.io/badge/Format-VTT-purple.svg)](screenshots/captionsgenratedsucessfully.png)

Shows successful caption generation.

<p align="center">
  <img src="screenshots/captionsgenratedsucessfully.png" alt="Captions Generated Successfully" width="900">
</p>

---

# 📄 Captions

[![SRT](https://img.shields.io/badge/Caption-SRT-blue.svg)](screenshots/captions.png)
[![VTT](https://img.shields.io/badge/Caption-VTT-purple.svg)](screenshots/captions.png)
[![Status](https://img.shields.io/badge/Status-Ready-brightgreen.svg)](screenshots/captions.png)

Shows generated SRT/VTT caption files.

<p align="center">
  <img src="screenshots/captions.png" alt="Caption Files" width="900">
</p>

---

# 🔥 Caption Burning

[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](screenshots/burningvideo.png)
[![Feature](https://img.shields.io/badge/Feature-Caption%20Burning-orange.svg)](screenshots/burningvideo.png)
[![Status](https://img.shields.io/badge/Status-Processing-yellow.svg)](screenshots/burningvideo.png)

Shows the FFmpeg caption-burning stage.

<p align="center">
  <img src="screenshots/burningvideo.png" alt="FFmpeg Caption Burning" width="900">
</p>

---

# 🎥 Captioned Video

[![Output](https://img.shields.io/badge/Output-Captioned%20Video-success.svg)](screenshots/captionedvideo.png)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](screenshots/captionedvideo.png)

Shows the final video with captions permanently embedded.

<p align="center">
  <img src="screenshots/captionedvideo.png" alt="Captioned Video Output" width="900">
</p>

---

# ⚙️ Settings

[![Settings](https://img.shields.io/badge/UI-Settings-blue.svg)](screenshots/settings.png)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](screenshots/settings.png)

The Settings page provides theme selection, AI provider selection,
provider-specific model selection and caption-language configuration.

<p align="center">
  <img src="screenshots/settings.png" alt="Application Settings" width="900">
</p>

### v1.4.1 Settings Flow

```text
🎨 Theme
   ↓
🤖 AI Provider
   ↓
🧠 Provider Model
   ↓
🌐 Caption Language
```

---

# ❓ Help

[![Help](https://img.shields.io/badge/UI-Help-orange.svg)](screenshots/help.png)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](screenshots/help.png)

The Help page provides usage guidance and troubleshooting for video uploads,
AI processing, providers/models, transcription, captions, FFmpeg, themes
and Settings.

<p align="center">
  <img src="screenshots/help.png" alt="Help Page" width="900">
</p>

---

# ℹ️ About

[![About](https://img.shields.io/badge/UI-About-lightgrey.svg)](screenshots/about.png)
[![Project](https://img.shields.io/badge/Project-AI%20Video%20Caption%20Generator-blue.svg)](screenshots/about.png)

The About page describes the project, versions, providers/models, themes,
folders, technology stack and testing status.

<p align="center">
  <img src="screenshots/about.png" alt="About Page" width="900">
</p>

---

# 🔄 Complete Visual Workflow

```text
📤 Upload Video
      ↓
💾 Save Original Video
      ↓
🎙️ Whisper Transcription
      ↓
🌐 Detect Original Language
      ↓
💬 Select Caption Language
      ↓
🤖 Select AI Provider
      ↓
🧠 Select Provider Model
      ↓
📝 Generate Captions
      ↓
📄 SRT + VTT
      ↓
🔥 FFmpeg Caption Burning
      ↓
🎥 Captioned Video
      ↓
📊 Dashboard / Outputs
```

---

# 📊 Verification

[![Tests](https://img.shields.io/badge/267%20Tests-Passing-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![CI](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Release](https://img.shields.io/badge/Release-v1.4.1-blue.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/releases/tag/v1.4.1)

## v1.4.1 Test Result

```text
267 collected
267 passed
0 failed
100% pass rate
19.83 seconds
```

Verified environment:

```text
Python 3.11.4
PyTest 9.1.1
Windows
GitHub Actions CI
```

---


---

# 📜 Screenshots by Release Version

The screenshot documentation preserves the application's visual evolution
from **v1.0.0 through v1.4.1**. Existing screenshots remain unchanged, while
the current v1.4.1 release screenshot is shown separately above.

## 🎬 v1.0.0 — Initial Release

**Core Ollama-based caption-generation application**

<p align="center">
  <img src="screenshots/AI-Video-Caption-Generator-pic.png"
       alt="AI Video Caption Generator v1.4.1 Release"
       width="900">
</p>


The original screenshot set documents the initial application workflow:

- 🏠 Dashboard
- 🎬 Caption Generator
- 📤 Video Upload
- 💾 Original Video Saved
- 🌐 Language Detection
- 📝 Caption Generation
- ✅ Captions Generated
- 📄 SRT/VTT Captions
- 🔥 FFmpeg Caption Burning
- 🎥 Captioned Video
- ⚙️ Settings
- ❓ Help
- ℹ️ About

These historical screenshots are retained in the sections below.

---

## 🚀 v1.1.0 — Multi-Provider AI Translation

**Release focus:** multi-provider AI translation and provider configuration.

Historical screenshots from the existing application UI remain applicable to
the v1.1.0 workflow:

<p align="center">
  <img src="screenshots/dashboard.png" alt="AI Video Caption Generator v1.1.0 Dashboard" width="800">
</p>

<p align="center">
  <img src="screenshots/initalcaptiongenratorpage.png" alt="AI Video Caption Generator v1.1.0 Caption Generator" width="800">
</p>

---

## 🚀 v1.2.0 — Timestamped Transcript Saving

**Release focus:** timestamped transcript persistence and caption workflow
improvements.

<p align="center">
  <img src="screenshots/detectlanguage.png" alt="AI Video Caption Generator v1.2.0 Language Detection" width="800">
</p>

<p align="center">
  <img src="screenshots/captionsgenratedsucessfully.png" alt="AI Video Caption Generator v1.2.0 Captions Generated" width="800">
</p>

---

## 🚀 v1.2.1 — Frontend / Application Improvements

**Release focus:** frontend and application improvements.

<p align="center">
  <img src="screenshots/aftervideoupload.png" alt="AI Video Caption Generator v1.2.1 Upload" width="800">
</p>

<p align="center">
  <img src="screenshots/captions.png" alt="AI Video Caption Generator v1.2.1 Captions" width="800">
</p>

---

## 🚀 v1.3.0 — Multi-Provider + Multi-Model AI Translation

**Release focus:** expanded provider architecture and multi-model AI
translation.

<p align="center">
  <img src="screenshots/settings.png" alt="AI Video Caption Generator v1.3.0 Settings" width="800">
</p>

<p align="center">
  <img src="screenshots/generatingcaptions.png" alt="AI Video Caption Generator v1.3.0 Caption Processing" width="800">
</p>

---

## 🚀 v1.4.0 — Custom Application Themes

**Release focus:** custom application theme selection.

<p align="center">
  <img src="screenshots/settings.png" alt="AI Video Caption Generator v1.4.0 Settings and Themes" width="800">
</p>

<p align="center">
  <img src="screenshots/dashboard.png" alt="AI Video Caption Generator v1.4.0 Dashboard" width="800">
</p>

---

## 🚀 v1.4.1 — Current Release

**Release focus:** tab-based frontend, 15 themes, multi-provider/model
Settings, Help/About improvements and UI readability.

<p align="center">
  <img src="screenshots/AI-Video-Caption-Generator-v1.4.1-pic.png"
       alt="AI Video Caption Generator v1.4.1 Release"
       width="900">
</p>

### v1.4.1 Visual Updates

- 🖥️ `app.py` + `apptab.py` tab-based frontend
- 🏠 Dashboard as default tab
- 🎨 15 themes
- 🌙 5 dark themes
- ☀️ 10 light themes
- 🖤 Light-theme text improvements
- 🔽 Dropdown/selectbox readability improvements
- 📝 Caption text visibility improvements
- 🕐 Recent Files readability improvements
- 🤖 8 AI providers
- 🧠 Provider-specific model selection
- ⚙️ Enhanced Settings
- ❓ Enhanced Help and Troubleshooting
- ℹ️ Enhanced About
- 🧪 267 tests passing

> **Screenshot asset note:** The repository's existing screenshots are reused
> for the historical release sections above because separate version-specific
> screenshot files for v1.1.0–v1.4.0 were not provided here. The v1.4.1
> release image is explicitly versioned as `AI-Video-Caption-Generator-v1.4.1-pic.png`.

---

# 📊 Version Screenshot Matrix

| Version | Visual Documentation | Main Visual Focus |
|---|---|---|
| **v1.0.0** | Existing screenshot set | Core caption workflow |
| **v1.1.0** | Existing UI screenshots | Multi-provider translation |
| **v1.2.0** | Existing UI screenshots | Timestamped transcript saving |
| **v1.2.1** | Existing UI screenshots | Frontend/application improvements |
| **v1.3.0** | Existing UI screenshots | Multi-provider + multi-model |
| **v1.4.0** | Existing UI screenshots | Theme selection |
| **v1.4.1** | Dedicated release image + existing UI screenshots | Tabs + 15 themes + multi-model Settings |

---

# 📜 Release Screenshot History

```text
v1.0.0  → Initial application screenshots
v1.1.0  → Caption workflow improvements
v1.2.0  → Caption / SRT / VTT improvements
v1.2.1  → Frontend/application improvements
v1.3.0  → Provider / translation improvements
v1.4.0  → Themes + multi-provider / multi-model improvements
v1.4.1  → Tab frontend + 15 themes + Settings / Help / About
```

Existing screenshots from earlier releases remain preserved in
`docs/screenshots/`.

---

## 👤 Author

**Nekkanti Satya Srinath**

- GitHub: https://github.com/satya66123
- LinkedIn: https://www.linkedin.com/in/satya-srinath-nekkanti-08b012a3/

---

© 2026 Nekkanti Satya Srinath
