from __future__ import annotations

import argparse
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def part_one(s: str) -> int:
    top = 0
    for i in s.split("\n\n"):
        total = sum(int(c) for c in i.splitlines())
        if total > top:
            top = total
    return top


def part_two(s: str) -> int:
    top_1 = top_2 = top_3 = 0
    for i in s.split("\n\n"):
        total = sum(int(c) for c in i.splitlines())
        if total > top_3:
            if total > top_2:
                if total > top_1:
                    top_1, top_2, top_3 = total, top_1, top_2
                else:
                    top_2, top_3 = total, top_2
            else:
                top_3 = total
    return top_1 + top_2 + top_3


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
