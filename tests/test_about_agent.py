"""Tests for the About page."""

from unittest.mock import MagicMock, patch

from pages.about_agent import main


def test_about_page_renders_title() -> None:
    """Render the About page title."""
    with patch(
        "pages.about_agent.st"
    ) as mock_st:
        main()

        mock_st.title.assert_called_once_with(
            "ℹ️ About"
        )


def test_about_page_renders_description() -> None:
    """Render the application description."""
    with patch(
        "pages.about_agent.st"
    ) as mock_st:
        main()

        mock_st.write.assert_any_call(
            "An AI-powered application for generating "
            "multilingual captions from videos."
        )


def test_about_page_renders_core_workflow() -> None:
    """Render the core caption workflow."""
    with patch(
        "pages.about_agent.st"
    ) as mock_st:
        main()

        workflow = (
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
            "Captioned Video"
        )

        mock_st.code.assert_called_once_with(
            workflow,
            language="text",
        )


def test_about_page_renders_technology_stack() -> None:
    """Render all technologies in the technology stack."""
    with patch(
        "pages.about_agent.st"
    ) as mock_st:
        main()

        expected_technologies = [
            "Python 3.11",
            "Streamlit",
            "OpenAI Whisper",
            "Ollama",
            "TranslateGemma 12B",
            "FFmpeg",
            "PyTest",
            "JSON storage",
        ]

        for technology in expected_technologies:
            mock_st.write.assert_any_call(
                f"• {technology}"
            )


def test_about_page_renders_project_scope() -> None:
    """Render the project scope information."""
    with patch(
        "pages.about_agent.st"
    ) as mock_st:
        main()

        mock_st.write.assert_any_call(
            "The application is focused specifically on "
            "video caption generation."
        )

        mock_st.write.assert_any_call(
            "Transcript data is used internally during "
            "processing and is not maintained as a separate "
            "transcript-history feature."
        )


def test_about_page_renders_dividers() -> None:
    """Render section dividers."""
    with patch(
        "pages.about_agent.st"
    ) as mock_st:
        main()

        assert mock_st.divider.call_count == 4


def test_about_page_renders_footer() -> None:
    """Render the About page footer."""
    with patch(
        "pages.about_agent.st"
    ) as mock_st:
        main()

        mock_st.caption.assert_called_once_with(
            "AI Video Caption Generator"
        )


def test_about_page_does_not_create_external_dependencies() -> None:
    """The About page should only render static content."""
    with patch(
        "pages.about_agent.st"
    ) as mock_st:
        main()

        # The page should render without requiring
        # agents, services, providers, databases,
        # Ollama, Whisper, or FFmpeg.
        assert mock_st.title.called
        assert mock_st.subheader.called
        assert mock_st.write.called
        assert mock_st.code.called
        assert mock_st.caption.called