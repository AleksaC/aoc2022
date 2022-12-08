from __future__ import annotations

import argparse
import os.path
from dataclasses import dataclass
from dataclasses import field


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


# at some point this solution started going in a wrong direction but since it was
# late night I just kept going with it until I got the solution
@dataclass
class Node:
    is_dir: bool
    name: str
    size: int = 0
    children: list[Node] = field(default_factory=list)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Node):
            raise TypeError
        return self.name == __o.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return self.name


def calculate_size(node: Node, limit: int):
    if not node.is_dir:
        return

    size = 0
    for child in node.children:
        if child.is_dir and child.size == 0:
            calculate_size(child, limit)

        if (child.is_dir and child.size < 0) or size + child.size > limit:
            node.size = -1
            return

        size += child.size

    node.size = size


def calculate_size_unlimited(node: Node):
    if not node.is_dir:
        return

    size = 0
    for child in node.children:
        if child.is_dir:
            calculate_size_unlimited(child)
        size += child.size

    node.size = size


def get_nodes(s: str) -> dict[Node, Node]:
    lines = iter(s.splitlines())

    # not sure if a starting dir is specified in the problem description,
    # either way doesn't hurt as "cd /" is the first cmd in the input
    pwd = "/"
    fs = {}
    while True:
        try:
            line = next(lines).split()

            if line[0] == "$":
                cmd = line[1]

                if cmd == "cd":
                    dest = line[2]

                    if dest == "/":
                        pwd = "/"
                    elif dest == "..":
                        pwd = os.path.dirname(pwd) or "/"
                    else:
                        pwd = os.path.join(pwd, dest)

                    pwd_node = Node(is_dir=True, name=pwd)
                    if pwd_node not in fs:
                        fs[pwd_node] = pwd_node
                    else:
                        pwd_node = fs[pwd_node]

                continue

            size_or_dir, name = line

            absname = os.path.join(pwd, name)
            new_node = (
                Node(is_dir=True, name=absname)
                if size_or_dir == "dir"
                else Node(is_dir=False, name=absname, size=int(size_or_dir))
            )

            if new_node not in fs:
                fs[new_node] = new_node
                fs[pwd_node].children.append(new_node)

        except StopIteration:
            break

    return fs


def part_one(s: str) -> int:
    fs = get_nodes(s)

    for node in fs:
        calculate_size(node, 100_000)

    total = 0
    for node in fs:
        if node.is_dir and node.size > 0 and node.size < 100_000:
            total += node.size

    return total


def part_two(s: str) -> int:
    fs = get_nodes(s)

    for node in fs:
        calculate_size_unlimited(node)

    total = 70_000_000
    target = 30_000_000

    used = fs[Node(is_dir=True, name="/")].size

    to_free_up = target - (total - used)  # I'm creating an object to index the dict LOL
    if to_free_up <= 0:
        return 0

    res = used
    diff = used - to_free_up
    for node in fs:
        if node.is_dir and node.size >= to_free_up:
            curr_diff = node.size - to_free_up
            if curr_diff < diff:
                diff, res = curr_diff, node.size

    return res


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
