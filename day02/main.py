from __future__ import annotations

import argparse
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def part_one(s: str) -> int:
    pts = 0
    for g in s.splitlines():
        p_1, p_2 = map(ord, g.split())
        p_1 -= 64
        p_2 -= 87
        if p_2 - p_1 == 1 or p_2 - p_1 == -2:
            pts += 6
        elif p_2 == p_1:
            pts += 3
        pts += p_2
    return pts


def part_two(s: str) -> int:
    pts = 0
    for g in s.splitlines():
        p_1, p_2 = map(ord, g.split())
        p_1 -= 64
        p_2 = (p_2 - 88) * 3
        if p_2 == 6:
            pts += 1 + p_1 % 3
        elif p_2 == 3:
            pts += p_1
        else:
            pts += 3 if p_1 == 1 else p_1 - 1
        pts += p_2
    return pts


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
