"""Validate the course structure and report beginner-facing setup problems."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT_FILES = {
    "README.md",
    "SETUP.md",
    "VS_CODE_SETUP.md",
    "SAFETY_AND_LAB_RULES.md",
    "CURRICULUM_GUIDE.md",
    "COURSE_QUALITY_STANDARD.md",
    "LEETCODE_GUIDE.md",
    "RESOURCES.md",
    "TROUBLESHOOTING.md",
    "COURSE_PLAN_DRAFT.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "GLOSSARY.md",
    "EXERCISE_STANDARD.md",
    "EXERCISE_REDESIGN_NOTES.md",
    "DENSE_LESSON_STANDARD.md",
    "TEACHING_DEPTH_AUDIT.md",
    "TEACHING_DEPTH_REPORT.md",
    "VIDEO_RESOURCE_STANDARD.md",
    "VIDEO_RESOURCES.md",
    "VIDEO_RESEARCH_NOTES.md",
    "video_resources.json",
    "pyproject.toml",
}
REQUIRED_DIRS = {"scripts", "tests", "shared", "projects", "specializations"}


def check() -> list[str]:
    errors: list[str] = []
    missing_files = sorted(
        name for name in REQUIRED_ROOT_FILES if not (ROOT / name).exists()
    )
    errors.extend(f"missing root file: {name}" for name in missing_files)
    missing_dirs = sorted(name for name in REQUIRED_DIRS if not (ROOT / name).is_dir())
    errors.extend(f"missing directory: {name}" for name in missing_dirs)

    day_dirs = sorted(ROOT.glob("day_*"))
    if len(day_dirs) != 120:
        errors.append(f"expected exactly 120 day directories, found {len(day_dirs)}")

    specialization_names = (
        "blue-team",
        "appsec",
        "dfir",
        "malware-analysis-foundations",
        "cloud-devsecops",
        "network-security",
    )
    for specialization in specialization_names:
        readme = ROOT / "specializations" / specialization / "README.md"
        if not readme.exists():
            errors.append(f"missing specialization guide: {readme.relative_to(ROOT)}")

    for day_dir in day_dirs:
        lesson = day_dir / f"{day_dir.name}.md"
        if not lesson.exists():
            errors.append(f"missing lesson: {lesson.relative_to(ROOT)}")
        for required in ("starter", "practice"):
            if not (day_dir / required).is_dir():
                errors.append(
                    f"missing {required} directory: {day_dir.relative_to(ROOT)}"
                )
        if (day_dir / "lab").exists() and not (day_dir / "lab/scope.md").exists():
            errors.append(f"security lab is missing scope: {day_dir.relative_to(ROOT)}")

    legacy_markers = (
        "30DaysOfPython",
        "30 Days Of Python",
        "sponsor",
        "telegram group",
    )
    for path in (ROOT / "README.md", ROOT / "SETUP.md"):
        if path.exists():
            text = path.read_text(encoding="utf-8").lower()
            for marker in legacy_markers:
                if marker.lower() in text:
                    errors.append(
                        f"legacy marker {marker!r} remains in {path.relative_to(ROOT)}"
                    )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict", action="store_true", help="return non-zero for any finding"
    )
    args = parser.parse_args()
    errors = check()
    if errors:
        print("Course doctor found:")
        for error in errors:
            print(f"- {error}")
        return 1 if args.strict else 0
    print("Course doctor: OK")
    print(f"Repository: {ROOT}")
    print("Root guides, setup files, directories, and lessons are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
