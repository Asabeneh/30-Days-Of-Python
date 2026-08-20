def threat_entry(
    asset: str, boundary: str, threat: str, control: str
) -> dict[str, str]:
    return {"asset": asset, "boundary": boundary, "threat": threat, "control": control}


def main() -> None:
    print(threat_entry("case record", "parser", "malformed field", "schema validation"))


if __name__ == "__main__":
    main()
