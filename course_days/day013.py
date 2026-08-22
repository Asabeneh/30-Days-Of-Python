def parse_severity(text: str) -> int:
    try:
        value = int(text)
    except ValueError as error:
        raise ValueError("severity must be an integer") from error
    if not 0 <= value <= 10:
        raise ValueError("severity is outside the allowed range")
    return value


def main() -> None:
    print(parse_severity("7"))


if __name__ == "__main__":
    main()
