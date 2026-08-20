"""Day 3 starter: parse a bounded status field."""


def parse_status(text: str) -> int:
    value = int(text)
    if not 100 <= value <= 599:
        raise ValueError("status must be an HTTP-style code")
    return value


def main() -> None:
    print(parse_status("200"))


if __name__ == "__main__":
    main()
