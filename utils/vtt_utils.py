"""WebVTT caption formatting utilities."""

from core.caption_models import CaptionSegment


def format_vtt_timestamp(seconds: float) -> str:
    """Convert seconds to a WebVTT timestamp."""
    if seconds < 0:
        raise ValueError("Timestamp cannot be negative.")

    milliseconds = round(seconds * 1000)

    hours = milliseconds // 3_600_000
    milliseconds %= 3_600_000

    minutes = milliseconds // 60_000
    milliseconds %= 60_000

    secs = milliseconds // 1_000
    milliseconds %= 1_000

    return f"{hours:02}:{minutes:02}:{secs:02}.{milliseconds:03}"


def generate_vtt(segments: list[CaptionSegment]) -> str:
    """Generate WebVTT content from caption segments."""
    if not segments:
        raise ValueError("Caption segments cannot be empty.")

    blocks: list[str] = ["WEBVTT", ""]

    for index, segment in enumerate(segments, start=1):
        if segment.start < 0:
            raise ValueError("Caption start time cannot be negative.")

        if segment.end <= segment.start:
            raise ValueError(
                "Caption end time must be greater than start time."
            )

        if not segment.text.strip():
            raise ValueError("Caption text cannot be empty.")

        start = format_vtt_timestamp(segment.start)
        end = format_vtt_timestamp(segment.end)

        blocks.extend(
            [
                str(index),
                f"{start} --> {end}",
                segment.text.strip(),
                "",
            ]
        )

    return "\n".join(blocks)