"""Day 9 starter: keep validation small and deterministic."""


def is_nonempty_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def main() -> None:
    for value in ["event", "", None, 7]:
        print(repr(value), is_nonempty_text(value))


if __name__ == "__main__":
    main()
