"""AI Video Caption Generator application."""

import os
from datetime import datetime
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from agents.caption_agent import CaptionAgent
from agents.dashboard_agent import DashboardAgent
from providers.translation_provider_factory import (
    TranslationProviderFactory,
)
from services.caption_file_service import CaptionFileService
from services.caption_generation_service import (
    CaptionGenerationService,
)
from services.transcript_service import TranscriptService
from services.video_caption_burn_service import (
    VideoCaptionBurnService,
)

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

APP_VERSION = "1.4.1"

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

THEMES = {
    # ========================================================
    # DARK THEMES — EXISTING
    # ========================================================
    "🌙 Dark": {
        "background": "#0e1117",
        "sidebar": "#161b22",
        "text": "#f5f7fa",
        "accent": "#58a6ff",
    },
    "🌌 Midnight Blue": {
        "background": "#07111f",
        "sidebar": "#081525",
        "text": "#f5f7fa",
        "accent": "#38bdf8",
    },
    "💜 Cosmic Purple": {
        "background": "#10091f",
        "sidebar": "#120a24",
        "text": "#faf7ff",
        "accent": "#d946ef",
    },
    "🌊 Ocean": {
        "background": "#061a1f",
        "sidebar": "#071e25",
        "text": "#effcff",
        "accent": "#22d3ee",
    },
    "🌿 Emerald": {
        "background": "#07170f",
        "sidebar": "#081b12",
        "text": "#f2fff6",
        "accent": "#34d399",
    },
    # ========================================================
    # LIGHT THEMES — NEW
    # ========================================================
    # ========================================================
    # LIGHT THEMES
    # ========================================================
    "☀️ Light": {
        "background": "#ffffff",
        "sidebar": "#f8fafc",
        "text": "#000000",
        "accent": "#2563eb",
    },
    "🌤️ Sky Light": {
        "background": "#f0f9ff",
        "sidebar": "#e0f2fe",
        "text": "#000000",
        "accent": "#0284c7",
    },
    "💜 Lavender Light": {
        "background": "#faf5ff",
        "sidebar": "#f3e8ff",
        "text": "#000000",
        "accent": "#9333ea",
    },
    "🌿 Mint Light": {
        "background": "#f0fdf4",
        "sidebar": "#dcfce7",
        "text": "#000000",
        "accent": "#16a34a",
    },
    "🌊 Aqua Light": {
        "background": "#ecfeff",
        "sidebar": "#cffafe",
        "text": "#000000",
        "accent": "#0891b2",
    },
    "🌸 Rose Light": {
        "background": "#fff1f2",
        "sidebar": "#ffe4e6",
        "text": "#000000",
        "accent": "#e11d48",
    },
    "🍑 Peach Light": {
        "background": "#fff7ed",
        "sidebar": "#ffedd5",
        "text": "#000000",
        "accent": "#ea580c",
    },
    "🌼 Amber Light": {
        "background": "#fffbeb",
        "sidebar": "#fef3c7",
        "text": "#000000",
        "accent": "#d97706",
    },
    "🩵 Ice Light": {
        "background": "#f8fafc",
        "sidebar": "#e2e8f0",
        "text": "#000000",
        "accent": "#475569",
    },
    "🌱 Sage Light": {
        "background": "#f6fdf8",
        "sidebar": "#e7f5ea",
        "text": "#000000",
        "accent": "#4d8b5b",
    },
}


