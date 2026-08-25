"""Application settings agent/page."""

import os

import streamlit as st

from config.caption_config import (
    DEFAULT_CAPTION_LANGUAGE,
    SUPPORTED_CAPTION_LANGUAGES,
)

TRANSLATION_PROVIDERS = {
    "Ollama": {
        "key": "ollama",
        "model": "qwen2.5:1.5b",
        "environment_variable": None,
    },
    "OpenAI": {
        "key": "openai",
        "model": "gpt-5-mini",
        "environment_variable": "OPENAI_API_KEY",
    },
    "Anthropic": {
        "key": "anthropic",
        "model": "claude-sonnet-4-5",
        "environment_variable": "ANTHROPIC_API_KEY",
    },
    "Gemini": {
        "key": "gemini",
        "model": "gemini-3.6-flash",
        "environment_variable": "GEMINI_API_KEY",
    },
    "Mistral": {
        "key": "mistral",
        "model": "mistral-medium-latest",
        "environment_variable": "MISTRAL_API_KEY",
    },
    "Groq": {
        "key": "groq",
        "model": "llama-3.1-8b-instant",
        "environment_variable": "GROQ_API_KEY",
    },
    "Cohere": {
        "key": "cohere",
        "model": "command-a-03-2025",
        "environment_variable": "COHERE_API_KEY",
    },
    "DeepSeek": {
        "key": "deepseek",
        "model": "deepseek-v4-flash",
        "environment_variable": "DEEPSEEK_API_KEY",
    },
}


def _get_api_key_status(provider_key: str) -> str:
    """Return the configuration status for a provider."""

    if provider_key == "ollama":
        return "🟢 Local Ollama"

    provider = next(
        (
            config
            for config in TRANSLATION_PROVIDERS.values()
            if config["key"] == provider_key
        ),
        None,
    )

    if provider is None:
        return "🔴 Unknown provider"

    environment_variable = provider["environment_variable"]

    if environment_variable and os.getenv(environment_variable):
        return "🟢 API key configured"

    return "🔴 API key missing"


def main() -> None:
    """Render the application settings page."""

    st.title("⚙️ Settings")

    st.write("Configure caption-generation preferences.")

    st.divider()

    # ---------------------------------------------------------
    # Whisper
    # ---------------------------------------------------------

    st.subheader("📝 Whisper Model")

    whisper_models = [
        "tiny",
        "base",
        "small",
        "medium",
        "large",
    ]

    current_whisper_model = st.session_state.get(
        "whisper_model",
        "base",
    )

    whisper_index = (
        whisper_models.index(current_whisper_model)
        if current_whisper_model in whisper_models
        else whisper_models.index("base")
    )

    whisper_model = st.selectbox(
        "Whisper model",
        whisper_models,
        index=whisper_index,
        help=(
            "Larger models generally provide better "
            "transcription quality but require more resources."
        ),
    )

    st.session_state["whisper_model"] = whisper_model

    st.divider()

    # ---------------------------------------------------------
    # Translation Provider
    # ---------------------------------------------------------

    st.subheader("🤖 Translation Provider")

    provider_names = list(TRANSLATION_PROVIDERS.keys())

    current_provider = st.session_state.get(
        "translation_provider",
        "ollama",
    )

    provider_keys = [config["key"] for config in TRANSLATION_PROVIDERS.values()]

    if current_provider in provider_keys:
        current_provider_index = provider_keys.index(current_provider)
    else:
        current_provider_index = 0

    translation_provider = st.selectbox(
        "AI provider",
        provider_names,
        index=current_provider_index,
        help=("Select the AI provider used for " "caption translation."),
    )

    provider_config = TRANSLATION_PROVIDERS[translation_provider]

    provider_key = provider_config["key"]
    translation_model = provider_config["model"]

    st.session_state["translation_provider"] = provider_key

    st.session_state["translation_model"] = translation_model

    # ---------------------------------------------------------
    # Selected Provider
    # ---------------------------------------------------------

    st.markdown(f"### {translation_provider}")

    st.text_input(
        "Default model",
        value=translation_model,
        disabled=True,
    )

    st.caption(
        f"Provider: **{translation_provider}**  |  " f"Model: **{translation_model}**"
    )

    status = _get_api_key_status(provider_key)

    st.write(f"Status: {status}")

    if provider_key == "ollama":
        st.info("Ollama runs locally and does not require " "a cloud API key.")
    else:
        st.info("The API key is read from the environment " "and is never displayed.")

    # ---------------------------------------------------------
    # Available Providers
    # ---------------------------------------------------------

    st.divider()

    st.subheader("🌐 Available AI Providers")

    provider_items = list(TRANSLATION_PROVIDERS.items())

    for start in range(0, len(provider_items), 4):
        row_items = provider_items[start : start + 4]

        provider_columns = st.columns(4)

        for column, (
            provider_name,
            config,
        ) in zip(
            provider_columns,
            row_items,
        ):
            with column:
                st.markdown(f"### {provider_name}")

                st.caption(f"`{config['model']}`")

                provider_status = _get_api_key_status(config["key"])

                st.write(provider_status)

    st.divider()

    # ---------------------------------------------------------
    # Caption Language
    # ---------------------------------------------------------

    st.subheader("💬 Default Caption Language")

    language_options = list(SUPPORTED_CAPTION_LANGUAGES.keys())

    current_language = st.session_state.get(
        "default_caption_language",
        DEFAULT_CAPTION_LANGUAGE,
    )

    language_index = (
        language_options.index(current_language)
        if current_language in language_options
        else language_options.index(DEFAULT_CAPTION_LANGUAGE)
    )

    default_language = st.selectbox(
        "Default caption language",
        language_options,
        index=language_index,
        format_func=lambda code: (f"{SUPPORTED_CAPTION_LANGUAGES[code]} " f"({code})"),
    )

    st.session_state["translation_provider"] = provider_key
    st.session_state["translation_model"] = translation_model

    st.session_state["default_caption_language"] = default_language

    st.success("Settings saved for this session.")

    st.divider()

    # ---------------------------------------------------------
    # Output Directories
    # ---------------------------------------------------------

    st.subheader("📁 Output Directories")

    st.code(
        "uploads/   → Uploaded videos\n"
        "captions/  → SRT / VTT files\n"
        "outputs/   → Captioned videos",
        language="text",
    )


if __name__ == "__main__":
    main()
