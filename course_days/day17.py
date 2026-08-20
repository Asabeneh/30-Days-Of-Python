from datetime import UTC, datetime


def parse_timestamp(text: str) -> datetime:
    value = datetime.fromisoformat(text.replace("Z", "+00:00"))
    if value.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return value.astimezone(UTC)


def main() -> None:
    print(parse_timestamp("2026-08-20T12:00:00Z"))


if __name__ == "__main__":
    main()
