"""Help page."""

import streamlit as st


def main() -> None:
    """Render the help page."""

    st.title("❓ Help")

    st.write(
        "Learn how to use the AI Video Caption Generator."
    )

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

    st.write(
        "MP4, MOV, AVI, MKV, and WebM."
    )

    st.divider()

    st.subheader("📄 Caption Formats")

    st.write(
        "The application generates both SRT and VTT."
    )

    st.divider()

    st.subheader("🤖 AI Processing")

    st.write(
        "Whisper is used for internal timestamped "
        "transcription."
    )

    st.write(
        "TranslateGemma 12B running locally through "
        "Ollama is used for caption translation."
    )

    st.divider()

    st.subheader("🔥 FFmpeg")

    st.write(
        "FFmpeg permanently burns the selected captions "
        "into the final video."
    )

    st.divider()

    st.subheader("🛠️ Troubleshooting")

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
        "TranslateGemma model missing"
    ):
        st.code(
            "ollama pull translategemma:12b",
            language="powershell",
        )

    with st.expander(
        "FFmpeg not found"
    ):
        st.code(
            "ffmpeg -version",
            language="powershell",
        )


if __name__ == "__main__":
    main()