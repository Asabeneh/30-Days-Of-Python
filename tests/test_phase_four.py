import asyncio
from pathlib import Path

from course_days.day033 import inventory
from course_days.day034 import python_version
from course_days.day037 import ordered_upper
from course_days.day038 import collect
from course_days.day039 import diff


def test_inventory_is_local_and_structured(tmp_path: Path) -> None:
    (tmp_path / "event.txt").write_text("synthetic", encoding="utf-8")
    assert inventory(tmp_path)[0]["name"] == "event.txt"


def test_subprocess_wrapper_returns_a_version() -> None:
    assert "Python" in python_version()


def test_concurrency_preserves_input_order() -> None:
    assert ordered_upper(["a", "b"]) == ["A", "B"]


def test_async_collection_returns_all_results() -> None:
    assert asyncio.run(collect(["a", "b"])) == ["a", "b"]


def test_baseline_diff_names_added_and_changed() -> None:
    result = diff({"mode": "safe"}, {"mode": "unsafe", "new": "value"})
    assert result["added"] == ["new"]
    assert result["changed"] == ["mode"]
