import os


def load_timeout() -> int:
    value = int(os.environ.get("APP_TIMEOUT", "5"))
    if not 1 <= value <= 60:
        raise ValueError("timeout must be between 1 and 60 seconds")
    return value


def main() -> None:
    print(load_timeout())


if __name__ == "__main__":
    main()
