import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Bounded synthetic log reader")
    parser.add_argument("--limit", type=int, default=100)
    return parser


def main() -> None:
    print(build_parser().parse_args([]))


if __name__ == "__main__":
    main()
