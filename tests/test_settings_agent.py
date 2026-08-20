"""Tests for the application settings agent/page."""

import os
from unittest.mock import MagicMock, patch

from pages.settings_agent import (
    TRANSLATION_PROVIDERS,
    main, _get_api_key_status,
)


def create_streamlit_mock() -> MagicMock:
    """Create a mocked Streamlit module."""
    mock_st = MagicMock()

    mock_st.session_state = {}

    mock_st.selectbox.side_effect = [
        "base",
        "Ollama",
        "en",
    ]

    mock_st.text_input.return_value = (
        "qwen2.5:1.5b"
    )

    mock_st.columns.return_value = [
        MagicMock(),
        MagicMock(),
        MagicMock(),
        MagicMock(),
    ]

    return mock_st


def test_translation_providers_configuration() -> None:
    """Verify all supported translation providers."""
    assert list(
        TRANSLATION_PROVIDERS.keys()
    ) == [
        "Ollama",
        "OpenAI",
        "Anthropic",
        "Gemini",
        "Mistral",
        "Groq",
        "Cohere",
        "DeepSeek",
    ]

    assert TRANSLATION_PROVIDERS["Ollama"]["key"] == "ollama"
    assert TRANSLATION_PROVIDERS["Ollama"]["model"] == "qwen2.5:1.5b"

    assert TRANSLATION_PROVIDERS["OpenAI"]["key"] == "openai"
    assert TRANSLATION_PROVIDERS["OpenAI"]["model"] == "gpt-5-mini"

    assert TRANSLATION_PROVIDERS["Anthropic"]["key"] == "anthropic"
    assert (
        TRANSLATION_PROVIDERS["Anthropic"]["model"]
        == "claude-sonnet-4-5"
    )

    assert TRANSLATION_PROVIDERS["Gemini"]["key"] == "gemini"
    assert (
        TRANSLATION_PROVIDERS["Gemini"]["model"]
        == "gemini-3.6-flash"
    )

    assert TRANSLATION_PROVIDERS["Mistral"]["key"] == "mistral"
    assert (
        TRANSLATION_PROVIDERS["Mistral"]["model"]
        == "mistral-medium-latest"
    )

    assert TRANSLATION_PROVIDERS["Groq"]["key"] == "groq"
    assert (
        TRANSLATION_PROVIDERS["Groq"]["model"]
        == "llama-3.1-8b-instant"
    )

    assert TRANSLATION_PROVIDERS["Cohere"]["key"] == "cohere"
    assert (
        TRANSLATION_PROVIDERS["Cohere"]["model"]
        == "command-a-03-2025"
    )

    assert TRANSLATION_PROVIDERS["DeepSeek"]["key"] == "deepseek"
    assert (
        TRANSLATION_PROVIDERS["DeepSeek"]["model"]
        == "deepseek-v4-flash"
    )


@patch.dict(
    os.environ,
    {"MISTRAL_API_KEY": "test-mistral-key"},
)
def test_get_api_key_status_mistral_configured() -> None:
    """Verify configured Mistral API key."""
    assert (
        _get_api_key_status("mistral")
        == "🟢 API key configured"
    )


@patch.dict(
    os.environ,
    {},
    clear=True,
)
def test_get_api_key_status_mistral_missing() -> None:
    """Verify missing Mistral API key."""
    assert (
        _get_api_key_status("mistral")
        == "🔴 API key missing"
    )


@patch.dict(
    os.environ,
    {"GROQ_API_KEY": "test-groq-key"},
)
def test_get_api_key_status_groq_configured() -> None:
    """Verify configured Groq API key."""
    assert (
        _get_api_key_status("groq")
        == "🟢 API key configured"
    )


@patch.dict(
    os.environ,
    {},
    clear=True,
)
def test_get_api_key_status_groq_missing() -> None:
    """Verify missing Groq API key."""
    assert (
        _get_api_key_status("groq")
        == "🔴 API key missing"
    )


@patch.dict(
    os.environ,
    {"COHERE_API_KEY": "test-cohere-key"},
)
def test_get_api_key_status_cohere_configured() -> None:
    """Verify configured Cohere API key."""
    assert (
        _get_api_key_status("cohere")
        == "🟢 API key configured"
    )


@patch.dict(
    os.environ,
    {},
    clear=True,
)
def test_get_api_key_status_cohere_missing() -> None:
    """Verify missing Cohere API key."""
    assert (
        _get_api_key_status("cohere")
        == "🔴 API key missing"
    )


@patch.dict(
    os.environ,
    {"DEEPSEEK_API_KEY": "test-deepseek-key"},
)
def test_get_api_key_status_deepseek_configured() -> None:
    """Verify configured DeepSeek API key."""
    assert (
        _get_api_key_status("deepseek")
        == "🟢 API key configured"
    )


@patch.dict(
    os.environ,
    {},
    clear=True,
)
def test_get_api_key_status_deepseek_missing() -> None:
    """Verify missing DeepSeek API key."""
    assert (
        _get_api_key_status("deepseek")
        == "🔴 API key missing"
    )


