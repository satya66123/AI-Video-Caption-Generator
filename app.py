"""AI Video Caption Generator application."""

from agents.caption_agent import CaptionAgent
from agents.dashboard_agent import DashboardAgent
from providers.translation_provider_factory import (
    TranslationProviderFactory,
)
from services.caption_generation_service import (
    CaptionGenerationService,
)
from services.caption_file_service import CaptionFileService
from services.video_caption_burn_service import (
    VideoCaptionBurnService,
)
from services.transcript_service import TranscriptService
from datetime import datetime


import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

load_dotenv()
# ============================================================
# Directories
# ============================================================

UPLOAD_DIR = Path("uploads")
CAPTION_DIR = Path("captions")
OUTPUT_DIR = Path("outputs")
TRANSCRIPT_DIR = Path("transcripts")



# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="AI Video Caption Generator",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# Application Constants
# ============================================================

APP_VERSION = "1.3.0"

CAPTION_LANGUAGES = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Bengali": "bn",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
}


# ============================================================
# Sidebar Navigation
# ============================================================

def save_generated_transcript(
    video_path: Path,
    segments: list,
) -> Path | None:
    """Save generated transcript with Whisper timestamps."""

    if not segments:
        return None

    TRANSCRIPT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    generated_at = datetime.now()

    filename_timestamp = generated_at.strftime(
        "%Y%m%d_%H%M%S"
    )

    transcript_path = (
        TRANSCRIPT_DIR
        / f"{video_path.stem}_{filename_timestamp}.txt"
    )

    lines = [
        f"Transcript: {video_path.name}",
        f"Generated: {generated_at.isoformat(timespec='seconds')}",
        "",
    ]

    for index, segment in enumerate(
        segments,
        start=1,
    ):
        start = float(
            getattr(segment, "start", 0.0)
        )

        end = float(
            getattr(segment, "end", 0.0)
        )

        transcript_text = str(
            getattr(segment, "text", "")
        ).strip()

        if not transcript_text:
            continue

        lines.append(
            f"{index:04d} | "
            f"[{start:08.2f} --> {end:08.2f}] "
            f"{transcript_text}"
        )

    transcript_path.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )

    return transcript_path

