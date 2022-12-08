from __future__ import annotations

import argparse
import os.path
import re
from collections import deque

from typing import cast


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

MOVE_RE = "move (\d+) from (\d+) to (\d+)"


def parse_input(s: str) -> tuple[list[deque[str]], list[tuple[int, int, int]]]:
    stack_rows, move_rows = map(lambda x: x.splitlines(), s.split("\n\n"))
    stack_rows = stack_rows[:-1]
    stacks: list[deque[str]] = []
    moves: list[tuple] = []

    for _ in range((len(stack_rows[0]) + 1) // 4):
        stacks.append(deque())

    for row in stack_rows:
        for i in range(0, len(row), 4):
            stack = row[i : i + 3]
            if stack != "   ":
                stacks[i // 4].appendleft(stack[1])

    for row in move_rows:
        moves.append(tuple(map(int, re.findall(MOVE_RE, row)[0])))

    return stacks, cast(list[tuple[int, int, int]], moves)


def part_one(s: str) -> str:
    stacks, moves = parse_input(s)
    for move in moves:
        q, f, t = move
        stacks[t - 1].extend(stacks[f - 1].pop() for _ in range(q))
    return "".join(stack[-1] for stack in stacks)


def part_two(s: str) -> str:
    stacks, moves = parse_input(s)
    for move in moves:
        q, f, t = move
        stacks[t - 1].extend(reversed([stacks[f - 1].pop() for _ in range(q)]))
    return "".join(stack[-1] for stack in stacks)


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
