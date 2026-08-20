"""Day 2 starter: preserve raw input while naming its context."""


def describe_event(raw_line: str, source: str) -> dict[str, str]:
    return {"raw": raw_line, "source": source}


def main() -> None:
    event = describe_event("login_failed user=maya", "synthetic-auth.log")
    print(event)


if __name__ == "__main__":
    main()
