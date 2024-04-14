#!/usr/bin/env python3
"""A script to count lines in a file or stream and LOC in a file."""

from argparse import ArgumentParser, Namespace
from io import TextIOWrapper


def parse_args() -> Namespace:
    """Parse command line arguments"""
    parser = ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument(
        "--lines-of-code",
        "-l",
        action="store_true",
    )
    return parser.parse_args()


def get_line_count(file: TextIOWrapper) -> int:
    """Get amount of lines in a file or stream"""
    base_length = len(file.readlines())
    file.seek(0)
    if file.read().endswith("\n"):
        return base_length + 1
    return base_length


def get_lines_of_code(file: TextIOWrapper) -> int:
    """Get amount of non-empty lines in a file or stream"""
    return len(list(filter(lambda line: len(line) > 1, file.readlines())))


def main():
    """Entry point for count lines"""
    args = parse_args()
    filename = args.filename
    target_loc = args.lines_of_code

    with open(filename, "r", encoding="utf-8") as file:
        if target_loc:
            print(get_lines_of_code(file))
            return

        print(get_line_count(file))


if __name__ == "__main__":
    main()
