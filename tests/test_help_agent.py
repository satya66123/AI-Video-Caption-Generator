"""Tests for the Help page."""

from unittest.mock import MagicMock, patch

from pages.help_agent import main


def create_streamlit_mock() -> MagicMock:
    """Create a mocked Streamlit module."""
    mock_st = MagicMock()

    ollama_expander = MagicMock()
    translate_expander = MagicMock()
    ffmpeg_expander = MagicMock()

    mock_st.expander.side_effect = [
        ollama_expander,
        translate_expander,
        ffmpeg_expander,
    ]

    return mock_st


def test_help_renders_title() -> None:
    """Render the Help page title."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.title.assert_called_once_with(
            "❓ Help"
        )


def test_help_renders_description() -> None:
    """Render the Help page description."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.write.assert_any_call(
            "Learn how to use the AI Video Caption Generator."
        )


def test_help_renders_how_to_use_section() -> None:
    """Render the How to Use section."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "🚀 How to Use"
        )


def test_help_renders_all_workflow_steps() -> None:
    """Render all eight workflow steps."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        expected_steps = [
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
            expected_steps,
            start=1,
        ):
            mock_st.write.assert_any_call(
                f"**{index}.** {step}"
            )


def test_help_renders_video_formats() -> None:
    """Render supported video formats."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "🎬 Supported Video Formats"
        )

        mock_st.write.assert_any_call(
            "MP4, MOV, AVI, MKV, and WebM."
        )


def test_help_renders_caption_formats() -> None:
    """Render supported caption formats."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "📄 Caption Formats"
        )

        mock_st.write.assert_any_call(
            "The application generates both SRT and VTT."
        )


def test_help_renders_ai_processing() -> None:
    """Render AI processing information."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "🤖 AI Processing"
        )

        mock_st.write.assert_any_call(
            "Whisper is used for internal timestamped "
            "transcription."
        )

        mock_st.write.assert_any_call(
            "TranslateGemma 12B running locally through "
            "Ollama is used for caption translation."
        )


def test_help_renders_ffmpeg_information() -> None:
    """Render FFmpeg information."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "🔥 FFmpeg"
        )

        mock_st.write.assert_any_call(
            "FFmpeg permanently burns the selected captions "
            "into the final video."
        )


def test_help_renders_troubleshooting_section() -> None:
    """Render the troubleshooting section."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "🛠️ Troubleshooting"
        )


def test_help_renders_ollama_troubleshooting() -> None:
    """Render Ollama troubleshooting instructions."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.expander.assert_any_call(
            "Ollama connection error"
        )


def test_help_renders_translategemma_troubleshooting() -> None:
    """Render TranslateGemma troubleshooting instructions."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.expander.assert_any_call(
            "TranslateGemma model missing"
        )


def test_help_renders_ffmpeg_troubleshooting() -> None:
    """Render FFmpeg troubleshooting instructions."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.expander.assert_any_call(
            "FFmpeg not found"
        )


def test_help_renders_ollama_command() -> None:
    """Render Ollama troubleshooting commands."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        assert mock_st.code.call_count == 3

        mock_st.code.assert_any_call(
            "ollama --version\n"
            "ollama list\n"
            "ollama serve",
            language="powershell",
        )


def test_help_renders_translategemma_command() -> None:
    """Render TranslateGemma installation command."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.code.assert_any_call(
            "ollama pull translategemma:12b",
            language="powershell",
        )


def test_help_renders_ffmpeg_command() -> None:
    """Render FFmpeg troubleshooting command."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        mock_st.code.assert_any_call(
            "ffmpeg -version",
            language="powershell",
        )


def test_help_renders_three_expanders() -> None:
    """Render all three troubleshooting expanders."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        assert mock_st.expander.call_count == 3


def test_help_renders_dividers() -> None:
    """Render all expected section dividers."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.help_agent.st",
        mock_st,
    ):
        main()

        assert mock_st.divider.call_count == 6