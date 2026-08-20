def environment_summary() -> dict[str, str]:
    return {"python": "3.11+", "environment": ".venv", "install": "python -m pip"}


def main() -> None:
    print(environment_summary())


if __name__ == "__main__":
    main()
