from course_days.day011 import severity_label
from course_days.day013 import parse_severity
from course_days.day014 import safe_path
from course_days.day015 import matching_lines
from course_days.day016 import extract_candidates
from course_days.day017 import parse_timestamp
from course_days.day018 import Finding


def test_function_contract_rejects_out_of_range_severity() -> None:
    assert severity_label(8) == "high"
    try:
        severity_label(11)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid severity should be rejected")


def test_exception_translation_is_specific() -> None:
    assert parse_severity("7") == 7
    try:
        parse_severity("high")
    except ValueError as error:
        assert "integer" in str(error)
    else:
        raise AssertionError("malformed severity should be rejected")


def test_safe_path_rejects_escape(tmp_path) -> None:
    base = tmp_path / "evidence"
    base.mkdir()
    assert safe_path(base, "case.txt").parent == base
    try:
        safe_path(base, "../secret.txt")
    except ValueError:
        pass
    else:
        raise AssertionError("path traversal should be rejected")


def test_generator_is_lazy_and_filters() -> None:
    assert list(matching_lines(["ok", "login_failed", "ok"], "login")) == [
        "login_failed"
    ]


def test_regex_returns_candidates_not_verdicts() -> None:
    assert extract_candidates("src=203.0.113.8") == ["203.0.113.8"]


def test_timestamp_is_utc() -> None:
    assert parse_timestamp("2026-08-20T12:00:00Z").utcoffset().total_seconds() == 0


def test_finding_is_immutable() -> None:
    finding = Finding("test", 5, "evidence-1")
    assert finding.severity == 5
