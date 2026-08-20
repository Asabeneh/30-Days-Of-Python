from course_days.day002 import describe_event
from course_days.day003 import parse_status
from course_days.day005 import classify
from course_days.day006 import bounded_matches
from course_days.day008 import normalize_username
from course_days.day009 import is_nonempty_text
from course_days.day010 import classify_event


def test_day_two_preserves_raw_and_source() -> None:
    assert describe_event("login_failed", "fixture.log") == {
        "raw": "login_failed",
        "source": "fixture.log",
    }


def test_day_three_rejects_out_of_range_status() -> None:
    assert parse_status("200") == 200
    try:
        parse_status("999")
    except ValueError as error:
        assert "status" in str(error)
    else:
        raise AssertionError("out-of-range status should be rejected")


def test_day_five_classifies_boundaries() -> None:
    assert classify(4, True)[0] == "ignore"
    assert classify(5, True)[0] == "review"
    assert classify(9, True)[0] == "urgent_review"
    assert classify(10, False)[0] == "ignore"


def test_day_six_respects_the_bound() -> None:
    lines = ["bad", "bad", "bad"]
    assert bounded_matches(lines, "bad", 2) == ["bad", "bad"]


def test_day_eight_preserves_case_insensitive_comparison() -> None:
    assert normalize_username("  Admin ") == "admin"


def test_day_nine_accepts_only_nonempty_text() -> None:
    assert is_nonempty_text("event") is True
    assert is_nonempty_text(" ") is False
    assert is_nonempty_text(None) is False


def test_day_ten_is_explainable_and_narrow() -> None:
    assert classify_event(9, True) == ("urgent_review", "high severity")
    assert classify_event(9, False)[0] == "ignore"
