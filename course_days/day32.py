from pathlib import Path


def cwd_name() -> str:
    return Path.cwd().name


def main() -> None:
    print(cwd_name())


if __name__ == "__main__":
    main()
