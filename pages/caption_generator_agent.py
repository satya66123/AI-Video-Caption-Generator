"""Caption Generator Streamlit page."""

import streamlit as st

from config.caption_config import SUPPORTED_CAPTION_LANGUAGES


def render() -> None:
    """Render the Caption Generator page."""
    st.title("🎬 Caption Generator")

    st.subheader("Language Selection")

    detected_language = st.text_input(
        "Detected Video Language",
        value="",
        placeholder="Detected language will appear here",
        disabled=True,
    )

    st.selectbox(
        "Caption Language",
        options=list(SUPPORTED_CAPTION_LANGUAGES.keys()),
        format_func=lambda code: SUPPORTED_CAPTION_LANGUAGES[code],
        index=0,
    )

    if detected_language:
        st.success(f"Detected language: {detected_language}")
    else:
        st.info("Upload a video to detect its spoken language.")


if __name__ == "__main__":
    render()