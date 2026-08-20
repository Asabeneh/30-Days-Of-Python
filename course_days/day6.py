"""Day 6 starter: process only a declared number of lines."""


def bounded_matches(lines: list[str], needle: str, limit: int) -> list[str]:
    if limit < 0:
        raise ValueError("limit must not be negative")
    return [line for line in lines[:limit] if needle in line]


def main() -> None:
    lines = ["ok", "login_failed user=maya", "ok"]
    print(bounded_matches(lines, "login_failed", 2))


if __name__ == "__main__":
    main()
