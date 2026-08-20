from pathlib import Path


def inventory(root: Path) -> list[dict[str, object]]:
    return [
        {"name": p.name, "size": p.stat().st_size}
        for p in root.iterdir()
        if p.is_file()
    ]


def main() -> None:
    print(inventory(Path("."))[:3])


if __name__ == "__main__":
    main()
