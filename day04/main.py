from __future__ import annotations

import argparse
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def part_one(s: str) -> int:
    count = 0
    for p in s.splitlines():
        (a, b), (c, d) = (map(int, i.split("-")) for i in p.split(","))
        if (a <= c and b >= d) or (c <= a and d >= b):
            count += 1
    return count


def part_two(s: str) -> int:
    count = 0
    for p in s.splitlines():
        (a, b), (c, d) = (map(int, i.split("-")) for i in p.split(","))
        if c <= a <= d or a <= c <= b:
            count += 1
    return count


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
