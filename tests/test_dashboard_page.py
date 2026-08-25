"""Tests for the Dashboard page."""

from unittest.mock import MagicMock, patch

from pages.dashboard_agent import main


def create_dashboard_mock() -> MagicMock:
    """Create a mocked DashboardAgent."""
    dashboard = MagicMock()

    dashboard.get_statistics.return_value = {
        "videos": 3,
        "caption_files": 6,
        "captioned_videos": 2,
    }

    dashboard.get_recent_files.return_value = [
        {
            "name": "gm_en_captioned.mp4",
            "path": "outputs/gm_en_captioned.mp4",
            "type": ".mp4",
        },
        {
            "name": "gm_en.srt",
            "path": "captions/gm_en.srt",
            "type": ".srt",
        },
    ]

    return dashboard


def create_columns() -> list[MagicMock]:
    """Create three mocked Streamlit columns."""
    return [
        MagicMock(),
        MagicMock(),
        MagicMock(),
    ]


def setup_streamlit_columns(
    mock_st: MagicMock,
    columns: list[MagicMock],
) -> None:
    """Configure mocked Streamlit columns."""
    mock_st.columns.return_value = columns

    for column in columns:
        column.__enter__.return_value = column
        column.__exit__.return_value = None


def test_dashboard_renders_title() -> None:
    """Render the dashboard title."""
    dashboard = create_dashboard_mock()
    columns = create_columns()

    with patch(
        "pages.dashboard_agent.DashboardAgent",
        return_value=dashboard,
    ):
        with patch("pages.dashboard_agent.st") as mock_st:

            setup_streamlit_columns(
                mock_st,
                columns,
            )

            main()

            mock_st.title.assert_called_once_with("📊 Dashboard")


def test_dashboard_renders_description() -> None:
    """Render the dashboard description."""
    dashboard = create_dashboard_mock()
    columns = create_columns()

    with patch(
        "pages.dashboard_agent.DashboardAgent",
        return_value=dashboard,
    ):
        with patch("pages.dashboard_agent.st") as mock_st:

            setup_streamlit_columns(
                mock_st,
                columns,
            )

            main()

            mock_st.write.assert_any_call(
                "Overview of your video caption generation activity."
            )


def test_dashboard_renders_statistics() -> None:
    """Render dashboard statistics."""
    dashboard = create_dashboard_mock()
    columns = create_columns()

    with patch(
        "pages.dashboard_agent.DashboardAgent",
        return_value=dashboard,
    ):
        with patch("pages.dashboard_agent.st") as mock_st:

            setup_streamlit_columns(
                mock_st,
                columns,
            )

            main()

            dashboard.get_statistics.assert_called_once()

            assert mock_st.metric.call_count == 3

            mock_st.metric.assert_any_call(
                "🎬 Videos",
                3,
            )

            mock_st.metric.assert_any_call(
                "📄 Caption Files",
                6,
            )

            mock_st.metric.assert_any_call(
                "🎥 Captioned Videos",
                2,
            )


def test_dashboard_requests_recent_files() -> None:
    """Request recent files with the expected limit."""
    dashboard = create_dashboard_mock()
    columns = create_columns()

    with patch(
        "pages.dashboard_agent.DashboardAgent",
        return_value=dashboard,
    ):
        with patch("pages.dashboard_agent.st") as mock_st:

            setup_streamlit_columns(
                mock_st,
                columns,
            )

            main()

            dashboard.get_recent_files.assert_called_once_with(
                limit=20,
            )


def test_dashboard_renders_recent_files() -> None:
    """Render recent files."""
    dashboard = create_dashboard_mock()
    columns = create_columns()

    with patch(
        "pages.dashboard_agent.DashboardAgent",
        return_value=dashboard,
    ):
        with patch("pages.dashboard_agent.st") as mock_st:

            setup_streamlit_columns(
                mock_st,
                columns,
            )

            main()

            mock_st.write.assert_any_call("**gm_en_captioned.mp4**")

            mock_st.write.assert_any_call("**gm_en.srt**")

            mock_st.caption.assert_any_call(
                "Type: .mp4  | Path: " "outputs/gm_en_captioned.mp4"
            )

            mock_st.caption.assert_any_call("Type: .srt  | Path: " "captions/gm_en.srt")


def test_dashboard_filters_gitkeep() -> None:
    """Do not render .gitkeep files."""
    dashboard = MagicMock()

    dashboard.get_statistics.return_value = {
        "videos": 1,
        "caption_files": 1,
        "captioned_videos": 0,
    }

    dashboard.get_recent_files.return_value = [
        {
            "name": ".gitkeep",
            "path": "uploads/.gitkeep",
            "type": "",
        },
        {
            "name": "gm.mp4",
            "path": "uploads/gm.mp4",
            "type": ".mp4",
        },
    ]

    columns = create_columns()

    with patch(
        "pages.dashboard_agent.DashboardAgent",
        return_value=dashboard,
    ):
        with patch("pages.dashboard_agent.st") as mock_st:

            setup_streamlit_columns(
                mock_st,
                columns,
            )

            main()

            rendered_write_calls = [
                call.args[0] for call in mock_st.write.call_args_list if call.args
            ]

            assert not any(".gitkeep" in value for value in rendered_write_calls)

            mock_st.write.assert_any_call("**gm.mp4**")


def test_dashboard_empty_recent_files() -> None:
    """Show an informational message when no files exist."""
    dashboard = MagicMock()

    dashboard.get_statistics.return_value = {
        "videos": 0,
        "caption_files": 0,
        "captioned_videos": 0,
    }

    dashboard.get_recent_files.return_value = []

    columns = create_columns()

    with patch(
        "pages.dashboard_agent.DashboardAgent",
        return_value=dashboard,
    ):
        with patch("pages.dashboard_agent.st") as mock_st:

            setup_streamlit_columns(
                mock_st,
                columns,
            )

            main()

            mock_st.info.assert_called_once_with("No files available yet.")


def test_dashboard_only_gitkeep_files() -> None:
    """Show no-files message when only .gitkeep exists."""
    dashboard = MagicMock()

    dashboard.get_statistics.return_value = {
        "videos": 0,
        "caption_files": 0,
        "captioned_videos": 0,
    }

    dashboard.get_recent_files.return_value = [
        {
            "name": ".gitkeep",
            "path": "uploads/.gitkeep",
            "type": "",
        },
    ]

    columns = create_columns()

    with patch(
        "pages.dashboard_agent.DashboardAgent",
        return_value=dashboard,
    ):
        with patch("pages.dashboard_agent.st") as mock_st:

            setup_streamlit_columns(
                mock_st,
                columns,
            )

            main()

            mock_st.info.assert_called_once_with("No files available yet.")


def test_dashboard_uses_dashboard_agent() -> None:
    """Create and use DashboardAgent."""
    dashboard = create_dashboard_mock()
    columns = create_columns()

    with patch(
        "pages.dashboard_agent.DashboardAgent",
        return_value=dashboard,
    ) as mock_agent:

        with patch("pages.dashboard_agent.st") as mock_st:

            setup_streamlit_columns(
                mock_st,
                columns,
            )

            main()

            mock_agent.assert_called_once_with()
