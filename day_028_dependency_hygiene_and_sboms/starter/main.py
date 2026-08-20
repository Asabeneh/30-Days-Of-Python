def dependency_record(name: str, version: str, purpose: str) -> dict[str, str]:
    if not all((name.strip(), version.strip(), purpose.strip())):
        raise ValueError("dependency fields must be non-empty")
    return {"name": name, "version": version, "purpose": purpose}


def main() -> None:
    print(dependency_record("pytest", "8.x", "tests"))


if __name__ == "__main__":
    main()
