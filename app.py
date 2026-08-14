import streamlit as st


st.set_page_config(
    page_title="AI Video Caption Generator",
    page_icon="🎬",
    layout="wide",
)


def main() -> None:
    """Run the Caption Generator application."""
    st.title("🎬 AI Video Caption Generator")

    st.info(
        "Caption Generator foundation initialized. "
        "Caption generation features will be added in later phases."
    )


if __name__ == "__main__":
    main()