def render_sidebar() -> str:
    """Render the application sidebar navigation."""

    with st.sidebar:

        # ----------------------------------------------------
        # Application Header
        # ----------------------------------------------------

        st.markdown(
            """
            <div style="text-align:center;">
                <div style="font-size:42px;">🎬</div>
                <h2 style="margin-bottom:0;">
                    AI Video
                </h2>
                <h3 style="margin-top:0;">
                    Caption Generator
                </h3>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        # ----------------------------------------------------
        # Navigation
        # ----------------------------------------------------

        st.markdown("### 🧭 Navigation")

        page = st.radio(
            "Navigation",
            options=[
                "🏠 Dashboard",
                "🎬 Caption Generator",
                "📄 Captions",
                "⚙️ Settings",
                "❓ Help",
                "ℹ️ About",
            ],
            label_visibility="collapsed",
        )

        st.divider()

        # ----------------------------------------------------
        # AI Provider Configuration
        # ----------------------------------------------------

        st.markdown("### 🤖 AI Provider")

        translation_providers = {
            "Ollama": {
                "key": "ollama",
                "models": [
                    "qwen2.5:1.5b",
                    "gemma2:2b",
                    "gemma3:4b",
                    "mistral:latest",
                    "phi3:latest",
                    "qwen3:latest",
                    "llama3.1:latest",
                    "llama3:8b",
                    "deepseek-coder:latest",
                ],
                "environment_variable": None,
            },
            "OpenAI": {
                "key": "openai",
                "models": [
                    "gpt-5-mini",
                    "gpt-4o",
                    "gpt-4o-mini",
                ],
                "environment_variable": "OPENAI_API_KEY",
            },
            "Anthropic": {
                "key": "anthropic",
                "models": [
                    "claude-sonnet-4-5",
                    "claude-haiku-4-5",
                    "claude-opus-4-1",
                ],
                "environment_variable": "ANTHROPIC_API_KEY",
            },
            "Gemini": {
                "key": "gemini",
                "models": [
                    "gemini-3.6-flash",
                    "gemini-2.5-flash",
                    "gemini-2.5-pro",
                ],
                "environment_variable": "GEMINI_API_KEY",
            },
            "Mistral": {
                "key": "mistral",
                "models": [
                    "mistral-medium-latest",
                    "mistral-large-latest",
                    "mistral-small-latest",
                ],
                "environment_variable": "MISTRAL_API_KEY",
            },
            "Groq": {
                "key": "groq",
                "models": [
                    "llama-3.3-70b-versatile",
                    "llama-3.1-8b-instant",
                    "mixtral-8x7b-32768",
                ],
                "environment_variable": "GROQ_API_KEY",
            },
            "Cohere": {
                "key": "cohere",
                "models": [
                    "command-a-03-2025",
                    "command-r-plus",
                    "command-r",
                ],
                "environment_variable": "COHERE_API_KEY",
            },
            "DeepSeek": {
                "key": "deepseek",
                "models": [
                    "deepseek-chat",
                    "deepseek-reasoner",
                    "deepseek-v4-flash",
                ],
                "environment_variable": "DEEPSEEK_API_KEY",
            },
        }

        # ----------------------------------------------------
        # Provider Selection
        # ----------------------------------------------------

        provider_names = list(translation_providers.keys())

        current_provider = st.session_state.get(
            "translation_provider",
            "ollama",
        )

        provider_keys = [
            config["key"]
            for config in translation_providers.values()
        ]

        provider_index = (
            provider_keys.index(current_provider)
            if current_provider in provider_keys
            else 0
        )

        selected_provider = st.selectbox(
            "Provider",
            options=provider_names,
            index=provider_index,
            key="sidebar_provider",
            help="Select the AI provider used for caption translation.",
        )

        # ----------------------------------------------------
        # Selected Provider Configuration
        # ----------------------------------------------------

        provider_config = translation_providers[selected_provider]

        provider_key = provider_config["key"]
        available_models = provider_config["models"]

        # ----------------------------------------------------
        # Model Selection
        # ----------------------------------------------------

        current_model = st.session_state.get(
            "translation_model"
        )

        if current_model not in available_models:
            current_model = available_models[0]

        translation_model = st.selectbox(
            "Model",
            options=available_models,
            index=available_models.index(current_model),
            key=f"sidebar_model_{provider_key}",
            help=f"Select the model for {selected_provider}.",
        )

        # ----------------------------------------------------
        # Save Selection
        # ----------------------------------------------------

        st.session_state["translation_provider"] = provider_key
        st.session_state["translation_model"] = translation_model



        # ----------------------------------------------------
        # Provider Status
        # ----------------------------------------------------

        if provider_key == "ollama":

            st.success(
                "🟢 Local Ollama",
            )

        elif provider_key == "openai":

            if os.getenv("OPENAI_API_KEY"):
                st.success(
                    "🟢 OpenAI configured",
                )
            else:
                st.warning(
                    "🔴 OpenAI API key missing",
                )

        elif provider_key == "anthropic":

            if os.getenv("ANTHROPIC_API_KEY"):
                st.success(
                    "🟢 Anthropic configured",
                )
            else:
                st.warning(
                    "🔴 Anthropic API key missing",
                )

        elif provider_key == "gemini":

            if os.getenv("GEMINI_API_KEY"):
                st.success(
                    "🟢 Gemini configured",
                )
            else:
                st.warning(
                    "🔴 Gemini API key missing",
                )

        st.divider()

        # ----------------------------------------------------
        # Current Language
        # ----------------------------------------------------

        st.markdown("### 🌐 Language")

        current_language = st.session_state.get(
            "default_caption_language",
            "en",
        )

        language_name = next(
            (
                name
                for name, code
                in CAPTION_LANGUAGES.items()
                if code == current_language
            ),
            "English",
        )

        st.write(language_name)

        st.divider()

        # ----------------------------------------------------
        # System Status
        # ----------------------------------------------------

        st.markdown("### 🟢 System Status")

        if provider_key == "ollama":
            st.write("🟢 Ollama")
        elif provider_key == "openai":
            st.write("🟢 OpenAI")
        elif provider_key == "anthropic":
            st.write("🟢 Anthropic")
        elif provider_key == "gemini":
            st.write("🟢 Gemini")

        st.write("🟢 Whisper")
        st.write("🟢 FFmpeg")

        # ----------------------------------------------------
        # Version
        # ----------------------------------------------------

        st.divider()

        st.caption(
            "AI Video Caption Generator"
        )

        st.caption(
            f"Version {APP_VERSION}"
        )

    return page


# ============================================================
# Upload
# ============================================================

def save_uploaded_video(uploaded_file) -> Path:
    """Save an uploaded video using its original filename."""

    UPLOAD_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = UPLOAD_DIR / Path(
        uploaded_file.name
    ).name

    output_path.write_bytes(
        uploaded_file.getbuffer()
    )

    return output_path


# ============================================================
# Caption Agent Factory
# ============================================================

def create_caption_agent() -> CaptionAgent:
    """Create a fully configured CaptionAgent."""

    # --------------------------------------------------------
    # Whisper
    # --------------------------------------------------------

    whisper_model = st.session_state.get(
        "whisper_model",
        "base",
    )

    transcript_service = TranscriptService(
        model_name=whisper_model,
    )

    # --------------------------------------------------------
    # Translation Provider
    # --------------------------------------------------------

    provider_name = st.session_state.get(
        "translation_provider",
        "ollama",
    )

    translation_model = st.session_state.get(
        "translation_model",
        "qwen2.5:1.5b",
    )

    # --------------------------------------------------------
    # API Key
    # --------------------------------------------------------

    api_key = None

    environment_variables = {
        "openai": "OPENAI_API_KEY",
        "anthropic": "ANTHROPIC_API_KEY",
        "gemini": "GEMINI_API_KEY",
        "mistral": "MISTRAL_API_KEY",
        "groq": "GROQ_API_KEY",
        "cohere": "COHERE_API_KEY",
        "deepseek": "DEEPSEEK_API_KEY",
    }

    environment_variable = environment_variables.get(
        provider_name
    )

    if environment_variable:
        api_key = os.getenv(environment_variable)


    # --------------------------------------------------------
    # Provider Factory
    # --------------------------------------------------------

    provider_kwargs = {
        "model": translation_model,
    }

    if api_key:
        provider_kwargs["api_key"] = api_key

    translation_provider = (
        TranslationProviderFactory.create(
            provider_name,
            **provider_kwargs,
        )
    )

    # --------------------------------------------------------
    # Caption Generation
    # --------------------------------------------------------

    caption_generation_service = (
        CaptionGenerationService(
            translation_provider=translation_provider,
        )
    )

    # --------------------------------------------------------
    # Caption Files
    # --------------------------------------------------------

    caption_file_service = CaptionFileService(
        CAPTION_DIR,
    )

    # --------------------------------------------------------
    # FFmpeg
    # --------------------------------------------------------

    video_caption_burn_service = (
        VideoCaptionBurnService(
            OUTPUT_DIR,
        )
    )

    # --------------------------------------------------------
    # Caption Agent
    # --------------------------------------------------------

    return CaptionAgent(
        transcript_service=transcript_service,
        caption_generation_service=(
            caption_generation_service
        ),
        caption_file_service=caption_file_service,
        video_caption_burn_service=(
            video_caption_burn_service
        ),
    )


# ============================================================
# Dashboard
# ============================================================

def render_dashboard() -> None:
    """Render the dashboard page."""

    st.title("🏠 Dashboard")

    st.write(
        "Overview of your AI Video Caption Generator."
    )

    st.divider()

    dashboard = DashboardAgent(
        upload_dir=UPLOAD_DIR,
        caption_dir=CAPTION_DIR,
        output_dir=OUTPUT_DIR,
    )

    statistics = dashboard.get_statistics()

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎬 Videos",
            statistics["videos"],
        )

    with col2:
        st.metric(
            "📄 Caption Files",
            statistics["caption_files"],
        )

    with col3:
        st.metric(
            "🎥 Captioned Videos",
            statistics["captioned_videos"],
        )

    st.divider()

    # --------------------------------------------------------
    # Recent Files
    # --------------------------------------------------------

    st.subheader("🕐 Recent Files")

    recent_files = dashboard.get_recent_files(
        limit=10,
    )

    if not recent_files:
        st.info(
            "No files available yet."
        )
        return

    for file_info in recent_files:

        st.write(
            f"**{file_info['name']}**"
        )

        st.caption(
            f"Type: {file_info['type']}  "
            f"| Path: {file_info['path']}"
        )


# ============================================================
# Caption Generator
# ============================================================

def render_caption_generator() -> None:
    """Render the complete caption generation workflow."""

    st.title(
        "🎬 AI Video Caption Generator"
    )

    st.write(
        "Generate captions in your selected language "
        "and permanently burn them into your video."
    )

    st.divider()

    # ========================================================
    # 1. Upload
    # ========================================================

    st.subheader("📤 Upload Video")

    uploaded_file = st.file_uploader(
        "Choose a video",
        type=[
            "mp4",
            "mov",
            "avi",
            "mkv",
            "webm",
        ],
        help=(
            "Upload a video to generate captions."
        ),
    )

    if uploaded_file is None:

        st.info(
            "Upload a video to begin the caption workflow."
        )

        return

    st.success(
        f"Selected video: {uploaded_file.name}"
    )

    st.video(uploaded_file)

    if st.button(
        "📥 Save Video",
        type="primary",
    ):

        video_path = save_uploaded_video(
            uploaded_file
        )

        st.session_state[
            "video_path"
        ] = str(video_path)

        # Clear old workflow results.
        st.session_state.pop(
            "detected_language",
            None,
        )

        st.session_state.pop(
            "caption_result",
            None,
        )

        st.session_state.pop(
            "captioned_video_path",
            None,
        )

        st.success(
            f"Video saved: {video_path.name}"
        )

    # ========================================================
    # 2. Current Video
    # ========================================================

    video_path_value = st.session_state.get(
        "video_path"
    )

    if not video_path_value:
        return

    video_path = Path(
        video_path_value
    )

    st.divider()

    st.subheader(
        "🎬 Current Video"
    )

    st.write(
        f"**Video:** `{video_path.name}`"
    )

    # ========================================================
    # 3. Language Detection
    # ========================================================

    st.subheader(
        "🌐 Language Detection"
    )

    if st.button(
        "🔍 Detect Video Language"
    ):

        with st.spinner(
            "Detecting spoken language..."
        ):

            try:

                agent = create_caption_agent()

                detection = agent.detect_language(
                    video_path
                )

                st.session_state[
                    "detected_language"
                ] = detection

            except Exception as exc:

                st.error(
                    f"Language detection failed: {exc}"
                )

    detected_language = st.session_state.get(
        "detected_language"
    )

    if detected_language:

        language_name = (
            detected_language.get(
                "language_name",
                detected_language.get(
                    "language",
                    "Unknown",
                ),
            )
        )

        language_code = (
            detected_language.get(
                "language",
                "",
            )
        )

        st.success(
            f"Detected language: "
            f"{language_name} "
            f"({language_code})"
        )

    # ========================================================
    # 4. Caption Language
    # ========================================================

    st.divider()

    st.subheader(
        "💬 Caption Language"
    )

    selected_language_name = st.selectbox(
        "Select the language for captions",
        options=list(
            CAPTION_LANGUAGES.keys()
        ),
    )

    selected_language = (
        CAPTION_LANGUAGES[
            selected_language_name
        ]
    )

    st.session_state[
        "caption_language"
    ] = selected_language

    st.info(
        f"Caption language: "
        f"{selected_language_name} "
        f"({selected_language})"
    )

    # ========================================================
    # 5. Generate Captions
    # ========================================================

    st.divider()

    st.subheader(
        "✨ Generate Captions"
    )

    st.write(
        "The video will be transcribed internally, "
        "translated with the configured AI provider, "
        "and converted into SRT and VTT caption files."
    )

    if st.button(
        "✨ Generate Captions",
        type="primary",
    ):

        with st.spinner(
            "Generating captions..."
        ):

            try:

                agent = create_caption_agent()

                result = (
                    agent.generate_caption_files(
                        video_path=video_path,
                        caption_language=(
                            selected_language
                        ),
                    )
                )

                st.session_state[
                    "caption_result"
                ] = result

                transcript_path = save_generated_transcript(
                    video_path=video_path,
                    segments=result.get(
                        "segments",
                        [],
                    ),
                )

                if transcript_path:
                    st.session_state[
                        "transcript_path"
                    ] = str(transcript_path)

                st.success(
                    "Captions generated successfully!"
                )

                if transcript_path:
                    st.info(
                        f"Transcript saved: "
                        f"{transcript_path.name}"
                    )

            except Exception as exc:

                st.error(
                    f"Caption generation failed: {exc}"
                )

    # ========================================================
    # 6. Caption Results
    # ========================================================

    caption_result = st.session_state.get(
        "caption_result"
    )

    if not caption_result:
        return

    st.divider()

    st.subheader(
        "📄 Generated Captions"
    )

    srt_path = Path(
        caption_result[
            "srt_path"
        ]
    )

    vtt_path = Path(
        caption_result[
            "vtt_path"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**SRT:** `{srt_path.name}`"
        )

        if srt_path.is_file():

            st.download_button(
                label="⬇️ Download SRT",
                data=srt_path.read_bytes(),
                file_name=srt_path.name,
                mime="application/x-subrip",
            )

    with col2:

        st.write(
            f"**VTT:** `{vtt_path.name}`"
        )

        if vtt_path.is_file():

            st.download_button(
                label="⬇️ Download VTT",
                data=vtt_path.read_bytes(),
                file_name=vtt_path.name,
                mime="text/vtt",
            )

    # ========================================================
    # 7. Caption Preview
    # ========================================================

    st.subheader(
        "👀 Caption Preview"
    )

    segments = caption_result.get(
        "segments",
        [],
    )

    if segments:

        for index, segment in enumerate(
            segments[:10],
            start=1,
        ):

            st.write(
                f"**{index}.** "
                f"`{segment.start:.2f}s → "
                f"{segment.end:.2f}s` "
                f"{segment.text}"
            )

        if len(segments) > 10:

            st.caption(
                f"Showing first 10 of "
                f"{len(segments)} captions."
            )

    # ========================================================
    # 7. Saved Transcript
    # ========================================================

    transcript_path_value = st.session_state.get(
        "transcript_path"
    )

    if transcript_path_value:
        transcript_path = Path(
            transcript_path_value
        )

        if transcript_path.is_file():
            st.subheader(
                "📝 Generated Transcript"
            )

            st.write(
                f"**Transcript:** "
                f"`{transcript_path.name}`"
            )

            st.download_button(
                label="⬇️ Download Transcript",
                data=transcript_path.read_bytes(),
                file_name=transcript_path.name,
                mime="text/plain",
                key=(
                    f"download_transcript_"
                    f"{transcript_path}"
                ),
            )

    # ========================================================
    # 8. Burn Captions
    # ========================================================

    st.divider()

    st.subheader(
        "🔥 Burn Captions Into Video"
    )

    if st.button(
        "🔥 Burn Captions Into Video",
        type="primary",
    ):

        with st.spinner(
            "Burning captions into video..."
        ):

            try:

                agent = create_caption_agent()

                result = (
                    agent.generate_captioned_video(
                        video_path=video_path,
                        caption_language=(
                            selected_language
                        ),
                    )
                )

                st.session_state[
                    "captioned_video_path"
                ] = str(
                    result[
                        "output_video"
                    ]
                )

                st.success(
                    "Captioned video created successfully!"
                )

            except Exception as exc:

                st.error(
                    f"Video captioning failed: {exc}"
                )

    # ========================================================
    # 9. Final Video
    # ========================================================

    captioned_video_value = (
        st.session_state.get(
            "captioned_video_path"
        )
    )

    if captioned_video_value:

        captioned_video_path = Path(
            captioned_video_value
        )

        if captioned_video_path.is_file():

            st.divider()

            st.subheader(
                "🎥 Final Captioned Video"
            )

            st.write(
                f"**Output:** "
                f"`{captioned_video_path.name}`"
            )

            st.video(
                str(
                    captioned_video_path
                )
            )

            st.download_button(
                label=(
                    "⬇️ Download "
                    "Captioned Video"
                ),
                data=(
                    captioned_video_path
                    .read_bytes()
                ),
                file_name=(
                    captioned_video_path.name
                ),
                mime="video/mp4",
            )


# ============================================================
# Captions Page
# ============================================================

def render_captions() -> None:
    """Render generated caption files."""

    st.title("📄 Captions")

    st.write(
        "Browse generated SRT and VTT caption files."
    )

    st.divider()

    if not CAPTION_DIR.exists():

        st.info(
            "No caption files have been generated yet."
        )

        return

    caption_files = sorted(
        [
            path
            for path in CAPTION_DIR.iterdir()
            if path.is_file()
            and path.suffix.lower()
            in {".srt", ".vtt"}
        ],
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )

    if not caption_files:

        st.info(
            "No caption files have been generated yet."
        )

        return

    for caption_file in caption_files:

        with st.expander(
            f"📄 {caption_file.name}"
        ):

            st.write(
                f"**Path:** `{caption_file}`"
            )

            content = caption_file.read_text(
                encoding="utf-8"
            )

            st.code(
                content,
                language="text",
            )

            mime = (
                "application/x-subrip"
                if caption_file.suffix.lower()
                == ".srt"
                else "text/vtt"
            )

            st.download_button(
                label=(
                    f"⬇️ Download "
                    f"{caption_file.name}"
                ),
                data=content,
                file_name=caption_file.name,
                mime=mime,
                key=f"download_{caption_file}",
            )


# ============================================================
# Settings
# ============================================================

def render_settings() -> None:
    """Render application settings."""

    st.title("⚙️ Settings")

    st.write(
        "Configure caption-generation preferences."
    )

    st.divider()

    # ========================================================
    # Whisper
    # ========================================================

    st.subheader("📝 Whisper Model")

    whisper_models = [
        "tiny",
        "base",
        "small",
        "medium",
        "large",
    ]

    current_whisper = st.session_state.get(
        "whisper_model",
        "base",
    )

    whisper_model = st.selectbox(
        "Whisper model",
        whisper_models,
        index=(
            whisper_models.index(current_whisper)
            if current_whisper in whisper_models
            else whisper_models.index("base")
        ),
        help=(
            "Larger models may improve transcription "
            "quality but require more resources."
        ),
    )

    st.session_state["whisper_model"] = whisper_model

    st.divider()

    # ========================================================
    # Translation Provider
    # ========================================================

    st.subheader("🤖 Translation Provider")

    translation_providers = {
        "Ollama": {
            "key": "ollama",
            "model": "qwen2.5:1.5b",
        },
        "OpenAI": {
            "key": "openai",
            "model": "gpt-5-mini",
        },
        "Anthropic": {
            "key": "anthropic",
            "model": "claude-sonnet-4-5",
        },
        "Gemini": {
            "key": "gemini",
            "model": "gemini-3.6-flash",
        },
        "Mistral": {
            "key": "mistral",
            "model": "mistral-medium-latest",
        },
        "Groq": {
            "key": "groq",
            "model": "llama-3.1-8b-instant",
        },
        "Cohere": {
            "key": "cohere",
            "model": "command-a-03-2025",
        },
        "DeepSeek": {
            "key": "deepseek",
            "model": "deepseek-v4-flash",
        },
    }

    provider_names = list(
        translation_providers.keys()
    )

    current_provider = st.session_state.get(
        "translation_provider",
        "ollama",
    )

    provider_keys = [
        config["key"]
        for config in translation_providers.values()
    ]

    provider_index = (
        provider_keys.index(current_provider)
        if current_provider in provider_keys
        else 0
    )

    selected_provider = st.selectbox(
        "AI provider",
        provider_names,
        index=provider_index,
        help=(
            "Select the AI provider used for "
            "caption translation."
        ),
    )

    provider_config = translation_providers[
        selected_provider
    ]

    provider_key = provider_config["key"]
    translation_model = provider_config["model"]

    st.session_state[
        "translation_provider"
    ] = provider_key

    st.session_state[
        "translation_model"
    ] = translation_model

    st.text_input(
        "Translation model",
        value=translation_model,
        disabled=True,
    )

    st.caption(
        f"Provider: **{selected_provider}**  |  "
        f"Model: `{translation_model}`"
    )

    # ========================================================
    # Provider Status
    # ========================================================

    if provider_key == "ollama":

        st.success(
            "🟢 Ollama is a local provider."
        )

        st.caption(
            "No cloud API key is required."
        )

    elif provider_key == "openai":

        if os.getenv("OPENAI_API_KEY"):
            st.success(
                "🟢 OpenAI API key configured."
            )
        else:
            st.warning(
                "🔴 OpenAI API key is missing."
            )

        st.caption(
            "API key is read from OPENAI_API_KEY."
        )

    elif provider_key == "anthropic":

        if os.getenv("ANTHROPIC_API_KEY"):
            st.success(
                "🟢 Anthropic API key configured."
            )
        else:
            st.warning(
                "🔴 Anthropic API key is missing."
            )

        st.caption(
            "API key is read from ANTHROPIC_API_KEY."
        )

    elif provider_key == "gemini":

        if os.getenv("GEMINI_API_KEY"):
            st.success(
                "🟢 Gemini API key configured."
            )
        else:
            st.warning(
                "🔴 Gemini API key is missing."
            )

        st.caption(
            "API key is read from GEMINI_API_KEY."
        )

    st.divider()

    # ========================================================
    # Available Providers
    # ========================================================

    st.subheader("🌐 Available AI Providers")

    columns = st.columns(4)

    for column, (
        provider_name,
        config,
    ) in zip(
        columns,
        translation_providers.items(),
    ):

        with column:

            st.markdown(
                f"### {provider_name}"
            )

            st.caption(
                config["model"]
            )

            if config["key"] == "ollama":

                st.write("🟢 Local")

            elif config["key"] == "openai":

                status = (
                    "🟢 Configured"
                    if os.getenv("OPENAI_API_KEY")
                    else "🔴 Missing"
                )

                st.write(status)

            elif config["key"] == "anthropic":

                status = (
                    "🟢 Configured"
                    if os.getenv("ANTHROPIC_API_KEY")
                    else "🔴 Missing"
                )

                st.write(status)

            elif config["key"] == "gemini":

                status = (
                    "🟢 Configured"
                    if os.getenv("GEMINI_API_KEY")
                    else "🔴 Missing"
                )

                st.write(status)

    st.divider()

    # ========================================================
    # Caption Language
    # ========================================================

    st.subheader(
        "🌐 Default Caption Language"
    )

    default_language = st.selectbox(
        "Default language",
        options=list(
            CAPTION_LANGUAGES.keys()
        ),
        index=0,
    )

    st.session_state[
        "default_caption_language"
    ] = CAPTION_LANGUAGES[
        default_language
    ]

    st.success(
        "Settings are saved for this session."
    )

    st.divider()

    # ========================================================
    # Directories
    # ========================================================

    st.subheader(
        "📁 Application Directories"
    )

    st.code(
        f"Uploads:  {UPLOAD_DIR}\n"
        f"Captions: {CAPTION_DIR}\n"
        f"Outputs:  {OUTPUT_DIR}",
        language="text",
    )


# ============================================================
# Help
# ============================================================

def render_help() -> None:
    """Render the help page."""

    st.title("❓ Help")

    st.write(
        "Learn how to use the AI Video Caption Generator."
    )

    st.divider()

    st.subheader(
        "🚀 How to Use"
    )

    steps = [
        "Upload your video.",
        "Save the video.",
        "Detect the spoken language.",
        "Select the caption language.",
        "Generate captions.",
        "Review the SRT/VTT captions.",
        "Burn captions into the video.",
        "Preview and download the final video.",
    ]

    for index, step in enumerate(
        steps,
        start=1,
    ):
        st.write(
            f"**{index}.** {step}"
        )

    st.divider()

    st.subheader(
        "🎬 Supported Video Formats"
    )

    st.write(
        "MP4, MOV, AVI, MKV, and WebM."
    )

    st.divider()

    st.subheader(
        "📄 Caption Formats"
    )

    st.write(
        "SRT and VTT."
    )

    st.divider()

    st.subheader(
        "🤖 AI Processing"
    )

    st.write(
        "Whisper provides internal timestamped "
        "transcription."
    )

    st.write(
        "Ollama provides local AI translation."
    )

    st.divider()

    st.subheader(
        "🔥 FFmpeg"
    )

    st.write(
        "FFmpeg permanently burns captions into "
        "the final video."
    )

    st.divider()

    st.subheader(
        "🛠️ Troubleshooting"
    )

    with st.expander(
        "Ollama connection error"
    ):

        st.code(
            "ollama --version\n"
            "ollama list\n"
            "ollama serve",
            language="powershell",
        )

    with st.expander(
        "FFmpeg connection error"
    ):

        st.code(
            "ffmpeg -version",
            language="powershell",
        )


# ============================================================
# About
# ============================================================

def render_about() -> None:
    """Render the About page."""

    st.title("ℹ️ About")

    st.write(
        "## 🎬 AI Video Caption Generator"
    )

    st.write(
        "An AI-powered application for generating "
        "multilingual captions from videos."
    )

    st.divider()

    st.subheader(
        "✨ Core Workflow"
    )

    st.code(
        "Video\n"
        "  ↓\n"
        "Whisper Transcript\n"
        "  ↓\n"
        "Language Detection\n"
        "  ↓\n"
        "Caption Language Selection\n"
        "  ↓\n"
        "Local Ollama Model\n"
        "  ↓\n"
        "SRT / VTT\n"
        "  ↓\n"
        "FFmpeg\n"
        "  ↓\n"
        "Captioned Video",
        language="text",
    )

    st.divider()

    st.subheader(
        "🧰 Technology Stack"
    )

    technologies = [
        "Python",
        "Streamlit",
        "OpenAI Whisper",
        "Ollama",
        "Qwen2.5 1.5B",
        "FFmpeg",
        "PyTest",
        "JSON storage",
    ]

    for technology in technologies:

        st.write(
            f"• {technology}"
        )

    st.divider()

    st.subheader(
        "📦 Project Scope"
    )

    st.write(
        "The application is focused specifically "
        "on video caption generation."
    )

    st.write(
        "Transcript data is used internally during "
        "processing and is not maintained as a "
        "separate transcript-history feature."
    )

    st.divider()

    st.caption(
        f"AI Video Caption Generator • "
        f"v{APP_VERSION}"
    )


# ============================================================
# Main Router
# ============================================================

def main() -> None:
    """Run the selected application page."""

    page = render_sidebar()

    if page == "🏠 Dashboard":

        render_dashboard()

    elif page == "🎬 Caption Generator":

        render_caption_generator()

    elif page == "📄 Captions":

        render_captions()

    elif page == "⚙️ Settings":

        render_settings()

    elif page == "❓ Help":

        render_help()

    elif page == "ℹ️ About":

        render_about()


if __name__ == "__main__":
    main()