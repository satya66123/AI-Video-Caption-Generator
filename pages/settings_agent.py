"""Application settings page."""

import streamlit as st

from config.caption_config import (
    DEFAULT_CAPTION_LANGUAGE,
    SUPPORTED_CAPTION_LANGUAGES,
)


def main() -> None:
    """Render the application settings."""

    st.title("⚙️ Settings")

    st.write(
        "Configure the models and default caption "
        "processing options."
    )

    st.divider()

    st.subheader("📝 Whisper")

    whisper_models = [
        "tiny",
        "base",
        "small",
        "medium",
        "large",
    ]

    whisper_model = st.selectbox(
        "Whisper model",
        whisper_models,
        index=whisper_models.index("base"),
        help=(
            "Larger models generally provide better "
            "transcription quality but require more resources."
        ),
    )

    st.session_state["whisper_model"] = whisper_model

    st.divider()

    st.subheader("✨ Translation")

    ollama_model = st.text_input(
        "Ollama translation model",
        value="translategemma:12b",
        help="Local Ollama model used for caption translation.",
    )

    st.session_state["ollama_model"] = ollama_model

    st.divider()

    st.subheader("💬 Default Caption Language")

    language_options = list(
        SUPPORTED_CAPTION_LANGUAGES.keys()
    )

    default_language = st.selectbox(
        "Default caption language",
        language_options,
        index=language_options.index(
            DEFAULT_CAPTION_LANGUAGE
        ),
        format_func=lambda code: (
            f"{SUPPORTED_CAPTION_LANGUAGES[code]} "
            f"({code})"
        ),
    )

    st.session_state[
        "default_caption_language"
    ] = default_language

    st.success("Settings saved for this session.")

    st.divider()

    st.subheader("📁 Output Directories")

    st.code(
        "uploads/   → Uploaded videos\n"
        "captions/  → SRT / VTT files\n"
        "outputs/   → Captioned videos",
        language="text",
    )


if __name__ == "__main__":
    main()