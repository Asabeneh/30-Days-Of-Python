SENSITIVE_KEYS = {"password", "token", "secret"}


def redact(event: dict[str, object]) -> dict[str, object]:
    return {
        key: "[REDACTED]" if key in SENSITIVE_KEYS else value
        for key, value in event.items()
    }


def main() -> None:
    print(redact({"actor": "maya", "token": "synthetic-only"}))


if __name__ == "__main__":
    main()
