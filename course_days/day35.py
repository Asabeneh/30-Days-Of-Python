from pathlib import Path


def permission_mode(path: Path) -> str:
    return oct(path.stat().st_mode & 0o777)


def main() -> None:
    print(permission_mode(Path(".")))


if __name__ == "__main__":
    main()
