from agents.caption_agent import CaptionAgent


def test_transcript_segments_convert_to_caption_segments() -> None:
    agent = CaptionAgent(
        language_detection_service=None,
        transcript_service=None,
    )

    transcript = {
        "text": "Hello everyone",
        "segments": [
            {
                "start": 0.0,
                "end": 2.5,
                "text": " Hello everyone ",
            },
            {
                "start": 2.5,
                "end": 5.0,
                "text": " Welcome ",
            },
        ],
    }

    result = agent.get_caption_segments(transcript)

    assert len(result) == 2

    assert result[0].start == 0.0
    assert result[0].end == 2.5
    assert result[0].text == "Hello everyone"

    assert result[1].start == 2.5
    assert result[1].end == 5.0
    assert result[1].text == "Welcome"


def test_empty_transcript_segments_are_rejected() -> None:
    agent = CaptionAgent(
        language_detection_service=None,
        transcript_service=None,
    )

    transcript = {
        "text": "",
        "segments": [],
    }

    try:
        agent.get_caption_segments(transcript)
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == ("Transcript does not contain caption segments.")
