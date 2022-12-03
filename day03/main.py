from __future__ import annotations

import argparse
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def get_priority(c: str) -> int:
    p = ord(c)
    return p - 96 if p >= 97 else p - 38


def part_one(s: str) -> int:
    total = 0
    for r in s.splitlines():
        fc, sc = set(r[: len(r) // 2]), set(r[len(r) // 2 :])
        total += sum(map(get_priority, fc & sc))
    return total


def part_two(s: str) -> int:
    inp = s.splitlines()

    total = 0
    for g in range(0, len(inp), 3):
        (b,) = set(inp[g]) & set(inp[g + 1]) & set(inp[g + 2])
        total += get_priority(b)

    return total


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
