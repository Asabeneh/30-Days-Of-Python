"""Day 8 starter: normalize without destroying raw evidence."""


def normalize_username(raw: str) -> str:
    return raw.strip().casefold()


def main() -> None:
    raw = "  Admin  "
    print({"raw": raw, "normalized": normalize_username(raw)})


if __name__ == "__main__":
    main()
