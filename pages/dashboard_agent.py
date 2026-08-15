"""Dashboard page."""

import streamlit as st

from agents.dashboard_agent import DashboardAgent


def main() -> None:
    """Render the dashboard."""
    st.title("📊 Dashboard")

    st.write(
        "Overview of your video caption generation activity."
    )

    st.divider()

    dashboard = DashboardAgent()

    statistics = dashboard.get_statistics()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎬 Videos",
            statistics["videos"],
        )

    with col2:
        st.metric(
            "📄 Caption Files",
            statistics["caption_files"],
        )

    with col3:
        st.metric(
            "🎥 Captioned Videos",
            statistics["captioned_videos"],
        )

    st.divider()

    st.subheader("🕐 Recent Files")

    recent_files = dashboard.get_recent_files(
        limit=20,
    )

    # Do not show Git placeholder files.
    recent_files = [
        file_info
        for file_info in recent_files
        if file_info["name"] != ".gitkeep"
    ]

    if not recent_files:
        st.info(
            "No files available yet."
        )
        return

    for file_info in recent_files:

        st.write(
            f"**{file_info['name']}**"
        )

        st.caption(
            f"Type: {file_info['type']}  "
            f"| Path: {file_info['path']}"
        )


if __name__ == "__main__":
    main()