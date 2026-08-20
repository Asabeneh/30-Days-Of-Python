from course_days.day23 import load_timeout
from course_days.day24 import validate_record
from course_days.day26 import redact
from course_days.day28 import dependency_record
from course_days.day30 import JournalEntry


def test_configuration_has_a_bounded_default(monkeypatch) -> None:
    monkeypatch.delenv("APP_TIMEOUT", raising=False)
    assert load_timeout() == 5


def test_json_boundary_requires_integer_severity() -> None:
    assert validate_record('{"severity": 5}') == {"severity": 5}


def test_redaction_removes_secret_value_from_output() -> None:
    assert redact({"token": "synthetic", "actor": "maya"}) == {
        "token": "[REDACTED]",
        "actor": "maya",
    }


def test_dependency_record_requires_all_fields() -> None:
    assert dependency_record("pytest", "8.x", "tests")["purpose"] == "tests"


def test_journal_entry_is_an_explicit_record() -> None:
    entry = JournalEntry("2026-08-20T12:00:00Z", "fixture", "event")
    assert entry.source == "fixture"
