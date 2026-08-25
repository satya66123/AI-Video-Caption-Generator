from pathlib import Path


def test_captioned_video_output_name() -> None:
    output = Path("outputs/gm_en_captioned.mp4")

    assert output.name == "gm_en_captioned.mp4"


def test_captioned_video_is_mp4() -> None:
    output = Path("outputs/gm_en_captioned.mp4")

    assert output.suffix == ".mp4"


def test_captioned_video_preserves_original_stem() -> None:
    original = Path("uploads/gm.mp4")
    output = Path("outputs/gm_en_captioned.mp4")

    assert output.name.startswith(original.stem)


def test_captioned_video_contains_language_code() -> None:
    output = Path("outputs/gm_en_captioned.mp4")

    assert "_en_" in output.name
