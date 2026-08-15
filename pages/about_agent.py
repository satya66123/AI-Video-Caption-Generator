"""About page."""

import streamlit as st


def main() -> None:
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
        "TranslateGemma 12B\n"
        "  ↓\n"
        "SRT / VTT\n"
        "  ↓\n"
        "FFmpeg\n"
        "  ↓\n"
        "Captioned Video",
        language="text",
    )

    st.divider()

    st.subheader("🧰 Technology Stack")

    technologies = [
        "Python 3.11",
        "Streamlit",
        "OpenAI Whisper",
        "Ollama",
        "TranslateGemma 12B",
        "FFmpeg",
        "PyTest",
        "JSON storage",
    ]

    for technology in technologies:
        st.write(f"• {technology}")

    st.divider()

    st.subheader("📦 Project Scope")

    st.write(
        "The application is focused specifically on "
        "video caption generation."
    )

    st.write(
        "Transcript data is used internally during "
        "processing and is not maintained as a separate "
        "transcript-history feature."
    )

    st.divider()

    st.caption(
        "AI Video Caption Generator"
    )


if __name__ == "__main__":
    main()