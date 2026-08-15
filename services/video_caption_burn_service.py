"""Service for burning captions into videos."""

import subprocess
from pathlib import Path

from utils.caption_utils import build_captioned_video_filename


class VideoCaptionBurnService:
    """Burn caption files permanently into videos."""

    def __init__(
        self,
        output_dir: str | Path = "outputs",
    ) -> None:
        """Initialize the video caption burn service."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def build_output_path(
        self,
        video_path: str | Path,
        language_code: str,
    ) -> Path:
        """Build the output path for a captioned video."""
        filename = build_captioned_video_filename(
            video_path,
            language_code,
        )

        return self.output_dir / filename

    def burn(
        self,
        video_path: str | Path,
        caption_path: str | Path,
        language_code: str,
    ) -> Path:
        """Burn captions permanently into the video."""
        video = Path(video_path)
        captions = Path(caption_path)

        if not video.is_file():
            raise FileNotFoundError(
                f"Video not found: {video}"
            )

        if not captions.is_file():
            raise FileNotFoundError(
                f"Caption file not found: {captions}"
            )

        output_path = self.build_output_path(
            video,
            language_code,
        )

        # Resolve the caption path to an absolute path.
        #
        # FFmpeg's subtitles filter requires special handling
        # for Windows drive-letter paths such as C:\...
        subtitle_path = captions.resolve().as_posix()

        # Escape the Windows drive-letter colon for FFmpeg's
        # filter syntax.
        subtitle_filter_path = subtitle_path.replace(
            ":",
            r"\:",
        )

        command = [
            "ffmpeg",
            "-y",
            "-i",
            str(video),
            "-vf",
            f"subtitles=filename='{subtitle_filter_path}'",
            "-c:a",
            "copy",
            str(output_path),
        ]

        try:
            subprocess.run(
                command,
                check=True,
                capture_output=True,
                text=True,
            )

        except subprocess.CalledProcessError as exc:
            error_message = (
                exc.stderr.strip()
                if exc.stderr
                else "No FFmpeg error output available."
            )

            raise RuntimeError(
                "FFmpeg failed to burn captions into "
                "the video.\n"
                f"{error_message}"
            ) from exc

        if not output_path.is_file():
            raise RuntimeError(
                "FFmpeg completed but output video "
                "was not created."
            )

        return output_path