from pathlib import Path


def baseline_report(root: Path, expected: dict[str, str]) -> dict[str, object]:
    observed = {
        path.name: str(path.stat().st_size) for path in root.iterdir() if path.is_file()
    }
    return {"expected": expected, "observed": observed, "scope": str(root)}


def main() -> None:
    print(baseline_report(Path("."), {}))


if __name__ == "__main__":
    main()
