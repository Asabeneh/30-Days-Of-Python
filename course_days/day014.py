from pathlib import Path


def safe_path(base: Path, requested: str) -> Path:
    candidate = (base / requested).resolve()
    base_resolved = base.resolve()
    if candidate != base_resolved and base_resolved not in candidate.parents:
        raise ValueError("path escapes the evidence directory")
    return candidate


def main() -> None:
    print(safe_path(Path("fixtures"), "case.txt"))


if __name__ == "__main__":
    main()
