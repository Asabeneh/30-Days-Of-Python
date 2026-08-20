from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMP_PREFIX = "__rename_tmp_day_"


def lesson_dirs() -> list[Path]:
    return sorted(
        (
            p
            for p in ROOT.iterdir()
            if p.is_dir() and re.fullmatch(r"day_\d+_.+", p.name)
        ),
        key=lambda p: int(p.name.split("_", 2)[1]),
    )


def rename_with_temporary_names(paths: list[tuple[Path, Path]]) -> None:
    temporary: list[tuple[Path, Path, Path]] = []
    for index, (old, new) in enumerate(paths):
        temp = old.with_name(f"{TEMP_PREFIX}{index:03d}")
        old.rename(temp)
        temporary.append((temp, old, new))
    for temp, _old, new in temporary:
        temp.rename(new)


def collect_mapping() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for directory in lesson_dirs():
        day = int(directory.name.split("_", 2)[1])
        new_name = re.sub(r"^day_\d+", f"day_{day:03d}", directory.name)
        mapping[directory.name] = new_name
        for child in directory.rglob("*"):
            if child.is_file() and child.name.startswith(directory.name):
                new_child = child.name.replace(directory.name, new_name, 1)
                mapping[str(child.relative_to(ROOT))] = str(
                    (
                        Path(new_name) / child.relative_to(directory).parent / new_child
                    ).as_posix()
                )
    for module in (ROOT / "course_days").glob("day*.py"):
        match = re.fullmatch(r"day(\d+)\.py", module.name)
        if match:
            mapping[str(module.relative_to(ROOT))] = str(
                (Path("course_days") / f"day{int(match.group(1)):03d}.py").as_posix()
            )
    return mapping


def rename_paths(mapping: dict[str, str]) -> None:
    directory_pairs = []
    for old, new in mapping.items():
        old_path = ROOT / old
        new_path = ROOT / new
        if old_path.parent == ROOT and old_path.is_dir():
            directory_pairs.append((old_path, new_path))
    rename_with_temporary_names(directory_pairs)

    module_pairs = []
    for old, new in mapping.items():
        old_path = ROOT / old
        new_path = ROOT / new
        if old_path.parent == ROOT / "course_days" and old_path.is_file():
            module_pairs.append((old_path, new_path))
    rename_with_temporary_names(module_pairs)

    for old, new in mapping.items():
        old_path = ROOT / old
        new_path = ROOT / new
        if old_path.is_file() and old_path != new_path:
            new_path.parent.mkdir(parents=True, exist_ok=True)
            old_path.rename(new_path)


def replace_references(mapping: dict[str, str]) -> None:
    text_files = [
        p
        for p in ROOT.rglob("*")
        if p.is_file()
        and ".git" not in p.parts
        and "node_modules" not in p.parts
        and p.suffix.lower()
        in {".md", ".py", ".json", ".toml", ".txt", ".yml", ".yaml", ".ini", ".sh"}
    ]
    replacements = sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True)
    for path in text_files:
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in replacements:
            updated = updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")


def main() -> None:
    mapping = collect_mapping()
    rename_paths(mapping)
    replace_references(mapping)
    print(
        f"Renamed {len(lesson_dirs())} lesson directories and "
        f"updated {len(mapping)} path mappings."
    )


if __name__ == "__main__":
    main()
