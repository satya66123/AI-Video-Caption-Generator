[![GitHub Actions](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions/workflows/python-app.yml)
[![Tests](https://img.shields.io/badge/Tests-153%20Passed-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator/actions)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/satya66123/AI-Video-Caption-Generator)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.com/)
[![Whisper](https://img.shields.io/badge/Speech-Whisper-blueviolet.svg)](https://github.com/openai/whisper)
[![FFmpeg](https://img.shields.io/badge/Video-FFmpeg-green.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Frequently Asked Questions

## What does the application do?

It converts spoken video content into multilingual captions and can permanently burn them into a separate video.

## Does it save the original video?

Yes. The original is preserved separately.

## Which subtitle formats are supported?

SRT and VTT.

## Which video formats are supported?

MP4, MOV, AVI, MKV and WebM.

## Which languages are supported?

English, Telugu, Hindi, Tamil, Kannada, Malayalam, Bengali, Marathi, Gujarati and Punjabi.

## Does translation require a cloud API?

The core translation workflow uses local Ollama.

## Which translation model is configured?

`translategemma:12b`.

## What does Whisper do?

Whisper performs internal timestamped transcription.

## What does FFmpeg do?

FFmpeg permanently burns captions into the final output video.

## Where are files stored?

Original videos are in `uploads/`, subtitle files in `captions/`, and captioned videos in `outputs/`.

## Are transcripts stored as transcript history?

No. Transcript data is used as an internal processing artifact.

## How many tests pass?

The final verified suite contains 145 passing tests.
