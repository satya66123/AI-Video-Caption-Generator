"""Tests for the application settings page."""

from unittest.mock import MagicMock, patch

from pages.settings_agent import main


def create_streamlit_mock() -> MagicMock:
    """Create a mocked Streamlit module."""
    mock_st = MagicMock()

    mock_st.session_state = {}

    mock_st.selectbox.side_effect = [
        "base",
        "en",
    ]

    mock_st.text_input.return_value = (
        "translategemma:12b"
    )

    return mock_st


def test_settings_renders_title() -> None:
    """Render the settings title."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.title.assert_called_once_with(
            "⚙️ Settings"
        )


def test_settings_renders_description() -> None:
    """Render the settings description."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.write.assert_any_call(
            "Configure the models and default caption "
            "processing options."
        )


def test_settings_renders_whisper_section() -> None:
    """Render the Whisper settings section."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "📝 Whisper"
        )


def test_settings_whisper_model() -> None:
    """Select and store the Whisper model."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        selectbox_calls = (
            mock_st.selectbox.call_args_list
        )

        assert selectbox_calls[0].args[0] == (
            "Whisper model"
        )

        assert selectbox_calls[0].args[1] == [
            "tiny",
            "base",
            "small",
            "medium",
            "large",
        ]

        assert (
            mock_st.session_state[
                "whisper_model"
            ]
            == "base"
        )


def test_settings_renders_translation_section() -> None:
    """Render the translation settings section."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "✨ Translation"
        )


def test_settings_ollama_model() -> None:
    """Select and store the Ollama model."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.text_input.assert_called_once_with(
            "Ollama translation model",
            value="translategemma:12b",
            help=(
                "Local Ollama model used for "
                "caption translation."
            ),
        )

        assert (
            mock_st.session_state[
                "ollama_model"
            ]
            == "translategemma:12b"
        )


def test_settings_renders_language_section() -> None:
    """Render the default caption language section."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "💬 Default Caption Language"
        )


def test_settings_default_language() -> None:
    """Select and store the default caption language."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        selectbox_calls = (
            mock_st.selectbox.call_args_list
        )

        language_call = selectbox_calls[1]

        assert language_call.args[0] == (
            "Default caption language"
        )

        assert language_call.args[1] == [
            "en",
            "te",
            "hi",
            "ta",
            "kn",
            "ml",
            "bn",
            "mr",
            "gu",
            "pa",
        ]

        assert (
            mock_st.session_state[
                "default_caption_language"
            ]
            == "en"
        )


def test_settings_language_format_function() -> None:
    """Verify the language selectbox formatter."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        language_call = (
            mock_st.selectbox.call_args_list[1]
        )

        format_func = language_call.kwargs[
            "format_func"
        ]

        assert format_func("en") == (
            "English (en)"
        )

        assert format_func("te") == (
            "Telugu (te)"
        )

        assert format_func("hi") == (
            "Hindi (hi)"
        )


def test_settings_saves_session_values() -> None:
    """Store all settings in Streamlit session state."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        assert mock_st.session_state == {
            "whisper_model": "base",
            "ollama_model": "translategemma:12b",
            "default_caption_language": "en",
        }


def test_settings_success_message() -> None:
    """Show the settings saved message."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.success.assert_called_once_with(
            "Settings saved for this session."
        )


def test_settings_output_directories() -> None:
    """Render the output directory information."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "📁 Output Directories"
        )

        mock_st.code.assert_called_once_with(
            "uploads/   → Uploaded videos\n"
            "captions/  → SRT / VTT files\n"
            "outputs/   → Captioned videos",
            language="text",
        )


def test_settings_renders_dividers() -> None:
    """Render all expected section dividers."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        assert mock_st.divider.call_count == 4