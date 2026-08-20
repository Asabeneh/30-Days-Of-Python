import json


def validate_record(text: str) -> dict[str, object]:
    record = json.loads(text)
    if not isinstance(record, dict) or not isinstance(record.get("severity"), int):
        raise ValueError("record must contain integer severity")
    return record


def main() -> None:
    print(validate_record('{"severity": 5}'))


if __name__ == "__main__":
    main()
