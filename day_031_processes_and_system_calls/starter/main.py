import os


def process_summary() -> dict[str, object]:
    return {"pid": os.getpid(), "cwd": os.getcwd()}


def main() -> None:
    print(process_summary())


if __name__ == "__main__":
    main()
