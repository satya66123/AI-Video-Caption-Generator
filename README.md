# AI Video Caption Generator

An AI-powered video caption generator that detects the spoken language of a video, allows the user to select a caption language, generates timestamped captions, creates SRT/VTT files, and optionally burns captions into the video.

## Current Status

Phase 0 — General Phase

The project foundation and repository structure are currently being prepared.

## Planned Workflow

Video
→ Detect Spoken Language
→ Select Caption Language
→ Generate Captions
→ SRT / VTT
→ Preview
→ Burn Captions Into Video

## Storage

Caption-related history will use JSON only.

The Caption Generator will not duplicate or store:

- Transcripts
- Video analysis
- Reports
- Existing exports
- Chat sessions
- Audio history
- Other unrelated video history

## Output Naming

Generated files will preserve the original video name.

Example:

```text
video.mp4
video_en.srt
video_en.vtt
video_en_captioned.mp4