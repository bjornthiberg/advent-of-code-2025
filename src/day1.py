import os
from typing import List

DIRECTORY = os.path.dirname(__file__)


def get_lines_from_file(file_path: str) -> List[str]:
    with open(os.path.join(DIRECTORY, file_path), "r") as f:
        return f.readlines()


def get_diff_from_line(line: str) -> tuple[int, int]:
    sign = -1 if line[0] == "L" else 1
    return (sign, int(line[1:]))


def part1(file_path: str) -> int:
    lines = get_lines_from_file(file_path)

    dial: int = 50
    has_been_zero: int = 0

    for line in lines:
        direction, steps = get_diff_from_line(line)
        dial = (dial + direction * steps) % 100
        if dial == 0:
            has_been_zero += 1

    return has_been_zero


def part2(file_path):
    dial = 50
    count = 0

    for d, n in map(get_diff_from_line, get_lines_from_file(file_path)):
        for _ in range(n):
            dial = (dial + d) % 100
            count += dial == 0

    return count


if __name__ == "__main__":
    print(f"Part 1: {part1('./input/day1.txt')}")
    print(f"Part 2: {part2('./input/day1.txt')}")
