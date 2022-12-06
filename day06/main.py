from __future__ import annotations

import argparse
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def get_unique_sequence(s: str, l: int) -> int:
    for i in range(len(s) - l):
        if len(set(s[i : i + l])) == l:
            return i + l


def part_one(s: str) -> int:
    return get_unique_sequence(s, 4)


def part_two(s: str) -> int:
    return get_unique_sequence(s, 14)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        data = f.read()
        print(f"Part one: {part_one(data)}")
        print(f"Part two: {part_two(data)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
