from scripts.video_catalog import load_catalog, timestamp, validate


def test_video_catalog_is_valid() -> None:
    resources = load_catalog()
    assert len(resources) >= 7
    assert validate(resources) == []


def test_timestamp_format_is_learner_friendly() -> None:
    assert timestamp(0) == "00:00"
    assert timestamp(252) == "04:12"
    assert timestamp(3723) == "1:02:03"