def apply_theme(theme_name: str) -> None:
    """Apply the selected application theme."""

    theme = THEMES[theme_name]

    # Light themes have black application text.
    light_theme = theme_name in {
        "☀️ Light",
        "🌤️ Sky Light",
        "💜 Lavender Light",
        "🌿 Mint Light",
        "🌊 Aqua Light",
        "🌸 Rose Light",
        "🍑 Peach Light",
        "🌼 Amber Light",
        "🩵 Ice Light",
        "🌱 Sage Light",
    }

    st.markdown(
        f"""
        <style>

        /* ====================================================
           MAIN APPLICATION
           ==================================================== */

        .stApp {{
            background-color: {theme["background"]} !important;
            color: {theme["text"]} !important;
        }}

        .stAppHeader {{
            background-color: {theme["background"]} !important;
        }}

        /* Main page text */
        .stApp p,
        .stApp label,
        .stApp span,
        .stApp h1,
        .stApp h2,
        .stApp h3,
        .stApp h4,
        .stApp h5,
        .stApp h6,
        .stApp li,
        .stApp strong,
        .stApp small {{
            color: {theme["text"]} !important;
        }}

        /* Markdown */
        [data-testid="stMarkdownContainer"] {{
            color: {theme["text"]} !important;
        }}

        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] span,
        [data-testid="stMarkdownContainer"] strong,
        [data-testid="stMarkdownContainer"] li {{
            color: {theme["text"]} !important;
        }}

        /* ====================================================
           SIDEBAR
           ==================================================== */

        [data-testid="stSidebar"] {{
            background-color: {theme["sidebar"]} !important;
        }}

        [data-testid="stSidebar"] * {{
            color: {theme["text"]} !important;
        }}

        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] h4 {{
            color: {theme["text"]} !important;
        }}

        /* ====================================================
           BUTTONS
           ==================================================== */

        .stButton > button {{
            border-color: {theme["accent"]} !important;
        }}

        .stButton > button:hover {{
            border-color: {theme["accent"]} !important;
        }}

        /* ====================================================
           SELECTBOX - CLOSED SELECT
           ==================================================== */

        [data-baseweb="select"] > div {{
            background-color: #1f2937 !important;
            border-color: {theme["accent"]} !important;
            color: #ffffff !important;
        }}

        [data-baseweb="select"] > div * {{
            color: #ffffff !important;
        }}

        [data-baseweb="select"] span {{
            color: #ffffff !important;
        }}

        [data-baseweb="select"] input {{
            color: #ffffff !important;
        }}

        /* Selectbox arrow */
        [data-baseweb="select"] svg {{
            fill: #ffffff !important;
            color: #ffffff !important;
        }}

        /* ====================================================
           SELECTBOX - OPEN DROPDOWN
           ==================================================== */

        [data-baseweb="popover"] {{
            background-color: #1f2937 !important;
        }}

        [data-baseweb="popover"] > div {{
            background-color: #1f2937 !important;
        }}

        [data-baseweb="menu"] {{
            background-color: #1f2937 !important;
        }}

        [data-baseweb="menu"] * {{
            background-color: #1f2937 !important;
            color: #ffffff !important;
        }}

        [role="listbox"] {{
            background-color: #1f2937 !important;
        }}

        [role="option"] {{
            background-color: #1f2937 !important;
            color: #ffffff !important;
        }}

        [role="option"] * {{
            color: #ffffff !important;
        }}

        [role="option"]:hover {{
            background-color: {theme["accent"]} !important;
            color: #ffffff !important;
        }}

        /* ====================================================
           TEXT INPUTS
           ==================================================== */

        [data-baseweb="input"] {{
            border-color: {theme["accent"]} !important;
        }}

        /* ====================================================
           EXPANDERS
           ==================================================== */

        [data-testid="stExpander"] {{
            border-color: {theme["accent"]} !important;
        }}

        /* ====================================================
           FILE UPLOADER
           ==================================================== */

        [data-testid="stFileUploader"] {{
            border-color: {theme["accent"]} !important;
        }}

        /* ====================================================
           LINKS
           ==================================================== */

        a {{
            color: {theme["accent"]} !important;
        }}

        /* ====================================================
           DIVIDERS
           ==================================================== */

        hr {{
            border-color: {theme["accent"]} !important;
        }}
        
        /* Caption text */
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] * {{
    color: {theme["text"]} !important;
}}

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <style>

        [data-testid="stMetric"] {{
            color: {theme["text"]} !important;
        }}

        [data-testid="stMetric"] label {{
            color: {theme["text"]} !important;
        }}

        [data-testid="stMetricLabel"] {{
            color: {theme["text"]} !important;
        }}

        [data-testid="stMetricLabel"] * {{
            color: {theme["text"]} !important;
        }}

        [data-testid="stMetricValue"] {{
            color: {theme["text"]} !important;
        }}

        [data-testid="stMetricValue"] * {{
            color: {theme["text"]} !important;
        }}

        [data-testid="stMetricValue"] div {{
            color: {theme["text"]} !important;
        }}
        
        # ====================================================
# RECENT FILES
# ====================================================

.recent-file {{
    background-color: {theme["sidebar"]} !important;
    border: 1px solid {theme["accent"]} !important;
    border-radius: 10px;
    padding: 12px 16px;
    margin-bottom: 10px;
}}

.recent-file-name {{
    color: {theme["text"]} !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}}

.recent-file-info {{
    color: {theme["text"]} !important;
    opacity: 0.85 !important;
    font-size: 13px !important;
}}

.recent-file-type {{
    color: {theme["accent"]} !important;
    font-weight: 700 !important;
    font-size: 13px !important;
}}

.recent-file-path {{
    color: {theme["text"]} !important;
    opacity: 0.85 !important;
    font-size: 13px !important;
}}

        [data-testid="stMetricValue"] p {{
            color: {theme["text"]} !important;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )


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

    filename_timestamp = generated_at.strftime("%Y%m%d_%H%M%S")

    transcript_path = TRANSCRIPT_DIR / f"{video_path.stem}_{filename_timestamp}.txt"

    lines = [
        f"Transcript: {video_path.name}",
        f"Generated: {generated_at.isoformat(timespec='seconds')}",
        "",
    ]

    for index, segment in enumerate(
        segments,
        start=1,
    ):
        start = float(getattr(segment, "start", 0.0))

        end = float(getattr(segment, "end", 0.0))

        transcript_text = str(getattr(segment, "text", "")).strip()

        if not transcript_text:
            continue

        lines.append(
            f"{index:04d} | " f"[{start:08.2f} --> {end:08.2f}] " f"{transcript_text}"
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

        st.markdown("### 🎨 Theme")

        theme_names = list(THEMES.keys())

        current_theme = st.session_state.get(
            "app_theme",
            theme_names[0],
        )

        selected_theme = st.selectbox(
            "Theme",
            theme_names,
            index=(
                theme_names.index(current_theme) if current_theme in theme_names else 0
            ),
            key="sidebar_theme",
        )

        st.session_state["app_theme"] = selected_theme

        apply_theme(selected_theme)

        st.divider()

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

        provider_keys = [config["key"] for config in translation_providers.values()]

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

        current_model = st.session_state.get("translation_model")

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

            st.success("🟢 Local")

        elif provider_key == "openai":

            if os.getenv("OPENAI_API_KEY"):
                st.success("🟢 API key configured")
            else:
                st.warning("🔴 API key missing")

        elif provider_key == "anthropic":

            if os.getenv("ANTHROPIC_API_KEY"):
                st.success("🟢 API key configured")
            else:
                st.warning("🔴 API key missing")

        elif provider_key == "gemini":

            if os.getenv("GEMINI_API_KEY"):
                st.success("🟢 API key configured")
            else:
                st.warning("🔴 API key missing")

        elif provider_key == "mistral":

            if os.getenv("MISTRAL_API_KEY"):
                st.success("🟢 API key configured")
            else:
                st.warning("🔴 API key missing")

        elif provider_key == "groq":

            if os.getenv("GROQ_API_KEY"):
                st.success("🟢 API key configured")
            else:
                st.warning("🔴 API key missing")

        elif provider_key == "cohere":

            if os.getenv("COHERE_API_KEY"):
                st.success("🟢 API key configured")
            else:
                st.warning("🔴 API key missing")

        elif provider_key == "deepseek":

            if os.getenv("DEEPSEEK_API_KEY"):
                st.success("🟢 API key configured")
            else:
                st.warning("🔴 API key missing")

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
                for name, code in CAPTION_LANGUAGES.items()
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

        st.caption("AI Video Caption Generator")

        st.caption(f"Version {APP_VERSION}")

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

    output_path = UPLOAD_DIR / Path(uploaded_file.name).name

    output_path.write_bytes(uploaded_file.getbuffer())

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

    environment_variable = environment_variables.get(provider_name)

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

    translation_provider = TranslationProviderFactory.create(
        provider_name,
        **provider_kwargs,
    )

    # --------------------------------------------------------
    # Caption Generation
    # --------------------------------------------------------

    caption_generation_service = CaptionGenerationService(
        translation_provider=translation_provider,
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

    video_caption_burn_service = VideoCaptionBurnService(
        OUTPUT_DIR,
    )

    # --------------------------------------------------------
    # Caption Agent
    # --------------------------------------------------------

    return CaptionAgent(
        transcript_service=transcript_service,
        caption_generation_service=(caption_generation_service),
        caption_file_service=caption_file_service,
        video_caption_burn_service=(video_caption_burn_service),
    )


# ============================================================
# Dashboard
# ============================================================


def render_dashboard() -> None:
    """Render the dashboard page."""

    st.title("🏠 Dashboard")

    st.write("Overview of your AI Video Caption Generator.")

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
        st.info("No files available yet.")
        return

    for file_info in recent_files:
        st.write(f"**{file_info['name']}**")

        st.caption(f"Type: {file_info['type']}  " f"| Path: {file_info['path']}")


# ============================================================
# Caption Generator
# ============================================================


def render_caption_generator() -> None:
    """Render the complete caption generation workflow."""

    st.title("🎬 AI Video Caption Generator")

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
        help=("Upload a video to generate captions."),
    )

    if uploaded_file is None:
        st.info("Upload a video to begin the caption workflow.")

        return

    st.success(f"Selected video: {uploaded_file.name}")

    st.video(uploaded_file)

    if st.button(
        "📥 Save Video",
        type="primary",
    ):
        video_path = save_uploaded_video(uploaded_file)

        st.session_state["video_path"] = str(video_path)

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

        st.success(f"Video saved: {video_path.name}")

    # ========================================================
    # 2. Current Video
    # ========================================================

    video_path_value = st.session_state.get("video_path")

    if not video_path_value:
        return

    video_path = Path(video_path_value)

    st.divider()

    st.subheader("🎬 Current Video")

    st.write(f"**Video:** `{video_path.name}`")

    # ========================================================
    # 3. Language Detection
    # ========================================================

    st.subheader("🌐 Language Detection")

    if st.button("🔍 Detect Video Language"):

        with st.spinner("Detecting spoken language..."):

            try:

                agent = create_caption_agent()

                detection = agent.detect_language(video_path)

                st.session_state["detected_language"] = detection

            except Exception as exc:

                st.error(f"Language detection failed: {exc}")

    detected_language = st.session_state.get("detected_language")

    if detected_language:
        language_name = detected_language.get(
            "language_name",
            detected_language.get(
                "language",
                "Unknown",
            ),
        )

        language_code = detected_language.get(
            "language",
            "",
        )

        st.success(f"Detected language: " f"{language_name} " f"({language_code})")

    # ========================================================
    # 4. Caption Language
    # ========================================================

    st.divider()

    st.subheader("💬 Caption Language")

    selected_language_name = st.selectbox(
        "Select the language for captions",
        options=list(CAPTION_LANGUAGES.keys()),
    )

    selected_language = CAPTION_LANGUAGES[selected_language_name]

    st.session_state["caption_language"] = selected_language

    st.info(f"Caption language: " f"{selected_language_name} " f"({selected_language})")

    # ========================================================
    # 5. Generate Captions
    # ========================================================

    st.divider()

    st.subheader("✨ Generate Captions")

    st.write(
        "The video will be transcribed internally, "
        "translated with the configured AI provider, "
        "and converted into SRT and VTT caption files."
    )

    if st.button(
        "✨ Generate Captions",
        type="primary",
    ):

        with st.spinner("Generating captions..."):

            try:

                agent = create_caption_agent()

                result = agent.generate_caption_files(
                    video_path=video_path,
                    caption_language=(selected_language),
                )

                st.session_state["caption_result"] = result

                transcript_path = save_generated_transcript(
                    video_path=video_path,
                    segments=result.get(
                        "segments",
                        [],
                    ),
                )

                if transcript_path:
                    st.session_state["transcript_path"] = str(transcript_path)

                st.success("Captions generated successfully!")

                if transcript_path:
                    st.info(f"Transcript saved: " f"{transcript_path.name}")

            except Exception as exc:

                st.error(f"Caption generation failed: {exc}")

    # ========================================================
    # 6. Caption Results
    # ========================================================

    caption_result = st.session_state.get("caption_result")

    if not caption_result:
        return

    st.divider()

    st.subheader("📄 Generated Captions")

    srt_path = Path(caption_result["srt_path"])

    vtt_path = Path(caption_result["vtt_path"])

    col1, col2 = st.columns(2)

    with col1:

        st.write(f"**SRT:** `{srt_path.name}`")

        if srt_path.is_file():
            st.download_button(
                label="⬇️ Download SRT",
                data=srt_path.read_bytes(),
                file_name=srt_path.name,
                mime="application/x-subrip",
            )

    with col2:

        st.write(f"**VTT:** `{vtt_path.name}`")

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

    st.subheader("👀 Caption Preview")

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
            st.caption(f"Showing first 10 of " f"{len(segments)} captions.")

    # ========================================================
    # 7. Saved Transcript
    # ========================================================

    transcript_path_value = st.session_state.get("transcript_path")

    if transcript_path_value:
        transcript_path = Path(transcript_path_value)

        if transcript_path.is_file():
            st.subheader("📝 Generated Transcript")

            st.write(f"**Transcript:** " f"`{transcript_path.name}`")

            st.download_button(
                label="⬇️ Download Transcript",
                data=transcript_path.read_bytes(),
                file_name=transcript_path.name,
                mime="text/plain",
                key=(f"download_transcript_" f"{transcript_path}"),
            )

    # ========================================================
    # 8. Burn Captions
    # ========================================================

    st.divider()

    st.subheader("🔥 Burn Captions Into Video")

    if st.button(
        "🔥 Burn Captions Into Video",
        type="primary",
    ):

        with st.spinner("Burning captions into video..."):

            try:

                agent = create_caption_agent()

                result = agent.generate_captioned_video(
                    video_path=video_path,
                    caption_language=(selected_language),
                )

                st.session_state["captioned_video_path"] = str(result["output_video"])

                st.success("Captioned video created successfully!")

            except Exception as exc:

                st.error(f"Video captioning failed: {exc}")

    # ========================================================
    # 9. Final Video
    # ========================================================

    captioned_video_value = st.session_state.get("captioned_video_path")

    if captioned_video_value:

        captioned_video_path = Path(captioned_video_value)

        if captioned_video_path.is_file():
            st.divider()

            st.subheader("🎥 Final Captioned Video")

            st.write(f"**Output:** " f"`{captioned_video_path.name}`")

            st.video(str(captioned_video_path))

            st.download_button(
                label=("⬇️ Download " "Captioned Video"),
                data=(captioned_video_path.read_bytes()),
                file_name=(captioned_video_path.name),
                mime="video/mp4",
            )


# ============================================================
# Captions Page
# ============================================================


def render_captions() -> None:
    """Render generated caption files."""

    st.title("📄 Captions")

    st.write("Browse generated SRT and VTT caption files.")

    st.divider()

    if not CAPTION_DIR.exists():
        st.info("No caption files have been generated yet.")

        return

    caption_files = sorted(
        [
            path
            for path in CAPTION_DIR.iterdir()
            if path.is_file() and path.suffix.lower() in {".srt", ".vtt"}
        ],
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )

    if not caption_files:
        st.info("No caption files have been generated yet.")

        return

    for caption_file in caption_files:
        with st.expander(f"📄 {caption_file.name}"):
            st.write(f"**Path:** `{caption_file}`")

            content = caption_file.read_text(encoding="utf-8")

            st.code(
                content,
                language="text",
            )

            mime = (
                "application/x-subrip"
                if caption_file.suffix.lower() == ".srt"
                else "text/vtt"
            )

            st.download_button(
                label=(f"⬇️ Download " f"{caption_file.name}"),
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
        "Configure caption-generation preferences, "
        "AI providers, models, and output options."
    )

    st.divider()

    # ========================================================
    # Theme
    # ========================================================

    st.subheader("🎨 Application Theme")

    st.caption("Select the visual theme used throughout the application.")

    theme_names = list(THEMES.keys())

    current_theme = st.session_state.get(
        "theme",
        theme_names[0],
    )

    theme_index = (
        theme_names.index(current_theme) if current_theme in theme_names else 0
    )

    selected_theme = st.selectbox(
        "Theme",
        options=theme_names,
        index=theme_index,
        key="settings_theme",
        help=("Choose a dark or light theme for the application."),
    )

    st.session_state["theme"] = selected_theme

    theme_config = THEMES[selected_theme]

    st.caption(f"Selected theme: **{selected_theme}**")

    st.write(
        f"Background: `{theme_config['background']}`  |  "
        f"Sidebar: `{theme_config['sidebar']}`  |  "
        f"Text: `{theme_config['text']}`  |  "
        f"Accent: `{theme_config['accent']}`"
    )

    st.divider()

    # ========================================================
    # Whisper Model
    # ========================================================

    st.subheader("📝 Whisper Model")

    st.caption(
        "Select the Whisper model used for speech "
        "transcription and language detection."
    )

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

    whisper_index = (
        whisper_models.index(current_whisper)
        if current_whisper in whisper_models
        else whisper_models.index("base")
    )

    whisper_model = st.selectbox(
        "Whisper model",
        whisper_models,
        index=whisper_index,
        help=(
            "Larger models may improve transcription "
            "quality but require more resources."
        ),
    )

    st.session_state["whisper_model"] = whisper_model

    st.info(f"Selected Whisper model: **{whisper_model}**")

    st.divider()

    # ========================================================
    # Translation Provider
    # ========================================================

    st.subheader("🤖 Translation Provider")

    st.caption("Select the AI provider used for caption translation.")

    TRANSLATION_PROVIDERS = {
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

    # ========================================================
    # Translation Provider
    # ========================================================

    st.subheader("🤖 Translation Provider")

    provider_names = list(TRANSLATION_PROVIDERS.keys())

    current_provider = st.session_state.get(
        "translation_provider",
        "ollama",
    )

    provider_keys = [config["key"] for config in TRANSLATION_PROVIDERS.values()]

    provider_index = (
        provider_keys.index(current_provider)
        if current_provider in provider_keys
        else 0
    )

    selected_provider = st.selectbox(
        "AI provider",
        provider_names,
        index=provider_index,
        key="settings_translation_provider",
    )

    provider_config = TRANSLATION_PROVIDERS[selected_provider]

    provider_key = provider_config["key"]

    st.session_state["translation_provider"] = provider_key

    # ========================================================
    # Model Selection
    # ========================================================

    st.subheader("🧠 AI Model")

    available_models = provider_config["models"]

    current_model = st.session_state.get(
        "translation_model",
        available_models[0],
    )

    model_index = (
        available_models.index(current_model)
        if current_model in available_models
        else 0
    )

    selected_model = st.selectbox(
        "Translation model",
        available_models,
        index=model_index,
        key="settings_translation_model",
    )

    st.session_state["translation_model"] = selected_model

    st.caption(f"Provider: **{selected_provider}**  |  " f"Model: **{selected_model}**")

    # ========================================================
    # Provider Status
    # ========================================================

    st.markdown("### 🔐 Provider Status")

    if provider_key == "ollama":

        st.success("🟢 Local")

    elif provider_key == "openai":

        if os.getenv("OPENAI_API_KEY"):
            st.success("🟢 API key configured")
        else:
            st.warning("🔴 API key missing")

    elif provider_key == "anthropic":

        if os.getenv("ANTHROPIC_API_KEY"):
            st.success("🟢 API key configured")
        else:
            st.warning("🔴 API key missing")

    elif provider_key == "gemini":

        if os.getenv("GEMINI_API_KEY"):
            st.success("🟢 API key configured")
        else:
            st.warning("🔴 API key missing")

    elif provider_key == "mistral":

        if os.getenv("MISTRAL_API_KEY"):
            st.success("🟢 API key configured")
        else:
            st.warning("🔴 API key missing")

    elif provider_key == "groq":

        if os.getenv("GROQ_API_KEY"):
            st.success("🟢 API key configured")
        else:
            st.warning("🔴 API key missing")

    elif provider_key == "cohere":

        if os.getenv("COHERE_API_KEY"):
            st.success("🟢 API key configured")
        else:
            st.warning("🔴 API key missing")

    elif provider_key == "deepseek":

        if os.getenv("DEEPSEEK_API_KEY"):
            st.success("🟢 API key configured")
        else:
            st.warning("🔴 API key missing")

    st.divider()

    # ========================================================
    # Available AI Providers
    # ========================================================

    st.subheader("🌐 Available AI Providers")

    columns = st.columns(4)

    for index, (
        provider_name,
        config,
    ) in enumerate(TRANSLATION_PROVIDERS.items()):
        with columns[index % 4]:

            st.markdown(f"### {provider_name}")

            models = config.get(
                "models",
                [],
            )

            st.caption(f"{len(models)} models available")

            if models:
                with st.expander("🧠 Models"):
                    for model in models:
                        st.write(f"• {model}")

            provider_key = config["key"]

            if provider_key == "ollama":

                st.success("🟢 Local")

            elif provider_key == "openai":

                if os.getenv("OPENAI_API_KEY"):
                    st.success("🟢 API key configured")
                else:
                    st.warning("🔴 API key missing")

            elif provider_key == "anthropic":

                if os.getenv("ANTHROPIC_API_KEY"):
                    st.success("🟢 API key configured")
                else:
                    st.warning("🔴 API key missing")

            elif provider_key == "gemini":

                if os.getenv("GEMINI_API_KEY"):
                    st.success("🟢 API key configured")
                else:
                    st.warning("🔴 API key missing")

            elif provider_key == "mistral":

                if os.getenv("MISTRAL_API_KEY"):
                    st.success("🟢 API key configured")
                else:
                    st.warning("🔴 API key missing")

            elif provider_key == "groq":

                if os.getenv("GROQ_API_KEY"):
                    st.success("🟢 API key configured")
                else:
                    st.warning("🔴 API key missing")

            elif provider_key == "cohere":

                if os.getenv("COHERE_API_KEY"):
                    st.success("🟢 API key configured")
                else:
                    st.warning("🔴 API key missing")

            elif provider_key == "deepseek":

                if os.getenv("DEEPSEEK_API_KEY"):
                    st.success("🟢 API key configured")
                else:
                    st.warning("🔴 API key missing")

    # ========================================================
    # Caption Language
    # ========================================================

    st.subheader("🌐 Default Caption Language")

    st.caption("Select the default target language for " "generated captions.")

    language_names = list(CAPTION_LANGUAGES.keys())

    current_language_code = st.session_state.get(
        "default_caption_language",
        CAPTION_LANGUAGES["English"],
    )

    language_codes = list(CAPTION_LANGUAGES.values())

    language_index = (
        language_codes.index(current_language_code)
        if current_language_code in language_codes
        else 0
    )

    default_language = st.selectbox(
        "Default language",
        options=language_names,
        index=language_index,
        format_func=lambda language: (
            f"{language} " f"({CAPTION_LANGUAGES[language]})"
        ),
    )


# ============================================================
# Help
# ============================================================


def render_help() -> None:
    """Render the help page."""

    st.title("❓ Help")

    st.write("Learn how to use the AI Video Caption Generator.")

    st.divider()

    st.subheader("🚀 How to Use")

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
        st.write(f"**{index}.** {step}")

    st.divider()

    st.subheader("🎬 Supported Video Formats")

    st.write("MP4, MOV, AVI, MKV, and WebM.")

    st.divider()

    st.subheader("📄 Caption Formats")

    st.write("SRT and VTT.")

    st.divider()

    # ========================================================
    # AI Processing
    # ========================================================

    st.subheader("🤖 AI Processing")

    st.write(
        "AI-powered caption translation is supported through "
        "multiple providers and selectable models."
    )

    help_translation_providers = {
        "Ollama": [
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
        "OpenAI": [
            "gpt-5-mini",
            "gpt-4o",
            "gpt-4o-mini",
        ],
        "Anthropic": [
            "claude-sonnet-4-5",
            "claude-haiku-4-5",
            "claude-opus-4-1",
        ],
        "Gemini": [
            "gemini-3.6-flash",
            "gemini-2.5-flash",
            "gemini-2.5-pro",
        ],
        "Mistral": [
            "mistral-medium-latest",
            "mistral-large-latest",
            "mistral-small-latest",
        ],
        "Groq": [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "mixtral-8x7b-32768",
        ],
        "Cohere": [
            "command-a-03-2025",
            "command-r-plus",
            "command-r",
        ],
        "DeepSeek": [
            "deepseek-chat",
            "deepseek-reasoner",
            "deepseek-v4-flash",
        ],
    }

    for provider_name, models in help_translation_providers.items():
        with st.expander(f"🤖 {provider_name} " f"({len(models)} models)"):
            for model in models:
                st.write(f"• {model}")

    st.divider()

    st.subheader("🔥 FFmpeg")

    st.write("FFmpeg permanently burns captions into " "the final video.")

    st.divider()

    # ========================================================
    # Troubleshooting
    # ========================================================

    st.subheader("🛠️ Troubleshooting")

    troubleshooting_items = [
        (
            "🎥 Video upload fails",
            [
                "Make sure the selected file is a supported video format.",
                "Verify that the uploaded file is not corrupted.",
                "Check that the application has permission to access the upload directory.",
            ],
        ),
        (
            "📝 Transcription fails",
            [
                "Check that the selected Whisper model is available.",
                "Try a smaller Whisper model if system resources are limited.",
                "Verify that the video contains a usable audio track.",
            ],
        ),
        (
            "🌐 Original language is not detected",
            [
                "Make sure the video contains clear spoken audio.",
                "Try processing the video again.",
                "Check the Whisper model configuration.",
            ],
        ),
        (
            "🤖 AI translation fails",
            [
                "Verify that the selected provider is correctly configured.",
                "For cloud providers, check that the required API key is available.",
                "For Ollama, verify that the Ollama service is running.",
                "Verify that the selected model is available for the selected provider.",
            ],
        ),
        (
            "🦙 Ollama model is unavailable",
            [
                "Make sure Ollama is running locally.",
                "Verify that the selected model has been downloaded.",
                "Check that the model name exactly matches the installed Ollama model.",
            ],
        ),
        (
            "🔑 API key error",
            [
                "Verify that the provider API key is configured in the environment.",
                "Restart the application after changing environment variables.",
                "Make sure the API key belongs to the selected provider.",
            ],
        ),
        (
            "📄 SRT/VTT files are not generated",
            [
                "Check that transcription completed successfully.",
                "Verify that caption generation returned caption segments.",
                "Check the Captions output directory.",
            ],
        ),
        (
            "🎬 Caption burn fails",
            [
                "Make sure FFmpeg is installed and available.",
                "Verify that the generated SRT file exists.",
                "Check that the source video can be processed by FFmpeg.",
                "Try generating the caption files again before burning them.",
            ],
        ),
        (
            "💾 Generated files are missing",
            [
                "Check the Uploads, Captions, Outputs, and Transcripts directories.",
                "Verify that the workflow completed successfully.",
                "Check the application status and error messages.",
            ],
        ),
        (
            "🎨 Theme text is not visible",
            [
                "Open Settings and select the required theme.",
                "For light themes, caption and interface text should use the configured light-theme text color.",
                "Refresh the application after changing the theme.",
            ],
        ),
        (
            "🧠 Wrong model is selected",
            [
                "Open Settings.",
                "Select the required AI provider.",
                "Select the required model from the provider's model list.",
                "The selected provider and model are stored in the current session.",
            ],
        ),
        (
            "🔄 Settings are not reflected",
            [
                "Settings are maintained for the current application session.",
                "Verify the selected provider, model, Whisper model, language, and theme.",
                "Refresh the application if a UI change is not immediately visible.",
            ],
        ),
    ]

    for title, solutions in troubleshooting_items:

        with st.expander(title):

            for solution in solutions:
                st.write(f"• {solution}")

    # ========================================================
    # Configuration Diagnostics
    # ========================================================

    TRANSLATION_PROVIDERS = {
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

    st.subheader("🔍 Configuration Diagnostics")

    diagnostic_columns = st.columns(4)

    with diagnostic_columns[0]:
        st.metric(
            "AI Providers",
            len(TRANSLATION_PROVIDERS),
        )

    with diagnostic_columns[1]:
        st.metric(
            "Themes",
            len(THEMES),
        )

    with diagnostic_columns[2]:
        st.metric(
            "Caption Languages",
            len(CAPTION_LANGUAGES),
        )

    with diagnostic_columns[3]:
        st.metric(
            "Application Version",
            APP_VERSION,
        )

    st.caption(
        "Use these values to quickly verify the current " "application configuration."
    )


# ============================================================
# About
# ============================================================


def render_about() -> None:
    """Render the About page."""

    st.title("ℹ️ About")

    st.write("## 🎬 AI Video Caption Generator")

    st.write(
        "An AI-powered application for generating " "multilingual captions from videos."
    )

    st.success(f"🚀 Current Release: v{APP_VERSION}")

    st.divider()

    # ========================================================
    # Core Workflow
    # ========================================================

    st.subheader("✨ Core Workflow")

    st.code(
        "Video\n"
        "  ↓\n"
        "Whisper Transcript\n"
        "  ↓\n"
        "Language Detection\n"
        "  ↓\n"
        "Caption Language Selection\n"
        "  ↓\n"
        "AI Translation Provider\n"
        "  ↓\n"
        "SRT / VTT\n"
        "  ↓\n"
        "FFmpeg\n"
        "  ↓\n"
        "Captioned Video",
        language="text",
    )

    st.divider()

    # ========================================================
    # Version History
    # ========================================================

    st.subheader("📦 Version History")

    versions = [
        (
            "v1.4.1",
            "Current Release",
            [
                "Added 10 new light themes.",
                "15 themes are now available.",
                "Improved light-theme text visibility.",
                "Improved dropdown and selectbox readability.",
                "Improved caption text visibility.",
                "Improved Recent Files styling.",
                "Added main-page tab navigation.",
                "Dashboard is the default tab.",
                "Improved frontend theme consistency.",
                "267 tests passing.",
                "Black 26.5.1 formatting support.",
                "pip 26.2.1 upgrade.",
            ],
        ),
        (
            "v1.4.0",
            "Released",
            [
                "Completed the previous major feature release.",
                "Improved the video caption-generation workflow.",
                "Enhanced caption processing and reliability.",
                "Maintained comprehensive automated testing.",
            ],
        ),
        (
            "v1.3.0",
            "Released",
            [
                "Enhanced translation provider architecture.",
                "Improved provider configuration.",
                "Improved caption-generation workflow.",
                "Expanded AI provider integration.",
            ],
        ),
        (
            "v1.2.0",
            "Released",
            [
                "Improved caption generation.",
                "SRT and VTT caption support.",
                "Improved video processing.",
                "Improved testing and reliability.",
            ],
        ),
        (
            "v1.1.0",
            "Released",
            [
                "Initial caption-generation workflow.",
                "Video processing improvements.",
                "Translation integration.",
                "Caption file generation.",
            ],
        ),
        (
            "v1.0.0",
            "Initial Release",
            [
                "Initial AI Video Caption Generator application.",
                "Video upload and processing.",
                "Whisper transcription.",
                "AI-powered caption generation.",
                "SRT and VTT support.",
                "FFmpeg caption burning.",
            ],
        ),
    ]

    for version, status, changes in versions:
        with st.expander(
            f"🚀 {version} — {status}",
            expanded=(version == APP_VERSION),
        ):
            for change in changes:
                st.write(f"• {change}")

    st.divider()

    # ========================================================
    # Themes
    # ========================================================

    st.subheader("🎨 Available Themes")

    dark_themes = [
        "🌙 Dark",
        "🌌 Midnight Blue",
        "💜 Cosmic Purple",
        "🌊 Ocean",
        "🌿 Emerald",
    ]

    light_themes = [
        "☀️ Light",
        "🌤️ Sky Light",
        "💜 Lavender Light",
        "🌿 Mint Light",
        "🌊 Aqua Light",
        "🌸 Rose Light",
        "🍑 Peach Light",
        "🌼 Amber Light",
        "🩵 Ice Light",
        "🌱 Sage Light",
    ]

    st.markdown("**🌙 Dark Themes**")

    for theme in dark_themes:
        st.write(f"• {theme}")

    st.markdown("**☀️ Light Themes**")

    for theme in light_themes:
        st.write(f"• {theme}")

    st.info("15 themes are available: " "5 dark themes and 10 light themes.")

    st.divider()

    # ========================================================
    # Technology Stack
    # ========================================================

    st.subheader("🧰 Technology Stack")

    technologies = [
        "Python 3.11",
        "Streamlit",
        "OpenAI Whisper",
        "Ollama",
        "Qwen2.5 1.5B",
        "FFmpeg",
        "PyTest",
        "JSON storage",
        "Black 26.5.1",
        "pip 26.2.1",
    ]

    for technology in technologies:
        st.write(f"• {technology}")

    st.divider()

    # ========================================================
    # Testing
    # ========================================================

    st.subheader("🧪 Testing")

    st.success("267 tests passed successfully.")

    st.write(
        "The project maintains automated testing across "
        "the application workflow, caption generation, "
        "providers, themes, and supporting components."
    )

    st.divider()

    # ========================================================
    # Project Scope
    # ========================================================

    st.subheader("📦 Project Scope")

    st.write(
        "The application is focused specifically "
        "on AI-powered video caption generation."
    )

    st.write(
        "The workflow supports video transcription, "
        "language detection, multilingual caption "
        "generation, SRT/VTT creation, and permanently "
        "burning captions into videos."
    )

    st.write(
        "Transcript data can be saved as a generated "
        "transcript file for the completed workflow."
    )

    st.divider()

    # ========================================================
    # Application Settings
    # ========================================================

    st.subheader("⚙️ Application Settings")

    settings = [
        (
            "📝 Whisper Model",
            "Configure the Whisper transcription model "
            "used for video speech recognition.",
        ),
        (
            "🤖 AI Provider",
            "Select the AI provider used for caption " "translation.",
        ),
        (
            "🧠 AI Model",
            "Select the translation model associated "
            "with the configured AI provider.",
        ),
        (
            "🔑 API Configuration",
            "Cloud provider API keys are loaded from "
            "environment variables when required.",
        ),
        (
            "🌐 Default Caption Language",
            "Configure the default language used when " "generating captions.",
        ),
        (
            "📁 Application Directories",
            "Manage the locations used for uploaded videos, "
            "caption files, generated videos, and transcripts.",
        ),
    ]

    for title, description in settings:
        with st.expander(title):
            st.write(description)

    st.divider()

    # ========================================================
    # Supported AI Providers
    # ========================================================

    st.subheader("🤖 Supported AI Providers")

    providers = [
        "Ollama",
        "OpenAI",
        "Anthropic",
        "Gemini",
        "Mistral",
        "Groq",
        "Cohere",
        "DeepSeek",
    ]

    provider_columns = st.columns(4)

    for index, provider in enumerate(providers):
        with provider_columns[index % 4]:
            st.write(f"• {provider}")

    st.caption(
        "Provider and model selections are maintained "
        "for the current application session."
    )

    st.divider()

    # ========================================================
    # Supported Caption Languages
    # ========================================================

    st.subheader("🌐 Supported Caption Languages")

    language_columns = st.columns(3)

    for index, language in enumerate(CAPTION_LANGUAGES.keys()):
        with language_columns[index % 3]:
            st.write(f"• {language}")

    st.divider()

    # ========================================================
    # Project Folders
    # ========================================================

    st.subheader("📁 Project Folders")

    st.write(
        "The application uses dedicated folders for "
        "uploaded videos, captions, generated outputs, "
        "and transcripts."
    )

    project_folders = [
        (
            "📤 Uploads",
            UPLOAD_DIR,
            "Stores uploaded video files.",
        ),
        (
            "📄 Captions",
            CAPTION_DIR,
            "Stores generated SRT and VTT caption files.",
        ),
        (
            "🎬 Outputs",
            OUTPUT_DIR,
            "Stores final videos with burned captions.",
        ),
        (
            "📝 Transcripts",
            TRANSCRIPT_DIR,
            "Stores generated transcript files.",
        ),
    ]

    folder_columns = st.columns(2)

    for index, (
        folder_name,
        folder_path,
        description,
    ) in enumerate(project_folders):

        with folder_columns[index % 2]:

            st.markdown(f"### {folder_name}")

            st.code(
                str(folder_path),
                language="text",
            )

            st.caption(description)

    st.divider()

    # ========================================================
    # Current Release
    # ========================================================

    st.subheader("🚀 Current Release")

    st.success(f"AI Video Caption Generator v{APP_VERSION}")

    st.caption("Stable release • 267 tests passing • " "15 themes")


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
