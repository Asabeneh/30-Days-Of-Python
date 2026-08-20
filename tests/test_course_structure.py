from scripts.course_doctor import REQUIRED_DIRS, REQUIRED_ROOT_FILES, ROOT, check


def test_required_root_files_exist() -> None:
    assert all((ROOT / name).is_file() for name in REQUIRED_ROOT_FILES)


def test_required_directories_exist() -> None:
    assert all((ROOT / name).is_dir() for name in REQUIRED_DIRS)


def test_first_ten_days_have_lesson_and_practice() -> None:
    day_dirs = sorted(ROOT.glob("[0-9][0-9][0-9]_day_*"))
    assert len(day_dirs) >= 10
    for day_dir in day_dirs[:10]:
        assert (day_dir / f"{day_dir.name}.md").is_file()
        assert (day_dir / "starter").is_dir()
        assert (day_dir / "practice").is_dir()


def test_course_doctor_has_no_findings() -> None:
    assert check() == []