def test_get_api_key_status_ollama() -> None:
    """Verify Ollama status."""
    assert (
        _get_api_key_status("ollama")
        == "🟢 Local Ollama"
    )


def test_get_api_key_status_unknown_provider() -> None:
    """Verify unknown provider status."""
    assert (
        _get_api_key_status("unknown")
        == "🔴 Unknown provider"
    )


@patch.dict(
    os.environ,
    {"OPENAI_API_KEY": "test-openai-key"},
)
def test_get_api_key_status_openai_configured() -> None:
    """Verify configured OpenAI API key."""
    assert (
        _get_api_key_status("openai")
        == "🟢 API key configured"
    )


@patch.dict(
    os.environ,
    {},
    clear=True,
)
def test_get_api_key_status_openai_missing() -> None:
    """Verify missing OpenAI API key."""
    assert (
        _get_api_key_status("openai")
        == "🔴 API key missing"
    )


@patch.dict(
    os.environ,
    {"ANTHROPIC_API_KEY": "test-anthropic-key"},
)
def test_get_api_key_status_anthropic_configured() -> None:
    """Verify configured Anthropic API key."""
    assert (
        _get_api_key_status("anthropic")
        == "🟢 API key configured"
    )


@patch.dict(
    os.environ,
    {},
    clear=True,
)
def test_get_api_key_status_anthropic_missing() -> None:
    """Verify missing Anthropic API key."""
    assert (
        _get_api_key_status("anthropic")
        == "🔴 API key missing"
    )


@patch.dict(
    os.environ,
    {"GEMINI_API_KEY": "test-gemini-key"},
)
def test_get_api_key_status_gemini_configured() -> None:
    """Verify configured Gemini API key."""
    assert (
        _get_api_key_status("gemini")
        == "🟢 API key configured"
    )


@patch.dict(
    os.environ,
    {},
    clear=True,
)
def test_get_api_key_status_gemini_missing() -> None:
    """Verify missing Gemini API key."""
    assert (
        _get_api_key_status("gemini")
        == "🔴 API key missing"
    )


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
            "Configure caption-generation preferences."
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
            "📝 Whisper Model"
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


def test_settings_renders_translation_provider() -> None:
    """Render the translation provider section."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "🤖 Translation Provider"
        )


def test_settings_translation_provider() -> None:
    """Select and store the translation provider."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        selectbox_calls = (
            mock_st.selectbox.call_args_list
        )

        provider_call = selectbox_calls[1]

        assert provider_call.args[0] == (
            "AI provider"
        )

        assert provider_call.args[1] == [
            "Ollama",
            "OpenAI",
            "Anthropic",
            "Gemini",
            "Mistral",
            "Groq",
            "Cohere",
            "DeepSeek",
        ]

        assert (
            mock_st.session_state[
                "translation_provider"
            ]
            == "ollama"
        )


def test_settings_translation_model() -> None:
    """Store the selected provider model."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        assert (
            mock_st.session_state[
                "translation_model"
            ]
            == "qwen2.5:1.5b"
        )

        mock_st.text_input.assert_called_once_with(
            "Default model",
            value="qwen2.5:1.5b",
            disabled=True,
        )


def test_settings_renders_selected_provider() -> None:
    """Render selected provider information."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.markdown.assert_any_call(
            "### Ollama"
        )

        mock_st.caption.assert_any_call(
            "Provider: **Ollama**  |  "
            "Model: **qwen2.5:1.5b**"
        )


def test_settings_renders_ollama_info() -> None:
    """Render Ollama information."""
    mock_st = create_streamlit_mock()

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.info.assert_any_call(
            "Ollama runs locally and does not require "
            "a cloud API key."
        )


def test_settings_renders_available_providers() -> None:
    """Render all available providers."""
    mock_st = create_streamlit_mock()

    columns = [
        MagicMock(),
        MagicMock(),
        MagicMock(),
        MagicMock(),
    ]

    mock_st.columns.return_value = columns

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        mock_st.subheader.assert_any_call(
            "🌐 Available AI Providers"
        )

        assert mock_st.columns.call_count == 2

        assert (
                mock_st.columns.call_args_list
                == [
                    ((4,), {}),
                    ((4,), {}),
                ]
        )


def test_settings_renders_all_provider_names() -> None:
    """Render all provider names."""
    mock_st = create_streamlit_mock()

    columns = [
        MagicMock(),
        MagicMock(),
        MagicMock(),
        MagicMock(),
    ]

    mock_st.columns.return_value = columns

    with patch(
        "pages.settings_agent.st",
        mock_st,
    ):
        main()

        rendered_markdown = [
            call.args[0]
            for call in mock_st.markdown.call_args_list
        ]

        assert "### Ollama" in rendered_markdown
        assert "### OpenAI" in rendered_markdown
        assert "### Anthropic" in rendered_markdown
        assert "### Gemini" in rendered_markdown


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

        language_call = selectbox_calls[2]

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
            mock_st.selectbox.call_args_list[2]
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
            "translation_provider": "ollama",
            "translation_model": "qwen2.5:1.5b",
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