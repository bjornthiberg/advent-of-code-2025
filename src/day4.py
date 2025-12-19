import os
from itertools import product
from typing import List, Tuple

DIRECTORY = os.path.dirname(__file__)


def get_lines_from_file(file_path) -> list[str]:
    with open(os.path.join(DIRECTORY, file_path), "r") as f:
        return f.read().splitlines()


def valid_neighbours(x: int, y: int, x_max: int, y_max: int) -> List[Tuple[int, int]]:
    return [
        (nx, ny)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if not (dx == 0 and dy == 0)
        if 0 <= (nx := x + dx) <= x_max and 0 <= (ny := y + dy) <= y_max
    ]


def part1(file_path):
    rows = get_lines_from_file(file_path)
    y_max, x_max = len(rows) - 1, len(rows[0]) - 1
    return sum(
        1
        for y, x in product(range(len(rows)), range(len(rows[0])))
        if rows[y][x] == "@"
        and sum(
            1 for nx, ny in valid_neighbours(x, y, x_max, y_max) if rows[ny][nx] == "@"
        )
        < 4
    )


def part2(file_path):
    rows = get_lines_from_file(file_path)
    y_max = len(rows) - 1
    x_max = len(rows[0]) - 1

    rolls_removed = 0

    while True:
        marked_for_removal = [
            (x, y)
            for y, row in enumerate(rows)
            for x, cell in enumerate(row)
            if cell == "@"
            and sum(
                1
                for nx, ny in valid_neighbours(x, y, x_max, y_max)
                if rows[ny][nx] == "@"
            )
            < 4
        ]

        if not marked_for_removal:
            break

        rows = [
            "".join(
                "." if (x, y) in marked_for_removal else cell
                for x, cell in enumerate(row)
            )
            for y, row in enumerate(rows)
        ]

        rolls_removed += len(marked_for_removal)

    return rolls_removed


if __name__ == "__main__":
    print(f"Part 1: {part1('./input/day4.txt')}")
    print(f"Part 2: {part2('./input/day4.txt')}")
