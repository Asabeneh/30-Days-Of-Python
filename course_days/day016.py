import re

IP_CANDIDATE = re.compile(r"(?<![0-9])(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![0-9])")


def extract_candidates(line: str) -> list[str]:
    return IP_CANDIDATE.findall(line)


def main() -> None:
    print(extract_candidates("src=203.0.113.8"))


if __name__ == "__main__":
    main()
