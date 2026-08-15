"""Caption agent."""

from pathlib import Path
from typing import Any

from config.caption_config import DEFAULT_CAPTION_LANGUAGE
from core.caption_models import CaptionSegment
from services.caption_generation_service import CaptionGenerationService
from services.language_detection_service import LanguageDetectionService
from utils.caption_utils import validate_caption_language
from services.caption_file_service import CaptionFileService
from services.video_caption_burn_service import VideoCaptionBurnService
from utils.srt_utils import generate_srt
from utils.vtt_utils import generate_vtt


class CaptionAgent:
    """Main agent responsible for the caption-generation workflow."""

    def __init__(
        self,
        language_detection_service: LanguageDetectionService | None = None,
        transcript_service: Any | None = None,
        caption_generation_service: (
            CaptionGenerationService | None
        ) = None,
            caption_file_service: CaptionFileService | None = None,
            video_caption_burn_service: VideoCaptionBurnService | None = None,
    ) -> None:
        """Initialize the caption agent."""
        self.caption_file_service = (
                caption_file_service
                or CaptionFileService()
        )

        self.video_caption_burn_service = (
                video_caption_burn_service
                or VideoCaptionBurnService()
        )
        self.language_detection_service = (
            language_detection_service
            or LanguageDetectionService()
        )

        # Transcript is an internal processing dependency.
        # It is not persisted as transcript history.
        self.transcript_service = transcript_service

        # Caption generation is kept injectable so tests can use
        # a mocked service and production can use TranslateGemma.
        self.caption_generation_service = (
            caption_generation_service
        )

    def select_caption_language(
        self,
        language_code: str = DEFAULT_CAPTION_LANGUAGE,
    ) -> str:
        """Validate and return the selected caption language."""
        normalized_language = language_code.strip().lower()

        if not validate_caption_language(normalized_language):
            raise ValueError(
                f"Unsupported caption language: {language_code}"
            )

        return normalized_language

    def generate_caption_files(
            self,
            video_path: str | Path,
            caption_language: str = DEFAULT_CAPTION_LANGUAGE,
    ) -> dict[str, Any]:
        """
        Generate translated SRT and VTT caption files.

        Transcript data remains internal and is not persisted.
        """
        selected_language = self.select_caption_language(
            caption_language
        )

        translated_segments = self.generate_captions(
            video_path=video_path,
            caption_language=selected_language,
        )

        srt_content = generate_srt(
            translated_segments
        )

        vtt_content = generate_vtt(
            translated_segments
        )

        srt_path = self.caption_file_service.save_srt(
            video_path=video_path,
            language_code=selected_language,
            content=srt_content,
        )

        vtt_path = self.caption_file_service.save_vtt(
            video_path=video_path,
            language_code=selected_language,
            content=vtt_content,
        )

        return {
            "video_path": str(video_path),
            "caption_language": selected_language,
            "segments": translated_segments,
            "srt_path": srt_path,
            "vtt_path": vtt_path,
        }

    def generate_captioned_video(
            self,
            video_path: str | Path,
            caption_language: str = DEFAULT_CAPTION_LANGUAGE,
    ) -> dict[str, Any]:
        """
        Generate captions and permanently burn them into the video.
        """
        result = self.generate_caption_files(
            video_path=video_path,
            caption_language=caption_language,
        )

        output_video = self.video_caption_burn_service.burn(
            video_path=video_path,
            caption_path=result["srt_path"],
            language_code=result["caption_language"],
        )

        result["output_video"] = output_video

        return result

    def transcribe(
        self,
        video_path: str | Path,
    ) -> Any:
        """
        Generate an internal timestamped transcript.

        The transcript is used only during caption generation
        and is not stored as transcript history.
        """
        if self.transcript_service is None:
            raise RuntimeError(
                "Transcript service is not configured."
            )

        return self.transcript_service.transcribe(
            video_path
        )

    def detect_language(
        self,
        video_path: str | Path,
    ) -> dict[str, object]:
        """Detect the spoken language of a video."""
        return self.language_detection_service.detect(
            video_path
        )

    def prepare_caption_workflow(
        self,
        video_path: str | Path,
        caption_language: str = DEFAULT_CAPTION_LANGUAGE,
    ) -> dict[str, Any]:
        """
        Prepare the internal video-to-caption workflow.

        The transcript is generated in memory and returned as part
        of the workflow result. It is not persisted as transcript
        history.
        """
        selected_language = self.select_caption_language(
            caption_language
        )

        transcript = self.transcribe(video_path)

        detected_language = self.detect_language(
            video_path
        )

        return {
            "video_path": str(video_path),
            "transcript": transcript,
            "detected_language": detected_language,
            "caption_language": selected_language,
        }

    def get_caption_segments(
        self,
        transcript: dict[str, Any],
    ) -> list[CaptionSegment]:
        """Convert internal transcript segments to caption segments."""
        segments = transcript.get("segments", [])

        if not segments:
            raise ValueError(
                "Transcript does not contain caption segments."
            )

        caption_segments: list[CaptionSegment] = []

        for segment in segments:
            caption_segments.append(
                CaptionSegment(
                    start=float(segment["start"]),
                    end=float(segment["end"]),
                    text=str(segment["text"]).strip(),
                )
            )

        return caption_segments

    def prepare_caption_segments(
        self,
        video_path: str | Path,
        caption_language: str = DEFAULT_CAPTION_LANGUAGE,
    ) -> dict[str, Any]:
        """
        Prepare timestamped caption segments for translation.

        The transcript remains an internal processing artifact
        and is not persisted as transcript history.
        """
        selected_language = self.select_caption_language(
            caption_language
        )

        transcript = self.transcribe(video_path)

        caption_segments = self.get_caption_segments(
            transcript
        )

        detected_language = self.detect_language(
            video_path
        )

        return {
            "video_path": str(video_path),
            "detected_language": detected_language,
            "caption_language": selected_language,
            "segments": caption_segments,
        }

    def generate_captions(
        self,
        video_path: str | Path,
        caption_language: str = DEFAULT_CAPTION_LANGUAGE,
    ) -> list[CaptionSegment]:
        """
        Generate translated caption segments from a video.

        Flow:
            Video
            -> internal transcript
            -> timestamped CaptionSegments
            -> TranslateGemma/translation provider
            -> translated CaptionSegments

        Transcript data is not persisted.
        """
        if self.caption_generation_service is None:
            raise RuntimeError(
                "Caption generation service is not configured."
            )

        prepared = self.prepare_caption_segments(
            video_path=video_path,
            caption_language=caption_language,
        )

        segments = prepared["segments"]
        target_language = prepared["caption_language"]

        return self.caption_generation_service.generate(
            segments=segments,
            target_language=target_language,
        )